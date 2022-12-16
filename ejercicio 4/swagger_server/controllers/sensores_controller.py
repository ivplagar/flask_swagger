import connexion
import six

from swagger_server.models.meassure import Meassure  # noqa: E501
from swagger_server.models.message import Message  # noqa: E501
from swagger_server import util


def get_historical_measures_by_sensor_and_type(sensor, start, end):  # noqa: E501
    """Obtener mediciones históricas del sensor en un rango de fechas

    Recuperar las mediciones de un sensor en un rango de fechas específico # noqa: E501

    :param sensor: ID del sensor
    :type sensor: str
    :param start: Fecha de inicio del rango (en formato yyyy-mm-dd)
    :type start: str
    :param end: Fecha de fin del rango (en formato yyyy-mm-dd)
    :type end: str

    :rtype: List[Meassure]
    """
    return 'do some magic!'


def get_last_meassure_by_sensor(sensor):  # noqa: E501
    """Obtener la última medición del sensor

    Recuperar la última medida de un sensor # noqa: E501

    :param sensor: ID del sensor
    :type sensor: str

    :rtype: Meassure
    """
    return 'do some magic!'
