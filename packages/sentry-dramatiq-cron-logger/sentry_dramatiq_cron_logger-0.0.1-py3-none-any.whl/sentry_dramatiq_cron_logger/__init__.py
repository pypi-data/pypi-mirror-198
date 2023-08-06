from typing import Optional, Set

import requests
from dramatiq.actor import Actor
from dramatiq.broker import Broker
from dramatiq.message import Message
from dramatiq.middleware import Middleware


class SentryCronMiddleware(Middleware):
    def __init__(
        self,
        *,
        sentry_dsn: Optional[str],
        organization: str,
        base_url: Optional[str] = None,
    ):
        self.base_url = base_url or "https://sentry.io/api/0/organizations"
        self.dsn = sentry_dsn
        self.organization = organization

    def _url(self, monitor_id: str, checkin_id: Optional[str] = None) -> str:
        base = f"{self.base_url}/{self.organization}/monitors/{monitor_id}/checkins/"
        if checkin_id:
            return base + f"{checkin_id}/"
        return base

    @property
    def _can_send_event(self) -> bool:
        return bool(self.dsn)

    def _update_monitor(self, monitor_id: str, status: Optional[str]):
        if not self._can_send_event:
            return
        headers = {"Authorization": f"DSN {self.dsn}"}
        json = {"status": status or "in_progress"}
        if status:
            return requests.put(
                self._url(monitor_id, "latest"), headers=headers, json=json
            )
        return requests.post(self._url(monitor_id), headers=headers, json=json)

    def _start_monitor(self, monitor_id: str):
        return self._update_monitor(monitor_id, None)

    def _end_monitor(self, monitor_id: str, status: str):
        return self._update_monitor(monitor_id, status)

    @property
    def actor_options(self) -> Set:
        return {"monitor_id"}

    @staticmethod
    def _get_monitor_id(broker: Broker, message: Message) -> Optional[str]:
        key = "monitor_id"
        actor: Actor = broker.get_actor(message.actor_name)
        return message.options.get(key) or actor.options.get(key)

    def before_process_message(self, broker: Broker, message: Message) -> None:
        monitor_id = self._get_monitor_id(broker, message)
        if not monitor_id:
            return
        self._start_monitor(monitor_id)

    def after_process_message(
        self, broker: Broker, message: Message, *, result=None, exception=None
    ) -> None:
        monitor_id = self._get_monitor_id(broker, message)
        if not monitor_id:
            return
        status = "error" if exception else "ok"
        self._end_monitor(monitor_id, status)
