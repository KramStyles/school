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
            alert(data);
            btn.html('Log In');
        }
    });
});