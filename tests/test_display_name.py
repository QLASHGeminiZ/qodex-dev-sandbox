import unittest

from display_name import normalise_display_name


class DisplayNameTests(unittest.TestCase):
    def test_trims_the_ends(self):
        self.assertEqual(normalise_display_name("  Qodex  "), "Qodex")

    def test_preserves_unicode(self):
        self.assertEqual(normalise_display_name("  Città 世界  "), "Città 世界")

    def test_empty_name(self):
        self.assertEqual(normalise_display_name("  "), "")

    def test_rejects_non_text(self):
        with self.assertRaises(TypeError):
            normalise_display_name(None)


if __name__ == "__main__":
    unittest.main()
