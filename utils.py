# screen width and height
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

import os
import sys

def resource_path(relative_path):
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)
