"""Domain validation for catalog evidence envelopes."""

from evidence_catalog.validation import (
    ValidationError, boolean, fields, identifier, integer, text,
)

PROJECT = 'build-evidence-verifier'


def validate_payload(payload):

    fields(payload, ("identity", "digest", "kind"))
    identifier(payload["identity"], "identity")
    text(payload["digest"], "build digest", 256)
    identifier(payload["kind"], "kind")


def example_payload():
    return {'identity': 'analyst-01', 'digest': 'synthetic-build-A', 'kind': 'test'}
