from datetime import date, datetime
import random
from app.database import *
from app.tec_db import setup_tec_db

# Ejemplo de inserción de datos

# 1. Agregar marcas de vehículos
brands = [Brand(name=name) for name in ["Toyota", "Honda", "Chevrolet", "Ford", "Nissan", "Mazda", "Hyundai", "Kia", "Volkswagen", "Subaru"]]
session.add_all(brands)
session.commit()

# 2. Agregar tipos de vehículos
vehicle_types = [VehicleType(name=name) for name in ["Sedan", "SUV", "Pickup", "Van", "Coupe", "Hatchback", "Convertible", "Wagon"]]
session.add_all(vehicle_types)
session.commit()

# 3. Agregar tipos de usuario
user_types = [UserType(name=name) for name in ["Base-User", "Super-Admin", "Institution-Admin"]]
session.add_all(user_types)
session.commit()

# 4. Agregar estados de viaje
trip_statuses = [
    TripStatus(name="Active"),
    TripStatus(name="Completed"),
    TripStatus(name="Cancelled"),
    TripStatus(name="Pending"),
    TripStatus(name="Scheduled")
]
session.add_all(trip_statuses)
session.commit()

# 5. Agregar géneros
genders = [Gender(name=name) for name in ["Male", "Female", "Other"]]
session.add_all(genders)
session.commit()

# 6. Agregar instituciones
institutions = [
    Institution(name="Instituto Tecnológico de Costa Rica", description="Institución de educación superior", address="Cartago, Costa Rica", acronym="TEC"),
    Institution(name="Universidad de Costa Rica", description="Universidad pública", address="San José, Costa Rica", acronym="UCR"),
    Institution(name="Universidad Nacional", description="Universidad pública", address="Heredia, Costa Rica", acronym="UNA"),
    Institution(name="ULACIT", description="Universidad privada", address="San José, Costa Rica", acronym="ULACIT"),
]
session.add_all(institutions)
session.commit()

# 7. Agregar usuarios
users = []
for i in range(1, 21):
    user = User(
        first_name=f'User{i}',
        first_surname='Surname',
        second_surname='Surname',
        identification=123456789 + i,
        birth_date=date(1995 + (i % 5), (i % 12) + 1, (i % 28) + 1),
        institutional_email=f'user{i}@example.com',
        phone_number=f'12345{i}',
        dl_expiration_date=date(2025 + (i % 5), (i % 12) + 1, (i % 28) + 1),
        gender_id=genders[i % len(genders)].id,
        user_type_id=user_types[i % len(user_types)].id,
        institution_id=institutions[i % len(institutions)].id
    )
    users.append(user)

session.add_all(users)
session.commit()

# 8. Agregar vehículos
vehicles = []
for i in range(1, 21):
    vehicle = Vehicle(
        license_plate=f'ABC{i:03d}',
        year=str(2010 + (i % 10)),
        max_capacity=5 + (i % 3),
        description='Sedan' if i % 2 == 0 else 'SUV',
        owner_id=users[i % len(users)].id,
        vehicle_type_id=vehicle_types[i % len(vehicle_types)].id,
        brand_id=brands[i % len(brands)].id
    )
    vehicles.append(vehicle)

session.add_all(vehicles)
session.commit()

# 9. Agregar paradas
stops = [
    Stop(latitude='9.9357', longitude='-84.0518', name='Cartago', description='Parada en Cartago'),
    Stop(latitude='9.9333', longitude='-84.0833', name='San José', description='Parada en San José'),
    Stop(latitude='9.9275', longitude='-84.0454', name='Heredia', description='Parada en Heredia'),
    Stop(latitude='9.9333', longitude='-84.1250', name='Alajuela', description='Parada en Alajuela'),
    Stop(latitude='9.9285', longitude='-84.0554', name='Liberia', description='Parada en Liberia'),
]
session.add_all(stops)
session.commit()

# 10. Agregar viajes
trips = []
for i in range(1, 21):
    trip = Trip(
        passenger_limit=4 + (i % 3),
        fare_per_person=1000 + (i * 100),
        route_url='https://goo.gl/maps/123456',
        departure_datetime=datetime(2024, 9, 25, 12 + (i % 12), 30),
        driver_id=users[i % len(users)].id,
        starting_point_id=stops[i % len(stops)].id,
        finishing_point_id=stops[(i + 1) % len(stops)].id,
        trip_status_id=trip_statuses[i % len(trip_statuses)].id,
        vehicle_id=vehicles[i % len(vehicles)].id
    )
    trips.append(trip)

session.add_all(trips)
session.commit()


# 11. Agregar pasajeros a los viajes
trip_passengers_list = []
for trip in trips:
    # Seleccionar un número aleatorio de pasajeros para cada viaje, 
    # garantizando que no haya duplicados y que no exceda el límite de pasajeros.
    num_passengers = min(trip.passenger_limit, len(users))
    passengers = random.sample(users, num_passengers)  # Selecciona pasajeros aleatorios

    for passenger in passengers:
        trip_passenger_entry = {
            'trip_id': trip.id,
            'user_id': passenger.id,
            'pickup_stop_id': stops[i % len(stops)].id  # Puedes seleccionar una parada de forma lógica
        }
        trip_passengers_list.append(trip_passenger_entry)

# Insertar múltiples registros en la tabla de asociación
session.execute(trip_passengers.insert(), trip_passengers_list)
session.commit()

print("Base de Datos poblada con éxito")

setup_tec_db()

