# Description: This is our main app functioning as the controller for our web app.
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify, session
#from flask_ngrok import run_with_ngrok
from model import deliberaide_output # !TODO replace with our model eventually

app = Flask(__name__) # This is how we create an instance of the Flask class for our app.
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/' 
#run_with_ngrok(app)  # !TODO (if we want to make it online and not just local). Starts ngrok when app is run

@app.route('/', methods=['GET', 'POST']) # This is the home page route. This decorator tells Flask what URL should trigger our function (home, in this case).
def home(title='deliberAIde'):
    if request.method == 'POST':
        session['scroll_to_output'] = True # Set the flag
        
        text = request.form['text'] # input transcript. Pass this text to your model and get the result
        # Filter Checkboxes
        topics = request.form.get('topics') # checkbox topics. Fetches value of the checkbox
        viewpoints = request.form.get('viewpoints') # checkbox viewpoints. 
        arguments = request.form.get('arguments') # checkbox args. 
        
        model_out = deliberaide_output(text) # !TODO replace with our model eventually
        
        final_output = {}
        
        if topics:
            final_output['topics'] = model_out.get('topics')
        if viewpoints:
            final_output['viewpoints'] = model_out.get('viewpoints')
        if arguments:
            final_output['arguments'] = model_out.get('arguments')
            
        output = final_output

        # Now return this output in the response
        # You can pass this output to the template and display it
        if not text:
            should_scroll = session.pop('scroll_to_output', False)
            return render_template('index.html', title=title, 
                                   should_scroll=should_scroll, output="Sorry, I didn't detect a transcript. Please try again!")
        if not (topics or viewpoints or arguments):
            should_scroll = session.pop('scroll_to_output', False)
            return render_template('index.html', title=title, 
                                   should_scroll=should_scroll, output="Sorry, it seems you haven't chosen any filters. Please try again!")
        
        should_scroll = session.pop('scroll_to_output', False)
        return render_template('index.html', title=title, 
                               should_scroll=should_scroll, output=output)
    
     # If it's a GET request, just render the page normally
    return render_template('index.html', title=title)


if __name__ == '__main__':
    app.run(debug=True)
    