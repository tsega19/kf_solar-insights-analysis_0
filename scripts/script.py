# import library
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import zscore

# import dataset
file_path = 'benin-malanville.csv'
data = pd.read_csv(file_path)

# Display dataset info
print("Dataset Overview")
print(data.info())
print("\nFirst 5 rows of the dataset")
print(data.head())

# check for missing value
print("\nMissing Values")
print(data.isnull().sum())

# Data Quality Check: Negative values in GHI, DNI, and DHI
print("\nNegative Values Check")
for column in ['GHI', 'DNI', 'DHI']:
    print(f"{column}: {(data[column] < 0).sum()} negative values")

# Summary Statistics
print("\nSummary Statistics")
print(data.describe())

# Convert Timestamp to datetime and set as index
# Try to infer the format automatically, handling errors by coercing them to NaT (Not a Time)
data['Timestamp'] = pd.to_datetime(data['Timestamp'], errors='coerce')

# If you know the actual format of your 'Timestamp' column, replace 'infer_datetime_format=True' with format='%Y-%m-%d %H:%M:%S' for example
# data['Timestamp'] = pd.to_datetime(data['Timestamp'], format='%Y-%m-%d %H:%M:%S', errors='coerce')

data.set_index('Timestamp', inplace=True)

# Check for and handle any NaT (Not a Time) values introduced due to errors
print("\nNumber of NaT values in index:", data.index.isnull().sum())
# If there are NaT values, you can drop them:
# data = data[data.index.notnull()]

# plt each distribution of catagorical data
plt.figure(figsize=(10, 6))
data[['GHI', 'DNI', 'DHI']].plot()
plt.title("Solar Radiation (GHI, DNI, DHI) Over Time")
plt.ylabel("Irradiance (W/m²)")
plt.xlabel("Time")
plt.legend()
plt.show()
#

# Monthly Averages Analysis
data['Month'] = data.index.month
monthly_avg = data.groupby('Month')[['GHI', 'DNI', 'DHI']].mean()
monthly_avg.plot(kind='bar', figsize=(10, 6))
plt.title("Monthly Averages of Solar Radiation")
plt.ylabel("Irradiance (W/m²)")
plt.xlabel("Month")
plt.xticks(ticks=range(12), labels=["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])
plt.show()


# Correlation Matrix
correlation_matrix = data.corr()
plt.figure(figsize=(12, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title("Correlation Matrix")
plt.show()

# Distribution Analysis: Histograms for key variables
columns_to_plot = ['GHI', 'DNI', 'DHI', 'Tamb', 'RH', 'WS']
data[columns_to_plot].hist(bins=20, figsize=(12, 8), edgecolor='black')
plt.suptitle("Histograms of Key Variables", y=0.95)
plt.show()

# Scatter Plot: GHI vs Tamb
plt.figure(figsize=(8, 6))
sns.scatterplot(x='Tamb', y='GHI', data=data, alpha=0.7)
plt.title("GHI vs. Ambient Temperature")
plt.xlabel("Ambient Temperature (°C)")
plt.ylabel("GHI (W/m²)")
plt.show()

# Z-Score Analysis: Outlier Detection
data_zscore = data.select_dtypes(include=np.number)
z_scores = np.abs(zscore(data_zscore))
outliers = (z_scores > 3).sum(axis=0)
print("\nNumber of Outliers per Column (Z-Score > 3):")
print(outliers)

# Bubble Chart: GHI vs Tamb vs RH
plt.figure(figsize=(10, 6))
plt.scatter(data['GHI'], data['Tamb'], s=data['RH'], alpha=0.6)
plt.title("GHI vs. Tamb vs. RH (Bubble Size: RH)")
plt.xlabel("GHI (W/m²)")
plt.ylabel("Ambient Temperature (°C)")
plt.colorbar(label="Relative Humidity (%)")
plt.show()


# Wind Analysis: Wind Rose Plot
!pip install windrose
try:
    from windrose import WindroseAxes
    ax = WindroseAxes.from_ax()
    ax.bar(data['WD'], data['WS'], normed=True, opening=0.8, edgecolor='black')
    ax.set_legend()
    plt.title("Wind Speed and Direction")
    plt.show()
except ImportError:
    print("Windrose library not installed. Install it using: pip install windrose")


# Impact of Cleaning on ModA and ModB
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