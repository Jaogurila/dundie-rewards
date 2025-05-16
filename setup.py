from setuptools import setup, find_packages

setup(
    name="dundiegur",
    version="0.1.0",
    description="Recompensa de pontos, bonus para funcionarios da empresa.",
    author="João Gurzilo",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "dundiegur = dundie.__main__:main"
        ]
    }      
)
