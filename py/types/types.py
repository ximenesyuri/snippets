def type_coprod_(*types):
    """
    implementation of Union[types]
    """
    for typ in types:
        if not isinstance(typ, type):
            raise TypeError(f"{typ} is not a valid type.")

    class _coprod(type):
        def __instancecheck__(cls, instance):
            return any(isinstance(instance, typ) for typ in cls._types)

    class coprod_(metaclass=_coprod):
        _types = types
    return coprod_

def type_prod_(*types):
    """
    implementation of Tuple[types]
    """
    for typ in types:
        if not isinstance(typ, type):
            raise TypeError(f"{typ} is not a valid type.")

    class _prod(type):
        def __instancecheck__(cls, instance):
            if not isinstance(instance, tuple):
                return False
            if len(instance) != len(cls._types):
                return False
            return all(isinstance(elem, typ) for elem, typ in zip(instance, cls._types))

    class prod_(metaclass=_prod):
        _types = types
    return prod_

def type_unprod_(*types):
    """
    implementation of Set(Union[types])
    """
    for typ in types:
        if not isinstance(typ, type):
            raise TypeError(f"{typ} is not a valid type.")

    class _unprod(type):
    def __instancecheck__(cls, instance):
        if not isinstance(instance, set):
            return False
        type_counts = {typ: types.count(typ) for typ in types}
        for elem in instance:
            for typ in type_counts:
                if isinstance(elem, typ) and type_counts[typ] > 0:
                    type_counts[typ] -= 1
                    break
            else:
                return False
        return all(count == 0 for count in type_counts.values())
    class unprod_(metaclass=_unprod):
        _types = types
    return unprod_
