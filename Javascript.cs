function sendMessage() {
    const input = document.getElementById("user-input");
    const chatBox = document.getElementById("chat-box");
    const userText = input.value.trim();

    if (userText === "") return;

    // Display user message
    const userMsg = document.createElement("div");
    userMsg.className = "user-message";
    userMsg.innerText = "You: " + userText;
    chatBox.appendChild(userMsg);

    // Convert input to lowercase
    const message = userText.toLowerCase();

    // Bot response
    let botReply = "";

    if (message.includes("fever")) {
        botReply = "Fever may be due to infection. Drink water, rest, and monitor temperature.";
    } 
    else if (message.includes("cough")) {
        botReply = "Cough can be caused by cold, allergy, or infection. If it lasts long, consult a doctor.";
    } 
    else if (message.includes("cold")) {
        botReply = "Common cold usually improves with rest, fluids, and warm food.";
    } 
    else if (message.includes("headache")) {
        botReply = "Headache may be due to stress, dehydration, or lack of sleep.";
    } 
    else if (message.includes("diabetes")) {
        botReply = "Diabetes is a condition where blood sugar levels become high. Healthy food and exercise help manage it.";
    } 
    else if (message.includes("covid")) {
        botReply = "COVID-19 symptoms include fever, cough, and breathing difficulty. Testing may be needed.";
    } 
    else {
        botReply = "Sorry, I can only provide basic health awareness. Please consult a doctor for medical advice.";
    }

    // Display bot message
    const botMsg = document.createElement("div");
    botMsg.className = "bot-message";
    botMsg.innerText = "Bot: " + botReply;
    chatBox.appendChild(botMsg);

    // Clear input
    input.value = "";

    // Auto-scroll
    chatBox.scrollTop = chatBox.scrollHeight;
}