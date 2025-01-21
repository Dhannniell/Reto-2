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
            
            