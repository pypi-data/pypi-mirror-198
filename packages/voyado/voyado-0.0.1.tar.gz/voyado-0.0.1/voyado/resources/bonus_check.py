from .base import *


class Bonus():
    print("PromotionsAssign:>>>> ")
    resource_name = 'bonuschecks'
    
    def redeem(self, apiObj,parentid,id):
        print("bonus redeem called")
        print(" self.connection called......",apiObj.connection)
        connection = apiObj.connection
        return connection.make_request("POST", "/contacts/{}/bonuschecks/{}/redeem".format(parentid,id), data=None, params=None, headers=None)

    
    