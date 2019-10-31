import hammock

class ORKG(object):

    def __init__(self, host=None, **kwargs):
        if host is not None and not host.startswith('http'):
            raise ValueError('host must begin with http or https')
        self.host = host if host is not None else 'http://127.0.0.1:8000'
        self.backend = hammock.Hammock(self.host)

    def check_connection(self):
        return self.backend.api.resources('R1').GET().json()


if __name__ == '__main__':
    client = ORKG()
    print(client.check_connection())