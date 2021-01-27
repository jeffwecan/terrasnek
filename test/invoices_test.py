"""
Module for testing the Terraform Cloud API Endpoint: Invoices.
"""

from .base import TestTFCBaseTestCase


class TestTFCInvoices(TestTFCBaseTestCase):
    """
    Class for testing the Terraform Cloud API Endpoint: Invoices.
    """

    _unittest_name = "invoi"
    _endpoint_being_tested = "invoices"

    def test_invoices(self):
        """
        Test the Invoice API endpoints.
        """
        invoices = self._api.invoices.list()
        print(invoices)
