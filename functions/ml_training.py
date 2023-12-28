#from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.pipeline import Pipeline
from sklearn.model_selection import cross_validate
import statistics as stats
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV
from sklearn.metrics import make_scorer, f1_score

def train_classifiers(classifiers, x, y, cv, scoring, scaler=None):
    results = {}

    for classifier in classifiers:
        if scaler is not None:
            # Create a pipeline with the specified scaler and the current classifier
            pipe = Pipeline([('scaler', scaler), ('classifier', classifier)])
        else:
            # Create a pipeline with only the classifier (no scaling)
            pipe = Pipeline([('classifier', classifier)])


        # Use cross_validate to obtain scores
        scores = cross_validate(pipe, x, y, cv=cv, scoring=scoring, n_jobs=-1, return_train_score=False)

        results[classifier.__class__.__name__] = {
            'Accuracy': stats.fmean(scores['test_Accuracy']),
            'F1-score': stats.fmean(scores['test_F1-score']),
            'G-Mean score': stats.fmean(scores['test_G-Mean score']),
            'Fit time': sum(scores['fit_time'])
        }

    return results


def train_classifiers_tuned(classifiers, x, y, cv, search_cv, scoring, param_grid, scaler=None):
    results = {}

    for classifier in classifiers:
        if scaler is not None:
            # Create a pipeline with the specified scaler and the current classifier
            pipe = Pipeline([('scaler', scaler), ('classifier', classifier)])
        else:
            # Create a pipeline with only the classifier (no scaling)
            pipe = Pipeline([('classifier', classifier)])

        # GridSearchCV with refit False
        grid_search = GridSearchCV(pipe, param_grid=param_grid, scoring=scoring,
                                   cv=search_cv, refit=False, n_jobs=-1)

        # Perform grid search
        grid_search.fit(x, y)

        # Get the best estimator
        best_estimator = grid_search.best_estimator_

        # Manually refit the best estimator on the entire training data on the F1 score
        best_estimator.fit(x, y, scoring='f1_score')

        # Calculate the F1 score of the manually refit model
        scores = cross_validate(best_estimator, x, y, cv=cv, scoring=scoring, n_jobs=-1, return_train_score=False)
        manual_f1 = stats.fmean(scores['test_F1-score'])

        results[classifier.__class__.__name__] = {
            'Accuracy': stats.fmean(scores['test_Accuracy']),
            'F1-score': manual_f1,
            'G-Mean score': stats.fmean(scores['test_G-Mean score']),
            'Fit time': sum(scores['fit_time'])
        }

    return results


# def train_classifiers_tuned(classifiers, x, y, cv, search_cv, scoring, param_grid, scaler=None):
#     results = {}

#     for classifier in classifiers:
#         if scaler is not None:
#             # Create a pipeline with the specified scaler and the current classifier
#             pipe = Pipeline([('scaler', scaler), ('classifier', classifier)])
#         else:
#             # Create a pipeline with only the classifier (no scaling)
#             pipe = Pipeline([('classifier', classifier)])

#         # GridSearchCV with refit False
#         grid_search = GridSearchCV(pipe, param_grid=param_grid, scoring=scoring,
#                                    cv=search_cv, refit=False, n_jobs=-1)

#         # Perform grid search
#         grid_search.fit(x, y)

#         # Get the best estimator
#         best_estimator = grid_search.best_estimator_

#         # Manually refit the best estimator on the entire training data
#         best_estimator.fit(x, y)

#         # Get the best parameters
#         best_params = grid_search.best_params_

#         # Use cross_validate to obtain scores
#         scores = cross_validate(best_estimator, x, y, cv=cv, scoring=scoring, n_jobs=-1, return_train_score=False)

        # results[classifier.__class__.__name__] = {
        #     'Accuracy': stats.fmean(scores['test_Accuracy']),
        #     'F1-score': stats.fmean(scores['test_F1-score']),
        #     'G-Mean score': stats.fmean(scores['test_G-Mean score']),
        #     'Fit time': sum(scores['fit_time']),
        #     'Best Parameters': best_params
        # }

#     return results
