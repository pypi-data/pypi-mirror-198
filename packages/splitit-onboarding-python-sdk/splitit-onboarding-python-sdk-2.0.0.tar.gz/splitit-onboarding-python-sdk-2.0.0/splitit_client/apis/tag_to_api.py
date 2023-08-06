import typing_extensions

from splitit_client.apis.tags import TagValues
from splitit_client.apis.tags.data_api import DataApi
from splitit_client.apis.tags.merchants_api import MerchantsApi

TagToApi = typing_extensions.TypedDict(
    'TagToApi',
    {
        TagValues.DATA: DataApi,
        TagValues.MERCHANTS: MerchantsApi,
    }
)

tag_to_api = TagToApi(
    {
        TagValues.DATA: DataApi,
        TagValues.MERCHANTS: MerchantsApi,
    }
)
