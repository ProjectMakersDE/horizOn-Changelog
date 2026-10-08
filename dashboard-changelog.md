---
layout: default
title: Dashboard Changelog
---

# Dashboard Changelog

All notable changes to the horizOn Dashboard (Frontend).

[Back to Overview](.)

## 1.105.1 (2026-10-05)


### Bug Fixes

* **quickstart:** publish approved bilingual tutorial catalog

# 1.105.0 (2026-10-02)


### Features

* **status:** add public status page at /status
* **validated-actions:** sus packages review, package export and sus quota

# 1.104.0 (2026-10-01)


### Bug Fixes

* **dashboard:** align admin fixtures and overflow actions
* **dashboard:** align admin layouts and preserve overflow actions
* **dashboard:** align responsive shell and dialog behavior
* **dashboard:** cancel obsolete player queries and scope reset to local filters
* **dashboard:** clarify crash and settings states
* **dashboard:** complete dev account-key fixtures and safe admin SSR
* **dashboard:** complete feature page-grid audit for
* **dashboard:** connect menu favorites and preserve sticky shell scrolling
* **dashboard:** identify ticket management page correctly
* **dashboard:** keep leaderboard preview functional and move rules guidance aside
* **dashboard:** keep player email addresses readable
* **dashboard:** keep table filters compact and stable
* **dashboard:** load leaderboard detail by ID for direct links
* **dashboard:** localize relative crash timestamps
* **dashboard:** map backend config category names to labels
* **dashboard:** offer the active leaderboard detail page size
* **dashboard:** refer to project selector in validated actions
* **dashboard:** restore ticket deep links and mobile guidance
* **dashboard:** restore ticket detail readability
* **dashboard:** show favorites in the Dashboard navigation panel
* **dashboard:** show isolated measured chart days
* **dashboard:** show unavailable cloud save count and valid page sizes
* **dashboard:** stabilize navigation and project context
* **dashboard:** translate profile catalog and correct key selector hint
* **dashboard:** use valid ticket sender roles in dev fixtures
* **feature-layout:** size stat card columns by row width so labels never collide with icons
* **i18n:** define common.copyFailed in all languages
* **i18n:** key translation cache by content revision
* **icons:** bundle dashboard navigation glyphs offline
* **pricing:** rename Validated Runs to Validated Actions in all languages and add home teaser chips
* **quickstart:** render inline code in rate limiting do and don't items
* **sidebar:** left align navigation labels so long names wrap cleanly
* **theme:** toggle effective system palette on first click
* **validated-actions:** align inline icons and keep stat labels clear of card icons
* **validated-actions:** expect translated reason keys in rules spec
* **validated-actions:** scope evidence record calls to their API key


### Features

* **api-explorer:** add a Validated Actions endpoint group with player session support
* **api-explorer:** offer the player session on every endpoint that requires it
* **dashboard:** add account-scoped favorites and player table columns
* **dashboard:** add project workspace shell and home overview
* **dashboard:** add Validated Actions feature page art and bento tile
* **dashboard:** align remaining feature pages with page grid
* **dashboard:** redesign priority feature pages for
* **dev-mode:** mock Validated Actions admin endpoints and list the feature in llms.txt
* **features:** show the Validated Actions video card and deep link the quickstart CTA
* **leaderboard:** show the score limit per API key
* **player-profile:** manage cosmetics catalog, unlocks and gift code grants
* **quickstart:** deep link Validated Actions cards, add REST card and planned tutorial video
* **quickstart:** guide engine setup and feature adoption with inline videos
* **quickstart:** redesign /quickstart as docs, course and cheat sheet
* **quickstart:** redesign the start steps
* **validated-actions:** add feature page, home tile and pitch in 15 languages
* **validated-actions:** add quickstart steps and concept box for Unity, Godot and Unreal
* **validated-actions:** add rules editor, runs list and validated-only leaderboards
* **validated-actions:** edit server-owned values and correct player state
* **validated-actions:** evidence review, evidence slots and leaderboard moderation

## 1.103.4 (2026-09-05)


### Bug Fixes

* restore inline styles under the content security policy

## 1.103.3 (2026-09-05)


### Bug Fixes

* **api-keys:** route account mutations session only
* **blog:** harden renderer and content security policy
* **release:** promote account-key and blog security fixes

## 1.103.2 (2026-08-20)


### Bug Fixes

* **users:** scope statistics and stabilize pagination

## 1.103.1 (2026-08-13)


Maintenance release without user-facing changes.

# 1.103.0 (2026-08-13)


### Bug Fixes

* run dashboard CI on local runners


### Features

* **news:** add scheduled publication time

## 1.102.4 (2026-08-08)


### Bug Fixes

* **api-keys:** forward never-expire account key choice

## 1.102.3 (2026-07-31)


### Bug Fixes

* **blog:** disclose AI-generated images

## 1.102.2 (2026-07-25)


### Bug Fixes

* **analytics:** make behavior insights actionable
* **analytics:** satisfy accessibility gate

## 1.102.1 (2026-07-25)


### Bug Fixes

* **analytics:** rebuild behavior insights

# 1.102.0 (2026-07-24)


### Features

* **blog:** render hero images at 3:2

# 1.101.0 (2026-07-10)


### Features

* **quickstart:** video cards show real titles, tighter summaries and a lightbox player

