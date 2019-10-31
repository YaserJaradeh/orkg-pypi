from orkg.utils import NamespacedClient, query_params, dict_to_url_params
from orkg.out import OrkgResponse


class ClassesClient(NamespacedClient):

    def by_id(self, id):
        self.client.backend._append_slash = True
        response = self.client.backend.classes(id).GET()
        return OrkgResponse(response)

    @query_params("q", "exact")
    def get(self, params=None):
        if len(params) > 0:
            self.client.backend._append_slash = False
            response = self.client.backend.classes.GET(dict_to_url_params(params))
        else:
            self.client.backend._append_slash = True
            response = self.client.backend.classes.GET()
        return OrkgResponse(response)

    @query_params("page", "items", "sortBy", "desc")
    def get_resource_by_class(self, class_name, params=None):
        if len(params) > 0:
            self.client.backend._append_slash = False
            response = self.client.backend.classes(class_name).resources.GET(dict_to_url_params(params))
        else:
            self.client.backend._append_slash = True
            response = self.client.backend.classes(class_name).resources.GET()
        return OrkgResponse(response)

    @query_params("id", "label", "uri")
    def add(self, params=None):
        if len(params) == 0:
            raise ValueError("at least label should be provided")
        else:
            self.client.backend._append_slash = True
            response = self.client.backend.classes.POST(json=params)
        return OrkgResponse(response)

    @query_params("label", "uri")
    def update(self, id, params=None):
        if len(params) == 0:
            raise ValueError("at least label should be provided")
        else:
            if not self.exists(id):
                raise ValueError("the provided id is not in the graph")
            self.client.backend._append_slash = True
            response = self.client.backend.classes(id).PUT(json=params)
        return OrkgResponse(response)

    def exists(self, id):
        return self.by_id(id)[0] == 200

