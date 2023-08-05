"""Module metadata"""
from setuptools import setup
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding="utf8")
setup(
    name='randomlib',
    version='4.5',
    author='Random',
    author_email='random.randomlib@gmail.com',
    description='An NLP Library for Marathi Language',
    url='https://github.com/l3cube-pune/MarathiNLP.git',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    packages=['randomlib','randomlib.autocomplete', 'randomlib.datasets', 'randomlib.hate',
              'randomlib.mask_fill', 'randomlib.model_repo', 'randomlib.preprocess', 'randomlib.sentiment',
              'randomlib.similarity', 'randomlib.tagger', 'randomlib.tokenizer'],
    include_package_data=True,
    install_requires=['importlib_resources','huggingface_hub==0.11.1','tqdm','pandas',
                      'sentence_transformers','transformers','numpy','torch','IPython'], #'openpyxl'
    license='MIT',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
