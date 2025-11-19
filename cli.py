#!/usr/bin/env python3
"""
CLI interface for itersys package.
"""

import sys
import json
import argparse
from itersys.iteration import chunk, flatten


def chunk_cmd(args):
    """Handle chunk command."""
    try:
        # Parse input as JSON list
        data = json.loads(args.input)
        if not isinstance(data, list):
            print("Error: Input must be a JSON array", file=sys.stderr)
            sys.exit(1)
        
        size = int(args.size)
        result = list(chunk(data, size))
        print(json.dumps(result))
    except json.JSONDecodeError:
        print("Error: Invalid JSON input", file=sys.stderr)
        sys.exit(1)
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


def flatten_cmd(args):
    """Handle flatten command."""
    try:
        # Parse input as JSON (can be nested array)
        data = json.loads(args.input)
        result = list(flatten(data))
        print(json.dumps(result))
    except json.JSONDecodeError:
        print("Error: Invalid JSON input", file=sys.stderr)
        sys.exit(1)


def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        description="itersys - Iterator and algorithm helpers CLI",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Chunk a list
  itersys chunk --input '[1,2,3,4,5]' --size 2
  # Output: [[1,2],[3,4],[5]]

  # Flatten a nested list
  itersys flatten --input '[1,[2,3],[4,[5]]]'
  # Output: [1,2,3,4,5]
        """
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Command to execute')
    
    # Chunk command
    chunk_parser = subparsers.add_parser('chunk', help='Chunk an iterable into smaller pieces')
    chunk_parser.add_argument('--input', required=True, help='JSON array to chunk')
    chunk_parser.add_argument('--size', required=True, type=int, help='Size of each chunk')
    chunk_parser.set_defaults(func=chunk_cmd)
    
    # Flatten command
    flatten_parser = subparsers.add_parser('flatten', help='Flatten a nested iterable')
    flatten_parser.add_argument('--input', required=True, help='JSON array to flatten')
    flatten_parser.set_defaults(func=flatten_cmd)
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        sys.exit(1)
    
    args.func(args)


if __name__ == '__main__':
    main()

