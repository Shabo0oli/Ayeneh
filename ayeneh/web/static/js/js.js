/**
 * Created by shahab on 8/10/19.
 */


$('#signup_form').on('submit',function (e) {
    e.preventDefault();
    $.ajax({
        url: '/signup/',
        cache: false,
        type: 'POST',
        data : $('#signup_form').serialize(),
        success: function(json_obj) {
            if (json_obj.status == 'success') {
                location.reload(true);
            } else {
                alert(json_obj.message);
            }

    }
    });
});


$('#signin_form').on('submit',function (e) {
    e.preventDefault();
    $.ajax({
        url: '/login/',
        cache: false,
        type: 'POST',
        data : $('#signin_form').serialize(),
        success: function(json_obj) {

        if (json_obj.status == 'success')
        {
            location.reload(true);
            } else {
                alert(json_obj.message);
        }
        document.getElementById("signin_form").reset();
    }
    });
});