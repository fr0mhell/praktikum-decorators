FROM python:3.9-slim-buster

### Set ROOT privileges
ENV C_FORCE_ROOT=True

### Set default workdir inside container
WORKDIR /catloader

### Add dependencies info
COPY requirements.txt ./

### Install dependencies
RUN pip install --no-cache-dir --src=/src -r ./requirements.txt

### !!! Add source code to container
COPY . ./

### Run Django
CMD ["python3", "app_docker.py"]
