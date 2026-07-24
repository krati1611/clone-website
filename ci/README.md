# CI activation

`ci/ci.yml` is the GitHub Actions workflow for this repo. It is parked here (not in
`.github/workflows/`) because the current `gh` OAuth token lacks the `workflow` scope —
GitHub rejects pushes that add `.github/workflows/*` without it.

Activate it (one-time, interactive terminal):

```sh
gh auth refresh -h github.com -s workflow
git mv ci/ci.yml .github/workflows/ci.yml && git commit -m "Activate CI" && git push
```
