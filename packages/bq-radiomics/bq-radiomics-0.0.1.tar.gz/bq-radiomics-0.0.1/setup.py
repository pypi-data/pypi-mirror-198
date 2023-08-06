# coding: utf-8

from setuptools import setup, find_packages
from pathlib import Path

# Get __verison_dunder without importing BQ_radiomics
version_file = Path(__file__).resolve().parent / 'BQ_radiomics' / 'version.py'
exec(open(version_file).read())


setup(
    name='bq-radiomics',
    download_url=f'https://github.com/dorkylever/BQ_radiomics/archive/refs/tags/0.0.1.tar.gz',
    version="0.0.1",
    packages=find_packages(exclude=("dev")),
    package_data={},  # Puts it in the wheel dist. MANIFEST.in gets it in source dist
    include_package_data=True,
    install_requires=[
        'appdirs',
        'setuptools==59.8.0',
        'matplotlib>=2.2.0',
        'numpy==1.21.5',
        'pandas>=1.1.0',
        'scikit-learn==1.0.2',
        'scipy>=1.1.0',
        'scikit-image==0.17.2',
        'seaborn>=0.9.0',
        'PyYAML>=3.13',
        'catboost==1.1.0',
        'SimpleITK>=2.1.0',
        'pyradiomics>=3.0.1',
        'threadpoolctl==3.1.0',
        'imbalanced-learn==0.9.0',
        'raster-geometry',
        'filelock',
        'psutil==5.9.3',
        'plotly',
        'logzero==1.7.0',
        'addict',
        'toml',
        'pynrrd',
        'pytest',
        'tqdm',
        'gitpython',
        'pacmap',
        'shap',
        'joblib',
        'wheel',
        'numexpr',
        'bottleneck',
        'cuda-python==11.8.1'
    ],
    extras_require={},
    url='https://github.com/dorkylever/BQ_radiomics',
    license='',
    author='Kyle Drover',
    author_email='kyle.drover@anu.edu.au',
    description='Perform Radiomics Feature Extraction and Machine Learning',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
     ],
    keywords=['radiomics'],
    entry_points ={
            'console_scripts': [
                'BQ_radiomics_reg=BQ_radiomics.scripts.BQ_radiomics_reg:main',
                'BQ_radiomics_get_test_data=BQ_radiomics.scripts.BQ_radiomics_get_test_data:main',
                'BQ_radiomics_get_walkthrough_data=BQ_radiomics.scripts.BQ_radiomics_get_walkthrough_data:main',
                'BQ_radiomics_job_runner=BQ_radiomics.scripts.BQ_radiomics_job_runner:main',
                'BQ_radiomics_permutation_stats=BQ_radiomics.scripts.BQ_radiomics_permutation_stats:main',
                'BQ_radiomics_stats=BQ_radiomics.scripts.BQ_radiomics_stats:main',
                'BQ_radiomics_pad_volumes=BQ_radiomics.utilities.BQ_radiomics_pad_volumes:main',
                'BQ_radiomics_convert_16_to_8=BQ_radiomics.utilities.BQ_radiomics_convert_16_to_8:main',
                'BQ_radiomics_img_info=BQ_radiomics.utilities.BQ_radiomics_img_info:main',
                'BQ_radiomics_ark_imp_pro=BQ_radiomics.scripts.BQ_radiomics_ark_img_pro:main',
                'BQ_radiomics_radiomics_runner=BQ_radiomics.scripts.BQ_radiomics_radiomics_runner:main',
                'BQ_radiomics_two_way_plotter=BQ_radiomics.scripts.two_way_plotter:main',
                'BQ_radiomics_machine_learning=BQ_radiomics.scripts.BQ_radiomics_machine_learning:main'
            ]
        },
)
