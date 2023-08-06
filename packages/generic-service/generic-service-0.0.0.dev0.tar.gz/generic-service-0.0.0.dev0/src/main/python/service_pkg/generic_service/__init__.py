"""
This module provides the classes from which to build service that can be
run as a daemon and controlled by signals.
"""

from .service import Service as Service  # pylint: disable=useless-import-alias
