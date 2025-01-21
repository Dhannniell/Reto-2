from abc import ABC, abstractmethod
from datetime import datetime

class Persona(ABC):
    pass

class Mascota(ABC):
    pass

class Cita(ABC):
    pass

# Definicion de subclases

class Cliente(Persona):
    pass

class RegistrarMascota(Mascota):
    pass

class CitaMascota(Cita):
    pass

class SistemaVeterinaria:
    pass

