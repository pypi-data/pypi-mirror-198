from setuptools import setup, find_namespace_packages

setup(
    name="t11p_h",
    version="1.0.0",
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
            "t11p_h\\GameGooseKiller\\font",
            ["t11p_h\\GameGooseKiller\\font\\UA Propisi.ttf"],
        ),
        (
            "t11p_h\\GameGooseKiller\\image",
            [
                "t11p_h\\GameGooseKiller\\image\\background.png",
                "t11p_h\\GameGooseKiller\\image\\bonus.png",
                "t11p_h\\GameGooseKiller\\image\\boom.png",
                "t11p_h\\GameGooseKiller\\image\\enemy.png",
                "t11p_h\\GameGooseKiller\\image\\Farm-Goose.ico",
                "t11p_h\\GameGooseKiller\\image\\gameover.png",
            ],
        ),
        (
            "t11p_h\\GameGooseKiller\\image\\background",
            [
                "t11p_h\\GameGooseKiller\\image\\background\\1-1.png",
                "t11p_h\\GameGooseKiller\\image\\background\\1-2.png",
                "t11p_h\\GameGooseKiller\\image\\background\\1-3.png",
            ],
        ),
        (
            "t11p_h\\GameGooseKiller\\image\Goose",
            [
                "t11p_h\\GameGooseKiller\\image\\Goose\\1-1.png",
                "t11p_h\\GameGooseKiller\\image\\Goose\\1-2.png",
                "t11p_h\\GameGooseKiller\\image\\Goose\\1-3.png",
                "t11p_h\\GameGooseKiller\\image\\Goose\\1-4.png",
                "t11p_h\\GameGooseKiller\\image\\Goose\\1-5.png",
            ],
        ),
    ],
    include_package_data=True,
    include_dirs=True,
    install_requires=["pygame", "prettytable", "prompt-toolkit"],
    entry_points={
        "console_scripts": ["powerhouse-helper=t11p_h.main:run"]
    },
)