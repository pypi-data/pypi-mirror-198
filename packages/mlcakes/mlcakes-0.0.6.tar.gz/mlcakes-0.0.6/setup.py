from setuptools import setup, find_packages


install_packages = [
    'scikit-learn==1.2.2',
    'numpy==1.23.5',
    'matplotlib==3.6.2',
]
setup(
    name='mlcakes',
    version='0.0.6',
     python_requires=">=3.9.*",
    packages=find_packages(),
    
    install_requires=install_packages,
    
    # Metadata for PYPI
    author='Billy',
    author_email='liangbilin0324@163.com',
    description="Some functional modules for machine learning.",
    
    # data file
    include_package_data=False
)


