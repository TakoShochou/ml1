FROM python:3

ARG UID

COPY requirements.txt /docker-build-assets/
RUN pip install --no-cache-dir -r /docker-build-assets/requirements.txt

RUN useradd -u ${UID} ml1
USER ml1
WORKDIR /home/ml1

CMD [ "python", "./main.py" ]