from __future__ import annotations

import logging

from artemis_common.consts import LOGSENE_KEY


class SyslogAdapter(logging.LoggerAdapter):
    def process(self, msg: str, kwargs: dict):
        extra = kwargs.setdefault('extra', {})
        extra[LOGSENE_KEY] = self.extra[LOGSENE_KEY]
        return msg, kwargs


def get_logger(name: str, token: str) -> SyslogAdapter:
    logger = logging.getLogger(name)
    return SyslogAdapter(
        logger,
        {LOGSENE_KEY: token},
    )
