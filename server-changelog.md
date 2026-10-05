---
layout: default
title: Server Changelog
---

# Server Changelog

All notable changes to the horizOn Server (Backend API).

[Back to Overview](.)

## 1.66.2 (2026-10-05)


### Bug Fixes

* **gift-codes:** use primary reads for redemption transactions

## 1.66.1 (2026-10-02)


### Bug Fixes

* **status:** encode PromQL queries as URI variables

# 1.66.0 (2026-10-02)


### Bug Fixes

* **validated-actions:** break the bean cycle through the run start context
* **validated-actions:** show the rules part size in the sus package detail


### Features

* **status:** add public status API with 90-day regional availability
* **validated-actions:** archive sus runs with start context and package export

# 1.65.0 (2026-10-01)


### Bug Fixes

* **dashboard:** preserve overview error statuses
* **dashboard:** read legacy usage bucket identifiers safely
* **gift-codes:** bind redemption to the player session
* **gift-codes:** require the player session for every redemption
* **leaderboard:** count a requested API key directly in /limits so a foreign key id cannot reset the shared score count cache
* **rate-limit:** send Retry-After on crash report and user log 429s and never announce 0 seconds
* **ratelimit:** enforce hard limit with 429 on leaderboard submit and cloud save
* **release:** gate server publication on compatible clients
* **validated-actions:** refuse run tickets with a non-canonical base64 spelling
* **validated-actions:** scope evidence lookups by API key and finish row clean-up after errors


### Features

* **api-explorer:** forward the player session to every App API route that requires it
* **api-explorer:** proxy the Validated Actions player endpoints with the player session
* **dashboard:** add scoped operational overview endpoint
* **leaderboard:** count the score limit per API key
* **player-profile:** avatar, frame, badges and cosmetic unlocks with gift code grants
* **sitemap:** list the quickstart docs articles
* **validated-actions:** evidence upload, review list and leaderboard moderation
* **validated-actions:** server-checked runs with single-use tickets and rules
* **validated-actions:** server-owned player state with daily caps

## 1.64.8 (2026-09-23)


### Bug Fixes

* **cloud-save:** enforce opt-in project client versions
* **news:** allow project-scoped account keys on owned news items

## 1.64.7 (2026-09-05)


### Bug Fixes

* bind leaderboard submissions to user sessions
* **blog:** sanitize stored markdown content
* cover gift code transaction execution
* **gift-codes:** strengthen transaction consistency
* make gift code redemption atomic
* **mongo:** preserve tenant routing in transactions
* **release:** promote security hardening to production
* revoke inactive account session privileges
* **security:** align Mongo integration fixtures
* **security:** bind email recipients to project keys
* **security:** bound Mongo integration resources
* **security:** close audit follow-up gaps
* **security:** configure Testcontainers API
* **security:** enforce Mongo integration execution
* **security:** harden actuator credentials
* **security:** harden anonymous user tokens
* **security:** harden public log ingestion
* **security:** harden SMTP test targets
* **security:** isolate account key management
* **security:** isolate Mongo integration scheduling
* **security:** keep disabled change stream injectable
* **security:** prevent auth email enumeration
* **security:** protect global cache and index operations
* **security:** protect settings secrets in data exports
* **security:** prove auth timing floor regression
* **security:** remove production GA4 test endpoint
* **security:** stabilize auth timing regression
* **security:** verify real public auth timing paths
* **support:** enforce tenant-bound ticket access

## 1.64.6 (2026-08-24)


### Bug Fixes

* **users:** allow scoped user deletion

## 1.64.5 (2026-08-20)


### Bug Fixes

* **users:** scope statistics by api key

## 1.64.4 (2026-08-13)


Maintenance release without user-facing changes.

## 1.64.3 (2026-08-13)


### Bug Fixes

* **news:** publish scheduled entries automatically
* run server CI on local runners

## 1.64.2 (2026-08-08)


### Bug Fixes

* **api-keys:** honor never-expire account keys

