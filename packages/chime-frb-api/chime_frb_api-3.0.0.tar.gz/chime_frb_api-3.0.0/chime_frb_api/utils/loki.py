"""Loki handler."""

import requests
from logging_loki import LokiHandler

from chime_frb_api.configs import LOKI_URLS


def add_handler(logger, site):
    """Add Loki handler to logger."""
    try:
        loki_url = LOKI_URLS[site]
        loki_sc = requests.get(
            loki_url.replace("loki/api/v1/push", "ready")
        ).status_code
        if loki_sc == 200:
            loki_handler = LokiHandler(
                url=loki_url,
                tags={"site": site, "pipeline": ""},
                version="1"
                # TODO: pipeline from bucket -nope this is just a string.
            )
            logger.root.addHandler(loki_handler)
            logger.info("Loki: ✔️")
            logger.debug(f"Loki url: {loki_url}")
        else:
            logger.warning("Loki: ✖")
            logger.debug("Reason: Reachable, but not ready.")
    except Exception:
        logger.warning("Loki: ✖")
        logger.debug("Reason: Unable to connect.")
