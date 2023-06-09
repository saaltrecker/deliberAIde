
def json_to_mermaid(target):
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

topics_json = {
    'Social media in political campaigns': 
        'Participant 1: "The role of social media in political campaigns is a subject that has gained significant attention in recent years. \
            It has become a powerful tool for politicians to engage with voters and spread their message. \
            However, there are concerns about the spread of misinformation and the manipulation of public opinion through targeted ads." \
            Participant 2: "I agree that social media provides a platform for political candidates to connect with a wider audience and mobilize support. \
            However, the lack of regulation and transparency in political advertising on these platforms is a major issue that needs to be addressed." \
            Participant 3: "I believe that social media has democratized political discourse and allowed marginalized voices to be heard. \
            It provides a platform for grassroots movements and enables citizens to participate in political discussions like never before.\
            We should focus on educating users about media literacy and critical thinking to combat misinformation." \
            Participant 4: "While social media has its benefits, the algorithms used by these platforms tend to create echo chambers and reinforce existing biases. \
            We need better regulation to ensure that diverse viewpoints are represented and to prevent the manipulation of public opinion through targeted content."', 
    'Revamping annual festival': 
        'Participant 1: "Our annual festival needs a revamp. The last one didn\'t pull in the crowds." \
            Participant 2: "Yeah, we can incorporate more local talent, add a stage for local bands." \
            Participant 3: "And more food stalls. Our region is known for its cuisine, we can showcase that." Participant 4: "Festivals are a great place to promote local crafts too. We have a rich tradition here." \
            Participant 5: "We should also think about sustainability. We can minimize waste and promote recycling." \
            Participant 6: "What about partnering with local businesses? They can sponsor the event." \
            Participant 7: "And we can organize workshops and competitions for kids. Involving families is important."\
            Participant 8: "Finally, we need to get the word out. A stronger marketing strategy maybe?" \
            Participant 9: "How about reaching out to local influencers? They can promote the event on social media." \
            Participant 10: "It seems we all agree then. More local flavor, sustainability, business partnerships, family activities, and better marketing. Shall we start drafting the plan?"'}

viewpoints_by_topics = {
'Social media in political campaigns': {
    'Powerful tool for engagement': 'Participant 1: "The role of social media in political campaigns is a subject that has gained significant attention in recent years. It has become a powerful tool for politicians to engage with voters and spread their message."',
    'Concerns about misinformation': {
        'Lack of regulation and transparency': 'Participant 2: "I agree that social media provides a platform for political candidates to connect with a wider audience and mobilize support. However, the lack of regulation and transparency in political advertising on these platforms is a major issue that needs to be addressed."',
        'Media literacy and critical thinking': 'Participant 3: "I believe that social media has democratized political discourse and allowed marginalized voices to be heard. It provides a platform for grassroots movements and enables citizens to participate in political discussions like never before. We should focus on educating users about media literacy and critical thinking to combat misinformation."'
    },
    'Echo chambers and bias reinforcement': 'Participant 4: "While social media has its benefits, the algorithms used by these platforms tend to create echo chambers and reinforce existing biases. We need better regulation to ensure that diverse viewpoints are represented and to prevent the manipulation of public opinion through targeted content."'
    },
'Revamping annual festival': {
    'Incorporating local talent': 'Yeah, we can incorporate more local talent, add a stage for local bands.',
    'Showcasing regional cuisine': 'And more food stalls. Our region is known for its cuisine, we can showcase that.',
    'Promoting local crafts': 'Festivals are a great place to promote local crafts too. We have a rich tradition here.',
    'Sustainability focus': 'We should also think about sustainability. We can minimize waste and promote recycling.',
    'Partnering with local businesses': 'What about partnering with local businesses? They can sponsor the event.',
    'Family activities': 'And we can organize workshops and competitions for kids. Involving families is important.',
    'Stronger marketing strategy': 'Finally, we need to get the word out. A stronger marketing strategy maybe?',
    'Engaging local influencers': 'How about reaching out to local influencers? They can promote the event on social media.'
}}

