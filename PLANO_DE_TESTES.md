# Plano de Testes - SaúdeConecta

## Introdução

Este documento descreve o plano de testes para o SaúdeConecta, um chatbot de saúde desenvolvido para fornecer informações básicas e alertas sobre condições médicas. O plano abrange testes funcionais para os dois principais atores do sistema: Usuário e Administrador.

## 1. Casos de Teste - Ator: Usuário

### 1.1 UC-01: Consultar Informações de Saúde

| ID | Caso de Uso | Descrição do Teste | Passos para Execução | Resultado Esperado |
| :--- | :--- | :--- | :--- | :--- |
| TC-001 | UC-01 | Consulta sobre febre (Teste de sucesso) | 1. Abrir o chat<br>2. Digitar "o que é febre"<br>3. Enviar mensagem | O chatbot deve retornar a resposta definida na knowledge_base.json sobre febre, incluindo sintomas e recomendações básicas |
| TC-002 | UC-01 | Consulta com variação de palavras-chave | 1. Abrir o chat<br>2. Digitar "estou com febre alta"<br>3. Enviar mensagem | O chatbot deve identificar a palavra-chave "febre" e retornar a resposta apropriada |
| TC-003 | UC-01 | Consulta não encontrada | 1. Abrir o chat<br>2. Digitar "qual a temperatura do sol"<br>3. Enviar mensagem | O chatbot deve retornar uma resposta padrão indicando que não tem informações sobre o assunto e sugerindo consulta médica |

### 1.2 UC-02: Receber Alerta de Sintoma Grave (RF04)

| ID | Caso de Uso | Descrição do Teste | Passos para Execução | Resultado Esperado |
| :--- | :--- | :--- | :--- | :--- |
| TC-004 | UC-02 | Alerta de sintoma grave - dor no peito | 1. Abrir o chat<br>2. Digitar "estou com muita dor no peito"<br>3. Enviar mensagem | O chatbot deve identificar "dor no peito" como sintoma grave e retornar mensagem de alerta com recomendação para procurar atendimento de emergência |
| TC-005 | UC-02 | Alerta de sintoma grave - múltiplos sintomas | 1. Abrir o chat<br>2. Digitar "estou com falta de ar e pressão no peito"<br>3. Enviar mensagem | O chatbot deve identificar os sintomas graves e retornar mensagem de alerta com número do SAMU (192) |
| TC-006 | UC-02 | Verificação de sintoma não grave | 1. Abrir o chat<br>2. Digitar "estou com dor de cabeça leve"<br>3. Enviar mensagem | O chatbot deve fornecer informações sobre dor de cabeça sem acionar o alerta de emergência |

### 1.3 UC-07: Interação com IA

| ID | Caso de Uso | Descrição do Teste | Passos para Execução | Resultado Esperado |
| :--- | :--- | :--- | :--- | :--- |
| TC-007 | UC-07 | Consulta não cadastrada usando IA | 1. Abrir o chat<br>2. Digitar pergunta não cadastrada<br>3. Enviar mensagem | O chatbot deve usar a IA para gerar uma resposta relevante e incluir o aviso sobre consulta médica |
| TC-008 | UC-07 | Resposta da IA com disclaimer | 1. Abrir o chat<br>2. Fazer qualquer pergunta não cadastrada<br>3. Enviar mensagem | A resposta deve incluir o disclaimer de que foi gerada por IA |
| TC-009 | UC-07 | Fallback para IA em caso de erro | 1. Desativar base de conhecimento<br>2. Fazer uma pergunta<br>3. Enviar mensagem | O sistema deve usar a IA como fallback e retornar uma resposta |

## 2. Casos de Teste - Ator: Administrador

### 2.1 UC-03: Gerenciar Base de Conhecimento

| ID | Caso de Uso | Descrição do Teste | Passos para Execução | Resultado Esperado |
| :--- | :--- | :--- | :--- | :--- |
| TC-010 | UC-03 | Adicionar nova pergunta/resposta | 1. Acessar painel admin<br>2. Selecionar "Adicionar novo item"<br>3. Preencher campos (keywords e resposta)<br>4. Salvar | Nova entrada deve ser adicionada ao knowledge_base.json e estar disponível para consulta |
| TC-011 | UC-03 | Editar resposta existente | 1. Acessar painel admin<br>2. Selecionar item existente<br>3. Modificar resposta<br>4. Salvar alterações | A resposta deve ser atualizada no knowledge_base.json e a nova versão deve ser retornada nas consultas |
| TC-012 | UC-03 | Remover pergunta/resposta | 1. Acessar painel admin<br>2. Selecionar item existente<br>3. Clicar em "Remover"<br>4. Confirmar remoção | O item deve ser removido do knowledge_base.json e não deve mais aparecer nas consultas |

### 2.2 UC-04: Gerenciar Palavras-chave de Alerta

| ID | Caso de Uso | Descrição do Teste | Passos para Execução | Resultado Esperado |
| :--- | :--- | :--- | :--- | :--- |
| TC-013 | UC-04 | Adicionar palavra-chave de alerta | 1. Acessar configurações de alerta<br>2. Adicionar nova palavra-chave<br>3. Salvar | Nova palavra-chave deve ser adicionada à lista ALERT_KEYWORDS e acionar alerta quando utilizada |
| TC-014 | UC-04 | Remover palavra-chave de alerta | 1. Acessar configurações de alerta<br>2. Remover palavra-chave existente<br>3. Salvar | Palavra-chave deve ser removida da lista ALERT_KEYWORDS e não deve mais acionar alerta |
| TC-015 | UC-04 | Editar mensagem de alerta | 1. Acessar configurações de alerta<br>2. Modificar texto do ALERT_RESPONSE<br>3. Salvar | Nova mensagem de alerta deve ser exibida quando sintomas graves forem detectados |

## 3. Testes Não-Funcionais

### 3.1 Desempenho e Escalabilidade

| ID | Descrição do Teste | Critério de Aceitação |
| :--- | :--- | :--- |
| TNF-001 | Tempo de resposta do chatbot | Resposta em menos de 2 segundos para consultas na base de conhecimento |
| TNF-002 | Tempo de resposta da IA | Resposta em menos de 5 segundos para consultas via IA |
| TNF-003 | Carga do sistema | Sistema deve suportar 100 usuários simultâneos |

### 3.2 Segurança e Conformidade

| ID | Descrição do Teste | Critério de Aceitação |
| :--- | :--- | :--- |
| TNF-004 | Validação de entrada | Sistema deve sanitizar todas as entradas para prevenir injeções |
| TNF-005 | Disclaimer médico | Todas as respostas devem incluir aviso sobre não substituir consulta médica |
| TNF-006 | Proteção de dados | Logs não devem armazenar informações pessoais identificáveis |

## 4. Ambiente de Testes

### 4.1 Requisitos de Ambiente

- Python 3.8+
- Node.js 14+
- FastAPI
- React.js
- Conexão com OpenAI API

### 4.2 Dados de Teste

- Base de conhecimento com pelo menos 5 entradas
- Lista de palavras-chave de alerta
- Chave de API válida para OpenAI

## 5. Critérios de Aceitação

- Todos os casos de teste críticos (TC-001 a TC-009) devem passar
- Nenhum erro crítico nos testes de segurança
- Tempo de resposta dentro dos limites especificados
- Todos os disclaimers médicos presentes