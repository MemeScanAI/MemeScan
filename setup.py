from setuptools import setup, find_packages

setup(
    name='memescan',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'requests',
        'numpy',
        'pandas',
        'solana',
        'web3',
        'tensorflow',  # or 'torch' depending on the AI model you use
    ],
    description='AI-powered Solana Memecoin Scanner',
    author='Your Name',
    author_email='your.email@example.com',
    url='https://github.com/yourusername/memescan',
)
