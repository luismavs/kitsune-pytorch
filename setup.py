from setuptools import find_namespace_packages
from setuptools import setup

setup(
    name="inw-kitsunetorch",
    version="0.2.12",
    description="Kitsune anomaly detection model implemented in PyTorch.",
    author="Guillem Orellana Trullols",
    author_email="guillem.orellana@gmail.com",
    maintainer="Luís Seabra",
    maintainer_email="luismavseabra@innowave.tech",
    packages=find_namespace_packages(include=["kitsune"]),
    python_requires="~=3.8",
    install_requires=[
        "typer",
        "torch",
        "torchdata",
        "pandas>=1.2",
        "scikit-learn>=0.24",
        "scipy~=1.8",
        "tqdm",
    ],
    zip_safe=False,
)
