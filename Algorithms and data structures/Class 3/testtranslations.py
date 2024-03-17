import os
import json
import unittest
from translations import collect_tbt_values, write_result_file


class TestTranslations(unittest.TestCase):
    def setUp(self):
        self.folder_path = 'test_translations'
        os.makedirs(self.folder_path, exist_ok=True)
        self.file_contents = {
            'file1.json': {
                "key1": "TBT:value1",
                "key2": "value2",
                "key3": "TBT:value3"
            },
            'file2.json': {
                "key4": "value4",
                "key5": "TBT:value5"
            }
        }
        for file_name, content in self.file_contents.items():
            file_path = os.path.join(self.folder_path, file_name)
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(content, f)

    def tearDown(self):
        for file_name in self.file_contents:
            file_path = os.path.join(self.folder_path, file_name)
            os.remove(file_path)
        os.rmdir(self.folder_path)

    def test_collect_tbt_values(self):
        tbt_data = collect_tbt_values(self.folder_path)

        expected_tbt_data = {
            'file1.json': {
                "key1": "TBT:value1",
                "key3": "TBT:value3"
            },
            'file2.json': {
                "key5": "TBT:value5"
            }
        }

        self.assertEqual(tbt_data, expected_tbt_data, "Collected TBT data does not match expected data")

    def test_write_result_file(self):
        # Test data
        test_data = {
            'file1.json': {
                "key1": "TBT:value1",
                "key3": "TBT:value3"
            },
            'file2.json': {
                "key5": "TBT:value5"
            }
        }

        result_file_path = 'test_result_file.json'
        write_result_file(test_data, result_file_path)

        self.assertTrue(os.path.exists(result_file_path))
        with open(result_file_path, 'r', encoding='utf-8') as f:
            result_data = json.load(f)
        self.assertEqual(result_data, test_data)


if __name__ == '__main__':
    unittest.main()
