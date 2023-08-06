function groupInfoInit (manager_host) {
    var $table_header = $(".header-fixed > thead");
    var $table_header_tr = $(".header-fixed > thead > tr");
    var $table_body = $(".header-fixed > tbody");
    var scrollBarSize = getBrowserScrollSize();
    var $btn_create = $("#btn_create");
    var $btn_search = $("#btn_search");
    var $btn_group_create = $('#btn_group_create');
    var $btn_group_update = $('#btn_group_update');
    var $btn_group_delete = $('#btn_group_delete');
    var group_info = {};
    var group_id = '';
    var filter_type = "";
    var filter_value = "";
    var current_page = 1;
    var current_page_size = 100;
    var host = window.location.host;

    getGroupList();
    $btn_create.bind('click', showCreate);
    $btn_search.bind('click', search);
    $btn_group_create.bind('click', createGroup);
    $("#group_create_modal").on("hidden.bs.modal", resetModal);
    $("#group_update_modal").on("hidden.bs.modal", resetModal);
    $btn_group_update.bind('click', updateGroup);
    $btn_group_delete.bind('click', deleteGroup);

    function showCreate() {
        $('#group_create_modal').modal('show');
    }

    function createGroup() {
        var data = {};
        var name = $('#group_create_modal input#name').val();
        var owner = $('#group_create_modal input#owner').val();
        data.name = name;
        data.owner = owner;
        $.ajax({
            type: "POST",
            url: "http://" + manager_host + "/group",
            data: JSON.stringify(data),
            dataType: "json",
            contentType: false,
            processData: false,
            success: function(data) {
                if (data.result != "ok") {
                    showWarningToast("operation failed", data.message);
                } else {
                    getGroupList();
                }
                $('#group_create_modal').modal('hide');
            },
            error: function() {
                showWarningToast("error", "request service failed");
            }
        });
    }

    function getGroupList(group_id) {
        var url = "http://" + manager_host + "/group?offset=" + ((current_page - 1) * current_page_size) + "&limit=" + current_page_size;
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
                $table_header_tr.append(getHeaderTR('id', 'group id', 'group id'));
                $table_header_tr.append(getHeaderTR('name', 'name', 'name'));
                $table_header_tr.append(getHeaderTR('owner', 'owner', 'owner'));
                $table_header_tr.append(getHeaderTR('ctime', 'create at', 'create at'));
                $table_header_tr.append(getHeaderTR('mtime', 'update at', 'update at'));
                $table_header_tr.append(getHeaderTR('operation', 'operation', 'operation'));
                var columns = [
                    "num",
                    "id",
                    "name",
                    "owner",
                    "ctime",
                    "mtime",
                    "operation"
                ];
                group_info = {};
                data.data.forEach(function (value, index, arrays) {
                    group_info[value["id"]] = value;
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
                $(".btn-update").bind('click', showGroupUpdate);
                $(".btn-delete").bind('click', showGroupDelete);
                $(".btn-detail").bind('click', showGroupInfo);

                if (group_id) {
                    var info = {};
                    if (group_info[group_id]) {
                        info = group_info[group_id];
                    }
                    document.getElementById("group_info_json").textContent = JSON.stringify(info, undefined, 4);
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
        getGroupList();
    }

    function showGroupUpdate() {
        group_id = $(this).attr("id");
        var info = group_info[group_id];
        $('#form_update input#name').val(info.name);
        $('#form_update input#owner').val(info.owner);
        $('#group_update_modal').modal('show');
    }

    function updateGroup() {
        var data = {};
        var name = $('#group_update_modal input#name').val();
        var owner = $('#group_update_modal input#owner').val();
        data.id = group_id
        data.name = name;
        data.owner = owner;
        $.ajax({
            type: "PUT",
            url: "http://" + host + "/groups",
            data: JSON.stringify(data),
            dataType: "json",
            contentType: false,
            processData: false,
            success: function(data) {
                if (data.result != "ok") {
                    showWarningToast("operation failed", data.message);
                } else {
                    getGroupList();
                }
                $('#group_update_modal').modal('hide');
            },
            error: function() {
                showWarningToast("error", "request service failed");
            }
        });
    }

    function showGroupDelete() {
        group_id = $(this).attr("id");
        $('#group_delete_modal').modal('show');
    }

    function deleteGroup() {
        $('#group_delete_modal').modal('hide');
        $.ajax({
            type: "DELETE",
            url: "http://" + manager_host + "/group/" + group_id,
            contentType: false,
            processData: false,
            success: function(data) {
                if (data.result != "ok") {
                    showWarningToast("operation failed", data.message);
                }
                getGroupList();
            },
            error: function() {
                showWarningToast("error", "request service failed");
            }
        });
    }

    function showGroupInfo() {
        var group_id = $(this).attr("id");
        document.getElementById("group_info_json").textContent = JSON.stringify(group_info[group_id], undefined, 4);
        $('#group_info_modal').modal('show');
    }

    function changePage() {
        current_page = Number($(this)[0].innerText);
        getGroupList();
    }

    function previousPage() {
        current_page--;
        if (current_page < 1) {
            current_page = 1;
        }
        getGroupList();
    }

    function nextPage() {
        current_page++;
        getGroupList();
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
        if (is_in('owner', keys)) {
            $('th#owner').css("width", "10%");
            $('td#owner').css("width", "10%");
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