import openai
import os
import json
from anytree import Node, RenderTree

openai.api_key  = os.environ.get('API_KEY')
def get_completion(prompt, model="gpt-4"):
    """messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
    )"""
    return {'here is a processef prompt' : "expected gtp response"}#response.choices[0].message["content"]
transcript = f"""
Participant 1: "The role of social media in political campaigns is a subject that has gained significant attention in recent years. It has become a powerful tool for politicians to engage with voters and spread their message. However, there are concerns about the spread of misinformation and the manipulation of public opinion through targeted ads." Participant 2: "I agree that social media provides a platform for political candidates to connect with a wider audience and mobilize support. However, the lack of regulation and transparency in political advertising on these platforms is a major issue that needs to be addressed." Participant 3: "I believe that social media has democratized political discourse and allowed marginalized voices to be heard. It provides a platform for grassroots movements and enables citizens to participate in political discussions like never before. We should focus on educating users about media literacy and critical thinking to combat misinformation." Participant 4: "While social media has its benefits, the algorithms used by these platforms tend to create echo chambers and reinforce existing biases. We need better regulation to ensure that diverse viewpoints are represented and to prevent the manipulation of public opinion through targeted content."
Participant 1: "What are we gonna do about the rising population? We can't keep up."  Participant 2: "We could start by improving our public services, specifically health and education." Participant 3: "I think immigration policies should be stricter. There are too many people coming in."  Participant 4: "Wait, but what if we focus on creating more jobs? More people means more workforce." Participant 5: "Let's not forget about housing. We need more and affordable homes." Participant 6: "The environment! We can't ignore the impact of population growth on nature." Participant 7: "What about promoting family planning programs? It has worked in some countries."
"""

#Old fake prompt
prompt = f"""
You are an assistant for group discussions, specialized on keeping track and documenting the discussion,/
that is, the topics discussed, the viewpoints/positions on each topic and the arguments/explanations given in support of each viewpoint./
Identify the topics discussed in the discussion transcript, delimited with triple backticks.
Proceed in the following steps:

Step 1: Are there one or several topics being discussed the transcript? A discussion topic refers to "the subject being talked about".
Step 2: If there is only one discussion topic, summarize the topic in 1 keyword, or more if necessary. Create a dictionary with the identified and summarized topic as key and the transcript as value.
        Format the dictionary in JSON-format.
        If there are several discussion topics, summarize each topic in 1 keyword, or more if necessary. Create a dictionary with all the identified and summarized topics as keys and the corresponding excerpts from the transcript as value.
        Format the dictionary in JSON-format.
Only include the dictionary in your response.
```{transcript}```
"""

topics = get_completion(prompt)
#topics_json = json.loads(topics)
#print(topics_json)
#print(topics_json.keys())
#topics_json.keys()
def get_viewpoints_by_topic(topics,transcript):
    result = {}
    topics={'topic1': 'excerpt1', 'topic2': 'excerpt2',
            'topic3': 'excerpt3', 'topic4': 'excerpt4'}
    transcript = f"this is an exaple transcript"
    """for topic, excerpt in topics.items():
        viewpoints = get_completion(prompt)
        viewpoints_json = json.loads(viewpoints)
        result.update(viewpoints_json)"""
    result = {'viewpoint1': 'content1', 'viewpoint2': 'content2'}
    return result
#viewpoints_by_topics = get_viewpoints_by_topic(topics_json,transcript)
def json_to_tree(viewpoints_by_topics):
    def process_viewpoint(name, viewpoint, parent=None):
        node = Node(name, parent=parent)
        if isinstance(viewpoint, dict):
            for sub_viewpoint, content in viewpoint.items():
                process_viewpoint(sub_viewpoint, content, parent=node)
        return node

    for topic, viewpoints in viewpoints_by_topics.items():
        topic_node = Node(topic)
        for viewpoint, content in viewpoints.items():
            process_viewpoint(viewpoint, content, parent=topic_node)
        for pre, _, node in RenderTree(topic_node):
            print("%s%s" % (pre, node.name))
    return topic_node

print(get_viewpoints_by_topic(topics,transcript))

#json_to_tree(viewpoints_by_topics)
def json_to_mermaid(viewpoints_by_topics):
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
    for topic, viewpoints in viewpoints_by_topics.items():
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

print(json_to_mermaid(get_viewpoints_by_topic(topics,transcript)))
