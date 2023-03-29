# -*- coding: utf-8 -*-
#
# Copyright (c) 2023, Ingram Micro
# All rights reserved.
#
import pytest

from reports.product_items.entrypoint import generate

parameters = {
   "product": {
        "all": True,
        "choices": ['PRD-207-752-513'],
    }
}

def test_product_items(
    mocker,
    progress,
    sync_client_factory,
    response_factory,
    extra_context_callback,
    response_product_items
):
    responses = [
        response_factory(
            query=None,
            value=response_product_items
        ),
        response_factory(
            query=None,
            value=response_product_items
        )
    ]

    client = sync_client_factory(responses)

    result = generate(client, parameters, progress)
    assert len(list(result)) == 20