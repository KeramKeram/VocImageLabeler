from collections import namedtuple
from commondatajson import CommonJsonData
import json
import jsonfunctions
import unittest


class MyTestCase(unittest.TestCase):
    # Test type: Approval test
    def test_add_two_rects(self):
        golden_json_file = open('approvaltestdata/jsonexample.json')
        data_golden = json.load(golden_json_file)
        json_file_example = open('testtemplatejson.json')
        data_example = json.load(json_file_example)

        Points = namedtuple('Points', ['x1', 'y1', 'x2', 'y2'])
        first_rect = Points(579, 584, 924, 1120)
        jason_output = jsonfunctions.add_rect_to_json(first_rect, "class1", data_example)
        second_rect = Points(120, 400, 1150, 800)
        jason_output = jsonfunctions.add_rect_to_json(second_rect, "class1", jason_output)
        self.assertEqual(data_golden, jason_output)

    def test_prepare_json_file(self):
        golden_json_file = open('approvaltestdata/jsontestprepare.json')
        data_golden = json.load(golden_json_file)
        test_data = CommonJsonData("/home/user/", "test.jpg", "/home/user/test.jpg", 800, 600)
        output_json = jsonfunctions.prepare_json_file(test_data)
        self.assertEqual(data_golden, output_json)


if __name__ == '__main__':
    unittest.main()
