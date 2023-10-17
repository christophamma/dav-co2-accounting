FROM ubuntu:22.04 as execution-image
# Install necessary system packages
ARG DEBIAN_FRONTEND=noninteractive
ENV TZ=Europe/Berlin

EXPOSE 8866

RUN apt-get update && apt-get install --no-install-recommends -y \
    libmagickwand-dev \
    curl \
    ca-certificates \
    python-is-python3 \
    git \
    && rm -rf /var/lib/apt/lists/*

RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH="${PATH}:/root/.local/bin"
WORKDIR /root
RUN git clone https://github.com/christophamma/dav-co2-accounting.git
WORKDIR /root/dav-co2-accounting
RUN poetry install
CMD poetry run voila --no-browser --Voila.ip=0.0.0.0 notebook/test_ui.ipynb




