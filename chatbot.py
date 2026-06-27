def get_response(user_message):
    user_message = user_message.lower()

    if "fever" in user_message:
        return "You may have a fever. Drink plenty of water and take adequate rest."

    elif "headache" in user_message:
        return "Headaches can occur due to stress, dehydration, or lack of sleep."

    elif "cough" in user_message:
        return "For cough, stay hydrated and avoid cold foods and drinks."

    elif "cold" in user_message:
        return "Take proper rest and drink warm fluids."

    elif "stomach pain" in user_message:
        return "Avoid spicy foods and consult a doctor if the pain continues."

    elif "vomiting" in user_message:
        return "Drink enough water to prevent dehydration and seek medical advice if necessary."

    elif "diarrhea" in user_message:
        return "Stay hydrated and eat light foods. Consult a doctor if symptoms persist."

    elif "hello" in user_message or "hi" in user_message:
        return "Hello! I am your AI Health Chatbot. How can I help you today?"

    elif "thank you" in user_message:
        return "You're welcome. Take care of your health."

    else:
        return "Please consult a healthcare professional for proper medical advice."