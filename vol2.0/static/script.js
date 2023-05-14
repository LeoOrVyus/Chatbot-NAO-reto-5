document.addEventListener('DOMContentLoaded', () => {
    const chatLog = document.getElementById('chat-log');
    const userInput = document.getElementById('user-input');
    const sendButton = document.getElementById('send-button');
  
    sendButton.addEventListener('click', () => {
      const userMessage = userInput.value;
      appendMessage('You', userMessage);
      userInput.value = '';
  
      fetch('/get_response', {
        method: 'POST',
        body: new URLSearchParams({
          user_input: userMessage
        })
      })
      .then(response => response.text())
      .then(data => {
        appendMessage('Bot', data);
      });
    });
  
    function appendMessage(sender, message) {
      const messageElement = document.createElement('div');
      messageElement.classList.add('message');
      messageElement.innerHTML = `<strong>${sender}: </strong>${message}`;
      chatLog.appendChild(messageElement);
    }
  });
  