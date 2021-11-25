import sys
import json
from pygraphviz import *

def drawGraph(filename, output='output/graph.png'):
    with open(filename, 'r') as f:
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