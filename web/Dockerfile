FROM python:3.7-alpine

ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE walshsoft.settings

# Install GeoDjango dependencies
RUN apk add --no-cache --virtual .build-deps \
        --repository http://dl-cdn.alpinelinux.org/alpine/edge/testing \
        gdal-dev \
        geos-dev \
        proj4-dev

RUN apk add alpine-sdk zlib-dev expat expat-dev libxml2-dev

# Install spatialite from source
RUN apk add sqlite sqlite-dev

RUN wget "http://www.gaia-gis.it/gaia-sins/freexl-sources/freexl-1.0.4.tar.gz" \
    && tar zxvf freexl-1.0.4.tar.gz && cd freexl-1.0.4 && ./configure && make && make install

RUN wget "http://www.gaia-gis.it/gaia-sins/libspatialite-4.3.0a.tar.gz" \
    && tar zxvf libspatialite-4.3.0a.tar.gz && cd libspatialite-4.3.0a && ./configure && make && make install

RUN wget "http://www.gaia-gis.it/gaia-sins/readosm-sources/readosm-1.1.0.tar.gz" \
    && tar zxvf readosm-1.1.0.tar.gz && cd readosm-1.1.0 && ./configure && make && make install

RUN wget "http://www.gaia-gis.it/gaia-sins/spatialite-tools-sources/spatialite-tools-4.3.0.tar.gz" \
    && tar zxvf spatialite-tools-4.3.0.tar.gz && cd spatialite-tools-4.3.0 && ./configure && make && make install

RUN mkdir /code
WORKDIR /code/

ADD requirements.txt /code/
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

ADD . /code/

EXPOSE 8000

CMD ["gunicorn", "walshsoft.wsgi:application", "--bind", ":8000"]
