from collections import namedtuple
import json
import jsonfunctions
import unittest


class MyTestCase(unittest.TestCase):
    # Test type: Approval test
    def test_add_two_rects(self):
        golden_json_file = open('approvaltestdata/json_example.json')
        data_golden = json.load(golden_json_file)
        json_file_example = open('templatejson.json')
        data_example = json.load(json_file_example)

        Points = namedtuple('Points', ['x1', 'y1', 'x2', 'y2'])
        first_rect = Points(579, 584, 924, 1120)
        jason_output = jsonfunctions.add_rect_to_json(first_rect, "class1", data_example)
        second_rect = Points(120, 400, 1150, 800)
        jason_output = jsonfunctions.add_rect_to_json(second_rect, "class1", jason_output)
        self.assertEqual(data_golden, jason_output)


if __name__ == '__main__':
    unittest.main()
