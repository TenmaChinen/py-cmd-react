import os, sys, shutil, json, webbrowser
from pathlib import Path

l_args = sys.argv[1:]
d_params = {'scope':'local', 'pkg_mgr':'npm'}
# d_params = {'scope':'global', 'pkg_mgr':'pnpm'}
d_options = {'scope':['global','local'], 'pkg_mgr':['npm','pnpm']}

for arg in l_args:
    if arg.__contains__('--') and arg.__contains__('='):
        arg = arg.strip('--')
        key, value = arg.split('=')
        if key in d_params and value in d_options[key]:
            d_params[key] = value
            continue

    print(f'\n    Arg : {arg} is not valid\n\n    Params must be:')
    for key in d_params.keys():
        values = ' or '.join(d_options[key])
        print(f'        --{key}={values}')
    print()
    sys.exit()

SRC_DIR = Path(__file__).resolve().parent / 'files'
DST_DIR = Path(os.getcwd()).resolve()

for file_name in os.listdir(SRC_DIR):
    src_file_path = SRC_DIR / file_name
    dst_file_path = DST_DIR / file_name
    if os.path.isfile(src_file_path):
        shutil.copy(src=src_file_path, dst=dst_file_path)
    elif os.path.isdir(src_file_path):
        shutil.copytree(src=src_file_path, dst=dst_file_path)

pkg_mgr = d_params['pkg_mgr']

if pkg_mgr == 'npm':
    os.system('npm init -y')
else:
    os.system('pnpm init')

with open('package.json','r+') as file:
    data = json.load(file)
    data['scripts'] = {
        'start' : 'webpack-dev-server --mode=development',
        'build' : 'webpack --mode=production'
        }
    file.seek(0)
    json.dump(data, file, indent=4)

# install sass for sass-loader

str_react_libs = 'react react-dom react-router-dom'
str_babel_libs = '@babel/core @babel/preset-env @babel/preset-react'
str_webpack_libs = 'webpack webpack-cli webpack-dev-server html-webpack-plugin'
str_loaders_libs = 'babel-loader css-loader style-loader file-loader sass sass-loader '

if d_params['scope'] == 'local':
    os.system(f'{pkg_mgr} i {str_react_libs} --S')
    os.system(f'{pkg_mgr} i {str_babel_libs} {str_webpack_libs} {str_loaders_libs} --D')
else:
    if pkg_mgr == 'npm':
        os.system(f'npm link {str_react_libs} {str_babel_libs} {str_webpack_libs} {str_loaders_libs}')
    else:
        os.system(f'pnpm link -g {str_react_libs} {str_babel_libs} {str_webpack_libs} {str_loaders_libs}')


webbrowser.open('http://localhost:8080/home')
os.system(f'{pkg_mgr} run start')