## 1.100.2 (2026-07-08)


### Bug Fixes

* **api-keys:** do not call the admin api-keys endpoint when logged out

## 1.100.1 (2026-07-08)


### Bug Fixes

* **quickstart:** repair dead reference links and rework goal navigation

# 1.100.0 (2026-07-08)


### Bug Fixes

* **i18n:** allow Seagull Storm example title in i18n check-strict
* **quickstart:** a11y labels, dead-import cleanup, DE label fixes, and funnel unit tests
* **quickstart:** drop non-functional sticky plan bar (global app-root overflow blocks position:sticky)
* **quickstart:** rate-limits reference body, one-player Erkunden tour, sticky plan bar, engine-switch step sync
* **quickstart:** stop SDK guide clobbering page title, hide step counter for stepless track


### Features

* **quickstart:** example cards and collapsed reference accordion
* **quickstart:** funnel i18n keys in 15 languages
* **quickstart:** funnel model interfaces
* **quickstart:** goal cards, plan bar, hero, engine picker
* **quickstart:** guided step card with copy block and step video
* **quickstart:** quiet video card (poster + summary, no autoplay)
* **quickstart:** rewrite page as goal-first funnel orchestrator
* **quickstart:** show "recommended to start" hint on the suggested goal card
* **quickstart:** stepper with single open step and progress
* **quickstart:** track data for Ausprobieren and Einbauen

## 1.99.2 (2026-07-04)


### Bug Fixes

* **dashboard:** show serving region in version footer instead of "unknown"
* **frontpages:** resolve PageSpeed accessibility, contrast, and image audits

## 1.99.1 (2026-07-02)


### Bug Fixes

* **ssr:** allow R2 tutorial videos via media-src in the CSP

# 1.99.0 (2026-07-02)


### Features

* **quickstart:** embed the 15 R2-hosted tutorial videos in the Dashboard Guide

## 1.98.1 (2026-06-27)


### Bug Fixes

* **dashboard:** localization + email AI-translate use the News table-action modal

# 1.98.0 (2026-06-26)


### Features

* **dashboard:** AI translation for email templates & localization, email tab/list UX fixes

# 1.97.0 (2026-06-26)


### Bug Fixes

* **localization:** reachable Import Language trigger, strict-safe copy-key, correct empty-state route
* **routing:** keep multi-segment localize paths as one router command


### Features

* **crash-reporting:** occurrence-detail device + stack-trace testids for tutorial capture

## 1.96.1 (2026-06-25)


### Bug Fixes

* **localization:** reachable Import Language trigger, strict-safe copy-key, correct empty-state route

# 1.96.0 (2026-06-24)


### Bug Fixes

* gated dev-only /api proxy in SSR server so the dev box reaches the backend
* **localization:** tolerate a list response without entries (avoid load crash)


### Features

* **localization:** dashboard quickstart for all SDKs + System Config category
* **localization:** management UI, frontpages, and 15-language i18n

## 1.95.1 (2026-06-21)


### Bug Fixes

* **icons:** restore icon size & centering after iconify migration

# 1.95.0 (2026-06-21)


### Bug Fixes

* **home:** fix hero LCP preload and deprioritize decorative seagull
* **legal:** render legal pages under zoneless change detection via signals


### Features

* **dashboard:** add data-testid coverage for tutorial capture
* **dashboard:** migrate icons from lucide-angular to offline iconify-icon (line-md)

## 1.94.4 (2026-06-15)


### Bug Fixes

* **ssr:** trust x-forwarded-scheme so ingress renders SSR not CSR shell

## 1.94.3 (2026-06-15)


### Bug Fixes

* **ssr:** fetch public SSR data over internal cluster DNS

## 1.94.2 (2026-06-15)


### Bug Fixes

* **ssr:** render pages with AngularNodeAppEngine instead of empty CSR shell

## 1.94.1 (2026-06-14)


### Performance Improvements

* **ssr:** cache evergreen pages 12h and blog 1h (was 10min)

# 1.94.0 (2026-06-11)


### Bug Fixes

* **auth:** keep access tokens in memory
* **auth:** preserve session across reload
* handle api explorer in dev mode
* strengthen dashboard coverage quality gates


### Features

* expand api explorer endpoint runner
* improve api explorer project testing
* merge API explorer updates into main

# 1.93.0 (2026-06-05)


### Bug Fixes

* **analytics:** guard behavior-analytics chart/timeline against missing points/events
* **i18n:** translate behavior-analytics frustration terms + titles for strict gate


### Features

* **analytics:** rework behavior-analytics page into 5 tabs

# 1.92.0 (2026-06-05)


### Bug Fixes

* **frontpages:** survive a partial public-stats response (whole-site crash)


### Features

* **analytics:** behavior capture + admin behavior-analytics page

## 1.91.1 (2026-06-03)


### Bug Fixes

* **home:** give testimonial cards a fixed height with clamp and modal

# 1.91.0 (2026-06-03)


### Features

* **seo:** English default served unprefixed at /

# 1.90.0 (2026-06-02)


### Bug Fixes

* align product/quickstart specs with forced horizon.pm base
* **frontpages:** enforce section alternation; fix pricing/home/about-us layout
* **seo:** derive SSR canonical/hreflang path from the request URL


### Features

