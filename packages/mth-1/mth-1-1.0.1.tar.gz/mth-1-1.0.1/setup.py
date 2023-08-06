from setuptools import setup, find_packages

setup(
    name="mth-1",
    version="1.0.1",
    description="mth-1",
    author="Python Powerhouse",
    license="MIT",
    url="https://github.com/NovykovDaniil/python-core-project",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(),
    include_package_data=True,
    # include_dirs=True,
    install_requires=["prettytable", "prompt-toolkit", 'pygame'],
    data_files=[
        (
            r"test_version_powerhouse_helper\GameGooseKiller\font",
            [r"test_version_powerhouse_helper\GameGooseKiller\font\UA Propisi.ttf"],
        ),
        (
            r"test_version_powerhouse_helper\GameGooseKiller\image",
            [
                r"test_version_powerhouse_helper\GameGooseKiller\image\background.png",
                r"test_version_powerhouse_helper\GameGooseKiller\image\bonus.png",
                r"test_version_powerhouse_helper\GameGooseKiller\image\boom.png",
                r"test_version_powerhouse_helper\GameGooseKiller\image\enemy.png",
                r"test_version_powerhouse_helper\GameGooseKiller\image\Farm-Goose.ico",
                r"test_version_powerhouse_helper\GameGooseKiller\image\gameover.png",
            ],
        ),
        (
            r"test_version_powerhouse_helper\GameGooseKiller\image\background",
            [
                r"test_version_powerhouse_helper\GameGooseKiller\image\background\1-1.png",
                r"test_version_powerhouse_helper\GameGooseKiller\image\background\1-2.png",
                r"test_version_powerhouse_helper\GameGooseKiller\image\background\1-3.png",
            ],
        ),
        (
            r"test_version_powerhouse_helper\GameGooseKiller\image\Goose",
            [
                r"test_version_powerhouse_helper\GameGooseKiller\image\Goose\1-1.png",
                r"test_version_powerhouse_helper\GameGooseKiller\image\Goose\1-2.png",
                r"test_version_powerhouse_helper\GameGooseKiller\image\Goose\1-3.png",
                r"test_version_powerhouse_helper\GameGooseKiller\image\Goose\1-4.png",
                r"test_version_powerhouse_helper\GameGooseKiller\image\Goose\1-5.png",
            ],
        ),
        (r'test_version_powerhouse_helper\GameGooseKiller', [r'test_version_powerhouse_helper\GameGooseKiller\Game_goose.py'])
    ],
    entry_points={
        "console_scripts": ["mth=test_version_powerhouse_helper.main:run"]
    },
)
