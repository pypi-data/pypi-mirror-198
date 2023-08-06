#!/usr/bin/python3
# coding=utf-8

from xarg import xarg

from git import Repo
from git import Commit
from typing import Iterator


def cmd_summary(_arg):
    _arg.add_opt('-r',
                 '--repo',
                 type=str,
                 nargs=1,
                 default=['.'],
                 help="specify repo path")
    _arg.add_opt('-b',
                 '--branch',
                 type=str,
                 nargs=1,
                 default=[None],
                 help="specify branch")
    # TODO: author option and datetime option
    _arg.add_opt('--author',
                 type=str,
                 nargs=1,
                 default=[None],
                 help="specify author")
    _arg.add_opt_on('-d', '--debug', help="show debug information")
    _arg.add_opt_on('--short', help="show prefix, default full 40-byte")
    _arg.add_opt_on('--datetime', help="show datetime, default show date")
    _arg.add_opt_on('--author-email', help="show author email")
    _arg.add_opt_on('--committer', help="show committer name")
    _arg.add_opt_on('--committer-email', help="show committer name and email")
    _arg.add_pos("path", 0, type=str, help="Commit with folder or file path")


def exec_summary(args):
    index = 0
    _repo = Repo(args.repo[0])
    _branch = args.branch[0]
    _author = args.author[0]
    # kwargs = {"author": args.author, "filter": args.path, "no_merges": True}
    kwargs = {"author": _author, "no_merges": True}
    _iter_commits = _repo.iter_commits(_branch, args.path, **kwargs)
    for commit in _iter_commits:
        index += 1
        _hexsha = commit.hexsha
        _datetime_format = {
            "date": '%Y-%m-%d',
            "datetime": '%Y-%m-%d %H:%M:%S',
        }["datetime" if args.datetime else "date"]
        _datetime = commit.committed_datetime.strftime(_datetime_format)
        _author = ("{} <{}>" if args.author_email else "{}").format(
            commit.author.name, commit.author.email)
        if args.committer or args.committer_email:
            _committer = ("{} <{}>" if args.committer_email else "{}").format(
                commit.committer.name, commit.committer.email)
            _author = "{}, {}".format(_author, _committer)
        _summary = commit.summary
        # _message = commit.message
        if args.short:
            _hexsha = _repo.git.rev_parse(_hexsha, short=9)
        _commit_info = f"{index}, {_hexsha}, {_datetime}, {_author}, {_summary}"
        print(_commit_info)


def main():
    _arg = xarg("xgit-summary", description="list commit summary")
    cmd_summary(_arg)
    args = _arg.parse_args()
    exec_summary(args)
