# middleware.py
import logging

class RequestResponseLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        # Logging relevant information
        logging.info(f"URL: {request.path}, Method: {request.method}, User: {request.user}")

        return response
