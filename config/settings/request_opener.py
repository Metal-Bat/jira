def request_objects_retriever(request: object) -> dict:
    """open request and get request items

    Args:
        request (object): request object

    Returns:
        dict: request items
    """
    method = str(getattr(request, "method", "")).upper()
    request_path = str(getattr(request, "get_full_path", ""))
    request_data = str(getattr(request, "data"))
    request_headers = str(getattr(request, "headers", ""))
    query_params = str([f"{k}: {v}" for k, v in request.GET.items()])
    query_params = query_params if query_params else ""

    data: dict = {
        "method": method,
        "request_path": request_path,
        "request_data": request_data,
        "request_headers": request_headers,
        "query_params": query_params,
    }

    return data
