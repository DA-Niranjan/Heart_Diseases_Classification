ORIGINAL_FEATURES = ['age', 'sex', 'chest_pain_type', 'resting_bp', 'cholestoral',
       'fasting_blood_sugar', 'restecg', 'max_hr', 'exang', 'oldpeak', 'slope',
       'num_major_vessels', 'thal']

ONE_HOT_ENCODED = ['age', 'sex', 'resting_bp', 'cholestoral', 'fasting_blood_sugar',
              'max_hr', 'exang', 'oldpeak', 'num_major_vessels', 'thal_1',
              'thal_2', 'thal_3', 'slope_1', 'slope_2', 'chest_pain_type_1',
              'chest_pain_type_2', 'chest_pain_type_3', 'restecg_1', 'restecg_2']

FEATURES_ENCODING = ['thal', 'slope', 'chest_pain_type', 'restecg']

FEATURES_SCALING = ['age', 'resting_bp', 'cholestoral', 'max_hr', 'oldpeak', 'num_major_vessels']

MODEL_NAME = r"models/Niranjan_Model_01_adaboost.joblib"