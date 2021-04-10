import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

# load data
data = pd.read_csv("data/Logs_export.csv")

data1 = data.groupby('DNS')[['DATE']].count().sort_values(by='DATE',ascending=False).reset_index()
data2 = data.groupby('COUNTRY_NAME')[['DNS']].count().sort_values(by='DNS',ascending=False).reset_index().head(5)
data3 = data.groupby('CITY')[['DNS']].count().sort_values(by='DNS',ascending=False).reset_index().head(5)

app = dash.Dash(__name__)

app.layout = html.Div(
    children=[
        html.H1(children="Web Logs Analytics",),
        html.P(
            children="Analyze the behavior of vviews"
            " to akumenius.com by date",
        ),
        dcc.Graph(
            figure={
                "data": [
                    {
                        "x": data1.DNS,
                        "y": data1.DATE,
                        "type": "bar",
                    },
                ],
                "layout": {"title": "Web Views"},
            },
        ),
        dcc.Graph(
            figure={
                "data": [
                    {
                        "x": data2.COUNTRY_NAME,
                        "y": data2.DNS,
                        "type": "bar",
                        "oriented": "h"
                    },
                ],
                "layout": {"title": "Country Views"},
            },
        ),
        dcc.Graph(
            figure={
                "data": [
                    {
                        "x": data3.CITY,
                        "y": data3.DNS,
                        "type": "bar",
                    },
                ],
                "layout": {"title": "City Views"},
            },
        ),
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)