
from src.weather import vädertyp


def välj_täcke(temp, regnar):
    väder = vädertyp(temp, regnar)

    if väder == "kallt":
        return "vintertäcke"
    elif väder == "regn":
        return "regntäcke"
    else:
        return "inget täcke"


## def välj_täcke(temp):
##    return "vintertäcke" if temp < 5 else "regntäcke"

