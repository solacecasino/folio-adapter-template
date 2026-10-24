"""My Adapter. folio.py (next to this file) handles talking to Folio."""

import folio


@folio.command("count")
def count():
    words = len(folio.text().split())
    folio.notify(f"This document has {words} words")


@folio.on("changed")
def changed(event):
    folio.status(f"{event['words']} words")


folio.run()
