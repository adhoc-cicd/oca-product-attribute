# -*- encoding: utf-8 -*-
###############################################################################
#                                                                             #
#   product_custom_attributes for OpenERP                                     #
#   Copyright (C) 2011 Akretion Benoît GUILLOT <benoit.guillot@akretion.com>  #
#                                                                             #
#   This program is free software: you can redistribute it and/or modify      #
#   it under the terms of the GNU Affero General Public License as            #
#   published by the Free Software Foundation, either version 3 of the        #
#   License, or (at your option) any later version.                           #
#                                                                             #
#   This program is distributed in the hope that it will be useful,           #
#   but WITHOUT ANY WARRANTY; without even the implied warranty of            #
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the             #
#   GNU Affero General Public License for more details.                       #
#                                                                             #
#   You should have received a copy of the GNU Affero General Public License  #
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.     #
#                                                                             #
###############################################################################

{
    'name': 'product_custom_attributes',
    'version': '6.1.0',
    'category': 'Generic Modules/Others',
    'license': 'AGPL-3',
    'description': """
    This module adds the posibility to easily create custom fields on products.
    Each product can be linked to an attribute set (such as camera, fridge...)
    and each attribute set has custom fields (for example you don't need the
    same field for a frigde and a camera)

    Need to install the lib unicode2ascii,
    http://github.com/akretion/unicode2ascii.git
    """,
    'author': "Akretion,Odoo Community Association (OCA)",
    'website': 'http://www.akretion.com/',
    'depends': ['product', 'stock'],
    'init_xml': [],
    'update_xml': [
        'ir_model_view.xml',
        'product_attribute_view.xml',
        'product_view.xml',
        'wizard/open_product_by_attribute_set.xml',
    ],
    'demo_xml': [],
    'installable': True,
    'active': False,
}
