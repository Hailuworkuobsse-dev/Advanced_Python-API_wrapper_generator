import unittest
from api_wrapper_generator.core.spec_parser import parse_openapi_spec

class TestSpecParser(unittest.TestCase):
    def test_parse_valid_spec(self):
        endpoints, api_name = parse_openapi_spec("examples/petstore_api.yaml")
        self.assertEqual(api_name, "Petstore API")
        self.assertIn("list_pets", endpoints)

    def test_parse_invalid_spec(self):
        endpoints, api_name = parse_openapi_spec("non_existent_file.yaml")
        self.assertIsNone(endpoints)

if __name__ == '__main__':
    unittest.main()