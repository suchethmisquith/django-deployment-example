from django import template

register = template.Library()



@register.filter(name='cut')
def cut(value, arg):
    """
    This cuts out all the values of arg
    """

    return value.replace(arg,'')

## changed below function with @register decorator.
# register.filter('cut',cut)
