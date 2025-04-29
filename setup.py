from setuptools import setup, find_packages

setup(
    name="text_classifier",
    version="0.1",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "fastapi",
        "uvicorn",
        "transformers",
        "torch",
        "pydantic"
    ],
    entry_points={
        "console_scripts": [
            "text-classifier-api=text_classifier.main:run"
        ]
    },
    include_package_data=True,
)
