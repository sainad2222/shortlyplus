FROM python:3.9

WORKDIR /usr/local/app/backend/shortener

RUN pip install --upgrade pip

RUN python -m pip install --upgrade setuptools wheel

COPY . .

RUN pip install -r requirements.txt

EXPOSE 50051

CMD ["python", "./main.py"]
