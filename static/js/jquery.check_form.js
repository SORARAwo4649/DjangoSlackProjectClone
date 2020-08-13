$(function (){
    $('#send').on('click', function (){
        if ($('#name').val() === '' ||
        $('#plan').val() === '' ||
        $('#date1').val() === '' ||
        $('#date2').val() === '' ||
        $('#date3').val() === ''){
            alert('空白があります');
            return false;
        }
        alert('送信完了')
    });
});