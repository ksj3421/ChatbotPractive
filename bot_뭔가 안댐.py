from bothub_client.bot import BaseBot
from bothub_client.messages import Message


class Bot(BaseBot):

    def send_welcome_message(self, event):
        message = Message(event).set_text('반가워요, MES기술팀 챗봇입니다.\n'\
                                          '궁금하신 시스템을 눌러보실래요?')\
                                .add_quick_reply('시스템보기')
        self.send_message(message)

    def handle_message(self, event, context):
        content = event.get('content')

        if content.startswith('/start'):
            self.send_welcome_message(event)
        elif content == '시스템보기':
            self.send_menu(event)
        # be aware of tailing space
        elif content.startswith('/show '):
            _, name = content.split()
            self.send_show(name, event)
        # be aware of tailing space
        elif content.startswith('/order_confirm '):
            _, name = content.split()
            self.send_order_confirm(name, event)
        elif content.startswith('/order '):
            _, name = content.split()
            self.send_order(name, event)

    def send_show(self, name, event):
        menu = self.get_project_data()['menu']
        selected_menu = menu[name]
        text = '{name}는 {description}\n담당자는 {price}이예요.'.format(name=name, **selected_menu)
        message = Message(event).set_text(text)\
                                .add_quick_reply('{} 주문'.format(name), '/order {}'.format(name))\
                                .add_quick_reply('시스템보기')

    def send_menu(self, event):
        menu = self.get_project_data()['menu']
        names = [name for name in menu.keys()]
        message = Message(event).set_text('어떤 시스템을 알아보고 싶으세요?')

        for name in names:
            message.add_postback_button(name, '/show {}'.format(name))

        self.send_message(message)

    def send_order_confirm(self, name, event):
        message = Message(event).set_text('{}에 대해 알아보시겠어요?'.format(name))\
                                .add_quick_reply('예', '/order {}'.format(name))\
                                .add_quick_reply('취소', '시스템보기')
        self.send_message(message)

    def send_order(self, name, event):
        self.send_message('담당자에게 메일을 전송하겠습니다.'.format(name))

