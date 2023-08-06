#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pathlib import Path

import MPSPlots

root_path = Path(MPSPlots.__path__[0])

example_directory = root_path.joinpath('examples')

doc_data_path = root_path.parents[0].joinpath('docs')

style_directory = root_path.joinpath('styles')
# -
