# Mlzoomcamp capstone project: image classificazione

[https://github.com/alexeygrigorev/mlbookcamp-code/tree/master/course-zoomcamp/12-capstone](https://github.com/alexeygrigorev/mlbookcamp-code/tree/master/course-zoomcamp/12-capstone)

Dataset: [https://www.kaggle.com/meowmeowmeowmeowmeow/gtsrb-german-traffic-sign](https://www.kaggle.com/meowmeowmeowmeowmeow/gtsrb-german-traffic-sign)

Goal: classify images with traffic signs.

## Description

The project is a classification problem. I want to classify images that contain traffic signs.

TODO...

## Repository

[https://github.com/asarzina/mlzoomcamp-capstone-project](https://github.com/asarzina/mlzoomcamp-capstone-project)

## Run locally with Docker

To run locally with Docker it's needed to comment the last line of Dockerfile

```Dockerfile
ENTRYPOINT ["gunicorn", "--bind=0.0.0.0:8080", "classification:app"]
# ENTRYPOINT ["gunicorn", "classification:app"]
```

```
docker build -t ml-zoomcamp-traffic-sign .

docker run -it --rm -p 8080:8080 ml-zoomcamp-traffic-sign:latest
```

## Demo APIs

Endpoint: [https://ml-zoomcamp-traffic-sign.herokuapp.com](https://ml-zoomcamp-traffic-sign.herokuapp.com)

### Heartbit API

GET `/heartbit`

Example:

```bash
curl --location --request GET 'https://ml-zoomcamp-traffic-sign.herokuapp.com/heartbit'
```

### Predict API

GET `/classification`

Example:

```bash
curl --location --request POST 'https://ml-zoomcamp-traffic-sign.herokuapp.com/classification' \
--header 'Content-Type: application/json' \
--data-raw '{
    "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c8/UK_traffic_sign_601.1.svg/2048px-UK_traffic_sign_601.1.svg.png"
}'
```

## Deploy to Heroku

To deploy to Heroku it's needed to uncomment the last line of Dockerfile

```Dockerfile
# ENTRYPOINT ["gunicorn", "--bind=0.0.0.0:8080", "classification:app"]
ENTRYPOINT ["gunicorn", "classification:app"]
```

- Install Heroku CLI locally (see [https://devcenter.heroku.com/articles/heroku-cli](https://devcenter.heroku.com/articles/heroku-cli))
- Login to Heroku
- Create Heroku app

```bash
heroku login

heroku container:login

heroku create ml-zoomcamp-traffic-sign
```

- Compile Docker image and deploy to Heroku

```bash
heroku container:push web -a ml-zoomcamp-traffic-sign

heroku container:release web -a ml-zoomcamp-traffic-sign
```
