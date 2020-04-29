
class Config:

    # Data set path
    DATA_PATH = 'Datasets/'
    # Emotional label
    CLASS_LABELS = ("Angry", "Happy", "Sad", "Surprise")

    # literation
    epochs = 20

    FEATURE_NUM = {
        'IS09_emotion': 384,
        'IS10_paraling': 1582,
        'IS11_speaker_state': 4368,
        'IS12_speaker_trait': 6125,
        'IS13_ComParE': 6373,
        'ComParE_2016': 6373
    }

    # Feature storage path
    FEATURE_PATH = 'Features/6-category/'
    # Training feature storage path
    TRAIN_FEATURE_PATH_LIBROSA = FEATURE_PATH + 'train_librosa_casia.p'
    # Predictive feature storage path
    PREDICT_FEATURE_PATH_LIBROSA = FEATURE_PATH + 'test_librosa_casia.p'

    MODEL_PATH = 'Models/'