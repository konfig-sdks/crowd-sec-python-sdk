from crowd_sec_python_sdk.paths.decisions.get import ApiForget
from crowd_sec_python_sdk.paths.decisions.delete import ApiFordelete
from crowd_sec_python_sdk.paths.decisions.head import ApiForhead


class Decisions(
    ApiForget,
    ApiFordelete,
    ApiForhead,
):
    pass
