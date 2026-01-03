# Wine Quality Data Analysis

Data science techniques to analyse quality of wines provided in the format of the files in the data directory. Vinho Verde dataset used to determine what chemical properties actually make a wine taste good.

## Overview

This project demonstrates how to take in raw data, perform exploratory data analysis and visualize relationships between chemical features (like acidity, pH, and alcohol) and the quality rating of the wine.

## Features

* **Data Ingestion & Cleaning**: Loads raw CSV data and checks for null values or integrity errors
* **Descriptive Statistics**: Calculates mean, median, and specific quality groupings (e.g., counting wines with ratings > 7 or < 5)
* **Advanced Visualization**:
    * **Scatter Matrix**: Visualizes distributions across all feature pairs
    * **Correlation Heatmap**: Highlights direct and inverse relationships between features (e.g., fixed acidity vs. pH)
    * **Joint Grids**: Detailed regression plots for specific feature comparisons
* **Outlier Detection**: Implements Tukey's Method (Interquartile Range) to identify and flag anomalous data points that could skew predictions

## Prerequisites

* **Operating System**: Any
* **Runtime**: Python 3.x (Anaconda distribution recommended)
* **Libraries**: `numpy`, `pandas`, `matplotlib`, `seaborn`, `scipy` (dependency)

## Quick Start

To use this program, simply run the main.py file while ensuring the data folder is in the same directory as main.py. If you'd like to try out other test data, modify line 6 appropriately.
