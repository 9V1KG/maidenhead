from setuptools import setup

requirements = "openlocationcode"
setup(
    name="Maiden",
    version="0.0a0",
    packages=["Maiden"],
    url="https://github.com/9V1KG/maidenhead",
    license="Please check with author",
    author="9V1KG",
    author_email="drklaus@bpmsg.com",
    install_requires=requirements,
    extras_require={
        'dev': [
            'pylint'
            'pytest',
            'pytest-pep8',
            'pytest-cov',
            'sphinx',
            'recommonmark',
            'black',
            'pylint'
        ]},
    description="Maidenhead locator functions",
)