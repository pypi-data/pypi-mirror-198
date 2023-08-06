import json
import logging
import os

import google.cloud.logging


class LoggingManager:
    """Logging Manager

    A wrapper on Python built-in logging module. that handles GCP Cloud Logging
    According to importance there are 6 levels i.e Debug,Info,Warning
        ,Error,Exception,Critical
    """

    def __init__(self, name: str = __name__, level: int = logging.DEBUG):
        """Initializing Logging Manager

        Args:
            name (str, optional): name of module/class which initialize
                logging. Defaults to __name__.
            level (int, optional): level to determine importance & up to what
                point capture logs. Defaults to logging.DEBUG.
            DEBUG : 10
            INFO : 20
            WARNING : 30
            ERROR : 40
            At time of initialization whatever the level is given below score
                levels will be ignored.
        """
        self.base_logging_level = level

        # set up the Google Cloud Logging python client library
        try:
            client = google.cloud.logging.Client()
            client.setup_logging()
        except Exception as e:  # noqa
            if os.environ.get("SERVICE_ACCOUNT_KEY_PATH"):
                # Following client will be used when testing locally
                client = google.cloud.logging.Client.from_service_account_json(
                    os.environ["SERVICE_ACCOUNT_KEY_PATH"]
                )
                client.setup_logging()

            if os.environ.get("EXCLUDE_KEYS"):
                self.exclude_keys = json.loads(os.environ["EXCLUDE_KEYS"])

            else:
                print("GCP Cloud Logging is not enabled for local testing")

        streamlogformat = "%(asctime)s [%(levelname)s] - %(name)s: %(message)s - JSON Payload: %(json_fields)s"  # noqa
        formatter = logging.Formatter(fmt=streamlogformat)

        self._logger = logging.getLogger(name)

        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(level)
        stream_handler.setFormatter(formatter)
        self._logger.addHandler(stream_handler)

        self._logger.setLevel(level)

    def _preprocess_json_params(self, params: dict):
        for key in self.exclude_keys:
            params.pop(key)

        return params

    def log(self, msg: str, json_params: dict, level: int):
        json_params = self._preprocess_json_params(json_params)
        self._logger.log(level, msg, extra={"json_fields": json_params})

    def debug(self, msg: str, json_params: dict):
        """Logs a debug message. Params: [msg] required"""
        json_params = self._preprocess_json_params(json_params)
        self._logger.debug(msg, extra={"json_fields": json_params})

    def info(self, msg: str, json_params: dict):
        """Logs a info message. Params: [msg] required"""
        json_params = self._preprocess_json_params(json_params)
        self._logger.info(msg, extra={"json_fields": json_params})

    def warning(self, msg: str, json_params: dict):
        """Logs a warning message. Params: [msg] required"""
        json_params = self._preprocess_json_params(json_params)
        self._logger.warning(msg, extra={"json_fields": json_params})

    def error(self, msg: str, json_params: dict):
        """Logs an error message. Params: [msg] required"""
        json_params = self._preprocess_json_params(json_params)
        self._logger.error(msg, extra={"json_fields": json_params})

    def exception(self, msg: str, json_params: dict):
        """Logs an exception. Params: [msg] required"""
        json_params = self._preprocess_json_params(json_params)
        self._logger.exception(msg, extra={"json_fields": json_params})
