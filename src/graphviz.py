import sys
import json
from pygraphviz import *

import dash
from dash import dcc
from dash import html
import dash_cytoscape as cyto
from dash.dependencies import Input, Output
import plotly.express as px

def drawGraph(filename, output='output/graph.png'):
    """ with open(filename, 'r') as f:
        data = json.load(f)
    
    G = AGraph(data)
    G.node_attr["fontcolor"] = "#FFFFFF"
    G.graph_attr["label"] = "Affecation"

    for institu in data:
        n = G.get_node(institu)
        n.attr['style'] = 'filled'
        n.attr['fillcolor'] = '#2e2c2a'

        for student in data[institu]:
            n = G.get_node(student)
            n.attr['style'] = 'filled'
            n.attr['fillcolor'] = '#e68015'

    G.layout(prog='neato')
    G.draw(output)
    print(f"Fichier '{output}' créer avec succée")
 """
    with open(filename, 'r') as f:
        data = json.load(f)
    app = dash.Dash(__name__)
    
    list_elements = []
    for inst in data:
        dict_i = {'data':{'id' : inst, 'label' : str(inst)}, 'style': {
            'background-color': 'red',
            'line-color': 'red'
        }}
        list_elements.append(dict_i)
        for s in data[inst]:
            dict_s = {'data':{'id' : s, 'label' : str(s)}, 'style': {
            'background-color': 'blue',
            'line-color': 'blue'
        }}
            dict_edge = {'data':{'source' : s, 'target' : inst}}
            list_elements.append(dict_s)
            list_elements.append(dict_edge)

    app.layout = html.Div([
        html.P("Dash Cytoscape:"),
        cyto.Cytoscape(
            id='cytoscape',
            elements=list_elements
                #{'data': {'id': 'ca', 'label': 'Canada'}}
               
            ,
            layout={'name': 'breadthfirst'},
            style={'width': '1920px', 'height': '1080px'}
        )
    ])

    app.run_server(debug=True)
    

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 graphviz.py <filename.csv> <output/dir/>")
        exit(1)
    
    filename = sys.argv[1]
    output_dir = sys.argv[2]
    if output_dir[-1] != '/':
        output_dir += '/'

    output = output_dir + filename.split('/')[-1].split('.')[0] + '.png'
    drawGraph(filename, output=output)