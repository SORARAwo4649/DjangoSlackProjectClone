$('#passpass').change(function () {

    //disabled属性の状態を取得する
    var target = $('input[name="pass"]').val();
    var mypassword = '2aw44ppj';
    if (target === mypassword) {
        $('button').prop('disabled', false);
    } else {
        $('button').prop('disabled', true);
    }
})
