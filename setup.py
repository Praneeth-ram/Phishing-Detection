from setuptools import setup, find_packages

setup(
    name="phishing_detection",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "scikit-learn",
        "xgboost"
    ],
    description="A local package for phishing URL detection using XGBoost.",
    author="Your Name",
    license="MIT"
)
