import os
import json

from config.config import config


def create_data_files():
    
    if not os.path.exists(config.segment_file_path):
        with open(config.segment_file_path, "w") as f:
            json.dump({}, f)
    
    if not os.path.exists(config.source_file_path):
        with open(config.source_file_path, "w") as f:
            json.dump({}, f)