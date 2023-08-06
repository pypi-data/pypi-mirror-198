function filesystemInit () {
    var $table_header = $(".header-fixed > thead");
    var $table_header_tr = $(".header-fixed > thead > tr");
    var $table_body = $(".header-fixed > tbody");
    var scrollBarSize = getBrowserScrollSize();
    var $btn_show_summary = $("#btn_show_summary");
    var $btn_show_clean_all = $("#btn_show_clean_all");
    var $btn_show_export = $("#btn_show_export");
    var $btn_delete_ok = $('#btn_delete_ok');
    var $btn_edit_save = $('#btn_edit_save');
    var $btn_clean_ok = $('#btn_clean_ok');
    var $btn_export_ok = $('#btn_export_ok');
    var current_page = 1;
    var current_page_size = 1000;
    var logs_info = {};
    var summary = {};
    var host = window.location.host;
    var delete_log_id = 0;
    var edit_log_id = 0;

    $btn_show_summary.bind('click', showSummary);
    $btn_show_clean_all.bind('click', showLogClean);
    $btn_clean_ok.bind('click', cleanAllChanges);
    $btn_show_export.bind('click', showLogExport);
    $btn_export_ok.bind('click', exportAllChanges);
    $btn_delete_ok.bind('click', deleteRecoverLine);
    $btn_edit_save.bind('click', editRecoverLine);


    getFileSystemLogs();
    

    function getFileSystemLogs() {
        $.ajax({
            dataType: "json",
            url: "http://" + host + "/filesystem/logs?offset=" + (((current_page - 1) * current_page_size) + 1) + "&limit=" + current_page_size,
            success: function(data) {
                if (data.result != "ok") {
                    showWarningToast("operation failed", data.message);
                }
                $table_header_tr.empty();
                $table_body.empty();
                $table_header_tr.append(getHeaderTR('num', 'num', '#'));
                $table_header_tr.append(getHeaderTR('source', 'source', 'source'));
                $table_header_tr.append(getHeaderTR('action', 'action', 'action'));
                $table_header_tr.append(getHeaderTR('path', 'path', 'path'));
                $table_header_tr.append(getHeaderTR('ctime', 'ctime', 'ctime'));
                $table_header_tr.append(getHeaderTR('mtime', 'mtime', 'mtime'));
                $table_header_tr.append(getHeaderTR('operation', 'operation', 'operation'));
                var columns = [
                    "num",
                    "source",
                    "action",
                    "path",
                    "ctime",
                    "mtime",
                    "operation"
                ];
                logs_info = {};
                data.logs.forEach(function (value, index, arrays) {
                    logs_info[value["num"]] = value;
                    var tr = '<tr id="table_item"' + ' class=' + value["status"] + '>';
                    for (var i=0; i<columns.length; i++) {
                        var col = columns[i];
                        if (col == 'num') {
                            tr += '<td id="' + col + '"><div class="outer"><div class="inner">&nbsp;' + value[col] + '</div></div></td>';
                        } else if (col == 'operation') {
                            tr += '<td id="' + col + '"><div class="outer"><div class="inner">';
                            tr += '<button id="' + value["num"] + '" type="button" class="btn btn-secondary btn-sm btn-operation btn-edit" onclick="this.blur();"><span class="oi oi-pencil" title="edit" aria-hidden="true"></span></button>';
                            tr += '<button id="' + value["num"] + '" type="button" class="btn btn-secondary btn-sm btn-operation btn-delete" onclick="this.blur();"><span class="oi oi-trash" title="delete" aria-hidden="true"></span></button>';
                            tr += '<button id="' + value["num"] + '" type="button" class="btn btn-secondary btn-sm btn-operation btn-detail" onclick="this.blur();"><span class="oi oi-spreadsheet" title="detail" aria-hidden="true"></span></button>';
                            tr += '</div></div></td>';
                        } else if (col == 'path' || col == 'action' || col == 'ctime' || col == 'mtime' || col == 'source') {
                            tr += '<td id="' + col + '"><div class="outer"><div class="inner"><span class="span-pre">' + value[col] + '</span></div></div></td>';
                        } else {
                            tr += '<td id="' + col + '"><div class="outer"><div class="inner">&nbsp;' + value[col] + '</div></div></td>';
                        }
                    }
                    tr += '</tr>';
                    $table_body.append(tr);
                });
                summary.total = data.total;
                summary.fsimage_total = data.fsimage_total;
                summary.editlog_total = data.editlog_total;

                var tbody = document.getElementById("table_body");
                if (hasVerticalScrollBar(tbody)) {
                    $table_header.css({"margin-right": scrollBarSize.width});
                }
                else {
                    $table_header.css({"margin-right": 0});
                }

                addColumnsCSS(columns);
                $(".btn-edit").bind('click', showLogEdit);
                $(".btn-delete").bind('click', showLogDelete);
                $(".btn-detail").bind('click', showLogDetail);

                generatePagination('#ul-pagination', current_page, current_page_size, 5, data.total);
                $('a.page-num').bind('click', changePage);
                $('a.previous-page').bind('click', previousPage);
                $('a.next-page').bind('click', nextPage);
            },
            error: function() {
                showWarningToast("error", "request service failed");
            }
        });
    }

    function showSummary() {
        document.getElementById("summary_json").textContent = JSON.stringify(summary, undefined, 4);
        $('#log_summary_modal').modal('show');
    }

    function showLogClean() {
        $('#log_clean_modal').modal('show');
    }

    function cleanAllChanges() {
        var data = {};
        data.params = {};
        data.command = "clean_all";
        $('#log_clean_modal').modal('hide');
        $.ajax({
            type: "PUT",
            url: "http://" + host + "/filesystem/logs",
            data: JSON.stringify(data),
            dataType: "json",
            contentType: false,
            processData: false,
            success: function(data) {
                if (data.result != "ok") {
                    showWarningToast("operation failed", data.message);
                }
                getFileSystemLogs();
            },
            error: function() {
                showWarningToast("error", "request service failed");
            }
        });
    }

    function showLogExport() {
        $('#log_export_modal').modal('show');
    }

    function exportAllChanges() {
        var data = {};
        data.params = {};
        data.command = "export";
        $('#log_export_modal').modal('hide');
        $.ajax({
            type: "PUT",
            url: "http://" + host + "/filesystem/logs",
            data: JSON.stringify(data),
            dataType: "json",
            contentType: false,
            processData: false,
            success: function(data) {
                if (data.result != "ok") {
                    showWarningToast("operation failed", data.message);
                }
                getFileSystemLogs();
            },
            error: function() {
                showWarningToast("error", "request service failed");
            }
        });
    }

    function showLogEdit() {
        var log_id = $(this).attr("id");
        edit_log_id = log_id;
        var log_info = logs_info[log_id];
        var log_content = log_info.raw;
        if (log_info.status == "edit") {
            log_content = log_info.new;
        }
        $('#log_edit_modal textarea#log_info').val(JSON.stringify(log_content, undefined, 4));
        $('#log_edit_modal').modal('show');
    }

    function editRecoverLine() {
        var data = {};
        var log_info = logs_info[edit_log_id];
        data.params = {};
        data.params.line_num = edit_log_id;
        var log_content = $('#log_edit_modal textarea#log_info').val();
        if (log_content) {
            data.command = "edit";
            data.params.content = JSON.parse(log_content);
        } else {
            data.command = "edit_cancel";
        }
        $('#log_edit_modal').modal('hide');
        $.ajax({
            type: "PUT",
            url: "http://" + host + "/filesystem/logs",
            data: JSON.stringify(data),
            dataType: "json",
            contentType: false,
            processData: false,
            success: function(data) {
                if (data.result != "ok") {
                    showWarningToast("operation failed", data.message);
                }
                getFileSystemLogs();
            },
            error: function() {
                showWarningToast("error", "request service failed");
            }
        });
    }

    function showLogDelete() {
        var log_id = $(this).attr("id");
        delete_log_id = log_id;
        var log_info = logs_info[log_id];
        if (log_info.status == "delete") {
            $('p#delete_message').text("Do you want to recover this line:" + log_id + "?");
        } else {
            $('p#delete_message').text("Do you want to delete this line:" + log_id + "?");
        }
        $('#log_delete_modal').modal('show');
    }

    function deleteRecoverLine() {
        var data = {};
        var log_info = logs_info[delete_log_id];
        data.command = "delete";
        if (log_info.status == "delete") {
            data.command = "delete_cancel";
        }
        data.params = {};
        data.params.line_num = delete_log_id;
        $('#log_delete_modal').modal('hide');
        $.ajax({
            type: "PUT",
            url: "http://" + host + "/filesystem/logs",
            data: JSON.stringify(data),
            dataType: "json",
            contentType: false,
            processData: false,
            success: function(data) {
                if (data.result != "ok") {
                    showWarningToast("operation failed", data.message);
                }
                getFileSystemLogs();
            },
            error: function() {
                showWarningToast("error", "request service failed");
            }
        });
    }

    function showLogDetail() {
        var log_id = $(this).attr("id");
        document.getElementById("log_info_json").textContent = JSON.stringify(logs_info[log_id], undefined, 4);
        $('#log_info_modal').modal('show');
    }

    function changePage() {
        current_page = Number($(this)[0].innerText);
        getFileSystemLogs();
    }

    function previousPage() {
        current_page--;
        if (current_page < 1) {
            current_page = 1;
        }
        getFileSystemLogs();
    }

    function nextPage() {
        current_page++;
        getFileSystemLogs();
    }

    function addColumnsCSS(keys) {
        var percent = 100.00;
        if (is_in('num', keys)) {
            $('th#num').css("width", "5%");
            $('td#num').css("width", "5%");
            percent -= 5.0;
        }
        if (is_in('source', keys)) {
            $('th#source').css("width", "5%");
            $('td#source').css("width", "5%");
            percent -= 5.0;
        }
        if (is_in('action', keys)) {
            $('th#action').css("width", "5%");
            $('td#action').css("width", "5%");
            percent -= 5.0;
        }
        if (is_in('ctime', keys)) {
            $('th#ctime').css("width", "10%");
            $('td#ctime').css("width", "10%");
            percent -= 10.0;
        }
        if (is_in('mtime', keys)) {
            $('th#mtime').css("width", "10%");
            $('td#mtime').css("width", "10%");
            percent -= 10.0;
        }
        if (is_in('operation', keys)) {
            $('th#operation').css("width", "8%");
            $('td#operation').css("width", "8%");
            percent -= 8.0;
        }
        if (is_in('path', keys)) {
            var width = percent;
            $('th#path').css("width", width + "%");
            $('td#path').css("width", width + "%");
        }
    }
}