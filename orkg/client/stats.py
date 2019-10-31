from orkg.utils import NamespacedClient
from orkg.out import OrkgResponse


class StatsClient(NamespacedClient):

    def get(self):
        self.client.backend._append_slash = True
        response = self.client.backend.stats.GET()
        return OrkgResponse(response)
