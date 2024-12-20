import random
from .tec_db import *

def setup_tec_db():
    # Lista de 200 nombres únicos
    nombres = [
        'Carlos', 'Ana', 'Luis', 'Maria', 'Jorge', 'Sofia', 'Raul', 'Gabriela', 'Pedro', 'Lucia',
        'Andres', 'Laura', 'David', 'Marta', 'Juan', 'Elena', 'Roberto', 'Patricia', 'Alberto', 'Daniela',
        'Fernando', 'Isabel', 'Jose', 'Beatriz', 'Ricardo', 'Carmen', 'Victor', 'Angela', 'Francisco', 'Adriana',
        'Cristian', 'Veronica', 'Miguel', 'Sandra', 'Enrique', 'Julia', 'Oscar', 'Paula', 'Eduardo', 'Claudia',
        'Manuel', 'Monica', 'Hector', 'Rosa', 'Felipe', 'Irene', 'Sebastian', 'Natalia', 'Gonzalo', 'Alejandra',
        'Ramiro', 'Noelia', 'Sergio', 'Lorena', 'Marcos', 'Esther', 'Rafael', 'Valeria', 'Guillermo', 'Eva',
        'Pablo', 'Ines', 'Esteban', 'Vanessa', 'Salvador', 'Silvia', 'Rodrigo', 'Alicia', 'Nicolas', 'Cristina',
        'Julio', 'Miriam', 'Agustin', 'Rebeca', 'Leandro', 'Teresa', 'Alvaro', 'Olga', 'Bruno', 'Yolanda',
        'Emilio', 'Sonia', 'Federico', 'Nuria', 'Hugo', 'Tamara', 'Leonardo', 'Belen', 'Joaquin', 'Sara',
        'Diego', 'Carolina', 'Martín', 'Lourdes', 'Ramón', 'Elisa', 'Vicente', 'Amparo', 'Simón', 'Raquel',
        'Mateo', 'Daniel', 'Santiago', 'Valentina', 'Alejandro', 'Samantha', 'Emiliano', 'Victoria', 
        'Camila', 'María', 'Ángel', 'José', 'Martina', 'Álvaro', 'Fernanda', 'Clara', 'Lucas', 'Patricia',
        'Alberto', 'Gloria', 'Tomás', 'Ximena', 'Pablo', 'Elías', 'Sara', 'Noah', 'Ingrid', 'Álex', 'Emma', 
        'Eva', 'Rafael', 'Guillermo', 'Bianca', 'Álvaro', 'Isabel', 'Dario', 'Silvia', 'Alina', 'Eduardo',
        'John', 'Emily', 'Michael', 'Olivia', 'James', 'Sophia', 'William', 'Emma', 'Benjamin', 'Ava',
        'Lucas', 'Mia', 'Henry', 'Isabella', 'Alexander', 'Amelia', 'Sebastian', 'Evelyn', 'Daniel', 'Harper',
        'Matthew', 'Ella', 'Joseph', 'Aria', 'David', 'Luna', 'Andrew', 'Camila', 'Samuel', 'Scarlett',
        'Christopher', 'Aurora', 'Anthony', 'Layla', 'Joshua', 'Chloe', 'Dylan', 'Grace', 'Nathan', 'Zoe',
        'Ryan', 'Riley', 'Isaac', 'Nora', 'Thomas', 'Hazel', 'Liam', 'Lily', 'Ethan', 'Sophie', 'Mason', 'Violet',
        'Logan', 'Ellie', 'Jacob', 'Stella', 'Jackson', 'Paisley', 'Caleb', 'Mila', 'Grayson', 'Addison',
        'Jack', 'Lucy', 'Owen', 'Savannah', 'Gabriel', 'Madeline', 'Carter', 'Victoria', 'Wyatt', 'Brooklyn',
        'Luke', 'Hannah', 'Jayden', 'Aubrey', 'Levi', 'Bella', 'Julian', 'Samantha', 'Elijah', 'Willow'
    ]

    users_tec = []

    for nombre in nombres:
        email = f'{nombre.lower()}@estudiantec.cr'
        password = nombre.lower()

        user_tec = User(
            email=email,
            password=password
        )

        users_tec.append(user_tec)

    session.add_all(users_tec)
    session.commit()
