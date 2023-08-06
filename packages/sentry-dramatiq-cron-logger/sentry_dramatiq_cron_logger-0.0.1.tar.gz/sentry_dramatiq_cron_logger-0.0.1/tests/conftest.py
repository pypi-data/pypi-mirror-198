import dramatiq
import pytest
from dramatiq import Worker
from dramatiq.brokers.stub import StubBroker
from sentry_dramatiq_cron_logger import SentryCronMiddleware


@pytest.fixture
def middleware():
    md = SentryCronMiddleware(
        sentry_dsn="some dsn", organization="does-not-exist", base_url="http://test"
    )

    def fake_update_monitor(monitor_id: str, status):
        print("_update_monitor", monitor_id, status)
        return {"monitor_id": monitor_id, "status": status}

    md._update_monitor = fake_update_monitor
    return md


@pytest.fixture()
def stub_broker_without_middleware():
    broker = StubBroker()
    broker.emit_after("process_boot")
    dramatiq.set_broker(broker)
    yield broker
    broker.flush_all()
    broker.close()


@pytest.fixture()
def stub_broker(stub_broker_without_middleware, middleware):
    broker = StubBroker()
    broker.add_middleware(middleware)
    broker.emit_after("process_boot")
    dramatiq.set_broker(broker)
    yield broker
    broker.flush_all()
    broker.close()


@pytest.fixture()
def stub_worker(stub_broker):
    worker = Worker(stub_broker, worker_timeout=100, worker_threads=32)
    worker.start()
    yield worker
    worker.stop()


@pytest.fixture
def middleware_without_dsn():
    return SentryCronMiddleware(sentry_dsn=None, organization="does-not-exist")
