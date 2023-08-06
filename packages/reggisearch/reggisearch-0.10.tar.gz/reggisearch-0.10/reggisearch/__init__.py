# based on https://stackoverflow.com/a/40583388/15096247
from winreg import *
import os

import re

roots_hives = {
    "HKEY_CLASSES_ROOT": HKEY_CLASSES_ROOT,
    "HKEY_CURRENT_USER": HKEY_CURRENT_USER,
    "HKEY_LOCAL_MACHINE": HKEY_LOCAL_MACHINE,
    "HKEY_USERS": HKEY_USERS,
    "HKEY_PERFORMANCE_DATA": HKEY_PERFORMANCE_DATA,
    "HKEY_CURRENT_CONFIG": HKEY_CURRENT_CONFIG,
    "HKEY_DYN_DATA": HKEY_DYN_DATA,
}


def parse_key(key):
    key = key.upper()
    parts = key.split("\\")
    root_hive_name = parts[0]
    root_hive = roots_hives.get(root_hive_name)
    partial_key = "\\".join(parts[1:])

    if not root_hive:
        raise Exception('root hive "{}" was not found'.format(root_hive_name))

    return partial_key, root_hive


def get_sub_keys(key):
    partial_key, root_hive = parse_key(key)

    with ConnectRegistry(None, root_hive) as reg:
        with OpenKey(reg, partial_key) as key_object:
            sub_keys_count, values_count, last_modified = QueryInfoKey(key_object)
            try:
                for i in range(sub_keys_count):
                    sub_key_name = EnumKey(key_object, i)
                    yield sub_key_name
            except WindowsError:
                pass


def get_values(key, fields):
    partial_key, root_hive = parse_key(key)
    data = {}
    with ConnectRegistry(None, root_hive) as reg:
        with OpenKey(reg, partial_key) as key_object:

            for field in fields:
                try:
                    value, type = QueryValueEx(key_object, field)
                    data[field] = value
                except WindowsError:
                    continue
    return data


def join(path, *paths):
    path = path.strip("/\\")
    paths = map(lambda x: x.strip("/\\"), paths)
    paths = list(paths)
    result = os.path.join(path, *paths)
    result = result.replace("/", "\\")
    return result

def search_values(mainkeys, subkeys):
    key = re.findall(r'\\[^\\]+$', mainkeys)[0]
    mainkeys = mainkeys[:-len(key)]
    key=key.strip('\\')
    allresults = {}
    if isinstance(subkeys, str):
        subkeys = [subkeys]
    elif isinstance(subkeys, tuple):
        subkeys = list(subkeys)
    for sub_key in get_sub_keys(mainkeys):
        path = join(mainkeys, sub_key)
        if sub_key.strip() == key:
            alva = get_values(path, subkeys)
            if alva:
                allresults[path] = alva
    return allresults

