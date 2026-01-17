# logging-in-python

Quick start
```python
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s [%(name)s] %(message)s")
logger = logging.getLogger(__name__)
logger.info("Hello from logging-in-python")
```

A bit about logging
- Why log: Logs record what your program does—helping debug issues, observe production behaviour, and support postmortems. Logs are routable, filterable, and persistent (unlike prints).
- Levels: Use DEBUG for diagnostics, INFO for normal events, WARNING for unexpected but handled situations, ERROR for recoverable failures, and CRITICAL for severe issues.
- Handlers & formatters: Handlers send logs to destinations (console, files, syslog, remote). Formatters shape output. Use JSON/structured formats for machine consumption (ELK/Loki).
- Context & correlation: Include module names, request IDs, or trace IDs so events across services can be correlated. Use `extra` or structured logging rather than string-concatenating context.
- Performance & safety: Avoid expensive work in log calls (use lazy formatting or level checks). Never log secrets—redact or omit sensitive fields.
- Testing: Use pytest's `caplog` to assert logs and levels in tests.

- For structured logging examples: pip install python-json-logger structl