from django import template

register=template.Library()



@register.filter(name='cut')
def cut(value,args):
    """
     This cuts off all the value of the string
    """

    return value.replace(args,'')




#register.filter('cut',cut)
