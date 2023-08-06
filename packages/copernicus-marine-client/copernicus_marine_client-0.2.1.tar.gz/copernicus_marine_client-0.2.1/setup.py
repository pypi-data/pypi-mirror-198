# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['copernicus_marine_client',
 'copernicus_marine_client.catalogue_parser',
 'copernicus_marine_client.command_line_interface']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.0.4',
 'numpy>=1.0',
 'opendap-downloader>0.8.0',
 'owslib>=0.27.2',
 'requests>=2.27.1']

entry_points = \
{'console_scripts': ['copernicus-marine = '
                     'copernicus_marine_client.command_line_interface.copernicus_marine:command_line_interface']}

setup_kwargs = {
    'name': 'copernicus-marine-client',
    'version': '0.2.1',
    'description': '',
    'long_description': '# Copernicus Marine Service client\n\nA library to facilitate the access of Copernicus Marine Service products and datasets.\n\n## Introduction\n\nThis package allows to recover products and datasets information from Command Line Interface or with Python code,\nas well as download subsets through opendap protocol.\n\n## Command Line Interface (CLI)\n\n### Command *describe*\nRetrieve information about products as JSON:\n\n```\n> copernicus-marine describe\n{\n  "products": [\n    {\n      "bbox": [\n        "-25.00",\n        "75.00",\n        "70.00",\n        "86.00"\n      ],\n      "created": "2011-10-11",\n      "product_id": "SEAICE_ARC_PHY_L3M_NRT_011_017",\n      "temporal_extent": [\n        "2021-04-27",\n        null\n      ],\n      "thumbnail": "https://catalogue.marine.copernicus.eu/documents/IMG/SEAICE_ARC_PHY_L3M_NRT_011_017.png",\n      "title": "ARCTIC Ocean and Sea-Ice Sigma-Nought"\n    }\n    ...\n  ]\n}\n```\n\nRetrieve all information about products and datasets as JSON:\n\n```\n> copernicus-marine describe --include-description --include-datasets --include-providers --include-keywords\n{\n  "products": {\n    "title": "ARCTIC Ocean and Sea-Ice Sigma-Nought",\n    "product_id": "SEAICE_ARC_PHY_L3M_NRT_011_017",\n    "thumbnail": "https://catalogue.marine.copernicus.eu/documents/IMG/SEAICE_ARC_PHY_L3M_NRT_011_017.png",\n    "description": "\'\'\'Short description:\'\'\' \\nFor the Arctic Ocean  - multiple Sentinel-1 scenes, Sigma0 calibrated and noise-corrected, with individual geographical map projections over Svalbard and Greenland Sea regions.\\n\\n\'\'\'DOI (product) :\'\'\'   \\nhttps://doi.org/10.48670/moi-00124",\n    "providers": [\n      {\n        "name": "OSI-METNO-OSLO-NO (SD)",\n        "roles": [\n          "pointOfContact"\n        ],\n        "url": null,\n        "email": "marine-servicedesk@met.no"\n      },\n      {\n        "name": "OSI-METNO-OSLO-NO (PM)",\n        "roles": [\n          "originator"\n        ],\n        "url": null,\n        "email": "cecilie.wettre@met.no"\n      },\n      {\n        "name": "OSI-METNO-OSLO-NO (WPL)",\n        "roles": [\n          "custodian"\n        ],\n        "url": null,\n        "email": "ositac-manager@met.no"\n      },\n      {\n        "name": "SIW-METNO-OSLO-NO",\n        "roles": [\n          "resourceProvider"\n        ],\n        "url": null,\n        "email": "ositac-prod@met.no"\n      },\n      {\n        "name": "SIW-METNO-OSLO-NO",\n        "roles": [\n          "distributor"\n        ],\n        "url": null,\n        "email": "cmems-tech@met.no"\n      }\n    ],\n    "created": "2011-10-11",\n    "bbox": [\n      "-25.00",\n      "75.00",\n      "70.00",\n      "86.00"\n    ],\n            "uri": "ftp://nrt.cmems-du.eu/Core/SEAICE_ARC_PHY_L3M_NRT_011_017/cmems_obs-si_arc_physic_nrt_L2-EW_PT1H-irr"\n          }\n        ]\n      }\n    ...\n    ]\n  }\n}\n\n```\n\nCheck out the help:\n\n```\n> copernicus-marine describe --help\nUsage: copernicus-marine describe [OPTIONS]\n\nOptions:\n  --one-line             Output JSON on one line\n  --include-description  Include product description in output\n  --include-datasets     Include product dataset details in output\n  --include-providers    Include product provider details in output\n  --include-keywords     Include product keyword details in output\n  -c, --contains TEXT    Filter catalogue output. Returns products with\n                         attributes matching a string token\n  --help                 Show this message and exit.\n```\n\n### Command *subset*\n\nDownload a dataset subset, based on dataset id, variable names and attributes slices:\n\n```\n> copernicus-marine subset -p METOFFICE-GLO-SST-L4-NRT-OBS-SST-V2 -v analysed_sst -v sea_ice_fraction -t 2021-01-01 2021-01-03 -g 0.0 0.1 0.0 0.1\n\n< Your login please:\n< Your password please:\n< Trying to download as one file...\n```\n\nFile downloaded to ./{dataset_id}.nc if not specified otherwise (through -o/--output-path and -f/--output-file options).\n\nCheck out the help:\n\n```\n> copernicus-marine subset --help\n\nUsage: copernicus-marine subset [OPTIONS]\n\n  Downloads subsets of datasets as NetCDF files taking into account the server\n  data query limit. A \'dataset-id\' (can be found via the \'copernicus-marine\n  describe\' command) is required.\n\n  Example:\n\n    copernicus-marine subset --dataset-id METOFFICE-GLO-SST-L4-NRT-OBS-SST-V2\n    --variable analysed_sst --variable sea_ice_fraction --temporal-subset\n    2021-01-01 2021-01-02 --geographical-subset 0.0 0.1 0.0 0.1\n\n    copernicus-marine subset -p METOFFICE-GLO-SST-L4-NRT-OBS-SST-V2 -v\n    analysed_sst   -v sea_ice_fraction -t 2021-01-01 2021-01-02 -g 0.0 0.1 0.0\n    0.1\n\nOptions:\n  -u, --dataset-url TEXT          The full dataset URL\n  -p, --dataset-id TEXT           The dataset id  [required]\n  -v, --variable TEXT             Specify dataset variables\n  -g, --geographical-subset <FLOAT RANGE FLOAT RANGE FLOAT RANGE FLOAT RANGE>...\n                                  The geographical subset as minimal latitude,\n                                  maximal latitude, minimal longitude and\n                                  maximal longitude\n  -t, --temporal-subset <DATETIME DATETIME>...\n                                  The temporal subset as start datetime and\n                                  end datetime\n  -d, --depth-range <FLOAT RANGE FLOAT RANGE>...\n                                  The depth range in meters, if depth is a\n                                  dataset coordinate\n  -o, --output-path PATH          The destination path for the downloaded\n                                  files. Default is the current directory\n                                  [required]\n  -f, --output-file PATH          Concatenate the downloaded data in the given\n                                  file name (under the output path)\n  -l, --limit INTEGER             Specify the download size limit (in MB) of\n                                  the Opendap server if it can\'t be provided\n                                  by the message error\n  --confirmation                  Print dataset metadata and ask for\n                                  confirmation before download\n  --help                          Show this message and exit.\n```\n\n\n## Installation\n\nUsing pip, for example:\n```\npip install copernicus-marine-client\n```\n## Technical details\n\nThis module is organized around two capabilities:\n- a catalogue, parsed from web requests, that contains informations on the available datasets\n- a downloader, to simplify the download of dataset files or subsets\n\nThe catalogue can be displayed by the user and is used by the downloader to link the user\nrequests with files or subset of files to retrieve.\nThe downloader will help the user download the needed datasets.\n',
    'author': 'jsouchard',
    'author_email': 'jsouchard@mercator-ocean.fr',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9',
}


setup(**setup_kwargs)
