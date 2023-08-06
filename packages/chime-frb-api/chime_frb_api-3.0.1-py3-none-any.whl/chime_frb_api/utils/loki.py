"""Loki handler."""

from logging import Logger

import requests
from logging_loki import LokiHandler

from chime_frb_api.configs import LOKI_URLS


def add_handler(logger: Logger, site: str, pipeline: str) -> None:
    """Add Loki handler to logger."""
    try:
        loki_url = LOKI_URLS[site]
        loki_sc = requests.get(
            loki_url.replace("loki/api/v1/push", "ready")
        ).status_code
        if loki_sc == 200:
            loki_handler = LokiHandler(
                url=loki_url, tags={"site": site, "pipeline": pipeline}, version="1"
            )
            logger.root.addHandler(loki_handler)
            logger.info("Loki Logs: ✔️")
            logger.debug(f"Loki URL: {loki_url}")
        else:
            raise AttributeError("Loki not ready.")
    except Exception as error:
        logger.warning("Loki Logs: ✖")
        logger.debug(error)
