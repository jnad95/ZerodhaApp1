import logging

from kiteconnect import KiteConnect

logging.basicConfig(level=logging.DEBUG)


class KiteClient:

    def __init__(self):
        print("system login")
        app_name = "2J23TradingApp"
        api_key = "bpqhnh3alxv9sujf"
        api_secret = "tcvz7td87twt5ihhktxgm48780omi8fq"
        self.kite = KiteConnect(api_key=api_key)
        # Redirect the user to the login url obtained
        # from kite.login_url(), and receive the request_token
        # from the registered redirect url after the login flow.
        # Once you have the request_token, obtain the access_token
        # as follows.
        print(self.kite.login_url())
        print("obtaining request token for login")
        request_token_here = None
        data = self.kite.generate_session(request_token_here, api_secret=api_secret)
        print("obtained data", data)
        self.kite.set_access_token(data["access_token"])
        print("system login complete")

    # Place an order
    def place_order(self, trading_symbol, exchange, transaction_type,
                    quantity, variety, order_type, product, validity):
        try:
            order_id = self.kite.place_order(
                tradingsymbol=trading_symbol,  # "INFY",
                exchange=self.kite.EXCHANGE_NSE,
                transaction_type=self.kite.TRANSACTION_TYPE_BUY,
                quantity=quantity,  # 1,
                variety=self.kite.VARIETY_AMO,
                order_type=self.kite.ORDER_TYPE_MARKET,
                product=self.kite.PRODUCT_CNC,
                validity=self.kite.VALIDITY_DAY
            )

            logging.info("Order placed. ID is: {}".format(order_id))
        except Exception as e:
            logging.info("Order placement failed: {}".format(e.message))

    def get_orders(self):
        # Fetch all orders
        self.kite.orders()

    def get_instruments(self):
        # Get instruments
        self.kite.instruments()

    def place_order_for_mf(self, tradingsymbol, transaction_type, amount, tag):
        # Place a mutual fund order
        self.kite.place_mf_order(
            tradingsymbol=tradingsymbol,  # "INF090I01239"
            transaction_type=self.kite.TRANSACTION_TYPE_BUY,
            amount=amount,  # 5000,
            tag=tag  # "mytag"
        )

    def cancel_order(self, order_id):
        # Cancel a mutual fund order
        self.kite.cancel_mf_order(order_id="order_id")

    def get_mf_instruments(self):
        # Get mutual fund instruments
        self.kite.mf_instruments()
