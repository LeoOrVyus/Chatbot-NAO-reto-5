import openai
import spacy
from chatbot_controller import ChatbotController
from chatbot_view import ChatbotView

# Ingresa tu clave de API de OpenAI aquí
api_key = ''

# Crear una instancia del controlador del chatbot y ejecutarlo
controller = ChatbotController(api_key)
controller.run_chatbot()
