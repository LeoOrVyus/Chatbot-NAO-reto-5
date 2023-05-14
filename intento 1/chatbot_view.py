class ChatbotView:
    @staticmethod
    def get_user_input():
        return input("Usuario: ")

    @staticmethod
    def display_response(response):
        print("Bot:", response)
