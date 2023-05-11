import tkinter as tk
from chatbot_controller import ChatbotController

class ChatbotGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.chatbot = ChatbotController(api_key='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')
        
        self.create_widgets()
        
    def create_widgets(self):
        # Configuración de estilo
        self.window.configure(bg="#4169E1")  # Fondo azul
        
        self.input_label = tk.Label(self.window, text="Consulta:", bg="#4169E1", fg="white")  # Texto blanco
        self.input_label.pack()
        
        self.input_entry = tk.Entry(self.window, width=50)
        self.input_entry.pack()
        self.input_entry.bind("<Return>", self.get_response_enter)  # Enviar mensaje con la tecla "Enter"
        
        self.output_label = tk.Label(self.window, text="Respuesta:", bg="#4169E1", fg="white")  # Texto blanco
        self.output_label.pack()
        
        self.output_text = tk.Text(self.window, height=10, width=50, bg="white")  # Fondo blanco
        self.output_text.pack()
        
        self.submit_button = tk.Button(self.window, text="Enviar", command=self.get_response)
        self.submit_button.pack()
        
    def get_response(self):
        user_input = self.input_entry.get()
        response = self.chatbot.generate_response(user_input)
        self.display_message(user_input, "Usuario")  # Mostrar mensaje del usuario
        self.display_message(response, "Bot")  # Mostrar respuesta del bot
        self.input_entry.delete(0, tk.END)
        
    def get_response_enter(self, event):
        self.get_response()
        
    def display_message(self, message, sender):
        formatted_message = f"{sender}: {message}\n"
        self.output_text.insert(tk.END, formatted_message)
        self.output_text.see(tk.END)  # Desplazarse automáticamente hacia abajo
        
    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    chatbot_gui = ChatbotGUI()
    chatbot_gui.run()
