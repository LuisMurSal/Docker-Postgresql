# Usar una imagen base con Python
FROM python:3.10-slim

# Establecer el directorio de trabajo
WORKDIR /app

# Instalar dependencias
RUN apt-get update && apt-get install -y postgresql-client && apt-get clean

# Copiar el archivo requirements.txt y luego instalar las dependencias de Python
COPY ./requirements.txt /app
RUN pip install --no-cache-dir -r requirements.txt

# Copiar la aplicación y el script de generación de datos
COPY ./app /app
COPY ./scripts/generate_fake_data.py /scripts/generate_fake_data.py

# Exponer el puerto 5000 para Flask
EXPOSE 5000

# Configurar el comando para ejecutar el script de generación de datos fake al inicio
CMD python3 /scripts/generate_fake_data.py && python3 /app/app.py
