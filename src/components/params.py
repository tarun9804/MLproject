import yaml

params = {
    "DecisionTree": {
        'criterion': ['squared_error', 'friedman_mse', 'absolute_error', 'poisson'],
        # 'splitter':['best','random'],
        # 'max_features':['sqrt','log2'],
    },
    "RandomForest": {
        # 'criterion':['squared_error', 'friedman_mse', 'absolute_error', 'poisson'],

        # 'max_features':['sqrt','log2',None],
        'n_estimators': [8, 16, 32, 64, 128, 256]
    },
    "Gradient Boosting": {
        # 'loss':['squared_error', 'huber', 'absolute_error', 'quantile'],
        'learning_rate': [.1, .01, .05, .001],
        'subsample': [0.6, 0.7, 0.75, 0.8, 0.85, 0.9],
        # 'criterion':['squared_error', 'friedman_mse'],
        # 'max_features':['auto','sqrt','log2'],
        'n_estimators': [8, 16, 32, 64, 128, 256]
    },
    "Linear Regression": {},
    "Lasso": {},
    "Ridge": {},
    "K-NearestNeighbour": {},
    "XGBoost": {
        'learning_rate': [.1, .01, .05, .001],
        'n_estimators': [8, 16, 32, 64, 128, 256]
    },
    "CatBoosting Regressor": {
        'depth': [6, 8, 10],
        'learning_rate': [0.01, 0.05, 0.1],
        'iterations': [30, 50, 100]
    },
    "AdaBoost": {
        'learning_rate': [.1, .01, 0.5, .001],
        # 'loss':['linear','square','exponential'],
        'n_estimators': [8, 16, 32, 64, 128, 256]
    }

}

with open("finetuneparam.yaml","w") as f:
    yaml.dump(params, f)
