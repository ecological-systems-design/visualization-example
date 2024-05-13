# Examples of Visualization Dashboard with Dash

## Recording

Recording of this tutorial is available:
  - permanently on the group server Y:\Software, tools, Languages\Visualization dashboards with dash and plotly.
  - (probably) until the end of April 2025 on the [ETHZ zoom server](https://ethz.zoom.us/rec/share/1PvkXqkOpUAiyPJ90zTgcf3Ui2io1vRO-sSnbsiLIOfvsAFz3cDh_z2KqHMLzoMC.WRA-z9eET82BX9Oe).

## Getting started

1. Download or `git clone` this repository
2. Create conda environment for this seminar by running in the terminal:

```
conda create -n dashboard
```

3. Activate the created conda environment

```
conda activate dashboard
```

4. Install the necessary python packages:

```
conda install pandas
conda install plotly
conda install dash
conda install -c conda-forge dash-bootstrap-components
conda install -c conda-forge geopandas
```

5. In the terminal, navigate to the repository's `src` folder and run

```
python app.py
```

6. To check out the dashboard with maps, run

```
python app_maps.py
```

This installation works for Fedora Linux 37 and Python 3.11.
