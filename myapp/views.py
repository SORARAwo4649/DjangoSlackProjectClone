from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, View
from slack import WebClient
from slack.errors import SlackApiError
import certifi
import ssl as ssl_lib

from .forms import NameForm


class CreatingChannels(View):
    def creating_channels(self, names):
        try:
            token = 'xoxb-1265411682005-1269328032261-XsGAtpe0jSLhnpqEBSOTZjBZ'
            ssl_context = ssl_lib.create_default_context(cafile=certifi.where())
            client = WebClient(
                token=f"{token}", ssl=ssl_context
            )

            # チャンネルの作成
            channel_name = f"メンター部屋-{names}様"
            response = client.conversations_create(
                name=channel_name,
                is_private=True,
            )
            channel_id = response["channel"]["id"]

            # チャンネルへの招待
            users_id = "U0187C0V4BB"
            response_invite = client.conversations_invite(
                channel=f"{channel_id}",
                users=f"{users_id}",
            )
            # ボットをチャンネルから退出させる
            response_leave = client.conversations_leave(
                channel=f"{channel_id}",
            )
        except SlackApiError as e:
            print(e)
            return e.response["ok"]


class CreatingView(TemplateView):
    template_name = 'creating.html'
    success_url = reverse_lazy('myapp:creating')
    form_class = NameForm

    def get(self, request, *args, **kwargs):
        context = {
            'message': "操作して下さい",
        }
        return render(request, 'creating.html', context)

    def post(self, request, *args, **kwargs):
        context = {
            'name': request.POST['name']
        }
        names = request.POST['name']
        slack_channels = CreatingChannels()
        name_check = slack_channels.creating_channels(names)
        print(name_check)
        # 規約違反だけどnotにするとNoneも判定されるため使えない
        if name_check == False:
            # 作成失敗ページへ遷移
            return render(request, 'creating_failed.html')
        return render(request, 'creating_done.html', context)
