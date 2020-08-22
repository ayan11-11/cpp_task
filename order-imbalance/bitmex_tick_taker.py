import argparse
import pandas as pd
import numpy as np
from lib import bitmex
import json

class Quote():
    """
    We use Quote objects to represent the bid/ask spread. When we encounter a
    'level change', a move of exactly 1 penny, we may attempt to make one
    trade. Whether or not the trade is successfully filled, we do not submit
    another trade until we see another level change.

    Note: Only moves of 1 penny are considered eligible because larger moves
    could potentially indicate some newsworthy event for the stock, which this
    algorithm is not tuned to trade.
    """

    def __init__(self):
        self.prev_bid = 0
        self.prev_ask = 0
        self.prev_spread = 0
        self.bid = 0
        self.ask = 0
        self.bid_size = 0
        self.ask_size = 0
        self.spread = 0
        self.traded = True
        self.level_ct = 1
        self.time = 0
        

    def reset(self):
        # Called when a level change happens
        self.traded = False
        self.level_ct += 1

    def update(self, data):
        # Update bid and ask sizes and timestamp
        askprice = 0
        bidprice = 0
        for x in data:
            if(x['side'] == 'Buy'):
                self.bid_size = x['size']
                bidprice = x['price']
            if(x['side'] == 'Sell'):    
                self.ask_size = x['size']
                askprice = x['price']

            # Check if there has been a level change
            if (self.bid != bidprice and self.ask != askprice and round(askprice - bidprice, 2) >= .01):
                # Update bids and asks and time of level change
                self.prev_bid = self.bid
                self.prev_ask = self.ask
                self.bid = bidprice
                self.ask = askprice
                # self.time = data.timestamp
                # Update spreads
                self.prev_spread = round(self.prev_ask - self.prev_bid, 3)
                self.spread = round(self.ask - self.bid, 3)
                print(
                    'Level change:', self.prev_bid, self.prev_ask,
                    self.prev_spread, self.bid, self.ask, self.spread, flush=True
                )
                # If change is from one penny spread level to a different penny
                # spread level, then initialize for new level (reset stale vars)
                if self.prev_spread == 0.01:
                    self.reset()


class Position():
    """
    The position object is used to track how many shares we have. We need to
    keep track of this so our position size doesn't inflate beyond the level
    we're willing to trade with. Because orders may sometimes be partially
    filled, we need to keep track of how many shares are "pending" a buy or
    sell as well as how many have been filled into our account.
    """

    def __init__(self):
        self.orders_filled_amount = {}
        self.pending_buy_shares = 0
        self.pending_sell_shares = 0
        self.total_shares = 0

    def update_pending_buy_shares(self, quantity):
        self.pending_buy_shares += quantity

    def update_pending_sell_shares(self, quantity):
        self.pending_sell_shares += quantity

    def update_filled_amount(self, order_id, new_amount, side):
        old_amount = self.orders_filled_amount[order_id]
        if new_amount > old_amount:
            if side == 'buy':
                self.update_pending_buy_shares(old_amount - new_amount)
                self.update_total_shares(new_amount - old_amount)
            else:
                self.update_pending_sell_shares(old_amount - new_amount)
                self.update_total_shares(old_amount - new_amount)
            self.orders_filled_amount[order_id] = new_amount

    def remove_pending_order(self, order_id, side):
        old_amount = self.orders_filled_amount[order_id]
        if side == 'buy':
            self.update_pending_buy_shares(old_amount - 100)
        else:
            self.update_pending_sell_shares(old_amount - 100)
        del self.orders_filled_amount[order_id]

    def update_total_shares(self, quantity):
        self.total_shares += quantity


def run():
    symbol = 'XBTUSD'
    max_shares = 500
    key_id='6YOT6PXt7MmygYpVAD8wtaX4'
    secret_key='Aq-82FDxlEZMrKnsCEeHCn5TqASDxQIJEM5pRYczMrwG9z5p'
    baseUrl='https://www.bitmex.com/api/v1/'
    print(baseUrl)
    symbol = symbol.upper()
    quote = Quote()
