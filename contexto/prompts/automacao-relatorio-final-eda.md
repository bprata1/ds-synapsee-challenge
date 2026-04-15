# Instruções de Automação: Relatório de Insights com Evidências Visuais

Agora que concluímos a Etapa 1, vamos preparar o nosso `markdowns-ativos/draft-relatorio.md` para ser a base da minha apresentação. Não quero apenas texto; preciso que o relatório seja visual e rico em dados.

## 1. Integração de Storytelling e Imagens

Para cada um dos 3 insights "matadores" que você identificou (O Combo Tóxico, A UTI dos Primeiros 6 Meses e O Paradoxo da Fibra Óptica) e para as respostas de "Quem é o "vilão" do Churn?" e "O impacto do tenure (tempo de casa)" (que você respondeu no chat para montar um resumo executivo), você deve:

* **Registrar o Insight:** Descrever o fenômeno de negócio conforme discutimos.
* **Incluir a Evidência Visual:** Inserir o link de Markdown para a imagem correspondente que você salvou em `reports/figures/`.
  * *Nota:* Use o caminho relativo correto para que a imagem apareça no preview do arquivo (ex: `![Descrição](../../reports/figures/nome_da_imagem.png)`).
* **Adicionar Dados de Suporte:** Extrair do notebook as pequenas tabelas ou métricas específicas (ex: taxas percentuais exatas) que comprovam o insight.

## 2. Estruturação do Relatório (Gatilho B)

Atualize o `draft-relatorio.md` seguindo o padrão de governança, mas organize esta seção especificamente para "Defesa Técnica da EDA". Além dos insights, inclua:

* **Tabela de Correlações:** Uma versão resumida em Markdown das top 5 features que mais impactam o Churn.
* **Resumo da Varredura de Qualidade:** O resultado da análise sistêmica (zero anomalias adicionais) para mostrar rigor metodológico.

## 3. Consolidação e Commit

* Após atualizar o relatório com as imagens e tabelas, verifique se os links das imagens estão funcionando.
* Execute o **Gatilho C (Commit)** com a mensagem: `docs(relatorio): integra insights de negócio com evidências visuais e tabelas de suporte`.

**Ação:** Prepare o relatório conforme as diretrizes acima. Assim que concluir, me avise para que eu possa validar o documento final antes de seguirmos para o Pipeline de Features.
