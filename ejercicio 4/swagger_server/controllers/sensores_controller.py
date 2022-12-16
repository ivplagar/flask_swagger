import connexion
import six

from swagger_server.models.meassure import Meassure  # noqa: E501
from swagger_server.models.message import Message  # noqa: E501
from swagger_server import util


def get_last_meassure_by_sensor(sensor):  # noqa: E501
    """Obtener la última medición del sensor

    Recuperar la última medida de un sensor # noqa: E501

    :param sensor: ID del sensor
    :type sensor: str

    :rtype: Meassure
    """
    return 'do some magic!'
