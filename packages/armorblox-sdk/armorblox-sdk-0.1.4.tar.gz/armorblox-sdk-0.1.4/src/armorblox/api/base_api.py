# -*- coding: utf-8 -*-

import json
import requests

class BaseApi:
    PAGE_SIZE = 50

    def __init__(self, config):
        self._config = config

    @property
    def version(self):
        return 'v1beta1'

    def headers(self):
        return {
            'X-Ab-Authorization': self._config.api_key,
            'Content-Type': 'application/json',
            'User-Agent': 'Armorblox-Python-SDK/' + self._config.sdk_version
        }

    def endpoint(self, path: str, api_version: str = None) -> str:
        if api_version is None:
            api_version = self.version
        return self._config.base_api_url.format(api_version) + path

    def list_params(self):
        return {
            'page_size': self.PAGE_SIZE,
            'page_token': '0',
        }

    def list_resource(self, path: str, headers: dict = None,
                      params: dict = None, options: dict = None):
        """

        Args:
            path: str
            headers: dict
            params: dict
            options: dict

        Raises:
            Exception:
        """
        h = self.headers()
        if headers is not None:
            h.update(headers)
        p = self.list_params()
        if params is not None:
            p.update(params)
            # Cap page size to PAGE_SIZE value for optimal performance
            p["page_size"] = min(p["page_size"], self.PAGE_SIZE)
        if options is None:
            options = {}
        response = requests.get(self.endpoint(path, options.get('api_version')),
                                headers=h, params=p)
        if response.status_code == 200:
            return response.json(), None
        else:
            return None, response
    
    def get_resource(self, path: str, resource_id: str, headers: dict = None,
                     params: dict = None, options: dict = None):
        """

        Args:
            path: str
            resource_id: str
            headers: dict
            params: dict
            options: dict
        Raises:
            Exception:
        """
        h = self.headers()
        if headers is not None:
            h.update(headers)
        if options is None:
            options = {}

        url = self.endpoint(path, options.get('api_version'))
        # ':' indicates that this is a tenant-scoped call and not a resource-scoped one
        if resource_id.startswith(':'):
            url = f"{url.rstrip('/')}{resource_id}"
        else:
            url = f"{url}/{resource_id}"

        response = requests.get(url, headers=h, params=params)

        if response.status_code == 200:
            return response.json()
        else:
            return {}


    def update_resource(self, path: str, resource_id: str, headers: dict = None,
                     params: dict = None, options: dict = None, body: dict = None):
        """

        Args:
            path: str
            resource_id: str
            headers: dict
            params: dict
            options: dict
            body: dict

        Raises:
            Exception:
        """
        h = self.headers()
        if headers is not None:
            h.update(headers)
        if options is None:
            options = {}

        url = self.endpoint(path, options.get('api_version')) + f"/{resource_id}"
        response = requests.patch(url, headers=h, params=params, data=json.dumps(body))
        if response.status_code == 200:
            return response.json(), None
        else:
            return None, response