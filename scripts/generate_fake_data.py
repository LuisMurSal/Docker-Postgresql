from faker import Faker
import psycopg2

# Configuración de la base de datos
DATABASE_URL = 'postgresql://flaskuser:flaskpassword@db:5432/flaskdb'

# Crear una instancia de Faker
fake = Faker()

# Conexión a la base de datos PostgreSQL
conn = psycopg2.connect(DATABASE_URL)
cursor = conn.cursor()

# Crear una tabla si no existe
cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100),
        address VARCHAR(255),
        email VARCHAR(100)
    );
""")

# Generar 10 usuarios falsos y agregarlos a la base de datos
for _ in range(10):
    name = fake.name()
    address = fake.address()
    email = fake.email()
    
    cursor.execute("INSERT INTO users (name, address, email) VALUES (%s, %s, %s)", (name, address, email))

# Guardar los cambios y cerrar la conexión
conn.commit()
cursor.close()
conn.close()

print("Datos falsos generados correctamente.")
