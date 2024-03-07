# Use a imagem oficial do Python como base
FROM python:3.10

# Defina o diretório de trabalho no contêiner
WORKDIR /app

# Instale as dependências do projeto
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copie o código fonte para o contêiner
COPY . .

# Exponha a porta 8000 para acesso externo
EXPOSE 8000

# Comando para iniciar o servidor Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