* **dashboard:** per-language URL routing + frontend batch
* **frontpages:** usability and UX overhaul
* **frontpages:** design + real-data corrections
* **quickstart:** consolidate docs hub into /quickstart, remove colliding frontend /docs
* **seo:** localize per-page title + description via SeoService

# 1.89.0 (2026-05-22)


### Features

* add dashboard api explorer

# 1.88.0 (2026-05-22)


### Features

* add searchable docs guide hub

## 1.87.8 (2026-05-22)


### Performance Improvements

* enable zoneless dashboard change detection

## 1.87.7 (2026-05-22)


### Performance Improvements

* unblock frontend init pipeline

## 1.87.6 (2026-05-22)


### Bug Fixes

* **dashboard:** keep prerendering disabled; supply MENU_ITEMS to SSR config

## 1.87.5 (2026-05-22)


### Bug Fixes

* **consent,tracking:** queue cookie-consent calls; bound sendBeacon by byte size


### Performance Improvements

* **bundle:** lazy-load marked, vanilla-cookieconsent; drop SSR compression
* **dashboard:** bound tracking payload, plug modal subscription leak, shell to OnPush
* **dashboard:** cache public GET requests, default page size 25, trim prod logging

## 1.87.4 (2026-05-15)


### Bug Fixes

* **i18n:** translate fallback values across all 36 i18n directories and gate CI on translation coverage

## 1.87.3 (2026-05-15)


Maintenance release without user-facing changes.

## 1.87.2 (2026-05-15)


### Bug Fixes

* **i18n:** translate reactivate keys for admin-account in 13 languages

## 1.87.1 (2026-05-14)


### Bug Fixes

* **quickstart:** cover all 10 core features per engine in /quickstart

# 1.87.0 (2026-05-12)


### Features

* **dashboard:** show region versions and edit user roles

## 1.86.3 (2026-05-11)


### Bug Fixes

* **account:** show banner and reactivate CTA for soft-deleted accounts

## 1.86.2 (2026-05-09)


### Bug Fixes

* **i18n:** update leaderboard FAQ and quickstart for multi-board feature

## 1.86.1 (2026-05-09)


### Bug Fixes

* show multi-leaderboard limit in pricing comparison

# 1.86.0 (2026-05-09)


### Features

* **leaderboard:** multi-board management UI

## 1.85.3 (2026-04-29)


### Bug Fixes

* preserve llm keys and translation parsing

## 1.85.2 (2026-04-29)


### Performance Improvements

* improve modal performance

## 1.85.1 (2026-04-27)


### Bug Fixes

* **api-keys:** hide account scope fields for project keys

# 1.85.0 (2026-04-27)


### Features

* **api-keys:** add account key scope controls

## 1.84.1 (2026-04-26)


### Bug Fixes

* improve dashboard filtering and navigation

# 1.84.0 (2026-04-26)


### Features

* add Apple Sign-In API key configuration modal

## 1.83.3 (2026-04-25)


### Bug Fixes

* **user-management:** route deactivate to user's api-key in all-keys mode

## 1.83.2 (2026-04-20)


### Bug Fixes

* **blog:** remove pause/resume keep-alive that triggered TTS 'interrupted' error

## 1.83.1 (2026-04-20)


### Bug Fixes

* **blog:** resolve silent text-to-speech playback on article detail

# 1.83.0 (2026-04-20)


### Bug Fixes

* **email-templates:** correct required variables and improve template documentation
* **email-templates:** correct required variables for system email templates
* **email-templates:** i18n updates for 14 languages


### Features

* **blog:** add summary box and text-to-speech to blog detail view
* **blog:** add summary box and TTS read-aloud to blog detail view
* **blog:** i18n translations for blog public read features

## 1.82.5 (2026-04-20)


### Bug Fixes

* unblock docker build for pre-built artifacts + clean up about-us dead code

## 1.82.4 (2026-04-20)


### Bug Fixes

* landingpage polish, mobile layout, dashboard sidebar scroll

## 1.82.3 (2026-04-20)


### Bug Fixes

* **apple-signin:** correct client-id prefix and button UX

## 1.82.2 (2026-04-20)


### Bug Fixes

* **apple-signin:** allow apple CSP script/frame sources

## 1.82.1 (2026-04-20)


### Bug Fixes

* **apple-signin:** align response account type with backend Account interface

# 1.82.0 (2026-04-20)


### Features

* **apple-signin:** add Sign in with Apple support to dashboard

# 1.81.0 (2026-04-18)


### Features

* **user-management:** replace max-users stat with limit card

# 1.80.0 (2026-04-18)


### Bug Fixes

* **resources:** make structured-data spec resilient to test order randomization


### Features

* **user-management:** add resend verification email action

# 1.79.0 (2026-04-18)


### Features

* **home:** replace simple integration card with 5-minute step tabs
* **home:** streamline trust section and add continuity faq

## 1.78.1 (2026-04-17)


### Bug Fixes

* **remote-config:** validate bulk import json against plan limits client-side
* **theme:** raise light-theme primary and muted-text contrast to WCAG AA
* **users,remote-config:** deduplicate users-tab cards and move import button into page header

# 1.78.0 (2026-04-16)


### Bug Fixes

* **about:** update test counts for frontend and backend
* **api-keys:** conditional modal info text and move key type to status filter area
* **api-keys:** guard against non-array response in getAccountApiKeys


### Features

