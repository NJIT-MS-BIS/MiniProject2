def squarerooting(num):
    try:
        if type(num) is not None:
            return round((float(num) ** 0.5), 8)
        else:
            return float(0)
    except (ValueError, TypeError):
        print ("Error: Check your data inputs")