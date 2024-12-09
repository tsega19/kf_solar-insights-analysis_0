```markdown
# Solar Radiation Data Analysis

## Overview

This project provides tools to analyze solar radiation datasets, focusing on solar metrics like GHI, DNI, and DHI. It includes data cleaning, visualization, and advanced analysis.

## Features

- Handle missing and erroneous data.
- Visualize key metrics and trends.
- Outlier detection using z-scores.
- Wind rose plots for wind speed and direction.
- Cleaning impact analysis on solar modules.

## Installation

1. Clone the repository.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Place your dataset (e.g., `data.csv`) in the project directory.
2. Run the analysis:
   ```bash
   python main.py
   ```

## Dependencies

- Python 3.8+
- Libraries: pandas, numpy, matplotlib, seaborn, scipy, windrose

## Dataset Requirements

The dataset should include columns like:
- **Timestamp**: Date and time.
- **GHI, DNI, DHI**: Solar metrics.
- **Tamb, RH, WS, WD**: Environmental data.

## Outputs

- Plots: Time-series, bar charts, correlation heatmaps, wind rose diagrams.
- Logs: Dataset summaries, missing data, and outlier detection.

