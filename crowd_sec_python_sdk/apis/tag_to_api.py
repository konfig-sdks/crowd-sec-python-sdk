import typing_extensions

from crowd_sec_python_sdk.apis.tags import TagValues
from crowd_sec_python_sdk.apis.tags.watchers_api import WatchersApi
from crowd_sec_python_sdk.apis.tags.bouncers_api import BouncersApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.WATCHERS: WatchersApi,
        TagValues.BOUNCERS: BouncersApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.WATCHERS: WatchersApi,
        TagValues.BOUNCERS: BouncersApi,
    }
)
