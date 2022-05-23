"""
    Butler REST API Documentation

           Welcome to Butler API Documentation and Explorer       Butler API is built on and conforms to Open API 3.0 spec.       This enables you to automatically generate language specific clients for       languages/frameworks listed here: https://openapi-generator.tech/docs/generators/#client-generators         # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Generated by: https://openapi-generator.tech
"""


import unittest

import butler
from butler.api.apps_api import AppsApi  # noqa: E501


class TestAppsApi(unittest.TestCase):
    """AppsApi unit test stubs"""

    def setUp(self):
        self.api = AppsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_app_run_status(self):
        """Test case for get_app_run_status

        Get the status of an extraction job started by the upload_documents endpoint  # noqa: E501
        """
        pass

    def test_get_document_extraction_results(self):
        """Test case for get_document_extraction_results

        Get extracted results of an extraction job started by the upload_documents endpoint after it completes  # noqa: E501
        """
        pass

    def test_upload_documents(self):
        """Test case for upload_documents

        Upload documents (PDFs, and image formats) to your app to start an extraction job. Returns an appRunId that can be used to check the status of the extraction job, and get its results  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
