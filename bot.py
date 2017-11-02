# -*- coding: utf-8 -*-

from __future__ import (absolute_import, division, print_function, unicode_literals)

from bothub_client.bot import BaseBot
from bothub_client.messages import Message
from .korbit import coin_detail


class Bot(BaseBot):
    def handle_message(self, event, context):
        message = event.get('content')

        if message == 'BTC':
            self.send_message(coin_detail('btc_krw'))
        elif message == 'ETH':
            self.send_message(coin_detail('eth_krw'))
        elif message == 'XRP':
            self.send_message(coin_detail('xrp_krw'))
        else:
            self.send_message('빠른 답장(Quick Replies)을 이용해주세요.')

        msg = Message(event).set_text('어떤 가상화폐 시세를 확인할까요?') \
            .add_quick_reply('BTC') \
            .add_quick_reply('ETH') \
            .add_quick_reply('XRP')
        self.send_message(msg)