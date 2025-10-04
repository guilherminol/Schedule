# Casos de Teste - SaúdeConecta

## Casos de Uso do Ator "Usuário"

### 1. Consultar Informações de Saúde

#### CT01 - Consulta sobre sintomas comuns
**ID:** CT01  
**Descrição:** Usuário consulta informações sobre sintomas comuns de gripe  
**Passos:**
1. Usuário acessa o chatbot SaúdeConecta
2. Usuário digita: "Estou com dor de cabeça, febre e coriza. O que pode ser?"
3. Sistema processa a consulta
4. Sistema retorna informações sobre gripe e orientações gerais
5. Sistema exibe aviso de que não substitui consulta médica

**Resultado Esperado:** Sistema deve fornecer informações claras sobre gripe, sintomas, cuidados gerais e orientar sobre quando procurar atendimento médico, sempre com o aviso de que não substitui consulta profissional.

#### CT02 - Consulta sobre prevenção de doenças
**ID:** CT02  
**Descrição:** Usuário busca orientações sobre prevenção de doenças cardiovasculares  
**Passos:**
1. Usuário acessa o chatbot SaúdeConecta
2. Usuário digita: "Como posso prevenir doenças do coração?"
3. Sistema processa a consulta
4. Sistema retorna informações sobre hábitos saudáveis e prevenção
5. Sistema exibe aviso de que não substitui consulta médica

**Resultado Esperado:** Sistema deve fornecer orientações claras sobre prevenção de doenças cardiovasculares, incluindo alimentação saudável, exercícios físicos, controle de fatores de risco e orientar sobre acompanhamento médico regular.

#### CT03 - Identificação de sinais de alerta
**ID:** CT03  
**Descrição:** Usuário descreve sintomas que indicam necessidade de atendimento médico urgente  
**Passos:**
1. Usuário acessa o chatbot SaúdeConecta
2. Usuário digita: "Estou com dor no peito forte, falta de ar e suor frio há 30 minutos"
3. Sistema processa a consulta
4. Sistema identifica sinais de alerta
5. Sistema recomenda busca imediata por atendimento médico
6. Sistema exibe aviso de que não substitui consulta médica

**Resultado Esperado:** Sistema deve identificar os sinais de alerta como possíveis sintomas de emergência médica, recomendar busca imediata por atendimento médico (pronto-socorro) e fornecer orientações sobre como proceder.

### 2. Buscar Unidades de Saúde

#### CT04 - Busca por unidades de saúde próximas
**ID:** CT04  
**Descrição:** Usuário busca unidades de saúde próximas à sua localização  
**Passos:**
1. Usuário acessa o chatbot SaúdeConecta
2. Usuário digita: "Preciso de um posto de saúde perto de mim"
3. Sistema solicita localização do usuário
4. Usuário informa sua localização (endereço ou CEP)
5. Sistema processa a solicitação
6. Sistema retorna lista de unidades de saúde próximas
7. Sistema exibe aviso de que não substitui consulta médica

**Resultado Esperado:** Sistema deve retornar uma lista de unidades de saúde próximas à localização informada, incluindo endereço, telefone, horário de funcionamento e tipo de atendimento oferecido.

#### CT05 - Busca por hospitais de emergência
**ID:** CT05  
**Descrição:** Usuário busca hospitais com pronto-socorro 24h próximos  
**Passos:**
1. Usuário acessa o chatbot SaúdeConecta
2. Usuário digita: "Preciso de um hospital com pronto-socorro 24h perto de mim"
3. Sistema solicita localização do usuário
4. Usuário informa sua localização
5. Sistema processa a solicitação
6. Sistema retorna lista de hospitais com pronto-socorro 24h
7. Sistema exibe aviso de que não substitui consulta médica

**Resultado Esperado:** Sistema deve retornar uma lista de hospitais com pronto-socorro 24h próximos à localização informada, incluindo endereço, telefone, distância e orientações sobre como chegar.

#### CT06 - Busca por unidades especializadas
**ID:** CT06  
**Descrição:** Usuário busca unidades de saúde especializadas em uma área específica  
**Passos:**
1. Usuário acessa o chatbot SaúdeConecta
2. Usuário digita: "Preciso de um cardiologista perto de mim"
3. Sistema solicita localização do usuário
4. Usuário informa sua localização
5. Sistema processa a solicitação
6. Sistema retorna lista de unidades com especialistas em cardiologia
7. Sistema exibe aviso de que não substitui consulta médica

**Resultado Esperado:** Sistema deve retornar uma lista de unidades de saúde que oferecem atendimento em cardiologia próximas à localização informada, incluindo endereço, telefone, horário de funcionamento e informações sobre agendamento.

## Critérios de Aceitação Gerais

- **Tempo de Resposta:** Todas as consultas devem ser respondidas em até 2 segundos (RNF02)
- **Aviso Obrigatório:** Todas as respostas devem incluir o aviso de que o sistema não substitui consulta médica profissional (RF06)
- **Precisão das Informações:** Todas as informações fornecidas devem ser baseadas em fontes médicas confiáveis (RNF06)
- **Interface Intuitiva:** A interface deve ser simples e guiar o usuário de forma clara (RNF01)
- **Disponibilidade:** O sistema deve estar disponível 24/7 (RNF05)
