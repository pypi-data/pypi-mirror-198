"""Configuration for :mod:`pytest`."""
import os

import ioc
import pytest
import unimatrix.runtime
from unimatrix.lib.test import TEST_STAGE


@pytest.fixture(scope='session', autouse=True)
def setup_environment():
    """Setup the runtime test environment."""
    unimatrix.runtime.on.sync('boot')


@pytest.fixture(scope="function", autouse=True)
def clean_environment():
    """Ensure that each test runs in a clean environment."""
    unimatrix.runtime.on.sync('boot')

    # If we are running unit or integration tests, also inspect the etc/
    # folder for a mock inversion-of-control configuration file.
    if TEST_STAGE in ('unit', 'integration')\
    and os.path.exists('etc/ioc.testing.conf'):
        ioc.load_config('etc/ioc.testing.conf')

    # The actual test is executed after the yield statement.
    yield

    # Ensure that the inversion-of-control container is cleared prior to
    # each test. While it would be conveniant to have each test use a
    # default configuration, this will eventually cause erratic behavior so
    # we force tests to setup their own container using ioc.provide().
    unimatrix.runtime.on.sync('shutdown')
