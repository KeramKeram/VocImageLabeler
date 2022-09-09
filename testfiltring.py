import filtring
import unittest


class MyTestCase(unittest.TestCase):
    def test_xml_filtering(self):
        list_files = [
            "Nok_original_train2_original_zgaedgeasg3453.png_483ab944-21c0-4055-b44c-81868860f2d6.png_fe6ba0eb-d49a-4ae6-89dc-21b8a75788ca.png",
            "Nok_original_train2_original_zgaedgeasg3453.xml",
            "nok_train_original_06_08_2022_21_43_42_cam0.jpg_d5819c8d-5ecd-4a6e-9c47-5e5fc340fd5b.jpg",
            "nok_train_original_06_08_2022_21_43_42_cam0.xml",
            "nok_train_original_06_08_2022_21_43_56_cam0.jpg_2511282f-8c50-4bbf-a274-1ea1c609e4f4.jpg",
            "nok_train_original_06_08_2022_21_43_56_cam0.jpg_34e7fbae-3842-42ae-b12e-0ec3fdd96d78.jpg",
            "nok_train_original_06_08_2022_21_43_58_cam0.jpg_2b7d18e7-5f3d-4f0f-ae85-cede921f0805.jpg",
            "nok_train_original_06_08_2022_21_43_58_cam0.jpg_85a76bf6-488f-45d0-8c80-9bb928797695.jpg",
            "nok_train_original_06_08_2022_21_43_58_cam0.xml",
            "t1_ogon.png",
            "t1_ogon.xml",
            "t2_ogon.png",
            "t2_ogon.xml",
            "t3_ogon.png",
            "t3_ogon.xml",
            "t4_ogon.png",
            "t4_ogon.xml",
            "test_original_WIN_20220202_16_13_59_ProCropped.png_7963d977-bf2d-4a3d-b887-5e8503f9bb3c.png",
            "test_original_WIN_20220202_16_13_59_ProCropped.xml"
            ]
        filtered_files = filtring.remove_xml_from_file_list(list_files)
        self.assertEqual(len(filtered_files), 11)


if __name__ == '__main__':
    unittest.main()
