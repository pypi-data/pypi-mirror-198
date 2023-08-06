import os
import urllib.request

class compileknu:
    def compile(file_path):
        
        with open(file_path, "r") as f:
            lines = f.readlines()

        im = False
        functions = {}  # A dictionary to store defined functions and their code
        try:
            # Loop through each line and execute the commands
            for line in lines:
                line = line.strip()
                if line.startswith("import") and line.endswith("kenu"):
                    im = True
                elif line.startswith("os.downloadFile"):
                    if im:
                        if '(' in line and ',' in line:
                            start_index = line.find('(') + 1
                            end_index = line.find(',', start_index)
                            url = line[start_index:end_index]
                            start_index = line.find(',') + 1
                            end_index = line.find(')', start_index)
                            filepath = line[start_index:end_index]
                            urllib.request.urlretrieve(url, filepath)
                elif line.startswith("os.cmd"):
                    if im:
                        if '(' in line:
                            start_index = line.find('(') + 1
                            end_index = line.find(')', start_index)
                            result = line[start_index:end_index]
                            if '"' in result:
                                start_index = line.find('"') + 1
                                end_index = line.find('"', start_index)
                                result = line[start_index:end_index]
                                os.system(result)
                            else:
                                exec(f"os.system({result})")
                        else:
                            print("There was an error while saying that.")
                    else:
                        print("There was an error while saying that. Could you have forgotten to import a module?")
                elif line.startswith("print(") and line.endswith(")"):
                    if im:
                        if '"' in line:
                            start_index = line.find('"') + 1
                            end_index = line.find('"', start_index)
                            result = line[start_index:end_index]
                            exec(f"print('{result}')")
                        elif '(' in line:
                            start_index = line.find('(') + 1
                            end_index = line.find(')', start_index)
                            result = line[start_index:end_index]
                            exec(f"print({result})")
                        else:
                            print("I have found an error. " + line + "\n                     ^^^^^^")
                        
                    else:
                        print("There was an error while saying that. Could you have forgotten to import a module?")
                elif line.startswith("!"):
                    # Check if line starts with "!", which indicates a variable assignment
                    if im:
                        variable_name, value = line[1:].split("=")
                        value = value.strip()
                        # Check if value is enclosed in quotes
                        if value.startswith('"') and value.endswith('"'):
                            value = value[1:-1]
                            exec(f"{variable_name} = '{value}'")
                        else:
                            exec(f"{variable_name} = {value}")
                    else:
                        print("There was an error while saying that. Could you have forgotten to import a module?")
                elif line.startswith("func "):
                    # Check if line defines a function
                    if im:
                        start_index = line.find(' ') + 1
                        end_index = line.find('(', start_index)
                        function_name = line[start_index:end_index]
                        function_body = line[end_index+1:-1]
                        functions[function_name] = function_body
                    else:
                        print("There was an error while saying that. Could you have forgotten to import a module?")
                elif line.startswith("}"):
                    # Check if line closes a function definition
                    if in_func:
                        in_func = False
                        func_body.append(line)
                        # Join the function body lines to create a single string
                        func_body_str = "\n".join(func_body)
                        # Add the function to the functions dictionary
                        functions[func_name] = func_body_str
                        # Reset the function name and body
                        func_name = ""
                        func_body = []
                    else:
                        print("Unexpected '}' found.")
                elif in_func:
                    # If currently inside a function definition, add the line to the function body
                    func_body.append(line)
                elif line.startswith("def "):
                    # Check if line defines a new function
                    if "(" in line and ")" in line:
                        # Extract the function name and parameters from the line
                        start_index = line.find("def ") + len("def ")
                        end_index = line.find("(")
                        func_name = line[start_index:end_index].strip()
                        params_start_index = end_index + 1
                        params_end_index = line.find(")")
                        params = line[params_start_index:params_end_index].strip()

                        # Add the function name and parameters to the functions dictionary
                        functions[func_name] = {"params": params, "body": []}
                        # Set in_func flag to True
                        in_func = True
                    else:
                        print("Invalid function definition: " + line)
                elif line.startswith("print(") and line.endswith(")"):
                    # Check if line prints the result of a function call
                    if im:
                        if '"' in line:
                            start_index = line.find('"') + 1
                            end_index = line.find('"', start_index)
                            result = line[start_index:end_index]
                            exec(f"print('{result}')")
                        elif '(' in line:
                            start_index = line.find('(') + 1
                            end_index = line.find(')', start_index)
                            func_call = line[start_index:end_index]
                            func_name = func_call.split("(")[0]
                            if func_name in functions:
                                # Get the function parameters from the line
                                params = func_call[len(func_name)+1:-1]
                                if len(params) == 0:
                                    # Call the function with no arguments
                                    result = exec(functions[func_name]["body"])
                                    print(result)
                                else:
                                    # Call the function with arguments
                                    result = exec(f"functions['{func_name}']['body']({params})")
                                    print(result)
                            else:
                                print("Function not defined: " + func_name)
                        else:
                            print("Invalid print statement: " + line)
                    else:
                        print("There was an error while saying that. Could you have forgotten to import a module?")
                elif line.startswith("!"):
                    # Check if line starts with "!", which indicates a variable assignment
                    if im:
                        variable_name, value = line[1:].split("=")
                        value = value.strip()
                        # Check if value is enclosed in quotes
                        if value.startswith('"') and value.endswith('"'):
                            value = value[1:-1]
                            exec(f"{variable_name} = '{value}'")
                        else:
                            exec(f"{variable_name} = {value}")
                    else:
                        print("There was an error while saying that. Could you have forgotten to import a module?")
                elif "" in line:
                    pass
                else:
                    print("Invalid command: " + line)
        except:
            pass
        # Return the functions dictionary
        return functions

