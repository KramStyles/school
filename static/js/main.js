$('#btnLogin').click(function (e) {
    e.preventDefault();
    frm = $('#frmLogin');
    btn = $(this);
    btn.html("<i class='fa fa-cog fa-spin'></i> Processing...");
    $.ajax({
        url: '/sign_in',
        method: 'POST',
        data: frm.serialize(),
        success: function (data) {
            if (data != 'ok') {
                Swal.fire({
                    title: 'Error!',
                    text: data,
                    icon: 'error',
                    confirmButtonText: 'Try Again'
                });
                btn.html('Log In');
            } else {
                Swal.fire({
                    title: 'Bravo!',
                    text: data,
                    icon: 'success',
                    confirmButtonText: 'Ok!'
                });
                setTimeout(() => {
                    document.location.assign('/add_admin');
                }, 3000)
            }

        }
    });
});

$('#selUserRole').change(function (e) {

    document.querySelector('#admin-details').className = 'white_card_body hide';
    document.querySelector('#user-details').className = 'white_card_body hide';
    VAL = $('#selUserRole').val();
    if (VAL === 'student') {
        document.querySelector('#user-details').className = 'white_card_body';
    } else if (VAL === 'admin') {
        document.querySelector('#admin-details').className = 'white_card_body';
    } else {
        document.querySelector('#admin-details').className = 'white_card_body hide';
        document.querySelector('#user-details').className = 'white_card_body hide';
    }

});

function myAjax(btn, frm, url, to = '') {
    $(btn).click(function (e) {
        e.preventDefault();
        frm = $(frm);
        btn = $(this);
        btnTxt = btn.html();
        console.log(btnTxt);
        btn.html("<i class='fa fa-cog fa-spin'></i> Processing...");
        $.ajax({
            url: `/${url}`,
            method: 'POST',
            data: frm.serialize(),
            success: function (data) {
                if (data != 'ok') {
                    btn.html(btnTxt);
                    Swal.fire({
                        title: 'Error!',
                        text: data,
                        icon: 'error',
                        confirmButtonText: 'Try Again'
                    });
                } else {
                    Swal.fire({
                        title: 'Bravo!',
                        text: data,
                        icon: 'success',
                        confirmButtonText: 'Ok!'
                    });
                    setTimeout(() => {
                        if (to === 0) window.top.location = window.top.location;
                        else if (to !== '') document.location.assign(`/${to}`);
                        else{
                            // Your papa!
                        }
                    }, 3000)
                }

            }
        });
    });
}

$(document).on('click','#icoAdminEdit', function (e) {
    $('#fname').val($(this).attr('data-name'));
    $('#mobile').val($(this).attr('data-mobile'));
    $('#email').val($(this).attr('data-email'));
    $('#address').val($(this).attr('data-address'));
    $('#username').text($(this).attr('data-user'));
    $('#txtUser').val($(this).attr('data-user'));
});


myAjax('#btn-admin-details', '#admin-details', 'new_admin', 'admin_list');
myAjax('#btnAdminEdit', '#frmAdminEdit', 'edit_admin', 'admin_list');