"""

from fix_sets.bots.has_url import has_url_append, already_has_url

"""

import sys
import os
from logs_fix.files import has_url_dir

already_has_url = [x.replace(".h", "") for x in os.listdir(has_url_dir)]


def find_has_url(study_id):
    file = has_url_dir / f"{study_id}.h"
    if file.exists():
        return True
    return False


def has_url_append(study_id):
    if "nohas" in sys.argv:
        return
    # ---
    file = has_url_dir / f"{study_id}.h"
    if not file.exists():
        file.touch()
        print(f"has_url_append: {study_id}")
