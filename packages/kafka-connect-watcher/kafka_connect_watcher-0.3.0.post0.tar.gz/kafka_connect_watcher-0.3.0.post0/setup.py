# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['kafka_connect_watcher', 'kafka_connect_watcher.aws_sns']

package_data = \
{'': ['*']}

install_requires = \
['aws-embedded-metrics>=3.0.0,<4.0.0',
 'compose-x-common>=1.2,<2.0',
 'importlib-resources>=5.10,<6.0',
 'jinja2>=3.1.2,<4.0.0',
 'jsonschema>=4.17.3,<5.0.0',
 'kafka-connect-api>=0.5.3,<0.6.0',
 'prometheus-client>=0.16,<0.17',
 'pyyaml>=6.0,<7.0']

entry_points = \
{'console_scripts': ['kafka-connect-watcher = '
                     'kafka_connect_watcher.cli:start_watcher',
                     'kafka_connect_watcher = '
                     'kafka_connect_watcher.cli:start_watcher']}

setup_kwargs = {
    'name': 'kafka-connect-watcher',
    'version': '0.3.0.post0',
    'description': 'Kafka Connect active watcher',
    'long_description': '\n===========================================\nKafka Connect Watcher\n===========================================\n\nService that will actively probe and monitor your Kafka connect clusters using the Connect API.\nIt can report metrics to AWS CloudWatch (Prometheus coming) using `AWS EMF`_ to allow creating alerts\nand alarms.\n\nFeatures\n=========\n\n* Scan multiple clusters at once\n* Implement different remediation rules\n* Include/Exclude lists for connectors to evaluate/ignore\n\nRoadmap\n=========\n\n* Prometheus support\n* Multiple channels of alerts (i.e. webhooks)\n\n\nSystems recommendations\n------------------------------\n\nWhen using multiple clusters, we recommend to provide multiple CPUs to the service as it\nhas multi-threading enabled, allowing for parallel processing of clusters & their respective connectors.\n\n\n.. _AWS EMF: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Embedded_Metric_Format_Specification.html\n',
    'author': 'John "Preston" Mille',
    'author_email': 'john@ews-network.net',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
