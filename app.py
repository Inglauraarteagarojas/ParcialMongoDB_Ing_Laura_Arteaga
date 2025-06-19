from flask import Flask, render_template, request, send_file
from io import BytesIO
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from datetime import datetime
import pytz

app = Flask(__name__)

# 40 preguntas
questions = [
    {"text": "MongoDB es una base de datos NoSQL.", "type": "true_false", "answer": "true"},
    {
  "text": "Un estudiante tiene una nota de 4.5. ¿Cuál sentencia imprime 'Aprobado' si la nota es mayor o igual a 3.0?",
  "type": "multiple",
  "options": [
    "if nota >= 3.0: print('Aprobado')",
    "if nota <= 3.0: print('Aprobado')",
    "if nota > 4.5: print('Aprobado')",
    "if nota == 3.0: print('Aprobado')"
  ],
  "answer": [
    "if nota >= 3.0: print('Aprobado')"
  ]
},
    

    
   {
  "text": "Un sensor mide la temperatura. Si es mayor a 30 se imprime 'Alerta de calor', si no, 'Temperatura normal'. ¿Cuál opción es correcta?",
  "type": "multiple",
  "options": [
    "if temp > 30: print('Alerta de calor') else: print('Temperatura normal')",
    "if temp > 30: print('Alerta de calor')",
    "if temp < 30: print('Temperatura normal')",
    "if temp > 30: print('Alerta de calor')\nelse: print('Temperatura normal')"
  ],
  "answer": [
    "if temp > 30: print('Alerta de calor')\nelse: print('Temperatura normal')"
  ]
},
   {
  "text": "Dada la ecuación x² + 6x - 2, ¿qué sentencia condicional verifica si las raíces son imaginarias y, en ese caso, les suma 4?",
  "type": "multiple",
  "options": [
    "if discriminante < 0: resultado = complex(-b, math.sqrt(-discriminante)) / (2*a); resultado += 4",
    "if discriminante < 0: resultado = (-b + sqrt(-discriminante)) / (2*a); resultado += 4",
    "if discriminante < 0: print('Raíces imaginarias'); resultado += 4",
    "if discriminante < 0: resultado = (-b + sqrt(discriminante)) / (2*a)"
  ],
  "answer": [
    "if discriminante < 0: resultado = complex(-b, math.sqrt(-discriminante)) / (2*a); resultado += 4"
  ]
},

   {
  "text": "¿Cuál sentencia imprime los números del 1 al 5?",
  "type": "multiple",
  "options": [
    "for i in range(1, 6): print(i)",
    "for i in range(5): print(i+1)",
    "while i <= 5: print(i); i += 1",
    "for i in range(1, 5): print(i)"
  ],
  "answer": [
    "for i in range(1, 6): print(i)",
    "for i in range(5): print(i+1)"
  ]
},
   {
  "text": "Si una raíz real de x² + 6x - 2 es un número entero, ¿qué ciclo `for` recorre las raíces y multiplica por 365 si son enteras?",
  "type": "multiple",
  "options": [
    "for r in raices: if r.is_integer(): print(r * 365)",
    "for r in raices: if isinstance(r, int): print(r * 365)",
    "for r in raices: if r % 1 == 0: print(r * 365)",
    "for r in raices: print(r * 365)"
  ],
  "answer": [
    "for r in raices: if r.is_integer(): print(r * 365)",
    "for r in raices: if r % 1 == 0: print(r * 365)"
  ]
},




   

    
    
    {"text": "MongoDB fue creado por Microsoft.", "type": "true_false", "answer": "false"},
    {"text": "MongoDB permite crear índices para mejorar el rendimiento de las consultas.", "type": "true_false", "answer": "true"},
    {"text": "MongoDB es una base de datos orientada a grafos.", "type": "true_false", "answer": "false"},
    {"text": "MongoDB puede almacenar datos geoespaciales.", "type": "true_false", "answer": "true"},
    
    {"text": "MongoDB es una base de datos relacional.", "type": "true_false", "answer": "false"},
    {"text": "MongoDB almacena datos en formato JSON o BSON.", "type": "true_false", "answer": "true"},
    {"text": "MongoDB Atlas es una plataforma en la nube para alojar bases de datos MongoDB.", "type": "true_false", "answer": "true"},
    {"text": "Para conectarse a MongoDB Atlas desde Python se necesita una URI.", "type": "true_false", "answer": "true"},
    {"text": "La URI de conexión incluye el usuario, contraseña y nombre del cluster.", "type": "true_false", "answer": "true"},
    {
        "text": "Selecciona los formatos válidos para almacenar datos en MongoDB.",
        "type": "multiple",
        "options": ["JSON", "BSON", "CSV", "XLSX"],
        "answer": ["JSON", "BSON"]
    },
    {
        "text": "Selecciona las librerías de Python que se usan para trabajar con MongoDB.",
        "type": "multiple",
        "options": ["pymongo", "sqlalchemy", "motor", "pandas"],
        "answer": ["pymongo", "motor"]
    },
    {"text": "MongoDB necesita un 'board' físico como Arduino para subir datos a la nube.", "type": "true_false", "answer": "false"},
    {"text": "El nombre de dominio del cluster de MongoDB Atlas termina en '.net'.", "type": "true_false", "answer": "true"},
    {"text": "MongoDB permite crear un usuario tipo root con acceso total a la base de datos.", "type": "true_false", "answer": "true"},
    {
        "text": "La sentencia `create database arduino_uno(sensor char, valor int, date datetime.now());` es válida en MongoDB.",
        "type": "true_false",
        "answer": "false"
    },
    {"text": "MongoDB se instala en Python con `pip install pymongo`.", "type": "true_false", "answer": "true"},
    {
        "text": "Selecciona lo que se necesita para conectarse a un cluster de MongoDB Atlas.",
        "type": "multiple",
        "options": ["URI", "Cluster", "Token de Firebase", "Usuario y contraseña"],
        "answer": ["URI", "Cluster", "Usuario y contraseña"]
    },
    {"text": "MongoDB Community es una versión gratuita para instalar localmente.", "type": "true_false", "answer": "true"},
    {"text": "MongoDB permite trabajar con colecciones en lugar de tablas.", "type": "true_false", "answer": "true"},

    {
        "text": "¿Cuál es la sintaxis correcta para insertar un dato con sensor DHT11, temperatura, humedad y timestamp?",
        "type": "multiple",
        "options": [
            "coleccion.insert({sensor: 'dht11', temperatura: 25, humedad: 80, tiempo: datetime.now()})",
            "coleccion.insert_one({'sensor': 'dht11', 'temperatura': temperatura, 'humedad': humedad, 'tiempo': datetime.now()})",
            "db.insert({'sensor': 'dht11', 'temperatura': 25, 'humedad': 80})",
            "coleccion.insertOne({...})"
        ],
        "answer": [
            "coleccion.insert_one({'sensor': 'dht11', 'temperatura': temperatura, 'humedad': humedad, 'tiempo': datetime.now()})"
        ]
    },
    {
        "text": "¿Cuál sería una consulta correcta para encontrar temperaturas entre 30°C y 50°C?",
        "type": "multiple",
        "options": [
            "coleccion.find({'temperatura': {'$gt': 30, '$lt': 50}})",
            "db.find({'temperatura': {'mayor': 30, 'menor': 50}})",
            "coleccion.find({temperatura: {$gte: 30, $lte: 50}})",
            "coleccion.find({'temperatura': {'$gte': 30, '$lte': 50}})"
        ],
        "answer": [
            "coleccion.find({'temperatura': {'$gt': 30, '$lt': 50}})",
            "coleccion.find({'temperatura': {'$gte': 30, '$lte': 50}})"
        ]
    },
    {
        "text": "¿Qué comandos permiten mostrar todos los documentos de una colección BSON?",
        "type": "multiple",
        "options": [
            "coleccion.find()",
            "coleccion.find({})",
            "db.find_all()",
            "db.collection.find_all()"
        ],
        "answer": [
            "coleccion.find()",
            "coleccion.find({})"
        ]
    },
    {
        "text": "¿Quién crea el `ObjectId` en un documento de MongoDB?",
        "type": "multiple",
        "options": [
            "El desarrollador manualmente",
            "El sistema MongoDB automáticamente al insertar el documento",
            "El servidor de MongoDB Atlas",
            "El método createObjectId() del usuario"
        ],
        "answer": [
            "El sistema MongoDB automáticamente al insertar el documento"
        ]
    },
    {
        "text": "¿Cuál comando permite encontrar el último dato insertado en una colección?",
        "type": "multiple",
        "options": [
            "coleccion.find().sort('_id', -1).limit(1)",
            "coleccion.last()",
            "db.collection.findLast()",
            "coleccion.find().sort({tiempo: -1}).limit(1)"
        ],
        "answer": [
            "coleccion.find().sort('_id', -1).limit(1)",
            "coleccion.find().sort({tiempo: -1}).limit(1)"
        ]
    },
    {
        "text": "¿Cuál es el método correcto para agregar un nuevo dato a una colección?",
        "type": "multiple",
        "options": [
            "coleccion.append({...})",
            "coleccion.insert_one({...})",
            "coleccion.add({...})",
            "coleccion.insert({...})"
        ],
        "answer": [
            "coleccion.insert_one({...})"
        ]
    },
    {
        "text": "¿Qué significa `coleccion.limit(7)`?",
        "type": "multiple",
        "options": [
            "Muestra solo los primeros 7 documentos",
            "Limita la base de datos a 7 registros permanentes",
            "Filtra los documentos por tamaño",
            "Es un error de sintaxis"
        ],
        "answer": [
            "Muestra solo los primeros 7 documentos"
        ]
    },
    {
        "text": "¿Qué opciones son válidas para actualizar un campo de un documento en MongoDB?",
        "type": "multiple",
        "options": [
            "coleccion.update_one({'sensor': 'dht11'}, {'$set': {'humedad': 60}})",
            "coleccion.update({'sensor': 'dht11'}, {'$set': {'humedad': 60}})",
            "db.update({'humedad': 60})",
            "coleccion.update_many({}, {'humedad': 60})"
        ],
        "answer": [
            "coleccion.update_one({'sensor': 'dht11'}, {'$set': {'humedad': 60}})",
            "coleccion.update({'sensor': 'dht11'}, {'$set': {'humedad': 60}})"
        ]
    },
    {
        "text": "¿Qué comando elimina un documento por condición en MongoDB?",
        "type": "multiple",
        "options": [
            "coleccion.remove({'sensor': 'dht11'})",
            "coleccion.delete_one({'sensor': 'dht11'})",
            "coleccion.erase({'sensor': 'dht11'})",
            "coleccion.delete_many({'sensor': 'dht11'})"
        ],
        "answer": [
            "coleccion.delete_one({'sensor': 'dht11'})",
            "coleccion.delete_many({'sensor': 'dht11'})"
        ]
    },
    {
        "text": "¿Qué comandos permiten insertar varios documentos al mismo tiempo?",
        "type": "multiple",
        "options": [
            "coleccion.insert_many([...])",
            "coleccion.insert_all([...])",
            "db.bulk_insert([...])",
            "coleccion.insert([...])"
        ],
        "answer": [
            "coleccion.insert_many([...])",
            "coleccion.insert([...])"
        ]
    },
    {
        "text": "¿Qué sentencia es válida para buscar todos los sensores DHT11?",
        "type": "multiple",
        "options": [
            "coleccion.find({'sensor': 'dht11'})",
            "coleccion.where({'sensor': 'dht11'})",
            "db.collection.find({'sensor': 'dht11'})",
            "coleccion.search({'sensor': 'dht11'})"
        ],
        "answer": [
            "coleccion.find({'sensor': 'dht11'})",
            "db.collection.find({'sensor': 'dht11'})"
        ]
    },
    {
        "text": "¿Qué comandos ordenan los documentos de forma descendente por temperatura?",
        "type": "multiple",
        "options": [
            "coleccion.find().sort('temperatura', -1)",
            "coleccion.sort({temperatura: -1})",
            "coleccion.find().order_by('temperatura')",
            "db.find().sort({'temperatura': -1})"
        ],
        "answer": [
            "coleccion.find().sort('temperatura', -1)",
            "db.find().sort({'temperatura': -1})"
        ]
    },
    {
        "text": "¿Cuál es la sintaxis correcta de un documento BSON?",
        "type": "multiple",
        "options": [
            "{'sensor': 'dht11', 'valor': 32}",
            "{sensor: 'dht11', valor: 32}",
            "{\"sensor\": \"dht11\", \"valor\": 32}",
            "{sensor = 'dht11'; valor = 32}"
        ],
        "answer": [
            "{'sensor': 'dht11', 'valor': 32}",
            "{\"sensor\": \"dht11\", \"valor\": 32}"
        ]
    },
    {"text": "¿Qué comando permite contar el número de documentos en una colección?",
     "type": "multiple",
     "options": [
         "coleccion.count_documents({})",
            "coleccion.count()",
            "coleccion.size()",
            "coleccion.document_count()"
        ],
        "answer": [
            "coleccion.count_documents({})",
            "coleccion.count()"
]

},
    {"text": "¿Qué comando permite eliminar todos los documentos de una colección?",
     "type": "multiple",
     "options": [
         "coleccion.delete_many({})",
         "coleccion.remove({})",
         "coleccion.clear()",
         "coleccion.drop()"
     ], 
        "answer": [
            "coleccion.delete_many({})",
            "coleccion.remove({})",
            "coleccion.drop()"
        ]   
    }
    
]

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        student_name = request.form.get("student_name", "No proporcionado")
        correct = 0
        blur_count = int(request.form.get("blur_count", 0))
        results = []

        for i, q in enumerate(questions):
            res = {
                "question": q["text"],
                "user_answer": None,
                "correct_answer": q["answer"],
                "is_correct": False
            }

            if q["type"] == "true_false":
                user_ans = request.form.get(f"q{i}")
                res["user_answer"] = user_ans
                if user_ans == q["answer"]:
                    res["is_correct"] = True
                    correct += 1

            elif q["type"] == "multiple":
                user_ans = request.form.getlist(f"q{i}")
                res["user_answer"] = user_ans
                if set(user_ans) == set(q["answer"]):
                    res["is_correct"] = True
                    correct += 1

            results.append(res)

        score = (correct / len(questions)) * 5 - (blur_count * 0.1)
        score = max(score, 0)

        return render_template("result.html", results=results, score=round(score, 2), blur_count=blur_count, student_name=student_name)

    return render_template("index.html", questions=questions)

