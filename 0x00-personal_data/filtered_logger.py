#!/usr/bin/env python3
import re

def filter_datum(fields, redaction, message, separator):
    parts = message.split(separator)
    for field in fields:
        parts = [re.sub(f"{field}=[^;]*", f"{field}={redaction}", part) for part in parts]
    return separator.join(parts)