## 1.64.1 (2026-08-07)


### Bug Fixes

* add conflict-safe cloud save revisions

# 1.64.0 (2026-08-07)


### Bug Fixes

* **users:** cover test account marker lifecycle
* **users:** include role in signin response
* **users:** remove BodySeasons test account marker


### Features

* **users:** mark internal test accounts

## 1.63.3 (2026-07-26)


### Bug Fixes

* **scheduling:** pin index maintenance outside the backup window

## 1.63.2 (2026-07-25)


### Bug Fixes

* **analytics:** repair traffic segmentation and filters

## 1.63.1 (2026-07-25)


### Bug Fixes

* **analytics:** rebuild behavior insights

# 1.63.0 (2026-07-19)


### Features

* **restore:** coordinate account-selective database restores

# 1.62.0 (2026-07-13)


### Features

* **auth:** add rotating refresh tokens

## 1.61.2 (2026-07-13)


### Bug Fixes

* **security:** encrypt retained cloud saves

## 1.61.1 (2026-07-13)


### Bug Fixes

* **auth:** accept long passwords at sign in
* **security:** bind and encrypt cloud saves
* **security:** encrypt cloud save admin operations
* **security:** migrate legacy cloud saves at startup

# 1.61.0 (2026-07-02)


### Features

* **user-management:** one-click Google auth via signInIfExists upsert sign-up

# 1.60.0 (2026-06-24)


### Features

* **localization:** backend storage, app + admin APIs, per-key limits

# 1.59.0 (2026-06-11)


### Bug Fixes

* add apple service test default
* add discord oauth test default
* **api-explorer:** send prefixed app api key
* **auth:** restore sessions from cookie
* enforce server coverage quality gates
* harden mongo integration tests and account limits
* keep server ci coverage gate deterministic
* provide test admin email default
* route api explorer app proxy internally
* stabilize remaining mongo integration assertions
* stabilize server test defaults in ci


### Features

* add admin api explorer proxy
* merge API explorer proxy into master
* proxy app endpoints in api explorer

# 1.58.0 (2026-06-05)


### Features

* **analytics:** behavior-analytics dimensions + admin endpoints

# 1.57.0 (2026-06-05)


### Features

* **analytics:** behavior analytics ingest + admin aggregations

# 1.56.0 (2026-06-03)


### Features

* **seo:** curate sitemap to needed public pages only
* **seo:** sitemap serves English unprefixed for horizon.pm

## 1.55.1 (2026-06-02)


### Bug Fixes

* null-safe session cache unless to stop 401s on cold cache

# 1.55.0 (2026-06-02)


### Features

* **i18n:** language-prefixed sitemap URLs + localized email links

## 1.54.5 (2026-05-22)


### Performance Improvements

* harden backend cache invalidation
* tune backend jvm and logging

## 1.54.4 (2026-05-22)


### Performance Improvements

* buffer feature telemetry and harden compression

## 1.54.3 (2026-05-22)


### Performance Improvements

* harden backend scheduling and async tasks

## 1.54.2 (2026-05-22)


### Bug Fixes

* **backend:** drop disabled mongo contributor from readiness probe group

## 1.54.1 (2026-05-22)


### Bug Fixes

* **blog-stats:** coerce $sum counters via Number to survive int64 promotion
* **security:** require authentication for admin API docs endpoints


### Performance Improvements

* **backend:** probes split, Tomcat sized for virtual threads, stop creating sessions on /api/v1/app
* **mongo:** index coverage, capped pagination, bulk-write retention sweeps
* **mongo:** kill collection scans on Stripe lookup, crash retention, sitemap

# 1.54.0 (2026-05-12)


### Features

* **system:** expose app region in version response

## 1.53.2 (2026-05-11)


### Bug Fixes

* **auth:** auto-reactivate soft-deleted accounts on re-login
* sync SystemConfig cache across backend pods via Mongo change stream

## 1.53.1 (2026-05-09)


