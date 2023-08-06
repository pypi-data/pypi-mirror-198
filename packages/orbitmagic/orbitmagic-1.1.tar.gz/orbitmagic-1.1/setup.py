from distutils.core import setup, Extension

orbitmagic_module = Extension('orbitmagic', sources=['orbitmagic.c'])
long_description = open('README.md').read()

setup(
    name='orbitmagic',
    version='1.1',
    author='JeongHan-Bae',
    author_email='mastropseudo@gmail.com',
    description='for helping magiciens',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/JeongHan-Bae/orbitmagic',
    ext_modules=[orbitmagic_module],
    license='MIT',
    package_data={'orbitmagic': ['LICENSE.txt', 'README.md']},
    data_files=[('share/doc/orbitmagic', ['LICENSE.txt']),('share/doc/orbitmagic', ['README.md'])]
)
