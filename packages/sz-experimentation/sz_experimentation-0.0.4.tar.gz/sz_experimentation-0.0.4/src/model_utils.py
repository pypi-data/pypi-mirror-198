from pathlib import Path
import json

def train_model(df_train,df_eval, config, format_df_for_pet_pattern,dataframe_to_jsonl):
    train_pet_df = format_df_for_pet_pattern(df_train, ['input_description', 'genereted_conditions'], 'label')
    val_pet_df = format_df_for_pet_pattern(df_eval, ['input_description', 'genereted_conditions'], 'label')
    
    Path("data/szinternal").mkdir(parents=True, exist_ok=True)
    dataframe_to_jsonl(train_pet_df, 'data/szinternal/train.jsonl')
    dataframe_to_jsonl(val_pet_df, 'data/szinternal/val.jsonl')
    return config


def get_the_model(output_path,Config,load_model):

  model_path = output_path + "/best_model.pt"
  config_path = output_path + "/config.json"

  config = json.load(open(config_path))
  config =  Config(kwargs=config)

  model =  load_model(config,model_path)
  return model