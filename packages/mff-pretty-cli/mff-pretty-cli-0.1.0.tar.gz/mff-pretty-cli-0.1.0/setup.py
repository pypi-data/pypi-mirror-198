# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pretty_cli']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'mff-pretty-cli',
    'version': '0.1.0',
    'description': 'Simple helper to get pretty printing in the CLI.',
    'long_description': '# Pretty-CLI: Pretty Printing for the CLI\n\nThis package provides `PrettyCli`, a class providing utilities for structured printing in the CLI. Simply use its `print()` and helper methods instead of the default `print()` and you\'re good to go!\n\nHere is a full example:\n\n```python\nfrom pretty_cli import PrettyCli\n\n\ncli = PrettyCli()\n\n\ndef main():\n    cli.main_title("my example file:\\nAmazing")\n    cli.print("Hello, world!")\n    cli.print("你好！")\n    cli.big_divisor() # Divisors, titles, etc. add blank space above/under as needed.\n    cli.print("Let\'s print a dict:")\n    cli.blank() # Add a blank if the previous line is not blank already.\n    cli.blank()\n    cli.blank()\n    cli.print({ # Enforces nice alignment of dict contents.\n        "foo": "bar",\n        "nested": { "hi": "there" },\n        "another one": { "how": "are you?", "fine": "thanks" },\n    })\n    cli.small_divisor()\n    cli.print("Some header styles:")\n    cli.chapter("a chapter")\n    cli.subchapter("a sub-chapter")\n    cli.section("a section")\n    cli.print("That\'s all, folks!")\n\n\nif __name__ == "__main__":\n    main()\n\n```\n\nAnd the produced output:\n\n```\n==================================================================\n======================== MY EXAMPLE FILE: ========================\n============================ AMAZING =============================\n==================================================================\n\nHello, world!\n你好！\n\n================================\n\nLet\'s print a dict:\n\nfoo:         bar\nnested:\n    hi:      there\nanother one:\n    how:     are you?\n    fine:    thanks\n\n----------------\n\nSome header styles:\n\n================ A Chapter ================\n\n-------- A Sub-Chapter --------\n\n[A Section]\n\nThat\'s all, folks!\n```\n',
    'author': 'Marc Fraile',
    'author_email': 'marc.fraile.fabrega@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
