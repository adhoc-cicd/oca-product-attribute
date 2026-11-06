# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from lxml import etree

from odoo.addons.base.tests.common import BaseCommon


class TestProductCode(BaseCommon):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.product_model = cls.env["product.product"]
        cls.product = cls.product_model.create({"name": "Test Product Code"})

    def test_product_code(self):
        """Check Product Code"""
        self.assertTrue(self.product.default_code, "Product code is not set.")

    def test_template_form_shows_code(self):
        """The template code stays visible with several variants"""
        view = self.env.ref("product.product_template_only_form_view")
        arch = self.env["product.template"].get_views([(view.id, "form")])["views"][
            "form"
        ]["arch"]
        node = etree.fromstring(arch).xpath("//field[@name='default_code']")[0]
        self.assertFalse(node.get("invisible"))
        self.assertEqual(node.get("required"), "product_variant_count == 1")
