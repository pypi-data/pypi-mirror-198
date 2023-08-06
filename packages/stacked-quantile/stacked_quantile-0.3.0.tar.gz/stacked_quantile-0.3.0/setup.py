# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['stacked_quantile']

package_data = \
{'': ['*']}

install_requires = \
['numpy>=1.24.1,<2.0.0']

setup_kwargs = {
    'name': 'stacked-quantile',
    'version': '0.3.0',
    'description': '',
    'long_description': '# stacked_quantile\n\n\'Stacked\' quantile functions. Close to weighted quantile functions.\n\nThese functions are used to calculate quantiles of a set of values, where each value\nhas a weight. The typical process for calculating a weighted quantile is to create a\nCDF from the weights, then interpolate the values to find the quantile.\n\nThese functions, however, treat weighted values (given integer weights) exactly as\nmultiple values.\n\nSo, values `(1, 2, 3)` with weights `(4, 5, 6)` will be treated as\n\n```\n(1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3)\n```\n\nIf the quantile falls exactly between\ntwo values, the non-weighted average of the two values is returned. This is\nconsistent with the "weights as occurrences" interpretation. Strips all zero-weight\nvalues, so these will never be included in such averages.\n\nIf using non-integer weights, the results will be as if some scalar were applied to\nmake all weights into integers.\n\nThis "weights as occurrences" interpretation has two pitfalls:\n\n1.  Identical values will be returned for different quantiles (e.g., the results\n    for quantiles == 0.5, 0.6, and 0.7 might be identical). The effect of this is\n    that some some common data practices like "robust scalar" will *not* be\n    robust because of the potential for a 0 interquartile range. Again this is\n    consistent, because the same thing could happen with repeated, non-weighted\n    values.\n\n2.  With any number of values, the stacked_median could still be the first or\n    last value (if it has enough weight), so separating by the median is not\n    robust. This could also happen with repeaded, non-weighted values. One\n    workaround is to divide the values into group_a = values strictly < median,\n    group_b = values strictly > median, then add == median to the smaller group.\n\n\nwhere `FPArray: TypeAlias = npt.NDArray[np.floating[Any]]`\n\n\n``` python\ndef get_stacked_quantile(values: FParray, weights: FPArray, quantile: float) -> float:\n    """Get a weighted quantile for a vector of values.\n\n    :param values: array of values with shape (n,)\n    :param weights: array of weights where weights.shape == values.shape\n    :param quantile: quantile to calculate, in [0, 1]\n    :return: weighted quantile of values\n    :raises ValueError: if values and weights do not have the same length\n    :raises ValueError: if quantile is not in interval [0, 1]\n    :raises ValueError: if values array is empty (after removing zero-weight values)\n    :raises ValueError: if weights are not all positive\n    """\n```\n\n``` python\ndef get_stacked_quantiles(\n    values: FPArray, weights: FPArray, quantile: float\n) -> FPArray:\n    """Get a weighted quantile for an array of vectors.\n\n    :param values: array of vectors with shape (..., m)\n        will return one m-length vector\n    :param weights: array of weights with shape (..., 1)\n        where shape[:-1] == values.shape[:-1]\n    :param quantile: quantile to calculate, in [0, 1]\n    :return: axiswise weighted quantile of an m-length vector\n    :raises ValueError: if values and weights do not have the same shape[:-1]\n\n    The "gotcha" here is that the weights must be passed as 1D vectors, not scalars.\n    """\n```\n\n``` python\ndef get_stacked_median(values: FPArray, weights: FPArray) -> float:\n    """Get a weighted median for a value.\n\n    :param values: array of values with shape (n,)\n    :param weights: array of weights where weights.shape == values.shape\n    :return: weighted median of values\n    :raises ValueError: if values and weights do not have the same length\n    :raises ValueError: if values array is empty (after removing zero-weight values)\n    :raises ValueError: if weights are not all positive\n    """\n```\n\n``` python\ndef get_stacked_medians(values: FPArray, weights: FPArray) -> FPArray:\n    """Get a weighted median for an array of vectors.\n\n    :param values: array of vectors with shape (..., m)\n        will return one m-length vector\n    :param weights: array of weights with shape (..., 1)\n        where shape[:-1] == values.shape[:-1]\n    :return: axiswise weighted median of an m-length vector\n    :raises ValueError: if values and weights do not have the same shape[:-1]\n\n    The "gotcha" here is that the weights must be passed as 1D vectors, not scalars.\n    """\n```\n\n',
    'author': 'Shay Hill',
    'author_email': 'shay_public@hotmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
