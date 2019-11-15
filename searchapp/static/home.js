$(document).ready(function(){
    function set_worksheet_type(type){
        window.location.href="student_view" + "?type=" + type;
    }

    $('.selectType').click(function(){
        set_worksheet_type($(this).attr('id'));
    });
});
