# -*- encoding: utf-8 -*-
##############################################################################
#
# Copyright (c) 2004-2008 Tiny SPRL (http://tiny.be) All Rights Reserved.
#
# $Id$
#
# WARNING: This program as such is intended to be used by professional
# programmers who take the whole responsability of assessing all potential
# consequences resulting from its eventual inadequacies and bugs
# End users who are looking for a ready-to-use solution with commercial
# garantees and support are strongly adviced to contract a Free Software
# Service Company
#
# This program is Free Software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.
###############################################################################
{
    "name": "Products & Pricelists - Define quality control and testing "
            "parameters in product",
    "version": "1.0",
    "author": "Tiny,Odoo Community Association (OCA)",
    "category": "Generic Modules/Inventory Control",
    "depends": ["base", "process", "product", "stock", "mrp"],
    "init_xml": [],
    "demo_xml": [],
    "description": """
    This module add quality control and testing parameters in product
    1> configure QC parameters for particular product.
    2> QC testing on purchased raw material.
    3> QC testing during production.
    3> QC testing on finished goods.
    """,
    "update_xml": [
        "security/ir.model.access.csv",
        "wizard_view.xml",
        "product_qt_view.xml",
    ],
    "active": False,
    "installable": True
}
