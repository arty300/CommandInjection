FROM python:3.13-slim

WORKDIR /app


RUN apt-get update && \
    apt-get install -y --no-install-recommends iputils-ping && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*


COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . /app


RUN mkdir -p /ctf && echo "ACTF{c0mm@Nd_1nj3c710n}" > /ctf/flag.txt && \
    chmod 400 /ctf/flag.txt && chown root:root /ctf/flag.txt && \
    chmod 700 /ctf

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "10000"]
