from types import MappingProxyType

from gendiff.formatters.plain import plain
from gendiff.formatters.stylish import stylish

STYLISH = 'stylish'
PLAIN = 'plain'

FORMATTERS = MappingProxyType({
    STYLISH: stylish,
    PLAIN: plain,
})


def get_formatter(style):
    if style in FORMATTERS:
        return FORMATTERS.get(style)
    raise ValueError
