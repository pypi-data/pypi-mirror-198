import json
import pkgutil
from typing import Any
from aiohttp import ClientSession
from yarl import URL

from PyMyGekko.resources import Blind


class PyMyGekkoApiClient:
    def __init__(
        self,
        username: str,
        apiKey: str,
        gekkoId: str,
        session: ClientSession,
        demo_mode: bool = False,
        scheme: str = "https",
        host: str = "live.my-gekko.com",
        port: int = None,
    ) -> None:
        self._url = URL.build(scheme=scheme, host=host, port=port)
        self._authentication_params = {
            "username": username,
            "key": apiKey,
            "gekkoid": gekkoId,
        }
        self._session = session
        self._demo_mode = demo_mode
        self._resources: Any = None
        self._status: Any = None

    async def try_connect(self) -> int:
        if self._demo_mode:
            return 200
        else:
            async with self._session.get(
                self._url.with_path("/api/v1/var"), params=self._authentication_params
            ) as resp:
                return resp.status

    async def read_data(self) -> None:
        if self._demo_mode:
            var_demo_data = pkgutil.get_data(
                __name__, "PyMyGekko/api_var_demo_data.json"
            )
            self._resources = json.loads(var_demo_data)
            status_demo_data = pkgutil.get_data(
                __name__, "PyMyGekko/api_var_status_demo_data.json"
            )
            self._status = json.loads(status_demo_data)
            return
        else:
            async with self._session.get(
                self._url.with_path("/api/v1/var"),
                params=self._authentication_params,
            ) as resp:
                self._resources = await resp.json(content_type="text/plain")
            async with self._session.get(
                self._url.with_path("/api/v1/var/status"),
                params=self._authentication_params,
            ) as resp:
                self._status = await resp.json(content_type="text/plain")

    def get_globals_network(self):
        if self._status == None:
            return None

        result = {}
        if self._status["globals"] and self._status["globals"]["network"]:
            network_data = self._status["globals"]["network"]
            for key in network_data:
                result[key] = network_data[key]["value"]

        return result

    def get_blinds(self) -> list[Blind] | None:
        if self._resources == None:
            return None

        result: list[Blind] = []
        if self._resources["blinds"]:
            blinds = self._resources["blinds"]
            for key in blinds:
                if key.startswith("item"):
                    result.append(Blind(key, blinds[key]["name"]))

        return result
