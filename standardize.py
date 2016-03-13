#!/usr/bin/python

import argparse

def standardize(args):
  with open(args.input_file, 'r') as fp:
    names = [line.lower() for line in fp.read().splitlines()
             if not line.startswith('#')]
  snames = set()
  for name in names:
    parts = name.split(' ')
    if len(parts) == 1:
      snames.add(parts[0])
      continue
    assert len(parts) == 2, name
    snames.add('%s %s' % (parts[0], parts[1]))
    snames.add('%s%s' % (parts[0], parts[1]))
  with open(args.output_file, 'w') as fp:
    for name in sorted(snames):
      print >> fp, name

def main():
  parser = argparse.ArgumentParser()
  parser.add_argument('--input_file', required=True)
  parser.add_argument('--output_file', required=True)
  standardize(parser.parse_args())

if __name__ == '__main__':
  main()

