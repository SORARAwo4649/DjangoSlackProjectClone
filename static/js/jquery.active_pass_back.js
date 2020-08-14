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

$("input[name='passpass']").change(function (){
    var that = this;
    $.ajax({
        type: "get",
        url: "{% url 'accounts:validate_password' %}",
        dataType: "json",
        data: {
            "passpass": $(this).val()
        }
    })
        .then(
            function (data) {
                if (!data.password) {
                    $(that).addClass("is-invalid");
                    $(that).after(
                        '<div class="invalid-feedback" style="display: block">'
                        + data.message
                        + "</div>"
                    );
                } else {
                    $(that).removeClass("is-invalid");
                    $(that).next().remove(":contain(" + data.message + ")");
                    $("button").prop("disabled", false);
                }
            }
        )
});
