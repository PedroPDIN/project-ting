import sys


def txt_importer(path_file):
    try:
        list_character_path = path_file.split('.')
        last_index = len(list_character_path) - 1
        current_values = []
  
        if list_character_path[last_index] != 'txt':
            return sys.stderr.write("Formato inválido\n")
  
        with open(path_file) as file:
            lines = file.readlines()
            print(lines)
  
            for line in lines:
            
                current_values.append(line.strip("\n"))
  
        return current_values
    except FileNotFoundError:
        return sys.stderr.write(f"Arquivo {path_file} não encontrado\n")
