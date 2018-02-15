import sys
import datetime
import subprocess

if __name__ == '__main__':
    tag = datetime.datetime.utcnow().strftime("%Y-%m-%d-%H%M")

    sys.exit(subprocess.call(["git", "tag", tag]))
