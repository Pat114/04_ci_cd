def vädertyp(temp, regnar):
    if regnar:
        return "regn"
    elif temp < 5:
        return "kallt"
    else:
        return "varmt"
