# Update Changelog

Use the format of [keep a change log](https://keepachangelog.com/)

Update the Changelog file

Current features:

- Upon new version adds the Unreleased section to the new version
- Update urls in `github` format

## Getting started

```bash
pip install update_changelog
update_changelog --type major
update_changelog --type minor
update_changelog --type patch
update_changelog --v 1.1.1
update_changelog --v 1.1.1 --changelog CHANGE_LOG.md 
```
