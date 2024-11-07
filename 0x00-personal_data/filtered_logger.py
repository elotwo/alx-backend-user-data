#!/usr/bin/env python3
import re
import logging
from typing import List


def filter_datum(fields, redaction, message, separator):
    """
    this function  obfuscate some log massages
    """
    parts = message.split(separator)
    for field in fields:
        parts = [
                re.sub(f"{field}=[^;]*", f"{field}={redaction}", part)
                for part in parts
        ]
    return separator.join(parts)


def get_logger():
    """
    this function returns a logger object
    """
    logging.getLogger(user_data)
    logging.basicConfig(level=logging.INFO,)
    return logger


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """
        initiating class
        """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        layout
        """

        record.msg = filter_datum(
                self.fields,
                self.REDACTION,
                record.getMessage(),
                self.SEPARATOR
        )
        return super(RedactingFormatter, self).format(record)
