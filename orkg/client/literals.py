from orkg.utils import NamespacedClient, query_params, dict_to_url_params
from orkg.out import OrkgResponse


class LiteralsClient(NamespacedClient):

    def by_id(self, id):
        self.client.backend._append_slash = True
        response = self.client.backend.literals(id).GET()
        return OrkgResponse(response)

    @query_params("q", "exact")
    def get(self, params=None):
        if len(params) > 0:
            self.client.backend._append_slash = False
            response = self.client.backend.literals.GET(dict_to_url_params(params))
        else:
            self.client.backend._append_slash = True
            response = self.client.backend.literals.GET()
        return OrkgResponse(response)

    @query_params("id", "label")
    def add(self, params=None):
        if len(params) == 0:
            raise ValueError("at least label must be provided")
        else:
            self.client.backend._append_slash = True
            response = self.client.backend.literals.POST(json=params)
        return OrkgResponse(response)

    @query_params("label")
    def update(self, id, params=None):
        if len(params) == 0:
            raise ValueError("label must be provided")
        else:
            if not self.exists(id):
                raise ValueError("the provided id is not in the graph")
            self.client.backend._append_slash = True
            response = self.client.backend.literals(id).PUT(json=params)
        return OrkgResponse(response)

    def exists(self, id):
        return self.by_id(id)[0] == 200
