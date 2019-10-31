from .utils import NamespacedClient, query_params, dict_to_url_params


class StatsClient(NamespacedClient):

    def get(self):
        self.client.backend._append_slash = True
        response = self.client.backend.stats.GET()
        return response.status_code, response.json()
