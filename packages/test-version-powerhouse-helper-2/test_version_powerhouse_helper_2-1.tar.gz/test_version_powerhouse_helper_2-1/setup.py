from setuptools import setup, find_packages

setup(
    name="test_version_powerhouse_helper_2",
    version="1",
    description="This is your console assistant by Python Powerhouse",
    author="Python Powerhouse",
    license="MIT",
    url="https://github.com/NovykovDaniil/python-core-project",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(),
    data_files=[
        (
            "test_version_powerhouse_helper\\GameGooseKiller\\font",
            ["test_version_powerhouse_helper\\GameGooseKiller\\font\\UA Propisi.ttf"],
        ),
        (
            "test_version_powerhouse_helper\\GameGooseKiller\\image",
            [
                "test_version_powerhouse_helper\\GameGooseKiller\\image\\background.png",
                "test_version_powerhouse_helper\\GameGooseKiller\\image\\bonus.png",
                "test_version_powerhouse_helper\\GameGooseKiller\\image\\boom.png",
                "test_version_powerhouse_helper\\GameGooseKiller\\image\\enemy.png",
                "test_version_powerhouse_helper\\GameGooseKiller\\image\\Farm-Goose.ico",
                "test_version_powerhouse_helper\\GameGooseKiller\\image\\gameover.png",
            ],
        ),
        (
            "test_version_powerhouse_helper\\GameGooseKiller\\image\\background",
            [
                "test_version_powerhouse_helper\\GameGooseKiller\\image\\background\\1-1.png",
                "test_version_powerhouse_helper\\GameGooseKiller\\image\\background\\1-2.png",
                "test_version_powerhouse_helper\\GameGooseKiller\\image\\background\\1-3.png",
            ],
        ),
        (
            "test_version_powerhouse_helper\\GameGooseKiller\\image\Goose",
            [
                "test_version_powerhouse_helper\\GameGooseKiller\\image\\Goose\\1-1.png",
                "test_version_powerhouse_helper\\GameGooseKiller\\image\\Goose\\1-2.png",
                "test_version_powerhouse_helper\\GameGooseKiller\\image\\Goose\\1-3.png",
                "test_version_powerhouse_helper\\GameGooseKiller\\image\\Goose\\1-4.png",
                "test_version_powerhouse_helper\\GameGooseKiller\\image\\Goose\\1-5.png",
            ],
        ),
    ],
    include_package_data=True,
    include_dirs=True,
    install_requires=["pygame", "prettytable", "prompt-toolkit"],
    entry_points={
        "console_scripts": ["powerhouse-helper=test_version_powerhouse_helper.main:run"]
    },
)
