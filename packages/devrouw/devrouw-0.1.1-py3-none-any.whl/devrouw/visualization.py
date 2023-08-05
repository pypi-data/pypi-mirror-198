import matplotlib.pyplot as plt
import pandas as pd

class visualization:
    def plot_histogram(data: pd.Series, title: str, x_label: str, y_label: str) -> None:
        """Plots a histogram of the given data using Matplotlib."""
        plt.hist(data)
        plt.title(title)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.show()

    def plot_line_chart(x: pd.Series, y: pd.Series, title: str, x_label: str, y_label: str) -> None:
        """Plots a line chart of the given data using Matplotlib."""
        plt.plot(x, y)
        plt.title(title)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.show()

    def plot_bar_chart(data: pd.Series, title: str, x_label: str, y_label: str) -> None:
        """Plots a bar chart of the given data using Matplotlib."""
        plt.bar(data.index, data.values)
        plt.title(title)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.show()

    def plot_scatter_chart(x: pd.Series, y: pd.Series, title: str, x_label: str, y_label: str) -> None:
        """Plots a scatter chart of the given data using Matplotlib."""
        plt.scatter(x, y)
        plt.title(title)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.show()

    def plot_heatmap(data: pd.DataFrame, title: str, x_label: str, y_label: str) -> None:
        """Plots a heatmap of the given data using Matplotlib."""
        plt.imshow(data, cmap='viridis')
        plt.title(title)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.colorbar()
        plt.show()
