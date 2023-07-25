from flask import Blueprint, Flask

from src.blueprints import gumballs
from src.config.configs import Config, get_config

blueprints: list[Blueprint] = [
    gumballs,
]


def create_app(app_config: str = "dev") -> Flask:
    app = Flask(__name__)
    chosen_config: type[Config] = get_config(app_config)
    app.config.from_object(chosen_config)

    for blueprint in blueprints:
        app.register_blueprint(blueprint)

    return app
