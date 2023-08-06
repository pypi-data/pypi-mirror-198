"""Friendly Base64 with str input and output, using UTF-8."""

# Written in 2023 by Eliah Kagan <degeneracypressure@gmail.com>.
#
# To the extent possible under law, the author(s) have dedicated all copyright
# and related and neighboring rights to this software to the public domain
# worldwide. This software is distributed without any warranty.
#
# You should have received a copy of the CC0 Public Domain Dedication along
# with this software. If not, see
# <http://creativecommons.org/publicdomain/zero/1.0/>.

__all__ = ['encode', 'decode']

import base64 as _base64


def encode(text: str) -> str:
    """Encode a string from UTF-8 text to Base64."""
    return _base64.b64encode(text.encode('utf-8')).decode('utf-8')


def decode(base64_text: str) -> str:
    """Decode a string from Base64 to UTF-8 text."""
    return _base64.b64decode(base64_text).decode('utf-8')
