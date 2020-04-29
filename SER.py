import numpy as np
from keras.utils import np_utils
import os
import pyttsx3
import random

from DNN_Model import LSTM_Model

from Utils import load_model, Radar, playAudio

import Librosa_Feature as lf
from Config import Config


# def Train(save_model_name: str, if_load: bool = True):
def Train(save_model_name, if_load):

    if (if_load == True):
        x_train, x_test, y_train, y_test = lf.load_feature(feature_path=Config.TRAIN_FEATURE_PATH_LIBROSA, train=True)
    else:
        x_train, x_test, y_train, y_test = lf.get_data(Config.DATA_PATH, Config.TRAIN_FEATURE_PATH_LIBROSA, train=True)

    y_train = np_utils.to_categorical(y_train)
    y_val = np_utils.to_categorical(y_test)

    model = LSTM_Model(input_shape=x_train.shape[1], num_classes=len(Config.CLASS_LABELS))

    x_train = np.reshape(x_train, (x_train.shape[0], 1, x_train.shape[1]))
    x_test = np.reshape(x_test, (x_test.shape[0], 1, x_test.shape[1]))

    print('-------------------------------- Start --------------------------------')

    model.train(x_train, y_train, x_test, y_val, n_epochs = Config.epochs)

    model.evaluate(x_test, y_test)
    model.save_model(save_model_name)
    print('---------------------------------- End ----------------------------------')

    return model


def Predict(model, file_path):
    
    file_path = os.path.dirname(os.path.abspath(__file__)) + '/' + file_path
    playAudio(file_path)

    test_feature = lf.get_data(file_path, Config.PREDICT_FEATURE_PATH_LIBROSA, train = False)

    test_feature = np.reshape(test_feature, (test_feature.shape[0], 1, test_feature.shape[1]))
    
    result = model.predict(test_feature)
    result = np.argmax(result)

    result_prob = model.predict_proba(test_feature)[0]
    print('Recogntion: ', Config.CLASS_LABELS[int(result)])
    print('Probability: ', result_prob)
    Response(Config.CLASS_LABELS[int(result)])
    Radar(result_prob)
    return Config.CLASS_LABELS[int(result)]

def Response(emotion):
    good = ["Optimism is the faith that leads to achievement. Nothing can be done without hope and confidence",
            "Be brave to stand for what you believe in even if you stand alone.",
            "The key to life is accepting challenges. Once someone stops doing this, he’s dead.",
            "Success is not final, failure is not fatal: it is the courage to continue that counts.",
            "Failures are made only by those who fail to dare, not by those who dare to fail.",
            "You can do anything as long as you have the passion, the drive, the focus, and the support.",
            "We are what we repeatedly do. Excellence, therefore, is not an act, but a habit.",
            "Only those who have learned the power of sincere and selfless contribution experience life's deepest joy: true fulfillment.",
            "Set your goals high, and don't stop 'til you get there."]
    if emotion == "Angry" or emotion == "Sad":
        word = random.sample(good, 1)
        print(word)
    # else:
    #     # word = ran
