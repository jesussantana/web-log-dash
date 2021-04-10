import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

# load data
data = pd.read_csv("data/Logs_export.csv")

data = data.query("DNS == 'www.akumenius.com' and COUNTRY_NAME == 'Spain'")
# data["Date"] = pd.to_datetime(data["DATE"], format="%Y-%m-%d")
data.sort_values("DATE", inplace=True)

app = dash.Dash(__name__)

app.layout = html.Div(
    children=[
        html.H1(children="Web Logs Analytics",),
        html.P(
            children="Analyze the behavior of visits"
            " to akumenius.com by date",
        ),
        dcc.Graph(
            figure={
                "data": [
                    {
                        "x": data.DATE,
                        "y": data.DNS.count(),
                        "type": "bar",
                    },
                ],
                "layout": {"title": "Web Visits"},
            },
        ),
        dcc.Graph(
            figure={
                "data": [
                    {
                        "x": data.DNS,
                        "y": data.CITY,
                        "type": "bar",
                    },
                ],
                "layout": {"title": "City Visits"},
            },
        ),
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)