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

    def test_add(self):
        orkg = ORKG()
        label = "test"
        res = orkg.resources.add(label=label)
        self.assertTrue(res.succeeded)
        self.assertEqual(res.content['label'], label)

    def test_update(self):
        orkg = ORKG()
        res = orkg.resources.add(label="Coco")
        self.assertTrue(res.succeeded)
        label = "test"
        res = orkg.resources.update(id=res.content['id'], label=label)
        self.assertTrue(res.succeeded)
        res = orkg.resources.by_id(res.content['id'])
        self.assertTrue(res.succeeded)
        self.assertEqual(res.content['label'], label)
