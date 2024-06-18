#!/usr/bin/env python3
import os
import re
from datetime import datetime, timedelta
from functools import reduce
from random import choice
from subprocess import Popen, PIPE

import matplotlib.pyplot as plt
import pandas as pd

from src import arguments

UI_CONFIGS = {
    'ok': {'chart_icon': '.', 'chart_color': 'green', 'log_color': '1;32'},
    'warn': {'chart_icon': '^', 'chart_color': 'orange', 'log_color': '1;38;5;202'},
    'error': {'chart_icon': 'X', 'chart_color': 'red', 'log_color': '1;31'},
}


def ui_color(color_pattern, value):
    return f'\033[{color_pattern}m{value}\033[00m'


def ui_config(latency):
    if latency <= 0:
        return UI_CONFIGS['error']
    if latency > args.max_acceptable_latency:
        return UI_CONFIGS['warn']
    return UI_CONFIGS['ok']


def ping(host, command, search_pattern):
    ping_command = command.replace('<HOST>', host)
    process = Popen(
        ping_command.split(),
        stdout=PIPE,
        universal_newlines=True
    )
    latency, stdout = -1, process.stdout.readlines()
    for line in stdout:
        res = re.search(search_pattern, line.strip(), re.IGNORECASE)
        if res:
            latency = float(res.group(1))
            break
    return {
        'date': datetime.now(),
        'host': host,
        'latency': latency,
        'error': 1 if latency < 0 else 0,
        'command': ping_command,
        'output': reduce(lambda x, y: f'{x}{y}', stdout)
    }


def plot_result(date, latency, ui):
    plt.scatter(x=date, y=latency, c=ui['chart_color'], marker=ui['chart_icon'])
    plt.pause(args.sleep_time)


def report(df):
    print('---------------< REPORT >---------------')
    no_errors = df[df['error'] == 0]

    result = no_errors['latency'].min()
    result = ui_color(ui_config(result)['log_color'], result)
    print(f'Latency | Min: {result} ms')

    result = no_errors['latency'].max()
    result = ui_color(ui_config(result)['log_color'], result)
    print(f'Latency | Max: {result} ms')

    result = no_errors['latency'].mean()
    result = ui_color(ui_config(result)['log_color'], result)
    print(f'Latency | AVG: {result} ms')

    print(f'Ping    | Acceptable: {(no_errors[no_errors["latency"] <= args.max_acceptable_latency]).shape[0]}')
    print(f'Ping    | Errors: {(df[df["error"] == 1]).shape[0]}')
    print(f'Ping    | Warnings: {(no_errors[no_errors["latency"] > args.max_acceptable_latency]).shape[0]}')
    print(f'Ping    | Total: {df.shape[0]}')

    print(f'Test Duration: {df["date"].max() - df["date"].min()}')
    print('----------------------------------------')


def main():
    records, started_at = [], datetime.now()
    try:
        if not args.no_chart:
            plt.figure(num='🐍 Py Ping')

        ending = datetime.now() + timedelta(seconds=args.duration)
        while datetime.now() < ending:
            result = ping(choice(args.hosts), args.command, args.result_pattern)
            records.append(result)
            ui = ui_config(result['latency'])

            pretty_date = result['date'].strftime("%Y-%m-%d %H:%M:%S")
            pretty_latency = ui_color(
                ui['log_color'],
                f'{result["latency"]} ms' if result['latency'] >= 0 else 'ERROR'
            )
            print(f'Time: {pretty_date} | Host: {result["host"]} | Latency: {pretty_latency}')
            if not args.no_chart:
                plot_result(result['date'], result['latency'], ui=ui)

    except Exception as ex:
        print(f'Ops! Something went wrong...\nError: {ex}')
    except KeyboardInterrupt:
        print(f'\nStopping execution...')
    finally:
        df = pd.DataFrame(records)
        report(df)
        path = f'data/{started_at.strftime("%Y%m%d.%H%M%S")}.csv'
        os.makedirs('data', exist_ok=True)
        df.to_csv(path, index=False)
        if not args.no_chart:
            plt.show()


if __name__ == '__main__':
    args = arguments.get()
    print(f'Args: {args}')
    main()
