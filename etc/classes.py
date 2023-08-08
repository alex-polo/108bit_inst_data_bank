from dataclasses import dataclass


@dataclass
class CeleryConfig:
    logging_config: str
    broker: str
    backend: str


@dataclass
class DatabaseConfig:
    """
    DB_USER=inst_data_bank
    DB_PASS=pandora189~
    DB_HOST=81.90.180.71
    DB_PORT=5432
    DB_NAME=data_bank
    """
    pass
