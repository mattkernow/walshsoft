from django.test import TestCase


class TestIntegrationPostcodeApiViews(TestCase):

    def test_postcode_view_returns_geojson(self):
        # Act
        response = self.client.get('/postcode/eh111ah')

        # Assert
        self.assertEquals(response.status_code, 200)

    def test_postcode_view_not_found(self):
        # Act
        response = self.client.get('/postcode/notapostcode123')

        # Assert
        self.assertEquals(response.status_code, 404)
