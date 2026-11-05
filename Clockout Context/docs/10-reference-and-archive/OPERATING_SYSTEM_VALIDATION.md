# Clockout Master v3 — final validation

Date: 2026-10-30. This is the current validation description; prior VALIDATION.md and CONSOLIDATION_REPORT.md describe earlier packages.

## Actual checks

The included [validate_master.py](validate_master.py) checks nonempty UTF-8 files, JSON/YAML parsing, CSV row shape, relative Markdown file links and heading anchors outside fenced historical quotations, source-ID uniqueness, claim/source integrity, registered extract files, manifest entrypoints, section directories, historical disposition destinations (including semicolon-separated multiple homes), coverage file-set equality, selected credential patterns and all SHA256SUMS entries. With a ZIP argument it checks CRC, exact file set, duplicate names, safe paths, one docs/ prefix and byte equality to the finalized folder.

[validation-results.json](validation-results.json) records the final successful structural check. The final archive was separately rechecked against the same tree after packaging. SHA256SUMS covers every packaged file except itself; it is not self-referential. The validation-result record is created before the final checksum generation, then the checks are repeated.

All 13 requested documentation walkthroughs are recorded in [FUNCTIONAL_SCENARIOS.md](FUNCTIONAL_SCENARIOS.md). Manual content review reconciled the five manuals, supporting procedures, templates, dated decisions and historical attribution. [file-coverage.csv](file-coverage.csv) accounts for every final file and records actions rather than treating counts as proof of quality.

## How to rerun

From the extracted docs/ directory, run `python3 10-reference-and-archive/validate_master.py`. To check the archive too, pass its actual path as the next argument. The validator requires Python 3.9+ and PyYAML; PyYAML was available in this execution environment and no dependency was installed. The script is read-only and does not refresh checksums, edit files or contact services. After authorized edits, regenerate checksums only after reviewing the change, then rerun checks and repackage. A changed file should fail the old checksum.

## Boundaries

Internal links inside authentic fenced source quotations are historical literal evidence and may refer to unbundled originals; they are not active package navigation. The validator does not certify every inline-code path, remote URL, legal duty, original source hash, catalog-only asset, commercial claim or live system. Pattern scanning is a bounded review, not proof that no possible secret exists. Full manual inspection of the packaged sources is not full recovery of absent originals. No customer execution, real application build, payment or live validation occurred in the scenario tests. External references are dated and should be rechecked before a material engagement.

## Earlier failures corrected before finalization

Preflight exposed existing Finder metadata, stale checksums after edits, and a validator assumption that each disposition cell contained only one path. Metadata was removed, checksums regenerated at the final gate, and semicolon-separated destinations validated individually. A metadata decode exception was fixed so the validator reports invalid files instead of crashing. No unresolved structural failure is accepted as a pass.
