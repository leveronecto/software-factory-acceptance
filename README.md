# Software Factory acceptance fixture

Dedicated trusted repository for manually invoked Cursor and Codex acceptance.
Uses Python 3 standard library only.

Required local check for every delivery:

```sh
python3 -m unittest discover -s tests -v
```

Work is delivered through an open, non-draft PR and the current structured
Factory report. Merge and deployment are performed manually by the human owner.
This repository has no deployment workflow.
