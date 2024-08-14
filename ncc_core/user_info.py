#!/usr/bin/python3
"""
Usage:
# ---
from ncc_core import user_info
username = user_info.username
password = user_info.password
# ---
"""
import configparser
from pathlib import Path

Dir = str(Path(__file__).parents[0])
# ---
dir2 = Dir.replace("\\", "/")
dir2 = dir2.split("/ncc/")[0] + "/ncc"
# ---
config = configparser.ConfigParser()
config.read(dir2 + "/confs/nccommons_user.ini")
# ---
username = config["DEFAULT"]["username"].strip()
password = config["DEFAULT"]["password"].strip()
