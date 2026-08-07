# Ship execution log

## Sprint S1 — Identity & Personas ✅ COMPLETE

| Story | Status | Evidence |
|---|---|---|
| S1.1 users + signup/login/logout | done | `sajha/regagg/auth.py`; scrypt + HMAC session cookie |
| S1.2 personas + entities + versioning | done | `sajha/regagg/personas.py`; JSONFlex config, indexed entities |
| S1.3 auth + persona API | done | `/auth/*`, `/personas*` in `admin.py` |
| S1.4 login gate + Personas tab UI | done | `ui_dashboard.html` |
| S1.5 Playwright harness + suites | done | `tests/ui/` — 22 specs green |

**Tests: 118 pytest + 22 Playwright, all green.**

### Bugs found and fixed this sprint (all by the new tests)

1. **Mapper collision** — a second class named `User` on the shared declarative
   Base broke string relationship resolution for *every* model (500s across the
   app). Renamed to `RegUser`; table name unchanged.
2. **DB pool exhaustion (production-breaking)** — thread-scoped sessions pinned
   one pooled connection per threadpool thread forever; FastAPI's threadpool is
   larger than the pool, so the server wedged for 30s per request under load.
   Fixed with contextvar-scoped sessions released per request + a pool sized to
   the concurrency. Runtime for the suite: 2.2m → 59s, pool errors 27 → 0.
4. **Auth error messages swallowed** — the host app rewrites 4xx bodies, so
   "Email or password is incorrect" never reached the user. Expected user
   outcomes now return 200 with `ok:false` and a message.
5. **Deep links raced the data load** — setting a `<select>` before the options
   existed silently did nothing, so "Financial News" showed the whole corpus.
   Boot now resolves a READY promise the jumps await.
6. **Hash deep-links ignored after login, and the app fought its own hash** —
   added `hashchange` routing plus a guard so the app's own updates don't
   re-route (which was resetting the lane from news to regulatory).
7. **Lane-blind deep links returned 0 rows** — "Financial News" + regulatory
   scope intersect to nothing; jumps now carry their lane, and Home's band
   chart pins the regulatory lane.
8. **No fetch timeout or retry** — one slow first response left every panel on
   "loading…" forever. Fetches now have a deadline and one retry; a failed
   first load is surfaced instead of swallowed behind the sign-in screen.

## Next: Sprint S2 — extraction & distillation (needs ANTHROPIC_API_KEY)
