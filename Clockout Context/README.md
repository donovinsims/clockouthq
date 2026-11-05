# Clockout knowledge base

Permanent, version-controlled business knowledge base for Clockout. GitHub visibility verified PUBLIC on 2026-11-02; Donovin chose to keep it public and pause this update’s push. Keep private records and secrets outside this folder. Public access does not establish redistribution rights for third-party materials.

**Start at [docs/README.md](docs/README.md)** — the canonical entry point. This root file is only a pointer and a map of the folder; it is not a competing source of truth.

## Layout

| Path | Purpose |
|---|---|
| `docs/` | The complete Clockout documentation set: founder, business foundation, market research, offers and sales, delivery and operations, marketing, tools, finance, execution/decisions, and the reference/archive section. |
| `.gitignore` | Keeps local archives, metadata, credentials and tool state out of version control. |
| `Clockout-Source-of-Truth-MASTER-v3-VERIFIED.zip` | Dated local baseline archive. Intentionally untracked. |

## For an AI agent

Read in this order: [docs/AGENTS.md](docs/AGENTS.md) → [docs/CURRENT_STATE.md](docs/CURRENT_STATE.md) → [docs/CHECKPOINT.md](docs/CHECKPOINT.md) when resuming → the relevant canonical document → [docs/OPEN_DECISIONS.md](docs/OPEN_DECISIONS.md). Use source extracts only when needed.

Update procedure: [docs/DOCS_MAINTENANCE.md](docs/DOCS_MAINTENANCE.md). Git workflow: [docs/07-tools-and-systems/github-setup-and-maintenance.md](docs/07-tools-and-systems/github-setup-and-maintenance.md).

Validation, run from the `docs/` directory:

```sh
python3 10-reference-and-archive/validate_master.py
```

## Boundary

The documents describe a business under active development. Dated statements describe their source date, not today. Missing evidence stays `UNKNOWN`; nothing here should be read as proof of revenue, customers, completed work or current system state.
