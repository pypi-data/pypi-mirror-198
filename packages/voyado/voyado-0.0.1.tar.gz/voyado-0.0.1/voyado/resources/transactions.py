from .base import *


class Receipts(CreateableApiResource):
    resource_name = 'receipts'
    print("resource_name::",resource_name)
    
    
class Transactions(CreateableApiResource):
    resource_name = 'transactions'
    print("resource_name::",resource_name)