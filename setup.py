import sys
from os import path
from setuptools import setup
from setuptools.extension import Extension

VERSION = "1.3.0"

WINDOWS_KWARGS = dict(
    include_dirs=(
        path.join('lib', 'windows', 'openexr-2.2', 'include'),
        path.join('lib', 'windows', 'zlib-1.2.3-lib', 'include')
    ),
    library_dirs=(
        path.join('lib', 'windows', 'openexr-2.2', 'lib'),
        path.join('lib', 'windows', 'zlib-1.2.3-lib', 'lib')
    ),
    libraries=[
        'Half', 'Iex-2_2', 'Imath-2_2', 'IlmImf-2_2', 'IlmThread-2_2',
        'zlibstatic'
    ],
    extra_compile_args=['/DVERSION#\\"%s\\"' % VERSION]
)

LINUX_KWARGS = dict(
    include_dirs=(
        '/usr/include/OpenEXR',
        '/usr/local/include/OpenEXR',
        '/opt/local/include/OpenEXR'
    ),
    library_dirs=(
        '/usr/local/lib',
        '/opt/local/lib'
    ),
    libraries=['Iex', 'Half', 'Imath', 'IlmThread', 'IlmImf', 'z'],
    extra_compile_args=['-DVERSION="%s"' % VERSION]
)

MACOS_KWARGS = dict(
    include_dirs=(
        '/usr/include/OpenEXR',
        '/usr/local/include/OpenEXR',
        '/opt/local/include/OpenEXR'
    ),
    library_dirs=(
        './lib/macos/openexr-2.2/lib',
        '/usr/lib/',
    ),
    libraries=['Iex', 'Half', 'Imath', 'IlmThread', 'IlmImf', 'z'],
    extra_compile_args=['-DVERSION="%s"' % VERSION],
)


extension_kwargs = None
requirements = []

if sys.platform == 'win32':
    extension_kwargs = WINDOWS_KWARGS
elif sys.platform == 'darwin':
    extension_kwargs = MACOS_KWARGS
else:
    extension_kwargs = LINUX_KWARGS

    if sys.platform.startswith('linux'):
        requirements.append('auditwheel')  # for manylinux


setup(
    name='OpenEXR',
    version=VERSION,
    author='James Bowman',
    author_email='jamesb@excamera.com',
    url='http://www.excamera.com/sphinx/articles-openexr.html',
    description="Python bindings for ILM's OpenEXR image file format",
    long_description="Python bindings for ILM's OpenEXR image file format",
    install_requires=requirements,
    ext_modules=[
        Extension(
            'OpenEXR',
            ['OpenEXR.cpp'],
            **extension_kwargs
        )
    ],
    py_modules=['Imath'],
)
