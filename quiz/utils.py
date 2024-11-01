from rest_framework import status
from rest_framework.views import exception_handler


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None:
        error = {'status': "failure", 'reason': str(response.data.items())}
        if response.status_code == status.HTTP_404_NOT_FOUND:
            error = {}
        response.data = error

    return response
