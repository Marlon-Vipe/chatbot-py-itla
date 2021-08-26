from main import message_probability
import random


def check_all_messages(message):
        highest_prob = {}

        def response(bot_response, list_of_words, single_response = False, required_words = []):
            nonlocal highest_prob
            highest_prob[bot_response] = message_probability(message, list_of_words, single_response, required_words)

        response('Hola, ¿en qué podemos ayudarte?', ['hola', 'klk', 'saludos', 'buenas'], single_response = True)
        response('El nuevo rector del ITLA es Omar Mendez Lluberes,', ['rector'], single_response = True)
        response('La forma de pago del cuatrimestre es la siguiente:\nSe divide el pago en 3 pagos. El primer pago es un 40 porciento del total de los créditos, el segundo pago el 40% y el tercer pago es el 20 porciento restante. está compuesto por el pago de inscripción, servicio estudiantil y derecho a laboratorio (RD$ 6,640.00). El monto equivalente a los créditos se divide en tres, dichos pagos se efectúan mensualmente.\nNota: Puede consultar su recibo de pago para ver las fechas límites de cada pago.', ['pagos', 'realizar pagos', 'metodo de pago'], single_response = True)
        response('Para consultar si tiene beca debe:\n1.Entrar al sistema ORBI\n2.Naturaleza Educación Superior\n3.Mi Menú\n4.Académico\n5.Consultar línea de tiempo\n6.Si el estudiante no puede visualizar debe de contactar al Departamento de Asistencia Financiera al 809-738-4852 ext 307', ['como', 'consultar', 'verificar', 'saber', 'si', 'tengo', 'beca', 'de', 'educacion', 'permanente'], required_words=['beca'])
        response('Para ver la solicitud de revision de calificaciones debe:\n1.Entrar al sistema ORBI Seleccionar\n2.naturaleza Técnico Superior\n3.Mi Menú\n4.Solicitud\n5.Revisión de calificación', ['como', 'puedo', 'ver', 'veo', 'mi', 'solicitud', 'revision', 'calificacion', 'calificaciones'], required_words=["revision"])
        response('Para retirar una asignatura debe Completar en el Departamento de Educación Permanente el formulario de Retiro Académico. Puede hacerlo desde el sistema académico ORBI entrando a mi Menú, solicitud, Retiro, seleccionar y grabar.', ['como', 'puedo', 'retirar', 'retiro', 'una', 'materia', 'asignatura'], single_response=True)
        response('Debe de pagar en caja($200), luego dirigirse a registro para completar la solicitud y el formulario, Registro da respuesta en 7 días laborales para récords de nota sin legalizar, y legalizados tiene una duración de 15 días laborales.', ['como', 'solicito', 'obtengo', 'mi', 'record', 'de', 'notas'], required_words=['record'])
        response('Estudiantes mayores de 16 años o en tercero de bachillerato para Educación Permanente.\nCompletar los requisitos de admisión del Técnico Superior.', ['quienes', 'como', 'pueden', 'puedo' 'edad', 'estudiar', 'entrar', 'ingresar', 'en', 'el', 'itla'], single_response = True)
        response('Entrar a nuestro portal web www.itla.edu.do, entrar al sistema ORBI. Seleccionar la opción en la naturaleza de Técnico Superior\nMi Menú\nGestión docencia\nHistórico de Calificación/Consultar calificación', ['como', 'puedo', 'visualizar', 'ver', 'veo', 'consultar', 'verifico', 'consulto', 'mi', 'mis', 'calificaciones', 'calificacion'], single_response=True)
        response('Estamos ubicados en la Autopista Las Américas, Km. 27, PCSD, La Caleta, Boca Chica 11606.', ['ubicados', 'direccion', 'donde', 'ubicacion'], single_response=True)
        response('En el Dpto. de Caja puede realizar los pagos ya sea presencial o llamando por teléfono con la tarjeta de crédito, internet banking, depósito, en horarios:\nBanco de Reservas Cuenta No. 010-252724-5 (Cuenta Única del Tesoro) Lunes - viernes │ 8:00 a. m. - 4:00 p. m.\nTeléfono: 809-738-4852 ext. 313\nEnviar comprobante al correo cobros@itla.edu.do, en el cuerpo de correo indicar su usuario para Educación Permanente o Matricula para Educación Superior.', ['donde', 'puedo', 'realizar', 'hacer', 'los', 'el', 'pago', 'pagos' 'pagar'], single_response=True)
        response('Requisitos: Ser estudiante del ITLA\n2 fotos 2×2\nTener seguro medico\nSi es menor firmar un documento de descargo de parte del padre o tutor\nLlenar el formulario de solicitud de alojamiento | Nota: La asignación de plaza está sujeto a disponibilidad.', ['cuales', 'son', 'los', 'requisitos', 'para', 'ingresar', 'entrar', 'solicitar', 'alojamiento','residencia', 'academica' ], required_words=['residencia'])

        best_match = max(highest_prob, key=highest_prob.get)
        #print(highest_prob)

        return unknown() if highest_prob[best_match] < 1 else best_match

def unknown():
    response = ['puedes decirlo de nuevo?', 'No estoy seguro de lo quieres', 'búscalo en google a ver que tal'][random.randrange(3)]
    return response
