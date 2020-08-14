$(function (){
    $('#send').on('click', function (){
        if ($('#name').val() === '' ||
        $('#plan').val() === '' ||
        $('#date1').val() === '' ||
        $('#date2').val() === '' ||
        $('#date3').val() === '' ||
        $('#mentee_id').val() === ''){
            alert('空白があります');
            return false;
        }
    });
});