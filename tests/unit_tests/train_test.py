import os

import src.train as train

args = train.parse_args()


def test_parse_args():

    assert args.inputpath == "data/processed/"
    assert args.outputpath == "artifacts"


path = train.get_path()


def test_load_data():

    X, y = train.load_data(args.inputpath)
    assert len(X) == len(y)
    assert "median_house_value" not in X.columns
    assert not X.isna().sum().sum()
    assert len(y.shape) == 1


def test_savemodel():
    model_names = ['lin_model', 'tree_model', 'forest_model', 'grid_search_model']
    for i in model_names:
        assert os.path.exists(path+args.outputpath+'/'+i+'/model.pkl')


test_parse_args()


test_load_data()


test_savemodel()
