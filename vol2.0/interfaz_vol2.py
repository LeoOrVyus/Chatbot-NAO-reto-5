import tkinter as tk
from chatbot_controller import ChatbotController

# Crear la ventana de la interfaz de chatbot
window = tk.Tk()
window.title("Chatbot")
window.geometry("400x500")
window.configure(background="#f0f0f0")  # Establecer color de fondo gris claro

# Crear el cuadro de texto de salida del chatbot
chatbot_output = tk.Text(window, height=20, bg="#f8f8f8", state="disabled")  # Establecer color de fondo gris claro
chatbot_output.pack(pady=10)

# Crear el cuadro de texto de entrada del usuario
user_input = tk.Entry(window, width=40, font=("Arial", 12))
user_input.pack(pady=10)

# Obtener la API key (debes reemplazar 'TU_API_KEY' con tu propia API key)
api_key = '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'

# Crear una instancia del controlador del chatbot
chatbot_controller = ChatbotController(api_key)

# Función para obtener la respuesta del chatbot
def get_chatbot_response(event=None):  # Agregar parámetro de evento
    # Obtener la pregunta del usuario
    question = user_input.get().strip()

    # Obtener la respuesta del chatbot utilizando el controlador
    response = chatbot_controller.generate_response(question)

    # Mostrar la respuesta en el cuadro de texto de salida
    chatbot_output.config(state="normal")
    chatbot_output.insert(tk.END, "Usuario: " + question + "\n", "user")
    chatbot_output.insert(tk.END, "Chatbot: " + response + "\n", "bot")
    chatbot_output.config(state="disabled")
    chatbot_output.see(tk.END)

    # Limpiar el cuadro de entrada
    user_input.delete(0, tk.END)

# Asociar la pulsación de la tecla "Enter" a la función get_chatbot_response()
user_input.bind("<Return>", get_chatbot_response)

# Crear el botón de enviar
send_button = tk.Button(window, text="Enviar", command=get_chatbot_response)
send_button.pack(pady=10)

# Configurar la fuente y el color del texto del usuario y el chatbot
chatbot_output.tag_configure("user", font=("Arial", 12), foreground="blue")
chatbot_output.tag_configure("bot", font=("Arial", 12), foreground="green")

# Ejecutar la ventana de la interfaz de chatbot
window.mainloop()
