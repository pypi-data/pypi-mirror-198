"""
mblog: a minimal markdown blog
"""
from __future__ import print_function

__VERSION__ = '1.7.0'

# pylint: disable=W
# pylint: disable=missing-docstring
try:

    import logging
    import sys

    import waitress

    from mblog.config import HOST, IP, PORT, URL, THREADS, DEBUG, USER

    from mblog.config import app
    from mblog.models import createDatabases
    from mblog.util import startBrowser
    from mblog.routes import *

except ImportError as importError:
    print("All dependencies aren't installed. \n Error: {} \n Run: $ pip install -r requirements.txt".format(
        str(importError)), file=sys.stderr)
    exit(1)


def startBlog():
    logging.basicConfig(level=logging.INFO)

    createDatabases()
    startBrowser(URL)

    try:
        if not DEBUG:
            waitress.serve(app, host=IP, port=PORT, threads=THREADS)
        else:
            app.run(host=IP, port=PORT, debug=DEBUG)
    except:
       app.run(host=IP, port=PORT, debug=DEBUG)