* **api-keys:** add API layer for account-api-keys endpoints
* **api-keys:** add i18n for key type filter and mcp setup (15 languages)
* **api-keys:** add keyType to ApiKey interface and DTOs
* **api-keys:** add type select filter tabs and mcp setup snippet
* **api-keys:** unified service for project and account keys

## 1.77.3 (2026-04-14)


### Performance Improvements

* **blog:** use embedded adjacent posts from detail response to cut 4.98MB

## 1.77.2 (2026-04-14)


### Bug Fixes

* **dashboard:** break leaderboard effect loop and restore remote-config import button

## 1.77.1 (2026-04-14)


### Bug Fixes

* **dashboard:** apply global api-key filter on feature navigation and shrink stat card value text

# 1.77.0 (2026-04-13)


### Features

* **dashboard:** unified shared feature-layout with prominent global API key selector

# 1.76.0 (2026-04-13)


### Features

* **dashboard:** apply shared feature-layout across all dashboard features

# 1.75.0 (2026-04-13)


### Features

* **dashboard:** introduce global api-key selector in dashboard topbar

# 1.74.0 (2026-04-13)


### Features

* **dashboard:** introduce shared feature-layout components

## 1.73.4 (2026-04-12)


### Bug Fixes

* pin email-sending seagull to background content via shared canvas

## 1.73.3 (2026-04-12)


### Bug Fixes

* move email-sending seagull 4% further down so it sits on the computer

## 1.73.2 (2026-04-12)


### Bug Fixes

* regenerate email-sending webp fallback, remove orphan avifs
* stop forcing object-fit: contain on email-sending background

## 1.73.1 (2026-04-12)


### Bug Fixes

* crop email-sending feature background to 2.357 aspect

# 1.73.0 (2026-04-12)


### Features

* apply playground-generated email-sending feature background

# 1.72.0 (2026-04-12)


### Features

* test SMTP with unsaved form and update new bento image

## 1.71.2 (2026-04-12)


### Bug Fixes

* regenerate EmailSending bentogrid placeholder

## 1.71.1 (2026-04-12)


### Bug Fixes

* move SMTP banner and sender override i18n keys to correct namespace

# 1.71.0 (2026-04-12)


### Features

* boost test coverage to 86% statements, add 238 tests

# 1.70.0 (2026-04-11)


### Bug Fixes

* **email-sending:** add missing feature background and bentogrid images


### Features

* add SMTP settings UI and system email templates support

# 1.69.0 (2026-04-11)


### Features

* **email-sending:** add multi-language template form and pricing table entry

# 1.68.0 (2026-04-11)


### Features

* **email-sending:** add email sending management feature

## 1.67.7 (2026-04-11)


### Bug Fixes

* **remote-config:** use bulk delete endpoint instead of parallel individual requests

## 1.67.6 (2026-04-11)


### Bug Fixes

* **remote-config:** improve import dialog hint text visibility

## 1.67.5 (2026-04-10)


### Bug Fixes

* apply persisted API key filter on init for leaderboard and feedback

## 1.67.4 (2026-04-10)


### Bug Fixes

* remove debug logs from API key filter chain

## 1.67.3 (2026-04-10)


### Bug Fixes

* add debug logs to leaderboard and user management handlers

## 1.67.2 (2026-04-10)


### Bug Fixes

* add debug logging to API key filter chain

## 1.67.1 (2026-04-10)


### Bug Fixes

* API key selector binding and filter propagation

# 1.67.0 (2026-04-10)


### Features

* global API key selector with session persistence

## 1.66.1 (2026-04-10)


### Bug Fixes

* **remote-config:** load all entries and fix action column width

# 1.66.0 (2026-04-10)


### Features

* standalone email-verified page without dashboard shell

## 1.65.4 (2026-04-10)


### Bug Fixes

* correct bug bounty background alignment and improve nav divider visibility

## 1.65.3 (2026-04-10)


### Bug Fixes

* revert hero gradient to original and upgrade nav button styling

## 1.65.2 (2026-04-10)


### Bug Fixes

* correct bug bounty background coverage and make hero-gradient compositable

## 1.65.1 (2026-04-10)


### Performance Improvements

* improve PageSpeed score with LCP preload, nav reorder, and background fix

# 1.65.0 (2026-04-09)


### Features

* **dashboard:** capture UTM parameters in tracking collect service

## 1.64.1 (2026-03-21)


### Bug Fixes

* resolve animation clipping on feature and bug bounty background layers

# 1.64.0 (2026-03-21)


### Features

* add animated 3-layer background system for all feature pages and bug bounty section

# 1.63.0 (2026-03-18)


### Features

* replace WebP backgrounds with responsive AVIF on about and compare pages

## 1.62.4 (2026-03-18)


### Bug Fixes

* reduce backdrop-blur from 10px to 6px and add glass effect to price cards

## 1.62.3 (2026-03-18)


### Bug Fixes

* fix section background animations and gradients stripped by Tailwind CSS 4 build

## 1.62.2 (2026-03-18)


### Bug Fixes

* align video language hint with YouTube settings button in real browsers

## 1.62.1 (2026-03-18)


### Bug Fixes

* add video language hint below YouTube embeds in quickstart guides

# 1.62.0 (2026-03-18)


### Bug Fixes

* increase hero section height to 80vh for better card visibility on FullHD
* unify landing page typography for consistent font sizes


