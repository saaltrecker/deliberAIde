# Description: This is our main app functioning as the controller for our web app.
import sys
import time

sys.path.append("../")

#from deliberAIde.model.model import get_topics, get_viewpoints_by_topic, get_arguments_by_viewpoint # model functions
#from deliberAIde.interface.functions.test_data import get_topics, get_viewpoints_by_topic, get_arguments_by_viewpoint # test data functions
#from deliberAIde.interface.functions.dict_create import dict_create
#from deliberAIde.interface.functions.mermaid import topics_json_to_mermaid_mindmap, views_json_to_mermaid_mindmap, args_json_to_mermaid_mindmap
from functions.test_data import get_topics, get_viewpoints_by_topic, get_arguments_by_viewpoint # test data functions
from functions.dict_create import dict_create
from functions.mermaid import topics_json_to_mermaid_mindmap, views_json_to_mermaid_mindmap, args_json_to_mermaid_mindmap


from flask import Flask, render_template#, request, redirect, jsonify, Response, stream_with_context
from flask_socketio import SocketIO, emit

app = Flask(__name__) # This is how we create an instance of the Flask class for our app.
app.config['SECRET_KEY'] = '125r053'
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/', methods=['GET', 'POST']) # This is the home page route. This decorator
                                        # tells Flask what URL should trigger our function (home, in this case).
def home():
    b_params = dict_create(should_scroll='False', text='', topics_filter=None,
                       viewpoints_filter=None, arguments_filter=None)
    return render_template('main.html',  b_params=b_params, output={})

@socketio.on('button_called')
def handle_button_called(data):
    start_time = time.time() #TODO: Comment out this time tracker
    text = data['text']
    topics_filter = data.get('topics', False)
    viewpoints_filter = data.get('viewpoints', False)
    arguments_filter = data.get('arguments', False)

    print(f"HERE ARE THE DATA: {data}")
    if topics_filter:
        try:
            socketio.sleep(1) #TODO: Remove this sleep
            topics = get_topics(text)
            print(f"TOPICS COLLECTED: {topics}")

            #emit('update', {"topics": topics})  # Send topics

            emit('update', {"topics_mindmap": topics_json_to_mermaid_mindmap(topics),
                            "viewpoints_filter": viewpoints_filter,
                            "arguments_filter": arguments_filter})  # Send topics mermaid diagram

            print("Here is the diagram code: ", topics_json_to_mermaid_mindmap(topics)) # Checking
            print("--- %s seconds ---" % (time.time() - start_time)) #TODO: Comment out this time tracker

        except Exception as e:
            emit('error', {"error": f"Error getting topics: {str(e)}"})  # Send error

    if viewpoints_filter:
        try:
            socketio.sleep(2) #TODO: Remove this sleep
            viewpoints = get_viewpoints_by_topic(topics, text)
            print(f"VIEWS COLLECTED: {viewpoints}")

            #emit('update', {"viewpoints": viewpoints})  # Send viewpoints

            emit('update', {"viewpoints_mindmap": views_json_to_mermaid_mindmap(viewpoints),
                            "arguments_filter": arguments_filter})  # Send viewpoints mermaid diagram

            print("--- %s seconds ---" % (time.time() - start_time)) #TODO: Comment out this time tracker

        except Exception as e:
            emit('error', {"error": f"Error getting viewpoints: {str(e)}"})  # Send error

    if arguments_filter:
        try:
            if not viewpoints:
                viewpoints = get_viewpoints_by_topic(topics, text)
            socketio.sleep(3) #TODO: Remove this sleep
            arguments = get_arguments_by_viewpoint(viewpoints, text)
            print(f"ARGS COLLECTED: {arguments}")
            #emit('update', {"arguments": arguments})  # Send arguments
            emit('update', {"arguments_mindmap": args_json_to_mermaid_mindmap(arguments)})  # Send arguments mermaid diagram

            print("Here is the diagram code: ", args_json_to_mermaid_mindmap(arguments)) # Checking
            print("--- %s seconds ---" % (time.time() - start_time)) #TODO: Comment out this time tracker
        except Exception as e:
            emit('error', {"error": f"Error getting arguments: {str(e)}"})  # Send error


@app.route('/use', methods=['GET', 'POST']) # This is the use route.
def use():
    return render_template('use.html')


@app.route('/mission', methods=['GET', 'POST']) # This is the mission route.
def mission():
    return render_template('mission.html')

if __name__ == '__main__':
    #socketio.run(app, host="0.0.0.0", port=sys.argv[1], allow_unsafe_werkzeug=True)
    socketio.run(app)
