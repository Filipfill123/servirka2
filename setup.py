import setuptools
import os

kwargs = {}

if os.path.isfile("requirements.txt"):
    with open('requirements.txt') as f:
        kwargs["install_requires"] = f.read().splitlines()

setuptools.setup(
    name="Servirka Karel",
    version="1.0",
    author="Jan Švec",
    author_email="honzas@ntis.zcu.cz",
    description="Example dialog manager for SpeechCloud platform",
    url="https://github.com/honzas83/speechcloud-servirka",
    data_files=[("static", ["index.html"])],
    py_modules=["servirka"],
    python_requires='>=3.7',
    **kwargs
)
