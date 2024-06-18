# 📊 ELK Stack

By Anthony Vilarim Caliani

![License](https://img.shields.io/github/license/avcaliani/python-apps?logo=apache&color=lightseagreen)
![#](https://img.shields.io/badge/elasticsearch-7.12.0-lightgrey.svg)
![#](https://img.shields.io/badge/logstash-7.12.0-yellow.svg)
![#](https://img.shields.io/badge/kibana-7.12.0-F04E98.svg)

This is a PoC where I've explored a little beat of the ELK Stack.  

```bash
# Starting services...
# Kibana URL: http://localhost:5601
docker-compose up -d
```

Checking docker logs...

```bash
docker ps
docker logs py-app
```

When you finsh... Press `Ctrl+C` and...

```bash
docker-compose down
```

## Screenshot

![#](.docs/screenshot.png)

## Related Links
s
- [ELK Configuration](http://blog.aeciopires.com/instalando-o-elastic-kibana-e-logstash-via-docker/)
- [Send Logs via LogStash](https://www.freecodecamp.org/news/how-to-use-elasticsearch-logstash-and-kibana-to-visualise-logs-in-python-in-realtime-acaab281c9de/)
