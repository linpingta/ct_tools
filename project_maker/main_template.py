#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set bg=dark noet ts=4 sw=4 fdm=indent :

# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree. An additional grant
# of patent rights can be found in the PATENTS file in the same directory.

""" Template Main Function"""
__author__ = 'linpingta@163.com'

import os
import sys

try:
    import ConfigParser
except ImportError:
    import configparser as ConfigParser
import logging
import argparse

if __name__ == '__main__':

    try:
        script_name = os.path.splitext(os.path.basename(__file__))[0]
        logging.basicConfig(filename=os.path.join(os.path.abspath(sys.path[0]), 'logs/' + script_name + '.log'),
                            level=logging.DEBUG,
                            format='[%(filename)s:%(lineno)s - %(funcName)s %(asctime)s;%(levelname)s] %(message)s',
                            datefmt='%a, %d %b %Y %H:%M:%S'
                            )
        logger = logging.getLogger('Base')
        conf_path = os.path.join(os.path.join(os.path.abspath(sys.path[0]), 'conf/%s.conf' % script_name))
        conf = ConfigParser.RawConfigParser()
        conf.read(conf_path)

        example_word = """example:
            DESCRIBE YOUR EXAMPLE HERE
            python base.py -t argument1
        """

        parser = argparse.ArgumentParser(prog='base', description='base template', epilog=example_word,
                                         formatter_class=argparse.RawDescriptionHelpFormatter)
        # add parameter if needed
        parser.add_argument('-t', '--template', help='argument description here', type=str)
        args = parser.parse_args()

        # main function
        print "Hello, World"

    except argparse.ArgumentTypeError as e:
        logger.exception(e)
    except Exception as e:
        logger.exception(e)
