#!/bin/bash
# @author       Anthony Vilarim Caliani
# @contact      github.com/avcaliani
#
# @Description
# Py Cassandra App.


info() {
  echo -e "\033[1;32mINFO\033[00m   $1"
}

error() {
  echo -e "\033[0;31mERROR\033[00m  $1"
}

echo -e "
                                   _
                                  | |
  ___ __ _ ___ ___  __ _ _ __   __| |_ __ __ _
 / __/ _\` / __/ __|/ _\` | '_ \ / _\` | '__/ _\` |
| (_| (_| \__ \__ \ (_| | | | | (_| | | | (_| |
 \___\__,_|___/___/\__,_|_| |_|\__,_|_|  \__,_|
                                  \033[1;34mRUNNER v19.10\033[00m
"

case "$1" in
  start)

    if [ ! -d ".venv" ]; then
      info "Creating python virtual environment..."
      python3 -m venv .venv
      source .venv/bin/activate && pip install -r requirements.txt && deactivate
    fi

    info "Deploying docker containers..."
    docker-compose up -d && sleep 15 && docker-compose ps

    # Status - U (up) or D (down)
    # State - N (normal), L (leaving), J (joining), M (moving)
    # Example: UN, UJ...
    info "(Node 01) Cassandra status..."
    sleep 30
    docker exec -it cassandra-node-01 nodetool status

    info "(Node 02) Cassandra status..."
    sleep 60
    docker exec -it cassandra-node-02 nodetool status

    sleep 15
    info "(Node 02) Loading data..."
    docker exec -it cassandra-node-02 cqlsh -f /app/init-cassandra.cql

    info "Running python script..."
    source .venv/bin/activate && python main.py && deactivate
    ;;

  stop)
    info "Cleaning things up..."
    docker-compose stop
    docker stop $(docker ps -a -q)
    if [ "$2" == "-rm" ]; then
      docker rm $(docker ps -a -q)
    fi
    ;;

  -h)
    info "  Available Commands:"
    info "   - start       : Start Application"
    info "   - stop        : Stop Application"
    info "   - stop -rm    : Stop Application and remove all containers"
    ;;

  *)
    error "Invalid option '$1'..."
    info "See available options running with \"-h\" flag :)"
    ;;

esac

info "Bye!"
exit 0
