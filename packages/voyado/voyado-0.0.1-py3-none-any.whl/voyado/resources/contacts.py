from .base import *


class Contacts(ListableApiResource,CreateableApiResource,UpdateableApiResource,DeleteableApiResource,CountableApiResource):
    resource_name = 'contacts'
    #print("customer class _____resource_name::",resource_name)
    
    def promote_to_member(self, id=None):
        if id:
            return PromoteToMember.get(self.id, id, connection=self._connection)
        else:
            pass
            """currently not avaialbale in voyado API'S"""
            #return PromoteToMember.all(self.id, connection=self._connection)
        
    def promotion(self,id=None):
        print("promotions::::::::::::::::::::")
        if id:
            return Promo.get(self.id, id, connection=self._connection)
        else:
            pass
            """currently not avaialbale in voyado API'S"""
            return Promo.all(self.id, connection=self._connection)
        
        
        
    def transactions(self,id=None):
        if id:
            return Transactions.get(self.id, id, connection=self._connection)
        else:
            pass
            """currently not avaialbale in voyado API'S"""
            #return Transactions.all(self.id, connection=self._connection)
        
    
    def update_contact_type(self,id=None):
        if id:
            return UpdateContactType.get(self.id, id, connection=self._connection)
        else:
            pass
            """currently not avaialbale in voyado API'S"""
            #return UpdateContactType.all(self.id, connection=self._connection)
        
        
    def unsubscribe_Email(self,id=None):
        if id:
            return UnsubscribeEmail.get(self.id, id, connection=self._connection)
        else:
            #pass
            """currently not avaialbale in voyado API'S"""
            return UnsubscribeEmail.all(self.id, connection=self._connection)
            
        
    def bonuschecks(self,id=None):
        if id:
            return BonusChecks.get(self.id, id, connection=self._connection)
        else:
            pass
            #return BonusChecks.get(self.id, connection=self._connection)
            
    def bonuscheck_available(self,id=None):
        #if id:
            BonusChecksAvailable.all(self.id, connection=self._connection)
        #else:
            
    def bonuscheck_redeemed(self,id=None):
        #if id:
            BonusChecksRedeemed.all(self.id, connection=self._connection)
       



class PromoteToMember(CreateableApiSubResource):
    resource_name = 'promoteToMember'
    parent_resource = 'contacts'
    parent_key = 'contact_id'
    
    
class Promo(ListableApiSubResource):
    print("here is promotions")
    # resource_name = 'options'
    # parent_resource = 'products'
    parent_key = 'contact_id'
    resource_name = 'promotions'
    parent_resource = 'contacts'
    count_resource = 'contacts/promotions' 
    
class Transactions(ListableApiSubResource):
    resource_name = 'transactions'
    parent_resource = 'contacts'
    parent_key = 'contact_id'
    count_resource = 'contacts/transactions'
    
    
class UpdateContactType(CreateableApiSubResource):
    resource_name = 'updateContactType'
    parent_resource = 'contacts'
    parent_key = 'contact_id'
    count_resource = 'contacts/updateContactType'
    
    
class UnsubscribeEmail(ListableApiSubResource):
    resource_name = 'unsubscribeEmail'
    parent_resource = 'contacts'
    parent_key = 'contact_id'
    count_resource = 'contacts/bykey'
    
class BonusChecks(ListableApiSubResource):
    resource_name = 'bonuschecks'
    parent_resource = 'contacts'
    parent_key = 'contact_id'
    count_resource = 'contacts/bonuschecks'
    
class BonusChecksAvailable(ListableApiSubResource):
    # resource_name = 'bonuschecks/available'
    # parent_resource = 'contacts'
    resource_name = 'payment_actions/capture'
    parent_resource = 'orders'
    parent_key = 'contact_id'
    count_resource = 'bonuschecks/available'

class BonusChecksRedeemed(ListableApiSubResource):
    resource_name = 'bonuschecks/redeemed'
    parent_resource = 'contacts'
    parent_key = 'contact_id'
    count_resource = 'bonuschecks/redeemed'
    

    


    
        
    
    
    