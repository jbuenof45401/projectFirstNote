def calcular_precio_producto(coste_producto):
    '''
    (num) -> float: valor del producto

    calcular el coste del producto aumentando el 50% de su valor como comision

    >>> calcular_precio_producto(5000)
    7500.0

    >>> calcular_precio_producto(1000)
    1500.0

    :param coste_producto: representa el coste del producto
    :return: valor del producto
    '''
    return coste_producto + (coste_producto * 0.5)


def calcular_precio_servicio(cantidad_horas):
    '''
    (num) -> num: precio por horas trabajadas

    >>> calcular_precio_servicio(5)
    500000

    >>> calcular_precio_servicio(4)
    400000

    :param cantidad_horas: horas de servicio prestado
    :return: valor de las horas prestadas
    '''

    return cantidad_horas * 100000


def calcular_precio_servicio_extras(cantidad_horas):
    '''
    (num) -> float: recibe las horas extra trabajadas, devuelve el valor por las horas extra

    >>> calcular_precio_servicio_extras(1)
    125000.0
    >>> calcular_precio_servicio_extras(2)
    250000.0

    :param cantidad_horas: cantidad de horas extra trabajadas
    :return: valor de las horas extra
    '''

    precio_hora_normal = calcular_precio_servicio(cantidad_horas)

    return precio_hora_normal + (precio_hora_normal*0.25)


def calcular_costo_envio(kilometros):
    '''
    (num) -> num: recibe kilometros y devuelve el valor por los kilometros recorridos

    >>> calcular_costo_envio(2)
    230

    >>> calcular_costo_envio(3)
    345

    :param kilometros: cantidad de kilometros recorridos
    :return: valor por los kilometros recorridos
    '''

    return  kilometros * 115

def calcular_precio_producto_fuera(coste_producto,
                                   kilometros):
    '''
    (num) -> num: devuelve el valor del producto y el recargo por kilometro recorrido


    :param coste_producto: num: costo del producto para jose
    :param kilometros: num: kilometros recorridos por jose
    :return: float: precio del producto mas recargo de envio
    '''

    return calcular_precio_producto(coste_producto) + calcular_costo_envio(kilometros)




def calcular_iva_producto(coste_producto, tasa):
    pass


def calcular_iva_servicio(cantidad_horas, tasa):
    pass


def calcular_iva_envio(kilometros, tasa):
    pass


def calcular_iva_servicio_fuera(cantidad_horas, tasa):
    pass


def calcular_recaudo_locales(coste_producto_1,
                             coste_producto_2,
                             coste_producto_3):
    pass

def calcular_recaudo_horas_extra(horas_1,
                                 horas_2,
                                 horas_3,
                                 horas_4):
    pass


def calcular_recaudo_mixto_local(coste_producto_1,
                                 coste_producto_2,
                                 horas_1,
                                 horas_2):
    pass