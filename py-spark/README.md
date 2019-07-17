# 🐍 PySpark
By Anthony Vilarim Caliani

[![#](https://img.shields.io/badge/open--jdk-1.8.x-red.svg)](#) [![#](https://img.shields.io/badge/scala-2.11.x-mediumvioletred.svg)](#) [![#](https://img.shields.io/badge/apache--spark-2.4.3-darkorange.svg)](#) [![#](https://img.shields.io/badge/python-3.7.x-blue.svg)](#)

## Repository Description
This is my Apache PySpark project. Here you will find some stuff that I've done while I was learning about how to work with PySpark.

---

## Before Installing
- You must have Java installed
- You must have `$JAVA_HOME` environment variable configured
- Download [_Apache Spark_](https://spark.apache.org/downloads.html)
  - Extract the downloaded Spark `.zip` or `.tar` file wherever you prefer

Now let's do this!

## Installing and Configuring PySpark

```sh
# First, we need to configure some environment variables.
# Edit ".bashrc" or ".bash_profile" file.
vi ~/.bashrc

# ATTENTION!
# My Spark Home is "/opt/spark" but it actually depends on
# where you extracted spark downloaded file.

# Now we are going to add some stuff \o/
# -------------------------------------------------------------

# Spark
export SPARK_HOME="/opt/spark"
export PATH="$SPARK_HOME/bin:$PATH"

# PySpark
export PATH="$SPARK_HOME/python:$PATH"
export PYSPARK_PYTHON=python3

# ---------------------------- :wq ----------------------------

# $PYSPARK_PYTHON variable is OPTIONAL and it defines which
# Python version PySpark is going to use.
# If you don't set up this variable PySpark is going to use
# your machine's default Python version.

# Now restart your terminal to get a new session or type
source ~/.bashrc

# Open PySpark terminal and be happy :)
pyspark

# THE END
```

---

## Related Links
- [Apache Spark: Official Website](https://spark.apache.org)
- [Tutorials Point: PySpark - Quick Guide](https://www.tutorialspoint.com/pyspark/pyspark_quick_guide.htm)

---

_You can find [@avcaliani](#) at [GitHub](https://github.com/avcaliani) or [GitLab](https://gitlab.com/avcaliani)._
