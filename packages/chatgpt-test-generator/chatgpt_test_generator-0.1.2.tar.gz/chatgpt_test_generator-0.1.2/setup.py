# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['chatgpt_test_generator']

package_data = \
{'': ['*']}

install_requires = \
['openai>=0.27.2,<0.28.0',
 'pytest>=7.2.2,<8.0.0',
 'setuptools>=67.6.0,<68.0.0',
 'toml>=0.10.2,<0.11.0']

setup_kwargs = {
    'name': 'chatgpt-test-generator',
    'version': '0.1.2',
    'description': 'AI based test generation tool.',
    'long_description': '## Chatgpt Test Generator\n\nEasy-to-use test generation tool. Powered by ChatGPT.\n\n###  **Project Structure:** \n```\n├── main.py\n├── poetry.lock\n├── pyproject.toml\n├── settings.toml\n└── tests\n```\n\n### **Usage:**\n\nGenerates automatic test for all functions with __#GPT ->__ syntax.\n\n_Available syntax rules will increase in next releases._\n\n__main.py__\n```\nimport chatgpt_test_generator\n\n\n# GPT ->\ndef search(array: list, number: int):\n    for idx, element in enumerate(array):\n        if element == number:\n            return idx\n\n    return -1\n\n\nif __name__ == "__main__":\n    chatgpt_test_generator.generate_tests_on_background()\n    \n```\n\nIn addition, the settings.toml file should be configured as follows:\n\n__settings.toml__\n```\n[default]\nCHATGPT_API_KEY = "YOUR OPEN-AI API KEY"\n```\n\n\nIf main.py is run, it will create tests for functions with GPT -> syntax under /test folder.\n\n```\n├── main.py\n├── poetry.lock\n├── pyproject.toml\n├── settings.toml\n└── tests\n    └── test_main.py\n```\n\n__test_main.py__\n```\nfrom main import search\n\n\ndef test_search():\n    array = [1, 2, 3, 4, 5]\n    assert search(array, 3) == 2\n    assert search(array, 6) == -1\n```\n\nIt doesn\'t matter how complex the project folder is.\n```\n├── comlex_folder1\n│ ├── complex_folder2\n│ └── complex_folder4\n│   └── example.py\n│ └── complex_folder_3\n├── main.py\n├── poetry.lock\n├── pyproject.toml\n├── settings.toml\n└── tests\n    └── test_main.py\n```\n\n__example.py__\n```\n# GPT ->\ndef divide_numbers(number1: int, number2: int):\n    return number1 / number2\n```\n\nIf I run main.py again, the output will be like this.\n```\n├── comlex_folder1\n│\xa0\xa0 ├── complex_folder2\n│\xa0\xa0 │\xa0\xa0 └── complex_folder4\n│\xa0\xa0 │\xa0\xa0     └── example.py\n│\xa0\xa0 └── complex_folder_3\n├── main.py\n├── poetry.lock\n├── pyproject.toml\n├── settings.toml\n└── tests\n    ├── test_example.py\n    └── test_main.py\n```\n\n__test_example.py__\n```\nfrom comlex_folder1.complex_folder2.complex_folder4.example import divide_numbers\n\n\ndef test_divide_numbers():\n    assert divide_numbers(4, 2) == 2\n    assert divide_numbers(9, 3) == 3\n    assert divide_numbers(2, 4) == 0.5\n    assert divide_numbers(-4, -2) == 2\n    assert divide_numbers(-9, 3) == -3\n    assert divide_numbers(-2, 4) == -0.5\n```',
    'author': 'Furkan Melih Ercan',
    'author_email': 'furkan.ercan@b2metric.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
