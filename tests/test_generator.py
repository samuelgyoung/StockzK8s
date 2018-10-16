import unittest
from stockzBin import getStock

#https://medium.com/bettercode/how-to-build-a-modern-ci-cd-pipeline-5faa01891a5b

def test_sample_stock():
    assert len(getStock.data('C')) >= 5
