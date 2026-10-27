# Outer Trail Games

Lightweight static website for https://outertrailgames.github.io/. Plain HTML and shared CSS; no build, JavaScript, packages, backend, external fonts, or paid services.

## Structure

- `index.html`: studio homepage, HexGlow card, contact, and a commented insertion point for future games.
- `hexglow/index.html`: game overview, three modes, genuine development screenshots, and a non-clickable Google Play availability placeholder.
- `hexglow/privacy.html`: standalone HTML privacy policy draft, with visible review status and date.
- `privacy.html`: website hosting and email privacy information.
- `404.html`: custom GitHub Pages error page using root-relative links.
- `assets/style.css`: shared responsive design; `assets/mark.svg`: studio mark.
- `assets/images/`: locally hosted game icon and screenshots; provenance in `docs/privacy-review.md`.
- `.nojekyll`: bypass Jekyll processing. `robots.txt` and `sitemap.xml`: discovery metadata.
- `docs/privacy-review.md`: implementation evidence and release checklist.
- `tools/check_site.py`: optional standard-library-only link and HTML checks, not a build step.

## Preview locally

From this repository, run:

```sh
python -m http.server 8000 --bind 127.0.0.1
```

Open http://127.0.0.1:8000/. Stop with Ctrl+C. Use an HTTP server rather than double-clicking HTML: links start at the site root. Python's simple server will not automatically use the custom error page; preview `/404.html` directly.

Run `python tools/check_site.py` to check local links, fragment targets, page metadata, images, and no-JavaScript content. In a browser, check each page at 320, 390, 768, and 1440 pixels, at 200% zoom, and using keyboard navigation. Confirm there is no horizontal scrolling and focus remains visible. Check the privacy page with JavaScript disabled (the entire site contains no scripts).

## Enable GitHub Pages

1. Finish the release checklist below. Commit and push the website files to the `main` branch of the public `outertrailgames/outertrailgames.github.io` repository.
2. In GitHub, open **Settings → Pages → Build and deployment**.
3. Select **Deploy from a branch**, branch **main**, folder **/(root)**, then Save.
4. Wait for GitHub's Pages deployment to finish. Enable **Enforce HTTPS** if offered.
5. Visit https://outertrailgames.github.io/ and `/hexglow/privacy.html` while signed out. Test a nonexistent path to confirm the custom 404 works.

No custom domain, Actions build workflow, or Sites hosting is needed. Repository settings and remote deployment were not changed by this implementation.

## Add another game

1. Create a directory such as `digward/` when approved public information is ready.
2. Copy `hexglow/index.html` as a structural starting point. Replace all game-specific text, assets, title, description, canonical URL, Open Graph fields, and navigation current-page state.
3. Add a separate privacy policy based on that game's actual data handling. Do not copy HexGlow's SDK disclosures without an audit.
4. Add an `article.game-card` under `#games` on the homepage. Use confirmed availability text and a real store URL only when supplied. Digward is not publicly advertised as available in this implementation.
5. Add published pages to `sitemap.xml`, update relevant footer links consistently, and run the checker.

Navigation and footer are intentionally present in every HTML file so they work without scripts or a build. Keep shared markup in sync when editing. Styling belongs in `assets/style.css`.

## Update privacy policies

Review the actual release app and provider documentation whenever SDKs, permissions, monetization, target audience, storage, or support practices change. Update the policy and its visible date, and reconcile the Google Play Data safety form and in-app link. Keep evidence and unresolved items in `docs/privacy-review.md`.

The HexGlow policy currently has `noindex, follow` and is omitted from the sitemap while it is a draft; it remains directly accessible without authentication or JavaScript. After resolving review items, remove the draft notice, replace draft-specific wording with confirmed practices, change robots to `index, follow`, and add its URL to the sitemap. Do not remove uncertainty by substituting unverified promises.

## Before publishing / Play submission

- Confirm the final release's SDK versions, merged permissions (including advertising ID), consent configuration, mediation partners, and Data safety declarations. Recheck the privacy draft against that release, then finalize it.
- Confirm the recorded 13+ audience and Play Console target countries/age groups. Test both age selections and required regional privacy choices.
- Confirm provider retention/deletion details and define the studio's support-email retention practice; update both policies as appropriate.
- Confirm the published Android app provides an accessible in-app privacy policy link (not found in the reviewed game code). Add it in a separate game change; this task leaves HexGlow untouched.
- Supply the actual Google Play listing URL and replace the availability note with a real store link. No fabricated store URL or disabled fake link is present.
- Review development screenshots for current appearance; replacements should come from the final game.
- Check AdMob's account-specific app-ads.txt instructions; add only the verified seller entry if required. No entry was invented.
- Complete browser/device visual checks, push, and enable Pages. Then supply `https://outertrailgames.github.io/hexglow/privacy.html` in Play Console and AdMob.

Public contact confirmed by the owner: **outertrailgames@gmail.com**.
