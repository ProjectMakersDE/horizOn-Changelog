---
layout: default
title: Dashboard Changelog
---

# Dashboard Changelog

All notable changes to the horizOn Dashboard (Frontend).

[Back to Overview](.)

## [1.103.3](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.103.2...v1.103.3) (2026-09-05)


### Bug Fixes

* **api-keys:** route account mutations session only ([4494f4e](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/4494f4ef45019319a12ae3ea965b17835cac3208))
* **blog:** harden renderer and content security policy ([b872f72](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/b872f7297371e16f2754d619ea25c50731035fdd))
* **release:** promote account-key and blog security fixes ([#35](https://github.com/ProjectMakersDE/horizOn-Dashboard/issues/35)) ([758f413](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/758f4130626d00248e121af521ff01ea43f9195a))

## [1.103.2](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.103.1...v1.103.2) (2026-08-20)


### Bug Fixes

* **users:** scope statistics and stabilize pagination ([128fa11](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/128fa11e69115fa9d97f5426200f331c30313120))

## [1.103.1](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.103.0...v1.103.1) (2026-08-13)


### Bug Fixes

* **ci:** dispatch changelog without gh cli ([f7df598](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/f7df598569c7f2cdfc048b705ef957ee2e2e8b66))

# [1.103.0](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.102.4...v1.103.0) (2026-08-13)


### Bug Fixes

* run dashboard CI on local runners ([812dacb](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/812dacbfc8c5b7d9a489f517631497f1fcad8b3a))


### Features

* **news:** add scheduled publication time ([54e243f](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/54e243ff34cfe2e892a0aeb10a15cd06392dcd77))

## [1.102.4](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.102.3...v1.102.4) (2026-08-08)


### Bug Fixes

* **api-keys:** forward never-expire account key choice ([7c75dc3](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/7c75dc3b07df62b14063b86adab790972e276752))

## [1.102.3](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.102.2...v1.102.3) (2026-07-31)


### Bug Fixes

* **blog:** disclose AI-generated images ([2f3c929](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/2f3c92901ba65198fde1f289c491296385588a6e))

## [1.102.2](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.102.1...v1.102.2) (2026-07-25)


### Bug Fixes

* **analytics:** make behavior insights actionable ([17f180a](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/17f180aca486f3b2c2cee43457a2a99074d71ac6))
* **analytics:** satisfy accessibility gate ([97ae945](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/97ae945a4f8b281801523faede7fdc55bda4433d))

## [1.102.1](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.102.0...v1.102.1) (2026-07-25)


### Bug Fixes

* **analytics:** rebuild behavior insights ([05a13d3](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/05a13d3e1ec08dc3fdaab416b552e7f8dcfd40ef))

# [1.102.0](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.101.0...v1.102.0) (2026-07-24)


### Features

* **blog:** render hero images at 3:2 ([35f8f19](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/35f8f196c18dcfb1640edec3198a309375cf9fb2))

# [1.101.0](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.100.2...v1.101.0) (2026-07-10)


### Features

* **quickstart:** video cards show real titles, tighter summaries and a lightbox player ([3149da3](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/3149da3c6ed451999cefabb3dc9e92947f8376aa))

## [1.100.2](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.100.1...v1.100.2) (2026-07-08)


### Bug Fixes

* **api-keys:** do not call the admin api-keys endpoint when logged out ([012ff78](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/012ff78a00d5d9ba980d5458499449debfb0c5c6))

## [1.100.1](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.100.0...v1.100.1) (2026-07-08)


### Bug Fixes

* **quickstart:** repair dead reference links and rework goal navigation ([ae9c795](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/ae9c7959c071278e81350cf056e709c1032150c6))

# [1.100.0](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.99.2...v1.100.0) (2026-07-08)


### Bug Fixes

* **i18n:** allow Seagull Storm example title in i18n check-strict ([4916d3d](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/4916d3d831cb91853c5375e4bf525bfb3850d7ef))
* **quickstart:** a11y labels, dead-import cleanup, DE label fixes, and funnel unit tests ([800f845](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/800f845159bb12034dc794acff0af655f19a153c))
* **quickstart:** drop non-functional sticky plan bar (global app-root overflow blocks position:sticky) ([08d3d2e](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/08d3d2e4e754c1b2b18f0d709880a1ec507b9435))
* **quickstart:** rate-limits reference body, one-player Erkunden tour, sticky plan bar, engine-switch step sync ([f49f310](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/f49f310382249a0606311a6ee1e65a606bf5ff46))
* **quickstart:** stop SDK guide clobbering page title, hide step counter for stepless track ([e6be325](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/e6be3254cb3595f734bc7bdeb0bd4ba4a2627290))


### Features

* **quickstart:** example cards and collapsed reference accordion ([b6cc683](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/b6cc6832530d0213f5aaea02c822b022c57baddc))
* **quickstart:** funnel i18n keys in 15 languages ([bc87853](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/bc8785387cadc0b90002aa448a92cfa72377fc76))
* **quickstart:** funnel model interfaces ([dbfe2a4](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/dbfe2a4141628fca0123214e7b97884bcb575d89))
* **quickstart:** goal cards, plan bar, hero, engine picker ([fbd2fe4](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/fbd2fe480fa4655ae14f520dbf2f3969c6a6258d))
* **quickstart:** guided step card with copy block and step video ([5396c7b](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/5396c7b9d351f3baa9c8bef6c09ec9f6640222ed))
* **quickstart:** quiet video card (poster + summary, no autoplay) ([96323ca](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/96323ca6364087e6c9ace5d03e62251f0a84f3c7))
* **quickstart:** rewrite page as goal-first funnel orchestrator ([8b1b2cd](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/8b1b2cd16dd4ad61e0bcb3ce0e6e1423d44ea96d))
* **quickstart:** show "recommended to start" hint on the suggested goal card ([a6e1f21](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/a6e1f21a6efb128759c337e3dbb48e6a1b1c3333))
* **quickstart:** stepper with single open step and progress ([24dffab](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/24dffab48789431c121f881a4309f748f5827b2b))
* **quickstart:** track data for Ausprobieren and Einbauen ([e9968d1](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/e9968d19eb8c757ec33a3d9eae3b666b43b0bc0d))

## [1.99.2](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.99.1...v1.99.2) (2026-07-04)


### Bug Fixes

* **dashboard:** show serving region in version footer instead of "unknown" ([995989a](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/995989adedc4d520e2373e2eada0467e4c255aec))
* **frontpages:** resolve PageSpeed accessibility, contrast, and image audits ([d01c50b](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/d01c50b5df448fe66697ec7f4b4f6e2ccd43190a))

## [1.99.1](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.99.0...v1.99.1) (2026-07-02)


### Bug Fixes

* **ssr:** allow R2 tutorial videos via media-src in the CSP (TASK-387) ([1f5b3da](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/1f5b3da68fb245d21a32be20966f10fe8e368edf))

# [1.99.0](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.98.1...v1.99.0) (2026-07-02)


### Features

* **quickstart:** embed the 15 R2-hosted tutorial videos in the Dashboard Guide (TASK-387) ([f110e2b](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/f110e2b5249b9963f39ebb55c15bb90b42d52b76))

## [1.98.1](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.98.0...v1.98.1) (2026-06-27)


### Bug Fixes

* **dashboard:** localization + email AI-translate use the News table-action modal (TASK-372/373) ([#18](https://github.com/ProjectMakersDE/horizOn-Dashboard/issues/18)) ([1a84b64](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/1a84b64828ed45f7ddb1bd3f3a8e7f784b41a4f5)), closes [#17](https://github.com/ProjectMakersDE/horizOn-Dashboard/issues/17)

# [1.98.0](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.97.0...v1.98.0) (2026-06-26)


### Features

* **dashboard:** AI translation for email templates & localization, email tab/list UX fixes ([#17](https://github.com/ProjectMakersDE/horizOn-Dashboard/issues/17)) ([07c5d71](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/07c5d71bd7c5258ad9d68de729ac5f35ae1e1275))

# [1.97.0](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.96.1...v1.97.0) (2026-06-26)


### Bug Fixes

* **localization:** reachable Import Language trigger, strict-safe copy-key, correct empty-state route ([0d27a00](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/0d27a003b07cff6fdfcee7c2f5d07599a0235c2f))
* **routing:** keep multi-segment localize paths as one router command ([4d26774](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/4d267748031a1a89ca67fd6cfcb4010fce107991))


### Features

* **crash-reporting:** occurrence-detail device + stack-trace testids for tutorial capture ([ad538d8](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/ad538d8de5b9d1898e076249fabada1e8b2ef1cf))

## [1.96.1](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.96.0...v1.96.1) (2026-06-25)


### Bug Fixes

* **localization:** reachable Import Language trigger, strict-safe copy-key, correct empty-state route ([c04141d](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/c04141d88436e0a77460a9be5424cd9a45444536))

# [1.96.0](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.95.1...v1.96.0) (2026-06-24)


### Bug Fixes

* gated dev-only /api proxy in SSR server so the dev box reaches the backend ([d11260b](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/d11260b66eeda8359fdf309b02861091b59c697d))
* **localization:** tolerate a list response without entries (avoid load crash) ([f9b45a8](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/f9b45a8b15039d01f2f7a1d4744b3e202e3a22ed))


### Features

* **localization:** dashboard quickstart for all SDKs + System Config category ([69052c5](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/69052c5e73706b2e4e7ee7de39594d26f13e00b8))
* **localization:** management UI, frontpages, and 15-language i18n ([43d076a](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/43d076ae8378ecb587685dfd358ed8cbc56a3815))

## [1.95.1](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.95.0...v1.95.1) (2026-06-21)


### Bug Fixes

* **icons:** restore icon size & centering after iconify migration (TASK-343) ([042c2cf](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/042c2cf20417d8570c1971fcf738a0c47f2d9645))

# [1.95.0](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.94.4...v1.95.0) (2026-06-21)


### Bug Fixes

* **home:** TASK-178 fix hero LCP preload and deprioritize decorative seagull ([39b0fe3](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/39b0fe370779a763a20aaa03fb9131d585c92c75))
* **legal:** render legal pages under zoneless change detection via signals ([96e6d4b](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/96e6d4badf65304b965822b2b6f460c1eee6d3b2))


### Features

* **dashboard:** add data-testid coverage for tutorial capture (TASK-333) ([049de85](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/049de8542abf9cbbd61631455551a878ea66b9e8))
* **dashboard:** migrate icons from lucide-angular to offline iconify-icon (line-md) ([74b7c6c](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/74b7c6c6ff1b79491d2131e9765d0f4b4df2d29d))

## [1.94.4](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.94.3...v1.94.4) (2026-06-15)


### Bug Fixes

* **ssr:** trust x-forwarded-scheme so ingress renders SSR not CSR shell ([0a1306c](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/0a1306cca07f1184af0bf15f303da33840e1ed1f))

## [1.94.3](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.94.2...v1.94.3) (2026-06-15)


### Bug Fixes

* **ssr:** fetch public SSR data over internal cluster DNS (TASK-317) ([b674e49](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/b674e496da4ecaf6c7c1a50a954f2d30e487085a))

## [1.94.2](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.94.1...v1.94.2) (2026-06-15)


### Bug Fixes

* **ssr:** render pages with AngularNodeAppEngine instead of empty CSR shell ([c536376](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/c536376c7499f2281e8bb8d0ec59b432bbbdb754))

## [1.94.1](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.94.0...v1.94.1) (2026-06-14)


### Performance Improvements

* **ssr:** cache evergreen pages 12h and blog 1h (was 10min) ([61cb151](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/61cb15188dce66f80d9606f52d3eaf53857b8929))

# [1.94.0](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.93.0...v1.94.0) (2026-06-11)


### Bug Fixes

* **auth:** keep access tokens in memory ([17c8ce1](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/17c8ce10c09d56f2e66096394fcdddc8df851b62))
* **auth:** preserve session across reload ([a8a9488](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/a8a9488eef2fb34c74af588d811e7102a38bac3c))
* handle api explorer in dev mode ([fb54730](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/fb547306b46fce9e42fe190fac5d61cfaced6938))
* strengthen dashboard coverage quality gates ([67f90e6](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/67f90e64f37a483b6a02b639465f576afbd2ccbc))


### Features

* expand api explorer endpoint runner ([66176cf](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/66176cfeb7c2d766f29e3e7df0346ff78257537e))
* improve api explorer project testing ([d8b40a1](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/d8b40a12b5103d97f8a5810bdec51a5e2219079b))
* merge API explorer updates into main ([9fa110b](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/9fa110b124ade91cc280aef00d75fac73b5a7e40))

# [1.93.0](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.92.0...v1.93.0) (2026-06-05)


### Bug Fixes

* **analytics:** guard behavior-analytics chart/timeline against missing points/events (TASK-276) ([fae5e12](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/fae5e123e591dc2304ce84f37937b6853f0f5bc5))
* **i18n:** translate behavior-analytics frustration terms + titles for strict gate (TASK-276) ([69825ff](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/69825ff77647cb5a539e2f8460d85dcf43560c8a))


### Features

* **analytics:** rework behavior-analytics page into 5 tabs (TASK-276) ([dec3f81](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/dec3f819e7812190b3be6172e60da006e36db6cf))

# [1.92.0](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.91.1...v1.92.0) (2026-06-05)


### Bug Fixes

* **frontpages:** survive a partial public-stats response (whole-site crash) ([c9bfeaf](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/c9bfeaf317683d6856586bb73c051a5b14609064))


### Features

* **analytics:** behavior capture + admin behavior-analytics page (TASK-276) ([196661f](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/196661ffdfe700d478d6aa401e378c2f8ae06da8))

## [1.91.1](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.91.0...v1.91.1) (2026-06-03)


### Bug Fixes

* **home:** give testimonial cards a fixed height with clamp and modal ([793beae](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/793beaef40913463beb867fe73795df87bdea32d))

# [1.91.0](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.90.0...v1.91.0) (2026-06-03)


### Features

* **seo:** English default served unprefixed at / (TASK-275) ([1bfe73f](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/1bfe73f761e84f09b92246fb86bf155cd0b2791c))

# [1.90.0](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.89.0...v1.90.0) (2026-06-02)


### Bug Fixes

* align product/quickstart specs with forced horizon.pm base ([e650fdb](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/e650fdbb7c83aa93cbb2260041d8c77a7092c92b))
* **frontpages:** enforce section alternation; fix pricing/home/about-us layout ([52b2850](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/52b28505ae16399de23f074e7d9463fa48817039))
* **seo:** derive SSR canonical/hreflang path from the request URL (TASK-263) ([8e8bc65](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/8e8bc656efa581ecf4713f86433abcd7ac041ca1))


### Features

* **dashboard:** per-language URL routing (TASK-263) + TASK-270 frontend batch ([4e4f7d8](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/4e4f7d82b6a95f568522f6183d1bc25591a24530))
* **frontpages:** TASK-273 usability and UX overhaul ([b3edad2](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/b3edad2a499f6fbbbd4f2a1ea55178416abf7fb9))
* **frontpages:** TASK-274 design + real-data corrections (review of TASK-273) ([f9d79c1](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/f9d79c1255c2e6a9137e31e62d49fc1e220ab002))
* **quickstart:** consolidate docs hub into /quickstart, remove colliding frontend /docs ([9c69d1f](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/9c69d1f8dd86e4c6b7c33b2ac792318d99aa6e3a))
* **seo:** localize per-page title + description via SeoService (TASK-271 [#4](https://github.com/ProjectMakersDE/horizOn-Dashboard/issues/4)) ([61bb0c6](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/61bb0c6c5030f60ed7976b46025a365263fe2a28))

# [1.89.0](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.88.0...v1.89.0) (2026-05-22)


### Features

* add dashboard api explorer ([451e90f](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/451e90f011a98fa9e10cca995b168f4c75333ae5))

# [1.88.0](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.87.8...v1.88.0) (2026-05-22)


### Features

* add searchable docs guide hub ([a5c658d](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/a5c658df621fd21aeedf2d136714de85251b225f))

## [1.87.8](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.87.7...v1.87.8) (2026-05-22)


### Performance Improvements

* enable zoneless dashboard change detection ([2a3e79a](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/2a3e79a569463de75aef93bf503fb3852dc13c0b))

## [1.87.7](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.87.6...v1.87.7) (2026-05-22)


### Performance Improvements

* unblock frontend init pipeline ([b89c0af](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/b89c0afb2290d696047e5c6266a587f2f9fe99f5))

## [1.87.6](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.87.5...v1.87.6) (2026-05-22)


### Bug Fixes

* **dashboard:** keep prerendering disabled; supply MENU_ITEMS to SSR config ([d03e0ac](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/d03e0acc48a852004382fa6f88058aff63cd0c4b))

## [1.87.5](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.87.4...v1.87.5) (2026-05-22)


### Bug Fixes

* **consent,tracking:** queue cookie-consent calls; bound sendBeacon by byte size ([d481443](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/d4814433360adaed12b9bfce876417dc5628fd64))


### Performance Improvements

* **bundle:** lazy-load marked, vanilla-cookieconsent; drop SSR compression ([9a13579](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/9a13579fea8dae21302d2140584db81b8d46add9))
* **dashboard:** bound tracking payload, plug modal subscription leak, shell to OnPush ([ea0bead](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/ea0bead01be4b6c7eb2bad431d2eedbf255da496))
* **dashboard:** cache public GET requests, default page size 25, trim prod logging ([c171099](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/c1710994d04f4f95d6563590f47d412f54facc72))

## [1.87.4](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.87.3...v1.87.4) (2026-05-15)


### Bug Fixes

* **i18n:** translate fallback values across all 36 i18n directories and gate CI on translation coverage ([c656532](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/c656532339413f6331165fbd684e9a92dd02d3e8))

## [1.87.3](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.87.2...v1.87.3) (2026-05-15)


### Bug Fixes

* **ci:** gate dashboard build on i18n key parity ([d52a0aa](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/d52a0aaf8000e1504655d1cc8d9d91770ec72c0c))

## [1.87.2](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.87.1...v1.87.2) (2026-05-15)


### Bug Fixes

* **i18n:** translate reactivate keys for admin-account in 13 languages ([ffadf82](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/ffadf82e60f521d7411b2f30b1a66a0446844508))

## [1.87.1](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.87.0...v1.87.1) (2026-05-14)


### Bug Fixes

* **quickstart:** cover all 10 core features per engine in /quickstart (TASK-217) ([46020a8](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/46020a82e03d49d6653c48fcd34f8fcf05470ce5))

# [1.87.0](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.86.3...v1.87.0) (2026-05-12)


### Features

* **dashboard:** show region versions and edit user roles ([446ea1f](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/446ea1f994747804ba9ab3ed8573a1df2821ffcd))

## [1.86.3](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.86.2...v1.86.3) (2026-05-11)


### Bug Fixes

* **account:** show banner and reactivate CTA for soft-deleted accounts ([28f1c4d](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/28f1c4d7c92e3018a4c2249692ad6544c3bbc7b0))

## [1.86.2](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.86.1...v1.86.2) (2026-05-09)


### Bug Fixes

* **i18n:** update leaderboard FAQ and quickstart for multi-board feature ([86ebb75](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/86ebb75c2f6a992d5fc8521ffb1a9e952567a5cc))

## [1.86.1](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.86.0...v1.86.1) (2026-05-09)


### Bug Fixes

* show multi-leaderboard limit in pricing comparison ([28aa975](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/28aa9750f42c0a911763e1fc0a5aae068a413475))

# [1.86.0](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.85.3...v1.86.0) (2026-05-09)


### Features

* **leaderboard:** multi-board management UI ([#10](https://github.com/ProjectMakersDE/horizOn-Dashboard/issues/10)) ([9841444](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/9841444eb080f8dac51ec9c899cb305d5c68eacb))

## [1.85.3](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.85.2...v1.85.3) (2026-04-29)


### Bug Fixes

* preserve llm keys and translation parsing ([fe6233e](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/fe6233e5fde9b0c6843e4e2299c6bc96ebe5f5dc))

## [1.85.2](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.85.1...v1.85.2) (2026-04-29)


### Performance Improvements

* improve modal performance ([d39fa36](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/d39fa368e50e7425f5ecea3b9178384de5acf517))

## [1.85.1](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.85.0...v1.85.1) (2026-04-27)


### Bug Fixes

* **api-keys:** hide account scope fields for project keys ([137cd1c](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/137cd1c1c703285ab1c11dcb64a8390828e492d6))

# [1.85.0](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.84.1...v1.85.0) (2026-04-27)


### Features

* **api-keys:** add account key scope controls ([bbc46bf](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/bbc46bf0f0ddb45a09b3b296758d52e3fdb21da0))

## [1.84.1](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.84.0...v1.84.1) (2026-04-26)


### Bug Fixes

* improve dashboard filtering and navigation ([5ee624e](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/5ee624e5bfd2aeaff30d4cadfd1b0042b13e201a))

# [1.84.0](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.83.3...v1.84.0) (2026-04-26)


### Features

* add Apple Sign-In API key configuration modal ([5c70dfd](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/5c70dfd173f6bd62f8958d219e9e233af7f4e821))

## [1.83.3](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.83.2...v1.83.3) (2026-04-25)


### Bug Fixes

* **user-management:** route deactivate to user's api-key in all-keys mode ([aef693d](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/aef693dfc49c9f8f659d9da842d31bedd8300132))

## [1.83.2](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.83.1...v1.83.2) (2026-04-20)


### Bug Fixes

* **blog:** remove pause/resume keep-alive that triggered TTS 'interrupted' error ([4aab3df](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/4aab3df66af4d10045c5512982da0fff942e4c8a))

## [1.83.1](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.83.0...v1.83.1) (2026-04-20)


### Bug Fixes

* **blog:** resolve silent text-to-speech playback on article detail ([81742c9](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/81742c9c7109b6d120df140ced56a923f0d1fbea))

# [1.83.0](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.82.5...v1.83.0) (2026-04-20)


### Bug Fixes

* **email-templates:** correct required variables and improve template documentation ([82b2acb](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/82b2acbb1bf11f0f0b934e33995dcf506b9a4072))
* **email-templates:** correct required variables for system email templates ([244a600](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/244a600ba30452680bd2df6efaa0532ecb243a07))
* **email-templates:** i18n updates for 14 languages (TASK-130) ([ec2f3c2](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/ec2f3c274b6a6831143e6628f5177d92b96ead74))


### Features

* **blog:** add summary box and text-to-speech to blog detail view ([49da0fe](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/49da0fe3c1b6e3706892a1b6eb0d440319ce9bc1))
* **blog:** add summary box and TTS read-aloud to blog detail view ([bf69dee](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/bf69dee604de6d4a6df0dd3f058f190e97f7f7d8))
* **blog:** i18n translations for blog public read features (TASK-1) ([7367433](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/73674338fc0acd4067f436b16f69c9d431bb2425))

## [1.82.5](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.82.4...v1.82.5) (2026-04-20)


### Bug Fixes

* unblock docker build for pre-built artifacts + clean up about-us dead code ([e048367](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/e048367d793fe87ac126e6571bd59b6c76d61fb5))

## [1.82.4](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.82.3...v1.82.4) (2026-04-20)


### Bug Fixes

* TASK-142 landingpage polish, mobile layout, dashboard sidebar scroll ([9151b19](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/9151b190d13776e32b17a3a3cbad7c4a7026fad8))

## [1.82.3](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.82.2...v1.82.3) (2026-04-20)


### Bug Fixes

* **apple-signin:** correct client-id prefix and button UX ([bf1b52e](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/bf1b52eee7fd084f175279b5654da362a44fcae9))

## [1.82.2](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.82.1...v1.82.2) (2026-04-20)


### Bug Fixes

* **apple-signin:** allow apple CSP script/frame sources ([620a1af](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/620a1afe2e3c585476be8b26ea654bb684019589))

## [1.82.1](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.82.0...v1.82.1) (2026-04-20)


### Bug Fixes

* **apple-signin:** align response account type with backend Account interface ([ae43b22](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/ae43b2208673db59e860d303e99fb04eee31c986))

# [1.82.0](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.81.0...v1.82.0) (2026-04-20)


### Features

* **apple-signin:** add Sign in with Apple support to dashboard ([4c83b9a](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/4c83b9a02d61c6daa486322c9a24658f9b40c4f9))

# [1.81.0](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.80.0...v1.81.0) (2026-04-18)


### Features

* **user-management:** replace max-users stat with limit card ([a907811](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/a907811fa6e0fff604d9042f01ab9a53284498cc))

# [1.80.0](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.79.0...v1.80.0) (2026-04-18)


### Bug Fixes

* **resources:** make structured-data spec resilient to test order randomization ([4e6014d](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/4e6014dbbe11b0f1f9fec240d6eea2758aaa423b))


### Features

* **user-management:** add resend verification email action ([7ccc189](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/7ccc189c310cf4a8ede27ff1f3682fed51cfcce3))

# [1.79.0](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.78.1...v1.79.0) (2026-04-18)


### Features

* **home:** replace simple integration card with 5-minute step tabs ([d534e98](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/d534e98dfccb5a9c56b42f4bfcdaff2dbcba9031))
* **home:** streamline trust section and add continuity faq ([c103e12](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/c103e12e19d61484b357923c336aadc05106bd9d))

## [1.78.1](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.78.0...v1.78.1) (2026-04-17)


### Bug Fixes

* **remote-config:** validate bulk import json against plan limits client-side ([94953f4](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/94953f4bad2d5a895a18d2076d02212eba79ee33))
* **theme:** raise light-theme primary and muted-text contrast to WCAG AA ([b96e956](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/b96e9563e7922881fa5e4012544c8e7514f832cc)), closes [#D87943](https://github.com/ProjectMakersDE/horizOn-Dashboard/issues/D87943)
* **users,remote-config:** deduplicate users-tab cards and move import button into page header ([3e1e05e](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/3e1e05ef9933861bcdb43bbddc6e68ba32b00d52))

# [1.78.0](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.77.3...v1.78.0) (2026-04-16)


### Bug Fixes

* **about:** update test counts for frontend and backend ([81c50cd](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/81c50cdb904ad49a5bb75ac419d17aadeef0f1fd))
* **api-keys:** conditional modal info text and move key type to status filter area ([95f213e](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/95f213e88d3aca6db390cf2b0b620acdfbeac952))
* **api-keys:** guard against non-array response in getAccountApiKeys ([5aa5068](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/5aa5068e5f2bbb57c1c10439f696289f45d60f76))


### Features

* **api-keys:** add API layer for account-api-keys endpoints ([9ff04c0](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/9ff04c06a9f6e91db43107a961a111bc616bd527))
* **api-keys:** add i18n for key type filter and mcp setup (15 languages) ([6ee0e96](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/6ee0e96e1aeff61e3503902dcdfaa6f23bcb8296))
* **api-keys:** add keyType to ApiKey interface and DTOs ([9358aa3](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/9358aa3c61352cdfd992a59b03f4c96ecef9d59c))
* **api-keys:** add type select filter tabs and mcp setup snippet ([6450cd1](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/6450cd1aaacca82d577b4538cc2f982b7e069fbe))
* **api-keys:** unified service for project and account keys ([38068a1](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/38068a1256a05577f8ed97a86385128cd39f9eb9))

## [1.77.3](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.77.2...v1.77.3) (2026-04-14)


### Performance Improvements

* **blog:** use embedded adjacent posts from detail response to cut 4.98MB ([4935a92](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/4935a92bd09087feebd16bf8cc4132613b8213dd))

## [1.77.2](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.77.1...v1.77.2) (2026-04-14)


### Bug Fixes

* **dashboard:** break leaderboard effect loop and restore remote-config import button ([30a76a4](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/30a76a43ec2e5b996ce7acb8be7b688864d4405e))

## [1.77.1](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.77.0...v1.77.1) (2026-04-14)


### Bug Fixes

* **dashboard:** apply global api-key filter on feature navigation and shrink stat card value text ([bd23c43](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/bd23c43bb346c94b5583387b4816148c02302e9a))

# [1.77.0](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.76.0...v1.77.0) (2026-04-13)


### Features

* **dashboard:** unified shared feature-layout with prominent global API key selector ([05ef4c2](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/05ef4c29760e4bb338c93c9579b847b751e580ae))

# [1.76.0](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.75.0...v1.76.0) (2026-04-13)


### Features

* **dashboard:** apply shared feature-layout across all dashboard features ([a10faa3](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/a10faa37286ce64a9bef11bdc5450b2c09ba1ee8))

# [1.75.0](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.74.0...v1.75.0) (2026-04-13)


### Features

* **dashboard:** introduce global api-key selector in dashboard topbar ([0f511d8](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/0f511d8d0f9a3f612329b51e32f752391e2e40ca))

# [1.74.0](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.73.4...v1.74.0) (2026-04-13)


### Features

* **dashboard:** introduce shared feature-layout components ([09e3f1c](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/09e3f1cd35c797cbb98f540318ca15aea63be0b8))

## [1.73.4](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.73.3...v1.73.4) (2026-04-12)


### Bug Fixes

* pin email-sending seagull to background content via shared canvas ([18ddd1f](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/18ddd1f83bc11d552c84e4c05d10fa2213fab2d3))

## [1.73.3](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.73.2...v1.73.3) (2026-04-12)


### Bug Fixes

* move email-sending seagull 4% further down so it sits on the computer ([042530a](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/042530af82c854d9a0f0ea86c9185d18b4a3cdae))

## [1.73.2](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.73.1...v1.73.2) (2026-04-12)


### Bug Fixes

* regenerate email-sending webp fallback, remove orphan avifs ([a48a1ea](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/a48a1eafd223d58134e258f61050dbc60e82ab6c))
* stop forcing object-fit: contain on email-sending background ([69a5bd9](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/69a5bd99215962dbb9407c211547278b7ed4e758))

## [1.73.1](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.73.0...v1.73.1) (2026-04-12)


### Bug Fixes

* crop email-sending feature background to 2.357 aspect ([68d78a1](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/68d78a134ba0dc539f3ea30087c44fc552ac9fcf))

# [1.73.0](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.72.0...v1.73.0) (2026-04-12)


### Features

* apply playground-generated email-sending feature background ([d0dee88](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/d0dee885c67c0f4477ccc67a96821ad0d565c1f1)), closes [#f39c12](https://github.com/ProjectMakersDE/horizOn-Dashboard/issues/f39c12) [#ff8a65](https://github.com/ProjectMakersDE/horizOn-Dashboard/issues/ff8a65)

# [1.72.0](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.71.2...v1.72.0) (2026-04-12)


### Features

* test SMTP with unsaved form and update new bento image ([9367424](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/93674248fc85551de503b12667e1f034a9484e9a))

## [1.71.2](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.71.1...v1.71.2) (2026-04-12)


### Bug Fixes

* regenerate EmailSending bentogrid placeholder ([a312a37](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/a312a37905572f0ec7d485a5ec6fdb9a143445bf))

## [1.71.1](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.71.0...v1.71.1) (2026-04-12)


### Bug Fixes

* move SMTP banner and sender override i18n keys to correct namespace ([3a1b951](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/3a1b951206657e3f08b9d4b4af2532e7b92b9187))

# [1.71.0](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.70.0...v1.71.0) (2026-04-12)


### Features

* boost test coverage to 86% statements, add 238 tests ([a419cbb](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/a419cbb07b889fcae771bce82f98bf65f844ab34))

# [1.70.0](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.69.0...v1.70.0) (2026-04-11)


### Bug Fixes

* **email-sending:** add missing feature background and bentogrid images ([02b9b43](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/02b9b4388f0e1f39fac67df169447bb2f50ec164))


### Features

* add SMTP settings UI and system email templates support ([668541f](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/668541f25ea09207fc4a05096516154a4f3e1a29))

# [1.69.0](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.68.0...v1.69.0) (2026-04-11)


### Features

* **email-sending:** add multi-language template form and pricing table entry ([8635136](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/8635136265c2e787e7b3198f6636d2bfa60bfc65))

# [1.68.0](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.67.7...v1.68.0) (2026-04-11)


### Features

* **email-sending:** add email sending management feature ([15a82af](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/15a82af542ee6d381300568f9c950e0e49fa6c3b))

## [1.67.7](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.67.6...v1.67.7) (2026-04-11)


### Bug Fixes

* **remote-config:** use bulk delete endpoint instead of parallel individual requests ([e2bece5](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/e2bece5f6a1f7236f49ab60bb5382b5d659fe0a1))

## [1.67.6](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.67.5...v1.67.6) (2026-04-11)


### Bug Fixes

* **remote-config:** improve import dialog hint text visibility ([ea573c8](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/ea573c8dc13a077bc7277e64fe8a5c17d09c364a))

## [1.67.5](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.67.4...v1.67.5) (2026-04-10)


### Bug Fixes

* apply persisted API key filter on init for leaderboard and feedback ([5c422f7](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/5c422f7a1655acc4d5450a0769d99d9044cc855b))

## [1.67.4](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.67.3...v1.67.4) (2026-04-10)


### Bug Fixes

* remove debug logs from API key filter chain ([1a495dc](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/1a495dc6efa5c73377597b5d1bcc2e53c82263b5))

## [1.67.3](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.67.2...v1.67.3) (2026-04-10)


### Bug Fixes

* add debug logs to leaderboard and user management handlers ([bc6c732](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/bc6c732c934e28d679a2ad1be1a2f7e20867e38c))

## [1.67.2](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.67.1...v1.67.2) (2026-04-10)


### Bug Fixes

* add debug logging to API key filter chain ([fe981a4](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/fe981a46787bbbc6c5f74bb9ebf040ea17380336))

## [1.67.1](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.67.0...v1.67.1) (2026-04-10)


### Bug Fixes

* API key selector binding and filter propagation ([a25ed97](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/a25ed9718839dfbcd87964d382af08be81acbff2))

# [1.67.0](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.66.1...v1.67.0) (2026-04-10)


### Features

* global API key selector with session persistence ([2a90a04](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/2a90a04c12f4739a45db423fdb59b1883c292035))

## [1.66.1](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.66.0...v1.66.1) (2026-04-10)


### Bug Fixes

* **remote-config:** load all entries and fix action column width ([956ec5a](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/956ec5a0d918df8e0c7cb66946b801ab20d929ba))

# [1.66.0](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.65.4...v1.66.0) (2026-04-10)


### Features

* standalone email-verified page without dashboard shell ([34762f5](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/34762f597a399b03a2c190bbd8bc9f2c0203febb))

## [1.65.4](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.65.3...v1.65.4) (2026-04-10)


### Bug Fixes

* correct bug bounty background alignment and improve nav divider visibility ([82f752c](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/82f752cf97ea49b3cd3f536daeb7248375fef622))

## [1.65.3](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.65.2...v1.65.3) (2026-04-10)


### Bug Fixes

* revert hero gradient to original and upgrade nav button styling ([d118421](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/d1184215f98f5ceea4955c951da2b5e4e550bfea))

## [1.65.2](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.65.1...v1.65.2) (2026-04-10)


### Bug Fixes

* correct bug bounty background coverage and make hero-gradient compositable ([c41bae3](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/c41bae3969e4766da6585a4c73971dc8a6faf91f))

## [1.65.1](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.65.0...v1.65.1) (2026-04-10)


### Performance Improvements

* improve PageSpeed score with LCP preload, nav reorder, and background fix ([ed07c7d](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/ed07c7dad756e686c7364f46f7be169a713d376e))

# [1.65.0](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.64.1...v1.65.0) (2026-04-09)


### Features

* **dashboard:** capture UTM parameters in tracking collect service ([#6](https://github.com/ProjectMakersDE/horizOn-Dashboard/issues/6)) ([fa514f6](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/fa514f676910fc2524f2f3832491b194aac41985))

## [1.64.1](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.64.0...v1.64.1) (2026-03-21)


### Bug Fixes

* resolve animation clipping on feature and bug bounty background layers ([7ac83b1](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/7ac83b176275c57c98778f43ccbca85f477d6c96))

# [1.64.0](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.63.0...v1.64.0) (2026-03-21)


### Features

* add animated 3-layer background system for all feature pages and bug bounty section ([cf0f544](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/cf0f544bca7d4460d8e887b103eb6c4eb8aac5b8))

# [1.63.0](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.62.4...v1.63.0) (2026-03-18)


### Features

* replace WebP backgrounds with responsive AVIF on about and compare pages ([de61b32](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/de61b32ace21ffce8bc7fff551e68ffad02dd094))

## [1.62.4](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.62.3...v1.62.4) (2026-03-18)


### Bug Fixes

* reduce backdrop-blur from 10px to 6px and add glass effect to price cards ([4411d44](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/4411d44da5f5dd9f8e565c3bf2373b6d57234804))

## [1.62.3](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.62.2...v1.62.3) (2026-03-18)


### Bug Fixes

* fix section background animations and gradients stripped by Tailwind CSS 4 build ([758ef99](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/758ef997f15a588d5accc471a15bd13601746a9b))

## [1.62.2](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.62.1...v1.62.2) (2026-03-18)


### Bug Fixes

* align video language hint with YouTube settings button in real browsers ([dcc6e5c](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/dcc6e5cbca33d31f475172abc6b9313a8e97ad14))

## [1.62.1](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.62.0...v1.62.1) (2026-03-18)


### Bug Fixes

* add video language hint below YouTube embeds in quickstart guides ([b13e40d](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/b13e40df10306cf55d5e6b9be6a14e761dfecfbc))

# [1.62.0](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.61.2...v1.62.0) (2026-03-18)


### Bug Fixes

* increase hero section height to 80vh for better card visibility on FullHD ([438c565](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/438c565da231322203d74acae45356a4d231cdc0))
* unify landing page typography for consistent font sizes ([7c393d8](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/7c393d8c5343e15e4387e80673b7293894886615))


### Features

* add animated background layers with seagulls for all homepage sections ([0ee06b8](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/0ee06b80aad016f373c54151c19d5a9fb6e3a801))

## [1.61.2](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.61.1...v1.61.2) (2026-03-13)


### Bug Fixes

* increase AVIF quality to q50 for small hero image breakpoints ([4446c6b](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/4446c6bb0754a788387cf689c557f3f2bab58813))

## [1.61.1](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.61.0...v1.61.1) (2026-03-12)


### Bug Fixes

* revert non-hero images back to WebP and fix pixel-wave divider z-index ([3eb211f](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/3eb211fdae0ff4f6245c8063d495108831dc1896))

# [1.61.0](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.60.2...v1.61.0) (2026-03-12)


### Features

* add animated 3-layer hero background and migrate to AVIF format ([2400da7](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/2400da746ca4a193374f9ab357d0b76623a9d678))

## [1.60.2](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.60.1...v1.60.2) (2026-03-12)


### Bug Fixes

* **comparison:** use hardcoded competitor names instead of translation keys ([7cf5657](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/7cf56573d5ba6c60ffd398898ddcb2a802d53c4d))
* improve background image quality and remove bg-fixed rendering issue ([42fffde](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/42fffded206de750cba2368f02df1ccf610a1dd5))

## [1.60.1](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.60.0...v1.60.1) (2026-03-06)


### Bug Fixes

* resolve comparison page issues and update homepage pricing ([98f3ae3](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/98f3ae3b86af78de9993d38a309be7811a79c171))

# [1.60.0](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.59.1...v1.60.0) (2026-03-06)


### Features

* **comparison:** use real Stripe prices and server-side exchange rate ([19d1db2](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/19d1db23a06bca594043355af717fb9473d5c207))

## [1.59.1](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.59.0...v1.59.1) (2026-03-06)


### Bug Fixes

* correct pricing tiers and translation interpolation on comparison pages ([766dc88](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/766dc88c941895790b8bb48d4c89a7af9edcd470))

# [1.59.0](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.58.5...v1.59.0) (2026-03-06)


### Features

* add SEO comparison pages (hub + 8 competitor alternatives) ([d0bb286](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/d0bb2865fe8f7cfbd36fb78c172c1f576f74a557))

## [1.58.5](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.58.4...v1.58.5) (2026-03-04)


### Bug Fixes

* **crash:** reload group after status/notes update instead of parsing empty 204 response ([5f247c6](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/5f247c633eeedb8f621e384ebaee24ee5bde11e1))

## [1.58.4](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.58.3...v1.58.4) (2026-03-04)


### Bug Fixes

* **crash:** register missing lucide icons for crash reporting ([b61514e](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/b61514eaa6b0d3ab860bba7c455ba4e607979498))

## [1.58.3](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.58.2...v1.58.3) (2026-03-04)


### Bug Fixes

* **about:** remove gap between top-nav and hero section ([f97573a](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/f97573a3618cf3c9ff8d37bd75b41a1cfbeb464c))

## [1.58.2](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.58.1...v1.58.2) (2026-03-04)


### Bug Fixes

* **home:** standardize typography to 4 consistent font sizes ([cb1fe26](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/cb1fe261ec3c92c4dd445e9b37f5d90f78910100))

## [1.58.1](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.58.0...v1.58.1) (2026-03-04)


### Bug Fixes

* **sdk-settings:** move SDK links editor from SDK settings to system config ([3ea4296](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/3ea429686fbbe7f9f205d806174c3b61f80f46a3))

# [1.58.0](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.57.0...v1.58.0) (2026-03-04)


### Features

* **sdk-settings:** add inline editing for SDK links ([0e07757](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/0e07757fdf968489087b739542b1d28594b3ec9e))

# [1.57.0](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.56.0...v1.57.0) (2026-03-04)


### Features

* add Daily Active Users, soft/hard rate limits to pricing comparison ([c32bc07](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/c32bc07166d1cba8e7f1839136b76ce91c01981a))

# [1.56.0](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.55.0...v1.56.0) (2026-03-03)


### Features

* unify website design with glass cards, nav restructuring, and hero adjustments ([1d129ba](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/1d129ba8579254e2654878dbebe42092528815d5))

# [1.55.0](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.54.3...v1.55.0) (2026-03-02)


### Features

* **quickstart:** add GitHub hero links, PHP info callout, clean up Unity prereqs, and language-aware YouTube embeds ([883b8e2](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/883b8e2414e44e245495f2cabf541408701f84ae))

## [1.54.3](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.54.2...v1.54.3) (2026-03-01)


### Bug Fixes

* **i18n:** add missing quickstart prerequisites/troubleshooting keys and fix simple-server category ([d1bcaaf](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/d1bcaafc078fccaa231538104c433e20d1fb1365))

## [1.54.2](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.54.1...v1.54.2) (2026-02-28)


### Bug Fixes

* **quickstart:** correct simpleServer translation keys for specialCards and faqs ([14e49ac](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/14e49ac3a4e23e64fbbb5ef10baa85209f477800))

## [1.54.1](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.54.0...v1.54.1) (2026-02-28)


### Bug Fixes

* **csp:** allow youtube.com in frame-src for quickstart video embeds ([634c089](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/634c0892321899b011eecd440bae29449a0f4a9b))

# [1.54.0](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.53.1...v1.54.0) (2026-02-28)


### Features

* **quickstart:** add YouTube video tutorials for dashboard, unity, rest-api, and support pages ([8effc3c](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/8effc3ca8c8e1b04edd49d0a78dc7e5b135e9ed5))

## [1.53.1](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.53.0...v1.53.1) (2026-02-28)


### Bug Fixes

* use full-resolution hero image on portrait screens ([6edfa49](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/6edfa49a2de191d2f1d12546183ee64cdd4d4c33))

# [1.53.0](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.52.1...v1.53.0) (2026-02-28)


### Features

* **pricing:** only show available accounts when fewer than 10 remain ([f76b1b6](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/f76b1b68c58ff25cdc4cf55718b2c86c46726276))

## [1.52.1](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.52.0...v1.52.1) (2026-02-27)


### Bug Fixes

* **products:** convert cloudSaveBytes to KB in comparison table ([6159288](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/61592883847fff62412491129b85bab7c6cfd6f8))

# [1.52.0](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.51.8...v1.52.0) (2026-02-27)


### Bug Fixes

* **i18n:** remove per-API-key reference from remote config limit message ([0ce5ed8](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/0ce5ed8c1b0347cd4aa5bb9009ef661d3c516088))
* **test:** add SystemConfigService mock to ProductService tests ([5ac3275](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/5ac3275473bedb47cbbcbd77df61c88f3f4b51a8))


### Features

* **products:** fetch real feature limits from API for comparison table ([341980b](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/341980b6eb188fd83df22e2ee8dd6a391d7c987a))

## [1.51.8](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.51.7...v1.51.8) (2026-02-27)


### Bug Fixes

* remove redundant frontend tracking in favor of server-side events ([c8231c5](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/c8231c5e494dddfe7111c93b4399b14e88f73fbe))

## [1.51.7](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.51.6...v1.51.7) (2026-02-26)


### Bug Fixes

* **ssr:** use route resolvers for blog pages to guarantee SSR content ([e39e508](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/e39e508386c53b2a38009b5d7afbaefdbc373d4d))
* **test:** update news spec for resolver-based data loading ([6bf2118](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/6bf211851bf6c764059bf10d227622d0b9e7a2f3))

## [1.51.6](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.51.5...v1.51.6) (2026-02-26)


### Bug Fixes

* **seo:** allow Googlebot to fetch public API endpoints ([2b7203a](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/2b7203aae01c7ce74844eb2396e250dc133436bc))

## [1.51.5](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.51.4...v1.51.5) (2026-02-26)


### Bug Fixes

* move commit command to parent workspace root ([433886e](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/433886eb4b2724e283da7951c04bc5143a784fc1))
* refactor CLAUDE.md to remove rules now in workspace root ([cc31d67](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/cc31d6791f1d59d3bdda617f8e8386f4a4987bfd))
* **ssr:** resolve relative API_URL for server-side data fetching ([c8ee77d](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/c8ee77d4ed16acb1b49ebb3d071870be59439bb4))

## [1.51.4](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.51.3...v1.51.4) (2026-02-25)


### Bug Fixes

* move bug bounty mascot to left side at -top-32 ([8e6b8d2](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/8e6b8d2b13cfc7c8090485f7e4527237a65c2260))

## [1.51.3](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.51.2...v1.51.3) (2026-02-25)


### Bug Fixes

* remove testimonial section scrollbar and reposition bug bounty mascot ([c57d67f](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/c57d67f3a889c151f808bb60b23ed48a073393bf))

## [1.51.2](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.51.1...v1.51.2) (2026-02-25)


### Bug Fixes

* remove testimonial card height constraint and fix unregistered icon ([5c925d0](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/5c925d0422f36fd78326e85af0b15ecc2cdf7669))

## [1.51.1](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.51.0...v1.51.1) (2026-02-25)


### Bug Fixes

* resolve home page glass styling, missing labels, testimonial height and mascot positioning ([30ecc73](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/30ecc73a2b337d9e5efb61b0a96dc486a60e2670))

# [1.51.0](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.50.0...v1.51.0) (2026-02-25)


### Bug Fixes

* remove billing toggles from comparison sections and prices from feature table ([6dc6213](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/6dc62134d9f3c16837855d5f0ebd5d473e7cbacf))


### Features

* polish home and features page UI/UX ([3671d91](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/3671d91993c8ee2a08d3e11d7149e65aafb647fe))

# [1.50.0](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.49.0...v1.50.0) (2026-02-24)


### Features

* replace hero gradient overlays with frosted glass text containers ([ef9d77b](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/ef9d77bceadd36028a9466326eaec2bfbedfd767))

# [1.49.0](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.48.0...v1.49.0) (2026-02-24)


### Features

* add background hero images and prev/next navigation to feature pages ([e4d252e](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/e4d252eee750c7305be11363061ffd822dbc7fc5))

# [1.48.0](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.47.0...v1.48.0) (2026-02-24)


### Features

* redesign feature detail pages with interactive mockups and quickstart improvements ([13943f7](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/13943f7f491804e4298abb03c07ace0956f411e3))

# [1.47.0](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.46.0...v1.47.0) (2026-02-23)


### Features

* extract shared quickstart-guide component and add reactive route params ([cd7b8a8](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/cd7b8a80e651432cf82e1cb65abc68c3913572ff))
* **frontend:** add version API method to PublicSystemApi ([df150fd](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/df150fd91f91b5dd526c65b740669c512952a054))
* **frontend:** add VersionManager for backend version fetching ([0c06d04](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/0c06d04af029acc66d254b3487ba2d3db34d167d))
* **frontend:** display frontend and backend version in footer ([d91f23c](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/d91f23c2516a8b0053faa2ece142e8cb3c1397bb))

# [1.46.0](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.45.0...v1.46.0) (2026-02-23)


### Features

* add bulk action support with confirmation dialogs to 12 data table features ([79b2ad2](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/79b2ad2dd6f9a39b4eec10a83c3c35221f3675ba))

# [1.45.0](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.44.1...v1.45.0) (2026-02-22)


### Features

* add 9 dedicated SEO feature pages with shared template architecture ([e1e1dd8](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/e1e1dd887f777ebddee55f26fc72aa24cebb5edb))

## [1.44.1](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.44.0...v1.44.1) (2026-02-22)


### Bug Fixes

* improve SDK section grid layout and testimonial card overflow ([b782b66](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/b782b66ba56e125aaea53b2863260515b9541fb3))

# [1.44.0](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.43.3...v1.44.0) (2026-02-22)


### Features

* add open source server section and dynamic API URL routing ([a815235](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/a81523516d039e49feb3fc01a340b5f30136e238))

## [1.43.3](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.43.2...v1.43.3) (2026-02-22)


### Bug Fixes

* display blog post title above hero image ([bbb3827](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/bbb382763207942267a879c0a56e368a51f3242e))

## [1.43.2](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.43.1...v1.43.2) (2026-02-22)


### Bug Fixes

* **i18n:** resolve broken translation key references across multiple features ([9ea845d](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/9ea845d180a58a16e8c137de12604fbab149d5b4))

## [1.43.1](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.43.0...v1.43.1) (2026-02-22)


### Bug Fixes

* use central domain for tracking collect in production ([f7540e4](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/f7540e4e11c260da02a4a970abd3f0f7de45c30b))

# [1.43.0](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.42.0...v1.43.0) (2026-02-22)


### Features

* activate Unreal Engine quickstart tab with SDK documentation ([f0fcf81](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/f0fcf8147643fd4985671580640e87a6015587d0))
* add crash reporting integration, cloud save enhancements, and UI improvements ([25827de](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/25827de6ddd4f7270016603ed005c409938a08a0))
* add public /resources page with SSR and i18n ([969a8d4](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/969a8d4c67a569f0222c96873a1b94d0aff9c1f0))
* mark Unreal Engine SDK as available and link SDKs to quickstart guide ([619010d](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/619010d3d7d73754ecc136199b965aa51ad092d4))

# [1.42.0](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.41.0...v1.42.0) (2026-02-22)


### Features

* add crash reporting integration, cloud save enhancements, and UI improvements ([#5](https://github.com/ProjectMakersDE/horizOn-Dashboard/issues/5)) ([4ef077a](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/4ef077affc00fe78ca300d37bbe69bd30ee7ff7a))

# [1.41.0](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.40.0...v1.41.0) (2026-02-21)


### Features

* add unified data table component and migrate all features ([#4](https://github.com/ProjectMakersDE/horizOn-Dashboard/issues/4)) ([68708b9](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/68708b9fa413af8f7183c7421c2fac4428b63fa7))

# [1.40.0](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.39.0...v1.40.0) (2026-02-21)


### Features

* **crash:** add i18n translations for all supported languages ([1d1b2fa](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/1d1b2faff1094fcc43a73a68bf4d7ba5ab521571))

# [1.39.0](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.38.2...v1.39.0) (2026-02-21)


### Features

* **crash:** add crash reporting page components and state service ([28a9ded](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/28a9dedaacaa616cd6226797d5b63c4c44335689))
* **crash:** add frontend models, API service, and feature config ([bd11a0c](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/bd11a0c600d1400404f39ecb43aee61d29eb4926))
* **crash:** add i18n translations for crash reporting ([93e4362](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/93e4362fea2e48533478ecd384034d38848ba465))

## [1.38.2](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.38.1...v1.38.2) (2026-02-21)


### Bug Fixes

* **blog:** use relative paths for blog images to avoid mixed content and CSP violations ([ecd4b7e](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/ecd4b7e35fd0fd0c3bba1c666d7e29df0e7257de))

## [1.38.1](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.38.0...v1.38.1) (2026-02-21)


### Bug Fixes

* **a11y:** use blog title as alt attribute for image preview in admin modal ([41e655f](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/41e655f8790dcef01ddf2d187c47d8d1f7851edc))

# [1.38.0](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.37.7...v1.38.0) (2026-02-21)


### Features

* **ssr:** enable SSR with real API data for public pages ([1ee0a27](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/1ee0a274251647d2533c958731afeeba128f1861))

## [1.37.7](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.37.6...v1.37.7) (2026-02-21)


### Bug Fixes

* **ui:** improve tour modal visibility in dark mode with secondary border and glow ([086d344](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/086d344650720ce0f315f7610f3226abcb982063))

## [1.37.6](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.37.5...v1.37.6) (2026-02-21)


### Bug Fixes

* **ui:** redesign modal with theme-aware styling and tighter spacing ([5b77dd5](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/5b77dd592fb1a8d16252ab890ead9323128d0ca3))

## [1.37.5](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.37.4...v1.37.5) (2026-02-21)


### Bug Fixes

* **ticket-system:** use updatedAt as fallback when lastMessageDate is null ([5de2d86](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/5de2d866b072aa68c5bf2669112c3a923783a181))

## [1.37.4](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.37.3...v1.37.4) (2026-02-21)


### Bug Fixes

* **ui:** redesign checkboxes with global styles for consistency and visibility ([0db9953](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/0db99538c8198de0baa882cb96e58e3a8ab9bd46))

## [1.37.3](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.37.2...v1.37.3) (2026-02-20)


### Bug Fixes

* **onboarding:** persist tour state on dismiss and resume on navigation ([893a76c](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/893a76cb5745bea6fa60b1f2c8843bffe2f54ee7))

## [1.37.2](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.37.1...v1.37.2) (2026-02-20)


### Bug Fixes

* **onboarding:** resolve tour dialog styling and interactivity issues ([38707d8](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/38707d8d9346b65618a4d87cbd88bc8f95a207c7))

## [1.37.1](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.37.0...v1.37.1) (2026-02-20)


### Bug Fixes

* **onboarding:** use default export from shepherd.js dynamic import ([a3ab1d8](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/a3ab1d8aef8189f3aac457b9ccd46d7ed898545a))

# [1.37.0](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.36.2...v1.37.0) (2026-02-20)


### Bug Fixes

* **i18n:** escape Chinese quotation marks in zh.toml onboarding section ([ac1fde0](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/ac1fde08c38df7806da432ff3bc43fa44c7c4e37))
* **ui:** add max-height and scroll overflow to all modal containers ([25d4d54](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/25d4d54a07cfb14972c766c3491228a987860078))


### Features

* **onboarding:** add data-onboarding attributes to target elements ([5d76491](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/5d7649160575639498e388e0594fc83ef7b18034))
* **onboarding:** add declarative tour steps config ([0b70cc3](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/0b70cc3b2ce7a3d15b900fbf651e7076afa936ed))
* **onboarding:** add horizOn theme CSS for Shepherd.js tour ([b403c8b](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/b403c8bd9e09823b496ce68f9f767591c101fe36))
* **onboarding:** add restart tour button to account settings ([6051c48](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/6051c4870f635b9b7aacec488b52c66d7712fa9e))
* **onboarding:** add storage keys and English i18n translations ([002e5fa](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/002e5fafba9f8f60db0f00eebd9cd0e1891f9fe4))
* **onboarding:** add tour translations for all 14 languages ([47f48f9](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/47f48f906859e8c028236be2f78cf6b4d991cc78))
* **onboarding:** create welcome modal component ([63579aa](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/63579aa95dedf63cad46663498744e3e1f2c96ce))
* **onboarding:** implement OnboardingTourService with lazy Shepherd.js loading ([0ad8979](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/0ad897907fb3881210da6756fa402771e6233250))
* **onboarding:** integrate tour service and welcome modal into dashboard ([1e5d9bd](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/1e5d9bdb4e31a94ddbd57242a2b8a658dd42ad75))
* **onboarding:** register onboarding-tour feature module ([86401af](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/86401af8a2d38e9724621dc3d4202e12f11266d6))

## [1.36.2](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.36.1...v1.36.2) (2026-02-20)


### Bug Fixes

* **i18n:** add missing modal.removeFoldout translation key to all languages ([d108b40](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/d108b40a841bd7b6ef70f2d765ae5f652d8f2111))

## [1.36.1](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.36.0...v1.36.1) (2026-02-20)


### Bug Fixes

* **modal:** replace hardcoded aria-label with translated foldout remove label ([c82da70](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/c82da709656797e1f5a8ce3d1edacc95f9ad59e9))

# [1.36.0](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.35.0...v1.36.0) (2026-02-20)


### Bug Fixes

* add missing register form i18n keys and hide accountId from user logs ([cd1525e](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/cd1525e1ffed034e0aa425e3efbc00e132d2479c))
* default-hide closed tickets in admin view and add multi-lang design doc ([200ea97](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/200ea97524b63c520bd4e4aeb025bc8e7721f2c5))
* **modal:** make modal scrollable when content exceeds viewport height ([5bc0036](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/5bc0036dd82c18a1f36845b5adfe304d3ba0b99d))
* **tickets:** add missing fields to TicketListResponse DTO and fix createdAt mapping ([8860871](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/88608713ac3350b683ef36f1b844e141f8416a51))


### Features

* add Ahrefs Web Analytics and clean up CSP after server-side tracking migration ([b5c752b](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/b5c752b39a7ee2377a208d8330677e93240c5d5a))
* add multi-language field utility and refactor content management modals ([2906e51](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/2906e516cfc6fe19b394e61c58fe464ab3dfaa06))

# [1.35.0](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.34.3...v1.35.0) (2026-02-19)


### Bug Fixes

* consolidate regional subdomain URLs to single horizon.pm domain ([427356b](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/427356b4ca6d523981205f3319cbfb9bbd80f169))


### Features

* replace client-side tracking with server-side TrackingCollectService ([538597f](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/538597f5b80b93ae481ffbc9e73ce8a5e043d6c5))

## [1.34.3](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.34.2...v1.34.3) (2026-02-19)


### Bug Fixes

* add regional subdomains to CSP img-src for blog images ([3b90f66](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/3b90f66777bc08e3cec917dd69b491fbe774419d))

## [1.34.2](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.34.1...v1.34.2) (2026-02-19)


### Bug Fixes

* **seo:** consolidate domain to horizon.pm and remove /home route ([#3](https://github.com/ProjectMakersDE/horizOn-Dashboard/issues/3)) ([24e0ef2](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/24e0ef29e3c279c6d7ee072c04c657d7954fb85a))

## [1.34.1](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.34.0...v1.34.1) (2026-02-17)


### Bug Fixes

* enable lazy background image loading on About Us page ([d5dd9c7](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/d5dd9c7d76edabf1a6f5563c881874358eacc8fe))

# [1.34.0](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.33.0...v1.34.0) (2026-02-17)


### Bug Fixes

* add missing analytics replay and cookie service wiring ([69d0c6b](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/69d0c6b6b78d2fd1a6a36a9dd5052e8673b71e1a))
* make Mori seagull images visible and inline on About Us page ([bdec386](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/bdec3868ae37b720dc51a68549525c840e7a5c0e))


### Features

* add cookie consent translations for pt, nl, pl, ru, zh, ja, ar, ko, tr, id ([2d79888](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/2d79888b34b2b93f28bfd39a4cad6a264f723307))
* add Google Consent Mode v2 default (all denied) before scripts load ([4c71254](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/4c71254f785262c0f220b7bee4140d9325e849ef))
* add Microsoft Advertising to cookie consent analytics services ([e1a2169](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/e1a21693bb00387f305a15e57d26282c4efd2c83))
* enhance About Us page with visual design and Mori seagulls ([9a1ced7](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/9a1ced737ff1c9215f1da8693cd48f65d8087dab))
* fire gtag consent update on cookie consent change ([f8f4041](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/f8f4041d416b442306f05c0afdc11de642c61b4a))

# [1.33.0](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.32.0...v1.33.0) (2026-02-17)


### Features

* add About Us page with indie dev story and live stats ([e414f81](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/e414f81af88c87d832ecea83c148f2ff36c08daf))

# [1.32.0](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.31.0...v1.32.0) (2026-02-17)


### Features

* **i18n:** SSR language detection from Accept-Language header ([0cbada4](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/0cbada4ddc1d28461f8facea8a6ede562f7c63f0))

# [1.31.0](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.30.1...v1.31.0) (2026-02-17)


### Features

* **seo:** canonicalize all regions to us.horizon.pm ([81c5413](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/81c5413db016c67ebdc9083faefd2cf4d837bc03))

## [1.30.1](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.30.0...v1.30.1) (2026-02-17)


### Bug Fixes

* add SEO page titles and meta descriptions to examples, quickstart, and blog pages ([d49b5a3](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/d49b5a36ecaa846ca63d12024e24ad7328502a98))

# [1.30.0](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.29.2...v1.30.0) (2026-02-16)


### Features

* add Meta Pixel conversion events for signup, purchase, and checkout ([0c00fbd](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/0c00fbd523246343783ea2206031856c44ba2641))

## [1.29.2](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.29.1...v1.29.2) (2026-02-16)


### Bug Fixes

* add Facebook domains to CSP for Meta Pixel tracking ([069224c](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/069224c266905f37317d922a56dbaffa07662e48))

## [1.29.1](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.29.0...v1.29.1) (2026-02-16)


### Bug Fixes

* set default Meta Pixel ID so pixel loads without env var override ([d7f694c](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/d7f694ca76638d8c77a4a6cd8bd5a8c56ec23f6f))

# [1.29.0](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.28.0...v1.29.0) (2026-02-16)


### Features

* add Meta Pixel (Facebook) tracking with cookie consent integration ([204cb06](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/204cb0696b53055ba083a78fa16f266332b14de7))

# [1.28.0](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.27.1...v1.28.0) (2026-02-15)


### Features

* add markdown rendering for blog detail page ([da035fe](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/da035fee81f61599712fba045107c2714bd86559))

## [1.27.1](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.27.0...v1.27.1) (2026-02-15)


### Bug Fixes

* auto-append /chat/completions to custom OpenAI base URLs ([923a064](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/923a06448fe3163038e8afa90b98cdb6a6b8e276))

# [1.27.0](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.26.5...v1.27.0) (2026-02-15)


### Features

* add optional base URL field for OpenAI and Gemini providers ([4866723](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/486672344626cc3ed39623dd78425a391415430f))

## [1.26.5](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.26.4...v1.26.5) (2026-02-15)


### Bug Fixes

* add blob: to CSP img-src for blog image preview ([32696f7](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/32696f7841518ee7bb67c9eb38aad0395d9293cc))

## [1.26.4](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.26.3...v1.26.4) (2026-02-15)


### Bug Fixes

* load blog image in modal when imageUrl is present ([4c616e9](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/4c616e9dacd43ddca2a09626542ce1db8da542ff))

## [1.26.3](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.26.2...v1.26.3) (2026-02-15)


### Bug Fixes

* resolve blog image visibility, missing translations, footer year, and deletion UX ([ed03c0d](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/ed03c0df9ce16d25d3c3e4e663144c088e034077))

## [1.26.2](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.26.1...v1.26.2) (2026-02-15)


### Bug Fixes

* allow LM Studio connections by relaxing CSP connect-src directive ([7d1e7b8](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/7d1e7b8713d3cffd2e5092039888de0e65a7e326))

## [1.26.1](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.26.0...v1.26.1) (2026-02-15)


### Bug Fixes

* attach auth token for ticket creation and expose blog hasImage field ([1e9e99a](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/1e9e99abca872b5a9192110dc8f67f11de2608a5))

# [1.26.0](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.25.0...v1.26.0) (2026-02-15)


### Bug Fixes

* **blog:** update news spec tests for card grid and Load More redesign ([ab8dad1](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/ab8dad1e16e33053cd2436e3e317176eab7a43d8))


### Features

* add blog redesign implementation plan ([c43e0a0](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/c43e0a0d0679ccdca73ab7b346be00aa4b36de2f))
* **blog:** create NewsDetail component with SEO meta tags and adjacent navigation ([e93c992](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/e93c992b14deb88a6b27c395200269b10b86ae04))
* **blog:** redesign blog list with card grid and Load More button ([4297f8d](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/4297f8da0a4789761e1b8b9da0dfcd44537869b5))
* **blog:** translate blog i18n keys for all languages and add productionUrl ([bc50fb2](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/bc50fb26a954d099d2e82ac07b85150dc6c22b3d))
* **blog:** update data layer for blog redesign ([c5e0163](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/c5e0163f5f9b67179e853bf03a1afe87d08d3b5b))
* **blog:** update English i18n keys for blog redesign ([950c8b3](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/950c8b375ad76401619f751f7a740314e65bdc12))
* finalize blog redesign design document ([d098c96](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/d098c96a3500a280c6e86264ad4af83307c6ff41))

# [1.25.0](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.24.1...v1.25.0) (2026-02-14)


### Features

* **blog:** add blog image upload UI with drag-and-drop support ([6494339](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/64943395dc4ed101dab2e96945d1cbebdf0ccab1))

## [1.24.1](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.24.0...v1.24.1) (2026-02-13)


### Bug Fixes

* improve Trust Bar alignment, light mode overlays, and sidebar button order ([ff594e8](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/ff594e890b0f5244ea02f6afed178699f9b21030))

# [1.24.0](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.23.3...v1.24.0) (2026-02-13)


### Features

* add changelog link to Trust Bar and dashboard sidebar ([8c825eb](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/8c825eb337009c9c2ae5d6cceac3de81321fc5cc))

## [1.23.3](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.23.2...v1.23.3) (2026-02-13)


### Bug Fixes

* use wildcard CSP for Clarity subdomains to fix v.clarity.ms block ([c99abf0](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/c99abf004dd0c781a1c356816cf0bc90570f431a))

## [1.23.2](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.23.1...v1.23.2) (2026-02-13)


### Bug Fixes

* add missing Bing UET and Clarity script domains to CSP ([b3b11c5](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/b3b11c566e70b3d9ebc22a5318adf968e49fdebe))

## [1.23.1](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.23.0...v1.23.1) (2026-02-13)


### Bug Fixes

* add missing GTM and Microsoft Clarity domains to CSP ([933de2f](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/933de2f0b78b37e8afb69ee82984c1a98867edb5))

# [1.23.0](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.22.17...v1.23.0) (2026-02-13)


### Features

* add GitHub SDK links to engine cards and allow Bing UET in CSP ([735c4ed](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/735c4edb123313a92019691b5b3894d753b57f1c))

## [1.22.17](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.22.16...v1.22.17) (2026-02-12)


### Bug Fixes

* add stats.g.doubleclick.net to CSP connect-src directive ([504dc91](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/504dc910ece20df23ea63d6322520c49acbcd027))

## [1.22.16](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.22.15...v1.22.16) (2026-02-11)


### Bug Fixes

* resolve lazy loading and scroll-to-pricing failures on deferred content ([53e1c4f](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/53e1c4f2a3faae599d522d457fa1ea7d566a8c39))

## [1.22.15](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.22.14...v1.22.15) (2026-02-11)


### Performance Improvements

* optimize CLS, reduce DOM size, and add admin accounts caching ([ffb4a54](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/ffb4a54e3fed3d19bdeee5fcde36bf4fe0e0bd3b))

## [1.22.14](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.22.13...v1.22.14) (2026-02-11)


### Bug Fixes

* suppress console errors from blocked third-party script loads ([c85a59d](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/c85a59d1fc859c38131b37102ad1e2a5d2bbf632))

## [1.22.13](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.22.12...v1.22.13) (2026-02-11)


### Performance Improvements

* add preconnect hints and optimize hero background image ([2378937](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/237893775b6b0749b0a5e5a8d83e4a43adf46c27))

## [1.22.12](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.22.11...v1.22.12) (2026-02-11)


### Bug Fixes

* add PWA icons and update manifest for installability compliance ([d1615fa](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/d1615fa367874383376afa7a2efae06c582e7563))

## [1.22.11](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.22.10...v1.22.11) (2026-02-11)


### Bug Fixes

* add missing Google Ads/GTM/GA4 domains to CSP for full tracking support ([989be33](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/989be338970a8b284ca5d36981c29f8033934881))

## [1.22.10](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.22.9...v1.22.10) (2026-02-11)


### Performance Improvements

* optimize page load performance based on Catchpoint report ([825eefa](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/825eefae8c6e57e00c3344314040c3678c9f7bb1))

## [1.22.9](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.22.8...v1.22.9) (2026-02-10)


### Bug Fixes

* add Google Ads audience pixel domain to CSP img-src ([63bb992](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/63bb992a925adcad75094dc6d9c98a60883e8f2b))

## [1.22.8](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.22.7...v1.22.8) (2026-02-10)


### Bug Fixes

* add Google Ads conversion domains to CSP connect-src ([804bd12](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/804bd1201685c88ee6072acb3ba4c55d42bc72a1))

## [1.22.7](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.22.6...v1.22.7) (2026-02-10)


### Bug Fixes

* send auth token with check-auth and guard against null response ([8da0fde](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/8da0fdefe53faa2b8f03427b345d2d99f2d4bdc2))

## [1.22.6](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.22.5...v1.22.6) (2026-02-10)


### Bug Fixes

* skip auth guards during SSR to prevent logout on page reload ([e1a0957](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/e1a0957ca00c8416dab87b2c64af46555a0f121d))

## [1.22.5](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.22.4...v1.22.5) (2026-02-10)


### Bug Fixes

* add missing Google Analytics and Ads domains to CSP connect-src ([1cfae44](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/1cfae44907d521748bfd55ec39c4a79e5fd0af2c))

## [1.22.4](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.22.3...v1.22.4) (2026-02-10)


### Bug Fixes

* add accounts.google.com to CSP script-src for Google Sign-In ([9713db3](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/9713db3757b1907e2f8271d685ecd9913b61324d))

## [1.22.3](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.22.2...v1.22.3) (2026-02-09)


### Performance Improvements

* add compression, CSP headers, web manifest, and fix accessibility contrast ([e9b7e1c](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/e9b7e1c84c0a374e9b612ebd256f35bceb51f0e1))

## [1.22.2](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.22.1...v1.22.2) (2026-02-09)


### Bug Fixes

* resolve mobile nav hydration mismatch causing layout flash ([ff39f01](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/ff39f01d87e8c0ca53650d73118a852ae15ffe63))

## [1.22.1](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.22.0...v1.22.1) (2026-02-09)


### Performance Improvements

* fix SSR hydration and eliminate duplicate HTTP requests on page load ([4e3cf0a](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/4e3cf0a2eee1361ce99c5bd031793659ed2f2408))

# [1.22.0](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.21.0...v1.22.0) (2026-02-09)


### Features

* **i18n:** translate admin-banner feature into all 13 languages ([aa64f14](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/aa64f1440294a97660ac3a7d342d00d6b9c0a8f0))

# [1.21.0](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.20.0...v1.21.0) (2026-02-09)


### Features

* **i18n:** add complete translation coverage for all 15 languages and build-time validation ([b50a4ba](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/b50a4baf46b047a6a097712e4850392d71cf7872))

# [1.20.0](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.19.1...v1.20.0) (2026-02-09)


### Features

* **i18n:** add quickstart and news translations for 13 languages and fix blog reactivity ([83c2005](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/83c20058396b56e93b265c1b6516e75f5683c60a))

## [1.19.1](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.19.0...v1.19.1) (2026-02-09)


### Bug Fixes

* prevent undefined params from being sent as literal strings in admin accounts API ([8ba009c](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/8ba009cfa9c2592338d5544e87c2dca394939946))

# [1.19.0](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.18.2...v1.19.0) (2026-02-09)


### Bug Fixes

* revert manual version bump and fix commit workflow for semantic-release ([c2f8639](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/c2f8639d9686d36decd2772683b3e559a5294345))


### Features

* **i18n:** add version-based cache-busting to translation file loading ([fbe0937](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/fbe093751934acff8c0e727403d57524586c0937))

## [1.18.2](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.18.1...v1.18.2) (2026-02-08)


### Bug Fixes

* correct testimonial API path, add gift code display, and fix news i18n key scoping ([f6a19c4](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/f6a19c4c574f46603db14a6887818481548a4a5e))

## [1.18.1](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.18.0...v1.18.1) (2026-02-08)


### Bug Fixes

* **dev-mode:** hide dev mode panel in production builds ([273efb1](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/273efb1021d529aa516f19ce422f8fe293d878c1))

# [1.18.0](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.17.1...v1.18.0) (2026-02-08)


### Features

* **testimonial:** add customer testimonial submission and admin review workflow ([29302cc](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/29302cc9b9583ebd0c6e47d808a00f43fe501b31))

# [1.16.0](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.15.0...v1.16.0) (2026-02-08)


### Bug Fixes

* **i18n:** remove duplicate home.hero and home.solution keys from public translation files ([0cac611](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/0cac611e83aae73a18ee4f9c31ca226ecf744884))


### Features

* add dev-mode, blog management, examples page mockups, and mobile responsiveness ([3d3a390](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/3d3a390b63f0e4b27f5ac2af76983a1c414d6cee))
* add rate limiting and help sections to Godot and REST API quickstart guides ([09b6420](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/09b6420bc6488bace306834ffb3942ddd06770e5))
* **dev-mode:** add mock endpoints for customer testimonial submission and review ([e8b03f4](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/e8b03f40977a0594be9beccc47ca39f07927dd8e))
* **i18n:** add testimonial submission and review translations for all languages ([e2b91f5](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/e2b91f56dc5ea4da62b77532eeae3e777bd7e09d))
* **i18n:** update sidebar translation keys for all languages ([f4ea022](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/f4ea022c6239283fcffc3278aee619f6dc5a7504))
* **mobile:** add Capacitor native platform support for Android and iOS ([9880e5d](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/9880e5dba419ffa5e3a95bf5a7a4b5f0d4f3571a))
* **system-config:** add testimonial reward category with i18n for all languages ([969e99d](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/969e99dc599fc6a015f87218d91e494fa518c1fa))
* **testimonial:** add admin review workflow with approve/reject actions ([a67b1f8](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/a67b1f8f06fa54a7170c10928b31149664347bde))
* **testimonial:** add customer testimonial submission page ([6ce8908](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/6ce89085e83d818552ef1b8006370982f3960fdf))
* **testimonial:** trigger release for customer submission and review workflow ([94c0aae](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/94c0aae2d3543fc211da2b2a5189fb635d1931cb))

# [1.15.0](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.14.0...v1.15.0) (2026-02-04)


### Bug Fixes

* enforce release-triggering commits and update SEO service tests for hreflang support ([937d75e](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/937d75efbb98918a34e9afb833b84a9990f7408c))
* generate fallback transaction_id for Google Ads conversion tracking ([a712878](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/a712878aa8a0bfe7d792f5c45fec14105136657e))


### Features

* add GA4/GTM analytics tracking and migrate SEO domain to us.horizon.pm ([f12bfab](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/f12bfabb93622ff34bcd422c66266d1c93eb48d7))

# [1.14.0](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.13.1...v1.14.0) (2026-02-01)


### Features

* add Google Ads conversion tracking to purchase success page ([cd612c6](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/cd612c6069ad6c7a0d05e669578426de62bcc989))
* add purchase success page for Stripe payment confirmation ([554dc63](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/554dc63ec4dd4095f4fa1aa84639342b77b95533))

## [1.13.1](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.13.0...v1.13.1) (2026-02-01)


### Bug Fixes

* use npm ci instead of artifact transfer for node_modules ([3aaac2e](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/3aaac2e4784754d56b9585052b6f8ad3f3e2712a))

# [1.13.0](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.12.4...v1.13.0) (2026-02-01)


### Features

* add Google Ads conversion tracking for registration ([bbbc355](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/bbbc355b3fcc9234b12d13d0fc6a5f741d9ea27f))

## [1.12.4](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.12.3...v1.12.4) (2026-02-01)


### Bug Fixes

* add SSR caching for home route to improve TTFB ([ce1e3ea](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/ce1e3eaba94a9883e310aed74077a7ebfabb3c32))

## [1.12.3](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.12.2...v1.12.3) (2026-01-31)


### Bug Fixes

* improve LCP with responsive hero image and optimized assets ([e81dc04](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/e81dc0464b7753230cd78d5e6496ab4781330c48))

## [1.12.2](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.12.1...v1.12.2) (2026-01-31)


### Performance Improvements

* restore parallel initialization for faster FCP/LCP ([7df231b](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/7df231bb70050afc1b6d060fcaff613425bf2024))

## [1.12.1](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.12.0...v1.12.1) (2026-01-31)


### Bug Fixes

* update initialization manager tests for phased execution ([651e5cf](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/651e5cf35994644f5271c40df2cd4bc097d26d66))


### Performance Improvements

* optimize PageSpeed with FOUC prevention and lazy image loading ([d96716e](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/d96716e829403cb3cb834e1de4038d4f1c271db2))

# [1.12.0](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.11.1...v1.12.0) (2026-01-31)


### Features

* add comprehensive SEO service with structured data and meta tag management ([5f7148f](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/5f7148fb15722616a0a9b2d3ac8c63eff1f112c7))

## [1.11.1](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.11.0...v1.11.1) (2026-01-30)


### Performance Improvements

* optimize bundle size and initial load performance ([3991d07](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/3991d07d407de33c499733d22e6053d8c2c697fd))

# [1.11.0](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.10.0...v1.11.0) (2026-01-28)


### Features

* add gclid tracking for Google Ads attribution ([bed2813](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/bed2813c0e1fef1a9c121d775fd4196bc8dcb800))
* add gclid tracking for Google Ads attribution ([97de189](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/97de1899ea3892a98e56716fd40635a5e744d8a0))

# [1.10.0](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.9.2...v1.10.0) (2026-01-28)


### Features

* add Google Tag Manager with cookie consent gate ([22e11b8](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/22e11b89230d1ce89d9be03afc6496ef7872db46))

## [1.9.2](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.9.1...v1.9.2) (2026-01-26)


### Bug Fixes

* switch SSR server to CommonEngine for better compatibility ([105c5cc](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/105c5cc89c2c0b8453918f6f64c9617220177ccf))

## [1.9.1](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.9.0...v1.9.1) (2026-01-26)


### Bug Fixes

* lazy-initialize Angular SSR engine to avoid manifest timing issues ([5cb1a05](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/5cb1a05a1dc4242998c24b0600f1da1f845d6333))

# [1.9.0](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.8.2...v1.9.0) (2026-01-26)


### Features

* add Express SSR server for production Docker deployment ([5bd28ab](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/5bd28abd3a237e41486173aa91d854ba74193dc7))

## [1.8.2](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.8.1...v1.8.2) (2026-01-26)


### Bug Fixes

* add SSR compatibility guards for browser-only APIs ([495b8be](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/495b8be64c14ad6fb2ff56c47f48c617030f8227))

## [1.8.1](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.8.0...v1.8.1) (2025-12-18)


### Bug Fixes

* add dynamic canonical URL and hreflang tags for regional SEO ([f442ebb](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/f442ebbebeea20131f0d265e459af623f6698df2))

# [1.8.0](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.7.0...v1.8.0) (2025-12-14)


### Features

* auto-refresh auth after subscription changes ([12f6da9](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/12f6da966aa63cae37014fa59cfc5b440f85f539))
* mark Godot SDK as available and improve price cards readability ([3c40a9e](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/3c40a9e33714b5c90faa009865728a1211146ded))

# [1.7.0](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.6.0...v1.7.0) (2025-12-09)


### Features

* expand FREE tier access and add marketing documentation ([e3dbad5](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/e3dbad563ef8c7221945e7ff32d5e64325caf339))

# [1.6.0](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.5.1...v1.6.0) (2025-12-07)


### Features

* add Unity SDK quickstart guide with step-by-step tutorial ([dac6ddb](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/dac6ddb364ea59d64335f5940a0b095aebbe326b))

## [1.5.1](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.5.0...v1.5.1) (2025-12-07)


### Performance Improvements

* optimize PageSpeed Insights performance and accessibility ([a60ae85](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/a60ae85a07e19a4784cdbd94128f6184e8f4c3b2))

# [1.5.0](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.4.0...v1.5.0) (2025-12-07)


### Features

* add email verification page and enhance user feedback with category/device info ([f89d426](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/f89d426dccdf8fa2d2f2920f3d27eba726c9e263))

# [1.4.0](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.3.0...v1.4.0) (2025-12-05)


### Features

* add docs link to sidebar and enhance home page translations ([d986009](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/d986009d4876c77395cc0aede2048da4cf019271))

# [1.3.0](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.2.0...v1.3.0) (2025-12-04)


### Features

* update signInWithGoogle method to include redirect URI ([ce5b8e6](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/ce5b8e66c8d44100a277d2ba902766bdcd9b67c8))

# [1.2.0](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.1.0...v1.2.0) (2025-12-04)


### Features

* update routing and canonical URLs to reflect new domain structure ([9529c8c](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/9529c8cef3f338bfb06a32b0eadfdc739c6cd624))

# [1.1.0](https://github.com/ProjectMakersDE/horizOn-Dashboard/compare/v1.0.0...v1.1.0) (2025-12-04)


### Bug Fixes

* enhance logging functionality and improve test coverage ([1790a1a](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/1790a1a0ca4fab4d7668153cef7be0900ca5c10a))
* revert home page ([e029b63](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/e029b63c55d25c630f504c45159d7ee23afbe3bc))
* update support titles and descriptions across multiple languages ([ff606a4](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/ff606a4ef23fcdb474ff2fc664741e8e29a07c03))


### Features

* add complete data export request functionality and update localization strings ([d274e69](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/d274e69b7c01f9b8beec3470c316f557b3819f7d))
* add section dividers to enhance layout and visual separation ([402e099](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/402e099e83539d9723c96c44f96912bff8ac5d4d))
* implement pixel wave section divider and update SVG assets ([90f7503](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/90f7503ea6a85e53722ee679a43a1928feaf64e8))

# 1.0.0 (2025-12-04)


### Features

* add testimonial management feature with dynamic home page integration ([7f14b92](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/7f14b927aee9a46d69a57cec4f81ea440b382ae0))
* redesign home page with new marketing sections and expanded content ([a63531b](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/a63531bd142adf9bcd44527301eb77b34ecbf343))


### Performance Improvements

* convert images to WebP format and add lazy loading ([d8ff6ee](https://github.com/ProjectMakersDE/horizOn-Dashboard/commit/d8ff6ee993dfc8a802a1e2ed8facc1d28ad27b22))
