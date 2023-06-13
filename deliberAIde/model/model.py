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

    Identify the topics discussed in the discussion transcript, delimited with triple backticks.

    Check the following steps but don't print each step only print what is asked:

    Step 1: Identify the topics discussed in the discussion transcript. Take the time to read the complete transcript, don't
            take words as a whole argument, analyze the complete argument and then decide on the topic.\
    Step 2: Analyze each topic (if there is more than one), and merge those into only one main topic.
            If there are topics that are as important as the main topic, display them as a second topic but only if it is linked to the
    main topic of discussion in the transcript. Only in this case, you can display more topics.\
    Step 3: Extract the statements related to each topic.\
    Step 4: State the necessary main topics of the entire transcript in a concise, descriptive sentence,
            in up to 3 words for each topic.\
    Step 5: Provide the output in a JSON format where the key is the topic and the value is a list of statements made by the
            participants.\

    Review transcript: '''{transcript}'''
    """

    topics = get_completion(prompt_topic)
    topics_json = json.loads(topics)

    return topics_json

# Function for getting completion from OpenAI instructing model to identify viewpoints per topic based on output from get_topics

def get_viewpoints_by_topic(topics,transcript):
    result = {}
    for topic, excerpt in topics.items():
        prompt = f"""
        You are an assistant for group discussions, specialized on keeping track and documenting the discussion,
        that is, the topics discussed, the viewpoints/positions on each topic and the arguments/explanations given in support of each viewpoint.
        For the topic "{topic}"elimited by triple hashtags, analyse the corresponding excerpt from the discussion.
        Your task is to identify all the viewpoints expressed on the topic.

        Proceed according to the following steps:

        Step 1: In the below discussion transcript, delimited by triple backticks,
                locate the excerpt corresponding to the topic and consider the rest
                of the transcript as context for the subsequent steps.
        Step 2: Are there one or several viewpoints being expressed in the excerpt?
                A "viewpoint" refers to "one's perspective of opinion on a particular topic".
        Step 3: If there is only one viewpoint, summarize the viewpoint in 3 keywords max,
                more keywords only if necessary to fully grasp the viewpoint. Viewpoint keywords
                should be expressed as noun phrases that describe the viewpoint in a depersonalized manner.
                For example, instead of “Supports Renewables”, the viewpoint keyword should be “Support for Renewables”.
                Instead of “Believes in Traditional Energy”, the viewpoint keyword should be “Belief in Traditional Energy”.

                If there are several viewpoints, summarize each viewpoint in 3 keywords max, more keywords only if
                necessary to fully grasp the topic. Viewpoint keywords should be expressed as noun phrases that describe
                the viewpoint in a depersonalized manner, as explained in the instruction for one viewpoint.
        Step 4: Disregard viewpoints that are not relevant to the current topic or more relevant to another topic. Only if a viewpoint is equally relevant to multiple topics, include it under all relevant topics.
        Step 5: Identify any linkages between viewpoints that build upon each other or propose solutions to identified issues. For instance, if a viewpoint such as 'Media literacy and critical thinking' is expressed as a solution to the issue identified in another viewpoint like 'Concerns about misinformation', classify it as a sub-viewpoint of the latter. Represent these sub-viewpoints appropriately within the hierarchical structure of the result dictionary.
        Step 6: Identify viewpoints that convey essentially the same stance on the topic. For example, viewpoints like 'Lack of regulation and transparency' and 'Need for better regulation' express similar concerns regarding the need for increased regulation in the domain. In such cases, merge these viewpoints into a single unified viewpoint that encapsulates both perspectives. Ensure this is reflected in the summary of viewpoints in the result dictionary.
        Step 7: Append the topics-dictionary with the identified and summarized viewpoints as sub-keys and the corresponding discussion excerpts as values.Format the dictionary in JSON-format.

        Only include the appended dictionary in your response.

        ```{transcript}```
        """
        viewpoints = get_completion(prompt)
        viewpoints_json = json.loads(viewpoints)
        result.update(viewpoints_json)
    return result


# Function for getting completion from OpenAI instructing model to identify arguments per viewpoint based on output from get_viewpoints_by_topic

def get_arguments_by_viewpoint(viewpoints_by_topic):
    prompt = f"""
        You are an assistant for group discussions, specialized on keeping track and documenting the discussion,
        that is, the topics discussed, the viewpoints and sub-viewpoints on each topic and the arguments/explanations given in support of each viewpoint and sub-viewpoint.
        For the dictionary {viewpoints_by_topic}, delimited by triple # below, loop through each viewpoint and sub-viewpoint to extract the arguments/explanations given in support of each viewpoint and sub-viewpoint from the corresponding discussion excerpt provided as value.
        Your task is to identify all the arguments/explanations given in support of each viewpoint and sub-viewpoint, summarize the arguments/explanations and document them together with the corresponding discussion excerpt.

        Proceed according to the following steps:
        Step 1: Identify all the viewpoints, sub-viewpoints and corresponding discussion excerpts in the dictionary. The keys of the second-level sub-dictionary/dictionaries represent the viewpoints. If there are sub-viewpoints, they are recorded as keys of the third-level sub-dictionaries.
                For example, in the below example, delimited by triple *, 'Powerful tool for engagement','Concerns about misinformation' and 'Echo chambers and bias reinforcement' viewpoints. 'Lack of regulation and transparency' and 'Media literacy and critical thinking' are sub-viewpoints belonging to the viewpoint 'Concerns about misinformation'. 'Participant 1: "The role of social media..." is the excerpt corresponding to the viewpoint 'Powerful tool for engagement'. 'Participant 2: "I agree that social media provides..." is the excerpt corresponding to the sub-viewpoint 'Lack of regulation and transparency.
                    ***{{
                    'Social media in political campaigns': {{
                        'Powerful tool for engagement': 'Participant 1: "The role of social media in political campaigns is a subject that has gained significant attention in recent years. It has become a powerful tool for politicians to engage with voters and spread their message."',
                        'Concerns about misinformation': {{
                            'Lack of regulation and transparency': 'Participant 2: "I agree that social media provides a platform for political candidates to connect with a wider audience and mobilize support. However, the lack of regulation and transparency in political advertising on these platforms is a major issue that needs to be addressed."',
                            'Media literacy and critical thinking': 'Participant 3: "I believe that social media has democratized political discourse and allowed marginalized voices to be heard. It provides a platform for grassroots movements and enables citizens to participate in political discussions like never before. We should focus on educating users about media literacy and critical thinking to combat misinformation."'
                        }},
                        'Echo chambers and bias reinforcement': 'Participant 4: "While social media has its benefits, the algorithms used by these platforms tend to create echo chambers and reinforce existing biases. We need better regulation to ensure that diverse viewpoints are represented and to prevent the manipulation of public opinion through targeted content."'
                        }},
                    'Revamping annual festival': {{
                        'Incorporating local talent': 'Yeah, we can incorporate more local talent, add a stage for local bands.',
                        'Showcasing regional cuisine': 'And more food stalls. Our region is known for its cuisine, we can showcase that.',
                        'Promoting local crafts': 'Festivals are a great place to promote local crafts too. We have a rich tradition here.',
                        'Sustainability focus': 'We should also think about sustainability. We can minimize waste and promote recycling.',
                        'Partnering with local businesses': 'What about partnering with local businesses? They can sponsor the event.',
                        'Family activities': 'And we can organize workshops and competitions for kids. Involving families is important.',
                        'Stronger marketing strategy': 'Finally, we need to get the word out. A stronger marketing strategy maybe?',
                        'Engaging local influencers': 'How about reaching out to local influencers? They can promote the event on social media.'
                        }}***

       Step 2: For each identified viewpoint or sub-viewpoint, extract all the argument given in support of the viewpoint/sub-viewpoint from the corresponding discussion excerpts.
               An "argument" refers to a statement or series of statements in support of a viewpoint expressed on a discussion topic.
               It can consist a series of statements, facts, or any kind of explanation or justification intended to develop or support a point of view.
               It is often structured as follows: a claim backed up with evidence, facts, and examples.

       Step 3: Summarize all the arguments per viewpoint or sub-viewpoint in one to three sentences.Make the summary long enough to capture the full complexity of the argument and make it understandable for an outsider unfamiliar with the discussion, but shorter than the corresponding discussion excerpt. Arguments should be expressed as noun phrases that describe the argument in a depersonalized manner.
               For example, instead of “Argues renewables are bad, because windmills destroy biodiversity”, the argument summary should be “Renewables are bad, because wind farms negatively impact biodiversity”.

        Step 4: Revise the dictionary {viewpoints_by_topic} in the following way:
                - Erase the discussion excerpts corresponding to each viewpoint or sub-viewpoint
                - In place of the erased discussion excerpts, insert a new sub-dictionary with all the argument summaries in support of the respective viewpoint or sub-viewpoint as keys and corresponding discussion excerpts as values.

        Only include the appended dictionary in your response.

        ###{viewpoints_by_topic}###

    """

    arguments = get_completion(prompt)

    prompt = f"""Given the following Python-style dictionary {arguments}, please convert it into a properly
    formatted JSON object.
    """
    arguments_json = get_completion(prompt)
    arguments_json = json.loads(arguments_json)

    return arguments_json
