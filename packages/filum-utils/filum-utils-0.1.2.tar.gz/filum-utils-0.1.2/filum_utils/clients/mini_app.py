from typing import Dict, Any, List

from filum_utils.clients.common import BaseClient
from filum_utils.config import config


class InstalledMiniAppsClient(BaseClient):
    def __init__(self):
        super().__init__(
            base_url=config.APPSTORE_BASE_URL,
            username=config.APPSTORE_USERNAME,
            password=config.APPSTORE_PASSWORD
        )

    def get_installed_mini_apps(self, mini_app_ids: List[int] = None, page: int = 0, size: int = 100):
        data = self._request(
            method="GET",
            endpoint="/internal/installed-mini-apps",
            params={
                "page": page,
                "size": size,
                "mini_app_ids": mini_app_ids
            }
        )

        return data.get("items") or []


class InstalledMiniAppClient(BaseClient):
    def __init__(self, installed_mini_app_id: int = None, installed_mini_app: Dict[str, Any] = None):
        super().__init__(
            base_url=config.APPSTORE_BASE_URL,
            username=config.APPSTORE_USERNAME,
            password=config.APPSTORE_PASSWORD
        )

        if installed_mini_app:
            self.installed_mini_app = installed_mini_app
        else:
            self.installed_mini_app = self._request(
                method="GET",
                endpoint=f"/internal/installed-mini-app/{installed_mini_app_id}"
            )

    def update_installed_mini_app_data(self, updated_data: Dict[str, Any]):
        self.installed_mini_app = self._request(
            method="PUT",
            endpoint=f"/internal/installed-mini-app/{self.installed_mini_app['id']}/data",
            data=updated_data
        )
