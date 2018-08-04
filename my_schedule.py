#! /usr/bin/python

from scheduler import scheduler
from subprocess import call

# Run Terminal Command
def executePythonScript(script=''):
    if script:
        call(['python','/Users/me/' + script])

# run
if __name__ == '__main__':

    # Create a new scheduler
    scheduler = scheduler()

    # Define our scheduler commands:
    scheduler.at('03:00').do(executePythonScript, script='nightly_backup.py')
    scheduler.at('04:00').do(executePythonScript, script='master_duplicate.py')
    scheduler.every(5).minutes().do(executePythonScript, script='dropbox_cleanup.py')

# eof