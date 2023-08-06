# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from splitit_client.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    API_DATA_GETCOUNTRIES = "/api/data/get-countries"
    API_DATA_GETCURRENCIES = "/api/data/get-currencies"
    API_DATA_GETPROCESSORS = "/api/data/get-processors"
    API_DATA_GETVERTICALS = "/api/data/get-verticals"
    API_DATA_STATUSLEGEND = "/api/data/status-legend"
    API_MERCHANTS_GET = "/api/merchants/get"
    API_MERCHANTS_GETDETAILS = "/api/merchants/get-details"
    API_MERCHANTS_CREATE = "/api/merchants/create"
