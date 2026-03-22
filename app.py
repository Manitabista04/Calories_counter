from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/moon/Desktop/Code/Calorie counter/instance/calories.db'
db = SQLAlchemy(app)

class foodEntry(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    food = db.Column(db.String(500), nullable = False)
    calories = db.Column(db.Integer, nullable =False)
    date_created = db.Column(db.DateTime, default= datetime.utcnow)
    
    def __repr__(self):
        return f"{self.food} - {self.calories}"

@app.route("/", methods = ['GET' ,'POST'])
def home():
    if request.method == 'POST':
        food =request.form['food']
        calories = request.form['calories']
        food_entry = foodEntry(food = food , calories = calories)
        db.session.add(food_entry)
        db.session.commit()
        
    allfoodEntry = foodEntry.query.all()
    return render_template('index.html' , allfoodEntry = allfoodEntry)

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True, port=5001)
