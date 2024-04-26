function sendText() {
    let userInput = document.getElementById('userInput');
    let text = userInput.value;
    displayMessage('You: ' + text);
    $.post('/ask', { text: text }, function(data) {
        displayMessage('Paula: ' + data.response);
        userInput.value = ''; // Clear input after sending
    });
}

function displayMessage(message) {
    let chatbox = document.getElementById('chatbox');
    chatbox.innerHTML += `<div>${message}</div>`;
    chatbox.scrollTop = chatbox.scrollHeight; // Scroll to the bottom
}
