import typing_extensions

from crowd_sec_python_sdk.paths import PathValues
from crowd_sec_python_sdk.apis.paths.decisions_stream import DecisionsStream
from crowd_sec_python_sdk.apis.paths.decisions import Decisions
from crowd_sec_python_sdk.apis.paths.decisions_decision_id import DecisionsDecisionId
from crowd_sec_python_sdk.apis.paths.watchers import Watchers
from crowd_sec_python_sdk.apis.paths.watchers_login import WatchersLogin
from crowd_sec_python_sdk.apis.paths.alerts import Alerts
from crowd_sec_python_sdk.apis.paths.alerts_alert_id import AlertsAlertId

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.DECISIONS_STREAM: DecisionsStream,
        PathValues.DECISIONS: Decisions,
        PathValues.DECISIONS_DECISION_ID: DecisionsDecisionId,
        PathValues.WATCHERS: Watchers,
        PathValues.WATCHERS_LOGIN: WatchersLogin,
        PathValues.ALERTS: Alerts,
        PathValues.ALERTS_ALERT_ID: AlertsAlertId,
    }
)

path_to_api = PathToApi(
    {
        PathValues.DECISIONS_STREAM: DecisionsStream,
        PathValues.DECISIONS: Decisions,
        PathValues.DECISIONS_DECISION_ID: DecisionsDecisionId,
        PathValues.WATCHERS: Watchers,
        PathValues.WATCHERS_LOGIN: WatchersLogin,
        PathValues.ALERTS: Alerts,
        PathValues.ALERTS_ALERT_ID: AlertsAlertId,
    }
)
