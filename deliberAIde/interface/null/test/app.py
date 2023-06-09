from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False) # holds each task, 200 char, 
    date_created = db.Column(db.DateTime, default=datetime.utcnow) # anytime a new to-do is created, holds date/time task was created

    def __repr__(self):
        return '<Task %r>' % self.id

with app.app_context():
    db.create_all()
    
@app.route('/', methods=['POST', 'GET']) # Adding two methods that this route can accept
def index():
    if request.method == 'POST':
        task_content = request.form['content'] # content is the name of the input field in the form
        new_task = Todo(content=task_content) # create new task object
        
        try: 
            db.session.add(new_task) # add new task to db
            db.session.commit() # commit changes to db
            return redirect('/') # redirect to home page
        except:
            return 'There was an issue adding your task'
        
    else:
        tasks = Todo.query.order_by(Todo.date_created).all() # get all tasks from db, order by date created
        return render_template('index.html', tasks=tasks) # pass tasks to template

if __name__ == "__main__":
    app.run(debug=True)