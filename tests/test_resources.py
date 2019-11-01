from unittest import TestCase
from orkg import ORKG


class TestResources(TestCase):
    """
    Some test scenarios might need to be adjusted to the content of the running ORKG instance
    """

    def test_by_id(self):
        orkg = ORKG()
        res = orkg.resources.by_id('R1')
        self.assertTrue(res.succeeded)

    def test_get(self):
        orkg = ORKG()
        res = orkg.resources.get()
        self.assertTrue(res.succeeded)
        self.assertEqual(len(res.content), 10)

    def test_get_with_items(self):
        orkg = ORKG()
        count = 30
        res = orkg.resources.get(items=30)
        self.assertTrue(res.succeeded)
        self.assertEqual(len(res.content), 30)
