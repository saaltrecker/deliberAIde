
def json_to_mermaid(output: dict):
    def process_viewpoint(name, viewpoint, parent=None):
        nonlocal counter
        node_id = f"N{counter}"
        counter += 1
        nodes[node_id] = name
        if parent is not None:
            edges.append(f"{parent} --> {node_id}")
        if isinstance(viewpoint, dict):
            for sub_viewpoint, content in viewpoint.items():
                process_viewpoint(sub_viewpoint, content, parent=node_id)

    counter = 0
    nodes = {}
    edges = []
    for topic, viewpoints in output.items():
        topic_id = f"N{counter}"
        nodes[topic_id] = topic
        counter += 1
        for viewpoint, content in viewpoints.items():
            process_viewpoint(viewpoint, content, parent=topic_id)

    mermaid_graph = "graph TB\n"
    for node_id, node_name in nodes.items():
        mermaid_graph += f'  {node_id}[{node_name}]\n'
    for edge in edges:
        mermaid_graph += f'  {edge}\n'
    for i in range(len(edges)):
        mermaid_graph += f"  linkStyle {i} stroke:#2ecd71,stroke-width:2px;\n"
    return mermaid_graph

def dict_to_mermaid(nested_dict, parent_node=None, mermaid_str=''):
    # Base case: if the nested_dict is not a dictionary, return the accumulated string
    if not isinstance(nested_dict, dict):
        return mermaid_str

    # Recursive case: for each item in the dictionary, add a line to the Mermaid string and recurse on the value
    for key, value in nested_dict.items():
        # Create a node name by replacing spaces with underscores (Mermaid node IDs can't have spaces)
        node_name = key.replace(' ', '_')
        
        # If there is a parent node, create an arrow from the parent node to this node
        if parent_node is not None:
            mermaid_str += f'  {parent_node} --> {node_name}\n'
        
        # Recurse on the value, using the current key as the parent node for the next level
        mermaid_str = dict_to_mermaid(value, parent_node=node_name, mermaid_str=mermaid_str)
    
    return mermaid_str