class Config:
    DEBUG: bool = False
    TESTING: bool = False


class DevConfig(Config):
    DEBUG: bool = True


config_map: dict[str, type[Config]] = {"dev": DevConfig}


def get_config(config_name: str) -> type[Config]:
    return config_map[config_name]
