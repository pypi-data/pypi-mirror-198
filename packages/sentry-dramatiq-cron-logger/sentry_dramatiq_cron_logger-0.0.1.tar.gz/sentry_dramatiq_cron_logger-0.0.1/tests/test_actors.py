import dramatiq
import pytest


def test_can_post_event_for_middleware(middleware):
    assert middleware._can_send_event, "we can post using this middleware"


def test_can_post_event_for_no_dsn_middleware(middleware_without_dsn):
    assert not middleware_without_dsn._can_send_event, "cannot send event without dsn"


def test_broker_gets_sentry_middleware(stub_broker, middleware):
    broker_middleware = stub_broker.middleware
    assert broker_middleware
    assert middleware.__class__.__name__ in [
        m.__class__.__name__ for m in broker_middleware
    ]


def test_broker_without_monitor_id_raises(stub_broker_without_middleware):
    with pytest.raises(ValueError):

        @dramatiq.actor(monitor_id="foobar")
        def add():
            return 2 + 2


def test_broker_with_middleware_does_not_raise(stub_broker):
    @dramatiq.actor(monitor_id="foobar")
    def add():
        return 2 + 2

    assert add.options.get("monitor_id") == "foobar"
