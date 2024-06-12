from rest_framework import response, decorators as rest_decorators, permissions as rest_permissions
from drf_yasg.utils import swagger_auto_schema

@swagger_auto_schema(
    method='post',
    operation_description="Dummy pay subscriptions method",
    responses={
        200: 'This is a dummy POST method that currently always returns success',
    }
)

@rest_decorators.api_view(["POST"])
@rest_decorators.permission_classes([rest_permissions.IsAuthenticated])
def paySubscription(request):
    return response.Response({"msg": "Success"}, 200)

@swagger_auto_schema(
    method='post',
    operation_description="Dummy List subscriptions method",
    responses={
        200: 'This is a dummy POST method that currently always returns success',
    }
)

@rest_decorators.api_view(["POST"])
@rest_decorators.permission_classes([rest_permissions.IsAuthenticated])
def listSubscriptions(request):
    return response.Response({"msg": "Success"}, 200)