### Features

* add animated background layers with seagulls for all homepage sections

## 1.61.2 (2026-03-13)


### Bug Fixes

* increase AVIF quality to q50 for small hero image breakpoints

## 1.61.1 (2026-03-12)


### Bug Fixes

* revert non-hero images back to WebP and fix pixel-wave divider z-index

# 1.61.0 (2026-03-12)


### Features

* add animated 3-layer hero background and migrate to AVIF format

## 1.60.2 (2026-03-12)


### Bug Fixes

* **comparison:** use hardcoded competitor names instead of translation keys
* improve background image quality and remove bg-fixed rendering issue

## 1.60.1 (2026-03-06)


### Bug Fixes

* resolve comparison page issues and update homepage pricing

# 1.60.0 (2026-03-06)


### Features

* **comparison:** use real Stripe prices and server-side exchange rate

## 1.59.1 (2026-03-06)


### Bug Fixes

* correct pricing tiers and translation interpolation on comparison pages

# 1.59.0 (2026-03-06)


### Features

* add SEO comparison pages (hub + 8 competitor alternatives)

## 1.58.5 (2026-03-04)


### Bug Fixes

* **crash:** reload group after status/notes update instead of parsing empty 204 response

## 1.58.4 (2026-03-04)


### Bug Fixes

* **crash:** register missing lucide icons for crash reporting

## 1.58.3 (2026-03-04)


### Bug Fixes

* **about:** remove gap between top-nav and hero section

## 1.58.2 (2026-03-04)


### Bug Fixes

* **home:** standardize typography to 4 consistent font sizes

## 1.58.1 (2026-03-04)


### Bug Fixes

* **sdk-settings:** move SDK links editor from SDK settings to system config

# 1.58.0 (2026-03-04)


### Features

* **sdk-settings:** add inline editing for SDK links

# 1.57.0 (2026-03-04)


### Features

* add Daily Active Users, soft/hard rate limits to pricing comparison

# 1.56.0 (2026-03-03)


### Features

* unify website design with glass cards, nav restructuring, and hero adjustments

# 1.55.0 (2026-03-02)


### Features

* **quickstart:** add GitHub hero links, PHP info callout, clean up Unity prereqs, and language-aware YouTube embeds

## 1.54.3 (2026-03-01)


### Bug Fixes

* **i18n:** add missing quickstart prerequisites/troubleshooting keys and fix simple-server category

## 1.54.2 (2026-02-28)


### Bug Fixes

* **quickstart:** correct simpleServer translation keys for specialCards and faqs

## 1.54.1 (2026-02-28)


### Bug Fixes

* **csp:** allow youtube.com in frame-src for quickstart video embeds

# 1.54.0 (2026-02-28)


### Features

* **quickstart:** add YouTube video tutorials for dashboard, unity, rest-api, and support pages

## 1.53.1 (2026-02-28)


### Bug Fixes

* use full-resolution hero image on portrait screens

# 1.53.0 (2026-02-28)


### Features

* **pricing:** only show available accounts when fewer than 10 remain

## 1.52.1 (2026-02-27)


### Bug Fixes

* **products:** convert cloudSaveBytes to KB in comparison table

# 1.52.0 (2026-02-27)


### Bug Fixes

* **i18n:** remove per-API-key reference from remote config limit message


### Features

* **products:** fetch real feature limits from API for comparison table

## 1.51.8 (2026-02-27)


### Bug Fixes

* remove redundant frontend tracking in favor of server-side events

## 1.51.7 (2026-02-26)


### Bug Fixes

* **ssr:** use route resolvers for blog pages to guarantee SSR content

## 1.51.6 (2026-02-26)


### Bug Fixes

* **seo:** allow Googlebot to fetch public API endpoints

## 1.51.5 (2026-02-26)


### Bug Fixes

* move commit command to parent workspace root
* refactor CLAUDE.md to remove rules now in workspace root
* **ssr:** resolve relative API_URL for server-side data fetching

## 1.51.4 (2026-02-25)


### Bug Fixes

* move bug bounty mascot to left side at -top-32

## 1.51.3 (2026-02-25)


### Bug Fixes

* remove testimonial section scrollbar and reposition bug bounty mascot

## 1.51.2 (2026-02-25)


### Bug Fixes

* remove testimonial card height constraint and fix unregistered icon

## 1.51.1 (2026-02-25)


### Bug Fixes

* resolve home page glass styling, missing labels, testimonial height and mascot positioning

# 1.51.0 (2026-02-25)


### Bug Fixes

* remove billing toggles from comparison sections and prices from feature table


### Features

* polish home and features page UI/UX

# 1.50.0 (2026-02-24)


### Features

* replace hero gradient overlays with frosted glass text containers

# 1.49.0 (2026-02-24)


### Features

* add background hero images and prev/next navigation to feature pages

# 1.48.0 (2026-02-24)


### Features

* redesign feature detail pages with interactive mockups and quickstart improvements

# 1.47.0 (2026-02-23)


### Features

* extract shared quickstart-guide component and add reactive route params
* **frontend:** add version API method to PublicSystemApi
* **frontend:** add VersionManager for backend version fetching
* **frontend:** display frontend and backend version in footer

# 1.46.0 (2026-02-23)


### Features

* add bulk action support with confirmation dialogs to 12 data table features

