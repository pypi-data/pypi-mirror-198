from setuptools import setup, find_packages

setup(
    name='rt_ppiscs',
    version='1.0.1',    
    description='Real-time simulations of ADF STEM probe position-integrated scattering cross-sections for single element fcc crystals in zone axis orientation using a densely connected neural network',
    url='https://github.com/Ivanlh20/rt_ppiscs',
    author='Ivan Lobato',
    author_email='ivanlh20@gmail.com',
    license='GPLv3',
    packages=find_packages(exclude=['test_exclude.py']),
    install_requires=['numpy', 'scipy'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    include_package_data=True,
    package_data={'': ['coef_scs_fcc.mat']},
)