# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['mojxml', 'mojxml.process']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.1.3,<9.0.0',
 'fiona>=1.9.1,<2.0.0',
 'lxml>=4.9.2,<5.0.0',
 'pyproj>=3.4.1,<4.0.0',
 'shapely>=2.0.1,<3.0.0']

entry_points = \
{'console_scripts': ['mojxml2ogr = mojxml.__main__:main']}

setup_kwargs = {
    'name': 'mojxml',
    'version': '0.2.1',
    'description': 'A tool for fast conversion of Japanese "MOJ Map XML" (land registration polygons) into geospatial formats.',
    'long_description': '# mojxml-py\n\n[![Test](https://github.com/MIERUNE/mojxml-py/actions/workflows/test.yml/badge.svg)](https://github.com/MIERUNE/mojxml-py/actions/workflows/test.yml) [![PyPI Package](https://img.shields.io/pypi/v/mojxml?color=%2334D058&label=PyPI%20package)](https://pypi.org/project/mojxml) [![codecov](https://codecov.io/gh/MIERUNE/mojxml-py/branch/main/graph/badge.svg?token=mkeysxV2xy)](https://codecov.io/gh/MIERUNE/mojxml-py)\n\n法務省登記所備付地図データ（地図XML）を各種GISデータ形式 (GeoJSON, GeoPackage, FlatGeobuf, etc.) に変換するコマンドラインツールです。Pythonライブラリとしても使用できます。\n\nA tool for fast conversion of Japanese "MOJ Map XML" (land registration polygons) into geospatial format, written in Python.\n\nXMLパーサとして [lxml](https://github.com/lxml/lxml) (libxml2) を使用することで、デジタル庁のリファレンス実装 ([mojxml2geojson](https://github.com/JDA-DM/mojxml2geojson)) よりも高速な変換を実現しています。また、配布されているZIPファイルをそのまま入力することもできます。\n\n## インストール\n\nUbuntu/Debian:\n\n```bash\napt install libgdal-dev\npip3 install mojxml\n```\n\nmacOS (Homebrew):\n\n```bash\nbrew install gdal\npip3 install mojxml\n```\n\n## コマンドラインインタフェース\n\n```\nUsage: mojxml2ogr [OPTIONS] DST_FILE SRC_FILES...\n\n  Convert MoJ XMLs to GeoJSON/GeoPackage/FlatGeobuf/etc.\n\n  DST_FILE: output filename (.geojson, .gpkg, .fgb, etc.)\n\n  SRC_FILES: one or more .xml/.zip files\n\nOptions:\n  --worker [multiprocess|thread|single]\n                                  [default: multiprocess]\n  -a, --arbitrary                 Include 任意座標系\n  -c, --chikugai                  Include 地区外 and 別図\n```\n\n- 出力フォーマットは、出力ファイル名の拡張子から自動で判断されます。\n- `-a` オプションを指定すると、任意座標系のXMLファイルも変換されます。\n- `-c` オプションを指定すると、地番が「地区外」「別図」の地物も出力されます。\n\n### 使用例\n\n```bash\n# XMLファイルをGeoJSONに変換する\n❯ mojxml2ogr output.geojson 15222-1107-1553.xml\n\n# 複数のXMLファイルを1つのGeoJSONに変換する\n❯ mojxml2ogr output.geojson 15222-1107-1553.xml 15222-1107-1554.xml\n\n# 配布用ZIPファイルに含まれる全XMLをFlatGeobufに変換する\n❯ mojxml2ogr output.fgb 15222-1107.zip\n\n# 3つのZIPファイルをまとめて1つのFlatGeobufに変換する\n❯ mojxml2ogr output.fgb 01202-4400.zip 01236-4400.zip 01337-4400.zip\n\n# zZIPファイルを1段階展開して出てくるZIPファイルも入力できる\n❯ mojxml2ogr output.fgb 15222-1107-15*.zip\n```\n\n## License\n\nMIT License\n',
    'author': 'MIERUNE Inc.',
    'author_email': 'info@mierune.co.jp',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/MIERUNE/mojxml-py',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8.7,<4.0',
}


setup(**setup_kwargs)
