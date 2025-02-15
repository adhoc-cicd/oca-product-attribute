##########################################################################
# Copyright (C) 2009  Sharoon Thomas  & Open ERP Community               #
#                                                                        #
# This program is free software: you can redistribute it and/or modify   #
# it under the terms of the GNU General Public License as published by   #
# the Free Software Foundation, either version 3 of the License, or      #
# (at your option) any later version.                                    #
#                                                                        #
# This program is distributed in the hope that it will be useful,        #
# but WITHOUT ANY WARRANTY; without even the implied warranty of         #
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the          #
# GNU General Public License for more details.                           #
#                                                                        #
# You should have received a copy of the GNU General Public License      #
# along with this program.  If not, see <http://www.gnu.org/licenses/>.  #
##########################################################################

{
    "name": "Product - Many Categories",
    "version": "6.1.0",
    "author": "Sharoon Thomas,Odoo Community Association (OCA)",
    "website": "",
    "category": "Added functionality",
    "depends": ['base', 'product'],
    "description": """
    This module extends the existing functionality of OpenERP Products
    (One product -> One Category)
    to One product -> Many Categories

    * Note: This module was built generically but in focus of the Magento
    OpenERP connector
    """,
    "init_xml": [],
    "update_xml": [
            'product_view.xml'
    ],
    "installable": True,
    "active": False,
}
