import openai

class ChatbotController:
    def __init__(self, api_key):
        self.api_key = api_key
        openai.api_key = api_key

    def generate_response(self, user_input):
        response = openai.Completion.create(
            engine='text-davinci-003',
            prompt=user_input,
            max_tokens=50,
            temperature=0.7,
            n=1,
            stop=None,
            echo=False
        )
        return response.choices[0].text.strip()
