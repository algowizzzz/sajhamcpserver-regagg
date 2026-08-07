#!/usr/bin/env python3
"""
Seed the desk personas a bank actually staffs.

Eight desks, each with the watchlist and lens that desk really uses. Names are
drawn from companies the corpus has genuinely reported on, so a pilot user sees
their own kind of page on day one instead of an empty demo.

    python scripts/regagg_seed_desks.py --email desk@bank.test

Re-running updates the personas in place (they are versioned), so this is safe
to use to refresh a pilot environment.
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO))

from sqlalchemy import select                              # noqa: E402
from sqlalchemy.orm import sessionmaker                    # noqa: E402

from sajha.core.config import get_settings                 # noqa: E402
from sajha.db.engine import get_engine, init_db            # noqa: E402
from sajha.regagg import auth, personas as P               # noqa: E402
from sajha.regagg.models import Persona                    # noqa: E402

# ── the desks ───────────────────────────────────────────────────────────────
# Each entry is what that desk is paid to notice, expressed as scope + weights.
# serious_threshold is the line between "read this now" and "read this later";
# desks that must not miss anything sit lower, desks drowning in flow sit higher.

DESKS = [
    {
        "name": "Corporate credit — issuers",
        "lane": "news",
        "who": "Credit analyst covering a corporate issuer book.",
        "entities": """Goodfood Market Corp., consumer
WestJet, airlines
Suncor Energy, energy
CVS Health Corporation, healthcare
Chipotle Mexican Grill, consumer
Moderna, Inc., pharma
Danaher Corporation, industrials
Toyota Motor Corporation, autos
SoftBank Group Corp., conglomerate
Uber Technologies Inc., technology
Shopify Inc., technology
Telesat, telecom
Paramount Global, media
Warner Bros. Discovery, media
The Walt Disney Company, media""",
        "config": {"salience": {"topic_weights": {"credit": 75, "guidance": 45,
                                                  "operations": 35, "deal": 30,
                                                  "rates": 20},
                                "serious_threshold": 45}},
    },
    {
        "name": "Counterparty credit risk (CCR)",
        "lane": "news",
        "who": "CCR officer watching trading counterparties and their stress.",
        "entities": """Citadel LLC, hedge fund
Goldman Sachs, bank
JPMorgan Chase & Co., bank
Bank of America, bank
HSBC Holdings plc, bank
Morgan Stanley, bank
SoftBank Group Corp., conglomerate
Nomura, bank
Deutsche Bank, bank
Barclays, bank""",
        "config": {"scope": {"classes": ["hedge fund", "leveraged", "margin",
                                         "prime broker", "clearing"]},
                   "salience": {"topic_weights": {"ccr": 80, "credit": 65,
                                                  "rates": 35, "regulatory": 40},
                                "serious_threshold": 45}},
    },
    {
        "name": "Market risk — rates & macro",
        "lane": "news",
        "who": "Market risk manager sizing rate and macro exposure.",
        # No entity list: a central bank is not an obligor. "The Fed was
        # mentioned" happens every day — for this desk the exception is a
        # POLICY MOVE, so it matches on topic and escalates on corroboration.
        # A high-volume desk also needs a higher bar, or every day is red.
        "entities": "",
        "config": {"scope": {"topics": ["rates"],
                             "classes": ["rate cut", "rate hike", "rate decision",
                                         "inflation", "yield", "intervention",
                                         "quantitative", "recession"]},
                   "salience": {"topic_weights": {"rates": 85, "regulatory": 40,
                                                  "credit": 35, "general": 10},
                                "serious_threshold": 100}},
    },
    {
        "name": "FX desk",
        "lane": "news",
        "who": "FX trader watching currency-moving policy and flows.",
        "entities": "",
        "config": {"scope": {"topics": ["rates"],
                             "classes": ["yen", "dollar", "euro", "sterling",
                                         "currency", "intervention", "peg",
                                         "tariff", "trade war", "devalu"]},
                   "salience": {"topic_weights": {"rates": 80, "regulatory": 35,
                                                  "deal": 15, "general": 10},
                                "serious_threshold": 95}},
    },
    {
        "name": "Equity desk",
        "lane": "news",
        "who": "Equity trader following large-cap names and earnings moves.",
        "entities": """SpaceX, technology
