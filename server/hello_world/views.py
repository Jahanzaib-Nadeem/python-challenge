from rest_framework import response, decorators as rest_decorators
from drf_yasg.utils import swagger_auto_schema

@swagger_auto_schema(
    method='get',
    operation_description="Dummy payView method",
    responses={
        200: 'This is a dummy GET method that currently always returns success',
    }
)

@rest_decorators.api_view(["GET"])
def payView(request):
    return response.Response({"msg": "Success"}, 200)