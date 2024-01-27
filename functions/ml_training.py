#from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.pipeline import Pipeline
from sklearn.model_selection import cross_validate
import statistics as stats
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV
from sklearn.metrics import make_scorer, f1_score
import seaborn as sns # data visualization library
import matplotlib.pyplot as plt

def train_classifiers(classifiers, x, y, cv, scoring, scaler=None):
  """
  Trains multiple classifiers.
  
  Makes a pipeline (depending on the normalization method) to train all classifiers given
  and then stores the results taken from cross_validate method in a dictionary.

  Parameters:
    list of classifiers,
    input variables (x),
    output variables (y),
    a dictionary with scores to calculate,
    the scaler which is the normalization method to use (default is None)

  Returns:
    A Dictionary containing the results for each classifier.
  """
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

      # Input the scores in a dictionary
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
        
        # GridSearchCV with refit on F1-score
        grid_search = GridSearchCV(pipe, param_grid=param_grid, scoring=make_scorer(f1_score, average = 'weighted'),
                                   cv=search_cv, refit=make_scorer(f1_score, average = 'weighted'), n_jobs=-1)

        # # Get the best estimator
        # best_estimator = grid_search.best_estimator_

        # Calculate the F1 score of the manually refit model
        scores = cross_validate(grid_search, x, y, cv=cv, scoring=scoring, n_jobs=-1, return_train_score=False)

        results[classifier.__class__.__name__] = {
            'Accuracy': stats.fmean(scores['test_Accuracy']),
            'F1-score': stats.fmean(scores['test_F1-score']),
            'G-Mean score': stats.fmean(scores['test_G-Mean score']),
            'Fit time': sum(scores['fit_time'])
        }

    return results


def plot_metrics(df):
    # set the plot style
    sns.set(style="whitegrid", palette="muted", font_scale=1)

    # Plot Accuracy
    plt.figure(figsize=(20, 4))
    acc = sns.barplot(data=df, x='Classifier', y='Accuracy', hue='Normalization method')
    acc.legend(loc='upper center', bbox_to_anchor=(0.5, 1.2), ncol=3)
    acc.set_ylim(0, 1)
    for container in acc.containers:
        acc.bar_label(container)
    plt.show()

    # Plot F1-score
    plt.figure(figsize=(20, 4))
    f1 = sns.barplot(data=df, x='Classifier', y='F1-score', hue='Normalization method')
    f1.legend(loc='upper center', bbox_to_anchor=(0.5, 1.2), ncol=3)
    f1.set_ylim(0, 1)
    for container in f1.containers:
        f1.bar_label(container)
    plt.show()

    # Plot G-Mean score
    plt.figure(figsize=(20, 4))
    gmean = sns.barplot(data=df, x='Classifier', y='G-Mean score', hue='Normalization method')
    gmean.legend(loc='upper center', bbox_to_anchor=(0.5, 1.2), ncol=3)
    gmean.set_ylim(0, 1)
    for container in gmean.containers:
        gmean.bar_label(container)
    plt.show()

    # Plot Fit time
    plt.figure(figsize=(20, 4))
    fit_time = sns.barplot(data=df, x='Classifier', y='Fit time', hue='Normalization method')
    fit_time.legend(loc='upper center', bbox_to_anchor=(0.5, 1.2), ncol=3)
    fit_time.set_ylim(0, max(df['Fit time']) + 1)
    for container in fit_time.containers:
        fit_time.bar_label(container)
    plt.show()

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
