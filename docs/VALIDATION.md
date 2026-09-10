# Validation record / Registro de validação

Review date / Data da revisão: 2026-09-10.

## Change and reason / Mudança e motivo

EN: Fixed nullable termination dates that prevented active employees from generating downstream data; added population and date-range validation.

PT: Corrigidas datas de desligamento nulas que impediam gerar dados de participantes ativos; adicionada validação de população e intervalo de datas.

## Reproduce / Reproduzir

```sh
python -m venv .venv
# Activate .venv for your shell / Ative .venv no seu terminal
python -m pip install -r requirements-validation.txt
python -m pytest -q
python -m examples.review_demo
```

## Example evidence / Evidência do exemplo

Seven generated tables; referential integrity is checked before the example summary is printed. / Sete tabelas geradas; a integridade referencial é verificada antes da impressão do resumo.

EN: The suite includes normal operations and regression cases for the corrected behavior. The example checks values produced by the implementation. Use the linked workflow to inspect the result for a specific commit; no performance benchmark is inferred from a passing build.

PT: A suíte inclui operações válidas e regressões dos comportamentos corrigidos. O exemplo verifica valores produzidos pela implementação. Consulte a automação para conferir o resultado de um commit específico; aprovação de compilação não implica benchmark de desempenho.

## Limits / Limites

EN: All records are synthetic and distributions are illustrative assumptions. Metric definitions are teaching choices, not a validated HR benchmark. Payroll is a simplified monthly model, not a payroll compliance engine.

PT: Todos os registros são fictícios e as distribuições são hipóteses ilustrativas. As métricas são escolhas didáticas, sem validação como referência de RH. A folha é um modelo mensal simplificado, sem cálculo de obrigações legais.

[Return to README / Voltar ao README](../README.md)

## Verified suite / Suíte verificada

**49 software tests passed / testes de software aprovados.**

The complete dbt build also passed 73 data tests, 21 models and 7 seeds. / A execução dbt também aprovou 73 testes de dados, 21 modelos e 7 tabelas de entrada.

README Mermaid syntax and local documentation links were checked. / A sintaxe Mermaid do README e os links locais da documentação foram conferidos.
