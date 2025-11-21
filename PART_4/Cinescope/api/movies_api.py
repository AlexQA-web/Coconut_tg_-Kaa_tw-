from PART_4.Cinescope.custom_requester.custom_requester import CustomRequester
from PART_4.Cinescope.constants import API_BASE_URL, MOVIES_ENDPOINT
from urllib.parse import urlencode

class MoviesAPI(CustomRequester):

    def __init__(self, session):
        super().__init__(session=session, base_url=API_BASE_URL)

    def get_movies(self, filters: dict | None = None, expected_status=200):
        endpoint = MOVIES_ENDPOINT
        if filters:
            query = urlencode(filters, doseq=True)
            endpoint = f"{MOVIES_ENDPOINT}?{query}"

        return self.send_request(
            method="GET",
            endpoint=endpoint,
            expected_status=expected_status,
        )

    def get_movie_by_id(self, movie_id, expected_status=200):
        return self.send_request(
            method="GET",
            endpoint=f"{MOVIES_ENDPOINT}/{movie_id}",
            expected_status=expected_status,
        )

    def create_movie(self, movie_data, expected_status=201):
        return self.send_request(
            method="POST",
            endpoint=MOVIES_ENDPOINT,
            data=movie_data,
            expected_status=expected_status,
        )

    def update_movie(self, movie_id, movie_data, expected_status=200):
        return self.send_request(
            method="PATCH",
            endpoint=f"{MOVIES_ENDPOINT}/{movie_id}",
            data=movie_data,
            expected_status=expected_status,
        )

    def delete_movie(self, movie_id, expected_status=200):
        return self.send_request(
            method="DELETE",
            endpoint=f"{MOVIES_ENDPOINT}/{movie_id}",
            expected_status=expected_status,
        )
