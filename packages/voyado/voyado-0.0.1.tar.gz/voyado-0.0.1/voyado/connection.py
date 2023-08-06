import logging as log
import requests

from json import dumps, loads
from math import ceil
from time import sleep
import json
try:
    from urllib import urlencode
except ImportError:
    from urllib.parse import urlencode


from requests.utils import requote_uri
from voyado.exception import *


class Connection(object):
    """
    Connection class manages the connection to the Bigcommerce REST API.
    """
    def __init__(self, host, auth, api_path='/api/v2/{}'):
        self.host = host
        self.api_path = api_path
     
        #print("API Host or path connection init___: %s/%s" % (self.host, self.api_path))
        # self.auth = auth
        # self.headers = {"Accept": "application/json"}
        self._last_response = None  # for debugging
        # create a session object
        self.timeout = 7.0  # need to catch timeout?
        self._session = requests.Session()
        self._session.auth = auth
        self._session.headers = {"Accept": "application/json"}

        self.__resource_meta = self.get()  # retrieve metadata about urls and resources
                    
    def full_path(self, url):
        #print("connection class full path___________",url)
        #print("path is :::", "https://" +self.host + self.api_path.format(url))
        return "https://" + self.host + self.api_path.format(url)


    def _run_method(self, method, url, data=None, query=None, headers=None):
        if query is None:
            query = {}
        if headers is None:
            headers = {}
    
        # make full path if not given
        if url and url[:4] != "http":
          
            if url[0] == '/':
                print("url if ::::",url)
               # can call with /resource if you want
                url = url[1:]
            url = self.full_path(url)
            print("url run method ::::",url)
        elif not url:  # blank path
            print("elif:::",url)
            url = self.full_path(url)

        qs = urlencode(query)
        if qs:
            qs = "?" + qs
        url += qs

        # mess with content
        if data:
            if not headers:  # assume JSON
                data = dumps(data)
                headers = {'Content-Type': 'application/json'}
            if headers and 'Content-Type' not in headers:
                data = dumps(data)
                headers['Content-Type'] = 'application/json'

        log.debug("%s %s" % (method, url))
        print("run___methods:", method, "url:", url, "data::",data, "headers::", self._session.headers)
        
        # make and send the request
        return self._session.request(method, url, data=data, headers=self._session.headers)
        ''' Making a call to API without using session '''
            # return requests.get( url, data=data, headers={"Accept": "application/json","X-Auth-token":"mcybbwc6bsu66qvdg44of9061g6e9cv"})
            
            
    def make_request(self, method, url, data=None, params=None, headers=None):
        response = self._run_method(method, url, data, params, headers)
        print("response",response,"response headers",response.status_code)
        return self._handle_response(url, response)


    def _handle_response(self, url, res, suppress_empty=True):
        """
        Returns parsed JSON or raises an exception appropriately.
        """
        #print("handel responses",res,"response status-code:",res.status_code,"response header",res.headers)
        self._last_response = res
        result = {}
        if res.status_code in (200, 201, 202):
            try:
                result = res.json()
                # print("result>>>>>>>>>>>>",result)
            except Exception as e:  # json might be invalid, or store might be down
                e.message += " (_handle_response failed to decode JSON: " + \
                    str(res.content) + ")"
                raise  # TODO better exception

        elif res.status_code == 204 and not suppress_empty:
            raise EmptyResponseWarning(
                "%d %s @ %s: %s" % (res.status_code, res.reason, url, res.content), res)
        elif res.status_code >= 500:
            raise ServerException(
                "%d %s @ %s: %s" % (res.status_code, res.reason, url, res.content), res)
        elif res.status_code == 429:
            raise RateLimitingException(
                "%d %s @ %s: %s" % (res.status_code, res.reason, url, res.content), res)
        elif res.status_code >= 400:
            raise ClientRequestException(
                "%d %s @ %s: %s" % (res.status_code, res.reason, url, res.content), res)
        elif res.status_code >= 300:
            raise RedirectionException(
                "%d %s @ %s: %s" % (res.status_code, res.reason, url, res.content), res)
        return result


class OAuthConnection(Connection):

    def __init__(self,host,api_path,store_key):

        self.host = host
        self.api_path = api_path
        # self.timeout = 1  # can attach to session?
        self._session = requests.Session()
        #print("auth session object", self._session)

        if not store_key:
            raise InvalidDataException("Invalid Credentials")
        self._session.headers = {
            "Accept": "application/json","Content-Type":"application/json","apikey":store_key}
        #self._session.headers.update(self._oauth_headers(client_id, api_token))
        self._last_response = None  # for debugging
        self.rate_limit = {}

    
    
    @staticmethod
    def _oauth_headers(cid, atoken):
        return {'X-Auth-Client': cid,
                'X-Auth-Token': atoken}

    def full_path(self, url):
        print("full path auth connection url_____________",   url)
        return "https://" + self.host + self.api_path.format(url)



    def _handle_response(self, url, res, suppress_empty=True):
        """
        Adds rate limiting information on to the response object
        """
        result = Connection._handle_response(
            self, url, res, suppress_empty)
        return result

