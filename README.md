# Streamy

A self-hosted video streaming platform designed to be used with [OBS](https://obsproject.com/).


## Project goals

* simple to use
* low video latency
* dockerized deployment


## Design

Video is ingested via [nginx-http-flv-module](https://github.com/winshining/nginx-http-flv-module/) using rtmp, and it is converted to HTTP-FLV. The web player uses [flv.js](https://github.com/Bilibili/flv.js) to play this video stream, but rtmp playback using VLC or some other player is also possible.

Backend is implemented using [django](https://www.djangoproject.com/).

Transcoding is not currently supported and all streams are at source quality.


## Usage (deployment)

Create a `django.env` with the following contents:

    SECRET_KEY=yoursecretkey

Start the containers:

    docker-compose up --build -d

Create a superuser:

    docker-compose run --rm backend python manage.py createsuperuser

The backend is now available at [http://localhost:8000](http://localhost:8000).


## License

MIT
