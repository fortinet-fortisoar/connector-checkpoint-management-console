""" Copyright start
  Copyright (C) 2008 - 2023 Fortinet Inc.
  All rights reserved.
  FORTINET CONFIDENTIAL & FORTINET PROPRIETARY SOURCE CODE
  Copyright end """

from requests import request, exceptions as req_exceptions
from connectors.core.connector import get_logger, ConnectorError
from connectors.core.utils import update_connnector_config
from datetime import datetime, timedelta


logger = get_logger("checkpoint-management-console")


class Checkpoint:
    def __init__(self, config, connector_info, *args, **kwargs):
        server_url = config.get("server_url")
        if not server_url.startswith('https://') and not server_url.startswith('http://'):
            server_url = "https://"+server_url
        if server_url.endswith("/"):
            server_url = server_url[:-1]
        self.url = server_url + "/web_api"
        self.username = config.get("username")
        self.password = config.get("password")
        self.api_key = config.get("api-key")
        self.verify_ssl = config.get("verify_ssl")
        self.token = self.get_token(config, connector_info, **kwargs)

    def get_token(self, config, connector_info, **kwargs):
        token = config.get("token")
        expiry_in = config.get("expiry_in")
        check_health = kwargs.get("check_health")
        if not check_health and token and expiry_in and datetime.fromtimestamp(int(expiry_in)) > datetime.now():
            return token
        else:
            if self.api_key:
                data = {"api-key": self.api_key}
            else:
                data = {
                  "username": self.username,
                  "password": self.password
                }
            if config.get("domain"):
                data.update({"domain": config["domain"]})
            data.update({"session-description": "FortiSOAR Session"})

            response = self.api_request("POST", "/login", data=data)
            session_timeout = response.get("session-timeout")
            current_time = datetime.now() + timedelta(seconds=(session_timeout-10))
            data_to_save = {
                "token": response.get("sid"),
                "expiry_in": int(current_time.timestamp())
            }
            update_connnector_config(connector_info["connector_name"], connector_info["connector_version"], data_to_save, config["config_id"])
            return token

    def api_request(self, method, endpoint, headers={}, params={}, data={}):
        try:
            params = self.build_params(params)
            data = self.build_params(data)
            endpoint = self.url + endpoint
            if "/login" not in endpoint:
                headers["X-chkp-sid"] = self.token
            headers["Content-Type"] = "application/json"

            logger.debug(f"\n---------------req-start---------------\n{method}-{endpoint}\nheaders: {headers}\nparams: {params}\ndata: {data}")
            try:
                from connectors.debug_utils.curl_script import make_curl
                make_curl(method, endpoint, headers=headers, params=params, data=data, verify_ssl=self.verify_ssl)
            except Exception as err:
                logger.error(f"Error in curl utils: {str(err)}")
            response = request(method, endpoint, headers=headers, params=params, data=data, verify=self.verify_ssl)

            if 200 <= response.status_code < 300:
                if response.text != "":
                    return response.json()
                else:
                    return True
            else:
                if response.text != "":
                    err_resp = response.json()
                    error_msg = 'Response [{0}: Details: {1}]'.format(response.status_code, err_resp)
                else:
                    error_msg = 'Response [{0}: Details {1}]'.format(response.status_code, response.content)
                logger.error(error_msg)
                raise ConnectorError(error_msg)
        except req_exceptions.SSLError:
            logger.error('An SSL error occurred')
            raise ConnectorError('An SSL error occurred')
        except req_exceptions.ConnectionError:
            logger.error('A connection error occurred')
            raise ConnectorError('A connection error occurred')
        except req_exceptions.Timeout:
            logger.error('The request timed out')
            raise ConnectorError('The request timed out')
        except req_exceptions.RequestException:
            logger.error('There was an error while handling the request')
            raise ConnectorError('There was an error while handling the request')
        except Exception as err:
            raise ConnectorError(str(err))

    def build_params(self, params):
        new_params = {}
        for key, value in params.items():
            if value is False or value == 0 or value:
                if key == "tags" and isinstance(value, str):
                    value = value.split(",")
                elif key == "details-level":
                    value = value.lower()
                elif key == "domains-to-process":
                    mapping = {"Current Domain": "CURRENT_DOMAIN", "All Domains on the Server": "ALL_DOMAINS_ON_THIS_SERVER"}
                    value = mapping.get(value)
                new_params[key] = value
        return new_params


def check_health_ex(config, connector_info):
    try:
        Checkpoint(config, connector_info, check_health=True)
        return True
    except Exception as err:
        raise ConnectorError(str(err))


def get_hosts_list(config, params, connector_info):
    ob = Checkpoint(config, connector_info)
    return ob.api_request("GET", "/show-hosts", data=params)


def get_host_details(config, params, connector_info):
    ob = Checkpoint(config, connector_info)
    return ob.api_request("GET", "/show-host", params=params)


def add_host(config, params, connector_info):
    ob = Checkpoint(config, connector_info)
    return ob.api_request("POST", "/add-host", data=params)


def update_host(config, params, connector_info):
    ob = Checkpoint(config, connector_info)
    return ob.api_request("POST", "/set-host", data=params)


def delete_host(config, params, connector_info):
    ob = Checkpoint(config, connector_info)
    return ob.api_request("POST", "/delete-host", data=params)


operations = {
    "add_host": add_host,
    "update_host": update_host,
    "get_hosts_list": get_hosts_list,
    "get_host_details": get_host_details,
    "delete_host": delete_host
}
