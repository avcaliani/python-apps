from argparse import ArgumentParser


def get():
    parser = ArgumentParser(description='🐍 Py Ping')
    parser.add_argument(
        '--duration',
        dest='duration',
        default=60 * 60 * 24,
        type=int,
        help='Execution duration in seconds. Default 24h.'
    )
    parser.add_argument(
        '--cmd',
        dest='command',
        default='ping -t 1 <HOST>',
        help='Ping command. Instead of specifying the IP set it as <HOST>.'
    )
    parser.add_argument(
        '--pattern',
        dest='result_pattern',
        default=r'.*time=(\d+\.?\d*)\sms',
        help='RegExp pattern to capture latency.'
    )
    parser.add_argument(
        '--hosts',
        dest='hosts',
        nargs='+',
        default=['8.8.8.8', '8.8.4.4'],
        help='Hosts.'
    )
    parser.add_argument(
        '--sleep',
        dest='sleep_time',
        default=1,
        type=int,
        help='Sleep time between requests in seconds.'
    )
    parser.add_argument(
        '--max-ping',
        dest='max_acceptable_latency',
        default=70,
        type=int,
        help='Max acceptable latency in ms.'
    )
    parser.add_argument(
        '--no-chart',
        dest='no_chart',
        nargs='?',
        type=bool,
        const=True,
        default=False,
        help='Disable chart.'
    )
    return parser.parse_args()
