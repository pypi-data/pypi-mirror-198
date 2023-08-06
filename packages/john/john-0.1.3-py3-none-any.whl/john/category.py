def is_integer(n):
    try:
        int(n)
    except:
        return False

    return True


def is_numeric(n):
    try:
        int(n)
    except:
        try:
            float(n)
        except:
            return False

    return True
