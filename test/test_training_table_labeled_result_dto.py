"""
    Butler REST API Documentation

           Welcome to Butler API Documentation and Explorer       Butler API is built on and conforms to Open API 3.0 spec.       This enables you to automatically generate language specific clients for       languages/frameworks listed here: https://openapi-generator.tech/docs/generators/#client-generators         # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import butler
from butler.model.model_field_type import ModelFieldType
from butler.model.training_column_dto import TrainingColumnDto
from butler.model.training_row_labeled_result_dto import TrainingRowLabeledResultDto
globals()['ModelFieldType'] = ModelFieldType
globals()['TrainingColumnDto'] = TrainingColumnDto
globals()['TrainingRowLabeledResultDto'] = TrainingRowLabeledResultDto
from butler.model.training_table_labeled_result_dto import TrainingTableLabeledResultDto


class TestTrainingTableLabeledResultDto(unittest.TestCase):
    """TrainingTableLabeledResultDto unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testTrainingTableLabeledResultDto(self):
        """Test TrainingTableLabeledResultDto"""
        # FIXME: construct object with mandatory attributes with example values
        # model = TrainingTableLabeledResultDto()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()