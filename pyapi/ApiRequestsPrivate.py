#this is probably all in requests ...
import requests
import time, hmac, hashlib, urllib

from ApiRequests import Request, ServerInfo
ServerAccount = None
######################################################
## do the importing of the ServerAccount class here ##
######################################################
#from ... import ... as ServerAccount
#from CryptsyAccount import CryptsyAccount as ServerAccount
if not ServerAccount:
    class ServerAccount():
        def __init__(self, pubDomain = '', pubApiPath = '', **params):
            """
                This is just some dummy class.
                To make this work, please set the pub_key and priv_key variables. You
                    can get this information from the settings of your account.
            """
            self.pub_key = 'PUT YOUR KEY HERE'
            self.priv_key = 'PUT YOUR SECRET HERE'
            return None


class RequestPrivate(Request):
    def __init__(self, Account = ServerAccount(), Info = ServerInfo()):
        """
            
        """
        Request.__init__(self, Info = Info)
        self.Account = Account
        return None
    
    def nonce(self):
        """
            get the next nonce to send along with a request
        """
        #don't like this solution somehow
        return str(int(round(time.time()*1000)))

    def fetch(self, method, data = {}, **other_params):
	"""
	    Make a simple post request.
	"""
	data['method'] = method
        data['nonce'] = self.nonce()
	headers = {
		   "Content-type": "application/x-www-form-urlencoded",
                   "Key":self.Account.pub_key,
		   "Sign": self._sign(data)
		   }
	s = requests.Session()
	prep_r = self.request( 
                              'POST', 
                              self.Info.privAddress,
                              None,
                              headers,
                              data,
                              **other_params
                              )
	return self.digest_response(s.send(prep_r),self._content_filter)
    
    def private_session(self, data, params = None, shedule = [],**other_params):
        """ This is for later
            Create a requests.Session instance to run one or several 
                requests.
            Arguments:
		- data: the content of the post request. put the requested method and 
		    parameters here.
                - params: either a dict or a list of dicts with the request 
                    parameters. If if is a list it needs to have the same length
                    as shedule.
                - shedule: list of different conditions to send requests (to do)
                    could be different times, etc. NOT IMPLEMENTED YET -> ignore
        """
        http_method = "POST"
        #url = self.privDomain+self.privApiPath
        #or
        url = self.Info.privAddress
        headers = {
                   "Content-type": "application/x-www-form-urlencoded",
                   "Key":self.Account.pub_key
                   }
        session = requests.Session()
        if len(shedule):
            pass #to do
        else:#params must be dict.
            data['nonce'] = self.nonce()
            headers["Sign"]=self._sign(data)
            prep_request = self.request( 
                               http_method, 
                               url,
                               params,
                               headers,
                               data,
                               **other_params
                               )
            return self.digest_response(session.send(prep_request),self._content_filter)
    
    def _sign(self,params,):
        """
            Create the signature
        """
        H = hmac.new(self.Account.priv_key, digestmod=hashlib.sha512)
        H.update(urllib.urlencode(params)) #dont like the urllib call
        #should be doable with requests only...
        return H.hexdigest()

