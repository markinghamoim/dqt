from setuptools import setup, find_packages
import os

# Read requirements from requirements.txt
def read_requirements():
    req_path = os.path.join(os.path.dirname(__file__), 'requirements.txt')
    if os.path.exists(req_path):
        with open(req_path, 'r') as f:
            return [line.strip() for line in f if line.strip() and not line.startswith('#')]
    return []

setup(
    name='pydqt',
    version='1.4.1',  # Update this to match your package version
    description='Python Data Query Tool',
    long_description='A project which aides in querying of both local and cloud based relational, tabular data.',
    author='Your Name',  # Update with your name
    author_email='your.email@example.com',  # Update with your email
    url='https://github.com/markinghamoim/dqt',
    packages=find_packages(),
    install_requires=read_requirements(),
    python_requires='>=3.8',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
    ],
)

