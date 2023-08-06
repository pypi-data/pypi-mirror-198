import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="vpscli",
    version="0.3.15",
    author="slipper",
    author_email="r2fscg@gmail.com",
    description="VPS manager",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/",
    packages=setuptools.find_packages(),
    package_data={
        setuptools.find_packages()[0]:
        ['data/*.txt', 'data/cauth', 'data/gost.sh']
    },
    install_requires=[
        'endlessh', 'redis', 'loguru', 'knivesout', 'pandas', 'pymysql', 'codefast', 'joblib', 'psutil', 'argparse',
        'uuidentifier', 'aiohttp', 'aiomysql', 'aioredis', 'aiofile', 'rich', 'matplotlib'
    ],
    entry_points={
        'console_scripts': [
            'vpsinit=vps.__init__:main',
            'vpspanel=vps.client:client',
            'vpsstatus=vps.status:status',
            'sysstat=vps.apps.sysstat:api',
            'sss=vps.apps.sysstat:api',
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
