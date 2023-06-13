# Description: This is our main app functioning as the controller for our web app.
import sys
import time

sys.path.append("../")

#from model.model import get_topics, get_viewpoints_by_topic, get_arguments_by_viewpoint # model functions
from interface.functions.test_data import get_topics, get_viewpoints_by_topic, get_arguments_by_viewpoint # test data functions
#from interface.functions.mermaid import json_to_mermaid

from flask import Flask, render_template#, request, redirect, jsonify, Response, stream_with_context
from flask_socketio import SocketIO, emit

from functions.dict_create import dict_create

app = Flask(__name__) # This is how we create an instance of the Flask class for our app.
app.config['SECRET_KEY'] = '125r053'
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/', methods=['GET', 'POST']) # This is the home page route. This decorator
                                        # tells Flask what URL should trigger our function (home, in this case).
def home():
    b_params = dict_create(should_scroll='False', text='', topics_filter=None,
                       viewpoints_filter=None, arguments_filter=None)
    # if request.method == 'POST':
    #     start = time.process_time()
    #     #time.sleep(4) # Introduce simulated time delay
    #     should_scroll = 'True'
    #     text = request.form['text'] # input transcript. Pass this text to your model and get the result
    #     # Filter Checkboxes
    #     topics_filter = request.form.get('topics') # checkbox topics. Fetches value of the checkbox
    #     viewpoints_filter = request.form.get('viewpoints') # checkbox viewpoints.
    #     arguments_filter = request.form.get('arguments') # checkbox args.

    #     output = {}
    #     mermaid_diagram = None

    #     b_params = dict_create(should_scroll=should_scroll, text=text, topics_filter=topics_filter,
    #                               viewpoints_filter=viewpoints_filter, arguments_filter=arguments_filter)


    #     if not text: # if no text is entered, return an error message saying input transcript
    #         return render_template('main.html', b_params=b_params,
    #                                output="Sorry, I didn't detect a transcript. Please try again!")

    #     if not (topics_filter or viewpoints_filter or arguments_filter): # if no filters are selected, return an error message saying select a filter
    #         return render_template('main.html', b_params=b_params,
    #                                output="Sorry, it seems you haven't chosen any filters. Please try again!")

    #     if topics_filter:
    #         #if not topics:
    #             try:
    #                 topics = get_topics(text)
    #                 output['topics'] = topics
    #                 #print(output)
    #                 print(time.process_time() - start)
    #             except Exception as e:
    #                 return render_template('main.html', b_params=b_params,
    #                        error_message=f'Error getting topics: {str(e)}')

    #     if viewpoints_filter:
    #        # if not viewpoints:
    #             try:
    #                 viewpoints = get_viewpoints_by_topic(topics, text)
    #                 output['viewpoints'] = viewpoints
    #                 mermaid_diagram = json_to_mermaid(viewpoints)
    #                 print('views have been collected')
    #                 print(time.process_time() - start)
    #             except Exception as e:
    #                 return render_template('main.html', b_params=b_params, error_message=f'Error getting viewpoints: {str(e)}')

    #     if arguments_filter:
    #         try:
    #             if not viewpoints:
    #                 viewpoints = get_viewpoints_by_topic(topics, text)
    #             arguments = get_arguments_by_viewpoint(viewpoints, text)
    #             output['arguments'] = arguments
    #             mermaid_diagram = json_to_mermaid(arguments)
    #             print(output)
    #             print(time.process_time() - start)
    #         except Exception as e:
    #             return render_template('main.html', b_params=b_params, error_message=f'Error getting arguments: {str(e)}')

    #     # Now return this output in the response
    #     # You can pass this output to the template and display it
    #     return render_template('main.html', b_params=b_params,
    #                            output=output,
    #                            mermaid_diagram=mermaid_diagram)

    # # If it's a GET request, just render the page normally
    # #should_scroll = 'False'
    return render_template('main.html',  b_params=b_params, output={})

@socketio.on('button_called')
def handle_button_called(data):
    start_time = time.time()
    text = data['text']
    topics_filter = data.get('topics', False)
    viewpoints_filter = data.get('viewpoints', False)
    arguments_filter = data.get('arguments', False)
    should_scroll = 'True'
    
    #b_params = dict_create(should_scroll=should_scroll, text=text, topics_filter=topics_filter, 
                            #viewpoints_filter=viewpoints_filter, arguments_filter=arguments_filter)
    
    print(f"HERE ARE THE DATA: {data}")
    if topics_filter:
        try:
            #socketio.sleep(2)
            topics = get_topics(text)
            print(f"TOPICS COLLECTED: {topics}")
            emit('update', {"topics": topics})  # Send topics
            print("--- %s seconds ---" % (time.time() - start_time))
        except Exception as e:
            emit('error', {"error": f"Error getting topics: {str(e)}"})  # Send error

    if viewpoints_filter:
        try:
            #socketio.sleep(2)
            viewpoints = get_viewpoints_by_topic(topics, text)
            print(f"VIEWS COLLECTED: {viewpoints}")
            emit('update', {"viewpoints": viewpoints})  # Send viewpoints
            print("--- %s seconds ---" % (time.time() - start_time))
        except Exception as e:
            emit('error', {"error": f"Error getting viewpoints: {str(e)}"})  # Send error
            
    if arguments_filter:
        try:
            if not viewpoints: 
                viewpoints = get_viewpoints_by_topic(topics, text)
            #socketio.sleep(2)
            arguments = get_arguments_by_viewpoint(viewpoints, text)
            print(f"ARGS COLLECTED: {arguments}")
            emit('update', {"arguments": arguments})  # Send arguments
            print("--- %s seconds ---" % (time.time() - start_time))
        except Exception as e:
            emit('error', {"error": f"Error getting arguments: {str(e)}"})  # Send error


@app.route('/use', methods=['GET', 'POST']) # This is the use route.
def use():
    return render_template('use.html')


@app.route('/mission', methods=['GET', 'POST']) # This is the mission route.
def mission():
    return render_template('mission.html')

if __name__ == '__main__':
    socketio.run(app)
    
