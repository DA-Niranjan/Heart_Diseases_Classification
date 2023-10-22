# Import the Modules

import pandas as pd, numpy as np
from sklearn import preprocessing
from src.constant import *

# apply same pre-processing and feature engineering techniques as applied during the training process
def encode_features(df, features):
       encoded_df = pd.DataFrame(columns=ONE_HOT_ENCODED)
       df = pd.get_dummies(data=df, columns=features, dtype=int)
       
       # Implement these steps to prevent dimension mismatch during inference
       for f in encoded_df.columns:
              if f in df.columns:
                     encoded_df[f]=df[f]
        
       encoded_df.fillna(0,inplace=True)
       
       return encoded_df

def normalize_data(df,features):
       scaler = preprocessing.MinMaxScaler()
       df[features] = scaler.fit_transform(df[features])
       return df

def apply_pre_processing(data,**kwargs):
       encoded = encode_features(data,kwargs["features_encoding"])
       processed_data = normalize_data(encoded, kwargs["features_scaling"])
       return processed_data  