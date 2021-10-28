import re
from rest_framework_json_api.filters import QueryParameterValidationFilter


class ChefsterQueryParamValidationFilter(QueryParameterValidationFilter):
    query_regex = re.compile(r"^(sort|include)$|^(?P<type>filter|fields|page|size)(\[[\w\.\-]+\])?$")
