import fastapi
import requests
#from api.temp_functions import get_completion,get_viewpoints_by_topic,json_to_tree,json_to_mermaid
import json
app = fastapi.FastAPI()

##run this file with uvicorn app:app --reload
###No functions are yet used. all the functions are mocked and return a string.
@app.get('/')
def index():
    return {
    'greeting': 'Hello'
    }


@app.get('/deliber')
def get_deliber():
    return {'topics':'topics1','viewpoints':'viewpoints1','tree':'tree1'}


@app.get('/topics')
def get_deliberAIde():
    transcript = f"""
    Participant 1: "The role of social media in political campaigns is a subject that has gained significant attention in recent years. It has become a powerful tool for politicians to engage with voters and spread their message. However, there are concerns about the spread of misinformation and the manipulation of public opinion through targeted ads." Participant 2: "I agree that social media provides a platform for political candidates to connect with a wider audience and mobilize support. However, the lack of regulation and transparency in political advertising on these platforms is a major issue that needs to be addressed." Participant 3: "I believe that social media has democratized political discourse and allowed marginalized voices to be heard. It provides a platform for grassroots movements and enables citizens to participate in political discussions like never before. We should focus on educating users about media literacy and critical thinking to combat misinformation." Participant 4: "While social media has its benefits, the algorithms used by these platforms tend to create echo chambers and reinforce existing biases. We need better regulation to ensure that diverse viewpoints are represented and to prevent the manipulation of public opinion through targeted content."
    Participant 1: "What are we gonna do about the rising population? We can't keep up."  Participant 2: "We could start by improving our public services, specifically health and education." Participant 3: "I think immigration policies should be stricter. There are too many people coming in."  Participant 4: "Wait, but what if we focus on creating more jobs? More people means more workforce." Participant 5: "Let's not forget about housing. We need more and affordable homes." Participant 6: "The environment! We can't ignore the impact of population growth on nature." Participant 7: "What about promoting family planning programs? It has worked in some countries."
    """
    # prompt = f"""
    # You are an assistant for group discussions, specialized on keeping track and documenting the discussion,/
    # that is, the topics discussed, the viewpoints/positions on each topic and the arguments/explanations given in support of each viewpoint./
    # Identify the topics discussed in the discussion transcript, delimited with triple backticks.
    # Proceed in the following steps:

    # Step 1: Are there one or several topics being discussed the transcript? A discussion topic refers to "the subject being talked about".
    # Step 2: If there is only one discussion topic, summarize the topic in 1 keyword, or more if necessary. Create a dictionary with the identified and summarized topic as key and the transcript as value.
    #     Format the dictionary in JSON-format.
    #     If there are several discussion topics, summarize each topic in 1 keyword, or more if necessary. Create a dictionary with all the identified and summarized topics as keys and the corresponding excerpts from the transcript as value.
    #     Format the dictionary in JSON-format.
    # Only include the dictionary in your response.
    # ```{transcript}```
    # """
#print(topics_json)
    return {'topics':'topics1','topics2':'topics2'}

@app.get('/viewpoints')
def get_viewpoints_by_topic_sample():
    result = {}
    topics={'topic1': 'viewpoints from topics', 'topic2': 'viewpoints from topics'}
    return topics

@app.get('/tree')
def json_to_tree_sample():
    print('tres')
    return {'tree':'tree1'}
