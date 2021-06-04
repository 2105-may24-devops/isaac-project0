
def write_css(path, css):
    '''Writes a .css file from the output of reader.construct()
    
    ---
    path:
        Path to the .css file to be written
        
    css:
        Dictionary of css to be written.
        Syntax:
            {
                'selector': [('property1', 'value1'), ('prop2', 'val2')],
                'sel2': [('prop3', 'val3')]
            }
    '''
    with open(path, 'w') as file:
        for selector, props in css.items():
            file.write(f'{selector} {{\n')
            for prop, val in props:
                file.write(f'\t{prop}: {val};\n')
            file.write('}\n\n')
