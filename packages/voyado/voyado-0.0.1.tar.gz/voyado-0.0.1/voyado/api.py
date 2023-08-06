
import os
import sys
from voyado.connection import Connection, OAuthConnection
# Needed for voyado-ApiResourceWrapper dynamic loading
from voyado.resources import *


class VoyadoApi(object):

    def __init__(self, api_url,store_key):
        self.api_service = os.getenv('API_ENDPOINT', api_url+'.voyado.com')
        self.api_path="/api/v2/{}"
        print("Entry point")
        if api_url:
            self.connection = OAuthConnection(self.api_service,self.api_path,store_key)
        else:
            raise Exception(
                "Must provide either (client_id and store_hash) or (host and basic_auth)")

    def __getattr__(self, item):
        
        """object. __getattr__(self, name) Is an object method that is called if the object's properties are not found. This method should 
        return the property value or throw AttributeError . Note that if the object property can be found through the normal mechanism, it will not be called."""

        return voyado_ApiResourceWrapper(item, self)





class voyado_ApiResourceWrapper(object):
    """
    Provides dot access to each of the API resources
    while proxying the connection parameter so that
    the user does not need to know it exists
    """

    def __init__(self, resource_class, api):
        """
        :param resource_class: String or Class to proxy
        :param api: API whose connection we want to use
        :return: A wrapper instance
        """
        if isinstance(resource_class, str):#check resource is  string or not
            self.resource_class = self.str_to_class(resource_class)
        else:
            self.resource_class = resource_class
        self.connection = api.connection


    def __getattr__(self, item):
        print("ApiResourceWrapper class __gettarr__ called gives name of method", item)
    
        result = lambda *args, **kwargs: (getattr(self.resource_class, item))(
            *args, connection=self.connection, **kwargs)        
        return result
        # return lambda *args, **kwargs: (getattr(self.resource_class, item))(*args, connection=self.connection, **kwargs)


    @classmethod
    def str_to_class(cls, str):
        """
        Transforms a string class name into a class object
        Assumes that the class is already loaded.
        """
        """getattr fun use to access attribute or variable from class object so it will return  attribute
              contact  <class 'voyado_resources.contacts.Contacts>"""

        return getattr(sys.modules[__name__], str)



