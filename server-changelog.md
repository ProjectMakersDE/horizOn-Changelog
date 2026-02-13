---
layout: default
title: Server Changelog
---

# Server Changelog

All notable changes to the horizOn Server (Backend API).

[Back to Overview](.)

# [1.18.0](https://github.com/ProjectMakersDE/horizOn-Dashboard-Backend/compare/v1.17.0...v1.18.0) (2026-02-11)


### Bug Fixes

* align commit workflow with frontend and document semantic-release ([e7f6f06](https://github.com/ProjectMakersDE/horizOn-Dashboard-Backend/commit/e7f6f0661eda064bcad781f668b45e329e2c9fac))


### Features

* add disposable email blocking and admin accounts list caching ([18ad94c](https://github.com/ProjectMakersDE/horizOn-Dashboard-Backend/commit/18ad94ca5ffc2cd716751c4a4a7224e07c25315f))

# [1.17.0](https://github.com/ProjectMakersDE/horizOn-Dashboard-Backend/compare/v1.16.1...v1.17.0) (2026-02-09)


### Features

* **blog:** add blog management feature with admin and public endpoints ([1291253](https://github.com/ProjectMakersDE/horizOn-Dashboard-Backend/commit/129125360095c096f573ee9ef58d6230614b898a))

## [1.16.1](https://github.com/ProjectMakersDE/horizOn-Dashboard-Backend/compare/v1.16.0...v1.16.1) (2026-02-08)


### Bug Fixes

* move customer testimonial endpoints to /api/v1/admin/ and store gift code on entity ([badc9f7](https://github.com/ProjectMakersDE/horizOn-Dashboard-Backend/commit/badc9f7f1acdd1f1b111b5fe0f709b8bf6744af3))

# [1.16.0](https://github.com/ProjectMakersDE/horizOn-Dashboard-Backend/compare/v1.15.0...v1.16.0) (2026-02-08)


### Features

* **testimonial:** add approval reward email template with gift code display ([e2f5eb3](https://github.com/ProjectMakersDE/horizOn-Dashboard-Backend/commit/e2f5eb30d36102c87dc1123e3e8591de1986348a))
* **testimonial:** add customer DTOs and repository query methods ([60f49c7](https://github.com/ProjectMakersDE/horizOn-Dashboard-Backend/commit/60f49c7d5d7b7e3a355f3df82db5390dd9a83518))
* **testimonial:** add customer submission and admin review endpoints ([db60837](https://github.com/ProjectMakersDE/horizOn-Dashboard-Backend/commit/db6083760953c2b03f8fdbca38b940c68cf0a95a))
* **testimonial:** add customer submission fields and reward system config ([1175bbc](https://github.com/ProjectMakersDE/horizOn-Dashboard-Backend/commit/1175bbcd21037e692ec3295afc9c224e18b5757c))
* **testimonial:** implement submission, review, and gift code reward logic ([3677308](https://github.com/ProjectMakersDE/horizOn-Dashboard-Backend/commit/36773087037f3adcaa7be7e80f2e694d6a57395b))
* **testimonial:** trigger release for customer submission and review endpoints ([1ba8bbc](https://github.com/ProjectMakersDE/horizOn-Dashboard-Backend/commit/1ba8bbc933d98f2ad89f1d8f78f5b2b5d9494931))

# [1.15.0](https://github.com/ProjectMakersDE/horizOn-Dashboard-Backend/compare/v1.14.0...v1.15.0) (2026-02-04)


### Features

* enhance GA4 conversion tracking with dedicated event methods and GCLID extraction ([a9815b5](https://github.com/ProjectMakersDE/horizOn-Dashboard-Backend/commit/a9815b5b685aff091afea0434742ee3dbe66a8d4))

# [1.14.0](https://github.com/ProjectMakersDE/horizOn-Dashboard-Backend/compare/v1.13.0...v1.14.0) (2026-01-30)


### Features

* add test endpoint for GA4 conversion service ([9bccdfc](https://github.com/ProjectMakersDE/horizOn-Dashboard-Backend/commit/9bccdfcd4e7dedbd485c8eea117a6a5fc2babb15))

# [1.13.0](https://github.com/ProjectMakersDE/horizOn-Dashboard-Backend/compare/v1.12.1...v1.13.0) (2026-01-30)


### Features

* add Google Ads conversion tracking for free account signups ([e8dae5d](https://github.com/ProjectMakersDE/horizOn-Dashboard-Backend/commit/e8dae5dbfeea1aec65ebe80e9cd7d69fff6011b1))

## [1.12.1](https://github.com/ProjectMakersDE/horizOn-Dashboard-Backend/compare/v1.12.0...v1.12.1) (2026-01-28)


### Bug Fixes

* **security:** register DaoAuthenticationProvider for HTTP Basic auth ([686ddb3](https://github.com/ProjectMakersDE/horizOn-Dashboard-Backend/commit/686ddb31a788c4bc3bbc7722b19eb0bfe928f2ed))

# [1.12.0](https://github.com/ProjectMakersDE/horizOn-Dashboard-Backend/compare/v1.11.0...v1.12.0) (2026-01-28)


### Features

* **security:** enable HTTP Basic auth for actuator/prometheus endpoint ([12a1e7d](https://github.com/ProjectMakersDE/horizOn-Dashboard-Backend/commit/12a1e7d4aee62a337cbc9de9e3a5bafcf6fea8a7))

# [1.11.0](https://github.com/ProjectMakersDE/horizOn-Dashboard-Backend/compare/v1.10.3...v1.11.0) (2026-01-28)


### Features

* allow all authenticated users to update their own GCLID ([39e1a5c](https://github.com/ProjectMakersDE/horizOn-Dashboard-Backend/commit/39e1a5cd6ec250938b38dd687ff861652a5476f0))

## [1.10.3](https://github.com/ProjectMakersDE/horizOn-Dashboard-Backend/compare/v1.10.2...v1.10.3) (2026-01-28)


### Bug Fixes

* add startup log message for better observability ([2db5a65](https://github.com/ProjectMakersDE/horizOn-Dashboard-Backend/commit/2db5a65ade67cc51c1a62c96bd5013adb8cad6d8))

# [1.10.0](https://github.com/ProjectMakersDE/horizOn-Dashboard-Backend/compare/v1.9.7...v1.10.0) (2026-01-28)


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

## [1.9.7](https://github.com/ProjectMakersDE/horizOn-Dashboard-Backend/compare/v1.9.6...v1.9.7) (2026-01-20)


### Bug Fixes

* enable Spring scheduling for scheduled tasks to run ([a661400](https://github.com/ProjectMakersDE/horizOn-Dashboard-Backend/commit/a661400794423dd4fe6f07bba4dd37d1107d01cc))

## [1.9.6](https://github.com/ProjectMakersDE/horizOn-Dashboard-Backend/compare/v1.9.5...v1.9.6) (2025-12-14)


### Bug Fixes

* use manual JSON parsing when Stripe deserializer fails ([e1fa417](https://github.com/ProjectMakersDE/horizOn-Dashboard-Backend/commit/e1fa417e030a148c6813782ff3f5ef72d99cb5be))

## [1.9.5](https://github.com/ProjectMakersDE/horizOn-Dashboard-Backend/compare/v1.9.4...v1.9.5) (2025-12-14)


### Bug Fixes

* add diagnostic logging to Stripe webhook for debugging ([7cf2c41](https://github.com/ProjectMakersDE/horizOn-Dashboard-Backend/commit/7cf2c41b3eb42d91b48f0c9d5cf251af7b6a583e))

## [1.9.4](https://github.com/ProjectMakersDE/horizOn-Dashboard-Backend/compare/v1.9.3...v1.9.4) (2025-12-14)


### Bug Fixes

* extract role from session metadata in Stripe webhook ([e1c7eb9](https://github.com/ProjectMakersDE/horizOn-Dashboard-Backend/commit/e1c7eb9629f02b6a78541ecacdb1407a87865d6f))

## [1.9.3](https://github.com/ProjectMakersDE/horizOn-Dashboard-Backend/compare/v1.9.2...v1.9.3) (2025-12-14)


### Bug Fixes

* handle empty Optional in Stripe webhook account resolution ([e9f095e](https://github.com/ProjectMakersDE/horizOn-Dashboard-Backend/commit/e9f095e644cb85d083e14f3e4c91f0e79fd2b008))

## [1.9.2](https://github.com/ProjectMakersDE/horizOn-Dashboard-Backend/compare/v1.9.1...v1.9.2) (2025-12-14)


### Bug Fixes

* allow webhook endpoints through security filter ([dd017ca](https://github.com/ProjectMakersDE/horizOn-Dashboard-Backend/commit/dd017ca5572e1fe56e6f6a20a784628e71c7bd1e))

## [1.9.1](https://github.com/ProjectMakersDE/horizOn-Dashboard-Backend/compare/v1.9.0...v1.9.1) (2025-12-09)


### Bug Fixes

* return empty response instead of 404 for missing LLM settings ([195c097](https://github.com/ProjectMakersDE/horizOn-Dashboard-Backend/commit/195c097c9df7aa1d29cf2894e0f98c193a0e71fe))
* return empty response instead of 404 for missing LLM settings ([cd23d32](https://github.com/ProjectMakersDE/horizOn-Dashboard-Backend/commit/cd23d32e45e2d0d9b52438a17a1d218c188f19a1))

# [1.9.0](https://github.com/ProjectMakersDE/horizOn-Dashboard-Backend/compare/v1.8.0...v1.9.0) (2025-12-07)


### Bug Fixes

* add missing EmailService mock in GoogleSignInServiceTest ([3d17d41](https://github.com/ProjectMakersDE/horizOn-Dashboard-Backend/commit/3d17d41abe4b08011ef554fda18f016a8e9dd486))


### Features

* add server-side logging to MongoDB with rate limiting ([75d0288](https://github.com/ProjectMakersDE/horizOn-Dashboard-Backend/commit/75d0288fd8b7ad9c07c8b82cc55246f73cea6225))

# [1.8.0](https://github.com/ProjectMakersDE/horizOn-Dashboard-Backend/compare/v1.7.0...v1.8.0) (2025-12-07)


### Features

* add admin email notifications for new accounts and support tickets ([f78095a](https://github.com/ProjectMakersDE/horizOn-Dashboard-Backend/commit/f78095a9f91045e296a36320717b2c73a959d626))
* integrate email service into support ticket functionality ([708ebe4](https://github.com/ProjectMakersDE/horizOn-Dashboard-Backend/commit/708ebe4a9b11bd9e0d4199ebf7c9145caa551903))

# [1.7.0](https://github.com/ProjectMakersDE/horizOn-Dashboard-Backend/compare/v1.6.0...v1.7.0) (2025-12-07)


### Features

* enhance user feedback functionality with additional fields and email verification endpoint ([09f8fc6](https://github.com/ProjectMakersDE/horizOn-Dashboard-Backend/commit/09f8fc69beeb178d036511ab340c22fb0d6abcf4))

# [1.6.0](https://github.com/ProjectMakersDE/horizOn-Dashboard-Backend/compare/v1.5.0...v1.6.0) (2025-12-05)


### Features

* add Discord invite code retrieval and update email templates for dark mode support ([1d236a4](https://github.com/ProjectMakersDE/horizOn-Dashboard-Backend/commit/1d236a4a3b5ca42bdd098fec490b32613d973044))

# [1.5.0](https://github.com/ProjectMakersDE/horizOn-Dashboard-Backend/compare/v1.4.0...v1.5.0) (2025-12-04)


### Features

* update Google sign-in flow to include redirect URI in requests ([d8c8506](https://github.com/ProjectMakersDE/horizOn-Dashboard-Backend/commit/d8c85069606ebf8959ec920a664dc76b0810a9b9))

# [1.4.0](https://github.com/ProjectMakersDE/horizOn-Dashboard-Backend/compare/v1.3.0...v1.4.0) (2025-12-04)


### Features

* add Google redirect URI configuration for OAuth integration ([8584549](https://github.com/ProjectMakersDE/horizOn-Dashboard-Backend/commit/8584549ab93f16580e416e6d7e33fa1c5c3f2e1a))

# [1.3.0](https://github.com/ProjectMakersDE/horizOn-Dashboard-Backend/compare/v1.2.0...v1.3.0) (2025-12-04)


### Bug Fixes

* enhance ProductService and PublicProductController tests for price and payment link functionalities ([d2dc0e0](https://github.com/ProjectMakersDE/horizOn-Dashboard-Backend/commit/d2dc0e08c3a333390c32c67691d006f9fc2f5fa3))


### Features

* implement Stripe price cache management with refresh and status endpoints ([2a5110e](https://github.com/ProjectMakersDE/horizOn-Dashboard-Backend/commit/2a5110e7235389de428d18dc494d28e2025538d8))

# [1.2.0](https://github.com/ProjectMakersDE/horizOn-Dashboard-Backend/compare/v1.1.0...v1.2.0) (2025-12-04)


### Features

* add testimonial management feature with public and admin APIs ([19548d7](https://github.com/ProjectMakersDE/horizOn-Dashboard-Backend/commit/19548d78dc71a6844159a383568940cdb1d324df))

# [1.1.0](https://github.com/ProjectMakersDE/horizOn-Dashboard-Backend/compare/v1.0.0...v1.1.0) (2025-12-04)


### Features

* add public platform statistics endpoint ([e1892bf](https://github.com/ProjectMakersDE/horizOn-Dashboard-Backend/commit/e1892bf1447d0179e8221a0b8e7e636cbc413721))

# 1.0.0 (2025-12-03)


### Features

* add semantic-release automation and input validation security ([88d1d50](https://github.com/ProjectMakersDE/horizOn-Dashboard-Backend/commit/88d1d50d764e46054f4c9317c273945a9a83fd1f))
