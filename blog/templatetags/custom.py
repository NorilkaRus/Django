from django import template
from django.db.models.fields.files import FieldFile


register = template.Library()


@register.simple_tag
@register.filter()
def mediapath(data: FieldFile) -> str:
    """
    Make url path to media

    Examples:
        <img src="{{ object.preview|mediapath }}" />
        or
        <img src="{% mediapath object.preview %}" />
    """
    return data.url if data else '#'
