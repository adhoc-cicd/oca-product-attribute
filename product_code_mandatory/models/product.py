# Copyright (C) 2018 - TODAY, Open Source Integrators
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    def _prepare_variant_values(self, combination):
        res = super()._prepare_variant_values(combination)
        # Only a template with a single variant passes its code on. With
        # attributes, each variant gets its own unique code.
        if self.default_code and not self.attribute_line_ids:
            res.update({"default_code": self.default_code})
        return res


class ProductProduct(models.Model):
    _inherit = "product.product"

    @api.model
    def _get_default_code(self):
        """Generate a new default_code using sequence."""
        return self.env["ir.sequence"].next_by_code("product.default.code")

    default_code = fields.Char(
        "Internal Reference", index=True, default=lambda self: self._get_default_code()
    )

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            # Generate the code only when none is provided, so codes coming
            # from the UI or an import are respected.
            if not vals.get("default_code"):
                vals["default_code"] = self._get_default_code()
        return super().create(vals_list)