# 1.45.0 (2026-02-22)


### Features

* add 9 dedicated SEO feature pages with shared template architecture

## 1.44.1 (2026-02-22)


### Bug Fixes

* improve SDK section grid layout and testimonial card overflow

# 1.44.0 (2026-02-22)


### Features

* add open source server section and dynamic API URL routing

## 1.43.3 (2026-02-22)


### Bug Fixes

* display blog post title above hero image

## 1.43.2 (2026-02-22)


### Bug Fixes

* **i18n:** resolve broken translation key references across multiple features

## 1.43.1 (2026-02-22)


### Bug Fixes

* use central domain for tracking collect in production

# 1.43.0 (2026-02-22)


### Features

* activate Unreal Engine quickstart tab with SDK documentation
* add crash reporting integration, cloud save enhancements, and UI improvements
* add public /resources page with SSR and i18n
* mark Unreal Engine SDK as available and link SDKs to quickstart guide

# 1.42.0 (2026-02-22)


### Features

* add crash reporting integration, cloud save enhancements, and UI improvements

# 1.41.0 (2026-02-21)


### Features

* add unified data table component and migrate all features

# 1.40.0 (2026-02-21)


### Features

* **crash:** add i18n translations for all supported languages

# 1.39.0 (2026-02-21)


### Features

* **crash:** add crash reporting page components and state service
* **crash:** add frontend models, API service, and feature config
* **crash:** add i18n translations for crash reporting

## 1.38.2 (2026-02-21)


### Bug Fixes

* **blog:** use relative paths for blog images to avoid mixed content and CSP violations

## 1.38.1 (2026-02-21)


### Bug Fixes

* **a11y:** use blog title as alt attribute for image preview in admin modal

# 1.38.0 (2026-02-21)


### Features

* **ssr:** enable SSR with real API data for public pages

## 1.37.7 (2026-02-21)


### Bug Fixes

* **ui:** improve tour modal visibility in dark mode with secondary border and glow

## 1.37.6 (2026-02-21)


### Bug Fixes

* **ui:** redesign modal with theme-aware styling and tighter spacing

## 1.37.5 (2026-02-21)


### Bug Fixes

* **ticket-system:** use updatedAt as fallback when lastMessageDate is null

## 1.37.4 (2026-02-21)


### Bug Fixes

* **ui:** redesign checkboxes with global styles for consistency and visibility

## 1.37.3 (2026-02-20)


### Bug Fixes

* **onboarding:** persist tour state on dismiss and resume on navigation

## 1.37.2 (2026-02-20)


### Bug Fixes

* **onboarding:** resolve tour dialog styling and interactivity issues

## 1.37.1 (2026-02-20)


### Bug Fixes

* **onboarding:** use default export from shepherd.js dynamic import

# 1.37.0 (2026-02-20)


### Bug Fixes

* **i18n:** escape Chinese quotation marks in zh.toml onboarding section
* **ui:** add max-height and scroll overflow to all modal containers


### Features

* **onboarding:** add data-onboarding attributes to target elements
* **onboarding:** add declarative tour steps config
* **onboarding:** add horizOn theme CSS for Shepherd.js tour
* **onboarding:** add restart tour button to account settings
* **onboarding:** add storage keys and English i18n translations
* **onboarding:** add tour translations for all 14 languages
* **onboarding:** create welcome modal component
* **onboarding:** implement OnboardingTourService with lazy Shepherd.js loading
* **onboarding:** integrate tour service and welcome modal into dashboard
* **onboarding:** register onboarding-tour feature module

## 1.36.2 (2026-02-20)


### Bug Fixes

* **i18n:** add missing modal.removeFoldout translation key to all languages

## 1.36.1 (2026-02-20)


### Bug Fixes

* **modal:** replace hardcoded aria-label with translated foldout remove label

# 1.36.0 (2026-02-20)


### Bug Fixes

* add missing register form i18n keys and hide accountId from user logs
* default-hide closed tickets in admin view and add multi-lang design doc
* **modal:** make modal scrollable when content exceeds viewport height
* **tickets:** add missing fields to TicketListResponse DTO and fix createdAt mapping


### Features

* add Ahrefs Web Analytics and clean up CSP after server-side tracking migration
* add multi-language field utility and refactor content management modals

# 1.35.0 (2026-02-19)


### Bug Fixes

* consolidate regional subdomain URLs to single horizon.pm domain


### Features

* replace client-side tracking with server-side TrackingCollectService

## 1.34.3 (2026-02-19)


### Bug Fixes

* add regional subdomains to CSP img-src for blog images

## 1.34.2 (2026-02-19)


### Bug Fixes

* **seo:** consolidate domain to horizon.pm and remove /home route

## 1.34.1 (2026-02-17)


### Bug Fixes

* enable lazy background image loading on About Us page

# 1.34.0 (2026-02-17)


### Bug Fixes

* add missing analytics replay and cookie service wiring
* make Mori seagull images visible and inline on About Us page


### Features

* add cookie consent translations for pt, nl, pl, ru, zh, ja, ar, ko, tr, id
* add Google Consent Mode v2 default (all denied) before scripts load
* add Microsoft Advertising to cookie consent analytics services
* enhance About Us page with visual design and Mori seagulls
* fire gtag consent update on cookie consent change

# 1.33.0 (2026-02-17)


### Features

* add About Us page with indie dev story and live stats

