class TestMoviesAPI:

    def test_create_movie(self, api_manager, movie_data):
        response = api_manager.movies_api.create_movie(movie_data)
        data = response.json()

        assert data["name"] == movie_data["name"]
        assert "id" in data

    def test_get_movie_by_id(self, api_manager, created_movie):
        movie_id, created_data, _ = created_movie

        response = api_manager.movies_api.get_movie_by_id(movie_id)
        data = response.json()

        assert data["id"] == movie_id
        assert data["name"] == created_data["name"]

    def test_update_movie(self, api_manager, created_movie):
        movie_id, _, _ = created_movie
        updated = {"name": "Updated name"}

        response = api_manager.movies_api.update_movie(movie_id, updated)
        data = response.json()

        assert data["name"] == "Updated name"

    def test_create_movie_without_required_field(self, api_manager, movie_data):
        bad_data = movie_data.copy()
        bad_data.pop("name")  # обязательное поле

        response = api_manager.movies_api.create_movie(
            bad_data,
            expected_status=400
        )

    def test_get_movies_with_filter_by_name(self, api_manager, created_movie):
        #TODO Как минимум 1 тест на проверку фильтров (для GET /movies)
        _, created_data, _ = created_movie

        response = api_manager.movies_api.get_movies(
            filters={"name": created_data["name"]}
        )
        data = response.json()
        movies = data["movies"]

        assert isinstance(movies, list)
        assert len(movies) > 0


class TestMoviesAuthNegative:

    def test_get_movies_unauthorized(self, unauthorized_api_manager):

        response = unauthorized_api_manager.movies_api.get_movies()  # без expected_status
        data = response.json()

        assert "movies" in data
        assert isinstance(data["movies"], list)

    def test_create_movie_unauthorized(self, unauthorized_api_manager, movie_data):

        response = unauthorized_api_manager.movies_api.create_movie(
            movie_data,
            expected_status=401
        )
        data = response.json()

    def test_create_movie_with_empty_name(self, api_manager, movie_data):
        bad_data = movie_data.copy()
        bad_data["name"] = ""

        response = api_manager.movies_api.create_movie(
            bad_data,
            expected_status=400,
        )
        data = response.json()

        assert "message" in data

    def test_create_movie_with_invalid_price_type(self, api_manager, movie_data):
        bad_data = movie_data.copy()
        bad_data["price"] = "not a number"

        response = api_manager.movies_api.create_movie(
            bad_data,
            expected_status=400,
        )
        data = response.json()

        assert "message" in data


    def test_get_movie_not_found(self, api_manager):
        non_existing_id = 999999

        response = api_manager.movies_api.get_movie_by_id(
            non_existing_id,
            expected_status=404,
        )
        data = response.json()

        assert data.get("statusCode") == 404