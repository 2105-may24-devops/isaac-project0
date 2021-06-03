import sys
import reader
import writer

try:
    from blessed import Terminal
    term = Terminal()
except ModuleNotFoundError:
    term.aqua = ''
    term.normal = ''

help_text = '''usage: python py0.py [output | -h] [-f file | -x file | -i | -c] [args]

Modes:
<output> -f <input>
Creates a .css file at <output> from the file at <input>.
Lines in input starting with '-' will indicate the remainder of the line
  is a selector to apply to the following lines
Lines not starting with a '-' should come in pairs, with the first of the pair
  being the property and the second being the value.

<output> -i
Creates a .css file at <output> from an interactive session.
Syntax for interactive entry is the same as for files.

<output> -c [args]
Creates a .css file at <output> from the supplied arguments.
Syntax for argument entry is the same as for files.

<output> -x <input>
Creates a .css file at <output> from an XML file at <input>.
XML should be formatted as <selector> <property> value </property> </selector>

-h
Prints this message.
'''

inline_syntax = f'''{term.aqua}Prefix selectors with '-'.
Put properties and values on seperate lines.
ie.{term.normal}
-p
font-size
12px
-h1
font-size
40px

{term.aqua}Empty line terminates input.
*** to view this message again.{term.normal}
'''

if __name__ == '__main__':
    if len(sys.argv) == 1 or sys.argv[1] == '-h':
        print(help_text)
    else:
        if sys.argv[2] == '-i':
            # Get input lines from interactive input
            print(inline_syntax)
            inlines = []
            while True:
                inline = input()
                if inline == '':
                    break
                if inline == '***':
                    print(inline_syntax)
                else:
                    inlines.append(inline)
            css = reader.construct(inlines)
        elif sys.argv[2] == '-f':
            # Input lines from a file
            css = reader.construct(reader.read_file(sys.argv[3]))
        elif sys.argv[2] == '-c':
            # Input lines from command line arguments
            css = reader.construct(sys.argv[3:])
        elif sys.argv[2] == '-x':
            # Input lines from a file as XML
            css = reader.construct(reader.read_xml(sys.argv[3]))
        else:
            raise Exception(f'Unknown input method {sys.argv[2]}')
        writer.write_css(sys.argv[1], css)
