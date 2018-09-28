# -*- coding: utf-8 -*-

from dask import dataframe as dd
from lapis.log.record import LapisLog

import threading

lalog = LapisLog()

class BaseReader(threading.Thread):
    def __init__(self, uri, sqlexp, chunk_size=5000):
        super().__init__()
