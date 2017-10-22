import logging

from pyramid.response import Response
from pyramid.view import view_config

logging.basicConfig(level=logging.DEBUG)


@view_config(route_name="api", request_method='POST', renderer='json')
def apiPost(request):
    logging.info('api post')
    logging.info(request.params['id'])
    logging.info(request.params['name'])
    return {'message': 'OK'}


@view_config(route_name="api", request_method='GET', renderer='json')
def api(request):
    logging.info('api')
    return {'message': 'OK'}


@view_config(route_name="toy", request_method='GET', renderer='json')
def toy(request):
    logging.info('/toy')
    return {'id': 1, 'name': '玩具'}
