# json-peek

A zero-dependency JSON inspector. Print a whole document, list top-level keys, or follow a dotted path such as `items.0.name`.

## Usage

```bash
python json_peek.py data.json --path items.0.name
```

## Options

- `--path a.b.0.c` — follow a dotted path
- `--keys` — print keys of the selected object
- `--compact` — no indentation
## License

MIT

## Notes

Contributions and small patches are welcome.
