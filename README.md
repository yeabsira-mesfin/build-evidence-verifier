# Build Evidence Verifier

I need to decide whether the evidence for a synthetic build meets a release policy before a reviewer signs off.

The starter inventories synthetic records. Implement the decision command and reporting workflow described in [ASSIGNMENT.md](ASSIGNMENT.md). Use Python 3.10 or newer with the standard library.

```sh
python evidence.py inventory examples/quorum-1/allow-0-extra-attestations-0.json
python -m unittest discover -s tests -v
python acceptance.py --inventory
```

Example files contain input and expected results. The acceptance runner passes only the input to your implementation.

## Existing evidence application

The starter includes a transactional evidence catalog, tenant-scoped queries, CSV/JSON imports and exports, audit verification, deterministic snapshots, evidence packages and a local HTML viewer. See [CATALOG.md](CATALOG.md) for a runnable walkthrough. The assignment decision feature builds on this existing application.

Run `python tools/count_loc.py` for the reproducible source-code count. Application code is counted separately from tests, tools and acceptance examples.
