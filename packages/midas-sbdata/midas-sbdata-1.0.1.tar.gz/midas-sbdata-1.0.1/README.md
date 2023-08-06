# MIDAS Simbench Data Simulator

## Description
This package contains a MIDAS module providing a simulator for Simbench data sets.

Although this package is intended to be used with MIDAS, it does not depend from anything MIDAS-related except for the `midas-util` package. You can use in any mosaik simulation scenario.

## Installation
This package will usually installed automatically together with `midas-mosaik`. It is available on pypi, so you can install it manually with

```bash
pip install midas-sbdata
```

## Usage
The complete documentation is available at https://midas-mosaik.gitlab.io/midas.

### Inside of MIDAS
To use the Simbench data inside of MIDAS, just add `sbdata` to your modules

```yaml
my_scenario:
  modules:
    - sbdata
    - ...
```

and configure it with:

```yaml
  sbdata_params:
    my_grid_scope:
      step_size: 900
      grid_name: my_grid_scope
      start_date: 2020-01-01 00:00:00+0100
      cos_phi: 0.9
      filename: 1-LV-rural3--0-sw.hdf5
      data_path: path/to/hdf-specified-by-filename
      load_scaling: 1.0
      load_mapping: default
      sgen_scaling: 1.0
      sgen_mapping: default
      storage_scaling: 1.0
      storage_mapping: default
      interpolate: False
      randomize_data: False
      noise_factor: 0.2
      randomize_cos_phi: False
      seed: ~
      seed_max: 1_000_000
```

All of the attributes show their default values and can optionally be left out. The *xxx*_mapping attributes can either be `default` or a dictionary with a specific mapping. When `default` is used, the mapping defined in the powergrid profiles is used.

## License
This software is released under the GNU Lesser General Public License (LGPL). See the license file for more information about the details.