#    qc = 'Q.%s' % symbol
 #   tc = 'T.%s' % symbol
    position = Position()

    # Establish streaming connection
    # conn = tradeapi.StreamConn(**opts)
    conn = bitmex.BitMEX(base_url=baseUrl, symbol=symbol, apiKey=key_id, apiSecret=secret_key)
    # Define our message handling
    data = conn.market_depth()
    json_data = json.dumps(data)
    loaded_json = json.loads(json_data)   
    quote.update(loaded_json)

    trade_data = conn.recent_trades()
    # if quote.traded:
    #     return

#         # We've received a trade and might be ready to follow it
#         if (
#             data.timestamp <= (
#                 quote.time + pd.Timedelta(np.timedelta64(50, 'ms'))
#             )
#         ):
#             # The trade came too close to the quote update
#             # and may have been for the previous level
#             return
    for x in trade_data:
        if x['size'] >= 100:
             if (x['price'] > quote.ask and quote.bid_size > (quote.ask_size * 1.8) and (position.total_shares + position.pending_buy_shares) < max_shares - 100):
                 
                 # Everything looks right, so we submit our buy at the ask
                 try:
                     o = conn.buy(500, quote.ask)
                     # Approximate an IOC order by immediately cancelling
                     conn.cancel(o['orderID'])
                     position.update_pending_buy_shares(100)
                     position.orders_filled_amount[o['orderID']] = 0
                     print('Buy at', quote.ask, flush=True)
                     quote.traded = True
                 except Exception as e:
                     print(e)
             elif (x['price'] == quote.bid and quote.ask_size > (quote.bid_size * 1.8) and (position.total_shares - position.pending_sell_shares) >= 100):
                 # Everything looks right, so we submit our sell at the bid
                 try:
                     o = conn.sell(quantity=100, price=quote.bid)
                     # Approximate an IOC order by immediately cancelling
                     conn.cancel(o['orderID'])
                     position.update_pending_sell_shares(100)
                     position.orders_filled_amount[o['orderID']] = 0
                     print('Sell at', quote.bid, flush=True)
                     quote.traded = True
                 except Exception as e:
                     print(e)

#     @conn.on(r'trade_updates')
#     async def on_trade_updates(conn, channel, data):
#         # We got an update on one of the orders we submitted. We need to
#         # update our position with the new information.
#         event = data.event
#         if event == 'fill':
#             if data.order['side'] == 'buy':
#                 position.update_total_shares(
#                     int(data.order['filled_qty'])
#                 )
#             else:
#                 position.update_total_shares(
#                     -1 * int(data.order['filled_qty'])
#                 )
#             position.remove_pending_order(
#                 data.order['id'], data.order['side']
#             )
#         elif event == 'partial_fill':
#             position.update_filled_amount(
#                 data.order['id'], int(data.order['filled_qty']),
#                 data.order['side']
#             )
#         elif event == 'canceled' or event == 'rejected':
#             position.remove_pending_order(
#                 data.order['id'], data.order['side']
#             )

#     conn.run(
#         ['trade_updates', tc, qc]
#     )


if __name__ == '__main__':
    # parser = argparse.ArgumentParser()
    # parser.add_argument(
    #     '--symbol', type=str, default='XBTUSD',
    #     help='Symbol you want to trade.'
    # )
    # parser.add_argument(
    #     '--quantity', type=int, default=500,
    #     help='Maximum number of shares to hold at once. Minimum 100.'
    # )
    # parser.add_argument(
    #     '--key-id', type=str, default='6YOT6PXt7MmygYpVAD8wtaX4',
    #     help='API key ID',
    # )
    # parser.add_argument(
    #     '--secret-key', type=str, default='Aq-82FDxlEZMrKnsCEeHCn5TqASDxQIJEM5pRYczMrwG9z5p',
    #     help='API secret key',
    # )
    # parser.add_argument(
    #     '--base-url', type=str, default='https://www.bitmex.com/api/v1/',
    #     help='set https://paper-api.alpaca.markets if paper trading',
    # )
    # args = parser.parse_args()
    # assert args.quantity >= 100
    run()
