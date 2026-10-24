# My Adapter

A [Folio](https://github.com/solacecasino/folio) adapter. Replace this with
what yours does.

---

## Making your own from this template

1. **Click "Use this template"** at the top of this page and name your repo
   (the name becomes your zip's name, such as `word-goals`).
2. **Edit it.** Change `adapter.toml` (name, description, commands) and
   `main.py`, and put your name in `LICENSE`. `folio.py` does the talking to Folio, so a command is a few
   lines:

   ```python
   @folio.command("count")
   def count():
       folio.notify(f"{len(folio.text().split())} words")
   ```

   Everything an adapter can do is in
   [docs/adapters.md](https://github.com/solacecasino/folio/blob/main/docs/adapters.md)
   and in the comments in `folio.py`.
3. **Try it.** In Folio choose **Folio → Adapters…**, click **Add an adapter
   from a folder instead…**, and pick your repo's folder. Pick it again
   after each change. To see `folio.log(...)` messages, start Folio from a
   terminal.
4. **Release it.** Set `version` in `adapter.toml`, then:

   ```sh
   git tag v0.1.0 && git push origin v0.1.0
   ```

   GitHub Actions publishes a release with your zip. A Rust adapter (add a
   `Cargo.toml` and set `run = ["./your-crate-name"]`) gets a zip for macOS,
   Windows and Linux automatically.
5. **Get it listed** in the [catalog](https://github.com/solacecasino/folio-adapters/blob/main/CATALOG.md):
   fill in the [List my adapter](https://github.com/solacecasino/folio-adapters/issues/new?template=list-my-adapter.yml)
   form with your repo's name. A check downloads your release, and if it
   installs, the listing is opened for you. Every later release shows up in
   the catalog by itself.

Python adapters need Python 3 on the computer running Folio.
