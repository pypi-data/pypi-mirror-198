# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['deep_time_series', 'deep_time_series.model']

package_data = \
{'': ['*']}

install_requires = \
['lightning>=2.0.0,<3.0.0',
 'matplotlib>=3.7.1,<4.0.0',
 'numpy>=1.24.2,<2.0.0',
 'pandas>=1.5.3,<2.0.0',
 'rich>=13.3.2,<14.0.0',
 'scikit-learn>=1.2.2,<2.0.0',
 'torch>=2.0.0,<3.0.0',
 'torchaudio>=2.0.1,<3.0.0',
 'torchvision>=0.15.1,<0.16.0',
 'xarray>=2023.2.0,<2024.0.0']

setup_kwargs = {
    'name': 'deep-time-series',
    'version': '0.1.1',
    'description': 'Deep learning library for time series forecasting based on PyTorch.',
    'long_description': '# DeepTimeSeries\n\nLast update Oct.19, 2022\n\nDeep learning library for time series forecasting based on PyTorch.\nIt is under development and the first released version will be announced soon.\n\n## Why DeepTimeSeries?\n\nDeepTimeSeries is inspired by libraries such as ``Darts`` and\n``PyTorch Forecasting``. So why was DeepTimeSeries developed?\n\nThe design philosophy of DeepTimeSeries is as follows:\n\n**We present logical guidelines for designing various deep learning models for\ntime series forecasting**\n\nOur main target users are intermediate-level users who need to develop\ndeep learning models for time series prediction.\nWe provide solutions to many problems that deep learning modelers face\nbecause of the uniqueness of time series data.\n\nWe additionally implement a high-level API, which allows comparatively beginners\nto use models that have already been implemented.\n\n## Supported Models\n\n| Model       | Target features | Non-target features | Deterministic | Probabilistic |\n| ----------- | --------------- | ------------------- | ------------- | ------------- |\n| MLP         | o               | o                   | o             | o             |\n| Dilated CNN | o               | o                   | o             | o             |\n| Vanilla RNN | o               | o                   | o             | o             |\n| LSTM        | o               | o                   | o             | o             |\n| GRU         | o               | o                   | o             | o             |\n| Transformer | o               | o                   | o             | o             |\n\n## Documentation\n\nhttps://bet-lab.github.io/DeepTimeSeries/\n',
    'author': 'Sangwon',
    'author_email': 'lsw91.main@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
