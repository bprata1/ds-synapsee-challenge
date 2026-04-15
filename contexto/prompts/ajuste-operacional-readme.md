# Comando de Ajuste: Regra de Negócio (UI) e Enriquecimento do README

Antes de partirmos para os relatórios finais da banca, precisamos corrigir um bug de regra de negócio na nossa interface e adicionar o guia de uso no repositório no readme, além das atualizações padrão do @atualizar-readme.md

## 1. Correção de Miopia Operacional no Streamlit (`app.py`)

Durante os testes, notamos que a tabela de "Top Clientes de Maior Risco" está exibindo clientes que já possuem `Churn = Yes` (ex-clientes). A equipe de retenção não pode ligar para quem já cancelou o serviço.

* **Ação Obrigatória:** Modifique o `app.py` para que a lista dos 10 maiores scores não possua clientes que já deram churn (Churn == 1, que já não estão mais com a empresa). Essa lista precisa desse filtro, pois ela é uma fila de prioridade.

## 2. Enriquecimento do README (Preservando o Histórico)

O nosso `README.md` atual já possui uma excelente base gerada pelos nossos comandos anteriores. Não reescreva o arquivo do zero.

* **Ação Obrigatória:** Leia o `README.md` atual. Mantenha a estrutura existente e adicione apenas duas novas seções onde fizer mais sentido visualmente e em termos de organização do projeto:
  * **Stack Tecnológico:** Liste as bibliotecas principais (e se já existir, atualize-o).
  * **Como Executar a interface de inferência:** Um guia passo a passo claro para rodar a interface web (incluindo o comando `streamlit run app.py` e a instrução para usar o `sample_upload_batch.csv` para testes).

## 3. Governança

* Atualize os `logs.md` registrando a correção do filtro de clientes ativos no Streamlit e a atualização do README.
* Faça um commit intermediário com a mensagem: `fix(deploy): oculta ex-clientes da fila de retencao na UI e enriquece README com guia de execucao`.

**Ação:** Implemente o filtro no `app.py`, atualize o `README.md` preservando sua estrutura original e me avise quando o commit estiver concluído!
