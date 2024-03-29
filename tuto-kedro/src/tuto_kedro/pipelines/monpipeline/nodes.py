"""
This is a boilerplate pipeline 'monpipeline'
generated using Kedro 0.19.3
"""
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

def load_and_normalize(digits):
    x = digits[0]
    y = digits[1]
    x = x / 255
    return x, y 

def split_data(x, y, parameters):
    X_train, X_test, y_train, y_test = train_test_split(x, y, test_size = parameters['test_size'], random_state = parameters['random_state']) 
    return X_train, X_test, y_train, y_test

def train_model(X_train, y_train, parameters):
    model = LogisticRegression(max_iter=parameters['max_iter'])
    model.fit(X_train, y_train)
    return model

def eval_model(model, X_test, y_test):
    accuracy = model.score(X_test, y_test)
    return {'accuracy': accuracy}