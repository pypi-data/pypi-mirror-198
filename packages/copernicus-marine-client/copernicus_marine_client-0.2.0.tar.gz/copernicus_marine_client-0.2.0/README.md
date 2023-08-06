# Copernicus Marine Service client

A library to facilitate the access of Copernicus Marine Service products and datasets.

## Introduction

This package allows to recover products and datasets information from Command Line Interface or with Python code,
as well as download subsets through opendap protocol.

## Command Line Interface (CLI)

### Command *describe*
Retrieve information about products as JSON:

```
> copernicus-marine describe
{
  "products": [
    {
      "bbox": [
        "-25.00",
        "75.00",
        "70.00",
        "86.00"
      ],
      "created": "2011-10-11",
      "product_id": "SEAICE_ARC_PHY_L3M_NRT_011_017",
      "temporal_extent": [
        "2021-04-27",
        null
      ],
      "thumbnail": "https://catalogue.marine.copernicus.eu/documents/IMG/SEAICE_ARC_PHY_L3M_NRT_011_017.png",
      "title": "ARCTIC Ocean and Sea-Ice Sigma-Nought"
    }
    ...
  ]
}
```

Retrieve all information about products and datasets as JSON:

```
> copernicus-marine describe --include-description --include-datasets --include-providers --include-keywords
{
  "products": {
    "title": "ARCTIC Ocean and Sea-Ice Sigma-Nought",
    "product_id": "SEAICE_ARC_PHY_L3M_NRT_011_017",
    "thumbnail": "https://catalogue.marine.copernicus.eu/documents/IMG/SEAICE_ARC_PHY_L3M_NRT_011_017.png",
    "description": "'''Short description:''' \nFor the Arctic Ocean  - multiple Sentinel-1 scenes, Sigma0 calibrated and noise-corrected, with individual geographical map projections over Svalbard and Greenland Sea regions.\n\n'''DOI (product) :'''   \nhttps://doi.org/10.48670/moi-00124",
    "providers": [
      {
        "name": "OSI-METNO-OSLO-NO (SD)",
        "roles": [
          "pointOfContact"
        ],
        "url": null,
        "email": "marine-servicedesk@met.no"
      },
      {
        "name": "OSI-METNO-OSLO-NO (PM)",
        "roles": [
          "originator"
        ],
        "url": null,
        "email": "cecilie.wettre@met.no"
      },
      {
        "name": "OSI-METNO-OSLO-NO (WPL)",
        "roles": [
          "custodian"
        ],
        "url": null,
        "email": "ositac-manager@met.no"
      },
      {
        "name": "SIW-METNO-OSLO-NO",
        "roles": [
          "resourceProvider"
        ],
        "url": null,
        "email": "ositac-prod@met.no"
      },
      {
        "name": "SIW-METNO-OSLO-NO",
        "roles": [
          "distributor"
        ],
        "url": null,
        "email": "cmems-tech@met.no"
      }
    ],
    "created": "2011-10-11",
    "bbox": [
      "-25.00",
      "75.00",
      "70.00",
      "86.00"
    ],
            "uri": "ftp://nrt.cmems-du.eu/Core/SEAICE_ARC_PHY_L3M_NRT_011_017/cmems_obs-si_arc_physic_nrt_L2-EW_PT1H-irr"
          }
        ]
      }
    ...
    ]
  }
}

```

Check out the help:

```
> copernicus-marine describe --help
Usage: copernicus-marine describe [OPTIONS]

Options:
  --one-line             Output JSON on one line
  --include-description  Include product description in output
  --include-datasets     Include product dataset details in output
  --include-providers    Include product provider details in output
  --include-keywords     Include product keyword details in output
  -c, --contains TEXT    Filter catalogue output. Returns products with
                         attributes matching a string token
  --help                 Show this message and exit.
```

### Command *subset*

Download a dataset subset, based on dataset id, variable names and attributes slices:

```
> copernicus-marine subset -p METOFFICE-GLO-SST-L4-NRT-OBS-SST-V2 -v analysed_sst -v sea_ice_fraction -t 2021-01-01 2021-01-03 -g 0.0 0.1 0.0 0.1

< Your login please:
< Your password please:
< Trying to download as one file...
```

File downloaded to ./{dataset_id}.nc if not specified otherwise (through -o/--output-path and -f/--output-file options).

Check out the help:

```
> copernicus-marine subset --help

Usage: copernicus-marine subset [OPTIONS]

  Downloads subsets of datasets as NetCDF files taking into account the server
  data query limit. A 'dataset-id' (can be found via the 'copernicus-marine
  describe' command) is required.

  Example:

    copernicus-marine subset --dataset-id METOFFICE-GLO-SST-L4-NRT-OBS-SST-V2
    --variable analysed_sst --variable sea_ice_fraction --temporal-subset
    2021-01-01 2021-01-02 --geographical-subset 0.0 0.1 0.0 0.1

    copernicus-marine subset -p METOFFICE-GLO-SST-L4-NRT-OBS-SST-V2 -v
    analysed_sst   -v sea_ice_fraction -t 2021-01-01 2021-01-02 -g 0.0 0.1 0.0
    0.1

Options:
  -u, --dataset-url TEXT          The full dataset URL
  -p, --dataset-id TEXT           The dataset id  [required]
  -v, --variable TEXT             Specify dataset variables
  -g, --geographical-subset <FLOAT RANGE FLOAT RANGE FLOAT RANGE FLOAT RANGE>...
                                  The geographical subset as minimal latitude,
                                  maximal latitude, minimal longitude and
                                  maximal longitude
  -t, --temporal-subset <DATETIME DATETIME>...
                                  The temporal subset as start datetime and
                                  end datetime
  -d, --depth-range <FLOAT RANGE FLOAT RANGE>...
                                  The depth range in meters, if depth is a
                                  dataset coordinate
  -o, --output-path PATH          The destination path for the downloaded
                                  files. Default is the current directory
                                  [required]
  -f, --output-file PATH          Concatenate the downloaded data in the given
                                  file name (under the output path)
  -l, --limit INTEGER             Specify the download size limit (in MB) of
                                  the Opendap server if it can't be provided
                                  by the message error
  --confirmation                  Print dataset metadata and ask for
                                  confirmation before download
  --help                          Show this message and exit.
```


## Installation

Using pip, for example:
```
pip install copernicus-marine
```
## Technical details

This module is organized around two capabilities:
- a catalogue, parsed from web requests, that contains informations on the available datasets
- a downloader, to simplify the download of dataset files or subsets

The catalogue can be displayed by the user and is used by the downloader to link the user
requests with files or subset of files to retrieve.
The downloader will help the user download the needed datasets.
