from src.preprocess import preprocess
import pandas as pd

def test_preprocess():
    df = preprocess("data/sample.csv")
    assert not df.isnull().values.any()
    assert len(df) > 0
