from unittest import TestCase
from orkg import ORKG


class TestStatements(TestCase):
    """
    Some test scenarios might need to be adjusted to the content of the running ORKG instance
    """
    orkg = ORKG()

    def test_by_id(self):
        res = self.orkg.statements.by_id('S1')
        self.assertTrue(res.succeeded)

    def test_get(self):
        res = self.orkg.statements.get()
        self.assertTrue(res.succeeded)
        self.assertEqual(len(res.content), 10)

    def test_get_with_items(self):
        count = 30
        res = self.orkg.statements.get(items=30)
        self.assertTrue(res.succeeded)
        self.assertEqual(len(res.content), 30)

    def test_add(self):
        subject = self.orkg.resources.add(label="ORKG Subject").content['id']
        predicate = self.orkg.predicates.add(label="ORKG Predicate").content['id']
        object = self.orkg.literals.add(label="ORKG Object").content['id']
        res = self.orkg.statements.add(subject_id=subject, predicate_id=predicate, object_id=object)
        self.assertTrue(res.succeeded)

    def test_update(self):
        st_id = 'S1'
        new_p_id = 'P1'
        res = self.orkg.statements.update(id=st_id, predicate_id=new_p_id)
        self.assertTrue(res.succeeded)
        res = self.orkg.statements.by_id(st_id)
        self.assertTrue(res.succeeded)
        self.assertEqual(res.content['predicate']['id'], new_p_id)

    def test_exists(self):
        found = self.orkg.statements.exists(id='S1')
        self.assertTrue(found)

    def test_not_exists(self):
        found = self.orkg.statements.exists(id='SS1')
        self.assertFalse(found)

    def test_delete(self):
        subject = self.orkg.resources.add(label="ORKG Subject 1").content['id']
        predicate = self.orkg.predicates.add(label="ORKG Predicate 1").content['id']
        object = self.orkg.literals.add(label="ORKG Object 1").content['id']
        res = self.orkg.statements.add(subject_id=subject, predicate_id=predicate, object_id=object)
        st_id = res.content['id']
        self.assertTrue(res.succeeded)
        res = self.orkg.statements.delete(id=st_id)
        self.assertTrue(res.succeeded)
        found = self.orkg.statements.exists(id=st_id)
        self.assertFalse(found)
