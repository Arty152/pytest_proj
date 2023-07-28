def get_val(collection, key, default='git'):
    """
    Возвращает значение из словаря по переданному ключу.
    :param collection: исходный словарь.
    :param key: ключ, по которому возвращается значение, если ключ существует.
    :param default: возвращается в случае отсутсвия ключа в словаре.
    :return: значения по ключу или default.
    """
    if key in collection:
        return collection[key]
    else:
        return default