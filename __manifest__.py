{
    'name': 'Stock Transport',
    'version': '1.0',
    'summary': 'stock transport application',
    'depends':[
        'base',
        'fleet',
        'stock_picking_batch',
    ],
    'data': [
        'security/ir.model.access.csv',

        'views/tms_stock_transport_view.xml',
        'views/tms_stock_batch_view.xml',
    ],
    'installable': True,
    'license': 'LGPL-3',
}

