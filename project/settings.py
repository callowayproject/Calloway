# Django settings for project project.

import bombay
import os
import sys

BOMBAY_ROOT = os.path.abspath(os.path.dirname(bombay.__file__))
sys.path.insert(0, os.path.join(BOMBAY_ROOT, 'apps'))

from bombay.settings import *

PUBLICATION_NAME = 'The Example Times'