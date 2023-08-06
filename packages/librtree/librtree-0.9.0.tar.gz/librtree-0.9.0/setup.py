# I tried to set-up this package according to PEP 517, but that
# as yet can't handle the building of extensions [1] so we need
# to do that here, possibly that changes later.
#
# [1] https://stackoverflow.com/questions/66157987/

from setuptools import setup, Extension
from distutils.ccompiler import new_compiler
from distutils.sysconfig import customize_compiler
import subprocess
import os

# we do need to do some inspection of the host in order to configure
# the package (and ensure that we can compile it).  Setuptools does
# not have much support for that, I did have a look at scikit-make,
# but it depends on CMake, which is non-standard.  Instead we make a
# shellout to autoconf, which is properly POSIX portable.

def cc_path():
    cc = new_compiler()
    customize_compiler(cc)
    return cc.compiler[0]

env = os.environ
env['CC'] = cc_path()

subprocess.run(['./configure'], cwd='src', env=env)

# regular setup.py

setup_args = dict(
    ext_package = 'librtree',
    ext_modules = [
        Extension(
            'ext',
            [
                'src/librtree/lib/bindex.c',
                'src/librtree/lib/branch.c',
                'src/librtree/lib/branches.c',
                'src/librtree/lib/bsrt.c',
                'src/librtree/lib/csv.c',
                'src/librtree/lib/error.c',
                'src/librtree/lib/json.c',
                'src/librtree/lib/node.c',
                'src/librtree/lib/package.c',
                'src/librtree/lib/page.c',
                'src/librtree/lib/postscript.c',
                'src/librtree/lib/rect.c',
                'src/librtree/lib/rectf.c',
                'src/librtree/lib/rtree.c',
                'src/librtree/lib/search.c',
                'src/librtree/lib/split.c',
                'src/librtree/lib/spvol.c',
                'src/librtree/lib/state.c',
                'src/librtree/ext.c',
            ],
            include_dirs = ['src/librtree/lib'],
            libraries = ['jansson'],
            define_macros = [('HAVE_CONFIG_H', 1)]
        )
    ]
)

setup(**setup_args)
