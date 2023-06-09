# Description: This is our main app functioning as the controller for our web app.
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify, session
#from flask_ngrok import run_with_ngrok
from model import json_to_mermaid, get_topics, get_viewpoints_by_topic, get_arguments_by_viewpoint # !TODO replace with our model eventually
from model import viewpoints_by_topics
#TODO: Clean up imports

app = Flask(__name__) # This is how we create an instance of the Flask class for our app. 

#run_with_ngrok(app)  # !TODO (if we want to make it online and not just local). Starts ngrok when app is run

@app.route('/', methods=['GET', 'POST']) # This is the home page route. This decorator 
                                        # tells Flask what URL should trigger our function (home, in this case).
def home(title='deliberAIde'):
    if request.method == 'POST':
        should_scroll = 'True'
        text = request.form['text'] # input transcript. Pass this text to your model and get the result
        # Filter Checkboxes
        topics = request.form.get('topics') # checkbox topics. Fetches value of the checkbox
        viewpoints = request.form.get('viewpoints') # checkbox viewpoints. 
        arguments = request.form.get('arguments') # checkbox args. 
        
        #model_out = deliberaide_output(text) # !TODO replace with our model eventually
        
        final_output = {}
        
        if topics:
            #final_output['topics'] = model_out.get('topics')
            final_output['topics'] = get_topics(text)
            mermaid_diagram = json_to_mermaid(final_output['topics'])
        if viewpoints:
            #final_output['viewpoints'] = model_out.get('viewpoints')
            final_output['viewpoints'] = get_viewpoints_by_topic(text)
            mermaid_diagram = json_to_mermaid(final_output['viewpoints'])
        if arguments:
            #final_output['arguments'] = model_out.get('arguments')
            final_output['arguments'] = get_arguments_by_viewpoint(text)
            mermaid_diagram = json_to_mermaid(final_output['arguments'])
            
        output = final_output

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
                               output=output,
                               mermaid_diagram=mermaid_diagram)
    
     # If it's a GET request, just render the page normally
    should_scroll = 'False'
    return render_template('index.html', title=title)


if __name__ == '__main__':
    app.run(debug=True)
    