import hammock
from .resources import ResourcesClient
from .predicates import PredicatesClient
from .classes import ClassesClient
from .literals import LiteralsClient
from .stats import StatsClient
from .statements import StatementsClient
from .papers import PapersClient


class ORKG(object):

    def __init__(self, host=None, **kwargs):
        if host is not None and not host.startswith('http'):
            raise ValueError('host must begin with http or https')
        self.host = host if host is not None else 'http://127.0.0.1:8000'
        self.backend = hammock.Hammock(self.host).api
        self.resources = ResourcesClient(self)
        self.predicates = PredicatesClient(self)
        self.classes = ClassesClient(self)
        self.literals = LiteralsClient(self)
        self.stats = StatsClient(self)
        self.statements = StatementsClient(self)
        self.papers = PapersClient(self)

    def ping(self):
        pass  # TODO: see how to ping ORKG host to know if it is alive
