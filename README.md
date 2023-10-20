# DAV Karlsruhe CO2 Tool
Diese Tool erleichtert die Eingabe der Rechnungsdaten für die DAV Klimabilanz

## Prerequisites
You need to be able to run Docker Containers.

## Installation

Pull the docker container
```sh
docker pull ghcr.io/christophamma/dav-co2-accounting:main
```

## Usage

Run the container with
```shell
docker run --rm -p 8866:8866 -v <LOCAL_DATA_DIRECTORY>:/root/dav-co2-accounting ghcr.io/christophamma/dav-co2-accounting:main
```
where `<LOCAL_DATA_DIRECTORY>` is a path to the bills pdf. 
All persistent data will be saved in this directory.

You can then access the tool at http://localhost:8866
