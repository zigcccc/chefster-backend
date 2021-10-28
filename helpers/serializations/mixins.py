class CreatorFieldFromRequestUserMixin:
    """
    Seralizer mixin that attaches user id from the
    current request Auth User to the creator field.
    """

    def to_internal_value(self, data):
        user_id = self.context["request"].user.id
        data["creator"] = user_id
        return super().to_internal_value(data)
