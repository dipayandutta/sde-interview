import os.path
PATHS = [
    '/one/two/three',
    '/one/two/three/',
    '/',
    '.',
    '',
]
for path in PATHS:
    splited_path=(path.replace("/",""))
    if splited_path != '':
        print(splited_path)
