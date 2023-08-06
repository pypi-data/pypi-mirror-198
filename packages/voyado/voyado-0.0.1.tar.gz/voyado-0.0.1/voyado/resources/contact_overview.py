from .base import *


class ContactOverview(ListableApiResource,CreateableApiResource,UpdateableApiResource,DeleteableApiResource):
    resource_name = 'contactoverview'
    print("resource_name::",resource_name)