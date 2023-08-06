from __future__ import annotations

from enum import Enum
from pydantic import BaseSettings


class Environment:
    KEY = 'ARTEMIS_ENV'
    DEV = DEFAULT = 'dev'
    PROD = 'prod'


class Tokens(str, Enum):
    logsene = 'logsene-app-token'


class ArtemisEnvironment(BaseSettings):
    artemis_env: str = 'dev'


artemis_env = ArtemisEnvironment().artemis_env
