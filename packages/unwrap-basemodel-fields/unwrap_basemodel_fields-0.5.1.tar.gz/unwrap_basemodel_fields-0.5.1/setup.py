# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['unwrapper']

package_data = \
{'': ['*']}

install_requires = \
['pydantic>=1.9.0,<2.0.0']

setup_kwargs = {
    'name': 'unwrap-basemodel-fields',
    'version': '0.5.1',
    'description': 'Unwrapper stores a Result object to implement unpacking of values if they are not None. The BaseModel object is also a little extended to work with the Result object.',
    'long_description': '# :recycle: Unwrapper pydantic optional fields :recycle:\n\n\nUnwrapper stores a **Result** object to implement unpacking of values if they are not **None**. The **BaseModel** object is also a little extended to work with the **Result** object.\n\n\n# :star: A simple example :star:\n```python\nfrom unwrapper import BaseModel, Result\n\nclass User(BaseModel):\n    name: Result[str]\n    age: int\n\ndata = {\n    "age": 20\n}\nuser = User(**data)\n#> User(name=Result(None), age=20)\nprint("Hello", user.name.unwrap(error_msg="What\'s your name?"), "!")\n#> ValueError: What\'s your name?\n```\n\n# :book: Documentation :book:\n* In :ru: [**Russian**](https://github.com/luwqz1/unwrap_basemodel_fields/blob/main/docs/RU.md) :ru:\n* In :us: [**English**](https://github.com/luwqz1/unwrap_basemodel_fields/blob/main/docs/EN.md) :us:\n',
    'author': 'Georgy howl',
    'author_email': 'howluwqz1@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/luwqz1/unwrap_basemodel_fields',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
