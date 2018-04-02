import time
from contextlib import contextmanager


@contextmanager
def timethis(label):
    start = time.time()
    try:
        yield
    finally:
        end = time.time()
        print('%s: %0.3f' % (label, end-start))


import tempfile
import shutil

@contextmanager
def tempdir():
    outdir = tempfile.mkdtemp()
    try:
        yield outdir
    finally:
        shutil.rmtree(outdir)

