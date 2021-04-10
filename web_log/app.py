import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import plotly.io as pio
import pandas as pd

template = "plotly_dark"
# load data
data = pd.read_csv("data/Logs_export.csv")

data1 = data.groupby('DNS')[['DATE']].count().sort_values(by='DATE',ascending=False).reset_index()
data2 = data.groupby('COUNTRY_NAME')[['DNS']].count().sort_values(by='DNS',ascending=False).reset_index().head(5)
data3 = data.groupby('CITY')[['DNS']].count().sort_values(by='DNS',ascending=False).reset_index().head(25)

app = dash.Dash(__name__)

'''import plotly.graph_objects as go

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2014_apple_stock.csv')

fig = go.Figure(go.Scatter(x = df['AAPL_x'], y = df['AAPL_y'],
                  name='Share Prices (in USD)'))

fig.update_layout(title='Apple Share Prices over time (2014)',
                   plot_bgcolor='rgb(230, 230,230)',
                   showlegend=True)

fig.show()'''

app.layout = html.Div(
    children=[
        html.H1(children="Web Logs Analytics",),
        html.P(
            children="Analyze the behavior of vviews"
            " to akumenius.com",
        ),
        dcc.Graph(
            figure={
                "data": [
                    {
                        "x": data1.DNS,
                        "y": data1.DATE,
                        "type": "scatter",
                    },
                ],
                
                "layout": {"title": "Web Views", "template":"template"},
            },
        ),
        dcc.Graph(
            figure={
                "data": [
                    {
                        "x": data2.DNS,
                        "y": data2.COUNTRY_NAME,
                        "type": "bar",
                        'orientation':'h',
                        'color':'COUNTRY_NAME',
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