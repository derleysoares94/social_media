from django import template
from ..models import Membership

register = template.Library()

@register.filter
def is_member(user, community):
    return Membership.objects.filter(user=user, community=community).exists()