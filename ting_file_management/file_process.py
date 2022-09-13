import sys
from ting_file_management.file_management import txt_importer

def process(path_file, instance):
    list_file = txt_importer(path_file)
    if path_file not in instance._data:
      instance.enqueue(path_file)

      return sys.stdout.write(str({
          "nome_do_arquivo": path_file,
          "qtd_linhas": len(list_file),
          "linhas_do_arquivo": list_file,   
      }))


def remove(instance):
    if len(instance) < 1:
        return sys.stdout.write("Não há elementos\n")
    
    current_file = instance.dequeue()
    return sys.stdout.write(str(f"Arquivo {current_file} removido com sucesso\n"))

def file_metadata(instance, position):
    try:
      current_instance = instance.search(position)
      list_file = txt_importer(current_instance)
          
      return sys.stdout.write(str({
            "nome_do_arquivo": current_instance,
            "qtd_linhas": len(list_file),
            "linhas_do_arquivo": list_file,
      }))
    except IndexError:
      return sys.stderr.write(str("Posição inválida\n"))
