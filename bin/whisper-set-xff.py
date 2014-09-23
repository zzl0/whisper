#!/usr/bin/env python

import os
import sys
import optparse

try:
    import whisper
except ImportError:
    raise SystemExit('[ERROR] Please make sure whisper is installed properly')


def set_xff(path, xff):
    with open(path) as f:
        header = whisper.__readHeader(f)
        agg_method = header['aggregationMethod']
        old_xff = header['xFilesFactor']

    try:
        whisper.setAggregationMethod(path, agg_method, xff)
    except IOError as e:
        sys.stderr.write("[ERROR] file '%s' not exist!\n" % path)
        option_parser.print_help()
        sys.exit(1)
    except whisper.WhisperException as e:
        raise SystemExit("[ERROR] %s" % e)

    print 'update xff: %s (%s -> %s)' % (path, old_xff, xff)


def main():
    usage="%%prog path <xFilesFactor>"
    option_parser = optparse.OptionParser(usage=usage)
    options, args = option_parser.parse_args()

    if len(args) < 2:
        option_parser.print_help()
        sys.exit(1)

    path, xff = args
    set_xff(path, xff)


if __name__ == '__main__':
    main()