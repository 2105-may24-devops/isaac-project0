
#open and write to the file located at path
#get the selector and props items from css reader
#write in the values from css reader to the file 
#and using selector and props items for formatting.
def write_css(path, css):
    with open(path, 'w') as file:
        for selector, props in css.items():
            file.write(f'{selector} {{\n')
            for prop, val in props:
                file.write(f'\t{prop}: {val};\n')
            file.write('}\n\n')
