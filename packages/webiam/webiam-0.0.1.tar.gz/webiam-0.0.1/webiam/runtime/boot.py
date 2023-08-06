# pylint: skip-file
"""Provides functions to execute on application startup and shutdown.

The :func:`boot()` function is invoked *once* when the application is started.
It is generally used to set up the inversion-of-control container for an
application.
"""
import ioc
import unimatrix.runtime


async def boot():
    """Invoked when the application starts."""
    pass


async def shutdown():
    """Invoked when the application gracefully terminates."""
    pass
