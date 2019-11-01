
class OrkgResponse(object):

    @property
    def succeeded(self):
        return str(self.status_code)[0] == '2'

    def __init__(self, response):
        self.status_code = response.status_code
        self.content = response.json() if len(response.content) > 0 else response.content
        self.url = response.url

    def __repr__(self):
        return "%s %s" % ("(Success)" if self.succeeded else "(Fail)", self.content)

    def __str__(self):
        return self.content
