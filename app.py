import streamlit as st
import pandas as pd

# ==========================================
# 1. PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="Global Food Price Intelligence",
    page_icon="🌾",
    layout="wide"
)


# ==========================================
# 2. LOAD DATASET
# ==========================================

@st.cache_data
def load_data():
    file_path = "data/raw/BGD_RTFP_mkt_2007_2026-10-05.csv"

    data = pd.read_csv(file_path)

    data["price_date"] = pd.to_datetime(data["price_date"])

    return data


try:
    df = load_data()

except FileNotFoundError:
    st.error(
        "Dataset file not found. Please check the CSV file path."
    )
    st.stop()


# ==========================================
# 3. FOOD ITEMS
# ==========================================

food_options = {
    "Rice": "c_rice",
    "Lentils": "c_lentils",
    "Oil": "c_oil",
    "Wheat Flour": "c_wheat_flour"
}


# ==========================================
# 4. DASHBOARD HEADER
# ==========================================

st.title("🌾 Global Food Price Intelligence")

st.subheader("Bangladesh Food Price Analytics")

st.write(
    "Explore food price trends, identify unusual price changes, "
    "and examine historical price estimates across markets."
)

st.caption(
    "Data source: World Bank Microdata Library. "
    "Values are dataset estimates; verify price units before "
    "interpreting them as consumer prices."
)


# ==========================================
# 5. SIDEBAR FILTERS
# ==========================================

st.sidebar.title("📊 Dashboard Filters")

selected_food = st.sidebar.selectbox(
    "Select Food Item",
    list(food_options.keys())
)

market_options = sorted(
    df["mkt_name"].dropna().unique().tolist()
)

selected_market = st.sidebar.selectbox(
    "Select Market",
    ["All Markets"] + market_options
)

min_date = df["price_date"].min().date()
max_date = df["price_date"].max().date()

selected_dates = st.sidebar.date_input(
    "Select Date Range",
    value=(min_date, max_date),
    min_value=min_date,
    max_value=max_date,
    key="dashboard_date_range"
)


# ==========================================
# 6. FILTER DATA
# ==========================================

selected_column = food_options[selected_food]

filtered_df = df.copy()

if selected_market != "All Markets":
    filtered_df = filtered_df[
        filtered_df["mkt_name"] == selected_market
    ]

if len(selected_dates) == 2:
    start_date, end_date = selected_dates

    filtered_df = filtered_df[
        (filtered_df["price_date"] >= pd.Timestamp(start_date))
        &
        (
            filtered_df["price_date"]
            < pd.Timestamp(end_date) + pd.Timedelta(days=1)
        )
    ]

elif len(selected_dates) == 1:
    selected_day = pd.Timestamp(selected_dates[0])

    filtered_df = filtered_df[
        filtered_df["price_date"].dt.date == selected_day.date()
    ]


# ==========================================
# 7. DASHBOARD METRICS
# ==========================================

st.markdown("---")

col1, col2, col3 = st.columns(3)

col1.metric(
    "Total Records",
    f"{len(df):,}"
)

col2.metric(
    "Markets",
    f"{df['mkt_name'].nunique():,}"
)

col3.metric(
    "Filtered Records",
    f"{len(filtered_df):,}"
)


# ==========================================
# 8. MONTHLY PRICE DATA
# ==========================================

monthly_chart = (
    filtered_df.groupby("price_date")[selected_column]
    .mean()
    .reset_index()
    .dropna(subset=[selected_column])
    .sort_values("price_date")
)


# ==========================================
# 9. PRICE TREND CHART
# ==========================================

st.markdown("---")

st.subheader(f"📈 {selected_food} Price Trend")

if not monthly_chart.empty:

    price_chart = monthly_chart.set_index("price_date")

    st.line_chart(
        price_chart[selected_column],
        x_label="Date",
        y_label="Estimated Price"
    )

    st.caption(
        "The chart shows the monthly mean of the selected "
        "price estimate across the selected market(s)."
    )

else:
    st.warning(
        "No price data is available for the selected filters."
    )


# ==========================================
# 10. PRICE ANOMALY DETECTION
# ==========================================

st.markdown("---")

st.subheader("🚨 Price Anomaly Detection")

