from .base import *


class Promotions(ListableApiResource,CreateableApiResource,UpdateableApiResource,DeleteableApiResource):
    resource_name = 'promotions/codes'
    print("resource_name::",resource_name)
    
    def pro_redeem(self,id=None):
        if id:
            return Proredeem.get(self.id, id, connection=self._connection)
        else:
            #pass
            """currently not avaialbale in voyado API'S"""
            return Proredeem.all(self.id, connection=self._connection)
    
    
class Proredeem(CreateableApiSubResource):
    resource_name = 'redeem'
    parent_resource = 'promotions/codes'
    parent_key = 'promotion_id'