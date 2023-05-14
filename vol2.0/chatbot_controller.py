import openai
import spacy
from chatbot_view import ChatbotView

class ChatbotController:
    def __init__(self, api_key):
        self.api_key = api_key
        openai.api_key = api_key
        self.nlp = spacy.load("es_core_news_md")
        self.questions = [
        "¿Cuál es el horario de clases?",
        "¿Cómo puedo inscribirme en un nuevo curso?",
        "¿Cuál es el costo de la matrícula escolar?",
        "¿Cuáles son los requisitos para solicitar una beca?",
        "¿Dónde puedo encontrar el calendario académico?",
        "¿Cuál es el procedimiento para solicitar una constancia de estudios?",
        "¿Cómo puedo acceder al sistema de notas en línea?",
        "¿Cuál es el proceso para solicitar una reunión con los profesores?",
        "¿Qué actividades extracurriculares ofrecen en el colegio?",
        "¿Cuáles son los servicios de apoyo disponibles para los estudiantes con necesidades especiales?",
        "¿Cuáles son las fechas de las vacaciones escolares?",
        "¿Cómo puedo solicitar una transferencia de colegio?",
        "¿Cuál es la política de tardanzas?",
        "¿Cuál es el proceso para obtener una beca deportiva?",
        "¿Cómo puedo solicitar una cita con el orientador escolar?",
        "¿Cuáles son los recursos tecnológicos disponibles para los estudiantes?",
        "¿Cuál es el proceso para solicitar una tarjeta estudiantil?",
        "¿Dónde puedo obtener información sobre los programas de intercambio estudiantil?",
        "¿Cuál es el procedimiento para solicitar una excusa médica?",
        "¿Cómo puedo acceder a los laboratorios de ciencias del colegio?",
        "Quiero hablar con algun profesor, director o administrativo de la escuela"
        ]

    def generate_response(self, user_input):
        # Saludo inicial
        if user_input.lower() in ['hola', 'qué tal', 'cómo estás']:
            return "Bot: ¡Hola! ¿En qué puedo ayudarte hoy?"
        
        # Pregunta sobre el estado
        if user_input.lower() == 'cómo estás':
            return "Bot: Bien, gracias. ¿Y tú?"

        # Obtener respuesta según el número ingresado
        try:
            index = int(user_input)
            if 1 <= index <= len(self.questions):
                question = self.questions[index - 1]
                return self.get_answer(question)
            else:
                return "Bot: Por favor, ingresa un número válido del 1 al 10."
        except ValueError:
            # Verificar si la pregunta del usuario coincide o es similar a alguna pregunta predefinida
            similarity_threshold = 0.8  # Umbral de similitud para considerar una pregunta similar
            best_similarity = 0
            best_question = None

            for question in self.questions:
                similarity = self.nlp(question).similarity(self.nlp(user_input))

                if similarity > best_similarity:
                    best_similarity = similarity
                    best_question = question

            if best_similarity >= similarity_threshold:
                return self.get_answer(best_question)
            else:
                return self.get_suggestions()

    def get_answer(self, question):
        # Lógica para obtener la respuesta según la pregunta
        # Puedes utilizar estructuras condicionales, consultas a bases de datos, etc.
        # Aquí se muestra un ejemplo básico de respuestas predefinidas
        if question == "¿Cuál es el horario de clases?":
            answer = "El horario de clases es de lunes a viernes de 8:00 am a 3:00 pm."
        elif question == "¿Cómo puedo inscribirme en un nuevo curso?":
            answer = "Puedes inscribirte en un nuevo curso llenando el formulario de inscripción en la oficina de administración."
        elif question == "¿Cuál es el costo de la matrícula escolar?":
            answer = "El costo de la matrícula escolar varía según el nivel educativo. Te recomiendo consultar la sección de pagos en nuestra página web para más información."
        elif question == "¿Cuáles son los requisitos para solicitar una beca?":
            answer = "Los requisitos para solicitar una beca pueden variar según el tipo de beca y la institución. Generalmente, se evalúa el rendimiento académico, la situación económica y otros criterios establecidos por el programa de becas. Te sugiero contactar la oficina de becas o asistencia financiera del colegio para obtener información detallada sobre los requisitos específicos."
        elif question == "¿Dónde puedo encontrar el calendario académico?":
            answer = "Puedes encontrar el calendario académico en nuestra página web oficial. Normalmente, se publica en la sección de estudiantes o en el área de recursos académicos. Si no lo encuentras, te recomiendo comunicarte con la secretaría académica del colegio para obtener una copia o más información al respecto."
        elif question == "¿Cuál es el procedimiento para solicitar una constancia de estudios?":
            answer = "El procedimiento para solicitar una constancia de estudios es el siguiente: debes completar el formulario de solicitud y presentarlo en la secretaría académica. Generalmente, se requiere una copia de tu documento de identidad y el pago de una tarifa administrativa. Te recomiendo verificar los detalles específicos en nuestra página web o consultando directamente con la secretaría académica."
        elif question == "¿Cómo puedo acceder al sistema de notas en línea?":
            answer = "Para acceder al sistema de notas en línea, debes ingresar a nuestra página web oficial y buscar la sección de acceso al sistema de notas. Allí deberás ingresar tus credenciales de usuario y contraseña proporcionadas por el colegio. Si tienes problemas para acceder, te recomiendo comunicarte con el departamento de tecnología o el soporte técnico del colegio para obtener ayuda adicional."
        elif question == "¿Cuál es el proceso para solicitar una reunión con los profesores?":
            answer = "El proceso para solicitar una reunión con los profesores es el siguiente: debes comunicarte con la coordinación académica o la secretaría del colegio para solicitar una cita. Ellos te indicarán los pasos a seguir y te asignarán una fecha y hora para la reunión. Si tienes algún motivo específico para la reunión, es recomendable mencionarlo al momento de hacer la solicitud."
        elif question == "¿Qué actividades extracurriculares ofrecen en el colegio?":
            answer = "Ofrecemos una variedad de actividades extracurriculares para nuestros estudiantes. Algunas de ellas incluyen deportes, clubes académicos, grupos de música, arte y teatro."
        elif question == "¿Cuáles son los servicios de apoyo disponibles para los estudiantes con necesidades especiales?":
            answer = "Ofrecemos una variedad de servicios de apoyo para estudiantes con necesidades especiales. Estos pueden incluir apoyo educativo individualizado, adaptaciones curriculares, terapias especializadas, asistencia de profesionales de apoyo y acceso a recursos de apoyo. Trabajamos en estrecha colaboración con los estudiantes, sus familias y el personal docente para garantizar una experiencia educativa inclusiva y exitosa."
        elif question == "¿Cuáles son las fechas de las vacaciones escolares?":
            answer = "Las fechas de las vacaciones escolares varían según el calendario académico de cada año. Te recomiendo consultar el calendario académico oficial del colegio para obtener información precisa sobre las fechas de las vacaciones. Este calendario generalmente está disponible en nuestra página web o puedes solicitar una copia en la secretaría del colegio."
        elif question == "¿Cómo puedo solicitar una transferencia de colegio?":
            answer = "Para solicitar una transferencia de colegio, debes seguir estos pasos: 1. Contacta a la secretaría del colegio actual para informarles sobre tu intención de transferirte. 2. Obtén los documentos requeridos para la transferencia, como boletas de calificaciones, certificados y otros registros académicos. 3. Investiga los requisitos y procedimientos del colegio al que deseas transferirte. 4. Completa el formulario de solicitud de transferencia proporcionado por el nuevo colegio. 5. Presenta la solicitud junto con los documentos requeridos al nuevo colegio. El nuevo colegio evaluará tu solicitud y te informará sobre el proceso de admisión y la aceptación de la transferencia."
        elif question == "¿Cuál es la política de tardanzas?":
            answer = "Nuestra política de tardanzas establece que los estudiantes deben llegar a tiempo a todas las clases y actividades escolares. Si un estudiante llega tarde, se espera que se registre su llegada tardía en la oficina de asistencia o en el lugar designado. Las consecuencias por tardanzas repetidas pueden incluir advertencias, llamadas de atención, actividades de recuperación o acciones disciplinarias adicionales según las políticas del colegio."
        elif question == "¿Cuál es el proceso para obtener una beca deportiva?":
            answer = "El proceso para obtener una beca deportiva puede variar según el colegio y el programa de becas. Por lo general, implica demostrar habilidades deportivas sobresalientes y cumplir con los requisitos académicos establecidos. Te recomiendo comunicarte con la oficina de deportes o la oficina de becas del colegio para obtener información específica sobre el proceso de solicitud, los plazos y los criterios de selección para las becas deportivas."
        elif question == "¿Cómo puedo solicitar una cita con el orientador escolar?":
            answer = "Para solicitar una cita con el orientador escolar, puedes seguir estos pasos: 1. Comunícate con la oficina de orientación o la secretaría del colegio para informarles sobre tu solicitud de cita. 2. Indica el motivo de la cita y si tienes alguna preferencia de fecha"
        if question == "¿Cuáles son los recursos tecnológicos disponibles para los estudiantes?":
            answer = "Contamos con una variedad de recursos tecnológicos disponibles para los estudiantes. Estos pueden incluir laboratorios de computación equipados con computadoras modernas, acceso a internet de alta velocidad, software educativo especializado, dispositivos móviles como tabletas o computadoras portátiles, y plataformas en línea para el aprendizaje y la colaboración. Además, ofrecemos capacitación y soporte técnico para asegurar que los estudiantes puedan aprovechar al máximo estos recursos."
        elif question == "¿Cuál es el proceso para solicitar una tarjeta estudiantil?":
            answer = "El proceso para solicitar una tarjeta estudiantil es el siguiente: 1. Completa el formulario de solicitud de tarjeta estudiantil proporcionado por el colegio. 2. Adjunta una fotografía reciente según las especificaciones indicadas. 3. Presenta la solicitud y la fotografía en la oficina de administración del colegio. 4. Paga cualquier tarifa requerida para la emisión de la tarjeta. Una vez procesada la solicitud, recibirás tu tarjeta estudiantil, la cual te identificará como estudiante del colegio y te permitirá acceder a ciertos beneficios y servicios dentro y fuera del campus."
        elif question == "¿Dónde puedo obtener información sobre los programas de intercambio estudiantil?":
            answer = "Puedes obtener información sobre los programas de intercambio estudiantil en la oficina de relaciones internacionales o la oficina de intercambio del colegio. Estas oficinas suelen proporcionar detalles sobre los programas de intercambio disponibles, los requisitos de elegibilidad, los destinos de intercambio, los plazos de solicitud y los beneficios del programa. También puedes consultar la página web oficial del colegio, donde generalmente se publica información relacionada con los programas de intercambio."
        elif question == "¿Cuál es el procedimiento para solicitar una excusa médica?":
            answer = "Si necesitas solicitar una excusa médica, debes seguir estos pasos: 1. Consulta a un médico y obtén un informe médico detallado que justifique tu ausencia debido a razones de salud. 2. Comunícate con la secretaría del colegio para informarles sobre tu situación y tu intención de presentar una excusa médica. 3. Presenta el informe médico en la secretaría del colegio dentro del plazo establecido. El personal de la secretaría evaluará tu situación y determinará si la excusa médica es válida según las políticas y procedimientos del colegio."
        elif question == "¿Cómo puedo acceder a los laboratorios de ciencias del colegio?":
            answer = "Para acceder a los laboratorios de ciencias del colegio, debes seguir estos pasos: 1. Asegúrate de cumplir con los requisitos de seguridad y capacitación necesarios para trabajar en un laboratorio. 2. Consulta el horario de disponibilidad de los laboratorios y elige un momento adecuado para utilizarlos"
        elif question == "Quiero hablar con algun profesor, director o administrativo de la escuela":
            answer = "Claro, a continuación te comparto los numeros del colegio: y nuestra pagina web:"
        # Agrega más respuestas según las preguntas
        # Agrega más respuestas según las preguntas que desees responder

        return answer

    def get_suggestions(self):
        suggestions = "Disculpa, no tengo acceso a esa información en este momento, pero puedo ayudarte con alguna de estas consultas:\n"
        for i, question in enumerate(self.questions, start=1):
            suggestions += f"{i}. {question}\n"
        return suggestions



    def run_chatbot(self):
        while True:
            user_input = ChatbotView.get_user_input()
            response = self.generate_response(user_input)
            ChatbotView.display_response(response)