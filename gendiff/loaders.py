import json
import types

import yaml

LOADERS = types.MappingProxyType({
    'json': json.loads,
    'yml': yaml.safe_load,
    'yaml': yaml.safe_load,
})


def get_loader(ext):
    return LOADERS[ext.lower()]
