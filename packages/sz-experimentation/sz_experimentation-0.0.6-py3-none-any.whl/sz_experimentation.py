import torch
import os

from adapet_helper_function import *
from training_ex_selection import *
from save_score import *
from model_utils import *
from collections.abc import Mapping

def start_training(df, segment_name, seed, checkpoint_path,config_dict, function_dict : dict):

  
    
    if isinstance(function_dict, Mapping) == False:
        raise ("Dictionary of functions is missing")

    if 'config' in vars():
        del(config)
    if 'model' in vars():
        del(model)
    if 'tokenizer' in vars():
        del(tokenizer)
    if 'checkpoint' in vars():
        del(checkpoint)
    torch.cuda.empty_cache()

    train_data, val_df, test_df = test_set_select(df,seed) # seed value? Done---

    # segment_name_dir = segment_name[:-4] ## /content/adapet/datasets/Consumer_Electronics.csv >> /content/adapet/datasets/Consumer_Electronics ## remove .csv from end
    sg_name = segment_name[25:-4] ## removing '/content/adapet/datasets/' and '.csv' to get the dataset name
    
    num_example_li = [10, 20, 30, 40, 50, 60, 70, 100, 'ALL'] # 27 yes = 13 no = 14 ## test this function...? no idea..

    for num_examples in num_example_li: # break the loop num_e > len(df) Done

      if  num_examples > len(train_data):
        break

      df_train = select_num_examples(train_data, num_examples)  ## check test this function...? Done
      print("training data : ", len(df_train))
    
      config = config_dict
      os.environ['SZ_ROOT'] = ''    

      output_path = os.path.join(os.environ['SZ_ROOT'], "exp_out", sg_name + '_' + str(num_examples))
      if not os.path.exists(output_path):
          os.makedirs(output_path)
      
      print(output_path)

      config['exp_dir'] = output_path
      config = train_model(df_train, val_df ,config, function_dict["format_df_for_pet_pattern"],function_dict["dataframe_to_jsonl"])
      config = function_dict['Config'](kwargs=config, mkdir=False)
      train(config, output_path, checkpoint_path,
            function_dict["Batcher"],
            function_dict["adapet"],
            function_dict["device"],
            function_dict["update_dict_val_store"],
            function_dict["get_avg_dict_val_store"],
            function_dict["dev_eval"]
            )
      
      save_preds(test_df,output_path,sg_name,num_examples,function_dict["Config"],function_dict["load_model"],function_dict["batch_data_from_dataframe"])