from django.test import TestCase
import requests_mock


class TestPostcodeApiViews(TestCase):

    @requests_mock.Mocker()
    def test_postcode_view_returns_geojson(self, mock_request):
        # Arrange
        response_as_dict = {'result': {'easting': 12345, 'northing': 54321}}
        mock_request.get('https://api.postcodes.io/postcodes/eh111ah', status_code=200, json=response_as_dict)

        # Act
        response = self.client.get('/postcode/eh111ah')

        # Assert
        self.assertEquals(response.status_code, 200)

    @requests_mock.Mocker()
    def test_postcode_view_not_found(self, mock_request):
        # Arrange
        mock_request.get('https://api.postcodes.io/postcodes/eh111ahhh', status_code=404)

        # Act
        response = self.client.get('/postcode/eh111ahhh')

        # Assert
        self.assertEquals(response.status_code, 404)

    @requests_mock.Mocker()
    def test_postcode_view_server_error(self, mock_request):
        # Arrange
        mock_request.get('https://api.postcodes.io/postcodes/eh111ah', status_code=500)

        # Act
        response = self.client.get('/postcode/eh111ah')

        # Assert
        self.assertEquals(response.status_code, 500)
