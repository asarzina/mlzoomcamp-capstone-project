# Mlzoomcamp capstone project: image classification

[https://github.com/alexeygrigorev/mlbookcamp-code/tree/master/course-zoomcamp/12-capstone](https://github.com/alexeygrigorev/mlbookcamp-code/tree/master/course-zoomcamp/12-capstone)

Dataset: [https://www.kaggle.com/meowmeowmeowmeowmeow/gtsrb-german-traffic-sign](https://www.kaggle.com/meowmeowmeowmeowmeow/gtsrb-german-traffic-sign)

Goal: classify images with traffic signs.

## Description

The `ipynb` file is written and executed in Colab.

### Dataset

The dataset we’ll be using to train our own custom traffic sign classifier is the German Traffic Sign Benchmark https://www.kaggle.com/valentynsichkar/traffic-signs-preprocessed.

### Goal

Classify images of traffic signs.

### About the dataset

The dataset contains preprocessed data for Traffic Signs saved into some pickle files.

The images are in the following files:

- train.p
- valid.p
- test.p

There are about 34799 images. There are also a csv file with the list of sign categories (labels.csv).

### Data Preparation

I've converted the database into images and save them into some directories with the names from labels.csv.

### Model

I created a model using Keras libraries, layers and optimizers. I tried some parameters to find the best model.

### Export model

The final model is exported to h5 file and used in dockerized python script.

### Publish

The project is published to Heroku.

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

This example returns a probability that the image is a "stop" signal equal to **0.9991000294685364**.

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
