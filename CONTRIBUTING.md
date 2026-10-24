# Contributing to Veepick documentation

Thank you for helping make these guides clearer and more useful.

## Useful contributions

- Correct an inaccurate step or broken link.
- Clarify an explanation or fix a typo.
- Suggest a guide for a common task.
- Improve accessibility or the documentation layout.

## Before proposing a change

1. Check the existing guide and open documentation issues.
2. Describe the page, the problem and your proposed improvement in English.
3. Keep the change focused and use the labels shown in the app.
4. Do not include private conversations, account details or credentials.

Use [Support](SUPPORT.md) for app or account help.

## Editing the website and guides

The website uses static HTML and CSS. Its guide content and Markdown are generated together from `scripts/build_docs.py` using the Python standard library.

```sh
python3 scripts/build_docs.py
git diff --check
```

Edit guide content in the generator, regenerate the pages, and include the corresponding HTML and Markdown updates. Styling is maintained in `styles.css`. Preview the homepage and guide pages at desktop and mobile widths, and check navigation and keyboard focus before submitting a pull request.

---

<p align="center">
  <sub>© 2026 Veepick · <a href="https://veepick.com/terms/?lang=en">Terms</a> · <a href="https://veepick.com/community-guidelines/?lang=en">Community Guidelines</a> · <a href="https://veepick.com/child-safety/?lang=en">Child Safety</a> · <a href="https://veepick.com/delete-account/?lang=en">Account Deletion</a> · <a href="https://veepick.com/privacy/?lang=en">Privacy</a></sub>
</p>
