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
                setTimeout(()=> {
                    document.location.assign('/add_admin');
                }, 3000)
            }

        }
    });
});