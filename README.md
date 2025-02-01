Notas para el Reto-2
Sistema de Gestión Veterinaria - Huella Feliz
Este proyecto es un sistema de gestión para clínicas veterinarias desarrollado con programación orientada a objetos en Python. Permite registrar clientes, mascotas, programar citas y gestionar historiales médicos de forma eficiente.

Características Principales
Registro de clientes: Almacena información básica de los dueños de mascotas (nombre, contacto, dirección).

Registro de mascotas: Asocia mascotas a clientes existentes con detalles como especie, raza y edad.

Gestión de citas:

Programación de citas con fecha, hora, servicio y veterinario asignado.

Actualización de citas existentes (fecha, hora, servicio o veterinario).

Historial médico: Consulta de todas las citas registradas para una mascota.

Validación de datos: Verificación de formatos de fecha/hora y campos obligatorios.

Requisitos
Python 3.6 o superior

Instalación y Ejecución
Clona o descarga el repositorio.

Ejecuta el script desde la terminal:

bash
Copy
python nombre_del_archivo.py
Uso
Al iniciar el sistema, se mostrará un menú interactivo con las siguientes opciones:

1. Registrar Cliente
Ingresa: Nombre, contacto y dirección.

Validaciones: Todos los campos son obligatorios.

2. Registrar Mascota
Requiere: Cliente existente.

Ingresa: Nombre de mascota, especie, raza y edad.

Validaciones: Edad debe ser número positivo.

3. Programar Cita
Requiere: Cliente y mascota existentes.

Ingresa:

Fecha (formato AAAA-MM-DD)

Hora (formato HH:MM)

Servicio (ej: consulta, vacunación)

Nombre del veterinario

Validaciones: Formato de fecha/hora correcto.

4. Actualizar Cita
Selecciona una cita existente.

Actualiza campos específicos (dejar vacíos los que no quieran modificarse).

5. Consultar Historial
Muestra todas las citas registradas para una mascota.

6. Salir
Cierra la aplicación.

Estructura de Clases
Diagrama de Clases Simplificado
Copy
Persona (Abstracta)
└── Cliente
    └── Mascotas[]

Mascota (Abstracta)
└── RegistrarMascota
    └── HistorialCitas[]

Cita (Abstracta)
└── CitaMascota

SistemaVeterinaria (Controlador Principal)
Detalles de Implementación
Clases Abstractas:

Persona: Base para clientes (implementa mostrar_informacion())

Mascota: Base para mascotas (implementa agregar_al_historial())

Cita: Base para citas (implementa actualizar())

Clases Concretas:

Cliente: Gestiona información de dueños y sus mascotas.

RegistrarMascota: Almacena datos de mascotas y su historial.

CitaMascota: Maneja detalles de citas con método de actualización flexible.

Sistema Principal:

SistemaVeterinaria: Coordina todas las operaciones mediante un menú interactivo.

Ejemplo de Flujo
Registrar cliente:

Copy
Nombre: María Gómez
Contacto: 555-1234
Dirección: Calle Flores 123
Registrar mascota:

Copy
Cliente: María Gómez
Nombre mascota: Toby
Especie: Perro
Raza: Golden Retriever
Edad: 5
Programar cita:

Copy
Fecha: 2024-03-20
Hora: 10:30
Servicio: Vacunación anual
Veterinario: Dr. Pérez