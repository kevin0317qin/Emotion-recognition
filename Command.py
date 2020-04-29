import argparse

from SER import Train, Predict
from Utils import load_model

def cmd1():

    paser = argparse.ArgumentParser(description = 'Speech Emotion Recognition')
    # python3 cmd.py -o p - a 'Test/fear.wav'

    # paser.add_argument(
    #     '-o',
    #     '--option',
    #     type = str,
    #     dest = 'option',
    #     help = "Use 'p' to predict directly or use 't' to train a model.")
    #
    # paser.add_argument(
    #     '-a',
    #     '--audio',
    #     type = str,
    #     dest = 'audio',
    #     help = "The path of audio which you want to predict.")
    #

    # args = paser.parse_args()

    # option = args.option.lower() # p / t
    option = 'p';
    model_name = "lstm"
    model_type = "lstm"
    feature = "l"
    load = True
    # audio = args.audio if args.audio else 'default.wav'
    audio = "output.wav"
    # predict
    if option == 'p':
        model = load_model(load_model_name = model_name, model_name = model_type)
        emotion = Predict(model, file_path = audio)
    return emotion
    # train
    # elif option == 't':
    #     Train(model_name = model_type, save_model_name = model_name, if_load = load, feature_method = feature)

    # else:
    #     print("Wrong option. 'p' for predicting, 't' for training")
    #     return


# if __name__ == '__main__':
#     cmd1()