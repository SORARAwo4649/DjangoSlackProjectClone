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
        def checking_slack_error(e_dict, error_id):
            # 規約違反だけどnotにするとNoneも判定されるため使えない
            if not isinstance(e_dict, str):
                if e_dict['ok'] == False:
                    if error_id == 1:
                        title = "チャンネル作成"
                    elif error_id == 2:
                        title = "定型文の作成"
                    elif error_id == 3:
                        title = "トピックの作成"
                    elif error_id == 4:
                        title = "メンター招待"
                    elif error_id == 5:
                        title = "メンティー招待"
                    elif error_id == 6:
                        title = "アプリの退場"
                    else:
                        title = "その他"

                    print(f"エラーID：{error_id}")

                    # 作成失敗ページへ遷移
                    error_text = {
                        "error_id": error_id,
                        "title": title,
                        "ok": e_dict["ok"],
                        "error": e_dict["error"],
                        "detail": e_dict["detail"]
                    }
                    return error_text

        # 本文
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
        if not isinstance(creating, str):
            creating_dict = creating.response
            error_id = 1
            # チャンネル作成のエラーをチェックする
            text = checking_slack_error(creating_dict, error_id)
            if text:
                return render(request, 'creating_failed.html', text)

        # チャンネル作成が成功したらidを返している
        channel_id = creating

        # 順次slackアプリを実行する
        # エラーチェックも行う
        # 定型文の送信
        sending = slack_channels.sending_message(channel_id)
        if not isinstance(creating, str):
            sending_dict = sending.response
            error_id = 2
            # チャンネル作成のエラーをチェックする
            text = checking_slack_error(sending_dict, error_id)
            if text:
                return render(request, 'creating_failed.html', text)

        # トピックの設定
        setting = slack_channels.setting_topic(channel_id)
        if not isinstance(creating, str):
            setting_dict = setting.response
            error_id = 3
            text = checking_slack_error(setting_dict, error_id)
            if text:
                return render(request, 'creating_failed.html', text)

        # メンター招待
        inviting = slack_channels.inviting_user(channel_id)
        if not isinstance(creating, str):
            inviting_dict = inviting.response
            error_id = 4
            text = checking_slack_error(inviting_dict, error_id)
            if text:
                return render(request, 'creating_failed.html', text)

        # メンティー招待
        # ブランクの許可
        if mentee_id:
            inviting_mentee = slack_channels.inviting_mentee(channel_id)
            if not isinstance(creating, str):
                inviting_mentee_dict = inviting_mentee.response
                error_id = 5
                text = checking_slack_error(inviting_mentee_dict, error_id)
                if text:
                    return render(request, 'creating_failed.html', text)

        # アプリの退場
        leaving = slack_channels.leaving_app(channel_id)
        if not isinstance(creating, str):
            leaving_dict = leaving.response
            error_id = 6
            text = checking_slack_error(leaving_dict, error_id)
            if text:
                return render(request, 'creating_failed.html', text)

        return render(request, 'creating_done.html', context)