### Bug Fixes

* expose multi-leaderboard limit in public feature limits

# 1.53.0 (2026-05-09)


### Features

* **leaderboard:** multi-board schema with slim scores

# 1.52.0 (2026-05-03)


### Features

* add user role update endpoint

# 1.51.0 (2026-04-30)


### Features

* support remote config glob filters

## 1.50.4 (2026-04-29)


### Bug Fixes

* preserve llm api keys on settings updates

## 1.50.3 (2026-04-29)


### Performance Improvements

* **remote-config:** use mongo bulk writes for imports

## 1.50.2 (2026-04-27)


### Bug Fixes

* **remote-config:** add filtered config lookup

## 1.50.1 (2026-04-27)


### Bug Fixes

* **health:** prevent edge caching of public health

# 1.50.0 (2026-04-27)


### Features

* **account-keys:** add scoped account keys

## 1.49.4 (2026-04-26)


### Bug Fixes

* support server-side user filters

## 1.49.3 (2026-04-26)


### Bug Fixes

* return Apple signup failures with proper status

## 1.49.2 (2026-04-25)


### Bug Fixes

* **user-management:** map InvalidApiKeyException to 403 instead of 401

## 1.49.1 (2026-04-20)


Maintenance release without user-facing changes.

# 1.49.0 (2026-04-20)


### Features

* **blog:** add summaries field for blog post summaries
* **blog:** add summaries field for per-language blog post summaries


### Performance Improvements

* **api-app:** reduce db round-trips across auth, crash-reports, user-logs, leaderboard
* **check-auth:** snapshot user state on session + atomic sliding update
* **crash-reports:** incremental user tracking, cached limit, atomic session mark
* **leaderboard/around:** facet around query, db-side bulk rank, count cache
* **user-logs:** async limit enforcement, cached count, bulk soft-delete

# 1.48.0 (2026-04-20)


### Features

* **apple-signin:** expose authStatus in SignUpResponse

# 1.47.0 (2026-04-20)


### Features

* **auth:** apple sign-in for accounts and users

## 1.46.2 (2026-04-19)


### Bug Fixes

* **email-template:** align RESERVED_SLUGS with token-only template variables

## 1.46.1 (2026-04-19)


### Bug Fixes

* **user-email:** drop horizon.pm link injection in account-SMTP path

# 1.46.0 (2026-04-19)


### Features

* **email:** allow leading underscore in template slug

## 1.45.2 (2026-04-18)


### Bug Fixes

* **user-management:** regenerate verification token on admin resend

## 1.45.1 (2026-04-18)


### Bug Fixes

* **async:** propagate AccountContextHolder to async executor threads

# 1.45.0 (2026-04-18)


### Features

* **app-api:** perf easy-wins + admin resend verification email

## 1.44.3 (2026-04-17)


### Bug Fixes

* **remote-config:** batch bulk-delete and bulk-upsert into single-round mongo writes


### Performance Improvements

* **app-api:** atomic $inc on redeem plus api-key from request context
* **app-api:** cache /remote-config/all responses per api key
* **app-api:** cache smtp config and email templates on send hot-path
* **app-api:** change-name via atomic updateFirst instead of findById+save
* **app-api:** skip getUserRank in /leaderboard/submit app path
* **app-api:** user-feedback submit uses context account plus count cache

## 1.44.2 (2026-04-17)


### Bug Fixes

* **user-auth:** scope google, email and anonymous identity per API key

## 1.44.1 (2026-04-17)


### Bug Fixes

* **api-keys:** treat legacy keys without key_type field as PROJECT

# 1.44.0 (2026-04-16)


### Features

