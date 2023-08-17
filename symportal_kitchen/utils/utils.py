import os
import logging


def generate_lock_file(filepath):
    with open(filepath, 'w') as file:
        file.write(f'Locked by process ID: {os.getpid()}')
        logging.debug(
            f'Lock file generated. Current process ID: {os.getpid()}')
        return


def remove_lock_file(filepath):
    if os.path.isfile(filepath):
        os.remove(filepath)
        logging.debug(
            f'The lock file {filepath} has been successfully removed.')
    else:
        logging.debug(f'File {filepath} does not exist.')


def lock_file_exists(filepath):
    if os.path.exists(filepath):
        logging.info(
            'Cron job process exists for the current script. Exiting.')
        return True
    else:
        return False
