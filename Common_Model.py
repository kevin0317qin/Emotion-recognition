import sys

from sklearn.metrics import accuracy_score


class Common_Model(object):

    def __init__(self, save_path: str = '', name: str = 'Not Specified'):
        self.model = None
        self.trained = False

    '''
    input:
        x_train: Training set sample
        y_train: Training set label
        x_val: Test set sample
        y_val: Test set label

    '''
    def train(self, x_train, y_train, x_val, y_val):
        raise NotImplementedError()

    '''

    input:
        samples: Audio features that need to be identified

    output:
        list: List of recognition results (labels)
    '''
    def predict(self, samples):
        raise NotImplementedError()
        

    def predict_proba(self, samples):
        if not self.trained:
            sys.stderr.write("No Model.")
            sys.exit(-1)
        return self.model.predict_proba(samples)

    '''
    save_model(): save model
    '''
    def save_model(self, model_name: str):
        raise NotImplementedError()


    def evaluate(self, x_test, y_test):

        predictions = self.predict(x_test)
        print(y_test)
        print(predictions)
        print('Accuracy:%.3f\n' % accuracy_score(y_pred = predictions, y_true = y_test))
 


