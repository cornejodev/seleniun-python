# 🗒️ Notes
- In order to avoid `ModuleNotFound` errors when making use of relative imports of modules in other folder levels while using **VSCode** and not Pycharm, do the following:

1. Add a `.env` file containing 
`
  PYTHONPATH=.
`

1. Then this setting in VSCode:
`
{
  "python.envFile": "${workspaceFolder}/.env",
  "python.pythonPath": "${workspaceFolder}/venv/bin/python"
}
`
