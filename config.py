import os

HETS_EXECUTABLE = os.environ.get("HETS_EXECUTABLE")

if not HETS_EXECUTABLE:
    raise Exception('Please provide env variable HETS_EXECUTABLE')