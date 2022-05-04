import src.score as score

args = score.parse_args()
path = score.get_path()


def test_parse_args():

    assert args.datapath == "data/processed"
    assert args.modelpath == "artifacts"


def test_load_models():
    models = score.load_models(path+args.modelpath)
    assert len(models) == 4


test_parse_args()


test_load_models()