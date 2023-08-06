from .base import *


class Tracking(CreateableApiResource,UpdateableApiResource):
    resource_name = 'tracking/carts'
    print("resource_name::",resource_name)
    


class TrackingBatch(CreateableApiResource,UpdateableApiResource):
    resource_name = 'tracking/carts/batch'
    print("resource_name::",resource_name)
    
    
    
class TrackingProductView(CreateableApiResource):
    resource_name = 'tracking/productview'
    print("resource_name::",resource_name)
    
    
    
class TrackingProductViews(CreateableApiResource):
    resource_name = 'tracking/productviews'
    print("resource_name::",resource_name)