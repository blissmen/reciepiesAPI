"""
Wait for database to be avaialble 
"""

from django.core.management.base import BaseCommand 
import time
from django.db import connection
from django.db.utils import OperationalError
from psycopg2 import OperationalError as Psycopg2Error

class Command(BaseCommand):
    help = 'Wait for database to be avaialble'

    def handle(self, *args, **kwargs):
        self.stdout.write('Waiting for database...')
        db_up = False;
        while db_up == False:
            try:
                self.check(databases=['default'])
                # connection.ensure_connection()
                db_up = True
            except (Psycopg2Error, OperationalError):
                self.stdout.write('Database connection not available, waiting 1 second...')
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS('Database connected!'))