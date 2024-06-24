"""
from logs_fix.files import has_url_dir, move_text_dir
"""
from pathlib import Path

Dir = Path(__file__).parent

has_url_dir = Dir / "has_url"
move_text_dir = Dir / "move_text"
