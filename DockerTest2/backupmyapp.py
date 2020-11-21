from flask import Flask, request, render_template
import dash
import dash_html_components as html
import dash_core_components as dcc
import stonkGraph
server = Flask(__name__)

@server.route('/')
def index():
    return render_template('index.html')

app = dash.Dash(
    __name__,
    server=server,
    routes_pathname_prefix='/dash/'
)
fig = stonkGraph.getfig()
app.layout = html.Div(
    dcc.Graph(
        id='basic-interactions',
        figure=fig
    ))
if __name__ == '__main__':
    app.run_server(debug=True, host='0.0.0.0', port=5000)
