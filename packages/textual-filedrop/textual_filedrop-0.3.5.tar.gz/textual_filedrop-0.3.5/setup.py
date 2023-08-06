# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['textual_filedrop']

package_data = \
{'': ['*']}

install_requires = \
['rich>=13.3.2,<14.0.0', 'textual>=0.15.1,<0.16.0']

setup_kwargs = {
    'name': 'textual-filedrop',
    'version': '0.3.5',
    'description': 'FileDrop widget for Textual, easily drag and drop files into your terminal apps.',
    'long_description': '![textual-filedrop](https://user-images.githubusercontent.com/16024979/208708722-e550d8ca-22a7-47f0-adf9-16cad570cdfd.png)\n\n# textual-filedrop\n\nAdd filedrop support to your [Textual](https://github.com/textualize/textual/) apps, easily drag and drop files into your terminal apps.\n\n> _Tested on `Windows` and [`macOS`](https://github.com/Textualize/textual/discussions/1414#discussioncomment-4467029)._\n\n> _[Nerd Font](https://www.nerdfonts.com/font-downloads) is required to display file icons._\n\n## Install\n\n```\npip install textual-filedrop\n```\n\nor\n\n```\ngit clone https://github.com/agmmnn/textual-filedrop.git\ncd textual-filedrop\npoetry install\n```\n\n## Note\n\nSince version [0.10.0](https://github.com/Textualize/textual/releases/tag/v0.10.0) Textual supports [bubble](https://textual.textualize.io/guide/events/#bubbling) for the [paste event](https://textual.textualize.io/events/paste/) ([Textualize/textual#1434](https://github.com/Textualize/textual/issues/1434)). So if the terminal where your app is running treats the file drag and drop as a paste event, you can catch it yourself with the `on_paste` function without widget.\n\n## Usage\n\n### `getfiles`\n\n`getfiles` returns an object containing the _path, filename, extension_ and _icon_ of the files.\n\n```py\nfrom textual_filedrop import getfiles\n\nclass MyApp(App):\n...\n    def on_paste(self, event) -> None:\n        files = getfiles(event)\n        print(files)\n```\n\n![](https://i.imgur.com/1xdpivC.png)\n\n### `FileDrop` Widget\n\nAs long as the `FileDrop` widget is in focus, it will give the information of the dragged files and render the file names with their icons on the screen.\n\n```py\nfrom textual_filedrop import FileDrop\n```\n\n```py\n# add FileDrop widget to your app\nyield FileDrop(id="filedrop")\n```\n\n```py\n# focus the widget\nself.query_one("#filedrop").focus()\n```\n\n```py\n# when the files are dropped\ndef on_file_drop_dropped(self, message: FileDrop.Dropped) -> None:\n    path = message.path\n    filepaths = message.filepaths\n    filenames = message.filenames\n    filesobj = message.filesobj\n    print(path, filepaths, filenames, filesobj)\n\n\n# output: path, [filepaths], [filenames], [filesobj]\n```\n\nYou can find more examples [here](./examples).\n\n## Examples\n\n### [subdomain_lister.py](./examples/subdomain_lister.py)\n\nDrag and drop the subdomain list files and see the results as a tree list.\n\n![subdomain_lister](https://user-images.githubusercontent.com/16024979/208706132-0a33bb21-51b8-441a-aeb9-668dbfcb382c.gif)\n\n### [fullscreen.py](./examples/fullscreen.py)\n\nFullscreen example, will show the results in the textual console.\n\n### [hidden.py](./examples/hidden.py)\n\nAs long as focus is on, the `FileDrop` widget will be active even if it is not visible on the screen.\n\n### [without_widget.py](./examples/without_widget.py)\n\nAn example that renders the object with the information of the dragged files returned from the `getfiles` function to the screen with `rich.json`.\n\n## Dev\n\n```\npoetry install\n\ntextual console\npoetry run textual run --dev examples/subdomain_lister.py\n```\n',
    'author': 'agmmnn',
    'author_email': 'agmmnn@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7.8,<4.0.0',
}


setup(**setup_kwargs)
