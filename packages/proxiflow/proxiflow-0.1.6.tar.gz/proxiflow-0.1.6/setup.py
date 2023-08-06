# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['proxiflow', 'proxiflow.config', 'proxiflow.core', 'proxiflow.utils']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.1.3,<9.0.0',
 'numpy>=1.24.2,<2.0.0',
 'polars>=0.16.7,<0.17.0',
 'pyaml>=21.10.1,<22.0.0',
 'scipy>=1.10.1,<2.0.0']

setup_kwargs = {
    'name': 'proxiflow',
    'version': '0.1.6',
    'description': 'Data Preprocessing flow tool in python',
    'long_description': '[![PyPi version](https://badgen.net/pypi/v/proxiflow/)](https://pypi.org/project/proxiflow)\n[![Documentation Status](https://readthedocs.org/projects/proxiflow/badge/?version=latest)](https://proxiflow.readthedocs.io/en/latest/?badge=latest)\n[![PyPI download month](https://img.shields.io/pypi/dm/proxiflow.svg)](https://pypi.python.org/pypi/proxiflow/)\n[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/tomesm/proxiflow/graphs/commit-activity)\n[![PyPI license](https://img.shields.io/pypi/l/proxiflow.svg)](https://pypi.python.org/pypi/proxiflow/)\n[![tests](https://github.com/tomesm/proxiflow/actions/workflows/tests.yml/badge.svg)](https://github.com/tomesm/proxiflow/actions/workflows/tests.yml)\n\n\n# ProxiFlow\n\nProxiFlow is a data preprocessig tool for machine learning that performs\ndata cleaning, normalization, and feature engineering.\n\nThe biggest advantage if this library (which is basically a wrapper over [polars](https://github.com/pola-rs/polars) data frame) is that it is configurable via YAML configuration file which makes it suitable for MLOps pipelines or for building API requests over it.\n\n## Documentation\nRead the full documentation [here](http://proxiflow.readthedocs.io/).\n\n## Usage\n\nTo use ProxiFlow, install it via pip:\n\n``` bash\npip install proxiflow\n```\n\nYou can then call it from the command line:\n\n``` bash\nproxiflow --config-file myconfig.yaml --input-file mydata.csv --output-file cleaned_data.csv\n```\n\nHere\\\'s an example of a YAML configuration file:\n\n``` yaml\ninput_format: csv\noutput_format: csv\n\ndata_cleaning: #mandatory\n  # NOTE: Not handling missing values can cause errors during data normalization\n  handle_missing_values:\n    drop: false\n    mean: true # Only Int and Float columns are handled \n    # mode: true # Turned off for now. \n\n  handle_outliers: true # Only Float columns are handled\n  remove_duplicates: true\n\ndata_normalization: # mandatory\n  min_max: #mandatory but values are not mandatory. It can be left empty\n    # Specify columns:\n    - Age # not mandatory\n  z_score: \n    - Price \n  log:\n    - Floors\n\nfeature_engineering:\n  one_hot_encoding: # mandatory\n    - Bedrooms      # not mandatory\n\n  feature_scaling:  # mandatory\n    degree: 2       # not mandatory. It specifies the polynominal degree\n    columns:        # not mandatory\n      - Floors      # not mandatory\n```\n\nThe above configuration specifies that duplicate rows should be removed\nand missing values should be dropped.\n\n## API\n\nProxiFlow can also be used as a Python library. Here\\\'s an example:\n\n``` python\nimport polars as pl\nfrom proxiflow.config import Config\nfrom proxiflow.core import Cleaner\n\n# Load the data\ndf = pl.read_csv("mydata.csv")\n\n# Load the configuration\nconfig = Config("myconfig.yaml")\n\n# Clean the data\ncleaner = Cleaner(config)\ncleaned_data = cleaner.clean_data(data)\n\n# Perform data normalization\nnormalizer = Normalizer(config)\nnormalized_data = normalizer.normalize(cleaned_data)\n\n# Perform feature engineering\nengineer = Engineer(config)\nengineered_data = engineer.execute(normalized_data)\n\n# Write the output data\nengineered_data.write_csv("cleaned_data.csv")\n```\n\n## Log\n\n-   \\[x\\] Data cleaning\n-   \\[x\\] Data normalization\n-   \\[x\\] Feature engineering',
    'author': 'Martin Tomes',
    'author_email': 'tomesm@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<3.11',
}


setup(**setup_kwargs)
