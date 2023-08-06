import pathlib
import unittest

from cleanghostimages import cleanghostimages


class TestCleanGhostImages(unittest.TestCase):

    ___input_files_dir = f"{ pathlib.Path(__file__).parent }/input_files"

    def test_absent_images(self):

        self.assertEqual(cleanghostimages.get_absent_images(["image1"], ["image1", "image2", "image3"]), ["image2", "image3"])
        self.assertEqual(cleanghostimages.get_absent_images(["image1", "image2"], ["image1", "image2"]), [])
        self.assertEqual(cleanghostimages.get_absent_images([], []), [])
        self.assertEqual(cleanghostimages.get_absent_images(["image1", "image2"], ["image1"]), [])

    def test_unused_images(self):
        self.assertEqual(cleanghostimages.get_unused_images(["image1"], ["image1"]), [])
        self.assertEqual(cleanghostimages.get_unused_images(["image1", "image2"], ["image1"]), ["image2"])
        self.assertEqual(cleanghostimages.get_unused_images(["image1"], ["image1", "image2"]), [])
        self.assertEqual(cleanghostimages.get_unused_images(["image1", "image2", "image3", "image5"], ["image1", "image3"]), ["image2", "image5"])

    def test_get_file_export_content(self):
        file_content = cleanghostimages.get_file_export_content(f"{ self.___input_files_dir }/test_can_read_file.txt")
        expected_file_content = """If this
is returned

  the test passes."""
        self.assertEqual(file_content, expected_file_content)
        self.assertRaises(FileNotFoundError, cleanghostimages.get_file_export_content, "iTEq7JTwyKx5ud8J75chRd3EzusPRV")

    def test_get_images_from_export_file(self):
        with open(f"{ self.___input_files_dir }/ghost_export_part.txt") as file:
            result = cleanghostimages.get_images_from_export_file(file.read())
            expected = [
                'content/images/2020/08/illustration12_o-1.png',
                'content/images/2022/12/vendors_compromised_service.png',
                'content/images/2020/08/illustration12_o-1.png',
                'content/images/2020/08/illustration12_o-1.png',
                'content/images/2022/12/vendors_compromised_service.png',
                'content/images/2022/12/vendors_compromised_service.png',
                'content/images/2020/08/Screenshot-from-2019-03-16-13-01-47.png',
                'content/images/2020/08/programming-583923_1280-1.jpg',
                'content/images/2020/11/123e.png',
                'content/images/2020/11/m554.jpg',
                'content/images/size/w600/2020/08/illustration12_o-1.png',
                'content/images/size/w1000/2020/08/illustration12_o-1.png',
                'content/images/size/w1600/2020/08/illustration12_o-1.png',
                'content/images/size/w600/2022/12/vendors_compromised_service.png'
            ]

            self.assertEqual(len(result), 14)
            self.assertEqual(result, expected)

    def test_get_sanitized_images_location_from_folder(self):
        ghost_install_dir = f"{ self.___input_files_dir }/test_get_images_from_folder"
        found_files = cleanghostimages.get_sanitized_images_location_from_folder(ghost_install_dir)
        expected_files = [
            'content/images/2022/01/dummy_file_3.png',
            'content/images/2022/12/dummy_file_3.jpeg',
            'content/images/size/w1000/2021/06/dummy_file_2.jpg',
            'content/images/size/w1000/2021/06/dummy_file_1.png'
        ]
        self.assertEqual(sorted(found_files), sorted(expected_files))

        # Test with an extra / to check that the content is still what is expected
        ghost_install_dir = f"{ self.___input_files_dir }//test_get_images_from_folder"
        found_files = cleanghostimages.get_sanitized_images_location_from_folder(ghost_install_dir)
        self.assertEqual(sorted(found_files), sorted(expected_files))

        self.assertRaises(FileNotFoundError, cleanghostimages.get_sanitized_images_location_from_folder, "/this/does/not/exist")

    def test_get_arguments_parser(self):
        parser = cleanghostimages.get_arguments_parser()

        # Test the required arguments
        self.assertRaises(SystemExit, parser.parse_args, "")
        self.assertRaises(SystemExit, parser.parse_args, "--json-export-file test".split(" "))
        self.assertRaises(SystemExit, parser.parse_args, "--ghost-dir test".split(" "))
        args = parser.parse_args("--ghost-dir test --json-export-file test2".split(" "))

        # Tests that the values are set where they should
        self.assertEqual(args.ghost_dir, "test")
        self.assertEqual(args.json_export_file, "test2")
        self.assertFalse(args.print_missing_images)
        self.assertFalse(args.statistics)
        self.assertFalse(args.print_unused_images)
        args = parser.parse_args("--json-export-file test1 --ghost-dir test2 --print-missing-images --statistics --print-unused-images".split(" "))
        self.assertTrue(args.print_missing_images)
        self.assertTrue(args.statistics)
        self.assertTrue(args.print_unused_images)
