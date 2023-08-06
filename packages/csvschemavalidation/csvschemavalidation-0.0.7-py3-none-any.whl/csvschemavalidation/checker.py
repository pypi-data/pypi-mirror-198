#!/usr/bin/python
# -*-coding: utf-8 -*-

import csv
import json
from itertools import chain
from typing import Dict, Optional

import jsonschema
from csvschemavalidation import defaults, definitions, validators, utilities


class Cell(object):
    def __init__(self, value, row_number: int, column_name: str):
        self.value = value
        self.row_number = row_number
        self.column_name = column_name


class RFCDialect(csv.Dialect):
    """
    Default dialect is strict RFC 4180
    """

    strict = True  # use strict mode by default to fit RFC 4180
    delimiter = ","
    doublequote = True
    lineterminator = "\r\n"
    quotechar = '"'
    quoting = csv.QUOTE_MINIMAL
    skipinitialspace = False


class Validator:
    def __init__(
        self,
        csvfile: str,
        schema: Dict,
        output: Optional[str] = None,
        errors: str = "raise",
        strict=True,
    ):
        """
        :param csvfile: Path to CSV file
        :param schema: CSV Schema in dict
        :param output: Path to output file of errors. If output is None, print the error message. Default: None.
        :param errors: {'raise', 'coerce', 'raise_all'} If error is 'raise', stop the validation when it meets the first error. If
        error is 'coerce', output all errors. If error is 'raise_all', raise all errors at once
        :param strict: Whether to follow RFC 4180 strictly when parsing CSV file
        """

        self.csvfile = csvfile

        self.schema = schema

        self.output = output

        self.strict = strict

        if errors not in ("raise", "coerce", "raise_all"):
            raise ValueError("Unknown value for parameter errors")
        self.errors = errors

        self.header = []
        self.header_length = None

        self.column_validators = {"columns": {}, "unfoundfields": {}}

        self._meta_schema_path = definitions.META_SCHEMA_PATH

        self.validate_schema()

        self.csv_dialect = self.prepare_dialect()

    def prepare_dialect(self):
        dialect_option_mapping = {
            "delimiter": "delimiter",
            "doubleQuote": "doublequote",
            "lineTerminator": "lineterminator",
            "quoteChar": "quotechar",
            "skipInitialSpace": "skipinitialspace",
        }
        schema_dialect = self.schema.get("dialect", {})
        return type(
            "CSVDialect",
            (RFCDialect,),
            {
                "strict": self.strict,
                **{
                    dialect_option_mapping.get(k, k): v
                    for k, v in schema_dialect.items()
                },
            },
        )

    def validate_schema(self):
        with open(self._meta_schema_path, "r") as meta_schema:
            jsonschema.validate(self.schema, json.load(meta_schema))

    def validate(self):
        with open(self.csvfile, "r") as csvfile:
            csv_reader = csv.reader(csvfile, dialect=self.csv_dialect)

            # Read first line as header
            self.header = next(csv_reader)
            self.header_length = len(self.header)

            self.prepare_field_schema()

            with utilities.file_writer(self.output) as output:
                # Concat errors from header checking and row checking
                list_errors = []
                for error in chain(
                    self.check_header(), self.check_rows(csv_reader)
                ):
                    if self.errors == "raise":
                        raise error
                    elif self.errors == "coerce":
                        output.write(str(error))
                        output.write("\n")
                    else:
                        list_errors.append(str(error))

            if len(list_errors) != 0:
                raise Exception("\n".join(list_errors))

    def prepare_field_schema(self):
        """
        Prepare validators from `fields` option for every column

        Sample self.column_validators
        {
            'columns':{
                0: {
                    'column': '<COLUMN_NAME>',
                    'field_schema': {'name':'id', 'type': 'number'},
                    'validators': [
                        < function csvchecker._validators.validate_type >,
                        < function csvchecker._validators.validate_type >
                    ],
                    'patternfields': {
                        '<PATTERN>': {
                            'field_schema': {'name':'id', 'type': 'number'},
                            'column': '<COLUMN_NAME>'
                        }
                    }
                }
            },
            'unfoundfields': {
                '<FIELD_NAME>': {
                    'field_schema': {'name':'id', 'type': 'number'},
                    'column': '<COLUMN_NAME>'
                }
            },
            'definitions': {
                'ref1': {
                    'validators': [
                        < function csvchecker._validators.validate_type >,
                        < function csvchecker._validators.validate_type >
                    ],
                    'field_schema': {'name':'id', 'type': 'number'}
                }
            },
            'patternfields': {
                'ref1': {
                    'validators': [
                        < function csvchecker._validators.validate_type >,
                        < function csvchecker._validators.validate_type >
                    ],
                    'field_schema': {'name':'id', 'type': 'number'}
                }
            }
        }
        """

        # Sample header_index {'col_1': [0, 1],}
        # column names might not be unique
        header_index = {}
        for k, v in enumerate(self.header):
            if v in header_index:
                header_index[v].append(k)
            else:
                header_index[v] = [k]

        for field_schema in self.schema.get("fields", defaults.FIELDS):
            column_info = {
                "field_schema": field_schema,
                "column_name": field_schema["name"],
            }

            utilities.find_data_validators(
                column_info=column_info, field_schema=field_schema
            )

            # Pass the validators to one or more than one columns
            if field_schema["name"] in header_index.keys():
                for column_index in header_index[field_schema["name"]]:
                    self.column_validators["columns"][
                        column_index
                    ] = column_info
            # Store the unfound field names in column_validators.unfoundfields
            else:
                self.column_validators["unfoundfields"][
                    field_schema["name"]
                ] = column_info

    def check_header(self):
        for validator_name, validator in validators.HEADER_VALIDATORS.items():
            if validator_name in self.schema:
                yield from validator(
                    header=self.header,
                    schema=self.schema,
                    column_validators=self.column_validators,
                )

        # required is defined under field or definitions, but it is validated with header
        yield from validators.header_validators.field_required(
            header=self.header,
            schema=self.schema,
            column_validators=self.column_validators,
        )

    # TODO: document for callback
    def check_rows(self, csvreader, callback=lambda *args: None):
        for row_index, row in enumerate(csvreader):
            row_number = row_index + 1

            validators.rfc4180_validators.number_of_fields(
                row=row,
                row_number=row_number,
                header_length=self.header_length,
            )

            for index, column_info in self.column_validators[
                "columns"
            ].items():
                # TODO: replace cell
                # cell = Cell(value=row[index], row_number=row_number, column_name=self.header[index])
                cell = {
                    "value": row[index],
                    "row_number": row_number,
                    "column_name": self.header[index],
                }

                # Update cell['value'] to None if value is in missingValues
                yield from validators.data_validators.missingvalues(
                    cell=cell,
                    schema=self.schema,
                    column_validators=self.column_validators,
                )

                for validator in column_info["validators"]:
                    # Type validator convert cell value into target type, other validators don't accept None value
                    yield from validator(
                        cell=cell,
                        schema=self.schema,
                        field_schema=column_info["field_schema"],
                    )

            callback(row_index, row)
