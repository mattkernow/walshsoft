from json import dumps
import requests

from django.contrib.gis.geos import Point
from django.core.serializers import serialize
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseServerError

from postcode_api.models import Postcode


class PostcodeNotFoundError(Exception):
    pass


class PostcodeServiceError(Exception):
    pass


def postcode(request, postcode):
    try:
        postcode = _get_postcode(postcode)
        as_geojson = serialize('geojson', [postcode], geometry_field='geom', fields=('postcode',), srid=27700)
        return HttpResponse(as_geojson, content_type='application/json')

    except PostcodeNotFoundError as e:
        return HttpResponseNotFound(dumps({'error': str(e)}), content_type='application/json')

    except PostcodeServiceError as e:
        return HttpResponseServerError(content={'error': str(e)}, content_type='application/json')


def _get_postcode(postcode):
    url = f'https://api.postcodes.io/postcodes/{postcode}'
    r = requests.get(url)
    if r.status_code == 200:
        result = r.json().get('result')
        geom = Point(result.get('eastings'), result.get('northings'))
        postcode_model = Postcode(postcode=postcode, geom=geom)
        return postcode_model
    elif r.status_code == 404:
        raise PostcodeNotFoundError(f"Postcode '{postcode}' not found")
    else:
        raise PostcodeServiceError('Postcode service error')
