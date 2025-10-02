# Projeto: Chatbot de Acesso à Informação de Saúde - "SaúdeConecta"

## I. Objetivo

O objetivo principal deste projeto é desenvolver um chatbot com Inteligência Artificial, chamado **SaúdeConecta**, para fornecer acesso rápido, seguro e confiável a informações de saúde e bem-estar. Alinhada ao **Objetivo de Desenvolvimento Sustentável (ODS) 3 da ONU**, a solução visa combater a desinformação, orientar os **usuários** sobre cuidados primários e prevenção de doenças, e direcioná-los aos serviços de saúde adequados, democratizando o acesso ao conhecimento em saúde.

## II. Problema

Atualmente, com a vasta quantidade de informações disponíveis na internet, muitas pessoas recorrem a fontes não confiáveis para tirar dúvidas sobre saúde, o que pode levar a autodiagnósticos perigosos, automedicação incorreta e ansiedade. Essa realidade gera uma série de problemas:

* **Para os Usuários:**
    * Dificuldade em distinguir informações médicas verdadeiras de "fake news".
    * Falta de orientação clara sobre quais sintomas necessitam de atenção médica imediata.
    * Insegurança sobre práticas de prevenção e hábitos saudáveis.
    * Dificuldade em encontrar informações sobre os serviços de saúde públicos disponíveis em sua localidade.

* **Para o Sistema de Saúde:**
    * Sobrecarga de unidades de saúde com casos que poderiam ser resolvidos com orientação primária.
    * Agravamento de condições de saúde por falta de informação ou busca tardia por atendimento.
    * Custos elevados associados ao tratamento de doenças que poderiam ser prevenidas.

O chatbot **SaúdeConecta** busca resolver essa lacuna, oferecendo um canal centralizado e confiável para informações de saúde, disponível 24 horas por dia.

## III. Tipo de Solução

A solução proposta é um **chatbot com Inteligência Artificial**, que poderá ser integrado a plataformas web e aplicativos de mensagens. A arquitetura será dividida em:

* **Interface do Chatbot (Frontend):** Será a interface de conversação com o usuário, projetada para ser intuitiva e acessível. Ela poderá ser um widget em um site ou integrada a apps como WhatsApp ou Telegram, permitindo que o usuário interaja por meio de texto em linguagem natural.
* **Motor de IA e Backend:** Será o cérebro da aplicação, responsável por toda a lógica de negócio. Utilizará técnicas de **Processamento de Linguagem Natural (PLN)** para interpretar as perguntas dos usuários, buscar respostas em uma base de conhecimento curada por profissionais de saúde e fornecer informações claras e precisas. O backend também gerenciará a integração com APIs externas (ex: mapas de unidades de saúde) e garantirá a privacidade dos dados.

Este modelo foi escolhido por sua alta acessibilidade, capacidade de oferecer respostas instantâneas e potencial de escalabilidade para atender a um grande número de usuários simultaneamente.

## IV. Requisitos

### Requisitos Funcionais (RFs)

**Módulo de Interação do Usuário**
* **RF01:** O sistema deve permitir que o usuário faça perguntas sobre saúde, sintomas e prevenção em linguagem natural.
* **RF02:** O sistema deve fornecer informações claras e objetivas sobre condições de saúde comuns.
* **RF03:** O sistema deve orientar o usuário sobre práticas de prevenção e estilo de vida saudável.
* **RF04:** O sistema deve ser capaz de identificar sinais de alerta em uma descrição de sintomas e recomendar a busca por atendimento médico profissional.
* **RF05:** O sistema deve fornecer informações sobre unidades de saúde próximas (hospitais, postos de saúde), quando solicitado.
* **RF06:** O sistema deve exibir um aviso claro de que não substitui uma consulta médica profissional.

**Módulo de Administração e Curadoria**
* **RF07:** O sistema deve possuir um painel administrativo para que profissionais de saúde autorizados gerenciem a base de conhecimento.
* **RF08:** O sistema deve permitir que o administrador cadastre, edite e valide novas informações (perguntas e respostas).
* **RF09:** O sistema deve permitir que o administrador visualize logs de conversas anonimizadas para identificar pontos de melhoria no chatbot.
* **RF10:** O sistema deve permitir que o administrador configure respostas para tópicos de alta prioridade ou emergências de saúde pública.

### Requisitos Não Funcionais (RNFs)

* **RNF01 (Usabilidade):** A interface de conversação deve ser simples, clara e guiar o usuário de forma intuitiva.
* **RNF02 (Desempenho):** O tempo de resposta do chatbot para uma consulta do usuário não deve exceder 2 segundos.
* **RNF03 (Responsividade):** Se implementado em uma interface web, o chatbot deve ser funcional em diferentes tamanhos de tela (desktop e smartphone).
* **RNF04 (Segurança e Privacidade):** As conversas devem ser tratadas de forma anônima e os dados armazenados devem seguir as diretrizes da LGPD (Lei Geral de Proteção de Dados). A comunicação deve ser criptografada (HTTPS).
* **RNF05 (Disponibilidade):** O serviço deve estar disponível para os usuários 24/7, com um tempo de atividade (uptime) de pelo menos 99,5%.
* **RNF06 (Confiabilidade):** Toda informação fornecida pelo chatbot deve ser baseada em fontes médicas confiáveis e validadas, como a Organização Mundial da Saúde (OMS) e o Ministério da Saúde.

## V. Diagrama de Caso de Uso

O diagrama abaixo ilustra as principais interações dos atores com o sistema **SaúdeConecta**.

**Atores:**
* **Usuário:** Pessoa que busca informações e orientações de saúde.
* **Administrador:** Profissional responsável por gerenciar e validar o conteúdo da base de conhecimento do chatbot.

```mermaid
graph TD
    subgraph Sistema SaúdeConecta
        direction LR

        Usuario[Usuário]
        Administrador[Administrador]

        uc_consultar[Consultar Informações de Saúde]
        uc_buscar_unidades[Buscar Unidades de Saúde]
        uc_receber_alerta[Receber Alerta para Procurar Médico]

        uc_gerenciar_base[Gerenciar Base de Conhecimento]
        uc_analisar_logs[Analisar Logs de Conversa]
        uc_configurar_alertas[Configurar Respostas de Emergência]

        Usuario --> uc_consultar
        Usuario --> uc_buscar_unidades
        
        uc_consultar -- includes --> uc_receber_alerta

        Administrador --> uc_gerenciar_base
        Administrador --> uc_analisar_logs
        Administrador --> uc_configurar_alertas
    end
