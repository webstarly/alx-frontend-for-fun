#!/usr/bin/python3

import sys


def convert_markdown_to_html(markdown_file, output_file):
    '''markdown to html'''
    try:
        with open(markdown_file, 'r') as md_file:
            markdown_text = md_file.read()
            html_content = "<html><body>" + markdown_text + "</body></html>"

            with open(output_file, 'w') as html_file:
                html_file.write(html_content)
    except FileNotFoundError as e:
        sys.stderr.write(f"Missing {e.filename}\n")
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.stderr.write("Usage: ./markdown2html.py README.md README.html\n")
        sys.exit(1)

    markdown_file = sys.argv[1]
    output_file = sys.argv[2]

    convert_markdown_to_html(markdown_file, output_file)
    sys.exit(0)
