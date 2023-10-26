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
    sed \
    && rm -rf /var/lib/apt/lists/*

# due to security issues with ps and pdf, conversion of these files is disallowed
# we remove this restriction in the following line
RUN sed -i '/disable ghostscript format types/,+6d' /etc/ImageMagick-6/policy.xml && \
    sed -i 's/name=\"disk\" value=\"1GiB\"/name=\"disk\" value=\"4GiB\"/' /etc/ImageMagick-6/policy.xml && \
    sed -i 's/name=\"memory\" value=\"256MiB\"/name=\"memory\" value=\"512MiB\"/' /etc/ImageMagick-6/policy.xml
RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH="${PATH}:/root/.local/bin"
WORKDIR /root
RUN git clone https://github.com/christophamma/dav-co2-accounting.git
WORKDIR /root/dav-co2-accounting
RUN poetry install
CMD poetry run voila --no-browser --Voila.ip=0.0.0.0 notebook/test_ui.ipynb




