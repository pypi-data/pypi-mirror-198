class ApiError(Exception):
    pass


class RequestError(ApiError):
    pass


class XmlError(ApiError):
    pass
