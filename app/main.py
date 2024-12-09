from utils import (
    load_dataset,
    display_dataset_info,
    check_missing_values,
    check_negative_values,
    display_summary_statistics,
    process_timestamps,
    plot_solar_radiation,
    analyze_monthly_averages,
    plot_correlation_matrix,
    plot_histograms,
    scatter_plot_ghi_vs_tamb,
    detect_outliers,
    plot_bubble_chart,
    plot_wind_rose,
    analyze_cleaning_impact,
)


def main(file_path):
    """
    Execute a series of data analysis and visualization tasks on a dataset.

    Args:
        file_path (str): The file path to the dataset to be loaded and analyzed.

    The function performs the following tasks:
    - Loads the dataset from the specified file path.
    - Displays an overview and the first few rows of the dataset.
    - Checks for missing and negative values in specified columns.
    - Displays summary statistics of the dataset.
    - Processes timestamps and sets them as the index.
    - Plots various visualizations including solar radiation over time,
      monthly averages, correlation matrix, histograms, scatter plots,
      bubble charts, wind rose, and the impact of cleaning on module readings.
    - Detects outliers in the dataset.
    """
    data = load_dataset(file_path)
    display_dataset_info(data)
    check_missing_values(data)
    check_negative_values(data, ['GHI', 'DNI', 'DHI'])
    display_summary_statistics(data)
    data = process_timestamps(data)
    plot_solar_radiation(data)
    analyze_monthly_averages(data)
    plot_correlation_matrix(data)
    plot_histograms(data, ['GHI', 'DNI', 'DHI', 'Tamb', 'RH', 'WS'])
    scatter_plot_ghi_vs_tamb(data)
    detect_outliers(data)
    plot_bubble_chart(data)
    plot_wind_rose(data)
    analyze_cleaning_impact(data)


if __name__ == "__main__":
    file_path = 'benin-malanville.csv'
    main(file_path)
