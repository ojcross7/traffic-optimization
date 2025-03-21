# Create src/dashboard.py
import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd
import requests

app = dash.Dash(__name__)


# Fetch live data from Flask API
def fetch_traffic_data():
    response = requests.get("http://localhost:5000/live_data")
    return pd.DataFrame(response.json())


app.layout = html.Div(
    [
        html.H1("Real-Time Traffic Dashboard"),
        dcc.Graph(id="traffic-heatmap"),
        dcc.Graph(id="signal-status"),
        dcc.Interval(id="interval", interval=5000),  # Refresh every 5s
    ]
)


@app.callback(
    [dash.Output("traffic-heatmap", "figure"), dash.Output("signal-status", "figure")],
    [dash.Input("interval", "n_intervals")],
)
def update_dashboard(n):
    df = fetch_traffic_data()

    heatmap = px.density_mapbox(
        df,
        lat="latitude",
        lon="longitude",
        z="congestion",
        mapbox_style="carto-positron",
    )

    signals = px.bar(
        df, x="intersection_id", y="green_time", title="Signal Timing Adjustments"
    )

    return heatmap, signals


if __name__ == "__main__":
    app.run_server(port=8050)
