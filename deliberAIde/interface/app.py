# Description: This is our main app functioning as the controller for our web app.
import sys
sys.path.append("../")
#from model.model import get_topics, get_viewpoints_by_topic, get_arguments_by_viewpoint # model functions
from interface.mermaid import json_to_mermaid, dict_to_mermaid, get_topics, get_viewpoints_by_topic, get_arguments_by_viewpoint
from flask import Flask, render_template, request
#from flask_ngrok import run_with_ngrok # !TODO (if we want to make it online and not just local)

app = Flask(__name__) # This is how we create an instance of the Flask class for our app. 

#run_with_ngrok(app)  # !TODO (if we want to make it online and not just local). Starts ngrok when app is run

@app.route('/', methods=['GET', 'POST']) # This is the home page route. This decorator 
                                        # tells Flask what URL should trigger our function (home, in this case).
def home(title='deliberAIde'):
    if request.method == 'POST':
        should_scroll = 'True'
        text = request.form['text'] # input transcript. Pass this text to your model and get the result
        # Filter Checkboxes
        topics_filter = request.form.get('topics') # checkbox topics. Fetches value of the checkbox
        viewpoints_filter = request.form.get('viewpoints') # checkbox viewpoints. 
        arguments_filter = request.form.get('arguments') # checkbox args. 
        
        output = {}
        
        if topics_filter:
            topics = get_topics(text)
            output['topics'] = topics
            mermaid_diagram = dict_to_mermaid(topics)
        if viewpoints_filter:
            viewpoints = get_viewpoints_by_topic(topics, text)
            output['viewpoints'] = viewpoints
            mermaid_diagram = json_to_mermaid(viewpoints)
        if arguments_filter:
            if viewpoints == None: 
                viewpoints = get_viewpoints_by_topic(topics, text)
            arguments = get_arguments_by_viewpoint(viewpoints)
            output['arguments'] = arguments
            mermaid_diagram = json_to_mermaid(arguments)

        # Now return this output in the response
        # You can pass this output to the template and display it
        if not text:
            return render_template('index.html', title=title, 
                                   should_scroll=should_scroll, 
                                   output="Sorry, I didn't detect a transcript. Please try again!")
        if not (topics or viewpoints or arguments):
            return render_template('index.html', title=title, 
                                   should_scroll=should_scroll, 
                                   output="Sorry, it seems you haven't chosen any filters. Please try again!")
        return render_template('index.html', title=title, 
                               should_scroll=should_scroll,
                            #    topics=topics,
                            #    viewpoints=viewpoints,
                            #    arguments=arguments,
                               output=output,
                               mermaid_diagram=mermaid_diagram)
    
     # If it's a GET request, just render the page normally
    should_scroll = 'False'
    return render_template('index.html', title=title)


if __name__ == '__main__':
    app.run(debug=True)
    