if len(monthly_chart) >= 5:

    anomaly_data = monthly_chart.copy()

    anomaly_data["price_change_pct"] = (
        anomaly_data[selected_column].pct_change() * 100
    )

    changes = anomaly_data["price_change_pct"].dropna()

    if len(changes) >= 3:

        q1 = changes.quantile(0.25)
        q3 = changes.quantile(0.75)

        iqr = q3 - q1

        lower_bound = q1 - 1.5 * iqr
        upper_bound = q3 + 1.5 * iqr

        anomalies = anomaly_data[
            (
                anomaly_data["price_change_pct"] < lower_bound
            )
            |
            (
                anomaly_data["price_change_pct"] > upper_bound
            )
        ].copy()

        col1, col2, col3 = st.columns(3)

        col1.metric(
            "Potential Anomalies",
            len(anomalies)
        )

        col2.metric(
            "Lower Threshold",
            f"{lower_bound:.2f}%"
        )

        col3.metric(
            "Upper Threshold",
            f"{upper_bound:.2f}%"
        )

        if not anomalies.empty:

            st.write(
                "Months with statistically unusual price changes:"
            )

            anomaly_table = anomalies[
                [
                    "price_date",
                    selected_column,
                    "price_change_pct"
                ]
            ].rename(
                columns={
                    "price_date": "Date",
                    selected_column: "Estimated Price",
                    "price_change_pct": "Monthly Change (%)"
                }
            )

            st.dataframe(
                anomaly_table.round(2),
                use_container_width=True,
                hide_index=True
            )

        else:
            st.success(
                "No potential anomalies detected for this selection."
            )

        st.caption(
            "Method: IQR applied to month-to-month percentage changes. "
            "These are statistical outliers, not proof of specific events."
        )

    else:
        st.info(
            "More monthly observations are needed for anomaly detection."
        )

else:
    st.info(
        "Select a wider date range for anomaly detection."
    )


# ==========================================
# 11. TWELVE-MONTH BASELINE FORECAST
# ==========================================

st.markdown("---")

st.subheader("🔮 12-Month Price Forecast")

if len(monthly_chart) >= 12:

    last_price = monthly_chart[selected_column].iloc[-1]

    last_date = monthly_chart["price_date"].max()

    future_dates = pd.date_range(
        start=last_date + pd.offsets.MonthBegin(1),
        periods=12,
        freq="MS"
    )

    forecast_df = pd.DataFrame({
        "price_date": future_dates,
        "forecast_price": [last_price] * 12
    })

    col1, col2 = st.columns(2)

    col1.metric(
        "Latest Estimated Price",
        f"{last_price:.2f}"
    )

    col2.metric(
        "Baseline Forecast",
        f"{last_price:.2f}"
    )

    st.caption(
        "Baseline method: the latest available estimate is repeated "
        "for the next 12 months. This is not a guarantee or an "
        "advanced predictive model."
    )

    forecast_chart = forecast_df.set_index("price_date")

    st.line_chart(
        forecast_chart["forecast_price"],
        x_label="Month",
        y_label="Forecast Price"
    )

    with st.expander("View forecast table"):

        display_forecast = forecast_df.rename(
            columns={
                "price_date": "Forecast Month",
                "forecast_price": "Forecast Price"
            }
        )

        display_forecast["Forecast Price"] = (
            display_forecast["Forecast Price"].round(2)
        )

        st.dataframe(
            display_forecast,
            use_container_width=True,
            hide_index=True
        )

else:
    st.info(
        "At least 12 monthly observations are required for forecasting."
    )


# ==========================================
# 12. DATA PREVIEW
# ==========================================

st.markdown("---")

with st.expander("📋 View Dataset Preview"):

    st.dataframe(
        filtered_df.head(100),
        use_container_width=True,
        hide_index=True
    )



# ==========================================
# 13. MODEL PERFORMANCE
# ==========================================

st.markdown("---")

st.subheader("📊 Forecast Model Performance")

st.write(
    "The following results come from the earlier rice-price "
    "forecasting experiment using a chronological train-test split."
)

model_results = pd.DataFrame({
    "Model": [
        "Naive Forecast",
        "Seasonal Naive",
        "Holt Exponential Smoothing"
    ],
    "MAE": [
        2.785,
        3.072,
        10.707
    ],
    "RMSE": [
        3.415,
        3.485,
        12.455
    ]
})

st.dataframe(
    model_results,
    use_container_width=True,
    hide_index=True
)

best_model = model_results.loc[
    model_results["MAE"].idxmin()
]

col1, col2 = st.columns(2)

col1.metric(
    "Best Model by MAE",
    best_model["Model"]
)

col2.metric(
    "Best Model MAE",
    f"{best_model['MAE']:.3f}"
)

st.bar_chart(
    model_results.set_index("Model")[["MAE", "RMSE"]],
    x_label="Forecasting Model",
    y_label="Error"
)

st.info(
    "Interpretation: Lower MAE and RMSE indicate smaller forecast "
    "errors on the evaluated test period. Naive Forecast performed "
    "best in the earlier rice-price experiment. These metrics are "
    "not recalculated for the currently selected food item or market."
)


# ==========================================
# 14. FOOTER
# ==========================================

st.markdown("---")

st.caption(
    "Global Food Price Intelligence | Data Analysis & Forecasting Project"
)

