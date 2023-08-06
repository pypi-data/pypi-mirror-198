import pandas as pd
import numpy as np

def test_set_select(df, seed = 42):
  train, validate, test = np.split(df.sample(frac=1, random_state= seed ),[int(.8*len(df)), int(.9*len(df))])

  df_yes = train.loc[train['label'] == 'yes'] 
  df_no = train.loc[train['label'] == 'no']

  if len(df_yes) > len(df_no):
    rem_ex = len(df_yes) - len(df_no)
    get_more_ex = df_yes.sample(rem_ex)
    train = pd.concat([train, get_more_ex, get_more_ex]).drop_duplicates(keep=False)
    test = pd.concat([test, get_more_ex], axis = 0)
  
  if len(df_no) > len(df_yes):
    rem_ex = len(df_no) - len(df_yes)
    get_more_ex = df_no.sample(rem_ex)
    train = pd.concat([train, get_more_ex, get_more_ex]).drop_duplicates(keep=False)
    test = pd.concat([test, get_more_ex], axis = 0)

  return train.reset_index(drop = True), validate.reset_index(drop = True), test.reset_index(drop = True)

def select_num_examples(train_df, num_examples):
  print("num_examples" , num_examples, "\n")

  df_yes = train_df.loc[train_df['label'] == 'yes'] 
  df_no = train_df.loc[train_df['label'] == 'no'] 
  print("num_yes : " ,len(df_yes)," num_no : ", len(df_no), "\n")

  if num_examples == 'ALL':
    train_df = train_df

  # elif len(df_yes) != len(df_no):
  #   train_df = train_df

  else:
    train_df = pd.concat([df_yes.sample(int(num_examples/2)),df_no.sample(int(num_examples/2))], axis = 0)
  
  return train_df.reset_index(drop = True)
