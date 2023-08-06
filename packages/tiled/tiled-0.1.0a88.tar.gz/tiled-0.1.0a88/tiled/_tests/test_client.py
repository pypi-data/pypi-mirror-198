import httpx

from ..adapters.mapping import MapAdapter
from ..client import Context, from_context
from ..server.app import build_app
from .utils import fail_with_status_code

tree = MapAdapter({})


def test_configurable_timeout():
    with Context.from_app(build_app(tree), timeout=httpx.Timeout(17)) as context:
        assert context.http_client.timeout.connect == 17
        assert context.http_client.timeout.read == 17


def test_client_version_check():
    with Context.from_app(build_app(tree)) as context:
        client = from_context(context)

        # Too-old user agent should generate a 400.
        context.http_client.headers["user-agent"] = "python-tiled/0.1.0a77"
        with fail_with_status_code(400):
            list(client)

        # Gibberish user agent should generate a 400.
        context.http_client.headers["user-agent"] = "python-tiled/gibberish"
        with fail_with_status_code(400):
            list(client)
