# 🌠 Py Spark
By Anthony Vilarim Caliani

[![#](https://img.shields.io/badge/licence-MIT-blue.svg)](#) [![#](https://img.shields.io/badge/open--jdk-1.8.x-red.svg)](#) [![#](https://img.shields.io/badge/scala-2.11.x-mediumvioletred.svg)](#) [![#](https://img.shields.io/badge/apache--spark-2.4.3-darkorange.svg)](#) [![#](https://img.shields.io/badge/python-3-yellow.svg)](#)

## Repository Description
This is my Apache PySpark project. Here you will find some stuff that I've done while I was learning about working with PySpark.

## Before Installing
- You must have Java installed
- You must have `$JAVA_HOME` environment variable configured
- Download [_Apache Spark_](https://spark.apache.org/downloads.html)
  - Extract the downloaded Spark `.zip` or `.tar` file wherever you prefer

Now let's do this!

## Installing and Configuring PySpark

```sh
# First, we need to configure some environment variables.
# Edit ".bashrc", ".bash_profile" or ".zshrc" file.
vim ~/.bashrc

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

## Quick Start

> 👉 Before run this script make sure that you have already created a Python 3 virtual environment ;)

```sh
# Execute "run.sh" script passing as argument the name of scprit file.
sh run.sh $SCRIPT

# Example
sh run.sh src/first.py
```

## Related Links
- [Apache Spark: Official Website](https://spark.apache.org)
- [Tutorials Point: PySpark - Quick Guide](https://www.tutorialspoint.com/pyspark/pyspark_quick_guide.htm)
