from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response
import os

def add_numbers(request):
    # Retrieve the numbers from the URL parameters
    num1 = request.matchdict['num1']
    num2 = request.matchdict['num2']
    
    # Perform addition
    result = int(num1) + int(num2)
    
    # Return the result as a response
    return Response(str(result))

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8080))
    with Configurator() as config:
        config.add_route('add', '/add/{num1}/{num2}')
        config.add_view(add_numbers, route_name='add')
        app = config.make_wsgi_app()
    server = make_server('0.0.0.0', port, app)
    print(f"Server running on port {port}")
    server.serve_forever()
