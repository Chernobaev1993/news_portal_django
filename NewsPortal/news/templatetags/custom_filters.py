from django import template

register = template.Library()


@register.filter()
def censor(value):
    """
    value: значение, к которому нужно применить фильтр
    code: код валюты
    """
    text_new = str(value)
    bad_words = ['духовой', 'опытные', 'школьников']
    lst = value.split()
    for word in lst:
        if word in bad_words:
            censor_word = word[0] + (len(word) - 1) * '*'
            text_new = text_new.replace(word, censor_word)
    return text_new
