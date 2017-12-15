#!/usr/bin/env python

""" MultiQC module to parse output from Preseq """

from __future__ import print_function
import logging
import numpy as np

from multiqc import config
from multiqc.plots import linegraph
from multiqc.modules.base_module import BaseMultiqcModule

# Initialise the logger
log = logging.getLogger(__name__)

