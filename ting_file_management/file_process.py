import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    list_file = txt_importer(path_file)
    file_found = True
    current_dict = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(list_file),
        "linhas_do_arquivo": list_file,
    }

    for element in range(len(instance)):
        if instance.search(element)["nome_do_arquivo"] == path_file:
            file_found = False

    if file_found:
        instance.enqueue(current_dict)

    return sys.stdout.write(str(current_dict))


def remove(instance):
    if len(instance) < 1:
        return sys.stdout.write("Não há elementos\n")

    current_file = instance.dequeue()["nome_do_arquivo"]
    return sys.stdout.write(str(
      f"Arquivo {current_file} removido com sucesso\n"
    ))


def file_metadata(instance, position):
    try:
        current_instance = instance.search(position)

        return sys.stdout.write(str(current_instance))
    except IndexError:
        return sys.stderr.write(str("Posição inválida\n"))
