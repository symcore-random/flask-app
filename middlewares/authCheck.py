from flask import g, request

def token_change():
    if request.method == 'GET':
        g.token='<tok>is get</tok>'
    else:
        g.token='<tok>not get</tok>'