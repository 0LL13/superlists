import logging


LOGGER = logging.getLogger(__name__)


# @pytest.fixture(scope="function")
def returns_None_if_no_such_token_fixture():
    LOGGER.info("Setting Up test_returns_None_if_no_such_token Fixture ...")
    yield
    LOGGER.info("Tearing Down test_returns_None_if_no_such_token Fixture ...")
