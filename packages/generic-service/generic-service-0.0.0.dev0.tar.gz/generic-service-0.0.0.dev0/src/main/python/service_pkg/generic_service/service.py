"""Defines the Service class"""


class Service: # pylint: disable=too-few-public-methods
    """
    This class provides the a super class from which to build a service
    that can be run as a daemon and controlled by signals.
    """

    def __init__(self) -> None:
        """
        Creates an instance of this class.
        """
