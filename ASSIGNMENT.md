# Build Evidence Verifier

I need to decide whether the evidence for a synthetic build meets a release policy before a reviewer signs off.

## Required decision command

`python evidence.py verify INPUT.json` reads a raw JSON object as shown under input in examples/. Records are pre-verified synthetic attestations with identity, digest and kind. Only records for the requested digest and allowlisted identities count. For each required kind count distinct identities; repeated attestations count once. Return an object mapping each required kind to its remaining shortfall, floored at zero. Reject negative requirements and invalid field types. This exercise evaluates supplied metadata offline.

Print the JSON decision to stdout. For invalid input return nonzero and write a readable diagnostic to stderr. Use exact JSON types, including rejecting booleans where integers are required. Input ordering must not affect the result. Preserve the inventory CLI.

## Reporting and integration work

Add a batch decision report for multiple releases and policies. Include per-kind supporting identities, missing thresholds and approved/blocked decisions, with stable sorting. Handle the same identity serving multiple kinds independently. Include tests for unlisted identities, cross-build isolation and conflicting duplicate release ids. Document the reporting CLI, its input schema, one working example, and failure behavior. Exercise both success and failure paths through subprocess tests. Keep input files read-only. Use deterministic output and temporary paths for tests.

## Estimated implementation session

Allow 40 minutes for input modeling, 90 for the decision algorithm, 65 for the reporting feature, 50 for validation and edge cases, 60 for integration and regression tests, and 30 for documentation and reviewer evidence. Total estimate: 5 hours 35 minutes. Record actual time worked.
