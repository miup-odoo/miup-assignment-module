{
    'name': 'Activate Stock Transport',
    'version': '1.0',
    'summary': 'activation stock transport application',
    'depends':[
        'base',
        'stock',
        'stock_picking_batch'
    ],
    'data': [
        'views/res_config_setting_view.xml',
    ],
    'installable': True,
    'license': 'LGPL-3',
}
