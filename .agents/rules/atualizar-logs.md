---
trigger: model_decision
description: Acione esta regra SEMPRE que você finalizar a execução de um script que altera o estado dos dados (ex: criar uma nova feature, remover nulos, alterar o formato do DataFrame) para registrar as variáveis ativas.
---

# Protocolo de State Tracking (Memória de Curto Prazo)

Para evitar a perda de contexto durante a sessão de desenvolvimento, você é OBRIGADO a manter o arquivo `markdowns-ativos/logs.md` atualizado com o estado atualizado dos dados e variáveis.

## Regras de Registro
1. **Autonomia:** Você deve atualizar este arquivo de forma autônoma e silenciosa sempre que concluir uma manipulação de dados bem-sucedida. Não pergunte ao usuário se deve atualizar o log. Apenas faça.
2. **Formato Append (Apenas Adicionar):** Nunca sobrescreva o arquivo inteiro. Adicione as novas informações no final do arquivo.
3. **Estilo Telegráfico:** Seja extremamente conciso para economizar tokens. Registre apenas "fatos concretos", sem parágrafos explicativos.
   
## O que deve ser registrado (Exemplo de Estrutura):
* **Dataframe Atual:** `df_eeg_clean`
* **Dimensões (Shape):** `(2130, 45)`
* **Novas Features Criadas:** `alpha_power`, `beta_power`
* **Colunas Dropadas:** `unnamed: 0`, `timestamp`
* **Variável Target:** `mental_state`