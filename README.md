# Build Evidence Verifier

I need to decide whether the evidence for a synthetic build meets a release policy before a reviewer signs off.

The starter inventories synthetic records. Implement the decision command and reporting workflow described in [ASSIGNMENT.md](ASSIGNMENT.md). Use Python 3.10 or newer with the standard library.

```sh
python evidence.py inventory examples/quorum-1/allow-0-extra-attestations-0.json
python -m unittest discover -s tests -v
python acceptance.py --inventory
```

Example files contain input and expected results. The acceptance runner passes only the input to your implementation.
