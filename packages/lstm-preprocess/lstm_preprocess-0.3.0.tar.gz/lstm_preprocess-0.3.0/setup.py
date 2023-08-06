import setuptools

try:
    import pypandoc
    long_description = pypandoc.convert_file('README.md', 'rst')
except(IOError, ImportError):
    long_description = open('README.md').read()

setuptools.setup(
    name="lstm_preprocess",
    version="0.3.0",
    author="song111",
    author_email="clarksoyoung@sina.com",
    description="This package provides fundamental operation on reshaping dataframes for Keras LSTM input",
    long_description_content_type="text/markdown",
    long_description=long_description,
    url="https://github.com/ysong126/lstm_reshaper",
    project_urls={
        "Bug Tracker": "https://github.com/ysong126/lstm_reshaper",
    },
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
