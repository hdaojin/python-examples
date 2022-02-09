# Python命令行选项

## getopt

```python
import getopt
if len(sys.argv) < 2:
    usage()
    sys.exit(1)
    try:
        opts, args = getopt.getopt(sys.argv[1:], 'ht:', ['help', 'template='])
    except getopt.GetoptError as err:
        print(err)
        usage()
        sys.exit(2)
#    output = None
#    verbose = False
    for opt, arg in opts:
        if opt in ('-h', '--help'):
            usage()
            sys.exit()
        elif opt in ('-t', '--template'):
            section = arg
            print(section)
```


## argparse

```python
    parser = argparse.ArgumentParser(
        description="Markdown file coverted to html and pdf file with python-markdown2 and wkhtmltopdf", formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('-v', '--version', action='version',
                        version='%(prog)s {}'.format(str(Version)))
    parser.add_argument('-t', '--template', required=False, nargs='?', const='DEFAULT', default='DEFAULT',
                        help='select a HTML template: {}\n(default: %(default)s)'.format(get_sections()))
    parser.add_argument('-i', required=True,
                        metavar='markdown_file', help='input a markdown file')
    parser.add_argument('-o', metavar='directory',
                        default='.', help='output directory\n(default: current directory)')
    args = parser.parse_args()

    md_file = Path(args.i)
    output_dir = Path(args.o)
    template = args.template
```