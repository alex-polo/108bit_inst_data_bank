from dataclasses import dataclass


@dataclass
class CeleryConfig:
    logging_config: str
    broker: str
    backend: str


@dataclass
class DatabaseConfig:
    db_user: str
    db_pass: str
    db_host: str
    db_port: str
    db_name: str
