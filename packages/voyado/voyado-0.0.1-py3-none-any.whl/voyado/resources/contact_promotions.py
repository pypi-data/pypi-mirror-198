from .base import *


class ContactPromotions():
    print("PromotionsAssign:>>>> ")
    resource_name = 'contact_promotions'
    
    def assign(self, apiObj,parentid,id):
        print("PromotionsAssign: assign called")
        print(" self.connection called......",apiObj.connection)
        connection = apiObj.connection
        return connection.make_request("POST", "/contacts/{}/promotions/{}/assign".format(parentid,id), data=None, params=None, headers=None)
    
    def redeem(self, apiObj,parentid,id,params):
        print("PromotionsAssign: redeem called")
        print(" self.connection called......",apiObj.connection)
        connection = apiObj.connection
        return connection.make_request("POST", "/contacts/{}/promotions/{}/redeem".format(parentid,id), data=None, params=params, headers=None)

    
    