# 1.32.0 (2026-02-17)


### Features

* **i18n:** SSR language detection from Accept-Language header

# 1.31.0 (2026-02-17)


### Features

* **seo:** canonicalize all regions to us.horizon.pm

## 1.30.1 (2026-02-17)


### Bug Fixes

* add SEO page titles and meta descriptions to examples, quickstart, and blog pages

# 1.30.0 (2026-02-16)


### Features

* add Meta Pixel conversion events for signup, purchase, and checkout

## 1.29.2 (2026-02-16)


### Bug Fixes

* add Facebook domains to CSP for Meta Pixel tracking

## 1.29.1 (2026-02-16)


### Bug Fixes

* set default Meta Pixel ID so pixel loads without env var override

# 1.29.0 (2026-02-16)


### Features

* add Meta Pixel (Facebook) tracking with cookie consent integration

# 1.28.0 (2026-02-15)


### Features

* add markdown rendering for blog detail page

## 1.27.1 (2026-02-15)


### Bug Fixes

* auto-append /chat/completions to custom OpenAI base URLs

# 1.27.0 (2026-02-15)


### Features

* add optional base URL field for OpenAI and Gemini providers

## 1.26.5 (2026-02-15)


### Bug Fixes

* add blob: to CSP img-src for blog image preview

## 1.26.4 (2026-02-15)


### Bug Fixes

* load blog image in modal when imageUrl is present

## 1.26.3 (2026-02-15)


### Bug Fixes

* resolve blog image visibility, missing translations, footer year, and deletion UX

## 1.26.2 (2026-02-15)


### Bug Fixes

* allow LM Studio connections by relaxing CSP connect-src directive

## 1.26.1 (2026-02-15)


### Bug Fixes

* attach auth token for ticket creation and expose blog hasImage field

# 1.26.0 (2026-02-15)


### Bug Fixes

* **blog:** update news spec tests for card grid and Load More redesign


### Features

* add blog redesign implementation plan
* **blog:** create NewsDetail component with SEO meta tags and adjacent navigation
* **blog:** redesign blog list with card grid and Load More button
* **blog:** translate blog i18n keys for all languages and add productionUrl
* **blog:** update data layer for blog redesign
* **blog:** update English i18n keys for blog redesign
* finalize blog redesign design document

# 1.25.0 (2026-02-14)


### Features

* **blog:** add blog image upload UI with drag-and-drop support

## 1.24.1 (2026-02-13)


### Bug Fixes

* improve Trust Bar alignment, light mode overlays, and sidebar button order

# 1.24.0 (2026-02-13)


### Features

* add changelog link to Trust Bar and dashboard sidebar

## 1.23.3 (2026-02-13)


### Bug Fixes

* use wildcard CSP for Clarity subdomains to fix v.clarity.ms block

## 1.23.2 (2026-02-13)


### Bug Fixes

* add missing Bing UET and Clarity script domains to CSP

## 1.23.1 (2026-02-13)


### Bug Fixes

* add missing GTM and Microsoft Clarity domains to CSP

# 1.23.0 (2026-02-13)


### Features

* add GitHub SDK links to engine cards and allow Bing UET in CSP

## 1.22.17 (2026-02-12)


### Bug Fixes

* add stats.g.doubleclick.net to CSP connect-src directive

## 1.22.16 (2026-02-11)


### Bug Fixes

* resolve lazy loading and scroll-to-pricing failures on deferred content

## 1.22.15 (2026-02-11)


### Performance Improvements

* optimize CLS, reduce DOM size, and add admin accounts caching

## 1.22.14 (2026-02-11)


### Bug Fixes

* suppress console errors from blocked third-party script loads

## 1.22.13 (2026-02-11)


### Performance Improvements

* add preconnect hints and optimize hero background image

## 1.22.12 (2026-02-11)


### Bug Fixes

* add PWA icons and update manifest for installability compliance

## 1.22.11 (2026-02-11)


### Bug Fixes

* add missing Google Ads/GTM/GA4 domains to CSP for full tracking support

## 1.22.10 (2026-02-11)


### Performance Improvements

* optimize page load performance based on Catchpoint report

## 1.22.9 (2026-02-10)


### Bug Fixes

* add Google Ads audience pixel domain to CSP img-src

## 1.22.8 (2026-02-10)


### Bug Fixes

* add Google Ads conversion domains to CSP connect-src

## 1.22.7 (2026-02-10)


### Bug Fixes

* send auth token with check-auth and guard against null response

## 1.22.6 (2026-02-10)


### Bug Fixes

* skip auth guards during SSR to prevent logout on page reload

## 1.22.5 (2026-02-10)


### Bug Fixes

* add missing Google Analytics and Ads domains to CSP connect-src

## 1.22.4 (2026-02-10)


### Bug Fixes

* add accounts.google.com to CSP script-src for Google Sign-In

## 1.22.3 (2026-02-09)


### Performance Improvements

* add compression, CSP headers, web manifest, and fix accessibility contrast

## 1.22.2 (2026-02-09)


### Bug Fixes

* resolve mobile nav hydration mismatch causing layout flash

## 1.22.1 (2026-02-09)


### Performance Improvements

* fix SSR hydration and eliminate duplicate HTTP requests on page load

# 1.22.0 (2026-02-09)


### Features

