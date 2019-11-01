from unittest import TestCase
from orkg import ORKG


class TestClasses(TestCase):
    """
    Some test scenarios might need to be adjusted to the content of the running ORKG instance
    """
    orkg = ORKG()

    def test_by_id(self):
        res = self.orkg.classes.by_id('Paper')
        self.assertTrue(res.succeeded)

    def test_get(self):
        res = self.orkg.classes.get_all()
        self.assertTrue(res.succeeded)

    def test_get_with_term(self):
        term = 'Paper'
        res = self.orkg.classes.get_all(q=term)
        self.assertTrue(res.succeeded)

    def test_get_resources_by_class(self):
        term = 'Paper'
        res = self.orkg.classes.get_resource_by_class(class_id=term)
        self.assertTrue(res.succeeded)

    def test_get_resources_by_class_with_items(self):
        term = 'Paper'
        res = self.orkg.classes.get_resource_by_class(class_id=term, items=30)
        self.assertTrue(res.succeeded)
        self.assertEqual(len(res.content), 30)

    def test_add(self):
        label = "Class Z"
        res = self.orkg.classes.add(label=label)
        self.assertTrue(res.succeeded)
        self.assertEqual(res.content['label'], label)

    def test_update(self):
        res = self.orkg.classes.add(label="Class A")
        self.assertTrue(res.succeeded)
        label = "Class B"
        res = self.orkg.classes.update(id=res.content['id'], label=label)
        self.assertTrue(res.succeeded)
        res = self.orkg.classes.by_id(res.content['id'])
        self.assertTrue(res.succeeded)
        self.assertEqual(res.content['label'], label)
