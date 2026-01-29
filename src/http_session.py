"""
Shared HTTP session management for efficient connection pooling.
"""
import requests
from typing import Optional
import logging

logger = logging.getLogger(__name__)

# Global shared session instance
_shared_session: Optional[requests.Session] = None


def get_shared_session() -> requests.Session:
    """
    Get or create a shared requests Session with connection pooling.

    Using a shared session provides:
    - Connection pooling (reuses TCP connections)
    - Automatic retry logic
    - Session-level headers and configuration
    - Better performance for multiple requests

    Returns:
        Shared requests.Session instance
    """
    global _shared_session

    if _shared_session is None:
        logger.info("Creating shared HTTP session with connection pooling")
        _shared_session = requests.Session()

        # Set default headers
        _shared_session.headers.update({
            'User-Agent': 'CBB-Predictor/1.0 (Basketball Analytics)',
            'Accept': 'application/json',
            'Accept-Encoding': 'gzip, deflate'
        })

        # Configure connection pooling
        adapter = requests.adapters.HTTPAdapter(
            pool_connections=10,  # Number of connection pools
            pool_maxsize=20,      # Max connections per pool
            max_retries=3,        # Retry failed requests
            pool_block=False      # Don't block when pool is full
        )

        # Mount adapter for both HTTP and HTTPS
        _shared_session.mount('http://', adapter)
        _shared_session.mount('https://', adapter)

    return _shared_session


def close_shared_session():
    """
    Close the shared session and clean up resources.
    Should be called at application shutdown.
    """
    global _shared_session

    if _shared_session is not None:
        logger.info("Closing shared HTTP session")
        _shared_session.close()
        _shared_session = None


def reset_shared_session():
    """
    Reset the shared session (useful for testing or error recovery).
    """
    close_shared_session()
    # Next call to get_shared_session() will create a new one
