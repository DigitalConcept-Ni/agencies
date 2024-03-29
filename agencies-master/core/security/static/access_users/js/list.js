var input_daterange;

var access_users = {
    config: [
        {
            targets: [0],
            visible: false,
        },
        {
            targets: [-2],
            class: 'text-center',
            render: function (data, type, row) {
                var name = data['name'];
                if (data['id'] === 'success') {
                    return '<span class="badge badge-success badge-pill">' + name + '</span>';
                }
                return '<span class="badge badge-danger badge-pill">' + name + '</span>';
            }
        },
        {
            targets: [-1],
            class: 'text-center',
            orderable: false,
            render: function (data, type, row) {
                return '<a rel="delete" class="btn btn-danger btn-xs btn-flat"><i class="fas fa-trash-alt"></i></a>';
            }
        },
    ],
    list: function (all) {
        var parameters = {
            'action': 'search',
            'start_date': input_daterange.data('daterangepicker').startDate.format('YYYY-MM-DD'),
            'end_date': input_daterange.data('daterangepicker').endDate.format('YYYY-MM-DD'),
        };
        if (all) {
            parameters['start_date'] = '';
            parameters['end_date'] = '';
        }

        let data = {
            'data': parameters,
            'inserInto': 'rowList',
            'th': ['Nro', 'Usuario', 'Registro', 'Direccion IP', 'Coordenadas', 'Exactitud', 'Intento', 'Opciones'],
            'table': 'tableList',
            'config': access_users.config,
            'modal': false,
        }

        drawTables(data);
        // $('#data').DataTable({
        //     responsive: true,
        //     // scrollX: true,
        //     // autoWidth: false,
        //     destroy: true,
        //     deferRender: true,
        //     ajax: {
        //         url: pathname,
        //         type: 'POST',
        //         data: parameters,
        //         dataSrc: "",
        //         headers: {
        //             'X-CSRFToken': csrftoken
        //         }
        //     },
        //     columns: [
        //         {"data": "id"},
        //         {"data": "user.username"},
        //         {"data": "date_joined"},
        //         {"data": "time_joined"},
        //         {"data": "ip_address"},
        //         {"data": "coords"},
        //         {"data": "accuracy"},
        //         {"data": "type.id"},
        //         {"data": "id"},
        //     ],
        //     order: [[2, "desc"], [3, "desc"]],
        //     columnDefs: [
        //         {
        //             targets: [-2],
        //             class: 'text-center',
        //             render: function (data, type, row) {
        //                 var name = row.type.name;
        //                 if (row.type.id === 'success') {
        //                     return '<span class="badge badge-success badge-pill">' + name + '</span>';
        //                 }
        //                 return '<span class="badge badge-danger badge-pill">' + name + '</span>';
        //             }
        //         },
        //         {
        //             targets: [-1],
        //             class: 'text-center',
        //             orderable: false,
        //             render: function (data, type, row) {
        //                 return '<a rel="delete" class="btn btn-danger btn-xs btn-flat"><i class="fas fa-trash-alt"></i></a>';
        //             }
        //         },
        //     ],
        //     initComplete: function (settings, json) {
        //
        //     }
        // });
    },
};

$(function () {

    input_daterange = $('input[name="date_range"]');

    input_daterange
        .daterangepicker({
            language: 'auto',
            startDate: new Date(),
            locale: {
                format: 'YYYY-MM-DD',
            }
        });

    $('.drp-buttons').hide();

    $('.btnSearch').on('click', function () {
        access_users.list(false);
    });

    $('.btnSearchAll').on('click', function () {
        access_users.list(true);
    });

    access_users.list(false);
});