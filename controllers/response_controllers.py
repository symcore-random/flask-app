from flask import make_response, request, g


def get_all():
    return make_response({'message': f'g_token:{g.token} method:{request.method}'}, 200)

def get_by_id(id):
    return make_response({'message': f'g_token:{g.token} method:{request.method} id:{id}'}, 200)

def create():
    return make_response({'message': f'g_token:{g.token} method:{request.method}'}, 200)

def update(id):
    return make_response({'message': f'g_token:{g.token} method:{request.method} id:{id}'}, 200)

def remove(id):
    return make_response({'message': f'g_token:{g.token} method:{request.method} id:{id}'}, 200)