* **account-api-keys:** add CRUD controller and service
* **api-keys:** add keyType field to distinguish PROJECT and ACCOUNT keys
* **api-keys:** add keyType filter overload to authenticateApiKey
* **api-keys:** expose keyType in responses and allow filtering
* **api-keys:** support custom key prefix and revoke reason
* **security:** add @SessionOnly annotation and interceptor
* **security:** add AccountApiKeyAuthentication token
* **security:** add AccountApiKeyAuthenticationFilter for X-Account-API-Key header
* **security:** audit-log mutations performed via account-api-key
* **security:** register AccountApiKeyAuthenticationFilter in SecurityConfig
* **security:** restrict sensitive endpoints to session auth via @SessionOnly
* **user-management:** add statistics endpoint for dashboard stats


### Performance Improvements

* **security:** add per-key rate-limit bucket for account api keys

## 1.43.1 (2026-04-14)


### Performance Improvements

* **blog:** embed adjacent posts in detail response to cut payload by 4.98MB

# 1.43.0 (2026-04-13)


### Features

* expose deleted api-key count and extended cloud-save statistics

## 1.42.1 (2026-04-12)


### Bug Fixes

* support SMTPS/STARTTLS auto-detection and unsaved-config tests

# 1.42.0 (2026-04-12)


### Features

* boost test coverage to 82% instructions, add 251 tests

# 1.41.0 (2026-04-11)


### Features

* add SMTP settings and system email template routing

# 1.40.0 (2026-04-11)


### Features

* **email-sending:** add email sending feature with template management and queue processing

## 1.39.6 (2026-04-11)


### Bug Fixes

* **remote-config:** add bulk delete endpoint and fix duplicate key error on soft-delete

## 1.39.5 (2026-04-11)


### Bug Fixes

* **remote-config:** raise bulk import limit from 100 to 10000 entries

## 1.39.4 (2026-04-11)


### Bug Fixes

* **remote-config:** raise DTO validation limit to 1024 so role-based limits apply

## 1.39.3 (2026-04-10)


### Bug Fixes

* **user-mgmt:** filter users by API key in getUsers endpoint

## 1.39.2 (2026-04-10)


### Bug Fixes

* **mail:** align default SMTP config with cluster Postfix relay

## 1.39.1 (2026-04-09)


### Bug Fixes

* **security:** resolve featureUsageFilter circular bean creation

# 1.39.0 (2026-04-09)


### Features

* **marketing:** admin marketing API backend

## 1.38.1 (2026-03-14)


### Bug Fixes

* add lastmod to static sitemap URLs for better Google indexing

# 1.38.0 (2026-03-06)


### Features

* add comparison pages to sitemap and improve index management

# 1.37.0 (2026-03-06)


### Features

* add cached EUR/USD exchange rate endpoint

## 1.36.2 (2026-03-01)


### Bug Fixes

* return 404 instead of 500 for NotFoundException and fix BrotliCompressionFilter order

## 1.36.1 (2026-02-27)


### Bug Fixes

* pass release version to Docker build for correct /version endpoint

# 1.36.0 (2026-02-27)


### Bug Fixes

* move commit command to parent workspace root
* refactor CLAUDE.md to remove rules now in workspace root
* **remote-config:** change limit counting from per-API-key to per-account
* send GA4 conversion events for all users regardless of GCLID


### Features

* **public-api:** add feature-limits endpoint for all tiers

# 1.35.0 (2026-02-24)


### Bug Fixes

* **usermanagement:** move password min-length validation to email signup logic


### Features

* **backend:** add app.version property with Gradle resource filtering
* **backend:** add GET /api/v1/public/system/version endpoint

## 1.34.2 (2026-02-22)


### Bug Fixes

* **blog:** exclude own blog from slug uniqueness check on update

## 1.34.1 (2026-02-22)


### Bug Fixes

* stagger scheduled task startup delays to prevent liveness probe failures
* **tracking:** use v4 UUID format for Bing CAPI pageLoadId and log error response body

# 1.34.0 (2026-02-22)


### Features

* add cloud save update endpoint, days-based account lifecycle, and Bing CAPI
* **sdk:** add public SDK resources endpoint

# 1.33.0 (2026-02-21)


### Bug Fixes

* **users:** add missing deleted-status filter to cleanup query


