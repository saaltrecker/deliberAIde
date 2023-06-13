# Description: This is our main app functioning as the controller for our web app.
import sys
import json
import time

sys.path.append("../")

#from model.model import get_topics, get_viewpoints_by_topic, get_arguments_by_viewpoint # model functions
from interface.functions.test_data import get_topics, get_viewpoints_by_topic, get_arguments_by_viewpoint # test data functions
from views.button_process import process_mission
from interface.functions.mermaid import json_to_mermaid, dict_to_mermaid
from flask import Flask, render_template, request, redirect, jsonify, Response, stream_with_context
from functions.dict_create import dict_create
#from flask_ngrok import run_with_ngrok # !TODO (if we want to make it online and not just local)

app = Flask(__name__) # This is how we create an instance of the Flask class for our app.

@app.route('/', methods=['GET', 'POST']) # This is the home page route. This decorator
                                        # tells Flask what URL should trigger our function (home, in this case).
def home():
    b_params = dict_create(should_scroll='False', text='', topics_filter=None,
                       viewpoints_filter=None, arguments_filter=None)
    if request.method == 'POST':
        time.sleep(4) # Introduce simulated time delay
        should_scroll = 'True'
        text = request.form['text'] # input transcript. Pass this text to your model and get the result
        # Filter Checkboxes
        topics_filter = request.form.get('topics') # checkbox topics. Fetches value of the checkbox
        viewpoints_filter = request.form.get('viewpoints') # checkbox viewpoints.
        arguments_filter = request.form.get('arguments') # checkbox args.

        output = {}
        mermaid_diagram = None

        b_params = dict_create(should_scroll=should_scroll, text=text, topics_filter=topics_filter,
                                  viewpoints_filter=viewpoints_filter, arguments_filter=arguments_filter)


        if not text: # if no text is entered, return an error message saying input transcript
            return render_template('main.html', b_params=b_params,
                                   output="Sorry, I didn't detect a transcript. Please try again!")

        if not (topics_filter or viewpoints_filter or arguments_filter): # if no filters are selected, return an error message saying select a filter
            return render_template('main.html', b_params=b_params,
                                   output="Sorry, it seems you haven't chosen any filters. Please try again!")

        if topics_filter:
            #if not topics:
                try:
                    topics = get_topics(text)
                    output['topics'] = topics
                except Exception as e:
                    return render_template('main.html', b_params=b_params,
                           error_message=f'Error getting topics: {str(e)}')

        if viewpoints_filter:
           # if not viewpoints:
                try:
                    viewpoints = get_viewpoints_by_topic(topics, text)
                    output['viewpoints'] = viewpoints
                    mermaid_diagram = json_to_mermaid(viewpoints)
                except Exception as e:
                    return render_template('main.html', b_params=b_params, error_message=f'Error getting viewpoints: {str(e)}')

        if arguments_filter:
            try:
                if not viewpoints:
                    viewpoints = get_viewpoints_by_topic(topics, text)
                arguments = get_arguments_by_viewpoint(viewpoints)
                output['arguments'] = arguments
                mermaid_diagram = json_to_mermaid(arguments)
            except Exception as e:
                return render_template('main.html', b_params=b_params, error_message=f'Error getting arguments: {str(e)}')

        # Now return this output in the response
        # You can pass this output to the template and display it
        return render_template('main.html', b_params=b_params,
                               output=output,
                               mermaid_diagram=mermaid_diagram)

    # If it's a GET request, just render the page normally
    #should_scroll = 'False'
    return render_template('main.html',  b_params=b_params, output={})


@app.route('/use', methods=['GET', 'POST']) # This is the use route.
def use():
    return render_template('use.html')


@app.route('/mission', methods=['GET', 'POST']) # This is the mission route.
def mission():
    b_params = dict_create(should_scroll='False', text='', topics_filter=None,
                       viewpoints_filter=None, arguments_filter=None)
    return render_template('mission.html', b_params=b_params, output={})

@app.route('/process_mission', methods=['POST'])
def process_mission2():
    return process_mission()


if __name__ == '__main__':
    app.run(debug=True)
