import streamlit as st
import pandas as pd
import joblib
import plotly.express as px

# -----------------------------
# PAGE CONFIG
# -----------------------------

st.set_page_config(
    page_title="Sales Forecasting Dashboard",
    page_icon="📈",
    layout="wide"
)

# -----------------------------
# LOAD REGISTRIES
# -----------------------------

forecast_registry = joblib.load(
    'forecast_registry.pkl'
)

best_model_registry = joblib.load(
    'best_model_registry.pkl'
)

metrics_registry = joblib.load(
    'metrics_registry.pkl'
)

# -----------------------------
# TITLE
# -----------------------------

st.title("📈 Multi-State Sales Forecasting Dashboard")

st.markdown(
    """
    Forecast next 8 weeks of sales using automatically selected best forecasting model.
    """
)

# -----------------------------
# STATE SELECTION
# -----------------------------

states = sorted(
    list(forecast_registry.keys())
)

selected_state = st.selectbox(
    "Select State",
    states
)

# -----------------------------
# BEST MODEL
# -----------------------------

best_model = best_model_registry[selected_state][
    'model_name'
]

st.subheader("🏆 Best Model")

st.success(best_model)

# -----------------------------
# FORECAST DATA
# -----------------------------

forecast_df = forecast_registry[
    selected_state
]

st.subheader("📅 8-Week Forecast")

st.dataframe(forecast_df)

# -----------------------------
# FORECAST CHART
# -----------------------------

fig = px.line(
    forecast_df,
    x='Date',
    y='Forecast',
    title=f'{selected_state} Sales Forecast',
    markers=True
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# -----------------------------
# METRICS
# -----------------------------

st.subheader("📊 Model Comparison")

metrics_df = metrics_registry[
    selected_state
]

st.dataframe(metrics_df)

# -----------------------------
# METRICS CHART
# -----------------------------

metric_fig = px.bar(
    metrics_df,
    x='Model',
    y='RMSE',
    title='RMSE Comparison'
)

st.plotly_chart(
    metric_fig,
    use_container_width=True
)

# -----------------------------
# FOOTER
# -----------------------------

st.markdown("---")

st.markdown(
    """
    Built using FastAPI, XGBoost, Prophet, SARIMA, LSTM and Streamlit
    """
)