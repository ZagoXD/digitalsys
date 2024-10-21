Feature: Enviar Currículo
  Como um candidato
  Eu quero submeter meu currículo
  Para que a empresa receba minhas informações.

  Scenario: Submeter um currículo válido
    Given que eu sou um usuário não autenticado
    When eu preencho o formulário de currículo corretamente
    And eu clico no botão "Submeter Currículo"
    Then o sistema deve mostrar uma mensagem de sucesso "Currículo enviado com sucesso!"