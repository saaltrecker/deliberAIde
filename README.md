# deliberAIde

![deliberAIde](./deliberAIde/interface/static/images/logo_deliberAIde.png)

## Description

deliberAIde is a deliberation assistant for situations where one wishes to promote equitable decision-making. The initial prototype, developed over 1 week, utilizes GPT-4 and prompt-engineering in handling a discussion transcript and performing topic, argument, and viewpoint analysis. It utilizes Flask API and a very simple HTML/JS/CSS UI to display the summarization results into a mermaid diagram.

We intend to continue further developing deliberAIde over the coming months, to include features such as real-time audio transcription, improved data visualization, sentiment analysis, and smoother UI/UX.

If you are interested in getting involved in the deliberAIde project, please reach out to one of the developers.

## Project Status

deliberAIde is ongoing and in it's early stages. If you have suggestions for features you would like to see, please reach out to our team!

Future features potentially include:

- Real-time audio transcription
- Improved data visualization
- Discourse mapping
- Analysis of agreements and conflicts (DPA)
- Tracking the deliberative quality
- A moderation feature to flag potentially harmful content

## Requirements

A list of required packages is found in the `requirements.txt` file. Shown below:

    openai
    flask
    flask_socketio
    gunicorn
    pandas
    python-dotenv


## Installation and Use

One can download and run **deliberAIde** locally with an openAPI key. Alternatively, future prototypes will be deployed on our [website](https://deliberaide.com), which is currently inactive. Bookmark it for later 😉

## Known Bugs

- The model effectively summarizes a transcript into it's topic(s), viewpoints, and arguments, however inconsistently builds the JSON output. Consistent JSON formation is to be improved in the next update.
- Difficulty in handling multiple topics of discussion.

## FAQ

To be updated as questions are received.
### Why deliberAIde?

deliberAIde was created as a tool to improve moderation within the context of deliberative assemblies, such as those seen in Ireland or Iceland in the past decades. We wish to empower minority voices to ensure everyone is heard, when crucial policy decisions can be taken that will affect their lives. Within the political atmosphere, this tool serves as a means to enhance the inclusion and engagement of participants, promote mutual understanding, facilitate effective decision-making, and bridge the gap between large-scale involvement and in-depth deliberations. By enabling efficient information processing and facilitating the selection of discursive representatives, deliberAIde strengthens the democratic process for governing AI. Our ultimate goal is to establish deliberAIde as the foundation of a non-profit democracy-tech company committed to making participatory decision-making more inclusive, scalable, and sustainable.

Although deliberAIde was initially conceptualized as a tool within deliberative assemblies, it's application goes wider than the political arena. One can imagine its use in union meetings, business engagements, within legal sessions, or at the local sports club. Whenever one wants to make truly equal and inclusive decisions, deliberAIde is there for you.

## Copyright and licensing information

This project is licensed under the terms of the GNU Affero General Public License v3.0. Please see the `LICENSE.txt` for specific details.