from rest_framework_json_api.pagination import JsonApiLimitOffsetPagination

from common.pagination import ChefsterJSONAPIPagination


class NoExtraFieldsQueryParamValidationMixin:
    # noinspection PyUnresolvedReferences
    def validate(self, attrs):
        attrs = super().validate(attrs)

        valid_keys = [
            ChefsterJSONAPIPagination.page_query_param,
            ChefsterJSONAPIPagination.page_size_query_param,
            JsonApiLimitOffsetPagination.limit_query_param,
            JsonApiLimitOffsetPagination.offset_query_param,
        ]

        return attrs


class CurrentUserDefault:
    """
    May be applied as a `default=...` value on a serializer field.
    Returns the current user.
    """

    requires_context = True

    def __call__(self, serializer_field):
        print(serializer_field.context["request"])
        return serializer_field.context["request"].user
