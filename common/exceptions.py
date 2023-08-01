from rest_framework import status
from rest_framework.exceptions import APIException


class PermissionException(APIException):
    status_code = status.HTTP_403_FORBIDDEN
    # default_detail = PermissionMsg.PERMISSION_DENIED
    default_code = 'permission_denied'
