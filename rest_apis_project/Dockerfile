
FROM python:3.12.3-slim 

RUN apt-get update && apt-get install -y curl

WORKDIR /home/root
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .

EXPOSE 8000

CMD ["uvicorn", "main:app"]