* **i18n:** translate admin-banner feature into all 13 languages

# 1.21.0 (2026-02-09)


### Features

* **i18n:** add complete translation coverage for all 15 languages and build-time validation

# 1.20.0 (2026-02-09)


### Features

* **i18n:** add quickstart and news translations for 13 languages and fix blog reactivity

## 1.19.1 (2026-02-09)


### Bug Fixes

* prevent undefined params from being sent as literal strings in admin accounts API

# 1.19.0 (2026-02-09)


### Bug Fixes

* revert manual version bump and fix commit workflow for semantic-release


### Features

* **i18n:** add version-based cache-busting to translation file loading

## 1.18.2 (2026-02-08)


### Bug Fixes

* correct testimonial API path, add gift code display, and fix news i18n key scoping

## 1.18.1 (2026-02-08)


### Bug Fixes

* **dev-mode:** hide dev mode panel in production builds

# 1.18.0 (2026-02-08)


### Features

* **testimonial:** add customer testimonial submission and admin review workflow

# 1.16.0 (2026-02-08)


### Bug Fixes

* **i18n:** remove duplicate home.hero and home.solution keys from public translation files


### Features

* add dev-mode, blog management, examples page mockups, and mobile responsiveness
* add rate limiting and help sections to Godot and REST API quickstart guides
* **dev-mode:** add mock endpoints for customer testimonial submission and review
* **i18n:** add testimonial submission and review translations for all languages
* **i18n:** update sidebar translation keys for all languages
* **mobile:** add Capacitor native platform support for Android and iOS
* **system-config:** add testimonial reward category with i18n for all languages
* **testimonial:** add admin review workflow with approve/reject actions
* **testimonial:** add customer testimonial submission page
* **testimonial:** trigger release for customer submission and review workflow

# 1.15.0 (2026-02-04)


### Bug Fixes

* enforce release-triggering commits and update SEO service tests for hreflang support
* generate fallback transaction_id for Google Ads conversion tracking


### Features

* add GA4/GTM analytics tracking and migrate SEO domain to us.horizon.pm

# 1.14.0 (2026-02-01)


### Features

* add Google Ads conversion tracking to purchase success page
* add purchase success page for Stripe payment confirmation

## 1.13.1 (2026-02-01)


### Bug Fixes

* use npm ci instead of artifact transfer for node_modules

# 1.13.0 (2026-02-01)


### Features

* add Google Ads conversion tracking for registration

## 1.12.4 (2026-02-01)


### Bug Fixes

* add SSR caching for home route to improve TTFB

## 1.12.3 (2026-01-31)


### Bug Fixes

* improve LCP with responsive hero image and optimized assets

## 1.12.2 (2026-01-31)


### Performance Improvements

* restore parallel initialization for faster FCP/LCP

## 1.12.1 (2026-01-31)


### Bug Fixes

* update initialization manager tests for phased execution


### Performance Improvements

* optimize PageSpeed with FOUC prevention and lazy image loading

# 1.12.0 (2026-01-31)


### Features

* add comprehensive SEO service with structured data and meta tag management

## 1.11.1 (2026-01-30)


### Performance Improvements

* optimize bundle size and initial load performance

# 1.11.0 (2026-01-28)


### Features

* add gclid tracking for Google Ads attribution

# 1.10.0 (2026-01-28)


### Features

* add Google Tag Manager with cookie consent gate

## 1.9.2 (2026-01-26)


### Bug Fixes

* switch SSR server to CommonEngine for better compatibility

## 1.9.1 (2026-01-26)


### Bug Fixes

* lazy-initialize Angular SSR engine to avoid manifest timing issues

# 1.9.0 (2026-01-26)


### Features

* add Express SSR server for production Docker deployment

## 1.8.2 (2026-01-26)


### Bug Fixes

* add SSR compatibility guards for browser-only APIs

## 1.8.1 (2025-12-18)


### Bug Fixes

* add dynamic canonical URL and hreflang tags for regional SEO

# 1.8.0 (2025-12-14)


### Features

* auto-refresh auth after subscription changes
* mark Godot SDK as available and improve price cards readability

# 1.7.0 (2025-12-09)


### Features

* expand FREE tier access and add marketing documentation

# 1.6.0 (2025-12-07)


### Features

* add Unity SDK quickstart guide with step-by-step tutorial

## 1.5.1 (2025-12-07)


### Performance Improvements

* optimize PageSpeed Insights performance and accessibility

# 1.5.0 (2025-12-07)


### Features

* add email verification page and enhance user feedback with category/device info

# 1.4.0 (2025-12-05)


### Features

* add docs link to sidebar and enhance home page translations

# 1.3.0 (2025-12-04)


### Features

* update signInWithGoogle method to include redirect URI

# 1.2.0 (2025-12-04)


### Features

* update routing and canonical URLs to reflect new domain structure

# 1.1.0 (2025-12-04)


### Bug Fixes

* enhance logging functionality and improve test coverage
* revert home page
* update support titles and descriptions across multiple languages


### Features

* add complete data export request functionality and update localization strings
* add section dividers to enhance layout and visual separation
* implement pixel wave section divider and update SVG assets

# 1.0.0 (2025-12-04)


### Features

* add testimonial management feature with dynamic home page integration
* redesign home page with new marketing sections and expanded content


### Performance Improvements

* convert images to WebP format and add lazy loading
