from graphene.test import Client
import unittest
from snapshottest import TestCase
from startwars_movies.schema import schema


class QueryTestCase(TestCase):
    def test_api_me(self):
        """Testing the API for /me"""
        client = Client(schema)
        self.assertMatchSnapshot(client.execute('''{ allPlanets }'''))


if __name__ == "__main__":
    unittest.main()