@app.route("/download_pdf", methods=["POST"])
def download_pdf():
    data = request.json
    results = data["results"]
    score = data["score"]
    blur_count = data["blur_count"]
    student_name = data.get("student_name", "Estudiante anónimo")

    # Hora Colombia
    tz = pytz.timezone("America/Bogota")
    hora_colombia = datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S")

    buffer = BytesIO()
    pdf = canvas.Canvas(buffer, pagesize=letter)
    width, height = letter
    y = height - 40

    pdf.setFont("Helvetica-Bold", 14)
    pdf.drawString(40, y, "Resultados del Cuestionario MongoDB")
    y -= 20
    pdf.setFont("Helvetica", 12)
    pdf.drawString(40, y, f"Nombre del estudiante: {student_name}")
    y -= 20
    pdf.drawString(40, y, f"Fecha y hora de envío (Colombia): {hora_colombia}")
    y -= 20
    pdf.drawString(40, y, f"Puntuación final: {score} de 5")
    y -= 20
    pdf.drawString(40, y, f"Ventanas fuera de foco: {blur_count}")
    y -= 30

    for idx, r in enumerate(results, 1):
        pdf.setFont("Helvetica-Bold", 10)
        pdf.drawString(40, y, f"{idx}. {r['question'][:90]}")
        y -= 12
        pdf.setFont("Helvetica", 10)
        pdf.drawString(50, y, f"Tu respuesta: {r['user_answer']}")
        y -= 12
        pdf.drawString(50, y, f"Respuesta correcta: {r['correct_answer']}")
        y -= 12
        pdf.drawString(50, y, "✔ Correcta" if r["is_correct"] else "✘ Incorrecta")
        y -= 18
        if y < 80:
            pdf.showPage()
            y = height - 40

    pdf.save()
    buffer.seek(0)

    return send_file(buffer, as_attachment=True, download_name="resultado_cuestionario.pdf", mimetype='application/pdf')

if __name__ == "__main__":
    app.run(debug=True)
