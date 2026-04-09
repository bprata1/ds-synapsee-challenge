---
trigger: model_decision
description: Quando utilizar o terminal para instalar, atualizar ou remover pacotes e bibliotecas Python (ex: executando comandos como pip install).
---

# Protocolo de Manutenção de Dependências

A reprodutibilidade deste projeto é inegociável. Para garantir que o ecossistema local e remoto estejam sempre em sincronia:

* **Sincronização Obrigatória:** Sempre que executar um comando para instalar, atualizar ou remover pacotes Python no terminal (ex: `pip install`), você deve **obrigatoriamente** executar o comando `pip freeze > requirements.txt` imediatamente em seguida.
* **Proibição de Omissão:** Esta etapa não pode ser ignorada, adiada ou pulada sob nenhuma circunstância. O rastreamento de dependências deve ser mantido em tempo real.