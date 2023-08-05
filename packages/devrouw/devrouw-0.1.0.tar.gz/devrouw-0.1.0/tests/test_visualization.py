import pandas as pd
import pytest
from mylibrary.visualization import *


@pytest.fixture
def sample_data():
    return pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])


def test_create_histogram(sample_data):
    create_histogram(sample_data, 'test_histogram.png')
    # TODO: Add assertion to check that the file was created


def test_create_boxplot(sample_data):
    create_boxplot(sample_data, 'test_boxplot.png')
    # TODO: Add assertion to check that the file was created


def test_create_scatterplot(sample_data):
    data1 = pd.Series([1, 2, 3, 4, 5])
    data2 = pd.Series([2, 4, 6, 8, 10])
    create_scatterplot(data1, data2, 'test_scatterplot.png')
    # TODO: Add assertion to check that the file was created


def test_create_lineplot(sample_data):
    create_lineplot(sample_data, 'test_lineplot.png')
    # TODO: Add assertion to check that the file was created


def test_create_heatmap(sample_data):
    data1 = pd.Series([1, 2, 3, 4, 5])
    data2 = pd.Series([2, 4, 6, 8, 10])
    create_heatmap(data1, data2, 'test_heatmap.png')
    # TODO: Add assertion to check that the file was created
