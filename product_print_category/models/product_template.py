# Copyright (C) 2021-Today: Coop IT Easy (<http://coopiteasy.be>)
# Copyright (C) 2022-Today: GRAP (http://www.grap.coop)
# @author: Rémy TAYMANS (<remy@coopiteasy.be>)
# @author: Sylvain LE GAL (https://twitter.com/legalsylvain)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import api, fields, models


class ProductTemplate(models.Model):
    _name = "product.template"
    _inherit = ["product.template", "product.print.category.mixin"]

    print_category_id = fields.Many2one(
        string="Print Category",
        comodel_name="product.print.category",
        compute="_compute_print_category_id",
        inverse="_inverse_print_category_id",
    )

    to_print = fields.Boolean(compute="_compute_to_print", inverse="_inverse_to_print")

    @api.depends("product_variant_ids", "product_variant_ids.print_category_id")
    def _compute_print_category_id(self):
        unique_variants = self.filtered(
            lambda template: len(template.product_variant_ids) == 1
        )
        for template in unique_variants:
            template.print_category_id = template.product_variant_ids.print_category_id
        for template in self - unique_variants:
            template.print_category_id = False

    def _inverse_print_category_id(self):
        for template in self:
            if len(template.product_variant_ids) == 1:
                template.product_variant_ids.print_category_id = (
                    template.print_category_id
                )

    @api.depends("product_variant_ids", "product_variant_ids.to_print")
    def _compute_to_print(self):
        unique_variants = self.filtered(
            lambda template: len(template.product_variant_ids) == 1
        )
        for template in unique_variants:
            template.to_print = template.product_variant_ids.to_print
        for template in self - unique_variants:
            template.to_print = False

    def _inverse_to_print(self):
        for template in self:
            if len(template.product_variant_ids) == 1:
                template.product_variant_ids.to_print = template.to_print

    def write(self, vals):
        res = super().write(vals)
        if self.env.context.get("update_to_print_category", True):
            self._update_to_print_values(vals)
        return res
