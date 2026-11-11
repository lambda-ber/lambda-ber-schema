# MDRepo API snapshots

These three complete public API JSON responses support the metadata-only import pilot:

- `MDR00020971.json`: apo Tau-tubulin kinase 2.
- `MDR00021021.json`: JAK3 with a ligand.
- `MDR00079393.json`: PLAS-20K aldose reductase ensemble with five replicas, ligand ZST and cofactor NAP.

`manifest.json` records retrieval times, source/API URLs, snapshot SHA-256 hashes,
generated examples, counts and conversion warnings. Source creator, contributor and
publication attribution is retained in the JSON. MDRepo contributions are CC BY 4.0
according to <https://mdrepo.org/faq>. No simulation payloads are included.

From the repository root, rebuild examples offline with:

```bash
uv run python scripts/import_mdrepo_pilot.py
```

Use `--refresh` to fetch new metadata snapshots for the same three IDs. See
`src/docs/examples/mdrepo-import.md` for mapping decisions and limitations.
