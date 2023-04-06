import os
import sys
import pandas as pd
import numpy as np
from pathlib import Path
import pickle
from datetime import datetime
from torch.utils.data import TensorDataset

# PROBE_ABLY_DIR = '/media/julia/Data/Code/PhD/Probe-Ably'
ENCODE_CONFIG_FILE = './experiments/encode_configs.json'

from nli_xy.encoding import parse_encode_config, encode_from_config

##  nli_xy create representations
encode_configs = parse_encode_config(ENCODE_CONFIG_FILE)

all_data_encodings = encode_from_config(encode_configs)