# ⭕ Py Oracle

By Anthony Vilarim Caliani

![License](https://img.shields.io/github/license/avcaliani/python-apps?logo=apache&color=lightseagreen)
![#](https://img.shields.io/badge/python-3.8.x-yellow.svg)
![#](https://img.shields.io/badge/database-oracle--xe--11g-red.svg)

This is an example of working with **Oracle Database** and **Python**.<br>
But, before you try it you must build `oracle-app` image.

```bash
docker-compose build
```

Well, now that you built the `oracle-app` image... Let's rock!

```bash
docker-compose up
# Output Sample...
# oracle-app    | ----------------------------------------
# oracle-app    | DATABASE
# oracle-app    | ----------------------------------------
# oracle-app    | Host: oracle-db
# oracle-app    | Port: 1521
# oracle-app    | SID: xe
# oracle-app    | User: system
# oracle-app    | Password: oracle
# oracle-app    | Oracle Version: 11.2.0.2.0
# oracle-app    | 
# oracle-app    | ----------------------------------------
# oracle-app    | DEVELOPERS
# oracle-app    | ----------------------------------------
# oracle-app    | (1, 'avcaliani', 'https://github.com/avcaliani', 1997, datetime.datetime(2020, 8, 19, 23, 4, 17))
# oracle-app    | That's all folks!
```

When you finsh testing... Press `Ctrl+C` and...

```bash
docker-compose down
```

## Related Links

- [Oracle Tutorial: Connecting to Oracle in Python](https://www.oracletutorial.com/python-oracle/connecting-to-oracle-database-in-python/)
- [DockerHub: Oracle XE 11g](https://hub.docker.com/r/oracleinanutshell/oracle-xe-11g)
- [Py Docs: CX Oracle](https://cx-oracle.readthedocs.io/en/latest/)
