from debug import logger
import logging
import os
import sys
from controllers.game import Game, initialize_pygame
from views.view_manager import ViewManager

# Ensure that working directory is sixth_corp
os.chdir((os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))


if __name__ == '__main__':
    logger.initialize_logging()
    logging.info('Start Application')

    initialize_pygame()
    view_manager = ViewManager()  # This instantiates the singleton class
    Game().run()

    sys.exit()
