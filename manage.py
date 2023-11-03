#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""

import os
import sys
from django.core.management import execute_from_command_line

# Import the DJANGO_SETTINGS_MODULE from the settings file
from settings import DJANGO_SETTINGS_MODULE


def main():
    """
    Main function to execute Django management commands.
    """
    try:
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', DJANGO_SETTINGS_MODULE)
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Ensure it's installed and available on your PYTHONPATH environment variable. "
            "Activate a virtual environment if needed."
        ) from exc

    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
