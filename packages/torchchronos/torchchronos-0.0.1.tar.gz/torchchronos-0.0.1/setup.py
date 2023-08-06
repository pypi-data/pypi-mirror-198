# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['torchchronos',
 'torchchronos.datasets',
 'torchchronos.lightning',
 'torchchronos.transforms']

package_data = \
{'': ['*']}

install_requires = \
['fastapi>=0.88.0,<0.89.0',
 'lightning>=2.0.0,<3.0.0',
 'sktime>=0.16.1,<0.17.0',
 'torch>=2.0.0,<3.0.0']

setup_kwargs = {
    'name': 'torchchronos',
    'version': '0.0.1',
    'description': 'PyTorch and Lightning compatible library that provides easy and flexible access to various time-series datasets for classification and regression tasks',
    'long_description': '# torchchronos\n**torchchronos* is an experimental PyTorch and Lightning compatible library that provides easy and flexible access to various time-series datasets for classification and regression tasks. It also provides a simple and extensible transform API to preprocess data.\nIt is inspired by the much more complex [torchtime](https://github.com/philipdarke/torchtime).\n\n## Installation\nYou can install torchchronos via pip:\n\n`pip install torchchronos`\n\n## Usage\n### Datasets\ntorchchronos currently provides access to several popular time-series datasets, including:\n\n- UCR/UEA Time Series Classification Repository\n\nTo use a dataset, you can simply import the corresponding dataset class and create an instance:\n\n```python\nfrom torchchronos.datasets import UCRUEADataset\nfrom torchchronos.transforms import PadFront\n\ndataset = UCRUEADataset(\'ECG5000\',path=Path(".cache/data"), transforms=PadFront(10))\n```\n\n### Data Modules\ntorchchronos also provides a multi gpu Lightning compatible DataModules to make it easy to load and preprocess data. For example:\n\n```python\nfrom torchchronos.lightning import UCRUEAModule\nfrom torchchronos.transforms import PadFront\n\nmodule = UCRUEAModule(\'ECG5000\', split_ratio= (0.75, 0.15), batch_size= 32) transforms=Compose([PadFront(10), PadBack(10)]))\n```\n\n### Transforms\ntorchchronos provides a flexible transform API to preprocess time-series data. For example, to normalize a dataset, you can define a transform like this:\n\n```python\nfrom torchchronos.transforms import Transform\n\nclass Normalize(Transform):\n    def __init__(self, mean=None, std=None):\n        self.mean = mean\n        self.std = std\n\n    def fit(self, data):\n        self.mean = data.mean()\n        self.std = data.std()\n\n    def transform(self, data):\n        return (data - self.mean) / self.std\n```\n\n## Roadmap\nThe following features are planned for future releases of torchchronos:\n\nSupport for additional time-series datasets, including:\n- Energy consumption dataset\n- Traffic dataset\n- PhysioNet Challenge 2012 (in-hospital mortality)\n- PhysioNet Challenge 2019 (sepsis prediction) datasets\nAdditional transform classes, including:\n- Resampling\n- Missing value imputation\n\nIf you have any feature requests or suggestions, please open an issue on our GitHub page.',
    'author': 'Maurice Kraus',
    'author_email': 'dev@mkraus.io',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<3.12',
}


setup(**setup_kwargs)
