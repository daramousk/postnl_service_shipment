# coding: utf-8

"""
    Labelling

    Generates a Base64 label  # noqa: E501

    OpenAPI spec version: v2_2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from postnl_service_shipment.api_client import ApiClient


class DefaultApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def shipment_v22_label_post(self, body, apikey, **kwargs):  # noqa: E501
        """shipment_v22_label_post  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.shipment_v22_label_post(body, apikey, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Request body: (required)
        :param str apikey: Authenticate using your API key (required)
        :param bool confirm: true or false; whether or not to confirm the shipments. Default value true.
        :return: Response
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.shipment_v22_label_post_with_http_info(body, apikey, **kwargs)  # noqa: E501
        else:
            (data) = self.shipment_v22_label_post_with_http_info(body, apikey, **kwargs)  # noqa: E501
            return data

    def shipment_v22_label_post_with_http_info(self, body, apikey, **kwargs):  # noqa: E501
        """shipment_v22_label_post  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.shipment_v22_label_post_with_http_info(body, apikey, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Request body: (required)
        :param str apikey: Authenticate using your API key (required)
        :param bool confirm: true or false; whether or not to confirm the shipments. Default value true.
        :return: Response
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'apikey', 'confirm']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method shipment_v22_label_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `shipment_v22_label_post`")  # noqa: E501
        # verify the required parameter 'apikey' is set
        if ('apikey' not in params or
                params['apikey'] is None):
            raise ValueError("Missing the required parameter `apikey` when calling `shipment_v22_label_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'confirm' in params:
            query_params.append(('confirm', params['confirm']))  # noqa: E501

        header_params = {}
        if 'apikey' in params:
            header_params['apikey'] = params['apikey']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/shipment/v2_2/label', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Response',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
