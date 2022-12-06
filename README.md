# py-cmd-react

## Description
Python command line module to automatically create a minimal and basic react template

This app it's just tested on windows system.

- standard library modules used:
 - sys : build in module to manage specific parameters and function from the system.

 - pathlib : build-in module to manage file paths as objects.

- shutil : build-in module to manage  high level operations like copy files or directories.

- os : build-in module used as interface of the operative system.

- webbrowser : build-in module that provides high-level interface to manage a browser.

## Setup

- Clone the repository anywhere in your local machine.

- Create a new system variable from envirorment variables named : PYTHONPATH
- Add the directory to PYTHONPATH to allow python have access to the module globally by using:
  `python -m module_name`

- Create another folder where you want to create the React project.

- Open the terminal inside this new folder and type: `python -m react`

- Wait until everything is set and a browser window will be open.

## Setup Troubles
- If you want to use the `--scope=global`, make sure to install the next requirements:

  ```
  npm i -g react react-dom react-router-dom
  
  npm i -g @babel/core @babel/preset-env @babel/preset-react @babel/core @babel/preset-env @babel/preset-react
  
  npm i -g webpack webpack-cli webpack-dev-server html-webpack-plugin
  
  npm i -g babel-loader css-loader style-loader sass-loader file-loader
  ```
  if you want to use the `--pkg_mgr=pnpm` then change the requirement commands from npm to pnpm.
  
  PNPM will be much faster and less error verbose while setting up the project.

## Arguments:

- scope :
  - --scope=global ( default )
  - --scope=local
- pkg_mgr ( package managner ) :
  - --pkg_mgr=npm ( default )
  - --pkg_mgr=pnpm

## Future Work
-

## Screenshots
#### Picking color