arguments_by_viewpoints = {
'Social media in political campaigns': {
    'Powerful tool for engagement': {
        'Powerful tool for engagement': {
            'Argument 1': 'Social media provides a platform for political candidates to connect with a wider audience and mobilize support.',
            'Argument 2': 'Social media has democratized political discourse, allowing marginalized voices to be heard and enabling citizens to participate in political discussions.',
            'Argument 3': 'Social media can be used to promote events and engage with the local community, as seen in the discussion about the annual festival.'}},
    'Concerns about misinformation': {
        'Lack of regulation and transparency': {
            'Concerns about misinformation': {
                'Lack of regulation and transparency': {
                    'Argument 1': 'The lack of regulation and transparency in political advertising on social media platforms is a major issue that needs to be addressed.',
                    'Argument 2': 'Algorithms used by social media platforms create echo chambers and reinforce existing biases, requiring better regulation to ensure diverse viewpoints and prevent manipulation of public opinion through targeted content.'}}},
        'Media literacy and critical thinking': {
            'Concerns about misinformation': {
                'Argument 1': 'Spread of misinformation and manipulation of public opinion through targeted ads on social media platforms',
                'Excerpt 1': 'Participant 1: "The role of social media in political campaigns is a subject that has gained significant attention in recent years. It has become a powerful tool for politicians to engage with voters and spread their message. However, there are concerns about the spread of misinformation and the manipulation of public opinion through targeted ads."',
                'Argument 2': 'Lack of regulation and transparency in political advertising on social media platforms',
                'Excerpt 2': 'Participant 2: "I agree that social media provides a platform for political candidates to connect with a wider audience and mobilize support. However, the lack of regulation and transparency in political advertising on these platforms is a major issue that needs to be addressed."',
                'Argument 3': 'Algorithms creating echo chambers and reinforcing existing biases',
                'Excerpt 3': 'Participant 4: "While social media has its benefits, the algorithms used by these platforms tend to create echo chambers and reinforce existing biases. We need better regulation to ensure that diverse viewpoints are represented and to prevent the manipulation of public opinion through targeted content."'}}},
    'Echo chambers and bias reinforcement': {
        'Echo chambers and bias reinforcement': {
            'Argument 1': 'Algorithms used by social media platforms create echo chambers and reinforce existing biases, leading to a lack of diverse viewpoints and potential manipulation of public opinion through targeted content.'
    }}},
'Revamping annual festival': {
    'Incorporating local talent': {
        'Incorporating local talent': {
            'Argument 1': 'Adding a stage for local bands to perform',
            'Argument 2': 'Showcasing regional cuisine through food stalls',
            'Argument 3': 'Promoting local crafts and traditions'
        }},
    'Showcasing regional cuisine': {
        'Showcasing regional cuisine': {
            'Argument 1': 'Our region is known for its cuisine, we can showcase that.'
        }},
    'Promoting local crafts': {
        'Promoting local crafts': {
            'Argument 1': 'Festivals are a great place to promote local crafts, as they showcase the rich tradition of the region'
        }},
    'Sustainability focus': {
        'Sustainability focus': {
            'Argument 1': 'Minimizing waste and promoting recycling at the festival'
        }},
    'Partnering with local businesses': {
        'Partnering with local businesses': {
            'Argument 1': 'Local businesses can sponsor the event'
        }},
    'Family activities': {
        'Family activities': {
            'Argument 1': 'Involving families is important, and organizing workshops and competitions for kids can help achieve that (Participant 7)'
        }},
    'Stronger marketing strategy': {
        'Stronger marketing strategy': {
            'Argument 1': 'Reaching out to local influencers to promote the event on social media'
        }},
    'Engaging local influencers': {
        'Engaging local influencers': {
            'Argument 1': 'Local influencers can promote the event on social media'
}}}}

def deliberaide_output(transcript: str): # Mock function, replace with our finished model function
    """This function takes in the transcript and returns a string of the output from our model.
    For our testing purposes of the HTML, it will just return a string saying 'deliberaide is working!'"""
    targets = {'topics': ['topic1', 'topic2', 'topic3'], 
                    'viewpoints': ['viewpoint1', 'viewpoint2', 'viewpoint3'],
                    'arguments': ['arg1', 'arg2', 'arg3']
    }
    return targets

def get_topics(transcript: str):
    return topics_json
def get_viewpoints_by_topic(transcript: str):
    return viewpoints_by_topics
def get_arguments_by_viewpoint(transcript: str):
    return arguments_by_viewpoints