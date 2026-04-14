---
trigger: model_decision
description: Acione obrigatoriamente esta regra de formatação ao executar o "Gatilho A" do protocolo-copiloto, para manter as definições das variáveis atualizadas no arquivo dicionario-features.md
---

# Padrão de Preenchimento: Dicionário de Features

O arquivo `markdowns-ativos/dicionario-features.md` é o mapa vivo (mutável) do projeto. Ele registra o "COMO" e "POR QUÊ" uma variável existe.

## Regras Estritas de Edição

1. **Mutabilidade (Sobrescrita Permitida):** Se a lógica matemática de uma feature mudar durante o projeto, você DEVE alterar a definição dela no dicionário para refletir a realidade atual. Não crie duplicatas.
2. **Inclusão Dinâmica:** Adicione novos blocos apenas quando novas variáveis analíticas, features preditivas ou scores forem criados.
3. **Campos Obrigatórios por Variável:**
   * `Descrição:` O objetivo de negócio da variável.
   * `Fórmula/Filtro:` Os limiares matemáticos exatos usados no código (ex: Z-score > 3, Janela de 5s).
   * `Status:` Ativa, Em Validação, ou Dropada.
