from django import template


register = template.Library()



@register.filter()
def currency(value, code='rub'):
   """
   value: значение, к которому нужно применить фильтр
   code: код валюты
   """

   return f'{value} {code}'