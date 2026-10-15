# 🌾 Global Food Price Intelligence

### Food Price Analytics, Anomaly Detection & Forecasting in Bangladesh

An interactive data science project for analyzing historical food price estimates in Bangladesh, identifying unusual price changes, comparing forecasting models, and exploring baseline forecasts through an interactive Streamlit dashboard.

The project combines data exploration, time-series analysis, statistical anomaly detection, forecasting evaluation, and interactive visualization to make food price data easier to understand.

---

## 📌 Table of Contents

- [Project Overview](#-project-overview)
- [Objectives](#-project-objectives)
- [Key Features](#-key-features)
- [Dashboard Preview](#-dashboard-preview)
- [Dataset Information](#-dataset-information)
- [Technologies Used](#-technologies-used)
- [Project Structure](#-project-structure)
- [Methodology](#-methodology)
- [Exploratory Data Analysis](#-exploratory-data-analysis)
- [Anomaly Detection](#-anomaly-detection)
- [Forecasting Models](#-forecasting-models)
- [Model Evaluation](#-model-evaluation)
- [Installation and Setup](#-installation-and-setup)
- [How to Use the Dashboard](#-how-to-use-the-dashboard)
- [Limitations](#-limitations)
- [Future Improvements](#-future-improvements)
- [Author](#-author)

---

## 📖 Project Overview

Food prices are an important part of economic analysis because changes in food prices can affect household purchasing power and affordability.

However, understanding historical food price movements requires more than simply looking at a table of numbers. Analysts need ways to explore trends over time, compare locations, identify unusual changes, and evaluate forecasting methods.

**Global Food Price Intelligence** addresses these analytical needs through an interactive data science dashboard built with Python and Streamlit.

The project uses monthly food price estimates for Bangladesh from the World Bank Microdata Library.

Users can explore different food commodities, select markets and date ranges, visualize historical price trends, identify statistically unusual monthly changes, and examine a simple 12-month baseline forecast.

The project also includes a comparison of three forecasting methods evaluated during the exploratory analysis.

### Project Type

- Data Science
- Exploratory Data Analysis (EDA)
- Time-Series Analysis
- Anomaly Detection
- Forecasting
- Interactive Data Visualization
- Web Application Development

---

## 🎯 Project Objectives

The main objectives of this project are:

1. Explore historical food price estimates in Bangladesh.
2. Analyze monthly and yearly price movements.
3. Compare food price trends across available markets.
4. Identify potential anomalies in monthly price changes.
5. Implement baseline time-series forecasting methods.
6. Evaluate forecasting performance using MAE and RMSE.
7. Build an interactive dashboard for data exploration.
8. Present analytical results through clear visualizations and tables.

---

## ✨ Key Features

### 1. Interactive Dashboard

The application is built using Streamlit and provides an interactive interface for exploring the dataset.

Users can select food commodities, markets, and date ranges to investigate different subsets of the data.

### 2. Food Commodity Selection

The dashboard supports four food commodities:

- Rice
- Lentils
- Oil
- Wheat Flour

The application uses the corresponding `c_` price-series columns for visualization.

### 3. Market Selection

Users can choose:

- All available markets
- An individual market

The selected market determines which observations are included in the price trend and related analysis.

### 4. Date Range Filtering

Users can select a time period to focus on a particular part of the historical dataset.

The selected date range affects the price trend, anomaly detection, and baseline forecast.

### 5. Price Trend Visualization

The dashboard displays a line chart of the selected price series over time.

When multiple markets are selected, the application calculates the mean of the selected price-series variable for each available date.

This allows users to explore broad historical patterns and compare them with individual market trends.

### 6. Statistical Anomaly Detection

The project uses the Interquartile Range (IQR) method to identify potential outliers in month-to-month percentage price changes.

The dashboard displays:

- Number of potential anomalies
- Lower statistical threshold
- Upper statistical threshold
- Dates associated with detected anomalies
- Corresponding price estimates
- Percentage changes

### 7. Twelve-Month Baseline Forecast

The dashboard provides a simple 12-month baseline forecast.

The current implementation repeats the latest available price estimate for the next 12 months.

This serves as a baseline for comparison rather than an advanced predictive model.

### 8. Forecast Model Comparison

The project includes results from an earlier rice-price forecasting experiment.

Three forecasting approaches were evaluated:

- Naive Forecast
- Seasonal Naive
- Holt Exponential Smoothing

The models were compared using Mean Absolute Error (MAE) and Root Mean Squared Error (RMSE).

## Dataset

This project uses the **Monthly Food Price Estimates by Product and Market** dataset for Bangladesh, published through the World Bank Microdata Library.

### Data Source

* **Publisher:** World Bank Microdata Library
* **Country:** Bangladesh
* **Dataset:** Monthly food price estimates by product and market
* **Dataset ID:** `BGD_2021_RTFP_v02_M`
* **Version used:** 2026-10-05
* **Official source:** https://microdata.worldbank.org/catalog/6164/get-microdata

### How to Download the Dataset

1. Open the official World Bank dataset page linked above.
2. Find the Bangladesh food price dataset and its available data downloads.
3. Download the version you want to use.
4. Extract the downloaded ZIP file if necessary.
5. Place the CSV file inside `data/raw/`.
6. Ensure the filename matches the one configured in `app.py`:

   `BGD_RTFP_mkt_2007_2026-10-05.csv`

If you download a newer version, update the filename in `app.py` accordingly.

### Dataset Structure

The dataset contains monthly food price estimates for different food products and markets in Bangladesh. This project uses the data for exploratory analysis, price-trend visualization, anomaly detection, and baseline forecasting.

The analysis depends on the selected dataset version. Newer versions may contain revised estimates or different observations.

### Data Attribution

Andrée, B. P. J. (2021). *Monthly food price estimates by product and market* (Version 2026-10-05). BGD_2021_RTFP_v02_M. Washington, DC: World Bank Microdata Library.

Dataset source: https://microdata.worldbank.org/catalog/6164/get-microdata

The dataset is provided by the World Bank. This project is an independent analytical project and is not affiliated with or endorsed by the World Bank.

## 🖥️ Dashboard Preview

The dashboard contains the following sections:

| Section | Description |
|---|---|
| Dashboard Filters | Select food, market, and date range |
| Summary Metrics | View dataset and filtered-record counts |
| Price Trend | Explore historical price estimates |
| Price Anomaly Detection | Identify unusual monthly percentage changes |
| Twelve-Month Forecast | Examine the baseline forecast |
| Forecast Model Performance | Compare previously evaluated forecasting models |
| Dataset Preview | Inspect filtered observations |

To add screenshots to this README later, create a `screenshots` directory and save your dashboard screenshots there.

For example:

```text
screenshots/
├── dashboard_overview.png
├── price_trend.png
├── anomaly_detection.png
└── model_performance.png
```

You can then embed an image using:

```markdown
![Dashboard Overview](screenshots/dashboard_overview.png)
```

---

## 📊 Dataset Information

### Data Source

**Source:** World Bank Microdata Library

**Dataset:** Monthly food price estimates by product and market

**Country:** Bangladesh

The project uses the following downloaded CSV file:

`BGD_RTFP_mkt_2007_2026-10-05.csv`

### Dataset Summary

| Attribute | Value |
|---|---|
| Country | Bangladesh |
| Number of records | 26,418 |
| Number of markets | 111 |
| Number of variables | 53 |
| Dataset time coverage | January 2007 – October 2026 |
| Observation frequency | Monthly |
| Currency metadata | BDT |
| Selected commodities | Rice, Lentils, Oil, Wheat Flour |

These figures describe the dataset examined during project development. The time coverage refers to the dataset's available date range, not necessarily the availability of every commodity in every market.

### Important Variables

| Variable | Description |
|---|---|
| `country` | Country name |
| `adm1_name` | First-level administrative area |
| `adm2_name` | Second-level administrative area |
| `mkt_name` | Market name |
| `lat` | Latitude |
| `lon` | Longitude |
| `price_date` | Observation date |
| `year` | Year of observation |
| `month` | Month of observation |
| `currency` | Currency metadata |
| `rice` | Rice-related variable |
| `lentils` | Lentils-related variable |
| `oil` | Oil-related variable |
| `wheat_flour` | Wheat-flour-related variable |
| `c_rice` | Selected rice price-series variable |
| `c_lentils` | Selected lentils price-series variable |
| `c_oil` | Selected oil price-series variable |
| `c_wheat_flour` | Selected wheat-flour price-series variable |
| `index_confidence_score` | Dataset confidence-related metadata |
| `spatially_interpolated` | Spatial interpolation indicator |

**Data interpretation note:** The precise definitions of the price-series prefixes and the unit of measurement must be verified against the original dataset documentation. The `BDT` currency metadata alone does not establish the price unit.

### Missing Values

During initial exploration, the following missing-value counts were observed:

| Variable | Missing Values |
|---|---:|
| `rice` | 22,752 |
| `lentils` | 22,270 |
| `oil` | 21,697 |
| `wheat_flour` | 21,638 |
| `inflation_rice` | 1,332 |
| `inflation_oil` | 1,332 |
| `inflation_lentils` | 1,332 |
| `inflation_wheat_flour` | 1,332 |
| `inflation_food_price_index` | 1,332 |
| `lat` | 238 |
| `lon` | 238 |

The selected `c_` price-series columns had no missing values in the initial full-dataset inspection.

Missing values should be assessed for the selected variable and market before conducting additional analyses.

---

## 🛠️ Technologies Used

### Programming Language

- Python

### Data Analysis

- Pandas
- NumPy

### Visualization

- Streamlit charts
- Matplotlib

### Statistical Analysis and Forecasting

- Scikit-learn
- Statsmodels

### Development Environment

- Visual Studio Code
- Jupyter Notebook
- Git
- GitHub

---

## 📁 Project Structure

The project is organized as follows:

```text
global-food-price-intelligence/
│
├── app.py
│
├── data/
│   └── raw/
│       └── BGD_RTFP_mkt_2007_2026-10-05.csv
│
├── notebooks/
│   └── 01_data_exploration.ipynb
│
├── screenshots/
│
├── requirements.txt
│
├── README.md
│
└── .gitignore
```

### File Descriptions

| File or Directory | Purpose |
|---|---|
| `app.py` | Main Streamlit dashboard |
| `data/raw/` | Original downloaded dataset |
| `notebooks/` | Data exploration and model experiments |
| `screenshots/` | Dashboard screenshots |
| `requirements.txt` | Python dependencies |
| `README.md` | Project documentation |
| `.gitignore` | Files and directories excluded from Git |

The `screenshots/`, `requirements.txt`, and `.gitignore` entries represent the intended project structure and should be created if they do not already exist.

---

## 🔬 Methodology

The project follows a structured data science workflow.

### Step 1: Data Collection

The food price dataset was obtained from the World Bank Microdata Library.

The downloaded CSV contains monthly observations for Bangladesh markets and multiple food-related variables.

### Step 2: Data Loading

The dataset was loaded into a Pandas DataFrame.

```python
import pandas as pd

file_path = (
    "data/raw/BGD_RTFP_mkt_2007_2026-10-05.csv"
)

df = pd.read_csv(file_path)

print("Dataset shape:", df.shape)

print(df.head())
```

### Step 3: Data Exploration

Initial exploration included:

- Inspecting column names
- Examining data types
- Checking missing values
- Reviewing descriptive statistics
- Counting available markets
- Checking observation dates
- Checking duplicate market-date rows
- Comparing food price-series variables

### Step 4: Date Preparation

The date variable was converted to a datetime type.

```python
df["price_date"] = pd.to_datetime(
    df["price_date"]
)
```

This enables chronological sorting, date filtering, and time-series analysis.

### Step 5: Price Trend Analysis

Monthly and yearly averages were calculated to examine historical price movements.

The initial rice-price analysis used the `c_rice` variable.

### Step 6: Monthly Percentage Change

Month-to-month percentage changes were calculated using:

```python
monthly_rice["price_change_pct"] = (
    monthly_rice["c_rice"].pct_change() * 100
)
```

This measures the percentage difference between consecutive observations in the selected monthly series.

### Step 7: Anomaly Detection

The IQR method was applied to the distribution of monthly percentage changes.

### Step 8: Forecasting

Three forecasting approaches were evaluated using a chronological training and testing split.

### Step 9: Interactive Application

The analysis was incorporated into a Streamlit application with interactive filters, charts, tables, and forecasting outputs.

---

## 📈 Exploratory Data Analysis

The initial rice-price analysis used the `c_rice` variable.

### Historical Summary

| Statistic | Value |
|---|---:|
| Number of monthly observations | 238 |
| Mean | 35.78 |
| Standard deviation | 9.38 |
| Minimum | 18.00 |
| Median | 33.22 |
| Maximum | 53.46 |

These statistics describe the monthly rice-price series examined during the initial analysis.

### Yearly Average Rice Price

The following yearly averages were calculated during exploration:

| Year | Average |
|---|---:|
| 2007 | 21.84 |
| 2010 | 29.50 |
| 2015 | 29.34 |
| 2017 | 38.92 |
| 2020 | 38.51 |
| 2021 | 43.48 |
| 2022 | 44.85 |
| 2023 | 46.85 |
| 2024 | 50.32 |
| 2025 | 52.74 |
| 2026 | 49.76 |

**Note:** The 2026 figure covers January through October, so it is not a full-year average.

The historical series shows a broad upward movement, although prices also declined during some periods.

These observations describe the dataset and do not establish the causes of price changes.

---

## 🚨 Anomaly Detection

The project uses the Interquartile Range method to identify unusually large or small month-to-month percentage changes.

### IQR Formula

The interquartile range is:

\[
IQR = Q_3 - Q_1
\]

The lower threshold is:

\[
Lower = Q_1 - 1.5 \times IQR
\]

The upper threshold is:

\[
Upper = Q_3 + 1.5 \times IQR
\]

A monthly percentage change below the lower threshold or above the upper threshold is classified as a potential anomaly.

### Initial Rice-Price Results

| Metric | Result |
|---|---:|
| Lower threshold | -5.93% |
| Upper threshold | +6.73% |
| Potential anomalies | 18 |

### Largest Monthly Increases

| Month | Percentage Change |
|---|---:|
| February 2013 | +10.84% |
| December 2007 | +9.74% |
| January 2010 | +9.72% |
| September 2016 | +8.72% |
| February 2007 | +8.02% |

These results come from the initial rice-price analysis.

The dashboard recalculates potential anomalies for the selected food item, market, and date range.

**Important:** Statistical anomalies identify unusual movements in the selected series. They do not prove that a particular event caused a price increase or decrease.

---

## 🔮 Forecasting Models

Three forecasting methods were evaluated during the initial rice-price experiment.

### 1. Naive Forecast

The Naive Forecast uses the last observed training value as the forecast for every test-period month.

This provides a simple baseline against which more complex forecasting methods can be compared.

### 2. Seasonal Naive

The Seasonal Naive method uses the value from 12 months earlier as the forecast.

For example, the value for November of one year is used to forecast November of the following year.

This method can be useful when annual seasonal patterns are present.

### 3. Holt Exponential Smoothing

Holt Exponential Smoothing models the level and trend of a time series.

The initial experiment used additive trend and no explicit seasonal component.

A trend-based method can perform poorly when its estimated trend does not continue into the evaluation period.

---

## 📊 Model Evaluation

The initial experiment used a chronological train-test split.

### Train-Test Split

| Dataset | Observations | Period |
|---|---:|---|
| Training | 190 | January 2007 – October 2022 |
| Testing | 48 | November 2022 – October 2026 |
| Total | 238 | January 2007 – October 2026 |

The chronological split preserves time order and avoids randomly mixing future observations into the training data.

### Evaluation Metrics

#### Mean Absolute Error (MAE)

MAE measures the average absolute difference between actual and forecast values.

\[
MAE = \frac{1}{n}\sum_{i=1}^{n}|y_i-\hat{y}_i|
\]

A lower MAE indicates smaller average absolute errors.

#### Root Mean Squared Error (RMSE)

RMSE is the square root of the average squared forecast error.

\[
RMSE = \sqrt{\frac{1}{n}\sum_{i=1}^{n}(y_i-\hat{y}_i)^2}
\]

RMSE penalizes larger errors more strongly than MAE.

### Initial Model Comparison

| Model | MAE | RMSE |
|---|---:|---:|
| Naive Forecast | 2.785 | 3.415 |
| Seasonal Naive | 3.072 | 3.485 |
| Holt Exponential Smoothing | 10.707 | 12.455 |

### Interpretation

In the initial rice-price experiment, the Naive Forecast achieved the lowest MAE and RMSE among the three tested methods.

The Seasonal Naive method performed slightly worse, while Holt Exponential Smoothing produced substantially larger errors.

These results indicate that the simple Naive Forecast performed best on this particular test period.

They do not establish that the Naive Forecast will perform best for every food item, market, or future period.

The dashboard displays these historical evaluation results as a reference. They are not recalculated for each selected commodity or market.

---

## 💻 Installation and Setup

Follow these steps to run the project locally.

### Prerequisites

Install:

- Python
- Visual Studio Code
- Git (optional, for version control)

### Step 1: Clone the Repository

If the project has been published to GitHub, clone it using:

```bash
git clone https://github.com/Sih-ab/global-food-price-intelligence.git
```

Clone the repository using the command above.

Alternatively, open your existing project folder directly in Visual Studio Code.

### Step 2: Open the Project Directory

Open the `global-food-price-intelligence` directory in VS Code.

Ensure that `app.py` and the `data/` directory are present.

### Step 3: Create a Virtual Environment

In the VS Code terminal, run:

```powershell
python -m venv .venv
```

Activate it in PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, use the Python executable inside the environment directly or follow the appropriate Windows environment-activation instructions.

### Step 4: Install Dependencies

If `requirements.txt` exists, run:

```powershell
python -m pip install -r requirements.txt
```

If the file has not been created yet, install the required packages:

```powershell
python -m pip install streamlit pandas numpy matplotlib scikit-learn statsmodels
```

### Step 5: Verify the Dataset Path

Ensure the downloaded CSV is located at:

```text
data/raw/BGD_RTFP_mkt_2007_2026-10-05.csv
```

The application currently expects this relative path.

### Step 6: Run the Dashboard

From the project root directory, execute:

```powershell
python -m streamlit run app.py
```

Streamlit will display a local address in the terminal.

Open that address in your browser to access the dashboard.

---

## 🧭 How to Use the Dashboard

### Step 1: Select a Food Item

Choose Rice, Lentils, Oil, or Wheat Flour from the sidebar.

### Step 2: Select a Market

Choose All Markets to examine the mean across available markets, or select an individual market.

### Step 3: Select a Date Range

Choose the historical period you want to analyze.

For meaningful anomaly detection and forecasting, use a sufficiently long period.

### Step 4: Explore Price Trends

Review the line chart to understand how the selected price series changes over time.

### Step 5: Examine Potential Anomalies

Review the IQR thresholds and the table of months with unusual percentage changes.

### Step 6: Review the Baseline Forecast

Examine the next 12 months of repeated baseline estimates.

Remember that the current baseline forecast assumes the latest selected estimate remains constant.

### Step 7: Compare Forecasting Models

Review the MAE and RMSE table from the initial rice-price forecasting experiment.

These metrics are historical experiment results rather than live metrics for the currently selected filters.

### Step 8: Inspect the Dataset

Expand the dataset preview to examine a sample of the filtered observations.

---

## ⚠️ Limitations

This project has several important limitations.

### 1. Price Variable Definitions

The exact definitions of the selected `c_` price-series variables and their measurement units should be confirmed using the original dataset documentation.

The currency metadata alone is insufficient to determine the price unit.

### 2. Missing Documentation

The original data dictionary was not available in the local project files during development.

Consequently, variable interpretations that require the data dictionary should be treated cautiously.

### 3. Statistical Anomalies

The IQR method identifies outliers in the distribution of monthly percentage changes.

It does not explain why a price change occurred or establish a causal relationship.

### 4. Baseline Forecast

The dashboard's 12-month forecast repeats the latest available estimate.

It does not model future trends, seasonality, policy changes, supply shocks, or other potential influences on food prices.

### 5. Historical Model Evaluation

The model comparison results come from a single chronological train-test split.

Further evaluation across different time periods would be needed to assess how stable the results are.

### 6. Market Aggregation

When All Markets is selected, the dashboard calculates a mean across available observations for each date.

This aggregate can conceal differences between markets.

### 7. No Causal Inference

The project is designed for descriptive analysis, anomaly detection, and forecasting.

It does not estimate the causal effects of economic events, policies, or other external factors.

---

## 🚀 Future Improvements

Several enhancements could make this project more powerful.

### Forecasting Improvements

- Implement SARIMA or another suitable seasonal time-series model.
- Compare additional forecasting approaches.
- Evaluate models using rolling-origin or walk-forward validation.
- Calculate evaluation metrics dynamically for each eligible commodity and market.
- Add prediction intervals when supported by the selected model.
- Compare baseline forecasts against more advanced methods.

### Anomaly Detection Improvements

- Evaluate rolling statistical thresholds.
- Compare IQR with robust z-scores.
- Investigate market-level anomalies separately.
- Visualize detected anomalies directly on the price trend chart.
- Explore possible external explanations using independently verified data.

### Dashboard Improvements

- Add a downloadable filtered dataset.
- Export anomaly tables as CSV.
- Add historical summary statistics.
- Compare multiple commodities on the same chart where appropriate.
- Add market-level comparison charts.
- Improve chart annotations and date formatting.
- Add automated data validation checks.

### Data Improvements

- Document the precise meaning and unit of each price variable.
- Track data versions and update dates.
- Investigate missing values in the original and estimated series.
- Add external economic indicators where suitable and reliably sourced.
- Distinguish observed estimates from interpolated or modeled values.

### Deployment Improvements

- Deploy the Streamlit application online.
- Add a reproducible dependency file.
- Add automated tests for data processing and forecasting functions.
- Improve repository documentation and screenshots.

---

## 👨‍💻 Author

**MD. Sihab Hossen**

Data Science | Python | Machine Learning | Data Visualization

GitHub: https://github.com/Sih-ab

---

## 📜 Disclaimer

This project is intended for educational and analytical purposes.

The results describe patterns in the selected dataset and should not be interpreted as official market-price quotations, guaranteed future prices, or proof of the causes of price movements.

Users should consult the original dataset documentation before interpreting price units, variable definitions, or data-quality indicators.

---

⭐ If you find this project useful, feel free to explore the code, reproduce the analysis, and suggest improvements.