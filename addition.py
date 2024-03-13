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
    
    # Create HTML response with larger font size
    html_response = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Addition Result</title>
        <style>
            body {{
                font-size: 24px; /* Increase font size */
            }}
        </style>
    </head>
    <body>
        <h1>Result:</h1>
        <p>The sum of {num1} and {num2} is: <span style="font-size: 36px;">{result}</span></p>
    </body>
    </html>
    """

    # Return the result as a response
    return Response(html_response, content_type='text/html')

def multiply_numbers(request):
    # Retrieve the numbers from the URL parameters
    num1 = request.matchdict['num1']
    num2 = request.matchdict['num2']
    
    # Perform multiplication
    result = int(num1) * int(num2)
    
    # Create HTML response with larger font size
    html_response = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Multiplication Result</title>
        <style>
            body {{
                font-size: 24px; /* Increase font size */
            }}
        </style>
    </head>
    <body>
        <h1>Result:</h1>
        <p>The product of {num1} and {num2} is: <span style="font-size: 36px;">{result}</span></p>
    </body>
    </html>
    """

    # Return the result as a response
    return Response(html_response, content_type='text/html')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8080))
    with Configurator() as config:
        config.add_route('add', '/add/{num1}/{num2}')
        config.add_view(add_numbers, route_name='add')

        config.add_route('multiply', '/multiply/{num1}/{num2}')
        config.add_view(multiply_numbers, route_name='multiply')

        app = config.make_wsgi_app()
    server = make_server('0.0.0.0', port, app)
    print(f"Server running on port {port}")
    server.serve_forever()


# editing in feature branch
# added another line
# dev

# editing in feature branch
# sample line
>>>>>>> a6aba81 (edited by nd)