### Features

* **crash:** add crash reporting entities
* **crash:** add repositories and MongoDB multi-tenant config
* **crash:** add request and response DTOs
* **crash:** add retention cleanup task
* **crash:** add service and controllers for crash reporting
* **crash:** add system config keys for crash report limits and retention

# 1.32.0 (2026-02-21)


### Features

* **crash:** add crash reporting feature

# 1.31.0 (2026-02-21)


### Features

* **support:** include updatedAt in ticket list response

## 1.30.1 (2026-02-20)


### Bug Fixes

* **seo:** remove auth pages from sitemap and fix blog slug truncation

# 1.30.0 (2026-02-20)


### Features

* **support:** allow anonymous ticket creation without guest email

## 1.29.2 (2026-02-20)


Maintenance release without user-facing changes.

## 1.29.1 (2026-02-20)


### Bug Fixes

* **account:** complete data export with settings, testimonials, sessions, and missing fields
* **gift-codes:** ensure isActive defaults to true on creation and allow re-creation after soft-delete
* remove erroneous googleId assignment in anonymous user creation
* **tickets:** fix createdAt 1970 timestamp and guest ticket 400 error with integration tests
* **user-logs:** remove internal accountId from UserLogResponse DTO

# 1.29.0 (2026-02-19)


### Bug Fixes

* **tracking:** disable Bing CAPI until pilot activation


### Features

* add Meta CAPI and Bing CAPI configuration properties
* add PublicCollectController for server-side tracking
* add server-side tracking feature DTOs
* implement BingConversionsClient for server-side Bing CAPI
* implement Ga4TrackingClient for server-side GA4 events
* implement MetaConversionsClient for server-side Meta CAPI
* implement TrackingDispatcherService with client stubs

## 1.28.1 (2026-02-19)


### Bug Fixes

* **seo:** consolidate domain defaults to horizon.pm

# 1.28.0 (2026-02-17)


### Features

* **seo:** add separate sitemap base URL property

# 1.27.0 (2026-02-16)


### Features

* **seo:** add dynamic sitemap.xml endpoint with blog posts

# 1.26.0 (2026-02-15)


### Features

* **blog:** add image consistency check and improve image retrieval flow

# 1.25.0 (2026-02-15)


### Features

* **blog:** add admin endpoint to retrieve blog post images

# 1.24.0 (2026-02-15)


### Features

* **blog:** expose hasImage field in blog response DTO

# 1.23.0 (2026-02-15)


### Features

* **blog:** add URL-friendly slug support for blog posts

# 1.22.0 (2026-02-15)


### Features

* **blog:** accept slug or UUID in public blog endpoints
* **blog:** add slug field to Blog entity with unique index
* **blog:** add slug field to PublicBlogResponse and BlogResponse DTOs
* **blog:** add slug finder methods to BlogRepository
* **blog:** add slug generation and lookup to BlogService
* **blog:** add startup migration to generate slugs for existing posts
* **blog:** use slug in imageUrl paths

# 1.21.0 (2026-02-14)


### Features

* **blog:** add blog image upload and serve via MongoDB GridFS

# 1.20.0 (2026-02-13)


Maintenance release without user-facing changes.

# 1.19.0 (2026-02-12)


### Features

* **auth:** grant actuator user admin role for n8n blog automation

# 1.18.0 (2026-02-11)


### Bug Fixes

* align commit workflow with frontend and document semantic-release


### Features

* add disposable email blocking and admin accounts list caching

# 1.17.0 (2026-02-09)


### Features

* **blog:** add blog management feature with admin and public endpoints

## 1.16.1 (2026-02-08)


### Bug Fixes

* move customer testimonial endpoints to /api/v1/admin/ and store gift code on entity

# 1.16.0 (2026-02-08)


### Features

