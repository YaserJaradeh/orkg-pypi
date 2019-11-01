from unittest import TestCase
from orkg import ORKG


class TestLiterals(TestCase):
    """
    Some test scenarios might need to be adjusted to the content of the running ORKG instance
    """
    orkg = ORKG()

    def test_by_id(self):
        res = self.orkg.literals.by_id('L1')
        self.assertTrue(res.succeeded)

    def test_get(self):
        res = self.orkg.literals.get_all()
        self.assertTrue(res.succeeded)

    def test_get_term(self):
        term = 'Python'
        res = self.orkg.literals.get_all(q=term)
        self.assertTrue(res.succeeded)

    def test_add(self):
        label = "ORKG rocks"
        res = self.orkg.literals.add(label=label)
        self.assertTrue(res.succeeded)
        self.assertEqual(res.content['label'], label)

    def test_update(self):
        res = self.orkg.literals.add(label="ORKG")
        self.assertTrue(res.succeeded)
        label = "Open Research Knowledge Graph"
        res = self.orkg.literals.update(id=res.content['id'], label=label)
        self.assertTrue(res.succeeded)
        res = self.orkg.literals.by_id(res.content['id'])
        self.assertTrue(res.succeeded)
        self.assertEqual(res.content['label'], label)
