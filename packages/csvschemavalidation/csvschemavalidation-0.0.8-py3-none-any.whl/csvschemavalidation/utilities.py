#!/usr/bin/python
# -*-coding: utf-8 -*-

import contextlib
import sys
from itertools import islice

from csvschemavalidation.validators import data_validators


@contextlib.contextmanager
def file_writer(file_name=None):
    writer = open(file_name, "w") if file_name is not None else sys.stdout
    yield writer
    if file_name is not None:
        writer.close()


def find_data_validators(column_info, field_schema):
    """
    Go through the options in field_schema, fetch the validators and add them into column_info['validators']
    """
    if "$ref" in field_schema.keys():
        column_info["ref"] = field_schema["$ref"]
    # Otherwise, make sure type checking is the first one
    else:
        # type checking always exists
        column_info["validators"] = [data_validators.field_type]

        for field_option in field_schema.keys():
            validator = data_validators.DATA_VALIDATORS.get(field_option)
            if validator is not None:
                column_info["validators"].append(validator)


def step_slice(g, step):
    """Yield successive step-sized chunks from generator."""
    while True:
        lines = list(islice(g, step))
        if not lines:
            return
        yield lines
