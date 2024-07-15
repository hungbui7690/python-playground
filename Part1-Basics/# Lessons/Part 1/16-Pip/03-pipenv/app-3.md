# Resolving the Unresolved Import Warning in VS Code

If you’re using VS Code, you may receive an unresolved import warning. The reason is that the VS code doesn’t know which Python interpreter to use.

Therefore, you need to switch the Python interpreter to the one located in the new virtual environment:

First, click the current Python interpreter at the right bottom corner of the VS Code:

![img](https://www.pythontutorial.net/wp-content/uploads/2020/10/Python-pipenv-VS-code-configuration.png)


Second, select the Python interpreter from the list:

![img](https://www.pythontutorial.net/wp-content/uploads/2020/10/Python-pipenv-select-Python-Interpreter.png)

In addition, you need to change the python.jediEnabled parameter in the settings.json to True:

To open the settings.json file, you open the Command Palette with the keyboard shortcut `CTRL + SHIFT + P` on Windows or `CMD + SHIFT + P` on macOS:

![img](https://www.pythontutorial.net/wp-content/uploads/2020/10/Python-pipenv-open-settings-JSON-format.png)

And the change the value to True as follows:

![img](https://www.pythontutorial.net/wp-content/uploads/2020/10/Python-pipenv-python.jediEnabled-True.png)

After that, you should save the file and restart the VS Code for the change.