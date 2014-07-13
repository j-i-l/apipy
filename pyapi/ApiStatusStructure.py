from ApiRequests import Request
import time


class StatusStructure():
    def __init__(self,
                 PlatformInfo,
                 keep_duration=60*60  #keep for 1 hour
                 ):
        self._init_Request(PlatformInfo)
        self.keep_duration = keep_duration
        self.MarketCurrent = {}
        self.TradesCurrent = {}
        self.Trades = {}  #potential longer than the Current version
        self.OrdersCurrent = {}
        self.Orders = {}  #potentially longer than the Current version
        self.TickersCurrent = {}  #{marketID:(time,ticker)
        self.Tickers = {}
        
        self.command_marketdata = '-'
        self.command_allmarketdata = '-'
        self.command_markettrades = '-'
        self.command_marketorders = '-'
        self.command_allmarketorders = '-'
        self.command_marketticker = '-'
        self.command_allmarketticker = '-'
        self.parameter_marketID = '-'
        
        
    def _init_Request(self, PlatformInfo):
        self.Request = Request(Info=PlatformInfo())
        return 0
    
    def get_MarketCurrent(self, marketID=None, mod_url=False):
        """
        Get the current market status

        Arguments:
            - marketID: Default=None, the ID or identifier of the 
                market for which the data should be fetched.
            - mod_url: Dafault=None, can be a list of terms to add 
                to the url.
        """
        kwargs = {}
        if marketID:
            kwargs['method'] = self._check(self.command_marketdata)
            kwargs['params'] = {self._check(self.parameter_marketID): marketID}
        else:
            kwargs['method'] = self._check(self.command_allmarketdata)
        if mod_url:
            kwargs['url_addons'] = mod_url
        market = self.Request.fetch(**kwargs)
        return time.time(), market
    
    def get_OrdersCurrent(self, marketID=None, mod_url=False):
        """
        Get the current market orders

        Arguments:
            - marketID: Default=None, the ID or identifier of the 
                market for which the data should be fetched.
            - mod_url: Dafault=None, can be a list of terms to add 
                to the url.
        """
        kwargs = {}
        if marketID:
            kwargs['method'] = self._check(self.command_marketorders)
            kwargs['params'] = {self._check(self.parameter_marketID): marketID}
        else:
            kwargs['method'] = self._check(self.command_allmarketorders)
        if mod_url:
            kwargs['url_addons'] = mod_url
        orders = self.Request.fetch(**kwargs)
        return time.time(), orders
    
    def get_Ticker(self, marketID=None, mod_url=False):
        """
        Get the latest Ticker

        Arguments:
            - marketID: Default=None, the ID or identifier of the 
                market for which the data should be fetched.
            - mod_url: Dafault=None, can be a list of terms to add 
                to the url.

        """
        kwargs = {}
        if marketID:
            kwargs['method'] = self._check(self.command_marketticker)
            kwargs['params'] = {self._check(self.parameter_marketID): marketID}
        else:
            kwargs['method'] = self._check(self.command_allmarketticker)
        if mod_url:
            kwargs['url_addons'] = mod_url
        ticker = self.Request.fetch(**kwargs)
        return time.time(), ticker
    
    @staticmethod
    def _check(to_check):
        """
        This function checks whether a command or parameter is 
            defined or not. It raises a ValueError if it is not defined.
        """
        if to_check != '-':
            return to_check
        else:
            raise ValueError('This command or parameter is not defined')