import pandas as pd


def describe_data(data: pd.DataFrame):
    """Returns basic statistics for the given data."""
    return data.describe()


def calculate_mean(data: pd.Series):
    """Calculates the mean of the given data."""
    return data.mean()


def calculate_median(data: pd.Series):
    """Calculates the median of the given data."""
    return data.median()


def calculate_mode(data: pd.Series):
    """Calculates the mode of the given data."""
    return data.mode()[0]


def calculate_variance(data: pd.Series):
    """Calculates the variance of the given data."""
    return data.var()


def calculate_standard_deviation(data: pd.Series):
    """Calculates the standard deviation of the given data."""
    return data.std()


def calculate_correlation(data1: pd.Series, data2: pd.Series):
    """Calculates the correlation between two sets of data."""
    return data1.corr(data2)


def calculate_covariance(data1: pd.Series, data2: pd.Series):
    """Calculates the covariance between two sets of data."""
    return data1.cov(data2)


def calculate_percentile(data: pd.Series, percentile: float):
    """Calculates the specified percentile of the given data."""
    return data.quantile(percentile / 100)


def calculate_zscore(data: pd.Series):
    """Calculates the z-score of the given data."""
    return (data - data.mean()) / data.std()
