def exists_word(word, instance):
    result = []
    lines_found = []

    for value in range(len(instance)):
        current_line = instance.search(value)
        for item, line in enumerate(current_line["linhas_do_arquivo"]):
            if word.lower() in line.lower():
                lines_found.append({"linha": item + 1})

        if lines_found:
            result.append({
                "palavra": f"{word}",
                "arquivo": current_line["nome_do_arquivo"],
                "ocorrencias": lines_found,
            })

    return result


def search_by_word(word, instance):
    """Aqui irá sua implementação"""
