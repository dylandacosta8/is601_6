import importlib, pkgutil
import os
from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self, a, b):
        pass #TODO

    @abstractmethod
    def help(self):
        pass #TODO

class PluginManager:
    def __init__(self):
        self.plugins = {}

    def load_plugins(self):
        # Path to the plugins directory
        plugins_dir = "calculator.plugins"

        # Automatically discover and load command plugins
        for module_name in self.list_command_modules(plugins_dir):
            try:
                # Import the module
                module = importlib.import_module(f"{plugins_dir}.{module_name}")
                # Get the command class (assumed to be named <ModuleName>Command)
                command_class = getattr(module, f"{module_name.capitalize()}Command")
                command_instance = command_class()
                
                # Use the module name as the command key
                self.plugins[module_name] = command_instance
            except Exception as e: #TODO
                print(f"Failed to load command '{module_name}': {e}") #TODO

    def list_command_modules(self, package):
        # Returns a list of command modules in the specified package
        return [name for _, name, _ in pkgutil.iter_modules([package.replace('.', os.sep)])]

    def get_command(self, command_name):
        return self.plugins.get(command_name)

    def list_plugins(self):
        return self.plugins.keys()
