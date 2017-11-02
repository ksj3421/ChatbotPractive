# -*- coding: utf-8 -*-

from __future__ import (absolute_import, division, print_function, unicode_literals)

from bothub_client.bot import BaseBot
from bothub_client.messages import Message


class Bot(BaseBot):

	def handle_message(self, event, context):
		message = event.get('content')
		menu = self.get_project_data().get('keyboard').split(',')

		if message == '/start':
			msg = Message(event).set_text('안녕하세요. MES기술팀 챗봇입니다.\n\n 현재 검색 가능한 명령어는 다음과 같습니다.\n\n사용가능한 명령어 :\n'+self.get_project_data().get('keyboard'))
			for item in menu:
				msg.add_keyboard_button(item)
			self.send_message(msg)

		elif message in menu:
			self.auto_response(event, message)

		else:
			self.send_message('Telegram 에서는 1:1 대화 안내는 지원되지 않습니다.')

	def auto_response(self, event, message):
		answer = self.get_project_data().get(message)
		msg = Message(event).set_text(answer.get('answer'))
		if answer.get('link'):
			msg.add_url_button(answer.get('title'), answer.get('link'))

		self.send_message(msg)