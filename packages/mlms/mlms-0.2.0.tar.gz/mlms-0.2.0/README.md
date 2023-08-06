# ML_ModelSelection

This package aims to facilitate model selection in Machine Learning. It is a common issue that ML practitioners often struggle to decide on the most appropriate model prior to optimization, as tuning hyperparameters can be time-consuming and computationally demanding. To simplify the process, this package enables users to train several machine learning models using their default hyperparameters and compare their performance, helping them determine the most suitable model to selectexit()

)

# Usage

`pip install mlms`

Then instantiate and use it like this:

`from MLMS import ModelSelection as MS`

`performance, models = MS.Select_Classifier('accuracy', 10, X_train, X_test, y_train, y_test)`

For classifiers, the performance can set as `accuracy` , `f1_score` , `precision`, `recall`, `roc_auc` and so on. Available classifiers are below

* `('LGR', LogisticRegression(n_jobs=-1))`,
* `('AB', AdaBoostClassifier())`,
* `('CART', DecisionTreeClassifier())`,
* `('GBC', GradientBoostingClassifier())`,
* `('XGBC', XGBClassifier())`,
* `('RFC', RandomForestClassifier())`,
* `('ETC', ExtraTreeClassifier())`,
* `('KNN', KNeighborsClassifier(n_jobs=-1))`,
* `('NB', GaussianNB())`,
* `('SVC', SVC())`,
* `('MLP', MLPClassifier()),`
* `('SGDC', SGDClassifier(n_jobs=-1)),`
* `('GPC', GaussianProcessClassifier(n_jobs=-1)),`
* `('PAC', PassiveAggressiveClassifier(n_jobs=-1))`
