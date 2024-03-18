from crowd_sec_python_sdk.paths.alerts.get import ApiForget
from crowd_sec_python_sdk.paths.alerts.post import ApiForpost
from crowd_sec_python_sdk.paths.alerts.delete import ApiFordelete
from crowd_sec_python_sdk.paths.alerts.head import ApiForhead


class Alerts(
    ApiForget,
    ApiForpost,
    ApiFordelete,
    ApiForhead,
):
    pass
