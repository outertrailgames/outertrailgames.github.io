# HexGlow website privacy review

Reviewed October 27, 2026. Source checkout: `C:/Users/T_Ada/Documents/Godot/Projects/hex-glow`. Read-only inspection; pre-existing modified and untracked files were left untouched. This is source-level evidence, not a production binary/network audit or legal compliance certification. The website is the only repository changed.

## Findings

| Topic | Evidence in HexGlow | Website treatment |
| --- | --- | --- |
| Identity | `scripts/purchase_service.gd`, Android export: `com.outertrailgames.hexglow` | Names HexGlow and Outer Trail Games |
| AdMob | `project.godot`, `scripts/ad_flow.gd`, `addons/AdmobPlugin/AdmobPlugin.gd` | Discloses third-party advertising data, not a no-data claim |
| SDK version | AdMob dependency `play-services-ads:24.9.0`; UMP `4.0.0` in `addons/HexGlowPrivacy/export_plugin.gd` | Final installed versions must be confirmed; current Google disclosure describes a newer SDK |
| Runtime ad configuration | Release uses real app-open/interstitial units; debug uses test units; first-party ID disabled; non-child-directed flag; G ad content rating | Disabling publisher first-party ID is not proof that advertising ID or other identifiers are absent |
| Consent | `native/privacy/HexGlowPrivacy.java`, `scripts/ad_flow.gd`, `scripts/purchase_panel.gd` | UMP gate, conditional Privacy choices, and Change age group described; console configuration and regional tests remain open |
| Audience | `nexus-node/docs/android-monetization-setup.md`: owner confirmed 13+; code stores under-16 boolean | Recorded audience disclosed; age prompt does not screen out under-13 users |
| Billing | `scripts/purchase_service.gd`: `hexglow_ad_free`; queries and acknowledges purchase tokens; caches ownership boolean | Describes Play checkout and restoration without promising removal of all service processing |
| Network permissions | `export_presets.cfg`: internet true; only explicitly enabled permission in source preset | Final merged manifest and advertising ID permission remain to inspect; no permission inferred absent from SDKs |
| Local storage | `scripts/save_store.gd`, `scripts/main.gd`: progress, attempts, exact puzzles, preferences, recovery files; ad age and entitlement config files | Local retention and Android clear-storage/uninstall instructions; distinguishes Google records |
| Backup | `export_presets.cfg`: `user_data_backup/allow=false` | Source configuration disables Android backup; confirm final artifact |
| Analytics/crashes | No separate Firebase, Sentry, analytics, crash reporting, HTTP endpoint or studio backend found in reviewed `scripts/` and `native/` | Qualified finding; SDK diagnostics explicitly disclosed |
| In-app policy | No privacy-policy URL found in reviewed scripts/native code | Separate game release action; game not edited |
| Contact | Owner supplied `outertrailgames@gmail.com` in this task | Used throughout website; support retention remains to define |

## Provider references

- [Google Mobile Ads data disclosure](https://developers.google.com/admob/android/privacy/play-data-disclosure): IP/approximate location, interactions, diagnostics, device/account identifiers, processing purposes and TLS. Current documentation describes version 25.5.0; reviewed project declares 24.9.0, so reconcile against final dependencies.
- [Google Privacy Policy](https://policies.google.com/privacy) and [retention explanation](https://policies.google.com/technologies/retention).
- [Google Play User Data policy](https://support.google.com/googleplay/android-developer/answer/10144311): public privacy policy, developer identity/contact, data handling, retention and deletion. A draft is not a completed release requirement.
- [GitHub Pages data collection](https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages#data-collection): GitHub logs visitor IP addresses for security.

## Owner / release confirmations still needed

1. Final release dependencies and merged manifest, advertising identifiers, AdMob mediation/other vendors, optional reporting settings, and actual network behavior. No additional vendors were identified in the inspected source configuration; console-side settings were not inspected.
2. Published AdMob consent messages, regional choice behavior, both age cohorts, and consistency between 13+ intent and Play audience declarations.
3. Provider-specific retention and deletion handling; the draft promises no invented retention period or deletion capability. Define support-email retention and request handling.
4. Real Play listing, current screenshots, in-app policy access, Data safety form, and any verified app-ads.txt entry.
5. Remove the draft status only after reconciliation. Use README's exact finalization and deployment steps.

## Asset provenance

Copied unchanged, not generated or represented as final-release screenshots:

- `assets/images/hexglow-icon.png` → `assets/icon/hexglow-512.png`.
- `assets/images/shapes.png` → `builds/generation-shapes-10-dark.png` (Form mode; original capture filename retained).
- `assets/images/colors.png` → `builds/generation-color_seams-10-dark.png`.
- `assets/images/light.png` → `nexus-node/docs/assets/procedural-validation/light_network-10-dark-complete.png`.

All selected images were visually inspected. The older `hexglow-three-modes.png` concept illustration was excluded. Studio mark is an original lightweight SVG; orbital decoration is CSS, not purported gameplay.

## Verification

The optional `tools/check_site.py` checks all HTML internal URLs and fragments, required metadata, image alternatives/dimensions, and absence of scripts and inline event handlers. HTTP smoke checks cover each requested route and its assets. Responsive CSS has stacked mobile layouts at 760/420 pixels, flexible navigation, constrained images, fluid headings, wrapped email addresses, and visible keyboard focus.

Browser automation inventory returned no available browsers in this session, so desktop/mobile visual rendering, zoom, and interactive keyboard checks remain manual. No claim of a completed visual device test is made. The live deployment is unverified until the owner pushes and enables Pages.

Completed checks: five HTML pages, 73 internal references, and 15 HTTP routes/assets passed. `git diff --check` passed. Served HTML/CSS/SVG/PNG assets total approximately 209 KB. No JavaScript is present.

## Data safety wording update - October 27, 2026

Updated the policy with explicit approximate location, interactions, diagnostics/performance, identifiers, age-group and purchase-history categories. Clarified transmission of the age flag to UMP/ads, purchase-token acknowledgement through Play, purposes, and limits of advertising controls. These statements describe source behavior, not a verified final Play Console submission. No new crash-log claim or provider retention period was introduced. Existing draft/release review status remains. Remaining game release checks are tracked in HexGlow's canonical `nexus-node/docs/android-monetization-setup.md`; this website update is recorded here.
