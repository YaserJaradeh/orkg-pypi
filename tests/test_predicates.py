from unittest import TestCase
from orkg import ORKG


class TestPredicates(TestCase):
    """
    Some test scenarios might need to be adjusted to the content of the running ORKG instance
    """
    orkg = ORKG()

    def test_by_id(self):
        res = self.orkg.predicates.by_id('P1')
        self.assertTrue(res.succeeded)

    def test_get(self):
        res = self.orkg.predicates.get()
        self.assertTrue(res.succeeded)
        self.assertEqual(len(res.content), 10)

    def test_get_with_items(self):
        count = 30
        res = self.orkg.predicates.get(items=30)
        self.assertTrue(res.succeeded)
        self.assertEqual(len(res.content), 30)

    def test_add(self):
        label = "test predicate"
        res = self.orkg.predicates.add(label=label)
        self.assertTrue(res.succeeded)
        self.assertEqual(res.content['label'], label)

    def test_update(self):
        res = self.orkg.predicates.add(label="Coco predicate")
        self.assertTrue(res.succeeded)
        label = "Test predicate"
        res = self.orkg.predicates.update(id=res.content['id'], label=label)
        self.assertTrue(res.succeeded)
        res = self.orkg.predicates.by_id(res.content['id'])
        self.assertTrue(res.succeeded)
        self.assertEqual(res.content['label'], label)
