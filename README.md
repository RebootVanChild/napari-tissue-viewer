# napari-tissue-viewer

[![License BSD-3](https://img.shields.io/pypi/l/napari-tissue-viewer.svg?color=green)](https://github.com/RebootVanChild/napari-tissue-viewer/raw/main/LICENSE)
[![PyPI](https://img.shields.io/pypi/v/napari-tissue-viewer.svg?color=green)](https://pypi.org/project/napari-tissue-viewer)
[![Python Version](https://img.shields.io/pypi/pyversions/napari-tissue-viewer.svg?color=green)](https://python.org)
[![tests](https://github.com/RebootVanChild/napari-tissue-viewer/workflows/tests/badge.svg)](https://github.com/RebootVanChild/napari-tissue-viewer/actions)
[![codecov](https://codecov.io/gh/RebootVanChild/napari-tissue-viewer/branch/main/graph/badge.svg)](https://codecov.io/gh/RebootVanChild/napari-tissue-viewer)
[![napari hub](https://img.shields.io/endpoint?url=https://api.napari-hub.org/shields/napari-tissue-viewer)](https://napari-hub.org/plugins/napari-tissue-viewer)

A image viewer for WashU HTAN

----------------------------------

This [napari] plugin was generated with [Cookiecutter] using [@napari]'s [cookiecutter-napari-plugin] template.

<!--
Don't miss the full getting started guide to set up your new package:
https://github.com/napari/cookiecutter-napari-plugin#getting-started

and review the napari docs for plugin developers:
https://napari.org/stable/plugins/index.html
-->

## Installation

You can install `napari-tissue-viewer` via [pip]:

    pip install napari-tissue-viewer



To install latest development version :

    pip install git+https://github.com/RebootVanChild/napari-tissue-viewer.git

## Usage

1. Load images:<br>
First, select files to load:<br>
For each tissue block:
* 5x image file path
* 20x image file path
* 5x registration file path
* 20x registration file path
* segmented 20x channel file path<br><br>
You don't have to fill all of them.<br>
If the images and the segmented channel are downsampled, please specify the scale factor.<br>
After file selection, press "load" to load.
2. Visualization controls:<br>
Press "auto contrast" to perform auto contrast on 5x images.<br>
Use the checkboxes to toggle visibilities of tissue blocks, layers and channels.


## Contributing

Contributions are very welcome. Tests can be run with [tox], please ensure
the coverage at least stays the same before you submit a pull request.

## License

Distributed under the terms of the [BSD-3] license,
"napari-tissue-viewer" is free and open source software

## Issues

If you encounter any problems, please [file an issue] along with a detailed description.

[napari]: https://github.com/napari/napari
[Cookiecutter]: https://github.com/audreyr/cookiecutter
[@napari]: https://github.com/napari
[MIT]: http://opensource.org/licenses/MIT
[BSD-3]: http://opensource.org/licenses/BSD-3-Clause
[GNU GPL v3.0]: http://www.gnu.org/licenses/gpl-3.0.txt
[GNU LGPL v3.0]: http://www.gnu.org/licenses/lgpl-3.0.txt
[Apache Software License 2.0]: http://www.apache.org/licenses/LICENSE-2.0
[Mozilla Public License 2.0]: https://www.mozilla.org/media/MPL/2.0/index.txt
[cookiecutter-napari-plugin]: https://github.com/napari/cookiecutter-napari-plugin

[file an issue]: https://github.com/RebootVanChild/napari-tissue-viewer/issues

[napari]: https://github.com/napari/napari
[tox]: https://tox.readthedocs.io/en/latest/
[pip]: https://pypi.org/project/pip/
[PyPI]: https://pypi.org/
