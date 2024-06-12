from drf_yasg import openapi

login_body_schema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'email': openapi.Schema(type=openapi.TYPE_STRING, description='Email of the user'),
        'password': openapi.Schema(type=openapi.TYPE_STRING, description='Password of the user'),
    }, required=['email', 'password']
)

login_success_schema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'refresh_token': openapi.Schema(type=openapi.TYPE_STRING, description='Refresh Token of the user'),
        'access_token': openapi.Schema(type=openapi.TYPE_STRING, description='Access Token of the user'),
    }
)

register_body_schema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'first_name': openapi.Schema(type=openapi.TYPE_STRING, description='First name of the user'),
        'last_name': openapi.Schema(type=openapi.TYPE_STRING, description='Last of the user'),
        'email': openapi.Schema(type=openapi.TYPE_STRING, description='Email of the user'),
        'email': openapi.Schema(type=openapi.TYPE_STRING, description='Email of the user'),
        'password': openapi.Schema(type=openapi.TYPE_STRING, description='Password of the user'),
        'password2': openapi.Schema(type=openapi.TYPE_STRING, description='Cofirm Password field'),
    }, required=['first_name', 'last_name', 'email', 'password', 'password2']
)

register_bad_request_schema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'field_name': openapi.Schema(type=openapi.TYPE_STRING, description='Error message')
    },
    example={"first_name": "This field may not be blank", "email": "User with this email already exists."}
)

user_response_schema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'id': openapi.Schema(type=openapi.TYPE_INTEGER, description='Unique id of the user'),
        'email': openapi.Schema(type=openapi.TYPE_STRING, description='Email of the user'),
        'is_staff': openapi.Schema(type=openapi.TYPE_BOOLEAN, description='Only staff members will has true value for this'),
        'first_name': openapi.Schema(type=openapi.TYPE_STRING, description='First name of the user'),
        'last_name': openapi.Schema(type=openapi.TYPE_STRING, description='Last name of the user'),
    }
)

subscription_schema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        'id': openapi.Schema(type=openapi.TYPE_INTEGER, description='Subscription id'),
        'start_date': openapi.Schema(type=openapi.TYPE_STRING, description='Starting date of the subscription'),
        'plan': openapi.Schema(type=openapi.TYPE_STRING, description='Price of the Subscription.'),
    }
)
subscriptions_array_schema = openapi.Schema(type=openapi.TYPE_ARRAY, items=subscription_schema)