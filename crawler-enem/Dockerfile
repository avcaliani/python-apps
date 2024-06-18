FROM python:3.10.4

# 👇 Spark Env
ENV JAVA_HOME="/opt/java" \
    SPARK_HOME="/opt/spark" \
    SPARK_VERSION="3.3.0" \
    HADOOP_VERSION="3" \
    PYSPARK_PYTHON=python

ENV PATH="$SPARK_HOME/bin:$SPARK_HOME/python:$PATH"

# 👇 Poetry Env
ENV POETRY_VERSION='1.1.14' \
    POETRY_VIRTUALENVS_CREATE=false \
    PATH="/root/.local/bin:$PATH"

WORKDIR /opt

# 👇 Installing Poetry
RUN apt-get update \
    && apt-get install -y build-essential python3-dev python3-setuptools curl \
    && pip install --upgrade --no-cache-dir pip \
    && curl -sSL https://install.python-poetry.org | python - --version "$POETRY_VERSION"

# 👇 Java
ADD "https://cdn.azul.com/zulu/bin/zulu8.56.0.21-ca-jdk8.0.302-linux_x64.tar.gz" .
RUN tar -xzf zulu*.tar.gz && rm -f zulu*.tar.gz && mv zulu* java

# 👇 Spark
ADD "https://archive.apache.org/dist/spark/spark-$SPARK_VERSION/spark-$SPARK_VERSION-bin-hadoop$HADOOP_VERSION.tgz" .
RUN tar -xzf spark*.tgz && rm -f spark*.tgz && mv spark* spark

# 👇 Postgres
ADD "https://repo1.maven.org/maven2/org/postgresql/postgresql/42.3.6/postgresql-42.3.6.jar" /opt/spark/jars/postgresql-42.3.6.jar

# 👇 Project Files
COPY *.toml .
COPY *.lock .

# 👇 Project Dependencies
RUN poetry install --no-dev

# 👇 Let's rock!
CMD tail -f /dev/null
