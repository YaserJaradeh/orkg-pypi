from unittest import TestCase
from orkg import ORKG


class TestResources(TestCase):

    def test_by_id(self):
        orkg = ORKG()
        res = orkg.resources.by_id('R1')
        self.assertTrue(res.succeeded)

    def test_get(self):
        orkg = ORKG()
        res = orkg.resources.get()
        self.assertTrue(res.succeeded)
        self.assertEqual(len(res.content), 10)
