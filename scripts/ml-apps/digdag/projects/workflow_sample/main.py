import cloudpickle
import pandas


def run_batch():
    with open('/app/models/sample/model.pkl', 'rb') as f:
        estimator_pkl = f.read()
        estimator = cloudpickle.loads(estimator_pkl)

    sample_datasets = pandas.DataFrame({
        'grade': [8.0, 7.0, 6.0],
        'bedrooms': [2.0, 3.0, 4.0],
        'floors': [1.0, 2.0, 3.0],
        'condition': [1.0, 2.0, 3.0],
        'yr_built': [1920.0, 1950.0, 1970.0],
        'yr_renovated': [1990, 2000.0, 2010.0]
    })
    result = estimator.predict(sample_datasets)
    print(result)
