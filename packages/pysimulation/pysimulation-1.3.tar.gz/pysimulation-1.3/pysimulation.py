import os
import pandas as pd
import datetime
import pytz
from decimal import *

# 新增下單時間限制（日盤）


class order:
    def __init__(self, account):
        self.account = account
        self.order = []

    def place_order(self, bidask, action, octype):
        if action == 'Buy':

            print('Order(\ncode:\t%s\naction:\t%s\noctype:\t%s\nprice:\t%s\nfee:\t%s\ntax:\t%s\nts:\t%s\n)' % (bidask['code'], action, octype, str(bidask['ask_price'][0]), '50', str(
                round(bidask['ask_price'][0] * 200 * 2 / 100000)), str(datetime.datetime.strftime(datetime.datetime.now(pytz.timezone('ROC')), '%Y-%m-%d %H:%M:%S'))))
            self.order.append({
                'code': bidask['code'],
                'action': action,
                'octype': octype,
                'price': round(bidask['ask_price'][0]),
                'fee': 50,
                'tax': round(bidask['ask_price'][0] * 200 * 2 / 100000),
                'ts': datetime.datetime.strftime(datetime.datetime.now(pytz.timezone('ROC')), '%Y-%m-%d %H:%M:%S')
            })
            update_order(self.account, (self.order)[-1])
            if octype == 'Cover':
                update_list_profit_loss(self.account)
        elif action == 'Sell':

            print('Order(\ncode:\t%s\naction:\t%s\noctype:\t%s\nprice:\t%s\nfee:\t%s\ntax:\t%s\nts:\t%s\n)' % (bidask['code'], action, octype, str(bidask['bid_price'][0]), '50', str(
                round(bidask['bid_price'][0] * 200 * 2 / 100000)), str(datetime.datetime.strftime(datetime.datetime.now(pytz.timezone('ROC')), '%Y-%m-%d %H:%M:%S'))))
            self.order.append({
                'code': bidask['code'],
                'action': action,
                'octype': octype,
                'price': round(bidask['bid_price'][0]),
                'fee': 50,
                'tax': round(bidask['bid_price'][0] * 200 * 2 / 100000),
                'ts': datetime.datetime.strftime(datetime.datetime.now(pytz.timezone('ROC')), '%Y-%m-%d %H:%M:%S')
            })
            update_order(self.account, (self.order)[-1])
            if octype == 'Cover':
                update_list_profit_loss(self.account)

    def list_trades(self):
        return self.order

    def list_profit_loss(self):
        if os.path.isfile('%s_profit_loss.csv' % self.account):
            df = pd.read_csv('%s_profit_loss.csv' % self.account)
            print(df.to_string())
            print('\ntotal profit/loss: %s\ntotal roi: %s%%\n' %
                  (str(sum(df['pnl'])), str(round(sum(df['pnl']) / 184000 * 100, 2))))
        else:
            print('No order found.\n')
        return

    def list_position(self, bidask):
        if os.path.isfile('%s_order.csv' % self.account):
            df = pd.read_csv('%s_order.csv' % self.account)
            last_trade = df.tail(1)
            if(last_trade['octype'] == 'Cover'):
                return []
            else:
                position = {'code': bidask['code'],
                            'direction': last_trade['action'],
                            'quantity': 1,
                            'price': last_trade['price'],
                            }
                if(last_trade['action'] == 'Buy'):
                    position['last_price'] = bidask['ask_price'][0]
                    position['pnl'] = (bidask['ask_price'][0] - last_trade['price']) * 200 - last_trade['fee'] - \
                        last_trade['tax'] - 50 - \
                        round(bidask['ask_price'][0] * 200 * 2 / 100000)
                else:
                    position['last_price'] = bidask['bid_price'][0]
                    position['pnl'] = (last_trade['price'] - bidask['bid_price'][0]) * 200 - last_trade['fee'] - \
                        last_trade['tax'] - 50 - \
                        round(bidask['bid_price'][0] * 200 * 2 / 100000)
                return position
        else:
            return []


def update_order(account, order):
    df = pd.DataFrame(order, index=[0])
    df.set_index('ts', inplace=True)
    if os.path.isfile('%s_order.csv' % account):
        df = pd.concat([pd.read_csv('%s_order.csv' %
                       account, index_col='ts'), df], axis=0)
        df.to_csv('%s_order.csv' % account)
    else:
        df.to_csv('%s_order.csv' % account)


def update_list_profit_loss(account):
    order = pd.read_csv('%s_order.csv' % account, index_col='ts')
    pnl = (order['price'][-1] - order['price'][-2]) * 200 - \
        order['fee'][-1] - order['fee'][-2] - \
        order['tax'][-1] - order['tax'][-2]
    roi = round((pnl / 184000) * 100, 2)
    df = {
        'ts': order.index[-1],
        'code': order['code'][-1],
        'fee': order['fee'][-1] + order['fee'][-2],
        'tax': order['tax'][-1] + order['tax'][-2],
        'entry_price': order['price'][-2],
        'cover_price': order['price'][-1],
        'pnl': pnl,
        'roi': str(roi) + '%'
    }
    df = pd.DataFrame(df, index=[0])
    df.set_index('ts', inplace=True)
    if os.path.isfile('%s_profit_loss.csv' % account):
        df = pd.concat([pd.read_csv('%s_profit_loss.csv' %
                       account, index_col='ts'), df], axis=0)
        df.to_csv('%s_profit_loss.csv' % account)
    else:
        df.to_csv('%s_profit_loss.csv' % account)
