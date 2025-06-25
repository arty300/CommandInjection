FROM python:3.13-slim

WORKDIR /app

# Install system dependencies with a single RUN command
RUN apt-get update && \
    apt-get install -y --no-install-recommends iputils-ping && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*


# Копируем зависимости и код
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . /app

# Создаём директорию и флаг
RUN mkdir -p /ctf && echo "CTF{command_injection_is_fun}" > /ctf/flag.txt && \
    chmod 400 /ctf/flag.txt && chown root:root /ctf/flag.txt && \
    chmod 700 /ctf

# Запускаем приложение
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "10000"]
