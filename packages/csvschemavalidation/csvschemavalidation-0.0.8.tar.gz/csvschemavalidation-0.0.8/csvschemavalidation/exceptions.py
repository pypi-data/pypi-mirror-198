#!/usr/bin/python
# -*-coding: utf-8 -*-


class ValidationError(Exception):
    def __init__(self, message, column=None, row_number=None, *args):
        self.message = message
        self.column = column
        self.row_number = row_number

        super(ValidationError, self).__init__(message, column, row_number, *args)

    def __str__(self):
        return "<%s: %r; column name: %s; row number: %s>" % (
            self.__class__.__name__,
            self.message,
            self.column,
            self.row_number,
        )
