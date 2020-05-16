import plotly.figure_factory as ff
import plotly.graph_objects as go
import pandas as pd

df = pd.read_csv('data/data.csv')

gantt = ff.create_gantt(df, index_col='Domain', show_colorbar=True)

with open('data/table_description.md', 'r') as f:
    mkdn = f.read()

import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()
app.layout = html.Div([
    dcc.Graph(figure=gantt),
    dcc.Markdown(children=mkdn)
])

app.run_server(debug=True, use_reloader=False)


if __name__ == '__main__':
    app.run_server(debug=True)