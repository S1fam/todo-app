
def parse(feet_inches_local):
    parts = feet_inches_local.split(" ")
    feet_local = float(parts[0])
    inches_local = float(parts[1])
    return {"feet": feet_local, "inches": inches_local}


def convert(feet_local, inches_local):
    meters = feet_local * 0.3048 + inches_local * 0.0254
    return meters
