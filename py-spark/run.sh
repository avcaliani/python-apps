#!/bin/bash
readonly APP_FILE=$1
readonly LOG_FILE="app.log"

spark_run() {

  if [ ! -d "./logs" ]; then
    mkdir ./logs
  fi

  echo "Running..."
  source venv/bin/activate

  if [ -z $(command -v tee) ]; then
    spark-submit $APP_FILE > "./logs/$LOG_FILE" 2>&1
  else
    spark-submit $APP_FILE 2>&1 | tee "./logs/$LOG_FILE"
  fi

  deactivate
  echo "Done!"
}

check_venv() {
  if [ ! -d "./venv" ]; then
    echo "FATAL: Python 'venv' is missing, please check it first." >&2
    exit 0
  fi
}

check_installation() {
  if [ -z $(command -v $1) ]; then
    echo "FATAL: '$2' is missing, please check it first." >&2
    exit 0
  fi
}

  # # #    #   #    #   #    #   #    # # #    #   #    # # #
  #   #    #   #    ##  #    ##  #      #      ##  #    #
  # #      #   #    # # #    # # #      #      # # #    #  ##
  #  #     #   #    #  ##    #  ##      #      #  ##    #   #
  #   #    # # #    #   #    #   #    # # #    #   #    # # #


echo "\n      ____              __"
echo "     / __/__  ___ _____/ /__"
echo "    _\\ \\/ _ \\/ _ \`/ __/  '_/"
echo "   /__ / .__/\\_,_/_/ /_/\\_\\"
echo "      /_/\n"
echo "  The Best Spark Submit Runner that you have ever seen!"
echo "  Made by @avcaliani\n\n"

check_installation "python3"      "Python 3"
check_installation "java"         "Java"
check_installation "spark-submit" "Spark Submit"

check_venv
spark_run
