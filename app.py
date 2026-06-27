from flask import Flask, render_template, request

app = Flask(__name__)

# Home Page
@app.route('/')
def home():
    return render_template('index.html')

# Login Page
@app.route('/login')
def login():
    return render_template('login.html')

# Chat Page
@app.route('/chat')
def chat():
    return render_template('chat.html')

# Chatbot Response
@app.route('/get_response', methods=['POST'])
def get_response():
    user_message = request.form['message'].lower()

    if "fever" in user_message:
        response = "You may have a fever. Drink plenty of water and take rest."
    elif "headache" in user_message:
        response = "Headache may occur due to stress or lack of sleep."
    elif "cough" in user_message:
        response = "For cough, stay hydrated and avoid cold foods."
    elif "cold" in user_message:
        response = "Take sufficient rest and drink warm fluids."
    elif "stomach pain" in user_message:
        response = "Avoid spicy foods and consult a doctor if pain continues."
    else:
        response = "Please consult a healthcare professional for proper medical advice."

    return response

if __name__ == '__main__':
    app.run(debug=True)