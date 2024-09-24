class Alumno1091:
    # Inicialización de atributos en ceros, cadenas vacías o fechas
    def __init__(self):
        self.id_cliente = 0
        self.nombre_cliente = ""
        self.direccion = ""
        self.telefono = ""
        self.correo_electronico = ""
        self.fecha_registro = None
        self.tipo_cliente = ""

    # Función para mostrar los datos
    def mostrar_datos(self):
        print(f"ID Cliente: {self.id_cliente}")
        print(f"Nombre Cliente: {self.nombre_cliente}")
        print(f"Dirección: {self.direccion}")
        print(f"Teléfono: {self.telefono}")
        print(f"Correo Electrónico: {self.correo_electronico}")
        print(f"Fecha Registro: {self.fecha_registro}")
        print(f"Tipo Cliente: {self.tipo_cliente}")

    # Función para listar 5 alumnos
    def listar_alumnos(self):
        alumnos = [
            {"alumno": 1, "nombre_cliente": "Juan", "direccion": "Calle 1", "telefono": "12345", "correo_electronico": "juan@example.com", "fecha_registro": "2023-09-24", "tipo_cliente": "Regular"},
            {"alumno": 2, "nombre_cliente": "Ana", "direccion": "Calle 2", "telefono": "23456", "correo_electronico": "ana@example.com", "fecha_registro": "2023-09-25", "tipo_cliente": "VIP"},
            {"alumno": 3, "nombre_cliente": "Pedro", "direccion": "Calle 3", "telefono": "34567", "correo_electronico": "pedro@example.com", "fecha_registro": "2023-09-26", "tipo_cliente": "Regular"},
            {"alumno": 4, "nombre_cliente": "Maria", "direccion": "Calle 4", "telefono": "45678", "correo_electronico": "maria@example.com", "fecha_registro": "2023-09-27", "tipo_cliente": "VIP"},
            {"alumno": 5, "nombre_cliente": "Luis", "direccion": "Calle 5", "telefono": "56789", "correo_electronico": "luis@example.com", "fecha_registro": "2023-09-28", "tipo_cliente": "Regular"}
        ]
        for alumno in alumnos:
            print(alumno)

    # Función para crear una tupla de 5 profesores
    def tupla_profes(self):
        profes = ("Profesor 1", "Profesor 2", "Profesor 3", "Profesor 4", "Profesor 5")
        for profe in profes:
            print(profe)

    # Función para crear un diccionario de 5 materias y calificaciones
    def dicionario_materia_califa(self):
        materias_califas = {
            "Matemáticas": 85,
            "Historia": 90,
            "Ciencias": 88,
            "Inglés": 92,
            "Arte": 75
        }
        for materia, califa in materias_califas.items():
            print(f"{materia}: {califa}")

    # Función para dar de alta un alumno
    def alta(self):
        print("La operación de alta se realizó correctamente.")

    # Función para dar de baja un alumno
    def baja(self):
        print("La operación de baja se realizó correctamente.")


# Creación de objeto y asignación de datos
obj = Alumno1091()
obj.id_cliente = 1
obj.nombre_cliente = "Diego"
obj.direccion = "Calle Falsa 123"
obj.telefono = "123456789"
obj.correo_electronico = "Diegor@hotmail.com"
obj.fecha_registro = "2023-09-24"
obj.tipo_cliente = "Regular"

# Utilizar los objetos y llamar a las funciones
obj.mostrar_datos()
obj.listar_alumnos()
obj.tupla_profes()
obj.dicionario_materia_califa()
