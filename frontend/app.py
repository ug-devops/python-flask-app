from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Frontend that sends data to the backend
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    data = {
        'name': request.form['name'],
        'email': request.form['email']
    }
    response = requests.post('http://backend-service:5001/api/data', json=data)
    return response.text

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

