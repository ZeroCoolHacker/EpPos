import calendar

from django import template

register = template.Library()


@register.filter()
def percentof(amount, total):
    # https://medium.com/@hakibenita/hey-52138a2949a8
    try:
        return '{:.1f}%'.format(amount / total * 100)
    except ZeroDivisionError:
        return None
