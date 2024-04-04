import pandas as pd

def bad_feats_rmv(feats:list,bad_feats:list):
    '''This function remove bad features'''
    for col in bad_feats:
        feats.remove(col)        
    return feats


def feat_eng(data:pd.DataFrame, feats:list):
    onehot_encoded = pd.get_dummies(data["lt"]).astype(int)
    data = pd.concat([data, onehot_encoded], axis =1)
    data.drop("lt",axis=1, inplace =True)
    feats = feats + ["A", "N"]
    feats.remove("lt")
    return data, feats

def missing_indication_imputation(data,feats):
    '''This function imputes the missing values by creating new binary feat for them and impute missing values by 0'''
    data_training = data[feats]
    missing_exo_feats = feats[2:-3]
    data_training["is_exo_missed"] = data_training[missing_exo_feats].\
        isna().iloc[:,0].values.astype(int)
    data_training[missing_exo_feats] = data_training[missing_exo_feats].fillna(0)
    data_training["is_akt_vkp_missed"] = data_training["akt_vkp"].\
        isna().values.astype(int)
    data_training["akt_vkp"] = data_training["akt_vkp"].fillna(0)
    return data_training