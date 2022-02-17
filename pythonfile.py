from dash import dash,html, dcc, Input, Output, State
import plotly.express as px
import requests
import plotly.graph_objects as go
import random
#Requesting API for image data
response = requests.get("https://dog.ceo/api/breeds/image/random")
#Getting the JSON version of the dictionary from the API endpoint
mypath = response.json()

#Beginning dash callout
app = dash.Dash()

#Layout for the image
app.layout = html.Div([
    html.Div([
        html.H1("Random Image Generator"),
#source of the html image keeps changing and thus needs to call the json path every time it is executed
        html.Div([html.Img( src=""+mypath.get("message") ,width="300" ,height="300")]),
#since 'src' will only take URLs,the path requires a random URL each time it is called. Hence +mypath.get() retrieves a unique URL each time it is called.
        html.A(html.Button('Refresh',id='Refresh page',n_clicks=0),href='/'),
        html.Div(id ='sentence-output', children=["Click above to refresh"],style={})
    ])
])
#The following code is to callback the refresh button to get a random photo each time the button is clicked
#If this does not work , running the file again on the local browser will display a new image to confirm that the retrieval works.
@app.callback(
    Output('sentence-output', 'children'),
    Input('Refresh page', 'n_clicks')
)
#This code is essentially a dummy function to provide some functionality for the callback to trigger the refresh.

def valchange(n):
    fig =["Click above to refresh"] #Intentionally made the text the same to trigger the callback.
    return fig

if __name__ == '__main__':
    app.run_server(debug = True)
