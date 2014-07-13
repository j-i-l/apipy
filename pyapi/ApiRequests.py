
#import time,json,datetime,httplib,decimal,os,pickle
##add dependencies to requests
import requests
#standard stuff (this is probably all available in requests, but 
#i didn't bother looking for it so far.
import urllib, hmac, hashlib
ServerInfo = None
######################################################
## do the importing of the ServerAccount class here ##
######################################################
#from ... import ... as ServerInfo
#from .CryptsyInfo import Info as ServerInfo
if not ServerInfo:
    class ServerInfo():
        def __init__(self, pubAddress=None, **params):
            """
                This is just some dummy class.
                To make this work, please at least set the pubDomain and pubApiDomain.
                    E.g. for www.crypsty.com:
                        pubAddress = 'http://pubapi.cryptsy.com/api.php'
                        privAddress = 'https://www.cryptsy.com/api'
            """
            self.pubAddress = pubAddress
            self.pubDomain, self.pubApiPath = None, None
            self.privDomain, self.privApiPath, self.privAddress = None, None, None
            for key in params:
                if key == 'privDomain':
                    self.privDomain = params[key]
                elif key == 'privApiPath':
                    self.privApiPath = params[key]
                elif key == 'pubDomain':
                    self.pubDomain = params[key]
                elif key == 'pubApiPath':
                    self.pubApiPath = params[key]
                else:
                    pass
            if self.pubDomain and self.pubApiPath:
                self.pubAddress = self.pubDomain+self.pubApiPath
            if self.privDomain and self.privApiPath:
                self.privAddress = self.privDomain+self.privApiPath


class ApiSuccessError(Exception):
    """
        Is raised if the request is valid but the api has the success status 0
    """
    pass


class Request():
    def __init__(self, Info = ServerInfo()):
        """
            This is the Requests class. It handles all public requests and is the 
                backbone of the PrivateRequests class.
            Usage:
                >>> req = CrypstyRequests()
                >>> response = req.public_session(params = {'method':'marketdatav2'}, **other_params)
                >>> print response
        """
        self.Info = Info
        return None
    
    def request(self, http_method, url, params, headers, data, **other_params):
        """
            check requests.Request class for details about **other_params
            This will return a requests.PreparedRequest object.
        """
        req = requests.Request(method=http_method,
                               url=url,
                               headers=headers,
                               data=data,
                               params=params,
                               **other_params)
        return req.prepare()
    
    def fetch(self, method=None, params={}, **other_params):
        """
            Make a simple get request
        """
        if method:
            params['method'] = method
        s = requests.Session()
        the_url = self.Info.pubAddress
        if 'url_addons' in other_params:
            the_url = the_url + '/' + '/'.join(other_params['url_addons'])
        print the_url
        prep_request = self.request(
            'GET',
            the_url,
            params,
            {},
            {},
            )
        return self.digest_response(s.send(prep_request), self._content_filter)
        
        
    
    #goes to public part if 
    def public_session(self, params={}, **other_params):
        """
            This method makes a simple GET request with parameters
        """
        http_method = 'GET'
        #url = self.Info.pubDomain+self.Info.pubApiPath
        #or
        url = self.Info.pubAddress
        headers = {}
        data = {}
        prep_request = self.request(
            http_method,
            url,
            params,
            headers,
            data,
            **other_params
        )
        session = requests.Session()
        return self.digest_response(session.send(prep_request), self._content_filter)
    
    def digest_response(self, response, content_filter=None):
        """
            This function should digest the return of a request in a halfway intelligent
                manner.
            The return of the request is processed depending on the status codes that 
                server returns.
            
            Arguments:
                - response is a requests.Response object
                - content_filter (default = None) can be a function that filters certain 
                    terms from the returned content.
            
            TO DO:
                It would be nice to handle each status code separately.
        """
        status_code = str(response.status_code)
        if status_code.startswith('1'): #continuing
            pass
        elif status_code.startswith('2'): #valid request
            as_json = response.json()
            return content_filter(as_json)
        elif status_code.startswith('3'): #redirection
            pass
        elif status_code.startswith('4'): #client error
            pass
        elif status_code.startswith('5'): #server error
            pass
        else:
            raise ValueError('The status code returned by the server is invalid. That is very odd')
        if response[u'success'] == 1:
            return response['return']
        else:
            raise ValueError('make a custom error for this...this is when the success return is not 1')
    
    def _content_filter(self, returned_dict):
        """
            This function is designed to only return part of the content the server returns.
            If left as is, the complete content in returned.
            
        """
        rest = returned_dict
        ###-----------------------###
        ### This part is optional ###
        ###-----------------------###
        #print rest
        if not 'success' in rest:
            return rest
        if int(rest.pop('success')) == 1:
            return rest[u'return']
        else:
            print rest
            raise ApiSuccessError('The server returns a valid response but the api failed to fulfil the request')
        ###-----------------------###
        return rest[u'return']
