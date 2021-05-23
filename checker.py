def check(value):
    if value is not None:
        ret= float(value.replace(',',''))
    else:
        ret= 0
    return ret