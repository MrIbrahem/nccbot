'''

python3 /data/project/ncc/nccbot/mass/radio/st3/na.py test

'''
import sys
import os

user_script_paths = [
    'I:/core/new',
    'I:/ncc',
    'I:/ncc/nccbot',
    'I:/ncc/nccbot/md_core',
    'I:/ncc/nccbot/ncc_core',
    '/data/project/ncc',
    '/data/project/ncc/nccbot',
    '/data/project/ncc/nccbot/md_core',
    '/data/project/ncc/nccbot/ncc_core',
]
for _u_path in user_script_paths:
    if os.path.exists(_u_path):
        sys.path.append(os.path.abspath(_u_path))

from mass.radio.st3.start3 import ids_by_caseId, main

# ---
print('ids_by_caseId: ', len(ids_by_caseId))
# ---
main(ids_by_caseId)
