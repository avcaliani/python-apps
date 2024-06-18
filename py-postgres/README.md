# 🐘 Postgres App

By Anthony Vilarim Caliani

![License](https://img.shields.io/github/license/avcaliani/python-apps?logo=apache&color=lightseagreen)
![#](https://img.shields.io/badge/python-3.9.x-yellow.svg)

## Quick Start

Install project dependencies.

```bash
poetry install
```

> ⚠️ Now on, you must activate poetry's venv.

Up Docker container.

```bash
docker-compose up -d
```

Before executing the main script, create a mocked dataset.

```bash
# Create mock dataset using default values...
python mock.py

# Or, try --help for more options...
python mock.py -h
```

Now, you can execute some operations into Postgres.

```bash
# Help
python main.py -h

# Execute main script
python main.py [ 'save' | 'report' ]
```

## Related Links

- [DockerHub: Postgres](https://hub.docker.com/_/postgres)
- [Pandas Docs: Save to SQL](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_sql.html)
- [Pandas Docs: Read SQL](https://pandas.pydata.org/docs/reference/api/pandas.read_sql.html)
- [Medium: Wrinting DataFrame to Postgres](https://towardsdatascience.com/upload-your-pandas-dataframe-to-your-database-10x-faster-eb6dc6609ddf)
- [Stack Overflow: Upsert](https://stackoverflow.com/a/62379384)
