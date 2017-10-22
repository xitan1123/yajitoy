from pyramid.config import Configurator


def add_cors_headers_response_callback(event):
    def cors_headers(request, response):
        response.headers.update({
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET, POST, PUT, DELETE',
            'Access-Control-Allow-Headers': 'Origin, Content-Type, Accept, Authorization',
            'Access-Control-Allow-Credentials': 'true',
            'Access-Control-Max-Age': '1728000'
        })
    event.request.add_response_callback(cors_headers)

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)

    from pyramid.events import NewRequest
    config.add_subscriber(add_cors_headers_response_callback, NewRequest)

    config.include('pyramid_jinja2')
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('item', '/item')
    config.add_route('toy', '/toy')
    config.add_route('api', '/api')
    config.scan()
    return config.make_wsgi_app()
