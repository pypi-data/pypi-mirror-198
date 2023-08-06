# -*- coding: utf-8 -*-
import sys
import argparse
from pawnlib.builder.generator import generate_banner
from pawnlib.__version__ import __version__ as _version
from pawnlib.config.globalconfig import pawnlib_config as pawn, pconf
from pawnlib.utils.log import AppLogger
from pawnlib.utils.http import disable_ssl_warnings
from pawnlib.typing import check, converter
from pawnlib.output import *
from pawnlib.output.color_print import *

from toolchains.utils import http
from toolchains.resource import CheckURL, ALLOW_OPERATOR
from pawnlib.typing import date_utils, str2bool, StackList
import time

__version__ = "0.0.1"


def get_parser():
    parser = argparse.ArgumentParser(description='HTTPING')
    parser = get_arguments(parser)
    return parser


def get_arguments(parser):
    parser.add_argument('url', help='url')
    parser.add_argument('-c', '--command', type=str, help=f'command', default=None, choices=["start", "stop", "restart", None])
    parser.add_argument('-v', '--verbose', action='count', help=f'verbose mode. view level', default=0)
    parser.add_argument('-s', '--sleep', type=float, help=f'sleep time seconds. ', default=1)
    parser.add_argument('-m', '--method', type=str, help=f'method. ', default="get")
    parser.add_argument('-t', '--timeout', type=int, help=f'timeout seconds ', default=10)
    parser.add_argument('--success', nargs='+', help=f'timeout. ', default=['status_code==200'])

    return parser


def check_url_process():
    check_url = CheckURL(
        url=pconf().args.url,
        method=pconf().args.method,
        # headers={
        #     'Content-Type': "application/json",
        #     # 'Content-Type': "application/x-www-form-urlencoded",
        #     # 'User-Agent': "CheckURL"
        # },
        timeout=pconf().args.timeout * 1000,
        ignore_ssl=False,
        # data={
        #     "jinwoo": "asdasd"
        # }
        # success_criteria=[
        #     ["status_code", ">=", 200],
            # ["timing.total", "<", 1]
        # ],
        # success_operator="and",
        success_criteria=pconf().args.success,
        success_operator="and",
    )

    pawn.increase(total_count=1)

    if pconf().args.verbose == 0:
        check_url.response.text = ""

    response_time = int(check_url.response.timing.get('total') * 1000)
    pconf().data.response_time.push(response_time)

    avg_response_time = f"{pconf().data.response_time.mean():.2f}"
    status_code = check_url.response.status_code

    message = f"<{pconf().fail_count}/{pconf().total_count}> url={pconf().args.url}, status_code={status_code}, {response_time}ms (avg: {avg_response_time})"

    if pconf().args.verbose > 0:
        message = f"{message} - {check_url.response}"

    if check_url.is_success():
        pawn.console.log(f"[green][ OK ][/green] {message}")
    else:
        pawn.increase(fail_count=1)
        pawn.console.log(f"[red][FAIL] {message} [/red]")


    # pawn.console.log(res)

def convert_list_criteria(arguments):
    result = []
    for argument in arguments:
        criteria = convert_criteria(argument)
        if criteria:
            result.append(criteria)
    return result

def convert_criteria(argument):
    for operator in ALLOW_OPERATOR:
        if operator in argument:
            result = argument.split(operator)
            if any( word in result[0] for word in ALLOW_OPERATOR + ['=']):
                pawn.console.log(f"[red]Invalid operator - '{argument}', {result}")
                sys.exit(-1)
            result.insert(1, operator)
            return result
    return False

def _find_operator(operator, argument):
    if operator in argument:
        res = argument.split(operator)
        pawn.console(res)
        return operator, argument

def main():
    banner = generate_banner(
        app_name="HTTPING",
        author="jinwoo",
        description="http ping",
        font="graffiti",
        version=f"{__version__} - pawn({_version})"
    )
    print(banner)
    # pawn_http.disable_ssl_warnings()
    parser = get_parser()
    args, unknown = parser.parse_known_args()

    pawn.console.log(args)

    args.success = convert_list_criteria(args.success)

    if len(args.success) == 0:
        sys.exit(f"Invalid arguments with success criteria = {args.success}")
    pawn.console.log(f"success criteria = {args.success}")

    args.try_pass = False
    pawn.set(
        args=args,
        try_pass=False,
        last_execute_point=0,
        data={
            "response_time": StackList()
        },
        fail_count=0,
        total_count=0,
    )



    if args.verbose > 2:
        pawn.set(PAWN_DEBUG=True)

    while True:
        check_url_process()
        time.sleep(args.sleep)



if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        pawn.console.log(f"[red] Error {e}")
