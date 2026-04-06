# PromptShield Test Repo

This repository is intentionally insecure and exists only for validating PromptShield AI Security.

It includes examples of:

- LLM API calls with user-controlled input
- Prompt logging
- Redacted PII-like values in prompts
- Redacted secret-like values near LLM usage
- Unsafe tool execution patterns
- Database/customer data sent to an LLM
- Harmful or disallowed text flowing into model input

Do not use this code in production.

## Contact

For questions about PromptShield AI Security, email [info@scalapps.com](mailto:info@scalapps.com).

## PromptShield GitHub Action

This repo includes a GitHub Actions workflow at `.github/workflows/promptshield.yml` that runs PromptShield on pull requests and on manual dispatch.

- Action: `Zero-Harm-AI-LLC/promptshield@v1`
- Trigger: pull requests (`opened`, `synchronize`, `reopened`) and manual runs
- Output: GitHub Actions annotations in the workflow run
- Default behavior: `fail-on: any` so pull requests with PromptShield findings fail the check and can be used to gate merges

If you want a less strict policy, change `fail-on` in `.github/workflows/promptshield.yml` to `low`, `medium`, `high`, or `never`.
