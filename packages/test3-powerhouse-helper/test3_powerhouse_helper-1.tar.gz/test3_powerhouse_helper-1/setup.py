from setuptools import setup, find_namespace_packages

setup(
    name="test3_powerhouse_helper",
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
    packages=find_namespace_packages(),
    data_files=[
        (
            "test_powerhouse_helper\\AddressBook\\address_saves",
            [
                "test_powerhouse_helper\\AddressBook\\address_saves\\address_book_auto_save.bin",
                "test_powerhouse_helper\\AddressBook\\address_saves\\address_book.log",
            ],
        ),
        (
            "test_powerhouse_helper\\NoteBook\\note_saves",
            [
                "test_powerhouse_helper\\NoteBook\\note_saves\\note_book_auto_save.bin",
                "test_powerhouse_helper\\NoteBook\\note_saves\\note_book.log",
            ],
        ),
        (
            "test_powerhouse_helper\\GameGooseKiller\\font",
            ["test_powerhouse_helper\\GameGooseKiller\\font\\UA Propisi.ttf"],
        ),
        (
            "test_powerhouse_helper\\GameGooseKiller\\image",
            [
                "test_powerhouse_helper\\GameGooseKiller\\image\\background.png",
                "test_powerhouse_helper\\GameGooseKiller\\image\\bonus.png",
                "test_powerhouse_helper\\GameGooseKiller\\image\\boom.png",
                "test_powerhouse_helper\\GameGooseKiller\\image\\enemy.png",
                "test_powerhouse_helper\\GameGooseKiller\\image\\Farm-Goose.ico",
                "test_powerhouse_helper\\GameGooseKiller\\image\\gameover.png",
            ],
        ),
        (
            "test_powerhouse_helper\\GameGooseKiller\\image\\background",
            [
                "test_powerhouse_helper\\GameGooseKiller\\image\\background\\1-1.png",
                "test_powerhouse_helper\\GameGooseKiller\\image\\background\\1-2.png",
                "test_powerhouse_helper\\GameGooseKiller\\image\\background\\1-3.png",
            ],
        ),
        (
            "test_powerhouse_helper\\GameGooseKiller\\image\Goose",
            [
                "test_powerhouse_helper\\GameGooseKiller\\image\\Goose\\1-1.png",
                "test_powerhouse_helper\\GameGooseKiller\\image\\Goose\\1-2.png",
                "test_powerhouse_helper\\GameGooseKiller\\image\\Goose\\1-3.png",
                "test_powerhouse_helper\\GameGooseKiller\\image\\Goose\\1-4.png",
                "test_powerhouse_helper\\GameGooseKiller\\image\\Goose\\1-5.png",
            ],
        ),
    ],
    include_package_data=True,
    include_dirs=True,
    install_requires=["pygame", "prettytable", "prompt-toolkit"],
    entry_points={
        "console_scripts": ["powerhouse-helper=test_powerhouse_helper.main:run"]
    },
)