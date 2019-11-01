from unittest import TestCase
from orkg import ORKG


class TestStats(TestCase):
    """
    Some test scenarios might need to be adjusted to the content of the running ORKG instance
    """
    orkg = ORKG()

    def test(self):
        res = self.orkg.stats.get()
        self.assertTrue(res.succeeded)
