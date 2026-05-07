from fastapi import FastAPI
import joblib
import pandas as pd

app = FastAPI(
    title="Sales Forecasting API",
    description="Multi-model Time Series Forecasting System",
    version="1.0"
)

forecast_registry = joblib.load(
    'forecast_registry.pkl'
)

best_model_registry = joblib.load(
    'best_model_registry.pkl'
)

metrics_registry = joblib.load(
    'metrics_registry.pkl'
)

@app.get("/")
def home():

    return {
        "message": "Forecasting API Running Successfully"
    }


@app.get("/states")
def get_states():

    return {
        "states": list(
            forecast_registry.keys()
        )
    }
@app.get("/forecast/{state}")
def get_forecast(state: str):

    if state not in forecast_registry:

        return {
            "error": "State not found"
        }

    forecast_df = forecast_registry[state]

    return {
        "state": state,
        "forecast": forecast_df.to_dict(
            orient='records'
        )
    }



@app.get("/best-model/{state}")
def get_best_model(state: str):

    if state not in best_model_registry:

        return {
            "error": "State not found"
        }

    return {
        "state": state,
        "best_model": best_model_registry[state][
            'model_name'
        ]
    }




@app.get("/metrics/{state}")
def get_metrics(state: str):

    if state not in metrics_registry:

        return {
            "error": "State not found"
        }

    metrics_df = metrics_registry[state]

    return {
        "state": state,
        "metrics": metrics_df.to_dict(
            orient='records'
        )
    }