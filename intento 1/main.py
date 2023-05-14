import openai
import spacy
from chatbot_controller import ChatbotController
from chatbot_view import ChatbotView

# Ingresa tu clave de API de OpenAI aquí
api_key = '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'

# Crear una instancia del controlador del chatbot y ejecutarlo
controller = ChatbotController(api_key)
controller.run_chatbot()
