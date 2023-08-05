import pandas as pd

class analysis:
    def __init__(self, data: pd.Series):
        self.data = data
    
    def describe_data(self):
        """Returns basic statistics for the given data."""
        return self.data.describe()

    def calculate_mean(self):
        """Calculates the mean of the given data."""
        return self.data.mean()

    def calculate_median(self):
        """Calculates the median of the given data."""
        return self.data.median()

    def calculate_mode(self):
        """Calculates the mode of the given data."""
        return self.data.mode()[0]

    def calculate_variance(self):
        """Calculates the variance of the given data."""
        return self.data.var()

    def calculate_standard_deviation(self):
        """Calculates the standard deviation of the given data."""
        return self.data.std()

    def calculate_correlation(self, other_data: pd.Series):
        """Calculates the correlation between two sets of data."""
        return self.data.corr(other_data)

    def calculate_covariance(self, other_data: pd.Series):
        """Calculates the covariance between two sets of data."""
        return self.data.cov(other_data)

    def calculate_percentile(self, percentile: float):
        """Calculates the specified percentile of the given data."""
        return self.data.quantile(percentile / 100)

    def calculate_zscore(self):
        """Calculates the z-score of the given data."""
        return (self.data - self.data.mean()) / self.data.std()
