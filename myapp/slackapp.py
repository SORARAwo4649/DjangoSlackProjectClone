from slack import WebClient
from slack.errors import SlackApiError
import certifi
import ssl as ssl_lib


class CreatingChannels:
    def __init__(self, names, plan, date1, date2, date3):
        # 初期設定***************************************************************
        token = 'xoxb-1287291111699-1302304008356-f1tUrFxULMdzFnoMONhoRHk5'
        self.users_id = 'U0180A2FVKR'
        # *********************************************************************

        print("start!!")
        self.names = names
        self.plan = plan
        self.date1 = date1
        self.date2 = date2
        self.date3 = date3

        # 開発用
        ssl_context = ssl_lib.create_default_context(cafile=certifi.where())
        self.client = WebClient(
            token=f"{token}", ssl=ssl_context
        )

    def creating_channels(self):
        try:
            # チャンネルの作成
            channel_name = f"メンター部屋-{self.names}様"
            response = self.client.conversations_create(
                name=channel_name,
                is_private=True,
            )
            channel_id = response["channel"]["id"]
            return channel_id

            # 順次実行する
            # self.sending_message(channel_id)
            # self.inviting_user(channel_id)
            # self.leaving_user(channel_id)

        except SlackApiError as e:
            print(e)
            return e.response["ok"]

    def sending_message(self, channel_id):
        try:
            # 定型文の送信
            self.client.chat_postMessage(
                channel=f"{channel_id}",
                text=f"管理者からのリクエストで、ボットが{self.names}様のメンター部屋を自動作成しました。\n※ボットの退出後にこのボットが再入室することは出来ません。またボット経由で第三者がメッセージのやり取りを見ることも出来ませんのでご安心ください。"
            )
        except SlackApiError as e:
            print(e)
            return e.response["ok"]

    def inviting_user(self, channel_id):
        try:
            # チャンネルへの招待
            self.client.conversations_invite(
                channel=f"{channel_id}",
                users=f"{self.users_id}",
            )
        except SlackApiError as e:
            print(e)
            return e.response["ok"]

    def leaving_app(self, channel_id):
        try:
            # ボットをチャンネルから退出させる
            self.client.conversations_leave(
                channel=f"{channel_id}",
            )
        except SlackApiError as e:
            print(e)
            return e.response["ok"]