* **testimonial:** add approval reward email template with gift code display
* **testimonial:** add customer DTOs and repository query methods
* **testimonial:** add customer submission and admin review endpoints
* **testimonial:** add customer submission fields and reward system config
* **testimonial:** implement submission, review, and gift code reward logic
* **testimonial:** trigger release for customer submission and review endpoints

# 1.15.0 (2026-02-04)


### Features

* enhance GA4 conversion tracking with dedicated event methods and GCLID extraction

# 1.14.0 (2026-01-30)


### Features

* add test endpoint for GA4 conversion service

# 1.13.0 (2026-01-30)


### Features

* add Google Ads conversion tracking for free account signups

## 1.12.1 (2026-01-28)


### Bug Fixes

* **security:** register DaoAuthenticationProvider for HTTP Basic auth

# 1.12.0 (2026-01-28)


### Features

* **security:** enable HTTP Basic auth for actuator/prometheus endpoint

# 1.11.0 (2026-01-28)


### Features

* allow all authenticated users to update their own GCLID

## 1.10.3 (2026-01-28)


### Bug Fixes

* add startup log message for better observability

## [Unreleased]

# 1.10.0 (2026-01-28)


### Features

* add GCLID tracking and GA4 server-side conversion events
* optimize ticket queries, improve test infrastructure, and enhance error handling
* add security headers and bulk rank calculation
* add gift code redemption cleanup task
* add caching to user feedback statistics

### Bug Fixes

* propagate account context to virtual threads in GiftCodeService
* set AccountContextHolder in GiftCodeServiceUnitTest for virtual thread context propagation

### Performance Improvements

* optimize API key fetching to reduce N+1 queries
* replace in-memory log aggregation with MongoDB aggregation pipeline
* replace in-memory statistics calculation in LeaderboardRepositoryCustomImpl
* batch user count queries in AccountUsageService
* make email sending asynchronous with @Async annotation

## 1.9.7 (2026-01-20)


### Bug Fixes

* enable Spring scheduling for scheduled tasks to run

## 1.9.6 (2025-12-14)


### Bug Fixes

* use manual JSON parsing when Stripe deserializer fails

## 1.9.5 (2025-12-14)


### Bug Fixes

* add diagnostic logging to Stripe webhook for debugging

## 1.9.4 (2025-12-14)


### Bug Fixes

* extract role from session metadata in Stripe webhook

## 1.9.3 (2025-12-14)


### Bug Fixes

* handle empty Optional in Stripe webhook account resolution

## 1.9.2 (2025-12-14)


### Bug Fixes

* allow webhook endpoints through security filter

## 1.9.1 (2025-12-09)


### Bug Fixes

* return empty response instead of 404 for missing LLM settings

# 1.9.0 (2025-12-07)


### Bug Fixes

* add missing EmailService mock in GoogleSignInServiceTest


### Features

* add server-side logging to MongoDB with rate limiting

# 1.8.0 (2025-12-07)


### Features

* add admin email notifications for new accounts and support tickets
* integrate email service into support ticket functionality

# 1.7.0 (2025-12-07)


### Features

* enhance user feedback functionality with additional fields and email verification endpoint

# 1.6.0 (2025-12-05)


### Features

* add Discord invite code retrieval and update email templates for dark mode support

# 1.5.0 (2025-12-04)


### Features

* update Google sign-in flow to include redirect URI in requests

# 1.4.0 (2025-12-04)


### Features

* add Google redirect URI configuration for OAuth integration

# 1.3.0 (2025-12-04)


### Bug Fixes

* enhance ProductService and PublicProductController tests for price and payment link functionalities


### Features

* implement Stripe price cache management with refresh and status endpoints

# 1.2.0 (2025-12-04)


### Features

* add testimonial management feature with public and admin APIs

# 1.1.0 (2025-12-04)


### Features

* add public platform statistics endpoint

# 1.0.0 (2025-12-03)


### Features

* add semantic-release automation and input validation security

# Changelog

All notable changes to this project will be documented in this file.

This file is automatically updated by [semantic-release](https://github.com/semantic-release/semantic-release).
