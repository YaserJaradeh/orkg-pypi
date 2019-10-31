import hammock
from .resources import ResourcesClient
from .predicates import PredicatesClient
from .classes import ClassesClient
from .literals import LiteralsClient


class ORKG(object):

    def __init__(self, host=None, **kwargs):
        if host is not None and not host.startswith('http'):
            raise ValueError('host must begin with http or https')
        self.host = host if host is not None else 'http://127.0.0.1:8000'
        self.backend: hammock.Hammock = hammock.Hammock(self.host).api
        self.resources = ResourcesClient(self)
        self.predicates = PredicatesClient(self)
        self.classes = ClassesClient(self)
        self.literals = LiteralsClient(self)