Palantir Technologies, technology
Advanced Micro Devices, Inc., semiconductors
Meta Platforms, Inc., technology
Alphabet Inc., technology
Apple Inc., technology
Amazon.com, Inc., technology
Shopify Inc., technology
Uber Technologies Inc., technology
The Walt Disney Company, media
Paramount Global, media
Warner Bros. Discovery, media
Moderna, Inc., pharma
Chipotle Mexican Grill, consumer
Toyota Motor Corporation, autos""",
        "config": {"salience": {"topic_weights": {"guidance": 70, "deal": 60,
                                                  "credit": 45, "rates": 30},
                                "serious_threshold": 55}},
    },
    {
        "name": "Underwriting & origination",
        "lane": "news",
        "who": "Underwriter pricing new credit — deals, financing, issuance.",
        "entities": """SpaceX, technology
Palantir Technologies, technology
Manipal Health Enterprises, healthcare
DLF Limited, real estate
Life Insurance Corporation of India, insurance
Milky Mist Dairy, consumer
Circle Internet Financial, LLC, fintech
Global Payments Inc., payments
SEI Investments Company, asset management
Willis Towers Watson, insurance""",
        "config": {"salience": {"topic_weights": {"deal": 80, "credit": 60,
                                                  "guidance": 45, "rates": 35},
                                "serious_threshold": 55}},
    },
    {
        "name": "Real estate sector",
        "lane": "news",
        "who": "Sector analyst on real estate and construction exposure.",
        "entities": """RioCan Real Estate Investment Trust, reit
DLF Limited, real estate
Brookfield, real estate
Oxford Properties, real estate
Cadillac Fairview, real estate""",
        "config": {"scope": {"classes": ["housing", "mortgage", "property",
                                         "real estate", "construction",
                                         "commercial real estate", "rent"]},
                   "salience": {"topic_weights": {"credit": 65, "rates": 55,
                                                  "deal": 45, "guidance": 35},
                                "serious_threshold": 45}},
    },
    {
        "name": "Hedge funds & financial institutions",
        "lane": "news",
        "who": "FI analyst covering banks, funds and payment institutions.",
        "entities": """Citadel LLC, hedge fund
JPMorgan Chase & Co., bank
Goldman Sachs, bank
Bank of America, bank
HSBC Holdings plc, bank
Visa Inc., payments
Global Payments Inc., payments
Circle Internet Financial, LLC, fintech
SEI Investments Company, asset management
BioCatch, fintech
Upstart, fintech
Life Insurance Corporation of India, insurance""",
        "config": {"scope": {"classes": ["hedge fund", "bank", "lender",
                                         "asset manager", "insurer"]},
                   "salience": {"topic_weights": {"ccr": 70, "credit": 65,
                                                  "regulatory": 55, "deal": 40},
                                "serious_threshold": 50}},
    },
    {
        "name": "Prudential rules owner",
        "lane": "regulatory",
        "who": "Owns the capital and AML rule families the bank runs on.",
        "entities": "",
        "config": {"scope": {"rule_families": ["osfi-car", "b-13", "fincen-aml",
                                               "basel", "sa-ccr"],
                             "regions": ["Canada", "United States"]},
                   "salience": {"topic_weights": {"regulatory": 80, "credit": 45},
                                "serious_threshold": 45}},
    },
]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--email", default="desk@bank.test")
    ap.add_argument("--password", default="pilot-desk-2026")
    args = ap.parse_args()

    init_db(get_settings())
    session = sessionmaker(bind=get_engine(), expire_on_commit=False)()

    user = auth.find_user(session, args.email)
    if user is None:
        user, err = auth.create_user(session, args.email, args.password,
                                     "Desk Pilot")
        if err:
            print(f"could not create {args.email}: {err}")
            return 1
        print(f"created user {args.email}")
    else:
        print(f"using existing user {args.email}")

    existing = {p.name: p for p in session.scalars(
        select(Persona).where(Persona.owner_id == user.user_id)).all()}

    for desk in DESKS:
        entities = P.parse_entities(desk["entities"])
        p = P.save_persona(
            session, owner_id=user.user_id, name=desk["name"], lane=desk["lane"],
            config=desk["config"], entities=entities,
            persona_id=existing[desk["name"]].persona_id
            if desk["name"] in existing else None)
        d = P.persona_dict(session, p)
        print(f"  {desk['name']:38s} {d['lane']:11s} "
              f"{d['entity_count']:>3d} names  {d['layout']}")
    print(f"\n{len(DESKS)} desks ready for {args.email}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
