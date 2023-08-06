from __future__ import annotations

import logging

from artemis_common.config import config
from artemis_common.consts import Tokens


class SyslogAdapter(logging.LoggerAdapter):
    def process(self, msg: str, kwargs: dict):
        extra = kwargs.setdefault('extra', {})
        extra[Tokens.logsene] = config.environment.logsene_token_artemis.get_secret_value()
        return msg, kwargs


def get_logger(name: str):
    logger = logging.getLogger(name)
    return SyslogAdapter(logger, {})
