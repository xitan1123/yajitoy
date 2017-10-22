import logging

from pyramid.view import view_config

logging.basicConfig(level=logging.DEBUG)


@view_config(route_name='home', renderer='templates/mytemplate.jinja2')
def my_view(request):
    logging.info('root /GET')
    return {'project': 'yajitoy'}
