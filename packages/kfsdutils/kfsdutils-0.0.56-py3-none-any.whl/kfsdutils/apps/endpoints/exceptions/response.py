from rest_framework.exceptions import ValidationError
from rest_framework.exceptions import APIException

class KubefacetsException(APIException):
    default_detail = "Unexpected Error"
    status_code = 500
    default_code = "unexpected_error"

    def __init__(self, detail, defaultCode, statusCode):
        self.detail = detail
        self.status_code = statusCode
        self.default_code = defaultCode