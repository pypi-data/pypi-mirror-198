import json
import requests

class Mapping(dict):
    """
    Mapping

    provides '.' access to dictionary keys
    """

    def __init__(self, mapping, *args, **kwargs):
        """
        Create a new mapping. Filters the mapping argument
        to remove any elements that are already methods on the
        object.

        For example, Orders retains its `coupons` method, instead
        of being replaced by the dict describing the coupons endpoint
        """

        mapping = mapping or {}
        print("inside mapping __init__ call:::::")

        filter_args = {k: mapping[k]
                       for k in mapping if k not in dir(self)}
        self.__dict__ = self
        dict.__init__(self, filter_args, *args, **kwargs)

    def __str__(self):
        """
        Display as a normal dict, but filter out underscored items first
        """
        return str({k: self.__dict__[k] for k in self.__dict__ if not k.startswith("_")})
    # Python program to demonstrate writing of __repr__ and

    def __repr__(self):
        return "<%s at %s, %s>" % (type(self).__name__, hex(id(self)), str(self))



class ApiResource(Mapping):
    print("Inside the ApiResource class")
    resource_name = ""  # The identifier which describes this resource in urls

    @classmethod
    def _create_object(cls, response, connection=None):
        if response and not isinstance(response, dict):
            #print("IF   response::")
            return [cls(obj, _connection=connection) for obj in response]
        else:
            #print("ELSE response::", response)
            return cls(response, _connection=connection)

    @classmethod
    def _make_request(cls, method, url, connection, data=None, params=None, headers=None):
        return connection.make_request(method, url, data, params, headers)

    
    @classmethod
    def _get_path(cls, id):
        print("_get_path_____",cls.resource_name, id)
        return "%s/%s" % (cls.resource_name, id)

    '''get method Without query parameter and with id'''

    @classmethod
    def get(cls, id, connection=None):
        response = cls._make_request('GET', cls._get_path(id), connection)
        #print("response in get", response)
        return cls._create_object(response, connection=connection)
    

    
    '''
    The get function without ID
    @classmethod
    def _get_path_(cls):
        #print("_get_path_____",cls)
        return "%s" % (cls.resource_name)
    
    @classmethod
    def _get_(cls, connection=None, **params):
        #print("before connection make request this get method called......", connection)
        response = cls._make_request(
            'GET', cls._get_path_(), connection, params=params)
        #print("response:: in get", response)
        return cls._create_object(response, connection=connection)
    '''

class ApiSubResource(ApiResource):
    parent_resource = ""
    parent_key = ""

    print("Inside the ApiSubResource class")

    @classmethod
    def _get_path(cls, id, parentid):
        return "%s/%s/%s/%s" % (cls.parent_resource, parentid, cls.resource_name, id)

    @classmethod
    def get(cls, parentid, id, connection=None, **params):
        print("***********inside get***********",parentid,id)
        response = cls._make_request('GET', cls._get_path(id, parentid), connection, params=params)
        return cls._create_object(response, connection=connection)
    

    def parent_id(self):
        print("parent-key:",parent_key)
        return self[self.parent_key]




class ListableApiResource(ApiResource):
    print("Inside the ListableApiResource class")
    
    @classmethod
    def _get_all_path(cls):
        return cls.resource_name
    
    @classmethod
    def all(cls, connection=None, **params):
        
         """
             Returns first page if no params passed in as a list.
         """
         request = cls._make_request('GET', cls._get_all_path(), connection, params=params)
         return cls._create_object(request, connection=connection)

    
class ListableApiSubResource(ApiSubResource):
    print("Inside the ListableApiSubResource class")
    
    @classmethod
    def _get_all_path(cls, parentid=None):
        # Not all sub resources require a parent id.  Eg: /api/v2/products/skus?sku=<value>
        if (parentid):
            return "%s/%s/%s" % (cls.parent_resource, parentid, cls.resource_name)
        else: 
            return "%s/%s" % (cls.parent_resource, cls.resource_name)

    @classmethod
    def all(cls, parentid=None, connection=None, **params):
        response = cls._make_request('GET', cls._get_all_path(parentid), connection, params=params)
        return cls._create_object(response, connection=connection)
         
    
    
    


class CreateableApiResource(ApiResource):
    print("Inside the CreateableApiResource class")
    @classmethod
    def _create_path(cls):
        return cls.resource_name

    @classmethod
    def create(cls, connection=None, **params):
        response = cls._make_request('POST', cls._create_path(), connection, data=params)
        return cls._create_object(response, connection=connection)
    
 



    
class CreateableApiSubResource(ApiSubResource): 
    print("Inside the CreateableApiSubResource class")  
    
    @classmethod
    def _create_path(cls, parentid):
        return "%s/%s/%s" % (cls.parent_resource, parentid, cls.resource_name)
    
    @classmethod
    def create(cls, parentid, connection=None, **params):
        response = cls._make_request('POST', cls._create_path(parentid), connection, data=params)
        return cls._create_object(response, connection=connection)

            



class UpdateableApiResource(ApiResource):
    print("Inside the UpdateableApiResource class")
    
    def _update_path(self):
        return "%s/%s" % (self.resource_name, self.id)
    
    def update(self, **updates):
        response = self._make_request('PUT', self._update_path(), self._connection, data=updates)
        return self._create_object(response, connection=self._connection)

    

class DeleteableApiResource(ApiResource):
    print("Inside the DeleteableApiResource class")
    
    def _delete_path(self):
        return "%s/%s" % (self.resource_name, self.id)

    def delete(self):
        return self._make_request('DELETE', self._delete_path(), self._connection)
    
    
    
        
class CountableApiResource(ApiResource):
    print("Inside the CountableApiResource class")   
    
    @classmethod
    def _count_path(cls):
        return "%s/count" % (cls.resource_name)
    
    @classmethod
    def count(cls, connection=None, **params):
        response = cls._make_request('GET', cls._count_path(), connection, params=params)
        return response['count']
        