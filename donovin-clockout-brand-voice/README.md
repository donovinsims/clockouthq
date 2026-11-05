# Donovin Sims | Personal AI voice system

Write original practical AI content for [Donovin Sims](https://x.com/donovinsims), solo founder of [Clockout](https://clockout.us). The system retains Corey Ganim's attributed writing mechanics and Ghostwriter methodology while using Donovin's own identity, positions and audiences.

**Positioning:** Teach practical AI so people can build useful things. Clockout helps owners find bottlenecks, fix processes and implement appropriate technology.

## Start here

1. Read the [Brand Voice & Bio](Donovin_Sims_Brand_Profile/01_Donovin_Sims_Brand_Voice_and_Bio.md), [two-audience ICP](Donovin_Sims_Brand_Profile/02_Donovin_Sims_Ideal_Customer_Profile.md) and [facts](voice-clone/profiles/donovin-sims/facts.md).
2. Use [WORKFLOW.md](WORKFLOW.md) and [BRIEF_TEMPLATE.md](BRIEF_TEMPLATE.md).
3. Apply [Donovin Voice Apply](integrations/voice-apply/SKILL.md); calibrate future real samples with [Voice Analyze](integrations/voice-analyze/SKILL.md).
4. Review [EDITORIAL_QUALITY_CHECKLIST.md](EDITORIAL_QUALITY_CHECKLIST.md) and [testing limits](TESTING_AND_LIMITATIONS.md).

## Regular content requests

Ask Codex: “Use Donovin Voice Apply to write a long X post for Audience A about making a work task easier with AI. Retrieve relevant Corey examples first, inspect the techniques, then check originality and return the strongest draft.”

The existing retrieval CLI now prepares balanced writing context with `brief`, supports pattern/format/topic and historical-performance views with `search`, checks prior drafts with `overlap`, and keeps generated/approved/published records in a separate nontraining ledger with `record`. No API or paid model is required. Research and check output stay out of the normal draft delivery. See [WORKFLOW.md](WORKFLOW.md) and the latest optimization section in [implementation report](docs/IMPLEMENTATION_REPORT.md).

## Audience and strategy

A: working professionals and everyday AI learners who want practical skills and independence.
B: business owners, founders and operators who may hire diagnosis and implementation.

[content-strategy.json](content-strategy.json) configures the initial **60/20/15/5** mix: practical education / agents-tools-builds / business operations / founder journey. Per 20 ideas, **12/4/3/1**, with one primary category each. This is a target, not measured history.

## Use in Codex

Open this folder and ask:
> Read AGENTS.md, the active Donovin profile and integrations/voice-apply/SKILL.md. Draft an original long X post for Audience A about turning meeting notes into a checked action list. Use a hypothetical sanitized example. Run the editorial and originality checks and return one draft for my review.

Local [AGENTS.md](AGENTS.md) routes work to this profile. No global skill installation is required. Scripts use Python 3.9+ standard library; optional existing PyYAML is used only for complete YAML validation.

## Use in ChatGPT

Run `python3 scripts/export_chatgpt.py`, then create a ChatGPT Project, upload [CHATGPT_CONTEXT.md](exports/CHATGPT_CONTEXT.md), and paste the text from [project instructions](Donovin_Sims_Brand_Profile/03_Donovin_Sims_Project_Instructions.txt) into its instructions. Attach a completed brief and request a draft. If execution is unavailable, automated originality cannot run there; bring the draft back to Codex for the commands below. The bundle contains curated public-safe profile guidance and structural abstractions, not internal source snapshots or the full corpus. See [workflow](WORKFLOW.md).

## Commands (from this project root)

```sh
python3 voice-clone/scripts/retrieve.py search "repetitive work" --profile donovin-sims --format long -k 4
python3 scripts/check_draft.py --format long --draft-file drafts/current/post.txt
python3 voice-clone/scripts/retrieve.py overlap --profile donovin-sims --draft-file drafts/current/post.txt --strict
python3 -m unittest discover -s tests -v
python3 scripts/validate_project.py
```

## Evidence and preservation

Active profile: [donovin-sims](voice-clone/profiles/donovin-sims/README.md). Authentic original Donovin posts ingested: **0**. Generated validation drafts are excluded from measurements.

[Corey research](voice-clone/profiles/corey-ganim/README.md) retains 405 original posts, 395 measured, 10 holdouts and the source archive. These describe Corey, not Donovin. [Ghostwriter originals and license](integrations/ghostwriter-upstream/LICENSE) remain intact. [Archived original active files](docs/archive/README.md) preserve recoverability.

[Source reconciliation](docs/SOURCE_RECONCILIATION.md) records current GitHub versus local differences, including the newer temporary website-price decision. The adjacent reference folder and remote knowledge base were read-only. No accounts changed, messages sent or content published.

See [implementation report and final tree](docs/IMPLEMENTATION_REPORT.md), [sample plan](validation/20-post-plan.json), and [validation review](validation/REVIEW.md).

Run draft-check examples after saving a fresh post to drafts/current/post.txt. For a saved revision, exclude only its own ledger record ID; other history remains in scope.
