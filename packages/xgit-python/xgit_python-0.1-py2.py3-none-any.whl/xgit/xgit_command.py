#!/usr/bin/python3
# coding=utf-8

from xarg import xarg

from .xgit_summary import cmd_summary
from .xgit_summary import exec_summary


def sub_command(args):
    if args.debug:
        print(args)
    {
        "summary": exec_summary,
    }[args.sub](args)


def main():
    _arg = xarg(
        "xgit",
        description="Git tool based on GitPython",
        epilog="For more, please visit https://github.com/zoumingzhe/xgit")
    _arg.add_opt_on('-d', '--debug', help="show debug information")
    _arg.add_subparsers(dest="sub", required=True)
    cmd_summary(_arg.add_parser("summary"))
    args = _arg.parse_args()
    sub_command(args)
