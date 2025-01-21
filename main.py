from abc import ABC, abstractmethod
from datetime import datetime

class Persona(ABC): # Define una clase abstracta llamada "Persona", heredando de ABC (Abstract Base Class).
    def __init__(self, nombre, contacto, direccion): # Constructor que inicializa los atributos básicos de la clase.
        self.nombre = nombre
        self.contacto = contacto
        self.direccion = direccion
        
    @abstractmethod
    def mostrar_informacion(self):
        pass

class Mascota(ABC): # Define una clase abstracta llamada "Mascota", que hereda de ABC (Abstract Base Class).
    def __init__(self, nombre, especie, raza, edad): # Constructor que inicializa los atributos básicos de la mascota.
        self.nombre = nombre
        self.especie = especie
        self.raza = raza 
        self.edad = edad
        self.historial_citas = []
        
    @abstractmethod
    def agregar_al_historial(self, detalles_servicio):
        pass

class Cita(ABC): # Define una clase abstracta llamada "Cita", que hereda de ABC (Abstract Base Class).
    def __init__(self, fecha, hora, servicio, veterinario): # Constructor que inicializa los detalles de una cita.
        self.fecha = fecha
        self.hora = hora
        self.servicio = servicio
        self.veterinario = veterinario
        
    @abstractmethod
    def actualizar(self, **kwargs):
        """
        Método abstracto para actualizar los detalles de la cita.
        Los parámetros serán proporcionados como argumentos clave-valor (**kwargs),
        permitiendo flexibilidad al actualizar diferentes atributos de la cita.
        """       
        pass # La implementación específica de este método será definida en las subclases.

# Definición de subclases.

class Cliente(Persona): # Define una clase "Cliente" que hereda de la clase base "Persona".
    def __init__(self, nombre, contacto, direccion):
        # Llama al constructor de la clase padre "Persona" para inicializar los atributos comunes.
        super().__init__(nombre, contacto, direccion)
        self.mascotas = [] # Inicializa una lista vacía para almacenar las mascotas asociadas al cliente.
        
    def agregar_mascota(self, mascota):
        self.mascotas.append(mascota)
    
    def mostrar_informacion(self):
        return f"Cliente: {self.nombre}, Contacto: {self.contacto}, Direccion {self.direccion}"
    

class RegistrarMascota(Mascota): # Clase que hereda de Mascota y añade funcionalidad para registrar información adicional al historial de citas.
    def agregar_al_historial(self, detalles_servicio):
        self.historial_citas.append(detalles_servicio)  # Agrega los detalles del servicio al historial.
        
    def obtener_historial(self):
        return self.historial_citas

class CitaMascota(Cita):
    def actualizar(self, **kwargs):
        for clave, valor in kwargs.item(): # Itera sobre los argumentos clave-valor proporcionados.
            if hasattr(self, clave):  # Verifica si el atributo existe en la instancia de la clase.
                setattr(self, clave, valor)  # Si el atributo existe, lo actualiza con el nuevo valor.

