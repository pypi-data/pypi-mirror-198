#!/usr/bin/python3
# coding:utf-8
# Copyright (c) 2023 ZouMingzhe <zoumingzhe@qq.com>

__version__ = "0.2"

import argparse


class xarg_parser():
    '''
    '''

    def __init__(self, argument_parser):
        assert type(argument_parser) is argparse.ArgumentParser
        self.__argument_parser = argument_parser

    # @staticmethod
    def check_name_opt(fn):
        '''
        check optional argument name
        '''

        def inner(self, *name, **kwargs):
            # 1. check short form optional argument ('-x')
            # 2. check long form optional argument ('--xx')
            # 3. only short form or long form or short form + long form
            # 模棱两可的数据（-1可以是一个负数的位置参数）
            # assert short_name is not None or long_name is not None
            # assert short_name is None or (type(short_name) is str and
            #                               short_name[0] == '-'), "short_name"
            # assert long_name is None or (type(long_name) is str and
            #                              long_name[:2] == '--'), "long_name"
            return fn(self, *name, **kwargs)

        return inner

    # @staticmethod
    def check_name_pos(fn):
        '''
        check positional argument name
        '''

        def inner(self, name, *args, **kwargs):
            assert type(
                name) is str and name[0] != '-', "positional argument name"
            return fn(self, name, *args, **kwargs)

        return inner

    @check_name_opt
    def add_opt(self, *name, **kwargs):
        '''
        '''
        self.__argument_parser.add_argument(*name, **kwargs)

    @check_name_opt
    def add_opt_on(self, *name, **kwargs):
        '''
        boolean optional argument, default value is False
        '''
        kwargs.update({
            "action": 'store_true',
        })
        for key in ("type", "nargs", "const", "default", "choices"):
            if key in kwargs:
                kwargs.pop(key)
        self.__argument_parser.add_argument(*name, **kwargs)

    @check_name_opt
    def add_opt_off(self, *name, **kwargs):
        '''
        boolean optional argument, default value is True
        '''
        kwargs.update({
            "action": 'store_false',
        })
        for key in ("type", "nargs", "const", "default", "choices"):
            if key in kwargs:
                kwargs.pop(key)
        self.__argument_parser.add_argument(*name, **kwargs)

    @check_name_pos
    def add_pos(self, name, nargs=-2, **kwargs):
        '''
        nargs < -1: '?' (0 or 1), default value
        nargs = -1: '+' (1+)
        nargs = 0: '*' (0+)
        nargs > 0: n
        default type is str
        '''
        _nargs = {0: '*', -1: '+'}
        assert type(nargs) is int, """nargs must be int,
    nargs < -1: 0 or 1 ('?') positional argument, default value
    nargs = -1: 1+ ('+') positional argument
    nargs = 0: 0+ ('*') positional argument
    nargs > 0: n positional argument"""
        kwargs.update({
            "nargs": nargs if nargs > 0 else _nargs.get(nargs, '?'),
        })
        self.__argument_parser.add_argument(name, **kwargs)

    def parse_args(self, *args, **kwargs) -> argparse.Namespace:
        '''
        '''
        args = self.__argument_parser.parse_args(*args, **kwargs)
        return args


class xarg(xarg_parser):
    '''
    '''

    def __init__(self, prog=None, **kwargs):
        kwargs.update({"prog": prog})
        self.__xarg = argparse.ArgumentParser(**kwargs)
        xarg_parser.__init__(self, self.__xarg)
        self.__xsub = None
        self.__subs = {}

    def add_subparsers(self, *args, **kwargs):
        '''
        subparsers
        '''
        # subparser: cannot have multiple subparser arguments
        assert self.__xsub is None
        self.__xsub = self.__xarg.add_subparsers(*args, **kwargs)

    def add_parser(self, sub_cmd, **kwargs) -> xarg_parser:
        '''
        subparsers
        '''
        assert type(self.__xsub) is argparse._SubParsersAction
        if sub_cmd in self.__subs:
            _sub = self.__subs[sub_cmd]
            assert type(_sub) is xarg_parser
            return _sub
        _sub_parser = self.__xsub.add_parser(sub_cmd, **kwargs)
        return self.__subs.setdefault(sub_cmd, xarg_parser(_sub_parser))
