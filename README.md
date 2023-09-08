# DAV Karlsruhe CO2 Tool
Diese Tool erleichtert die Eingabe der Rechnungsdaten für die DAV Klimabilanz

## Prerequisites
We use [Poetry](https://python-poetry.org/) for package management.

Install it by following the installation instructions at https://python-poetry.org/docs/


## Installation

To install run
```sh
poetry install
```
This will install all project dependencies in a separate poetry managed virtual python environment.

## Run it

Optionally place an example bill in the pdf directory:
```shell
curl -o pdf/example_bill.pdf https://www.ionos.de/startupguide/fileadmin/StartupGuide/Vorlagen_KMU/Rechnungsvorlage-Muster.pdf
```

Run the tool with
```shell
poetry run poe co2tool
```