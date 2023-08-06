import google.cloud.logging
import logging
import json
from typing import Any

# Setup logging
# client = google.cloud.logging.Client.from_service_account_json(
#     './common/ceetu-project-log.json')
client = google.cloud.logging.Client()
client.setup_logging()


def insert_log(msg):
    logging.info(msg)


def insert_json_log(msg):
    logging.info(log_json_object(msg))


def insert_extra_log(msg, extramsg):
    logging.info(msg, extra=log_object(extramsg))


def insert_exception(msg):
    logging.exception(msg)


def get_json(data) -> Any:
    return json.loads(data)


def log_object(data) -> Any:
    return {"json_fields": get_json(data)}


def log_json_object(data) -> Any:
    return {"respmsg": get_json(data)}
