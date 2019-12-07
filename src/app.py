import logging
import os
import sys

from controllers import game
from debug import logger

# Ensure that working directory is sixth_corp
os.chdir((os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


if __name__ == '__main__':
    logger.initialize_logging()
    logging.info('Start Application')

    game.initialize_pygame()
    g = game.Game()
    g.run()

    sys.exit()
