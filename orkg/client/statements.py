from orkg.utils import NamespacedClient, query_params, dict_to_url_params
from orkg.out import OrkgResponse


class StatementsClient(NamespacedClient):

    def by_id(self, id):
        self.client.backend._append_slash = True
        response = self.client.backend.statements(id).GET()
        return OrkgResponse(response)

    @query_params("page", "items", "sortBy", "desc")
    def get(self, params=None):
        if len(params) > 0:
            self.client.backend._append_slash = False
            response = self.client.backend.statements.GET(dict_to_url_params(params))
        else:
            self.client.backend._append_slash = True
            response = self.client.backend.statements.GET()
        return OrkgResponse(response)

    @query_params("page", "items", "sortBy", "desc")
    def get_by_subject(self, subject_id, params=None):
        if len(params) > 0:
            self.client.backend._append_slash = False
            response = self.client.backend.statements.subject(subject_id).GET(dict_to_url_params(params))
        else:
            self.client.backend._append_slash = True
            response = self.client.backend.statements.subject(subject_id).GET()
        return OrkgResponse(response)

    @query_params("page", "items", "sortBy", "desc")
    def get_by_predicate(self, predicate_id, params=None):
        if len(params) > 0:
            self.client.backend._append_slash = False
            response = self.client.backend.statements.predicate(predicate_id).GET(dict_to_url_params(params))
        else:
            self.client.backend._append_slash = True
            response = self.client.backend.statements.predicate(predicate_id).GET()
        return OrkgResponse(response)

    @query_params("page", "items", "sortBy", "desc")
    def get_by_object(self, object_id, params=None):
        if len(params) > 0:
            self.client.backend._append_slash = False
            response = self.client.backend.statements.object(object_id).GET(dict_to_url_params(params))
        else:
            self.client.backend._append_slash = True
            response = self.client.backend.statements.object(object_id).GET()
        return OrkgResponse(response)

    @query_params("subject_id", "predicate_id", "object")
    def add(self, params=None):
        if len(params) == 0:
            raise ValueError("all parameters must be provided")
        else:
            self.client.backend._append_slash = True
            response = self.client.backend.statements.POST(json=params)
        return OrkgResponse(response)

    @query_params("subject_id", "predicate_id", "object_id")
    def update(self, id, params=None):
        if len(params) == 0:
            raise ValueError("at least one parameter must be provided")
        else:
            if not self.exists(id):
                raise ValueError("the provided id is not in the graph")
            self.client.backend._append_slash = True
            response = self.client.backend.statements(id).PUT(json=params)
        return OrkgResponse(response)

    def exists(self, id):
        return self.by_id(id)[0] == 200
