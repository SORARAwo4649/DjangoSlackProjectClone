$('#passpass').change(function () {

    //disabled属性の状態を取得する
    var target = $('input[name="pass"]').val();
    var mypassword = '2aw44ppj';
    if (target === mypassword) {
        //disabled属性を付与する
        $('button').prop('disabled', false);
    } else {
        //disabled属性を解除する
        $('button').prop('disabled', true);
    }
})
