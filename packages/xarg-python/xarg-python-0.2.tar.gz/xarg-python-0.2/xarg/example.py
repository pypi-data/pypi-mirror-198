#!/usr/bin/python3
# coding:utf-8
# Copyright (c) 2023 ZouMingzhe <zoumingzhe@qq.com>

from xarg import xarg


def main():
    _arg = xarg("xarg-hello",
                description="hello the world",
                epilog="This is the xarg project test command-line.")
    _arg.add_subparsers()
    _sub = _arg.add_parser("opt")
    _sub.add_opt("-x")
    _sub.add_opt("-arg")
    _sub.add_opt("-o", "--opt")
    _sub = _arg.add_parser("opt-on")
    _sub.add_opt_on("--opt-on")
    _sub = _arg.add_parser("opt-off")
    _sub.add_opt_off("--opt-off")
    _sub = _arg.add_parser("pos-default")
    _sub.add_pos("pos")
    _sub = _arg.add_parser("pos-1")
    _sub.add_pos("pos_1", 1)
    _sub = _arg.add_parser("pos-2")
    _sub.add_pos("pos_2", 2)
    _sub = _arg.add_parser("pos-0+")
    _sub.add_pos("pos_0+", 0)
    _sub = _arg.add_parser("pos-1+")
    _sub.add_pos("pos_1+", -1)
    _sub = _arg.add_parser("pos-0-or-1")
    _sub.add_pos("pos_0_or_1")
    print(_arg.parse_args())
