import logging
import random
import re
import string

import pattern.en
import sqlite3 as sql

import misc

connection = sql.connect('