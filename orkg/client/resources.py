from .utils import NamespacedClient, query_params, dict_to_url_params


class ResourcesClient(NamespacedClient):

    @query_params("q", "exact", "page", "items", "sortBy", "exclude")
    def get_all(self, params=None):
        if len(params) > 0:
            self.client.backend._append_slash = False
            response = self.client.backend.resources.GET(dict_to_url_params(params))
        else:
            self.client.backend._append_slash = True
            response = self.client.backend.resources.GET()
        return response.status_code, response.json()

    @query_params("id", "label", "classes")
    def add(self, params=None):
        if len(params) == 0:
            raise ValueError("at least label should be provided")
        else:
            self.client.backend._append_slash = True
            response = self.client.backend.resources.POST(json=params)
        return response.status_code, response.json()

    @query_params("label", "classes")
    def update(self, id, params=None):
        if len(params) == 0:
            raise ValueError("at least label should be provided")
        else:
            if not self.exists(id):
                raise ValueError("the provided id is not in the graph")
            self.client.backend._append_slash = True
            response = self.client.backend.resources(id).PUT(json=params)
        return response.status_code, response.json()

    def exists(self, id):
        return self.client.backend.resources(id).GET().status_code == 200

