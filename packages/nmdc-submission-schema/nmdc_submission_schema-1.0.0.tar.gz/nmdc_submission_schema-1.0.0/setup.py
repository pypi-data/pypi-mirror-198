# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['nmdc_submission_schema', 'nmdc_submission_schema.datamodel']

package_data = \
{'': ['*'], 'nmdc_submission_schema': ['schema/*']}

install_requires = \
['linkml-runtime>=1.4.9,<2.0.0']

setup_kwargs = {
    'name': 'nmdc-submission-schema',
    'version': '1.0.0',
    'description': 'The home of the NMDC submission schema. *Not* the home of sheets_and_friends. *Not* a GH pages host of NMDC DataHarmonizer interfaces.',
    'long_description': '# submission-schema\n\nThe home of the NMDC submission schema. *Not* the home of sheets_and_friends. *Not* a GH pages host of NMDC DataHarmonizer interfaces.\n\nNote that the while this repo is named `submission-schema`, the generated artifacts are named `nmdc_submission_schema` for disambiguation purposes when publishing to PyPI.\n\n## Website\n\n* [https://microbiomedata.github.io/submission-schema](https://microbiomedata.github.io/submission-schema)\n\n## Repository Structure\n\n* [examples/](examples/) - example data\n* [project/](project/) - project files (do not edit these)\n* [src/](src/) - source files (edit these)\n    * [nmdc_submission_schema](src/nmdc_submission_schema)\n        * [schema](src/nmdc_submission_schema/schema) -- LinkML schema (edit this)\n* [datamodel](src/nmdc_submission_schema/datamodel) -- Generated python datamodel\n* [tests](tests/) - python tests\n\n## Developer Documentation\n\n<details>\nUse the `make` command to generate project artefacts:\n\n- `make all`: make everything\n- `make deploy`: deploys site\n\n</details>\n\n## Credits\n\nthis project was made with [linkml-project-cookiecutter](https://github.com/linkml/linkml-project-cookiecutter)\n',
    'author': 'Mark Andrew Miller',
    'author_email': 'mam@lbl.gov',
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
