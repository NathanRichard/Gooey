"""
Util for talking to the client program in order to retrieve
dynamic defaults for the UI
"""
import json
import subprocess
import sys


def fetchDynamicProperties(target, encoding, force_stdio_encoding):
    """
    Sends a gooey-seed-ui request to the client program it retrieve
    dynamically generated defaults with which to seed the UI
    """
    cmd = '{} {}'.format(target, 'gooey-seed-ui --ignore-gooey')
    if force_stdio_encoding:
        sys.stdout.reconfigure(encoding=encoding)
        sys.stdin.reconfigure(encoding=encoding)
        sys.stderr.reconfigure(encoding=encoding)
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if proc.returncode != 0:
        out, _ = proc.communicate()
        return json.loads(out.decode(encoding))
    else:
        # TODO: useful feedback
        return {}

