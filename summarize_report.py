"""
IPCC Report Summarizer & Translator (Yoruba / Hausa)
-----------------------------------------------------
Takes an actual IPCC report PDF (e.g. a Summary for Policymakers) and produces:
  1. A plain-language English summary for a non-technical, general adult reader
  2. A Yoruba translation of that summary
  3. A Hausa translation of that summary

This replaces an earlier version of this project that only summarized the
IPCC homepage. This version reads real report content directly from a PDF.

Usage:
    python summarize_report.py path/to/report.pdf
    python summarize_report.py path/to/report.pdf --pages 1-5
    python summarize_report.py path/to/report.pdf --out summary.md

Requirements:
    pip install -r requirements.txt
    Set ANTHROPIC_API_KEY in your environment or a .env file (see .env.example)
"""

import argparse
import os
import sys

from dotenv import load_dotenv
from pypdf import PdfReader
from anthropic import Anthropic

load_dotenv()

MODEL = "claude-sonnet-5"
MAX_CHARS = 12000  # keep the excerpt within a reasonable prompt size


def extract_pdf_text(pdf_path: str, page_range: str | None = None) -> str:
    """Extract text from a PDF, optionally limited to a page range like '1-5'."""
    reader = PdfReader(pdf_path)
    total_pages = len(reader.pages)

    if page_range:
        start, end = page_range.split("-")
        start, end = int(start) - 1, int(end)
        start = max(start, 0)
        end = min(end, total_pages)
    else:
        start, end = 0, total_pages

    text_parts = []
    for i in range(start, end):
        page_text = reader.pages[i].extract_text() or ""
        text_parts.append(page_text)

    full_text = "\n".join(text_parts).strip()

    if not full_text:
        raise ValueError(
            "No extractable text found in the given page range. "
            "This PDF may be scanned/image-based and would need OCR first."
        )

    return full_text[:MAX_CHARS]


def generate_summary(client: Anthropic, report_excerpt: str) -> dict:
    """Call Claude to produce an English plain-language summary plus
    Yoruba and Hausa translations of that same summary."""

    prompt = f"""You are helping a community organization make an IPCC climate
report excerpt accessible to non-technical residents who are not scientists.

Given the excerpt below, respond ONLY with a JSON object (no markdown fences,
no preamble) with exactly these keys:

- "english": a plain-language summary in 4-6 sentences, no jargon, aimed at a
  general adult reader with no science background
- "yoruba": a Yoruba translation of that same plain-language summary
- "hausa": a Hausa translation of that same plain-language summary
- "key_terms": a short list (3-5 items) of any technical terms from the
  excerpt that were simplified or omitted, so a reader can look them up if
  they want more detail

Report excerpt:
{report_excerpt}
"""

    response = client.messages.create(
        model=MODEL,
        max_tokens=1500,
        messages=[{"role": "user", "content": prompt}],
    )

    text_block = next((b.text for b in response.content if b.type == "text"), "{}")

    import json

    cleaned = text_block.strip().removeprefix("```json").removesuffix("```").strip()
    return json.loads(cleaned)


def format_output(result: dict, source_file: str) -> str:
    return f"""# Climate Report Summary

*Source: {os.path.basename(source_file)}*
*Generated with Claude — machine translation, not reviewed by a native speaker. See README for validation status.*

## Plain-Language Summary (English)

{result.get('english', '')}

---

## Yoruba Summary

{result.get('yoruba', '')}

---

## Hausa Summary

{result.get('hausa', '')}

---

## Terms Simplified or Omitted

{chr(10).join('- ' + t for t in result.get('key_terms', []))}
"""


def main():
    parser = argparse.ArgumentParser(description="Summarize and translate an IPCC report excerpt.")
    parser.add_argument("pdf_path", help="Path to the IPCC report PDF")
    parser.add_argument("--pages", help="Page range to read, e.g. '1-5' (default: whole doc, capped by length)")
    parser.add_argument("--out", default=None, help="Output markdown file (default: prints to stdout)")
    args = parser.parse_args()

    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        print("ERROR: Set ANTHROPIC_API_KEY in your environment or a .env file.", file=sys.stderr)
        sys.exit(1)

    client = Anthropic(api_key=api_key)

    print(f"Reading {args.pdf_path}...", file=sys.stderr)
    excerpt = extract_pdf_text(args.pdf_path, args.pages)

    print("Generating summary and translations with Claude...", file=sys.stderr)
    result = generate_summary(client, excerpt)

    output = format_output(result, args.pdf_path)

    if args.out:
        with open(args.out, "w", encoding="utf-8") as f:
            f.write(output)
        print(f"Written to {args.out}", file=sys.stderr)
    else:
        print(output)


if __name__ == "__main__":
    main()
