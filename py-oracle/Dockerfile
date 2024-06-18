FROM python:3

# Oracle Instant Client
WORKDIR /opt/oracle

ADD "https://download.oracle.com/otn_software/linux/instantclient/19800/instantclient-basic-linux.x64-19.8.0.0.0dbru.zip" .
RUN apt-get update \
    && apt-get install libaio1 \
    && unzip *.zip \
    && sh -c "echo /opt/oracle/instantclient_19_8 > /etc/ld.so.conf.d/oracle-instantclient.conf" \
    && ldconfig

ENV LD_LIBRARY_PATH=/opt/oracle/instantclient_19_8:$LD_LIBRARY_PATH

# Python App
WORKDIR /app
ADD . .
RUN  pip install -r requirements.txt
CMD sleep 20 && python main.py
