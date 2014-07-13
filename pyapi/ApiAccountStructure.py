from ApiRequests import Request
from ApiRequestsPrivate import RequestPrivate 
from ApiInfoStructure import InfoStructure
import time

class AccountStructure():
    def __init__(self, PlatformInfo, public_key='', private_key='',):
        """
        This class should be a genuine class of an account on
            some platform. The idea is to write a specific class
            to any platform that inherits from this class
            and (if necessary) overwrites its functions.
            
        """
        self.pub_key = public_key
        self.priv_key = private_key
        self._init_Request(Platform=PlatformInfo)
        self.MyTrades = {}
        self.MyOrders = {}
        self.MyTransactions = {}

        ##Those have to adapted to the specific platform
        self.command_account_info = ''
        self.command_market_info = ''
        self.command_trades_history = ''
        self.command_open_orders = ''
        self.command_my_transactions = ''
        self.command_my_trades = ''
        self.command_my_orders = ''
        self.command_new_order = ''
        self.command_cancel_order = ''
        self.command_cancel_all_orders = ''
        self.parameter_ordertype = ''
        self.parameter_market = ''
        self.parameter_quantity = ''
        self.parameter_price = ''
        self.parameter_order_id = ''
        self.parameter_market_id = ''
        
    def _init_Requests(self, PlatfromInfo):
        #PlatformInfo = Info()
        self.Request = RequestPrivate(Account=self, Info=PlatformInfo)
        self.pubRequest = Request(Info=PlatformInfo)
        return 0
    
    def update_Info(self,):
        return self.Request.fetch(self.command_account_info)
    
    def update_MarketInfo(self,):
        return self.Request.fetch(self.command_market_info)

    def update_TradeHistory(self, ):
        return self.Request.fetch(self.command_trades_history)
    
    def update_OpenOrders(self, ):
        return self.Request.fetch(self.command_open_orders)
    
    
    def update_MyTransactions(self, ):
        return self.Request.fetch(self.command_my_transactions)
    
    def update_MyTrades(self, ):
        return self.Request.fetch(self.command_my_trades)
    
    def update_MyOrders(self, ):
        return self.Request.fetch(self.command_my_orders)
    
    
    def CreateOrder(self, market, order_type, quantity, price):
        params = {
                  self.parameter_ordertype: order_type,
                  self.parameter_market: market,
                  self.parameter_quantity: quantity,
                  self.parameter_price: price
                  }
        if self._order_possible(params):#check if funds are ok, etc.
            now = time.time()
            order_id = self.Request.fetch(self.command_new_order, params=params)
            self.MyOpenOrders[order_id] = params
            self.MyOpenOrders[order_id][u'timestamp'] = now
        return 0
    
    def _order_possible(self, params):
        #do whatever check you want to do...
        #if ok:
        #return True
        #if not
        #return False
        return True
    
    def CancelOrder(self, **orders):
        if self.parameter_order_id in orders:
            canceled_orders = self.Request.fetch(self.command_cancel_order,
                                                 params={
                                                     self.parameter_order_id: orders[self.parameter_order_id]
                                                 }
                                                 )
        if self.parameter_market_id in orders:#cancel all orders in a market(if possible by api)
            canceled_orders = self.Request.fetch(self.command_cancel_order,
                                                 params={
                                                     self.parameter_market_id: orders[self.parameter_market_id]
                                                 }
                                                 )
        if not len(orders.keys()):#no specifications -> cancel all orders
            all_canceled_orders = self.Request.fetch(self.command_cancel_all_orders)
        return 0
    
    

