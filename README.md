# Projeto: Sistema de Agendamento para Salões de Beleza - "AgendaBeauty"

## I. Objetivo

O objetivo principal deste projeto é desenvolver uma plataforma web, chamada **AgendaBeauty**, para modernizar e automatizar o processo de agendamento de horários em salões de beleza, barbearias e para profissionais autônomos da área da estética. A solução visa oferecer uma experiência fluida e conveniente para os **clientes**, ao mesmo tempo que otimiza a gestão da agenda e dos serviços para os **profissionais** e **gestores** dos estabelecimentos.

## II. Problema

Atualmente, muitos salões de beleza e profissionais autônomos ainda dependem de métodos manuais e pouco eficientes para gerenciar seus agendamentos, como agendas de papel, ligações telefônicas ou trocas de mensagens em aplicativos como o WhatsApp. Essa abordagem gera uma série de problemas:

* **Para os Profissionais/Salões:**
    * Alto risco de erros humanos, como agendamentos duplos ou horários esquecidos.
    * Dificuldade em gerenciar cancelamentos e remarcações de forma ágil.
    * Falta de um canal centralizado para divulgar serviços, preços e horários disponíveis.
    * Gasto de tempo considerável em tarefas administrativas em vez de focar no atendimento ao cliente.

* **Para os Clientes:**
    * Falta de visibilidade clara sobre os horários disponíveis, exigindo contato direto.
    * Demora na confirmação do agendamento, dependendo da disponibilidade do profissional para responder.
    * Dificuldade para agendar serviços fora do horário comercial do estabelecimento.

A plataforma **AgendaBeauty** busca resolver essa ineficiência, centralizando a gestão da agenda e simplificando o processo de agendamento para ambas as partes.

## III. Tipo de Solução

A solução proposta é uma **aplicação web responsiva**, composta por um frontend e um backend, que funcionará como uma plataforma de serviços (SaaS - *Software as a Service*).

* **Frontend:** Será a interface com o usuário, desenvolvida para ser intuitiva e de fácil utilização tanto em desktops quanto em dispositivos móveis (smartphones e tablets). Responsável por exibir os serviços, a agenda, os formulários de agendamento e os painéis de gerenciamento.
* **Backend:** Será o cérebro da aplicação, responsável por toda a lógica de negócio, incluindo o cadastro de usuários (clientes e profissionais), gerenciamento de serviços, controle de horários, notificações e a segurança dos dados. Ele fornecerá uma API para se comunicar com o frontend.

Este modelo de solução foi escolhido por ser acessível de qualquer lugar, não exigir instalação por parte do usuário e permitir a centralização completa das informações, facilitando a gestão e o acesso em tempo real.

## IV. Requisitos

### Requisitos Funcionais (RFs)

**Módulo de Gestão de Contas**
* **RF01:** O sistema deve permitir que Clientes e Profissionais se cadastrem na plataforma fornecendo nome, e-mail e senha.
* **RF02:** O sistema deve permitir que usuários cadastrados realizem login.

**Módulo do Cliente**
* **RF03:** O sistema deve permitir que o Cliente visualize a lista de profissionais/salões cadastrados.
* **RF04:** O sistema deve permitir que o Cliente visualize os serviços e preços oferecidos por um profissional.
* **RF05:** O sistema deve exibir a agenda de um profissional com os horários disponíveis e ocupados.
* **RF06:** O sistema deve permitir que o Cliente selecione um serviço e um horário disponível para realizar um agendamento.
* **RF07:** O sistema deve permitir que o Cliente visualize seus próprios agendamentos (futuros e passados).
* **RF08:** O sistema deve permitir que o Cliente cancele um agendamento com antecedência mínima definida pelo profissional.

**Módulo do Profissional**
* **RF09:** O sistema deve permitir que o Profissional cadastre e gerencie os serviços que oferece (nome, descrição, duração e preço).
* **RF10:** O sistema deve permitir que o Profissional defina sua jornada de trabalho (dias da semana e horários de atendimento).
* **RF11:** O sistema deve permitir que o Profissional visualize sua agenda diária, semanal e mensal.
* **RF12:** O sistema deve permitir que o Profissional confirme ou cancele agendamentos feitos por clientes.
* **RF13:** O sistema deve permitir que o Profissional bloqueie horários em sua agenda para uso pessoal.

### Requisitos Não Funcionais (RNFs)

* **RNF01 (Usabilidade):** A interface deve ser intuitiva e de fácil navegação, exigindo o mínimo de cliques para realizar as ações principais.
* **RNF02 (Desempenho):** As páginas e, principalmente, a agenda, devem carregar em no máximo 3 segundos.
* **RNF03 (Responsividade):** A aplicação deve se adaptar e ser plenamente funcional em diferentes tamanhos de tela (desktop, tablet e smartphone).
* **RNF04 (Segurança):** Os dados dos usuários, especialmente as senhas, devem ser armazenados de forma criptografada. A comunicação deve utilizar HTTPS.
* **RNF05 (Disponibilidade):** O sistema deve estar disponível para acesso 24/7, com um tempo de atividade (uptime) de pelo menos 99%.

## V. Diagrama de Caso de Uso

O diagrama abaixo ilustra as principais interações dos atores com o sistema **AgendaBeauty**.

**Atores:**
* **Cliente:** Pessoa que busca e agenda serviços de beleza.
* **Profissional:** Pessoa que oferece os serviços e gerencia sua própria agenda.

```mermaid
graph TD
    subgraph Sistema AgendaBeauty
        direction LR

        Cliente[Cliente]
        Profissional[Profissional]

        uc_agendar[Realizar Agendamento]
        uc_visualizar_agenda_cliente[Visualizar Meus Agendamentos]
        uc_cancelar[Cancelar Agendamento]

        uc_gerenciar_servicos[Gerenciar Serviços]
        uc_gerenciar_agenda_prof[Gerenciar Agenda]
        uc_definir_horarios[Definir Jornada de Trabalho]

        Cliente --> uc_agendar
        Cliente --> uc_visualizar_agenda_cliente
        Cliente --> uc_cancelar

        uc_agendar -->|include| uc_visualizar_agenda_cliente

        Profissional --> uc_gerenciar_servicos
        Profissional --> uc_gerenciar_agenda_prof
        Profissional --> uc_definir_horarios
    end
