import logging

from rest_framework.response import Response
from rest_framework.views import exception_handler

from config.settings.request_opener import request_objects_retriever

logger = logging.getLogger("")


def error_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None:
        if response.status_code in [405, 429, 403]:
            return Response({"data": [], "success": False, "message": "درخواست نامعتبر"}, status=403)
        return response

    data = request_objects_retriever(context["request"])
    error = f"ERROR [{exc}] METHOD:{data['method']} REQUEST_PATH:{data['request_path']} REQUEST_BODY:{data['request_headers']} QUERY_PARAMS:{data['query_params']}"  # noqa:E501
    print("\033[93m" + error + "\033[0m")
    logger.critical(error, extra={"status_code": "500"})
    return Response({"data": [], "success": False, "message": "خطایی رخ داده است"}, status=400)
