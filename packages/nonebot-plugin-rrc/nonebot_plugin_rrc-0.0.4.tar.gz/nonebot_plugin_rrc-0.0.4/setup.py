import os
import setuptools
with open("README.md", "r", encoding="utf-8", errors="ignore") as f:
    long_description = f.read()
    setuptools.setup(
    name='nonebot_plugin_rrc',
    version='0.0.4',
    author='QingmuCat',
    author_email='1242550160@qq.com',
    url='https://github.com/QingMuCat/nonebot_plugin_rrc',
    description='''修仙插件''',
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Natural Language :: Chinese (Simplified)"
    ],
    include_package_data=True,
    platforms="any",
    install_requires=[
            'fastapi==0.89.1',
            'nonebot-adapter-onebot==2.2.1',
            'nonebot2==2.0.0rc3',
    ],
    )