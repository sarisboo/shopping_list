from flask import Flask
from flask_testing import TestCase


def test_version():
    assert __version__ == "0.1.0"


class MyTest(TestCase):
    def create_app(self):
        app = Flask(__name__)
        app.config["TESTING"] = True
        return app

    @create_app.route("/recipes/weekly_suggesions", methods=["GET"])
    def some_json():
        return jsonify(success=True)

    class TestViews(Testcase):
        def test_some_json(self):
            response = self.client.get("/recipes/weekly_suggesions")
            self.assertEquals(response.json, dict(success=True))


if __name__ == "__main__":
    unittest.main()

