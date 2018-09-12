import os

import falcon

import resources


def create_app(image_store):
    api = falcon.API()
    api.add_route('/resources', resources.Collection(image_store))
    api.add_route('/resources/{name}', resources.Item(image_store))
    return api


def get_app():
    storage_path = os.environ.get('FALCON_STORAGE_PATH', '/tmp')
    image_store = resources.ImageStore(storage_path)
    return create_app(image_store)
