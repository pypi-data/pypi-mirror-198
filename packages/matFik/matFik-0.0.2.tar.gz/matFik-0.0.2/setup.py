from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience  :: Education',
    'Operating System :: Microsoft :: Windows :: Windows 10',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
]

setup(
    name='matFik',
    version='0.0.2',
    description='Matrix Function',
    long_description=open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
    url='',
    author='Fikri Kamaluddin',
    author_email='fikrikamaluddin07@gmail.com',
    license='MIT',
    classifiers=[],
    keywords='matrix',
    packages=find_packages(),
    install_required=['']
)