import math

def reorder_point(daily_demand: float, lead_time_days: float, sigma_demand: float, z: float) -> int:
    if daily_demand < 0 or lead_time_days < 0 or sigma_demand < 0 or z < 0:
        raise ValueError("Todos los parámetros deben ser mayores o iguales a cero")

    lt = math.ceil(lead_time_days)
    base = daily_demand * lt
    safety = z * sigma_demand * math.sqrt(lt)
    rop = base + safety

    return max(0, math.ceil(rop))
