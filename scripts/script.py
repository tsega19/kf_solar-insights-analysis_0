import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import zscore
from windrose import WindroseAxes


def load_dataset(file_path):
    data = pd.read_csv(file_path)
    return data


def display_dataset_info(data):
    print("Dataset Overview")
    print(data.info())
    print("\nFirst 5 rows of the dataset")
    print(data.head())


def check_missing_values(data):
    print("\nMissing Values")
    print(data.isnull().sum())


def check_negative_values(data, columns):
    print("\nNegative Values Check")
    for column in columns:
        print(f"{column}: {(data[column] < 0).sum()} negative values")


def display_summary_statistics(data):
    print("\nSummary Statistics")
    print(data.describe())


def process_timestamps(data, column='Timestamp'):
    data[column] = pd.to_datetime(data[column], errors='coerce')
    data.set_index(column, inplace=True)
    print("\nNumber of NaT values in index:", data.index.isnull().sum())
    return data


def plot_solar_radiation(data):
    plt.figure(figsize=(10, 6))
    data[['GHI', 'DNI', 'DHI']].plot()
    plt.title("Solar Radiation (GHI, DNI, DHI) Over Time")
    plt.ylabel("Irradiance (W/m²)")
    plt.xlabel("Time")
    plt.legend()
    plt.show()


def analyze_monthly_averages(data):
    data['Month'] = data.index.month
    monthly_avg = data.groupby('Month')[['GHI', 'DNI', 'DHI']].mean()
    monthly_avg.plot(kind='bar', figsize=(10, 6))
    plt.title("Monthly Averages of Solar Radiation")
    plt.ylabel("Irradiance (W/m²)")
    plt.xlabel("Month")
    plt.xticks(ticks=range(12), labels=["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])
    plt.show()


def plot_correlation_matrix(data):
    correlation_matrix = data.corr()
    plt.figure(figsize=(12, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
    plt.title("Correlation Matrix")
    plt.show()


def plot_histograms(data, columns):
    data[columns].hist(bins=20, figsize=(12, 8), edgecolor='black')
    plt.suptitle("Histograms of Key Variables", y=0.95)
    plt.show()


def scatter_plot_ghi_vs_tamb(data):
    plt.figure(figsize=(8, 6))
    sns.scatterplot(x='Tamb', y='GHI', data=data, alpha=0.7)
    plt.title("GHI vs. Ambient Temperature")
    plt.xlabel("Ambient Temperature (°C)")
    plt.ylabel("GHI (W/m²)")
    plt.show()


def detect_outliers(data):
    data_zscore = data.select_dtypes(include=np.number)
    z_scores = np.abs(zscore(data_zscore))
    outliers = (z_scores > 3).sum(axis=0)
    print("\nNumber of Outliers per Column (Z-Score > 3):")
    print(outliers)


def plot_bubble_chart(data):
    plt.figure(figsize=(10, 6))
    plt.scatter(data['GHI'], data['Tamb'], s=data['RH'], alpha=0.6)
    plt.title("GHI vs. Tamb vs. RH (Bubble Size: RH)")
    plt.xlabel("GHI (W/m²)")
    plt.ylabel("Ambient Temperature (°C)")
    plt.colorbar(label="Relative Humidity (%)")
    plt.show()


def plot_wind_rose(data):
    try:
        ax = WindroseAxes.from_ax()
        ax.bar(data['WD'], data['WS'], normed=True, opening=0.8, edgecolor='black')
        ax.set_legend()
        plt.title("Wind Speed and Direction")
        plt.show()
    except ImportError:
        print("Windrose library not installed. Install it using: pip install windrose")


def analyze_cleaning_impact(data):
    plt.figure(figsize=(12, 6))
    sns.boxplot(x='Cleaning', y='ModA', data=data)
    plt.title("Impact of Cleaning on Module A")
    plt.xlabel("Cleaning Event (1 = Yes, 0 = No)")
    plt.ylabel("ModA Reading (W/m²)")
    plt.show()

    plt.figure(figsize=(12, 6))
    sns.boxplot(x='Cleaning', y='ModB', data=data)
    plt.title("Impact of Cleaning on Module B")
    plt.xlabel("Cleaning Event (1 = Yes, 0 = No)")
    plt.ylabel("ModB Reading (W/m²)")
    plt.show()
