def create_diff(first_dict, second_dict):
    keys = sorted(set(first_dict) | set(second_dict))

    result = []

    for key in keys:
        first_value = first_dict.get(key)
        second_value = second_dict.get(key)

        if first_value is None:
            result.append('+ {0}: {1}'.format(key, second_value))
        elif second_value is None:
            result.append('- {0}: {1}'.format(key, first_value))
        elif first_value == second_value:
            result.append('  {0}: {1}'.format(key, first_value))
        else:
            result.append('- {0}: {1}'.format(key, first_value))
            result.append('+ {0}: {1}'.format(key, second_value))

    return '{{\n  {0}\n}}'.format('\n  '.join(result))
