FROM agrigorev/zoomcamp-model:3.8.12-slim

RUN pip install pipenv
RUN pip install keras-image-helper
RUN pip install https://github.com/alexeygrigorev/tflite-aws-lambda/raw/main/tflite/tflite_runtime-2.7.0-cp38-cp38-linux_x86_64.whl

WORKDIR /app

COPY ["Pipfile", "Pipfile.lock", "./"]

RUN pipenv install --system --deploy

COPY ["classification.py", "traffic-sign-model.tflite", "./"]

EXPOSE 8080

ENTRYPOINT ["gunicorn", "--bind=0.0.0.0:8080", "classification:app"]
#ENTRYPOINT ["gunicorn", "classification:app"]