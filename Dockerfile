FROM agrigorev/zoomcamp-model:3.8.12-slim

RUN apt-get update && apt-get install -y libgomp1
RUN pip install pipenv

COPY ["Pipfile", "Pipfile.lock", "./"]

RUN pipenv install --system --deploy

COPY ["classification.py", "traffic-sign-model.h5", "./"]

EXPOSE 8080

ENTRYPOINT ["gunicorn", "--bind=0.0.0.0:8080", "classification:app"]
#ENTRYPOINT ["gunicorn", "classification:app"]