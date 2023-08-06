function loginInit() {
    var scrollBarSize = getBrowserScrollSize();
    var $btn_register = $("#btn-register");
    var $btn_create = $("#btn-create-account");
    var $btn_login = $("#btn-log-in");
    var host = window.location.host;

    $btn_register.bind('click', showCreateAccount);
    $btn_create.bind('click', createAccount);
    $btn_login.bind('click', login);

    function showCreateAccount() {
        $('#register-modal').modal('show');
    }

    function createAccount() {
        var data = {};
        var name = $('#register-modal input#name').val();
        var password = $('#register-modal input#password').val();
        var confirm_password = $('#register-modal input#confirm-password').val();
        var email = $('#register-modal input#email').val();
        var phone = $('#register-modal input#phone').val();
        if (password == confirm_password) {
            data.name = name;
            data.password = password;
            data.email = email;
            data.phone = phone;
            data.login = false;
            $.ajax({
                type: "POST",
                url: "http://" + host + "/login",
                data: JSON.stringify(data),
                dataType: "json",
                contentType: false,
                processData: false,
                success: function(data) {
                    if (data.result != "ok") {
                        showWarningToast("operation failed", data.message);
                    } else {
                        $('.login-form-container input#name').val(name);
                    }
                    $('#register-modal').modal('hide');
                },
                error: function() {
                    showWarningToast("error", "request service failed");
                }
            });
        } else {
            showWarningToast("error", "password not equal to confirm password");
        }
    }

    function login() {
        var data = {};
        var name = $('.login-form-container input#name').val();
        var password = $('.login-form-container input#password').val();
        if (name && password) {
            data.name = name;
            data.password = password;
            data.login = true;
            $.ajax({
                type: "POST",
                url: "http://" + host + "/login",
                data: JSON.stringify(data),
                dataType: "json",
                contentType: false,
                processData: false,
                success: function(data) {
                    if (data.result != "ok") {
                        showWarningToast("operation failed", data.message);
                    } else {
                        window.location.replace("http://" + host + "/cluster");
                    }
                },
                error: function() {
                    showWarningToast("error", "request service failed");
                }
            });
        } else {
            showWarningToast("error", "need name and password");
        }
    }
}