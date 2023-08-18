# deliberAIde

![deliberAIde](./deliberAIde/interface/static/images/logo_deliberAIde.png)

## Description

__deliberAIde__ is a deliberation assistant for situations where one wishes to promote more inclusive and effective decision-making. The initial prototype, developed over 1 week, utilizes GPT-4 and prompt-engineering in handling a discussion transcript and performing topic, argument, and viewpoint analysis. It utilizes Flask API and a very simple HTML/JS/CSS UI to display the summarization results into a mermaid minmap.

We intend to continue further developing deliberAIde over the coming months, to include features such as real-time audio transcription, improved data visualization, conflict analysis, and more intuitive UI/UX.
​
If you are interested in getting involved in the deliberAIde project, please reach out to one of the developers.

## Project Status

deliberAIde is ongoing and in its early stages. If you have suggestions for features you would like to see, please reach out to our team!
​
Future features potentially include:
​
- Real-time audio transcription
- Improved data visualization
- Discourse mapping
- Analysis of agreements and conflicts (automated Deliberative Policy Analysis)
- Tracking the deliberative quality
- A moderation feature to flag potentially harmful content
​

## Requirements

A list of required packages is found in the `requirements.txt` file. Shown below:

    openai
    flask
    flask_socketio
    gunicorn
    pandas
    python-dotenv

## Installation and Use

One can download and run **deliberAIde** locally with your own openAPI key. Alternatively, future prototypes will be deployed on our [website](https://deliberaide.com), which is currently inactive. Bookmark it for later 😉

## Known Bugs

- The model effectively summarizes a transcript into it's topic(s), viewpoints, and arguments, however inconsistently builds the JSON output. Consistent JSON formation is to be improved in the next update.
- Difficulty in handling multiple topics of discussion.

## FAQ

To be updated as questions are received.

### Why deliberAIde?

Data indicates a decline in inclusiveness and equal participation in political processes in democratic countries. Deliberative democracy formats like citizen assemblies have been gaining popularity as a solution, but still face barriers to inclusivity, participation, and consensus-building. This is where deliberAIde comes in. deliberAIde's mission is to create as an AI-powered tool to assist moderation and participation within deliberative decision-making processes like citizen assemblies, in order to empower inclusive and effective policy decisions. It closes remaining gaps through real-time transcription, translation, language simplification and visualization so everyone can engage, while AI-powered conflict analysis enhances mutual understanding and consensus-building. By enabling efficient information processing and facilitating comprehension, deliberAIde strengthens inclusion, equal participation and effective conflict resolution in deliberative forums. 

Our goal as a non-profit democracy-tech company is to make participatory decision-making more inclusive, effective, and sustainable. Although conceptualized for deliberative assemblies, deliberAIde's application is wider, from business to civil society. deliberAIde ensures all voices are heard for truly equal and inclusive decisions - from corporate board rooms to community town halls.

## Copyright and licensing information

All rights reserved. We are working on the way we will (open-source) license our product.
