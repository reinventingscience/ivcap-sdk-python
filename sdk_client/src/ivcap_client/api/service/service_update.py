from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient
from ...models.invalid_parameter_value import InvalidParameterValue
from ...models.invalid_scopes_t import InvalidScopesT
from ...models.not_implemented_t import NotImplementedT
from ...models.resource_not_found_t import ResourceNotFoundT
from ...models.service_description_t import ServiceDescriptionT
from ...models.service_status_rt import ServiceStatusRT
from ...types import UNSET, Response, Unset


def _get_kwargs(
    id: str,
    *,
    client: AuthenticatedClient,
    json_body: ServiceDescriptionT,
    force_create: Union[Unset, None, bool] = UNSET,
) -> Dict[str, Any]:
    url = "{}/1/services/{id}".format(client.base_url, id=id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["force-create"] = force_create

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    json_json_body = json_body.to_dict()

    return {
        "method": "put",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
        "params": params,
    }


def _parse_response(
    *, response: httpx.Response
) -> Optional[Union[Any, InvalidParameterValue, InvalidScopesT, NotImplementedT, ResourceNotFoundT, ServiceStatusRT]]:
    if response.status_code == 200:
        response_200 = ServiceStatusRT.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == 403:
        response_403 = InvalidScopesT.from_dict(response.json())

        return response_403
    if response.status_code == 404:
        response_404 = ResourceNotFoundT.from_dict(response.json())

        return response_404
    if response.status_code == 422:
        response_422 = InvalidParameterValue.from_dict(response.json())

        return response_422
    if response.status_code == 501:
        response_501 = NotImplementedT.from_dict(response.json())

        return response_501
    return None


def _build_response(
    *, response: httpx.Response
) -> Response[Union[Any, InvalidParameterValue, InvalidScopesT, NotImplementedT, ResourceNotFoundT, ServiceStatusRT]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    json_body: ServiceDescriptionT,
    force_create: Union[Unset, None, bool] = UNSET,
) -> Response[Union[Any, InvalidParameterValue, InvalidScopesT, NotImplementedT, ResourceNotFoundT, ServiceStatusRT]]:
    """update service

     Update an existing services and return its status.

    Args:
        id (str): ID of services to update Example: Enim officiis non repudiandae debitis maxime..
        force_create (Union[Unset, None, bool]): Create if not already exist
        json_body (ServiceDescriptionT):  Example: {'account-id': 'cayp:account:acme', 'banner':
            'http://stark.info/tess.gaylord', 'description': 'This service ...', 'metadata': [{'name':
            'Odit aut quod nihil aperiam.', 'value': 'Ut enim ut fugit possimus pariatur.'}, {'name':
            'Odit aut quod nihil aperiam.', 'value': 'Ut enim ut fugit possimus pariatur.'}, {'name':
            'Odit aut quod nihil aperiam.', 'value': 'Ut enim ut fugit possimus pariatur.'}, {'name':
            'Odit aut quod nihil aperiam.', 'value': 'Ut enim ut fugit possimus pariatur.'}], 'name':
            'Fire risk for Lot2', 'parameters': [{'description': 'The name of the region as according
            to ...', 'label': 'Region Name', 'name': 'region', 'type': 'string'}, {'label':
            'Rainfall/month threshold', 'name': 'threshold', 'type': 'float', 'unit': 'm'}],
            'provider-id': 'cayp:provider:acme', 'provider-ref': 'service_foo_patch_1', 'references':
            [{'title': 'Commodi aut voluptatem magni.', 'uri': 'http://mclaughlintremblay.name/adam'},
            {'title': 'Commodi aut voluptatem magni.', 'uri': 'http://mclaughlintremblay.name/adam'},
            {'title': 'Commodi aut voluptatem magni.', 'uri': 'http://mclaughlintremblay.name/adam'}],
            'tags': ['tag1', 'tag2'], 'workflow': {'argo': 'Sed ut in distinctio consequatur aut
            voluptas.', 'basic': {'command': ['Unde fuga sed veniam.', 'Et aut autem deserunt sit
            architecto.', 'Quidem nulla quae provident dolor amet nulla.'], 'cpu': {'limit': 'Deserunt
            fugiat hic eos quaerat voluptas distinctio.', 'request': 'Reprehenderit molestiae
            cupiditate voluptas et voluptatibus illum.'}, 'image': 'Officiis consequatur corporis
            autem.', 'memory': {'limit': 'Deserunt fugiat hic eos quaerat voluptas distinctio.',
            'request': 'Reprehenderit molestiae cupiditate voluptas et voluptatibus illum.'}}, 'opts':
            'Et vel.', 'type': 'Alias aut voluptas molestiae.'}}.

    Returns:
        Response[Union[Any, InvalidParameterValue, InvalidScopesT, NotImplementedT, ResourceNotFoundT, ServiceStatusRT]]
    """

    kwargs = _get_kwargs(
        id=id,
        client=client,
        json_body=json_body,
        force_create=force_create,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    id: str,
    *,
    client: AuthenticatedClient,
    json_body: ServiceDescriptionT,
    force_create: Union[Unset, None, bool] = UNSET,
) -> Optional[Union[Any, InvalidParameterValue, InvalidScopesT, NotImplementedT, ResourceNotFoundT, ServiceStatusRT]]:
    """update service

     Update an existing services and return its status.

    Args:
        id (str): ID of services to update Example: Enim officiis non repudiandae debitis maxime..
        force_create (Union[Unset, None, bool]): Create if not already exist
        json_body (ServiceDescriptionT):  Example: {'account-id': 'cayp:account:acme', 'banner':
            'http://stark.info/tess.gaylord', 'description': 'This service ...', 'metadata': [{'name':
            'Odit aut quod nihil aperiam.', 'value': 'Ut enim ut fugit possimus pariatur.'}, {'name':
            'Odit aut quod nihil aperiam.', 'value': 'Ut enim ut fugit possimus pariatur.'}, {'name':
            'Odit aut quod nihil aperiam.', 'value': 'Ut enim ut fugit possimus pariatur.'}, {'name':
            'Odit aut quod nihil aperiam.', 'value': 'Ut enim ut fugit possimus pariatur.'}], 'name':
            'Fire risk for Lot2', 'parameters': [{'description': 'The name of the region as according
            to ...', 'label': 'Region Name', 'name': 'region', 'type': 'string'}, {'label':
            'Rainfall/month threshold', 'name': 'threshold', 'type': 'float', 'unit': 'm'}],
            'provider-id': 'cayp:provider:acme', 'provider-ref': 'service_foo_patch_1', 'references':
            [{'title': 'Commodi aut voluptatem magni.', 'uri': 'http://mclaughlintremblay.name/adam'},
            {'title': 'Commodi aut voluptatem magni.', 'uri': 'http://mclaughlintremblay.name/adam'},
            {'title': 'Commodi aut voluptatem magni.', 'uri': 'http://mclaughlintremblay.name/adam'}],
            'tags': ['tag1', 'tag2'], 'workflow': {'argo': 'Sed ut in distinctio consequatur aut
            voluptas.', 'basic': {'command': ['Unde fuga sed veniam.', 'Et aut autem deserunt sit
            architecto.', 'Quidem nulla quae provident dolor amet nulla.'], 'cpu': {'limit': 'Deserunt
            fugiat hic eos quaerat voluptas distinctio.', 'request': 'Reprehenderit molestiae
            cupiditate voluptas et voluptatibus illum.'}, 'image': 'Officiis consequatur corporis
            autem.', 'memory': {'limit': 'Deserunt fugiat hic eos quaerat voluptas distinctio.',
            'request': 'Reprehenderit molestiae cupiditate voluptas et voluptatibus illum.'}}, 'opts':
            'Et vel.', 'type': 'Alias aut voluptas molestiae.'}}.

    Returns:
        Response[Union[Any, InvalidParameterValue, InvalidScopesT, NotImplementedT, ResourceNotFoundT, ServiceStatusRT]]
    """

    return sync_detailed(
        id=id,
        client=client,
        json_body=json_body,
        force_create=force_create,
    ).parsed


async def asyncio_detailed(
    id: str,
    *,
    client: AuthenticatedClient,
    json_body: ServiceDescriptionT,
    force_create: Union[Unset, None, bool] = UNSET,
) -> Response[Union[Any, InvalidParameterValue, InvalidScopesT, NotImplementedT, ResourceNotFoundT, ServiceStatusRT]]:
    """update service

     Update an existing services and return its status.

    Args:
        id (str): ID of services to update Example: Enim officiis non repudiandae debitis maxime..
        force_create (Union[Unset, None, bool]): Create if not already exist
        json_body (ServiceDescriptionT):  Example: {'account-id': 'cayp:account:acme', 'banner':
            'http://stark.info/tess.gaylord', 'description': 'This service ...', 'metadata': [{'name':
            'Odit aut quod nihil aperiam.', 'value': 'Ut enim ut fugit possimus pariatur.'}, {'name':
            'Odit aut quod nihil aperiam.', 'value': 'Ut enim ut fugit possimus pariatur.'}, {'name':
            'Odit aut quod nihil aperiam.', 'value': 'Ut enim ut fugit possimus pariatur.'}, {'name':
            'Odit aut quod nihil aperiam.', 'value': 'Ut enim ut fugit possimus pariatur.'}], 'name':
            'Fire risk for Lot2', 'parameters': [{'description': 'The name of the region as according
            to ...', 'label': 'Region Name', 'name': 'region', 'type': 'string'}, {'label':
            'Rainfall/month threshold', 'name': 'threshold', 'type': 'float', 'unit': 'm'}],
            'provider-id': 'cayp:provider:acme', 'provider-ref': 'service_foo_patch_1', 'references':
            [{'title': 'Commodi aut voluptatem magni.', 'uri': 'http://mclaughlintremblay.name/adam'},
            {'title': 'Commodi aut voluptatem magni.', 'uri': 'http://mclaughlintremblay.name/adam'},
            {'title': 'Commodi aut voluptatem magni.', 'uri': 'http://mclaughlintremblay.name/adam'}],
            'tags': ['tag1', 'tag2'], 'workflow': {'argo': 'Sed ut in distinctio consequatur aut
            voluptas.', 'basic': {'command': ['Unde fuga sed veniam.', 'Et aut autem deserunt sit
            architecto.', 'Quidem nulla quae provident dolor amet nulla.'], 'cpu': {'limit': 'Deserunt
            fugiat hic eos quaerat voluptas distinctio.', 'request': 'Reprehenderit molestiae
            cupiditate voluptas et voluptatibus illum.'}, 'image': 'Officiis consequatur corporis
            autem.', 'memory': {'limit': 'Deserunt fugiat hic eos quaerat voluptas distinctio.',
            'request': 'Reprehenderit molestiae cupiditate voluptas et voluptatibus illum.'}}, 'opts':
            'Et vel.', 'type': 'Alias aut voluptas molestiae.'}}.

    Returns:
        Response[Union[Any, InvalidParameterValue, InvalidScopesT, NotImplementedT, ResourceNotFoundT, ServiceStatusRT]]
    """

    kwargs = _get_kwargs(
        id=id,
        client=client,
        json_body=json_body,
        force_create=force_create,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    id: str,
    *,
    client: AuthenticatedClient,
    json_body: ServiceDescriptionT,
    force_create: Union[Unset, None, bool] = UNSET,
) -> Optional[Union[Any, InvalidParameterValue, InvalidScopesT, NotImplementedT, ResourceNotFoundT, ServiceStatusRT]]:
    """update service

     Update an existing services and return its status.

    Args:
        id (str): ID of services to update Example: Enim officiis non repudiandae debitis maxime..
        force_create (Union[Unset, None, bool]): Create if not already exist
        json_body (ServiceDescriptionT):  Example: {'account-id': 'cayp:account:acme', 'banner':
            'http://stark.info/tess.gaylord', 'description': 'This service ...', 'metadata': [{'name':
            'Odit aut quod nihil aperiam.', 'value': 'Ut enim ut fugit possimus pariatur.'}, {'name':
            'Odit aut quod nihil aperiam.', 'value': 'Ut enim ut fugit possimus pariatur.'}, {'name':
            'Odit aut quod nihil aperiam.', 'value': 'Ut enim ut fugit possimus pariatur.'}, {'name':
            'Odit aut quod nihil aperiam.', 'value': 'Ut enim ut fugit possimus pariatur.'}], 'name':
            'Fire risk for Lot2', 'parameters': [{'description': 'The name of the region as according
            to ...', 'label': 'Region Name', 'name': 'region', 'type': 'string'}, {'label':
            'Rainfall/month threshold', 'name': 'threshold', 'type': 'float', 'unit': 'm'}],
            'provider-id': 'cayp:provider:acme', 'provider-ref': 'service_foo_patch_1', 'references':
            [{'title': 'Commodi aut voluptatem magni.', 'uri': 'http://mclaughlintremblay.name/adam'},
            {'title': 'Commodi aut voluptatem magni.', 'uri': 'http://mclaughlintremblay.name/adam'},
            {'title': 'Commodi aut voluptatem magni.', 'uri': 'http://mclaughlintremblay.name/adam'}],
            'tags': ['tag1', 'tag2'], 'workflow': {'argo': 'Sed ut in distinctio consequatur aut
            voluptas.', 'basic': {'command': ['Unde fuga sed veniam.', 'Et aut autem deserunt sit
            architecto.', 'Quidem nulla quae provident dolor amet nulla.'], 'cpu': {'limit': 'Deserunt
            fugiat hic eos quaerat voluptas distinctio.', 'request': 'Reprehenderit molestiae
            cupiditate voluptas et voluptatibus illum.'}, 'image': 'Officiis consequatur corporis
            autem.', 'memory': {'limit': 'Deserunt fugiat hic eos quaerat voluptas distinctio.',
            'request': 'Reprehenderit molestiae cupiditate voluptas et voluptatibus illum.'}}, 'opts':
            'Et vel.', 'type': 'Alias aut voluptas molestiae.'}}.

    Returns:
        Response[Union[Any, InvalidParameterValue, InvalidScopesT, NotImplementedT, ResourceNotFoundT, ServiceStatusRT]]
    """

    return (
        await asyncio_detailed(
            id=id,
            client=client,
            json_body=json_body,
            force_create=force_create,
        )
    ).parsed