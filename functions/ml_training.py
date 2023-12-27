#from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.pipeline import Pipeline
from sklearn.model_selection import cross_validate
import statistics as stats

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