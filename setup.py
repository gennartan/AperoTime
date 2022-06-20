from setuptools import setup

setup(
        name='aperotime',
        version='1.0',
        description='Apero time api',
        author='Antoine Gennart',
        include_package_data=True,
        packages=['aperotime'],
        install_requires=[
            'anyio==3.6.1',
            'asgiref==3.5.2',
            'click==8.1.3',
            'fastapi==0.78.0',
            'h11==0.13.0',
            'idna==3.3',
            'pydantic==1.9.1',
            'sniffio==1.2.0',
            'starlette==0.19.1',
            'typing_extensions==4.2.0',
            'uvicorn==0.17.6'],
        entry_points={
            'console_scripts':['apero = aperotime.__main__:main'],
        },
    )


