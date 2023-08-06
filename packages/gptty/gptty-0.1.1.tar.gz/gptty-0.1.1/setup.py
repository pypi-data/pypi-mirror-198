from setuptools import setup, find_packages

with open("README.md", 'r') as f:
    long_description = f.read()

setup(
    name='gptty',
    version='0.1.1',
    description=' Chat GPT wrapper in your TTY ',
    author='Sig Janoska-Bedi',
    author_email='signe@atreeus.com',
    long_description=long_description, 
    long_description_content_type='text/markdown',
    url="https://github.com/signebedi/gptty",
    packages=find_packages(),
    install_requires=[
        'click',
        'pandas',
        'openai'
    ],
    entry_points={
        'console_scripts': [
            'gptty=gptty.__main__:main',
        ],
    },
    python_requires='>=3.8',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent'
    ]
)