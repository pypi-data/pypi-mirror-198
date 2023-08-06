from .base import *


class orders(CreateableApiResource,UpdateableApiResource):
    resource_name = 'orders'
    print("resource_name::",resource_name)