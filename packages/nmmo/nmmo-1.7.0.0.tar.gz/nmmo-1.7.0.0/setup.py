from itertools import chain

from setuptools import find_packages, setup

REPO_URL = "https://github.com/neuralmmo/environment"

extra = {
    'docs': [
        'sphinx-rtd-theme==0.5.1',
        'sphinxcontrib-youtube==1.0.1',
        ],
    'cleanrl': [
        'wandb==0.12.9',
        'supersuit==3.3.5',
        'tensorboard',
        'torch',
        'openskill',
        ],
    }

extra['all'] = list(set(chain.from_iterable(extra.values())))
 
setup(
    name="nmmo",
    description="Neural MMO is a platform for multiagent intelligence research inspired by "
    "Massively Multiplayer Online (MMO) role-playing games. Documentation hosted at neuralmmo.github.io.",
    long_description_content_type="text/markdown",
    version=open('nmmo/version.py').read().split()[-1].strip("'"),
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'pytest<7',
        'pytest-pythonpath==0.7.4',
        'pytest-benchmark==3.4.1',
        'openskill==4.0.0',
        'fire==0.4.0',
        'setproctitle==1.1.10',
        'service-identity==21.1.0',
        'autobahn==19.3.3',
        'Twisted==19.2.0',
        'vec-noise==1.1.4',
        'imageio==2.23.0',
        'tqdm==4.61.1',
        'lz4==4.0.0',
        'h5py==3.7.0',
        'ordered-set==4.1.0',
        'pettingzoo==1.19.0',
        'gym==0.23.0',
        'pylint==2.16.0',
        'py==1.11.0',
        'scipy==1.10.0',
        'numpy==1.23.3',
        'numpy-indexed==0.3.7'
    ],
    extras_require=extra,
    python_requires=">=3.7",
    license="MIT",
    author="Joseph Suarez",
    author_email="jsuarez@mit.edu",
    url=REPO_URL,
    keywords=["Neural MMO", "MMO"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Developers",
        "Environment :: Console",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.9",
    ],
)

