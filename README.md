# Boas-vindas ao repositório do TING (Trybe is not Google)!

<details>
  <summary><strong>👨‍💻 O que foi desenvolvido</strong></summary><br />


Neste projeto tem como finalidade implementar de forma prática um programa que simule um algoritmo de indexação(Pilhas, Deque, Nó, Listas Ligadas e Listas Duplamente Ligadas) de documentos similar ao do Google. O programa deverá ser capaz de identificar ocorrências de termos em arquivos _TXT_.
  
Para isso, o programa desenvolvido terá dois módulos:
- **Módulo de gerenciamento de arquivos** que permite anexar arquivos de texto (formato _TXT_) e;
- **Módulo de buscas** que permite operar funções de busca sobre os arquivos anexados.

🚵 Habilidades exercitadas:

 - Manipular Pilhas;

 - Manipular Deque;

 - Manipular Nó & Listas Ligadas e;

 - Manipular Listas Duplamente Ligadas.

</details>

<details>
  <summary><strong>Instalação do projeto</strong></summary><br />

  1. Clone o repositório

  - Use o comando: `git clone git@github.com:tryber/sd-016-a-project-ting.git`
  - Entre na pasta do repositório que você acabou de clonar:
    - `cd sd-016-a-project-ting`

  2. Crie o ambiente virtual para o projeto

  - `python3 -m venv .venv && source .venv/bin/activate`

  3. Instale as dependências

  - `python3 -m pip install -r dev-requirements.txt`
</details>

# Requisitos

## Pacote `ting_file_management`

### 1 - Implementar uma fila para armazenar os arquivos que serão lidos.

- Preencha a classe `Queue`, presente no arquivo `queue.py` utilizando as estruturas vistas no módulo.

- A fila (Queue) deve ser uma estrutura `FIFO`, ou seja, o primeiro item a entrar, deve ser o primeiro a sair. Utilize seus conhecimentos de estruturas de dados para otimizar as operações implementadas.

- A fila deve implementar os métodos de inserção (`enqueue`), remoção (`dequeue`) e busca (`search`).

- O tamanho da fila deverá ser exposto utilizando o método `__len__` que permitirá, após implementado, o uso do comando `len(instancia_da_fila)` para se obter o tamanho da fila.

- Na busca uma exceção do tipo `IndexError` deve ser lançada caso um índice inválido seja passado. Para uma fila com `N` elementos, índices válidos são inteiros entre `0` e `N-1`.

### 2 - Implementar uma função `txt_importer` dentro do módulo `file_management` capaz de importar notícias a partir de um arquivo TXT, utilizando "\n" como separador.

- Caso o arquivo TXT não exista, ŕ exibida a mensagem `Arquivo {path_file} não encontrado` na `stderr`, em que `{path_file}` é o caminho do arquivo;

- Caso a extensão do arquivo seja diferente de .txt, deve ser exibida a mensagem `Formato inválido` na `stderr`;

- A função deve retornar uma lista contendo as linhas do arquivo.

<details>
<summary><b>Exemplo simples de um arquivo txt a ser importado</b></summary>

```md
Acima de tudo,
é fundamental ressaltar que a adoção de políticas descentralizadoras nos obriga
à análise do levantamento das variáveis envolvidas.
```
</details>

### 3 - Implementar uma função `process` dentro do módulo `file_process` capaz de ler o arquivo carregado na função anterior e efetuar o pré-processamento do conteúdo.

- A função irá receber como parâmetro a fila implementada no requisito 1 e o caminho do arquivo;

- A instância da fila recebida por parâmetro deve ser utilizada para registrar o processamento dos arquivos;

- Deve-se ignorar arquivos que já tenham sido processados anteriormente (ou seja, que tenham o mesmo caminho);

- Após cada nova inserção válida, a função deve mostrar via `stdout` os dados processados, conforme estrutura no exemplo abaixo.

<details>
<summary><b>Exemplo da estrutura de saída:</b></summary>

```python
{
    "nome_do_arquivo": "arquivo_teste.txt", # Caminho do arquivo recém adicionado
    "qtd_linhas": 3,                        # Quantidade de linhas existentes no arquivo
    "linhas_do_arquivo": [...]              # linhas retornadas pela função do requisito 2
}
```
</details>

### 4 - Implementar uma função `remove` dentro do módulo `file_process` capaz de remover o primeiro arquivo processado

- A função recebe como parâmetro a fila implementada no requisito 1.

- Caso não existam arquivos na fila, a função deve apenas emitir a mensagem `Não há elementos` via `stdout`;

- Em caso de sucesso de remoção, deve ser emitida a mensagem `Arquivo {path_file} removido com sucesso` via `stdout`, em que `{path_file}` é o caminho do arquivo.


### 5 - Implementar uma função `file_metadata` dentro do módulo `file_process` capaz de apresentar as informações superficiais de um arquivo processado.


- A função irá receber como parâmetro a fila implementada no requisito 1 e o índice a ser buscado;

- Caso a posição não exista, deve ser exibida a mensagem de erro `Posição inválida` via `stderr`;

- Caso a posição seja válida, as informações relacionadas ao arquivo devem ser mostradas via `stdout`, seguindo o exemplo de estrutura abaixo.

<details>
<summary><b>Exemplo da estrutura de saída em caso de sucesso:</b></summary>

```python
{
    "nome_do_arquivo": "arquivo_teste.txt",
    "qtd_linhas": 3,
    "linhas_do_arquivo": [...]
}
```
</details>

### 6 - Implementar uma função `exists_word`, dentro do módulo `word_search`, que verifique a existência de uma palavra em todos os arquivos processados.

- A função recebe como parâmetros a palavra a ser buscada e a fila implementada no requisito 1;

- A função deve retornar uma lista com as informações de cada arquivo e suas linhas em que a palavra foi encontrada, conforme exemplo da estrutura de retorno;

- Caso a palavra não seja encontrada em nenhum arquivo, deve-se retornar uma lista vazia;

- A fila não deve ser modificada durante a busca. Ela deve permanecer com os mesmos arquivos processados antes e depois da busca.

<details>
<summary><b>Exemplo da estrutura de retorno:</b></summary>

```python
[{
  "palavra": "de",
  "arquivo": "arquivo_teste.txt",
  "ocorrencias": [
    {
      "linha": 2
    },
    {
      "linha": 7
    }
  ]
}]
````
</details>

#### :warning: Importante :warning:: O grupo Trybe foi responsável por realizar o inicio do projeto (e também os commits iniciais), mas precisamente a estrutura do projeto e as configuração dos tests para a avaliação do projeto.