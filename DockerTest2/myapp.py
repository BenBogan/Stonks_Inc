from flask import Flask, request, render_template
import dash
import dash_html_components as html
import dash_core_components as dcc
import stonkGraph

app = dash.Dash(__name__)
fig = stonkGraph.getfig()
app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='''
        Dash: A web application framework for Python.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])
# app.layout = html.Div(
#     dcc.Graph(
#         id='basic-interactions',
#         figure=fig
#     ))
if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0', port=5000)
