---
layout: default
title: Server Changelog
---

# Server Changelog

All notable changes to the horizOn Server (Backend API).

[Back to Overview](.)

# [1.38.0](https://github.com/ProjectMakersDE/horizOn-Server/compare/v1.37.0...v1.38.0) (2026-03-06)


### Features

* add comparison pages to sitemap and improve index management ([213cb3d](https://github.com/ProjectMakersDE/horizOn-Server/commit/213cb3dcc26bbd9133a80412edb846e5984b555c))

# [1.37.0](https://github.com/ProjectMakersDE/horizOn-Server/compare/v1.36.2...v1.37.0) (2026-03-06)


### Features

* add cached EUR/USD exchange rate endpoint ([ebf28ee](https://github.com/ProjectMakersDE/horizOn-Server/commit/ebf28ee57988ebb7260e1fd1bc9aa42b11870214))

## [1.36.2](https://github.com/ProjectMakersDE/horizOn-Server/compare/v1.36.1...v1.36.2) (2026-03-01)


### Bug Fixes

* return 404 instead of 500 for NotFoundException and fix BrotliCompressionFilter order ([655984d](https://github.com/ProjectMakersDE/horizOn-Server/commit/655984d77f872f2f91f0842f05aa94da892808ec))

## [1.36.1](https://github.com/ProjectMakersDE/horizOn-Server/compare/v1.36.0...v1.36.1) (2026-02-27)


### Bug Fixes

* pass release version to Docker build for correct /version endpoint ([59c0c0a](https://github.com/ProjectMakersDE/horizOn-Server/commit/59c0c0a31735af8b44335f01b2a962e92f23e8c5))

# [1.36.0](https://github.com/ProjectMakersDE/horizOn-Server/compare/v1.35.0...v1.36.0) (2026-02-27)


### Bug Fixes

* move commit command to parent workspace root ([3cab16d](https://github.com/ProjectMakersDE/horizOn-Server/commit/3cab16d313f52856fa7d335cf97b1d0a7e3d2ce9))
* refactor CLAUDE.md to remove rules now in workspace root ([3b23cb5](https://github.com/ProjectMakersDE/horizOn-Server/commit/3b23cb570b996f5fa73639ae9768e2d1571b5de5))
* **remote-config:** change limit counting from per-API-key to per-account ([1dbbcb1](https://github.com/ProjectMakersDE/horizOn-Server/commit/1dbbcb12676c4a54bc44157d49a2ef3172e48b01))
* send GA4 conversion events for all users regardless of GCLID ([921ec4a](https://github.com/ProjectMakersDE/horizOn-Server/commit/921ec4a7bd1a3d5872d9fd2f3defa78bfee045f3))
* **test:** update GoogleAdsConversion tests for always-send behavior ([d21d202](https://github.com/ProjectMakersDE/horizOn-Server/commit/d21d2020d3a2a29501f29f2fc8152afbcab0c4cc))


### Features

* **public-api:** add feature-limits endpoint for all tiers ([d33d3ca](https://github.com/ProjectMakersDE/horizOn-Server/commit/d33d3ca0300459b0ef456fae62a6c8506582176f))

# [1.35.0](https://github.com/ProjectMakersDE/horizOn-Server/compare/v1.34.2...v1.35.0) (2026-02-24)


### Bug Fixes

* **usermanagement:** move password min-length validation to email signup logic ([b8b8530](https://github.com/ProjectMakersDE/horizOn-Server/commit/b8b8530b0d872eb38b54522e2373737f314bbfd2))


### Features

* **backend:** add app.version property with Gradle resource filtering ([9a85479](https://github.com/ProjectMakersDE/horizOn-Server/commit/9a854794827d4bf72c16624d3c08708e656d32c2))
* **backend:** add GET /api/v1/public/system/version endpoint ([fd291cb](https://github.com/ProjectMakersDE/horizOn-Server/commit/fd291cb5587fbc4a192e86ad553567ffa8b133a2))

## [1.34.2](https://github.com/ProjectMakersDE/horizOn-Server/compare/v1.34.1...v1.34.2) (2026-02-22)


### Bug Fixes

* **blog:** exclude own blog from slug uniqueness check on update ([5227109](https://github.com/ProjectMakersDE/horizOn-Server/commit/522710942bc7b9b6c9613b7cabf631162b665e84))

## [1.34.1](https://github.com/ProjectMakersDE/horizOn-Server/compare/v1.34.0...v1.34.1) (2026-02-22)


### Bug Fixes

* stagger scheduled task startup delays to prevent liveness probe failures ([ad44e58](https://github.com/ProjectMakersDE/horizOn-Server/commit/ad44e58474a2c801319a8165aa4e393473c8ab8a))
* **tracking:** use v4 UUID format for Bing CAPI pageLoadId and log error response body ([0f74912](https://github.com/ProjectMakersDE/horizOn-Server/commit/0f74912fbc05e83eb270f5261ad0486008b70b67))

# [1.34.0](https://github.com/ProjectMakersDE/horizOn-Server/compare/v1.33.0...v1.34.0) (2026-02-22)


### Features

* add cloud save update endpoint, days-based account lifecycle, and Bing CAPI ([4e1b49d](https://github.com/ProjectMakersDE/horizOn-Server/commit/4e1b49de5beb7dd6e2798e0f2f7d5ce3b2914b3d))
* **sdk:** add public SDK resources endpoint ([d9ab477](https://github.com/ProjectMakersDE/horizOn-Server/commit/d9ab477f383fd10867931d36388aa8bfcc44fca8))

# [1.33.0](https://github.com/ProjectMakersDE/horizOn-Dashboard-Backend/compare/v1.32.0...v1.33.0) (2026-02-21)


### Bug Fixes

* **users:** add missing deleted-status filter to cleanup query ([03d8013](https://github.com/ProjectMakersDE/horizOn-Dashboard-Backend/commit/03d80130f2c579ac87370bbe7950136d7909a3a5))


### Features

* **crash:** add crash reporting entities ([7d401d9](https://github.com/ProjectMakersDE/horizOn-Dashboard-Backend/commit/7d401d9f50eb8b661c2735dc0192c8d662973640))
* **crash:** add repositories and MongoDB multi-tenant config ([17a7127](https://github.com/ProjectMakersDE/horizOn-Dashboard-Backend/commit/17a7127660444c2f5b28abb5d92e78e1417031a9))
* **crash:** add request and response DTOs ([862cb8a](https://github.com/ProjectMakersDE/horizOn-Dashboard-Backend/commit/862cb8a59a24874c4f53f76e3d24b8d333ebd575))
* **crash:** add retention cleanup task ([39410ba](https://github.com/ProjectMakersDE/horizOn-Dashboard-Backend/commit/39410ba780c9e951053dec81e08a39a7d1c6088c))
* **crash:** add service and controllers for crash reporting ([f3944fa](https://github.com/ProjectMakersDE/horizOn-Dashboard-Backend/commit/f3944fab9cfd8979b4037b1ca4bc5e13cbd19e2f))
* **crash:** add system config keys for crash report limits and retention ([cbd37b8](https://github.com/ProjectMakersDE/horizOn-Dashboard-Backend/commit/cbd37b8d4b511dbb79484e7cbcd1ba27603670ba))

# [1.32.0](https://github.com/ProjectMakersDE/horizOn-Dashboard-Backend/compare/v1.31.0...v1.32.0) (2026-02-21)


### Features

* **crash:** add crash reporting feature ([#20](https://github.com/ProjectMakersDE/horizOn-Dashboard-Backend/issues/20)) ([73db18a](https://github.com/ProjectMakersDE/horizOn-Dashboard-Backend/commit/73db18ab4b511513d84147276183a170d473f014))

# [1.31.0](https://github.com/ProjectMakersDE/horizOn-Dashboard-Backend/compare/v1.30.1...v1.31.0) (2026-02-21)


### Features

* **support:** include updatedAt in ticket list response ([860d2da](https://github.com/ProjectMakersDE/horizOn-Dashboard-Backend/commit/860d2da65b03670d0c8b0df11026fde168dc0eac))

## [1.30.1](https://github.com/ProjectMakersDE/horizOn-Dashboard-Backend/compare/v1.30.0...v1.30.1) (2026-02-20)


### Bug Fixes

* **seo:** remove auth pages from sitemap and fix blog slug truncation ([4a2196b](https://github.com/ProjectMakersDE/horizOn-Dashboard-Backend/commit/4a2196bdd1bfaecf89e4fb73862b7a6de0bd109a))

# [1.30.0](https://github.com/ProjectMakersDE/horizOn-Dashboard-Backend/compare/v1.29.2...v1.30.0) (2026-02-20)


### Features

* **support:** allow anonymous ticket creation without guest email ([98e8100](https://github.com/ProjectMakersDE/horizOn-Dashboard-Backend/commit/98e8100c4d715f1c57b8d5808f31afa3c754acda))

## [1.29.2](https://github.com/ProjectMakersDE/horizOn-Dashboard-Backend/compare/v1.29.1...v1.29.2) (2026-02-20)


### Bug Fixes

* **ci:** enforce clean commit message policy in project guidelines ([b369a2e](https://github.com/ProjectMakersDE/horizOn-Dashboard-Backend/commit/b369a2e89e1f5bcffafc22df30fe2da9d666dc3f))

## [1.29.1](https://github.com/ProjectMakersDE/horizOn-Dashboard-Backend/compare/v1.29.0...v1.29.1) (2026-02-20)


### Bug Fixes

* **account:** complete data export with settings, testimonials, sessions, and missing fields ([44eddea](https://github.com/ProjectMakersDE/horizOn-Dashboard-Backend/commit/44eddea5beef6af3d2ee16e0e4c0b02bed52d9fe))
* **gift-codes:** ensure isActive defaults to true on creation and allow re-creation after soft-delete ([bbb3b06](https://github.com/ProjectMakersDE/horizOn-Dashboard-Backend/commit/bbb3b06292464043bc0c5d30509cc514ff5b353b))
* remove erroneous googleId assignment in anonymous user creation ([6e825cb](https://github.com/ProjectMakersDE/horizOn-Dashboard-Backend/commit/6e825cb889a0fbcef6d2d9f93ecd99883b6477fa))
* **tickets:** fix createdAt 1970 timestamp and guest ticket 400 error with integration tests ([9f2a85a](https://github.com/ProjectMakersDE/horizOn-Dashboard-Backend/commit/9f2a85a7379bf489ef13279ab8d606417e3f51a7))
* **user-logs:** remove internal accountId from UserLogResponse DTO ([bbbd220](https://github.com/ProjectMakersDE/horizOn-Dashboard-Backend/commit/bbbd220b4000e08576726d63d899aea1365d0dfd))

# [1.29.0](https://github.com/ProjectMakersDE/horizOn-Dashboard-Backend/compare/v1.28.1...v1.29.0) (2026-02-19)


### Bug Fixes

* **tracking:** disable Bing CAPI until pilot activation ([75e5dca](https://github.com/ProjectMakersDE/horizOn-Dashboard-Backend/commit/75e5dcaa13f9d8884c78b8d73bbca717bf4d9f14))


### Features

* add Meta CAPI and Bing CAPI configuration properties ([568b481](https://github.com/ProjectMakersDE/horizOn-Dashboard-Backend/commit/568b4810432846f9fb7dc1d4da2896c07195bda4))
* add PublicCollectController for server-side tracking ([4309d06](https://github.com/ProjectMakersDE/horizOn-Dashboard-Backend/commit/4309d0627fccad68b07e9ac85c544252d0bb3a2e))
* add server-side tracking feature DTOs ([ef0fc39](https://github.com/ProjectMakersDE/horizOn-Dashboard-Backend/commit/ef0fc393133a8ef4eec324edd770b7e93a2dd491))
* implement BingConversionsClient for server-side Bing CAPI ([6d17af7](https://github.com/ProjectMakersDE/horizOn-Dashboard-Backend/commit/6d17af7de4e7850f48530d9d1b5b26d860f57b3f))
* implement Ga4TrackingClient for server-side GA4 events ([6b32e78](https://github.com/ProjectMakersDE/horizOn-Dashboard-Backend/commit/6b32e780cddbf97c53bdda1b974f95836b17195b))
* implement MetaConversionsClient for server-side Meta CAPI ([e12adb5](https://github.com/ProjectMakersDE/horizOn-Dashboard-Backend/commit/e12adb5e8a28147852e03b97d2a6ef0d28269bf7))
* implement TrackingDispatcherService with client stubs ([6a32017](https://github.com/ProjectMakersDE/horizOn-Dashboard-Backend/commit/6a32017d388dab6a73fba9eca5c4da99f1fc9b24))

## [1.28.1](https://github.com/ProjectMakersDE/horizOn-Dashboard-Backend/compare/v1.28.0...v1.28.1) (2026-02-19)


### Bug Fixes

* **seo:** consolidate domain defaults to horizon.pm ([#19](https://github.com/ProjectMakersDE/horizOn-Dashboard-Backend/issues/19)) ([edc3c06](https://github.com/ProjectMakersDE/horizOn-Dashboard-Backend/commit/edc3c0663f6028902ed41d373ac386007c59598d))

# [1.28.0](https://github.com/ProjectMakersDE/horizOn-Dashboard-Backend/compare/v1.27.0...v1.28.0) (2026-02-17)


### Features

* **seo:** add separate sitemap base URL property ([47dd0c6](https://github.com/ProjectMakersDE/horizOn-Dashboard-Backend/commit/47dd0c60f52ddf1513daae08ea554446a2ab4a8f))

# [1.27.0](https://github.com/ProjectMakersDE/horizOn-Dashboard-Backend/compare/v1.26.0...v1.27.0) (2026-02-16)


### Features

* **seo:** add dynamic sitemap.xml endpoint with blog posts ([5ec6a94](https://github.com/ProjectMakersDE/horizOn-Dashboard-Backend/commit/5ec6a942e8a0f0d852aba68a82a4991c361bde21))

# [1.26.0](https://github.com/ProjectMakersDE/horizOn-Dashboard-Backend/compare/v1.25.0...v1.26.0) (2026-02-15)


### Features

* **blog:** add image consistency check and improve image retrieval flow ([d0f2a8e](https://github.com/ProjectMakersDE/horizOn-Dashboard-Backend/commit/d0f2a8e530ac329f9963b358254bcb1871816383))

# [1.25.0](https://github.com/ProjectMakersDE/horizOn-Dashboard-Backend/compare/v1.24.0...v1.25.0) (2026-02-15)


### Features

* **blog:** add admin endpoint to retrieve blog post images ([2f614b0](https://github.com/ProjectMakersDE/horizOn-Dashboard-Backend/commit/2f614b0c34e5b942a3e74de489a2c293edb8557c))

# [1.24.0](https://github.com/ProjectMakersDE/horizOn-Dashboard-Backend/compare/v1.23.0...v1.24.0) (2026-02-15)


### Features

* **blog:** expose hasImage field in blog response DTO ([ac50f91](https://github.com/ProjectMakersDE/horizOn-Dashboard-Backend/commit/ac50f91fc8ca434285d23e6b4eb61c84227dacbc))

# [1.23.0](https://github.com/ProjectMakersDE/horizOn-Dashboard-Backend/compare/v1.22.0...v1.23.0) (2026-02-15)


### Features

* **blog:** add URL-friendly slug support for blog posts ([ba7eb3d](https://github.com/ProjectMakersDE/horizOn-Dashboard-Backend/commit/ba7eb3d7421eb6a52dc86883f6af0da9c1aa1fcf))

# [1.22.0](https://github.com/ProjectMakersDE/horizOn-Dashboard-Backend/compare/v1.21.0...v1.22.0) (2026-02-15)


### Features

* **blog:** accept slug or UUID in public blog endpoints ([9567684](https://github.com/ProjectMakersDE/horizOn-Dashboard-Backend/commit/95676846b9b3d003275f979a396f1ee254831c8e))
* **blog:** add slug field to Blog entity with unique index ([05eabf7](https://github.com/ProjectMakersDE/horizOn-Dashboard-Backend/commit/05eabf7eb6ecf8a49f2511bbec56d84f1b336a91))
* **blog:** add slug field to PublicBlogResponse and BlogResponse DTOs ([8b96fc7](https://github.com/ProjectMakersDE/horizOn-Dashboard-Backend/commit/8b96fc706df3b69fac9c69c9c87e139f15f164b6))
* **blog:** add slug finder methods to BlogRepository ([88a07b6](https://github.com/ProjectMakersDE/horizOn-Dashboard-Backend/commit/88a07b6f8ad5d91abd04f82942de7a5867fd134c))
* **blog:** add slug generation and lookup to BlogService ([724a95d](https://github.com/ProjectMakersDE/horizOn-Dashboard-Backend/commit/724a95dd3841770a9d7e0fa0e22ebd6d58151d4e))
* **blog:** add startup migration to generate slugs for existing posts ([0846ab4](https://github.com/ProjectMakersDE/horizOn-Dashboard-Backend/commit/0846ab464b9e355ecde5e3cf63b1b2387d9c73e2))
* **blog:** use slug in imageUrl paths ([ef5d9d2](https://github.com/ProjectMakersDE/horizOn-Dashboard-Backend/commit/ef5d9d2a8bbbe093263a319099b79c05451370bc))

# [1.21.0](https://github.com/ProjectMakersDE/horizOn-Dashboard-Backend/compare/v1.20.0...v1.21.0) (2026-02-14)


### Features

* **blog:** add blog image upload and serve via MongoDB GridFS ([4afc5b9](https://github.com/ProjectMakersDE/horizOn-Dashboard-Backend/commit/4afc5b9811c2073a861ff9796efac5caf0116727))

# [1.20.0](https://github.com/ProjectMakersDE/horizOn-Dashboard-Backend/compare/v1.19.0...v1.20.0) (2026-02-13)


### Features

* **ci:** trigger changelog sync after new release ([d9d3bac](https://github.com/ProjectMakersDE/horizOn-Dashboard-Backend/commit/d9d3bacac33328bb89bd42c7d2dc19cb25b6d5bc))

# [1.19.0](https://github.com/ProjectMakersDE/horizOn-Dashboard-Backend/compare/v1.18.0...v1.19.0) (2026-02-12)


### Features

* **auth:** grant actuator user admin role for n8n blog automation ([7667858](https://github.com/ProjectMakersDE/horizOn-Dashboard-Backend/commit/7667858c51423053472376817fc6a03ca6e96047))

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

## [Unreleased]

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

### Refactoring

* split large SupportTicketService into focused services
* remove redundant EmailManager wrapper class
* refactor to constructor injection and remove field injection
* standardize documentation language
* secure Spring Boot Actuator endpoints
* remove hardcoded secrets from configuration files

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

# Changelog

All notable changes to this project will be documented in this file.

This file is automatically updated by [semantic-release](https://github.com/semantic-release/semantic-release).
