var brands = {
    config: [
        {
            targets: [0],
            visible: false,
        },
        {
            targets: [-1],
            class: 'text-center',
            orderable: false,
            render: function (data, type, row) {
                var buttons = '<a href="' + pathname + 'update/' + row[0] + '/" class="btn btn-warning btn-xs btn-flat"><i class="fas fa-edit"></i></a> ';
                buttons += '<a rel="delete" type="button" class="btn btn-danger btn-xs btn-flat"><i class="fas fa-trash-alt"></i></a>';
                return buttons;
            }
        },
    ],
    list: function () {

        let data = {
            'data': {'action': 'search'},
            'inserInto': 'rowList',
            'th': ['Nro', 'Nombre', 'Descripcion', 'Opciones'],
            'table': 'tableList',
            'config': brands.config,
            'modal': false,
        }
        drawTables(data);
    }
};

$(function () {
    brands.list();
});
