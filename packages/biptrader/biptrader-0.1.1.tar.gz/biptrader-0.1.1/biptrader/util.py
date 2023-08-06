from jproperties import Properties


def load_properties_dict(path):
    result = {}
    props = Properties()
    with open(path, 'rb') as config_file:
        props.load(config_file)
        for item in props.items():
            result[item[0]] = item[1].data
    return result