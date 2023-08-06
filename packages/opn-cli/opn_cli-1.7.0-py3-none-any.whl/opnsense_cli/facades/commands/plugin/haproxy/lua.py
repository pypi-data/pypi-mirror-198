from opnsense_cli.facades.commands.plugin.haproxy.base import HaproxyFacade
from opnsense_cli.api.plugin.haproxy import Settings, Service


class HaproxyLuaFacade(HaproxyFacade):
    jsonpath_base = '$.haproxy.luas.lua'
    uuid_resolver_map = {
    }

    def __init__(self, settings_api: Settings, service_api: Service):
        super().__init__()
        self._complete_model_data_cache = None
        self._settings_api = settings_api
        self._service_api = service_api

    def list_luas(self):
        return self._get_luas_list()

    def show_lua(self, uuid):
        luas = self._get_luas_list()
        lua = next((item for item in luas if item["uuid"] == uuid), {})
        return lua

    def _get_luas_list(self):
        return self._api_mutable_model_get(self._complete_model_data, self.jsonpath_base, self.uuid_resolver_map)

    def create_lua(self, json_payload: dict):
        result = self._settings_api.addLua(json=json_payload)
        self._apply(result)
        return result

    def update_lua(self, uuid, json_payload: dict):
        result = self._settings_api.setLua(uuid, json=json_payload)
        self._apply(result)
        return result

    def delete_lua(self, uuid):
        result = self._settings_api.delLua(uuid)
        self._apply(result)
        return result
