#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os #что значит import?
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myapp.settings')
    try:# проверяет код на наличие ошибок. 
        from django.core.management import execute_from_command_line
    except ImportError as exc: # except позволяет обрабатывать ошибку.
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':#  что значит эта консрукция 
    main()
