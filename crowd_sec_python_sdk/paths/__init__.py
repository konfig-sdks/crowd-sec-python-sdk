# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from crowd_sec_python_sdk.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    DECISIONS_STREAM = "/decisions/stream"
    DECISIONS = "/decisions"
    DECISIONS_DECISION_ID = "/decisions/{decision_id}"
    WATCHERS = "/watchers"
    WATCHERS_LOGIN = "/watchers/login"
    ALERTS = "/alerts"
    ALERTS_ALERT_ID = "/alerts/{alert_id}"
