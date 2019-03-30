
import subprocess
import sys

def pg_dump(url):
    try:

        return subprocess.Popen(['pg_dump',url], stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    except OSError:
        sys.exit(1)

def dump_file_name(url,timestamp=None):
    filename = url.split('/')[-1]

    if timestamp:
        return  f"{filename}-{timestamp}.sql"

    else:
        return f"{filename}.sql"

