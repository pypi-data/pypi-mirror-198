from setuptools import find_packages, setup

setup(
    name='Hello-World-Pini',
    packages=find_packages(),
    version='1.0.0',
    description='Esse pacote tem uma função que imprime a string Hello world',
    long_description='Esse pacote tem uma função que imprime a string Hello world...',
    author='Mateus',
    author_email='mateusfeitosa.olivi@gmail.com',
    license='MIT',
    keywords=['dev', 'web'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ],
)

# twine upload --username MateusOlivi dist/Hello-World-1.0.0.tar.gz dist/Hello_World-1.0.0-py3-none-any.whl
