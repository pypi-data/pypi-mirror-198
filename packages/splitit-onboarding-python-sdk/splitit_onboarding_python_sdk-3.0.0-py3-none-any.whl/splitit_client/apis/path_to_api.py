import typing_extensions

from splitit_client.paths import PathValues
from splitit_client.apis.paths.api_data_get_countries import ApiDataGetCountries
from splitit_client.apis.paths.api_data_get_currencies import ApiDataGetCurrencies
from splitit_client.apis.paths.api_data_get_processors import ApiDataGetProcessors
from splitit_client.apis.paths.api_data_get_verticals import ApiDataGetVerticals
from splitit_client.apis.paths.api_data_status_legend import ApiDataStatusLegend
from splitit_client.apis.paths.api_merchants_get import ApiMerchantsGet
from splitit_client.apis.paths.api_merchants_get_details import ApiMerchantsGetDetails
from splitit_client.apis.paths.api_merchants_create import ApiMerchantsCreate
from splitit_client.apis.paths.api_merchants_create_developer import ApiMerchantsCreateDeveloper

PathToApi = typing_extensions.TypedDict(
    'PathToApi',
    {
        PathValues.API_DATA_GETCOUNTRIES: ApiDataGetCountries,
        PathValues.API_DATA_GETCURRENCIES: ApiDataGetCurrencies,
        PathValues.API_DATA_GETPROCESSORS: ApiDataGetProcessors,
        PathValues.API_DATA_GETVERTICALS: ApiDataGetVerticals,
        PathValues.API_DATA_STATUSLEGEND: ApiDataStatusLegend,
        PathValues.API_MERCHANTS_GET: ApiMerchantsGet,
        PathValues.API_MERCHANTS_GETDETAILS: ApiMerchantsGetDetails,
        PathValues.API_MERCHANTS_CREATE: ApiMerchantsCreate,
        PathValues.API_MERCHANTS_CREATE_DEVELOPER: ApiMerchantsCreateDeveloper,
    }
)

path_to_api = PathToApi(
    {
        PathValues.API_DATA_GETCOUNTRIES: ApiDataGetCountries,
        PathValues.API_DATA_GETCURRENCIES: ApiDataGetCurrencies,
        PathValues.API_DATA_GETPROCESSORS: ApiDataGetProcessors,
        PathValues.API_DATA_GETVERTICALS: ApiDataGetVerticals,
        PathValues.API_DATA_STATUSLEGEND: ApiDataStatusLegend,
        PathValues.API_MERCHANTS_GET: ApiMerchantsGet,
        PathValues.API_MERCHANTS_GETDETAILS: ApiMerchantsGetDetails,
        PathValues.API_MERCHANTS_CREATE: ApiMerchantsCreate,
        PathValues.API_MERCHANTS_CREATE_DEVELOPER: ApiMerchantsCreateDeveloper,
    }
)
