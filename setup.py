import setuptools

with open('README.md', 'r') as f:
    long_description = f.read()

setuptools.setup(
    name='tfhubartifact',
    version='0.0.6',
    author='Mark Moloney',
    author_email='m4rkmo@gmail.com',
    description='BentoML artifact framework for TensorFlow Hub models',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/markmo/tfhubartifact',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    install_requires=[
        # 'BentoML==0.10.1',
        # 'tensorflow==2.0.0',
        # 'tensorflow-hub==0.5.0',
    ],
    python_requires='>=3.6',
)
