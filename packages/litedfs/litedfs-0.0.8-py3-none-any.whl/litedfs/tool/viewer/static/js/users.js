function usersInit (manager_host) {
    var $table_header = $(".header-fixed > thead");
    var $table_header_tr = $(".header-fixed > thead > tr");
    var $table_body = $(".header-fixed > tbody");
    var scrollBarSize = getBrowserScrollSize();
    var $btn_create = $("#btn_create");
    var $btn_search = $("#btn_search");
    var $btn_user_create = $('#btn_user_create');
    var $btn_user_update = $('#btn_user_update');
    var $btn_user_delete = $('#btn_user_delete');
    var user_info = {};
    var user_id = '';
    var filter_type = "";
    var filter_value = "";
    var current_page = 1;
    var current_page_size = 100;
    var host = window.location.host;

    getUserList();
    $btn_create.bind('click', showCreate);
    $btn_search.bind('click', search);
    $btn_user_create.bind('click', createUser);
    $("#user_create_modal").on("hidden.bs.modal", resetModal);
    $("#user_update_modal").on("hidden.bs.modal", resetModal);
    $btn_user_update.bind('click', updateUser);
    $btn_user_delete.bind('click', deleteUser);

    function showCreate() {
        $('#user_create_modal').modal('show');
    }

    function createUser() {
        var data = {};
        var name = $('#user_create_modal input#name').val();
        var password = $('#user_create_modal input#password').val();
        var confirm_password = $('#user_create_modal input#confirm-password').val();
        var email = $('#user_create_modal input#email').val();
        var phone = $('#user_create_modal input#phone').val();
        if (password == confirm_password) {
            data.name = name;
            data.password = password;
            data.email = email;
            data.phone = phone;
            $.ajax({
                type: "POST",
                url: "http://" + manager_host + "/user",
                data: JSON.stringify(data),
                dataType: "json",
                contentType: false,
                processData: false,
                success: function(data) {
                    if (data.result != "ok") {
                        showWarningToast("operation failed", data.message);
                    } else {
                        getUserList();
                    }
                    $('#user_create_modal').modal('hide');
                },
                error: function() {
                    showWarningToast("error", "request service failed");
                }
            });
        } else {
            showWarningToast("error", "password not equal to confirm password");
        }
    }

    function getUserList(user_id) {
        var url = "http://" + host + "/user?offset=" + ((current_page - 1) * current_page_size) + "&limit=" + current_page_size;
        if (filter_type) {
            url += "&" + filter_type + "=" + filter_value;
        }
        $.ajax({
            dataType: "json",
            url: url,
            success: function(data) {
                if (data.result != "ok") {
                    showWarningToast("operation failed", data.message);
                }
                $table_header_tr.empty();
                $table_body.empty();
                $table_header_tr.append(getHeaderTR('num', 'num', '#'));
                $table_header_tr.append(getHeaderTR('id', 'user id', 'user id'));
                $table_header_tr.append(getHeaderTR('name', 'name', 'name'));
                $table_header_tr.append(getHeaderTR('email', 'email', 'email'));
                $table_header_tr.append(getHeaderTR('phone', 'phone', 'phone'));
                $table_header_tr.append(getHeaderTR('ctime', 'create at', 'create at'));
                $table_header_tr.append(getHeaderTR('mtime', 'update at', 'update at'));
                $table_header_tr.append(getHeaderTR('operation', 'operation', 'operation'));
                var columns = [
                    "num",
                    "id",
                    "name",
                    "email",
                    "phone",
                    "ctime",
                    "mtime",
                    "operation"
                ];
                user_info = {};
                data.data.forEach(function (value, index, arrays) {
                    user_info[value["id"]] = value;
                    var tr = '<tr id="table_item">';
                    for (var i=0; i<columns.length; i++) {
                        var col = columns[i];
                        if (col == 'num') {
                            tr += '<td id="' + col + '"><div class="outer"><div class="inner">&nbsp;' + ((current_page - 1) * current_page_size + index + 1) + '</div></div></td>';
                        } else if (col == 'operation') {
                            tr += '<td id="' + col + '"><div class="outer"><div class="inner">';
                            tr += '<button id="' + value["id"] + '" type="button" class="btn btn-secondary btn-sm btn-operation btn-update" onclick="this.blur();"><span class="oi oi-arrow-circle-top" title="update" aria-hidden="true"></span></button>';
                            tr += '<button id="' + value["id"] + '" type="button" class="btn btn-secondary btn-sm btn-operation btn-delete" onclick="this.blur();"><span class="oi oi-circle-x" title="delete" aria-hidden="true"></span></button>';
                            tr += '<button id="' + value["id"] + '" type="button" class="btn btn-secondary btn-sm btn-operation btn-detail" onclick="this.blur();"><span class="oi oi-spreadsheet" title="detail" aria-hidden="true"></span></button>';
                            tr += '</div></div></td>';
                        } else if (col == 'id') {
                            tr += '<td id="' + col + '"><div class="outer"><div class="inner"><span class="span-pre">' + value[col] + '</span></div></div></td>';
                        } else if (col == 'name') {
                            tr += '<td id="' + col + '" title="' + value[col] + '"><div class="outer"><div class="inner">&nbsp;' + value[col] + '</div></div></td>';
                        } else if (col == 'ctime' || col == 'mtime') {
                            tr += '<td id="' + col + '"><div class="outer"><div class="inner"><span class="span-pre">' + dateFormat(value[col]) + '</span></div></div></td>';
                        } else {
                            tr += '<td id="' + col + '"><div class="outer"><div class="inner">&nbsp;' + value[col] + '</div></div></td>';
                        }
                    }
                    tr += '</tr>';
                    $table_body.append(tr);
                });

                var tbody = document.getElementById("table_body");
                if (hasVerticalScrollBar(tbody)) {
                    $table_header.css({"margin-right": scrollBarSize.width});
                }
                else {
                    $table_header.css({"margin-right": 0});
                }

                addColumnsCSS(columns);
                $(".btn-update").bind('click', showUserUpdate);
                $(".btn-delete").bind('click', showUserDelete);
                $(".btn-detail").bind('click', showUserInfo);

                if (user_id) {
                    var info = {};
                    if (user_info[user_id]) {
                        info = user_info[user_id];
                    }
                    document.getElementById("user_info_json").textContent = JSON.stringify(info, undefined, 4);
                }

                // generatePagination(current_page, current_page_size, 5, data.total);
                // $('a.page-num').bind('click', changePage);
                // $('a.previous-page').bind('click', previousPage);
                // $('a.next-page').bind('click', nextPage);

                hideWaitScreen();
            },
            error: function() {
                showWarningToast("error", "request service failed");
                hideWaitScreen();
            }
        });
    }

    function search() {
        filter_type = $('#filter').val();
        filter_value = $('input#filter_input').val();
        current_page = 1;
        getUserList();
    }

    function showUserUpdate() {
        user_id = $(this).attr("id");
        var info = user_info[user_id];
        $('#form_update input#name').val(info.name);
        $('#form_update input#password').val("");
        $('#form_update input#confirm-password').val("");
        $('#sform_update input#email').val(info.email);
        $('#form_update input#phone').val(info.phone);
        $('#user_update_modal').modal('show');
    }

    function updateUser() {
        var data = {};
        var name = $('#user_update_modal input#name').val();
        var password = $('#user_update_modal input#password').val();
        var confirm_password = $('#user_update_modal input#confirm-password').val();
        var email = $('#user_update_modal input#email').val();
        var phone = $('#user_update_modal input#phone').val();
        if (password == confirm_password) {
            data.id = user_id
            data.name = name;
            data.password = password;
            data.email = email;
            data.phone = phone;
            $.ajax({
                type: "PUT",
                url: "http://" + host + "/users",
                data: JSON.stringify(data),
                dataType: "json",
                contentType: false,
                processData: false,
                success: function(data) {
                    if (data.result != "ok") {
                        showWarningToast("operation failed", data.message);
                    } else {
                        getUserList();
                    }
                    $('#user_update_modal').modal('hide');
                },
                error: function() {
                    showWarningToast("error", "request service failed");
                }
            });
        } else {
            showWarningToast("error", "password not equal to confirm password");
        }
    }

    function showUserDelete() {
        user_id = $(this).attr("id");
        $('#user_delete_modal').modal('show');
    }

    function deleteUser() {
        $('#user_delete_modal').modal('hide');
        $.ajax({
            type: "DELETE",
            url: "http://" + manager_host + "/user/" + user_id,
            contentType: false,
            processData: false,
            success: function(data) {
                if (data.result != "ok") {
                    showWarningToast("operation failed", data.message);
                }
                getUserList();
            },
            error: function() {
                showWarningToast("error", "request service failed");
            }
        });
    }

    function showUserInfo() {
        var user_id = $(this).attr("id");
        document.getElementById("user_info_json").textContent = JSON.stringify(user_info[user_id], undefined, 4);
        $('#user_info_modal').modal('show');
    }

    function changePage() {
        current_page = Number($(this)[0].innerText);
        getUserList();
    }

    function previousPage() {
        current_page--;
        if (current_page < 1) {
            current_page = 1;
        }
        getUserList();
    }

    function nextPage() {
        current_page++;
        getUserList();
    }

    function resetModal(e) {
        $("#" + e.target.id).find("input:text").val("");
        $("#" + e.target.id).find("input:file").val(null);
        $("#" + e.target.id).find("textarea").val("");
    }

    function addColumnsCSS(keys) {
        var percent = 100.00;
        if (is_in('num', keys)) {
            $('th#num').css("width", "5%");
            $('td#num').css("width", "5%");
            percent -= 5.0;
        }
        if (is_in('name', keys)) {
            $('th#name').css("width", "10%");
            $('td#name').css("width", "10%");
            percent -= 10.0;
        }
        if (is_in('create_at', keys)) {
            $('th#create_at').css("width", "10%");
            $('td#create_at').css("width", "10%");
            percent -= 10.0;
        }
        if (is_in('update_at', keys)) {
            $('th#update_at').css("width", "10%");
            $('td#update_at').css("width", "10%");
            percent -= 10.0;
        }
        if (is_in('email', keys)) {
            $('th#email').css("width", "10%");
            $('td#email').css("width", "10%");
            percent -= 10.0;
        }
        if (is_in('phone', keys)) {
            $('th#phone').css("width", "10%");
            $('td#phone').css("width", "10%");
            percent -= 10.0;
        }
        if (is_in('operation', keys)) {
            $('th#operation').css("width", "8%");
            $('td#operation').css("width", "8%");
            percent -= 8.0;
        }
        if (is_in('id', keys)) {
            var width = percent;
            $('th#id').css("width", width + "%");
            $('td#id').css("width", width + "%");
        }
    }
}