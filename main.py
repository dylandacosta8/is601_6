import concurrent.futures
from calculator.plugins import PluginManager
from decimal import Decimal

# REPL function
def repl():
    # Initialize the PluginManager and load plugins
    plugin_manager = PluginManager()
    plugin_manager.load_plugins()

    # Display menu function
    def display_menu():
        print("\nAvailable plugins:")
        for command in plugin_manager.list_plugins():
            print(f" - {command}")
        print("\nExample input: add 5 3")

    # Display the menu when the application starts
    display_menu()

    while True:
        user_input = input("\nEnter command (e.g., add 5 3) or 'menu' to see options or 'exit' to quit: ").strip().lower()

        if user_input == "exit":
            print("Exiting the calculator. Goodbye!")
            break
        elif user_input == "menu":
            display_menu()
            continue

        try:
            operation, value1, value2 = user_input.split()

            # Convert values to Decimal
            value1 = Decimal(value1)
            value2 = Decimal(value2)

            # Check if the operation is valid
            command_instance = plugin_manager.get_command(operation)
            if command_instance is None:
                print("Invalid operation. Type 'menu' to see available plugins.")
                continue

            # Execute the command in a separate process
            with concurrent.futures.ProcessPoolExecutor() as executor:
                future = executor.submit(command_instance.execute, value1, value2)
                result = future.result()  # This will block until the result is available

            print(f"Result: {result}")

        except ValueError:
            print("Invalid input. Please enter valid numbers and an operation.")
        except ZeroDivisionError:
            print("Error: Division by zero.")
        except Exception as e:
            print(f"An error occurred: {e}")

# Starting the REPL
if __name__ == "__main__":
    repl()
