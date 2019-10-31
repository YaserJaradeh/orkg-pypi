from orkg.utils import NamespacedClient, query_params, dict_to_url_params
from orkg.out import OrkgResponse


class ResourcesClient(NamespacedClient):

    def by_id(self, id):
        self.client.backend._append_slash = True
        response = self.client.backend.resources(id).GET()
        return OrkgResponse(response)

    @query_params("q", "exact", "page", "items", "sortBy", "exclude", "desc")
    def get(self, params=None):
        if len(params) > 0:
            self.client.backend._append_slash = False
            response = self.client.backend.resources.GET(dict_to_url_params(params))
        else:
            self.client.backend._append_slash = True
            response = self.client.backend.resources.GET()
        return OrkgResponse(response)

    @query_params("id", "label", "classes")
    def add(self, params=None):
        if len(params) == 0:
            raise ValueError("at least label should be provided")
        else:
            self.client.backend._append_slash = True
            response = self.client.backend.resources.POST(json=params)
        return OrkgResponse(response)

    @query_params("label", "classes")
    def update(self, id, params=None):
        if len(params) == 0:
            raise ValueError("at least label should be provided")
        else:
            if not self.exists(id):
                raise ValueError("the provided id is not in the graph")
            self.client.backend._append_slash = True
            response = self.client.backend.resources(id).PUT(json=params)
        return OrkgResponse(response)

    def exists(self, id):
        return self.by_id(id)[0] == 200

