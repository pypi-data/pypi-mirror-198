from setuptools import setup, find_packages


setup(
    name="TeamQuiz",
    version="0.0.4-alpha",
    author="Dawood",
    description="A simple quiz program",
    packages=find_packages(),
    install_requires=["requests"],
    url='https://github.com/DawoodLaiq/competition_api',
    entry_points={
        "console_scripts": [
            "TeamQuiz = TeamQuiz.TeamQuiz:TeamQuiz",
        ]
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)