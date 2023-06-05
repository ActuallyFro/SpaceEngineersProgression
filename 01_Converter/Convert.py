import json
import re

def generate_json_graph_representation(file_path):
    # Open and read the .puml file
    with open(file_path, 'r') as file:
        lines = file.readlines()

    graph_objects = []
    nodes = {}
    x = 0
    y = 0

    # Iterate over each line in the file
    for line in lines:
        stripped_line = line.strip()

        # Check if the line is a node
        if stripped_line.startswith('+'):
            node_depth = stripped_line.count('+')
            node_name = stripped_line.lstrip('+').strip()
            node_id = re.sub('\s+', '_', node_name)

            nodes[node_depth] = node_id

            if node_depth > 1:
                graph_objects.append({
                    "id": f"{nodes[node_depth-1]}-to-{node_id}",
                    "type": "edge",
                    "renderSettings": [{"labelOffsetX": 0, "labelOffsetY": 0, "fillColor": "black", "labelFontSize": 12, "labelColor": "#aaa"}],
                    "source": nodes[node_depth-1],
                    "sourceId": nodes[node_depth-1],
                    "target": node_name,
                    "targetId": node_id
                })

            graph_objects.append({
                "id": node_id,
                "type": "node",
                "renderSettings": [{"labelOffsetX": 0, "labelOffsetY": 0, "fillColor": "#00b4f0", "labelFontSize": 12, "labelColor": "black", "outlineColor": "black", "radiusSize": 20, "nodeColor": "#00b4f0", "nodeColorOutline": "black", "labelAnchor": "middle"}],
                "label": node_name,
                "properties": [],
                "index": node_depth,
                "x": x,
                "y": y,
                "vy": 0,
                "vx": 0,
                "fx": x,
                "fy": y
            })
            x += 10
            y += 10

    graph_representation = {
        "graphObjects": graph_objects,
        "graphSettingsTitle": "Space Engineers Progression",
        "graphSettingsDirectionality": "undirected",
        "GraphMLXMLData": "",
        "renderSettings": []
    }

    # Write the graph representation to a .json file
    with open('graph_representation.json', 'w') as json_file:
        json.dump(graph_representation, json_file, indent=4)

# Call the function with the path to your .puml file
generate_json_graph_representation('FinalEntriesSpaceEngineers.puml')
