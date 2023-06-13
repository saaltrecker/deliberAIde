import pandas as pd
import openai
import os
import json

openai.api_key = os.environ.get('OPENAI_API_KEY')

# Helper function to get completion from model based on a prompt input; model to be call can be changed for example GTP-3.5-turbo instead of GPT-4

def get_completion(prompt, model="gpt-4"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]

# Function for getting completion from OpenAI instructing model to identify topics based on a discussion transcript

def get_topics(transcript):

    prompt_topic = f"""
    You are an assistant for group discussions, specializing in keeping track of and documenting the discussion,/
    that is, the topics discussed, the viewpoints/positions on each topic, and the arguments/explanations given in support of each viewpoint./

    Identify the one or several main topics discussed in the discussion transcript, delimited with triple backticks. If there are multiple identified topics, but they all center around the same main topic, only record the main topic. Don't record sub-topics.

    Provide the output in JSON-format.
    
    Review transcript: '''{transcript}'''
    """

    topics = get_completion(prompt_topic)
    topics_json = json.loads(topics)

    return topics_json

# Function for getting completion from OpenAI instructing model to identify viewpoints per topic based on output from get_topics

# Function for getting completion from OpenAI instructing model to identify viewpoints per topic based on output from get_topics

def get_viewpoints_by_topic(topics_json,transcript):
    prompt = f"""
    You are an assistant for group discussions, specialized on keeping track and documenting the discussion,
    that is, the topics discussed, the viewpoints/positions on each topic and the arguments/explanations given in support of each viewpoint.
    For each main topic in "{topics_json}", analyse the corresponding excerpt from the below discussion transcript, deliminted by triple backticks.
    Your task is to identify all the viewpoints expressed on the topic.

    Proceed according to the following steps:

    Step 1: Are there one or several viewpoints being expressed in the excerpt?
                A "viewpoint" refers to "one's perspective of opinion on a particular topic".
    Step 2: If there is only one viewpoint, summarize the viewpoint in 3 keywords max,
                more keywords only if necessary to fully grasp the viewpoint. Viewpoint keywords
                should be expressed as noun phrases that describe the viewpoint in a depersonalized manner.
                For example, instead of “Supports Renewables”, the viewpoint keyword should be “Support for Renewables”.
                Instead of “Believes in Traditional Energy”, the viewpoint keyword should be “Belief in Traditional Energy”.

                If there are several viewpoints, summarize each viewpoint in 3 keywords max, more keywords only if
                necessary to fully grasp the topic. Viewpoint keywords should be expressed as noun phrases that describe
                the viewpoint in a depersonalized manner, as explained in the instruction for one viewpoint.
    Step 3: Disregard viewpoints that are not relevant to the current topic or more relevant to another topic. Only if a viewpoint is equally relevant to multiple topics, include it under all relevant topics.
    Step 4: Identify any linkages between viewpoints that build upon each other or propose solutions to identified issues. For instance, if a viewpoint such as 'Media literacy and critical thinking' is expressed as a solution to the issue identified in another viewpoint like 'Concerns about misinformation', classify it as a sub-viewpoint of the latter. Represent these sub-viewpoints appropriately within the hierarchical structure of the result dictionary.
    Step 5: Identify viewpoints that convey essentially the same stance on the topic. For example, viewpoints like 'Lack of regulation and transparency' and 'Need for better regulation' express similar concerns regarding the need for increased regulation in the domain. In such cases, merge these viewpoints into a single unified viewpoint that encapsulates both perspectives. Ensure this is reflected in the summary of viewpoints in the result dictionary.
    Step 6: Append the topics-dictionary with the identified and summarized viewpoints and sub-viewpoints.Format the dictionary in JSON-format with the appropriate keys and sub-keys for topics,viewpoints and sub-viewpoints.

    Only include the appended dictionary in your response.

    ```{transcript}```
    """
    viewpoints = get_completion(prompt)
    viewpoints_json = json.loads(viewpoints)
    return viewpoints_json


# Function for getting completion from OpenAI instructing model to identify arguments per viewpoint based on output from get_viewpoints_by_topic

def get_arguments_by_viewpoint(viewpoints_json, transcript):
    prompt = f"""
        You are an assistant for group discussions, specialized on keeping track and documenting the discussion,
        that is, the topics discussed, the viewpoints and sub-viewpoints on each topic and the arguments/explanations given in support of each viewpoint and sub-viewpoint.
        Loop through each viewpoint and sub-viewpoint {viewpoints_json} and extract the arguments/explanations given in support of each viewpoint and sub-viewpoint from the corresponding excerpt in the below discussion transcript, delimited by triple hashtags.
        Your task is to identify all the arguments/explanations given in support of each viewpoint and sub-viewpoint, summarize the arguments/explanations and document them.

        Proceed according to the following steps:
        Step 1: Identify all the viewpoints and sub-viewpoints in {viewpoints_json}.

        Step 2: For each identified viewpoint and sub-viewpoint, extract all the argument given in support of the viewpoint/sub-viewpoint from the corresponding excerpt in the below discussion transcript.
               An "argument" refers to a statement or series of statements in support of a viewpoint expressed on a discussion topic.
               It can consist a series of statements, facts, or any kind of explanation or justification intended to develop or support a point of view.
               It is often structured as follows: a claim backed up with evidence, facts, and examples.

        Step 3: Summarize all the arguments per viewpoint or sub-viewpoint in one or multiple sentences.Make the summary long enough to capture the full complexity of the argument and make it understandable for an outsider unfamiliar with the discussion, but shorter than the corresponding discussion excerpt. Arguments should be expressed as noun phrases that describe the argument in a depersonalized manner.
               For example, instead of “Argues renewables are bad, because windmills destroy biodiversity”, the argument summary should be “Renewables are bad, because wind farms negatively impact biodiversity”.

        Step 4: Revise the dictionary {viewpoints_json} in the following way:
                - For each viewpoint and sub-viewpoint, insert a new sub-dictionary with all the argument summaries in support of the respective viewpoint or sub-viewpoint. Format the dictionary in JSON-format.

        Only include the appended dictionary in your response.

        ###{transcript}###

    """

    arguments = get_completion(prompt)
    arguments_json = json.loads(arguments)

    return arguments_json