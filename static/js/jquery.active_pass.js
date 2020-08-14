// $(document).ready(function () {

// csrfトークンの取得
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

const csrftoken = getCookie('csrftoken');

function csrfSafeMethod(method) {
    return ['GET', 'OPTIONS', 'HEAD', 'TRACE'].includes(method);
}

$.ajaxSetup({
    beforeSend: function (xhr, setting) {
        if (!csrfSafeMethod(setting.type) && !this.crossDomain)
            xhr.setRequestHeader("X-CSRFToken", csrftoken)
    }
});

// 機能の追加
$("#check_password").on('click', function () {
    $.ajax({
        url: "{% url 'accounts:ajax' %}",
        type: 'POST',
        dataType: 'json',
        timeout: 5000,
        data: {
            text: $('input[name="passpass"]').val()
        }
    }).done(function (data) {
        if (data) {
            $("#signup").prop('disabled', false);
        } else {
            alert("パスワードが不正です");
        }
    }).fail(function () {
        alert("通信失敗")
    })
});
// });
