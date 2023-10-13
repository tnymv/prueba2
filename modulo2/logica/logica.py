from reservacion.models import TipoHabitacion
def verificar_disponibilidad(tipo_habitacion, fecha_entrada, fecha_salida):
    # Implementa la lógica para verificar la disponibilidad de habitaciones aquí
    habitaciones_disponibles = TipoHabitacion.objects.filter(tipo=tipo_habitacion, reservacion__fecha_entrada__lte=fecha_entrada, reservacion__fecha_salida__gte=fecha_salida)
    return habitaciones_disponibles


def calcular_costos_transferencia(ruta):
    
    tarifas = {
        "Aeropuerto - Hotel": 200.00,
        "Hotel - Aeropuerto": 200.00,
        "Hotel - Quetzaltenango Guatemala": 400.00,
        "Quetzaltenango Guatemala - Hotel": 400.00
    }
    if ruta in tarifas:
        return tarifas[ruta]
    else:
        return 100.00  # Tarifa mínima por ruta

def calcular_cargo(cliente, tipo_habitacion, tipo_cliente, codigo_tarifa):
    if tipo_cliente == "corporativo" and codigo_tarifa:
        # Implementa la lógica para aplicar descuentos según el código de tarifa único
        descuento = 0.1  # Ejemplo de descuento del 10%
        if tipo_habitacion == "Simple":
            tarifa_base = 700.00
        elif tipo_habitacion == "Doble":
            tarifa_base = 1200.00
        elif tipo_habitacion == "Triple":
            tarifa_base = 2000.00
        elif tipo_habitacion == "Matrimonial":
            tarifa_base = 2500.00
        cargo_total = tarifa_base - (tarifa_base * descuento)
        return cargo_total
    else:
        # Implementa la lógica para calcular el cargo estándar para clientes no corporativos
        # Puedes usar las tarifas estándar aquí
        pass
