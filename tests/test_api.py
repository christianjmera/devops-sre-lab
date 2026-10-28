import json
import threading
import unittest
from http.server import HTTPServer
from urllib.request import urlopen
from urllib.error import HTTPError

from app.main import HealthHandler


class TestHealthAPI(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server = HTTPServer(
            ("127.0.0.1", 0),
            HealthHandler,
        )
        cls.port = cls.server.server_address[1]
        cls.thread = threading.Thread(
            target=cls.server.serve_forever,
            daemon=True,
        )
        cls.thread.start()

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()
        cls.server.server_close()
        cls.thread.join()

    def test_health_returns_200_and_json(self):
        with urlopen(
            f"http://127.0.0.1:{self.port}/health"
        ) as response:
            self.assertEqual(response.status, 200)
            self.assertEqual(
                response.headers.get_content_type(),
                "application/json",
            )
            body = json.load(response)

        self.assertEqual(body["status"], "healthy")
        self.assertEqual(
            body["service"],
            "devops-sre-lab",
        )

    def test_unknown_path_returns_404(self):
        with self.assertRaises(HTTPError) as error:
            urlopen(f"http://127.0.0.1:{self.port}/")

        self.assertEqual(error.exception.code, 404)


if __name__ == "__main__":
    unittest.main()
