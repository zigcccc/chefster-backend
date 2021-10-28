from rest_framework_json_api.pagination import JsonApiPageNumberPagination


class ChefsterJSONAPIPagination(JsonApiPageNumberPagination):
    page_size_query_param = "size"
    page_query_param = "page"

    def get_paginated_response(self, data):
        response = super().get_paginated_response(data)
        response.data["meta"]["pagination"]["page_size"] = self.get_page_size(self.request)
        return response
