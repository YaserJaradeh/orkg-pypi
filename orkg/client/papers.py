from orkg.utils import NamespacedClient, query_params, dict_to_url_params
from orkg.out import OrkgResponse


class PapersClient(NamespacedClient):

    def add(self, params=None):
        """
        Create a new paper in the ORKG instance
        :param params: paper Object
        :return: an OrkgResponse object containing the newly created paper ressource
        """
        self.client.backend._append_slash = True
        response = self.client.backend.papers.POST(json=params)
        return OrkgResponse(response)

