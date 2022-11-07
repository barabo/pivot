import unittest


class ImportTestCase(unittest.TestCase):
    def testImport(self):
        import pivot as _


class TestCase(unittest.TestCase):
    def setUp(self):
        from pivot import pivot as module

        self.module = module

    def testPivot(self):
        # fmt: off
        input = [
            "filename", "bytes", "type",
            "/foo/bar.sh", 123, "script",
            "/foo/baz.sh", 456, "script",
            "/foo/bar.py", 7890, "script",
            "/foo/bar", 1234, "exe",
        ]
        expected = [
            "filename", "bytes", "type:script", "type:exe",
            "/foo/bar.sh", 123, "1", "0",
            "/foo/baz.sh", 456, "1", "0",
            "/foo/bar.py", 7890, "1", "0",
            "/foo/bar", 1234, "0", "1",
        ]
        # fmt: on
        actual = self.module.pivot(input, headings=["type"])
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()
