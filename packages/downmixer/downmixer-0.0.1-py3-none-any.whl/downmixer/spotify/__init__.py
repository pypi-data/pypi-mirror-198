"""Wrapper/helper for the [spotipy](https://github.com/spotipy-dev/spotipy) package to make use of Downmixer's
`library` paackage and facilitate calls with pagination."""

import logging
from typing import Optional

from downmixer.spotify.client import SpotifyClient

logger = logging.getLogger("downmixer").getChild(__name__)


class Spotify:
    """Holds info about the Spotify connection like scope, login/authorixation and a SpotifyClient instance."""

    def __init__(self):
        self._spotipy_client: Optional[SpotifyClient] = None

    def login(self):
        scope = "user-library-read,playlist-read-private,playlist-read-collaborative"
        logger.debug("Creating SpotifyClient, asking user to log in...")
        self._spotipy_client = SpotifyClient(scope)
        logger.info("Creaeted SpotifyClient")
