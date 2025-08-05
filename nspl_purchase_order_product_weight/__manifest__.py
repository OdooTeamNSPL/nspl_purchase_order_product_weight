{
    'name': 'Purchase Order Product Weight Information',
    'version': '17.0',
    'summary': 'Show product weight in Purchase Order lines and reports.',
    'description': """
    This module displays product weight details directly in Purchase Orders:

    ✔ Automatically shows product weight in Purchase Order lines  
    ✔ Dynamically calculates total weight based on ordered quantity  
    ✔ Weight details included in RFQ and Purchase Order PDF reports  
    ✔ Set product weight in Product > Inventory tab  

    Simplify logistics and ensure accurate documentation with this enhancement.
    """,
    'sequence': 11,
    'author': 'Namah Softech Private Limited',
    'maintainer': 'Namah Softech Private Limited',
    'company': 'Namah Softech Private Limited',
    'website': 'https://www.namahsoftech.com',
    'support': 'support@namahsoftech.com',
    'price': 19.99,
    'currency': 'USD',
    'contributors': ['Shivani Solanki'],
    'license': 'AGPL-3',
    'depends': ['purchase', 'product', 'stock'],
    'data': [
        'views/purchase_order_views.xml',
        'report/purchase_order_report_templates.xml',
        'report/purchase_order_report.xml',
    ],
    'images': ['static/description/img/banner.png'],
    'installable': True,
    'application': False,
    'auto_install': False,
}
