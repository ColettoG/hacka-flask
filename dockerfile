# Use uma imagem base com Python
FROM python:3.10-slim

# Defina o diretório de trabalho
WORKDIR /app

# Copie os arquivos do projeto para o diretório de trabalho
COPY . /app

# Instale as dependências
RUN pip install --no-cache-dir pandas scikit-learn flask

# Exponha a porta em que a aplicação Flask será executada
EXPOSE 5000

# Comando para iniciar a aplicação Flask
CMD ["python", "app.py"]