class SistemaVeterinaria: # # Define la clase "SistemaVeterinaria" que administra la información de los clientes de la veterinaria.
    def __init__(self): #Constructor de la clase. Inicializa la lista de clientes, que almacenará objetos de tipo Cliente.
        self.clientes = []
    
    
    # Método que permite registrar un nuevo cliente en el sistema.
    # Solicita al usuario que ingrese los datos necesarios y verifica que todos los campos sean completados.    
    def registrar_clientes(self):
        try:
            # Solicita los datos del cliente mediante la entrada del usuario.
            nombre = input("Por favor, ingrese el nombre del cliente:").strip()
            contacto = input("Por favor, ingrese el contacto: ").strip()
            direccion = input("Por favor, ingrese la direccion: ").strip()
            
            # Verifica si alguno de los campos está vacío y genera un error si es el caso.
            if not nombre or not contacto or not direccion:
                raise ValueError("Es obligatorio completar todos los campos.")
            
        except ValueError as e:
            # Captura el error si ocurre alguna excepción y muestra un mensaje de error.
            print(f"Error: {e}")

            
    #Método que permite registrar una nueva mascota asociada a un cliente.        
    def registrar_mascota(self):
        try:
            # Solicita el nombre del cliente para asociarlo a la mascota.
            nombre_cliente = input("Ingrese el nombre del cliente para asociar la mascota:").strip()
            # Busca al cliente en la lista de clientes.
            cliente = next((c for c in self.clientes if c.nombre == nombre_cliente),None)
            
            # Si no se encuentra el cliente, lanza un error.
            if not cliente:
                raise ValueError("No se encontró al cliente.")
            
            # Solicita los detalles de la mascota.
            nombre_mascota = input("Por favor, ingrese el nombre de la mascota:").strip()
            especie = input("Por favor, ingrese la especie: ").strip()
            raza = raza = input("Por favor, ingrese la raza: ").strip()
            edad = int(input("Por favor, ingrese la edad: ")).strip()
            
            # Verifica que los detalles de la mascota sean válidos.
            if not nombre_mascota or not especie or not raza or edad <= 0:
                raise ValueError("Detalles de la mascota inválidos.")
            
            # Crea una nueva mascota e asocia los detalles ingresados.
            mascota = RegistrarMascota(nombre_mascota, especie, raza, edad)
            cliente.agregar_mascota(mascota)
            print("¡Mascota registrada con éxito!")
            
        except ValueError as e:
            # Captura cualquier error relacionado con valores inválidos y muestra un mensaje de error.
            print(f"Error: {e}")
    
    #Método que permite programar una cita para una mascota asociada a un cliente.        
    def programar_cita(self): 
        try:
            # Solicita el nombre del cliente y el nombre de la mascota.
            nombre_cliente = input("Ingrese el nombre del cliente para asociar la mascota:").strip()
            nombre_mascota = input("Ingrese el nombre de la mascota:").strip()
            
            # Busca al cliente en la lista de clientes.
            cliente = next((c for c in self.clientes if c.nombre == nombre_cliente), None)
            
            # Si no se encuentra el cliente, lanza un error.
            if not cliente:
                raise ValueError("Cliente no encontrado.")
            
            # Busca la mascota asociada al cliente.
            mascota = next((m for m in cliente.mascotas if m.nombre == nombre_mascota), None)
            
            # Si no se encuentra la mascota, lanza un error.
            if not mascota:
                raise ValueError("Mascota no encontrada.")
            
            # Solicita la fecha, hora, servicio y nombre del veterinario para la cita.
            fecha = input("Ingrese la fecha (AAAA-MM-DD): ").strip()
            hora = input("Ingrese la hora (HH:MM): ").strip()
            servicio = input("Ingrese el servicio (consulta, vacunacion, etc): ").strip()
            veterinario = input("Ingrese el nombre del veterinario: ").strip()
            
            # Verifica que la fecha y hora tengan el formato adecuado.
            datetime.strptime(fecha, "%Y-%m-%d")
            datetime.strptime(hora, "%H:%M")
            
            # Valida que los detalles del servicio y veterinario sean válidos.
            if not servicio or not veterinario:
                raise ValueError("Detalles de la cita inválidos.")
            
            # Crea una nueva cita para la mascota.
            cita = CitaMascota(fecha, hora, servicio, veterinario)
            mascota.agregar_al_historial(cita)
            print("¡Cita programada con éxito!")
            
        except ValueError as e:
            # Captura cualquier error relacionado con valores inválidos y muestra un mensaje de error
            print(f"Error: {e}")
            
            
def actualizar_citas(self):
        try:
            # Solicita el nombre del cliente y el nombre de la mascota.
            nombre_cliente = input("Ingrese el nombre del cliente para asociar la mascota:").strip()
            nombre_mascota = input("Ingrese el nombre de la mascota:").strip()
        
            cliente = next((c for c in self.clientes if c.nombre == nombre_cliente),None)
            
            if not cliente:
                raise ValueError("Cliente no encontrado.")
            
            mascota =next((m for m in cliente.mascotas if m.nombre == nombre_mascota), None)
            if not mascota:
                raise ValueError("Mascota no encontrada.")
            
            if not mascota.historial_citas:
                raise ValueError("No hay citas registradas para esta mascota.")
            
            print("\nCitas disponibles para actualizar:")
            for i, cita in enumerate(mascota.historial_citas):
                