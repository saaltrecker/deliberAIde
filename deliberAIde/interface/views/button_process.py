# Description: This is our main app functioning as the controller for our web app.
import sys
import json
import time
sys.path.append("../")
#from model.model import get_topics, get_viewpoints_by_topic, get_arguments_by_viewpoint # model functions
from interface.functions.test_data import get_topics, get_viewpoints_by_topic, get_arguments_by_viewpoint # test data functions
from interface.functions.mermaid import json_to_mermaid, dict_to_mermaid
from functions.dict_create import dict_create
from flask import Flask, request, jsonify, Response, stream_with_context

def process_mission():
    def generate():
        data = request.get_json()  # get the data from the request
        text = data['text']
        topics_filter = data.get('topics', False)
        viewpoints_filter = data.get('viewpoints', False)
        arguments_filter = data.get('arguments', False)
        should_scroll = 'True'

        b_params = dict_create(should_scroll=should_scroll, text=text, topics_filter=topics_filter, 
                                  viewpoints_filter=viewpoints_filter, arguments_filter=arguments_filter)

        if topics_filter:
            try:
                time.sleep(2)
                topics = get_topics(text)
                print('fetching topics was successful')
                yield f'data: {json.dumps({"topics": topics})}\n\n'  # Send topics
            except Exception as e:
                yield f'data: {json.dumps({"error": f"Error getting topics: {str(e)}"})}\n\n'  # Send error

        if viewpoints_filter:
            try:
                time.sleep(2)
                viewpoints = get_viewpoints_by_topic(topics, text)
                yield f'data: {json.dumps({"viewpoints": viewpoints})}\n\n'  # Send viewpoints
            except Exception as e:
                yield f'data: {json.dumps({"error": f"Error getting viewpoints: {str(e)}"})}\n\n'  # Send error

        if arguments_filter:
            try:
                if not viewpoints: 
                    viewpoints = get_viewpoints_by_topic(topics, text)
                time.sleep(2)
                arguments = get_arguments_by_viewpoint(viewpoints)
                yield f'data: {json.dumps({"arguments": arguments})}\n\n'  # Send arguments
            except Exception as e:
                yield f'data: {json.dumps({"error": f"Error getting arguments: {str(e)}"})}\n\n'  # Send error
    
    return Response(stream_with_context(generate()), mimetype='text/event-stream')
