from unittest.mock import patch
from psycopg2 import OperationalError as Psycopg2Error

from django.core.management import call_command
from django.db.utils import OperationalError
from django.test import SimpleTestCase


class CommandTests(SimpleTestCase):
    @patch('core.management.commands.wait_db.Command.check')
    def test_wait_for_db_ready(self, patched_check):
        patched_check.return_value = True

        call_command('wait_db')

        patched_check.assert_called_once_with(databases=['default'])
    @patch('core.management.commands.wait_db.Command.check')
    @patch('time.sleep')
    def test_wait_for_db_not_ready(self, patched_sleep,patched_check):
        patched_check.side_effect = [Psycopg2Error] * 2 + [OperationalError] * 3 + [True]

        call_command('wait_db')
        patched_sleep.assert_called()
        self.assertEqual(patched_check.call_count, 6)
        patched_check.assert_called_with(databases=['default'])