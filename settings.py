# settings.py
import os
import random
import glob
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

DIRECTORY_A = os.environ.get("DIRECTORY_A")
DIRECTORY_B = os.environ.get("DIRECTORY_B")
DIRECTORY_C = os.environ.get("DIRECTORY_C")