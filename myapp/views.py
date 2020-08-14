from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView

from .forms import NameForm
from .slackapp import CreatingChannels


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
        # 入力フォームから値を持ってくる
        names = request.POST['name']
        plan = request.POST['plan']
        date1 = request.POST['date1']
        date2 = request.POST['date2']
        date3 = request.POST['date3']
        mentee_id = request.POST['mentee_id']

        # Slack API を起動する
        slack_channels = CreatingChannels(
            names, plan, date1, date2, date3, mentee_id
        )
        creating = slack_channels.creating_channels()

        # 規約違反だけどnotにするとNoneも判定されるため使えない
        if isinstance(creating, bool):
            if creating == False:
                # 作成失敗ページへ遷移
                return render(request, 'creating_failed.html')

        # チャンネル作成が成功したらidを返している
        channel_id = creating

        # 順次slackアプリを実行する
        slack_channels.sending_message(channel_id)
        slack_channels.setting_topic(channel_id)
        slack_channels.inviting_user(channel_id)
        slack_channels.inciting_mentee(channel_id)
        slack_channels.leaving_app(channel_id)

        return render(request, 'creating_done.html', context)
