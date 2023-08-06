from setuptools import setup, find_packages

def readme():
    with open('README.md') as f:
        return f.read()


entry_points = '''
[pygments.lexers]
барвінок=pygments_periwinkle_lexer:PeriwinkleLexer
'''

setup(
    name='pygments-periwinkle-lexer',
    version='0.0.2',
    description='Лексер для Барвінку.',
    long_description=readme(),
    author='Федуняк Роман',
    author_email='fedynuak.roma@gmail.com',
    url='https://github.com/periwinkle-lang',
    packages=find_packages(),
    entry_points=entry_points,
    install_requires=[
        'Pygments>=2.14.0'
    ],
    license='MIT License',
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Natural Language :: Ukrainian",
        "Programming Language :: Python :: 3 :: Only",
        "Environment :: Plugins",
    ],
)
