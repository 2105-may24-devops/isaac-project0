import re

def read_file(path):
    with open(path, 'r') as file:
        # Simply return the lines with newlines stripped
        return (l.rstrip() for l in file.readlines() if l != '\n')

def read_xml(path):
    # This is a temporary algorithm
    # Hopefully I can write an actual XML parser at a later time
    with open(path, 'r') as file:
        f = ''.join(file.readlines())
    tokens = (t.strip() for t in re.split(r'[<>]', f) if t.strip())
    
    lines = []
    selector = None
    prop = None
    
    for token in tokens:
        if not selector:
            selector = token
            lines.append(f'-{selector}')
        elif token[0] == '/':
            if token == '/' + selector:
                if prop: # Tags closed out of order
                    raise Exception('Invalid XML: Tag closed out of order')
                selector = None
            elif token == '/' + prop:
                prop = None
            else:
                raise Exception('Invalid XML: Unknown tag closed')
        elif not prop:
            prop = token
            lines.append(f'{prop}')
        else:
            lines.append(f'{token}')
    else:
        if selector or prop: # At least one tag not closed
            raise Exception('Invalid XML: File ended before tag closed')
    
    return lines

def construct(lines):
    '''Constructs a dictionary of css properties from a list of input lines.
    Input line syntax explained in p0.inline_syntax
    '''
    css = {}
    selector = None
    prop = None
    for line in lines:
        if line[0] == '-': # Update the selector
            if prop == None: # Only update if syntax is correct
                selector = line[1:]
            else: # Error out if we have a property with no value
                raise Exception(f'Unmatched property {prop}')
        else:
            if prop: # We have a property, so this is a value
                if selector in css: # Append the prop/val pair to the selector
                    css[selector].append((prop, line))
                else: # Or create it if it doesn't exist
                    css[selector] = [(prop, line)]
                prop = None # The next line will be a property
            else: # This line will be a property
                prop = line
    else: # Make sure the final property has been matched
        if prop is not None:
            raise Exception(f'Unmatched property {prop}')
            
    return css