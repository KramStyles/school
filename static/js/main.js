$('#btnLogin').click(function (e) {
    e.preventDefault();
    frm = $('#frmLogin');
    $.ajax({
        url: '/sign_in',
        method: 'POST',
        data: frm.serialize(),
        success: function (data) {
            alert(data);
        }
    });
});