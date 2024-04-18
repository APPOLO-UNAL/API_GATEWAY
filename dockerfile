# Usamos la imagen oficial de Python
FROM python:3.9-slim

# Establecemos el directorio de trabajo en /app
WORKDIR /app

# Copiamos los archivos de requerimientos al contenedor
COPY requirements.txt requirements.txt

# Instalamos las dependencias usando pip
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos todos los archivos del directorio actual al contenedor en /app
COPY . .

# Exponemos el puerto 5000 en el contenedor
EXPOSE 5000

# Comando para ejecutar la aplicación
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5000"]