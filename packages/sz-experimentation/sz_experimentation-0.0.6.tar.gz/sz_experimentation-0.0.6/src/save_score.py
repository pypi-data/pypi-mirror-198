from model_utils import get_the_model

from sz_metrics import SZ_Calibration_Metric
import os
import torch
import pandas as pd

def get_performance_and_ue_score(df_test,output_path,Config,load_model,batch_data_from_dataframe):
  batches = batch_data_from_dataframe(df_test, desc_cols=['input_description', 'genereted_conditions'], batch_size=4)

  adapet_logits = []
  adapet_pred = []

  classifier_logits = []
  classifier_pred = []
  model = get_the_model(output_path,Config,load_model)

  with torch.no_grad():
    for batch in batches:

      pred_lbl, lbl_logits, cls_prob = model.predict(batch) # make it editable
      cls_pred = torch.argmax(cls_prob, dim=1)

      adapet_logits.extend(lbl_logits.cpu().numpy().tolist())
      adapet_pred.extend(pred_lbl.cpu().numpy().tolist())

      classifier_logits.extend(cls_prob.cpu().numpy().tolist())
      classifier_pred.extend(cls_pred.cpu().numpy().tolist())

  true_label = [1 if x == 'yes' else 0 for x in df_test["label"]]

  df_test['adapet_machine_label'] = ['yes' if x == 1 else "no" for x in adapet_pred]
  df_test["adapet_logits"] = adapet_logits

  df_test['calssifier_machine_label'] = ['yes' if x == 1 else "no" for x in classifier_pred]
  df_test["classifier_logits"] = classifier_logits

  

  adapet_pscore_dict = SZ_Calibration_Metric.get_performance_metrics(true_label,adapet_pred)
  classifier_pscore_dict = SZ_Calibration_Metric.get_performance_metrics(true_label,classifier_pred)

  adapet_ue_score_dict = SZ_Calibration_Metric.get_ue_metrics(true_label ,adapet_logits)
  classifier_ue_score_dict = SZ_Calibration_Metric.get_ue_metrics(true_label ,classifier_logits)

  return adapet_pscore_dict,classifier_pscore_dict,adapet_ue_score_dict,classifier_ue_score_dict, df_test


def save_preds(df_test,output_path,sg_name,num_examples,Config,load_model,batch_data_from_dataframe):

    adapet_pscore_dict,classifier_pscore_dict,adapet_ue_score_dict,classifier_ue_score_dict, df_test = get_performance_and_ue_score(df_test,output_path,Config,load_model,batch_data_from_dataframe)
    # link the label and probability into a dataframe
    adapet_score_dict = {**adapet_pscore_dict, **adapet_ue_score_dict}
    classifier_score_dict = {**classifier_pscore_dict, **classifier_ue_score_dict}

    adapet_pscore_dict_df = pd.DataFrame([adapet_score_dict])
    adapet_pscore_dict_df.insert(loc=0, column='Name', value= sg_name +"_"+ str(num_examples) + "_"+ 'adapet_score')

    classifier_pscore_dict_df = pd.DataFrame([classifier_score_dict])
    classifier_pscore_dict_df.insert(loc=0, column='Name', value= sg_name + "_" + str(num_examples) + "_" + 'classifier_score')

    df = pd.concat([ adapet_pscore_dict_df, classifier_pscore_dict_df], axis=0)

    save_preds_path = os.path.exists('/content/adapet/save_preds')
    if not save_preds_path:
      os.mkdir('/content/adapet/save_preds')
    df.to_csv("/content/adapet/save_preds/" + sg_name +"_"+ str(num_examples) + ".csv",index=False)

    save_test_data_path = os.path.exists('/content/adapet/save_test_data/')
    if not save_test_data_path:
      os.mkdir('/content/adapet/save_test_data/')
    df_test.to_csv("/content/adapet/save_test_data/" + sg_name +"_"+ str(num_examples) + ".csv",index=False)