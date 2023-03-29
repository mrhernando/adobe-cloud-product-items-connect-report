# -*- coding: utf-8 -*-
#
# Copyright (c) 2023, Ingram Micro
# All rights reserved.
from reports import api_calls
from reports import utils

def generate(
    client=None,
    input_data=None,
    progress_callback=None,
    renderer_type='xlsx',
    extra_context_callback=None,
):
    """
    Extracts data from Connect using the ConnectClient instance
    and input data provided as arguments, applies
    required transformations (if any) and returns the data rendered
    by the given renderer on the arguments list.
    Some renderers may require extra context data to generate the report
    output, for example in the case of the Jinja2 renderer...

    :param client: An instance of the CloudBlue Connect
                    client.
    :type client: cnct.ConnectClient
    :param input_data: Input data used to calculate the
                        resulting dataset.
    :type input_data: dict
    :param progress_callback: A function that accepts t
                                argument of type int that must
                                be invoked to notify the progress
                                of the report generation.
    :type progress_callback: func
    :param renderer_type: Renderer required for generating report
                            output.
    :type renderer_type: string
    :param extra_context_callback: Extra content required by some
                            renderers.
    :type extra_context_callback: func
    """
    items = api_calls.request_items(client, input_data["product"]['choices'][0])
    progress = 0
    total = items.count()
    for item in items:
        yield (
            utils.get_basic_value(item,'id'),
            utils.get_basic_value(item, 'name'),
            utils.get_basic_value(item, 'description'),
            utils.get_basic_value(item, 'type'),
            utils.get_basic_value(item, 'period'),
            utils.get_complex_value(item,['commitment','count']),
            utils.get_basic_value(item, 'mpn'),
            utils.get_complex_value(item, ['unit', 'unit']),
            utils.get_basic_value(item, 'status'),
            utils.get_complex_value(item, ['events','created','at']),
            utils.get_complex_value(item, ['events', 'updated', 'at'])
        )

        progress += 1
        progress_callback(progress, total)

