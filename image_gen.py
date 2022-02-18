from dash import dash,html, dcc, Input, Output, State
import plotly.express as px
import requests
import plotly.graph_objects as go
import random

app = dash.Dash()

#Layout for the image
app.layout = html.Div([
    html.Div([
        html.H1("Random Image Generator"),
#source of the html image keeps changing and thus needs to call the json path every time it is executed
        html.Div(id='container', children = []),
        html.A(html.Button('Refresh',id='Refresh page',n_clicks=0),href='/')
    ])
])

@app.callback(
    Output('container', 'children'),
    [Input('Refresh page', 'n_clicks')],
    [State('container','children')]
)

def valchange(n,children):
    response = requests.get("https://dog.ceo/api/breeds/image/random")
    #Getting the JSON version of the dictionary from the API endpoint locally
    mypath= response.json()
    new_div=[]
    new_app = html.Div(
                    children=[
                        (html.Img(src=""+mypath.get('message'),width="300" ,height="300"))
                     ]
)
    new_div.append(new_app)
    return new_div

if __name__ == '__main__':
    app.run_server(debug = True)
