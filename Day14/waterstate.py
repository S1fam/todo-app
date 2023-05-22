melting_point = 0
boiling_point = 0


def water_state(temperature_local):
    if temperature_local < melting_point:
        state = "Solid"
    elif melting_point < temperature_local < boiling_point:
        state = "Liquid"
    else:
        state = "Gas"
    return state
