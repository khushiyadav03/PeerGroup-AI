import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer

def preprocess_data(df, numerical_features, categorical_features):
    """
    Preprocesses the student data: scales numerical features and encodes categorical ones.
    Returns the processed feature matrix and the feature names.
    """
    transformers = []
    
    if numerical_features:
        transformers.append(('num', StandardScaler(), numerical_features))
    
    if categorical_features:
        transformers.append(('cat', OneHotEncoder(), categorical_features))
    
    preprocessor = ColumnTransformer(transformers=transformers)
    
    X = preprocessor.fit_transform(df)
    
    # Get feature names after encoding
    feature_names = []
    try:
        feature_names = preprocessor.get_feature_names_out()
    except AttributeError:
        # Fallback for older sklearn versions
        if categorical_features and 'cat' in preprocessor.named_transformers_:
            cat_encoder = preprocessor.named_transformers_['cat']
            cat_names = cat_encoder.get_feature_names_out(categorical_features)
            feature_names = numerical_features + list(cat_names)
        else:
            feature_names = numerical_features
            
    return X, feature_names


