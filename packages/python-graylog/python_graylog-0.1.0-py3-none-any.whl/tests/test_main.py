import logging
import os
import sys

import graylog.http

# Get the path of the current file
current_file_path = os.path.abspath(__file__)

# Get the parent directory of the current file
parent_dir_path = os.path.dirname(os.path.dirname(current_file_path))

sys.path.append(parent_dir_path)

import graylog


def test():
    logger = logging.getLogger('test_logger')
    logger.setLevel(logging.DEBUG)

    # handler = graylog.GELFUDPHandler('82.157.73.141', 12202)
    handler = graylog.http.GELFHTTPHandler('log.kxxxl.com', 80)
    logger.addHandler(handler)

    logger.debug('''This is a test message from python-graylog.''')

    print('Done.')


if __name__ == '__main__':
    test()
