
def write_css(path, css):
    with open(path, 'w') as file:
        for selector, props in css.items():
            file.write(f'{selector} {{\n')
            for prop, val in props:
                file.write(f'\t{prop}: {val};\n')
            file.write('}\n\n')
