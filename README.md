Sistema de Cadastro de Usuários (Python CRUD)

Um sistema de gerenciamento de usuários desenvolvido em Python para consolidar conceitos de manipulação de dados, persistência em arquivos e experiência do usuário (UX) via linha de comando.

   Funcionalidades (CRUD Completo)
- **Cadastrar:** Adiciona novos usuários com validação em tempo real.
- **Listar:** Exibe todos os usuários salvos no banco de dados local.
- **Buscar:** Localiza usuários específicos através do e-mail.
- **Editar:** Atualiza dados de usuários existentes de forma intuitiva.
- **Remover:** Exclui registros do sistema.

   Tecnologias e Conceitos Utilizados
- **Python 3**: Linguagem principal.
- **JSON**: Utilizado para persistência de dados (armazenamento em arquivo `.json`).
- **Expressões Regulares (Regex)**: Validação rigorosa de nomes e e-mails.
- **Tratamento de Exceções (`try/except`)**: Garantia de integridade para campos numéricos (idade).
- **F-Strings**: Formatação dinâmica de strings para melhor interface.
- **Módulo OS**: Verificação de existência de arquivos no sistema.

   Diferenciais do Projeto
- **UX Resiliente**: O sistema permite que o usuário corrija entradas inválidas sem ser expulso do menu principal.
- **Edição Inteligente**: Na edição, o usuário pode apenas apertar `Enter` para manter o valor atual do campo.
- **Persistência Real**: Os dados não são perdidos ao fechar o programa, sendo carregados automaticamente ao iniciar.

   
   Como executar
   
1. Clone o repositório:
   ```bash
   git clone [https://github.com/seu-usuario/seu-repositorio.git](https://github.com/seu-usuario/seu-repositorio.git)