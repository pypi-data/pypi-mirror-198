import sys
import os
import urllib.request
import loadwave

def main():
    arg = sys.argv[1]
    if ".knu" in arg:
        file_path = sys.argv[1]
        with open(file_path, "r") as f:
            lines = f.readlines()
        im = False
        try:
            # Loop through each line and execute the commands
            for line in lines:
                    line = line.strip()
                    if line.startswith("import") and line.endswith("kenu"):
                        if os.path.isfile(os.path.join(os.environ['APPDATA'], "kenucorp", "modules") + "\\kenu.knu"):
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
                                print("I have found an error. " + line + "\n^^^^^^")
                            
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
    elif sys.argv[1] == "gonder":
            kisi = sys.argv[2]
            print(f"{kisi}'ye hemen kenu atıyorum abi.")
    elif arg == "install":
        modul = sys.argv[2]
        new_folder = os.path.join(os.environ['APPDATA'], "kenucorp", "modules")
        os.makedirs(new_folder, exist_ok=True)
        print("Loading...")
        downloadModule(modul)
        print("The module downloaded successfully.")
@loadwave.process 
def downloadModule(name):
    filepath = os.path.join(os.environ['APPDATA'], "kenucorp", "modules") + f"\\{name}.py"
    urllib.request.urlretrieve("https://kenucorp.com/modules/" + name + ".knu", filepath)