To use `update_historic.py` script, copy a historical file from [BCV page](https://www.bcv.org.ve/estadisticas/tipo-cambio-de-referencia-smc) into `input/historic/` and run the script

```python
uv run python -m app.scripts.update_historic
```

Further reading:

- [Downloading of historical data](docs/downloading_historic_files.md)
- [Parsing of historical data](docs/parsing_historic.md)
