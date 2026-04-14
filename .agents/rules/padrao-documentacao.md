---
trigger: glob
globs: *.py, *.ipynb
---

# Diretrizes de Escrita e Documentação de Código

O código desenvolvido deve ser autoexplicativo e tratado como material de auditoria e apresentação.

* **Docstrings:** Toda função, classe ou script principal deve conter docstrings detalhadas explicando entradas, saídas e a lógica de negócio principal.
* **Comentários Estratégicos:** Utilize comentários *inline* para explicar decisões não óbvias. O código diz **como** algo está sendo feito; seus comentários devem explicar **por que** aquela matemática ou regra de negócio foi escolhida.
* **Nomenclatura Limpa:** Utilize variáveis descritivas e autoexplicativas (`taxa_conversao` em vez de `tc`, `modelo_arvore_decisao` em vez de `mdl`).
