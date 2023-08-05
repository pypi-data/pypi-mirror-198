import pandas as pd
import pytest
from devrouw.analysis import analysis


@pytest.fixture
def sample_data():
    return pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])


def test_describe_data(sample_data):
    result = describe_data(sample_data)
    assert result['count'] == 10
    assert result['mean'] == 5.5
    assert result['std'] == pytest.approx(2.8722813232690143, 1e-6)


def test_calculate_mean(sample_data):
    result = calculate_mean(sample_data)
    assert result == 5.5


def test_calculate_median(sample_data):
    result = calculate_median(sample_data)
    assert result == 5.5


def test_calculate_mode(sample_data):
    result = calculate_mode(sample_data)
    assert result == 1


def test_calculate_variance(sample_data):
    result = calculate_variance(sample_data)
    assert result == 9.166666666666666


def test_calculate_standard_deviation(sample_data):
    result = calculate_standard_deviation(sample_data)
    assert result == pytest.approx(3.0276503540974917, 1e-6)


def test_calculate_correlation(sample_data):
    data1 = pd.Series([1, 2, 3, 4, 5])
    data2 = pd.Series([2, 4, 6, 8, 10])
    result = calculate_correlation(data1, data2)
    assert result == pytest.approx(1.0, 1e-6)


def test_calculate_covariance(sample_data):
    data1 = pd.Series([1, 2, 3, 4, 5])
    data2 = pd.Series([2, 4, 6, 8, 10])
    result = calculate_covariance(data1, data2)
    assert result == 5.0


def test_calculate_percentile(sample_data):
    result = calculate_percentile(sample_data, 50)
    assert result == 5.5


def test_calculate_zscore(sample_data):
    result = calculate_zscore(sample_data)
    expected_result = pd.Series(
        [-1.5666989036012806, -1.2185435916898848, -0.8703882797784889, -0.5222329678670931,
         -0.17407765595569724, 0.17407765595569724, 0.5222329678670931, 0.8703882797784889,
         1.2185435916898848, 1.5666989036012806])
    assert result.equals(expected_result)
