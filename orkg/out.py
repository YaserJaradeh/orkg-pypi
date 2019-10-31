
class OrkgResponse(object):

    @property
    def succeeded(self):
        return str(self.status_code)[0] == '2'

    def __init__(self, response):
        self.status_code = response.status_code
        self.content = response.json()
        self.url = response.url
