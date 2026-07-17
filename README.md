# IPCC Report Summarizer & Nigerian Language Translator

Makes IPCC climate report content accessible to non-technical readers by
generating a plain-language English summary, plus Yoruba and Hausa
translations of that summary, using Claude.

## What this actually does

Give it a real IPCC report PDF (e.g. a Summary for Policymakers) and a page
range, and it will:

1. Extract the text from those pages
2. Ask Claude to produce a plain-language, jargon-free summary in English
3. Ask Claude to translate that summary into Yoruba and Hausa
4. List any technical terms that were simplified or dropped, so a reader who
   wants more detail knows what to look up

Output is a clean Markdown file with all three summaries side by side.

## What this does NOT do (yet)

Being upfront about current limitations rather than overstating scope:

- **No OCR.** If the PDF is scanned/image-based rather than text-based, this
  will fail with a clear error rather than silently returning nothing.
- **No native-speaker validation.** The Yoruba and Hausa outputs are machine
  translations from Claude. They have not been reviewed by a native speaker
  for accuracy, tone, or regional dialect appropriateness. Treat this as a
  first draft, not a final community-facing document, until that review
  happens.
- **Single-excerpt at a time.** It doesn't yet process a whole multi-hundred
  page report automatically — you choose a page range per run. Chunking a
  full report into sections is on the roadmap below.
- **No web interface yet.** This is a command-line tool. A simple web UI is
  possible but not built.

## Setup

```bash
git clone https://github.com/Bayo-sb/<repo-name>.git
cd <repo-name>
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
# edit .env and add your own ANTHROPIC_API_KEY
```

## Usage

```bash
# Summarize the first 5 pages of a report, print to terminal
python summarize_report.py path/to/report.pdf --pages 1-5

# Save output to a file instead
python summarize_report.py path/to/report.pdf --pages 1-5 --out summary.md
```

## Roadmap / what I'd do differently or next

- Add OCR fallback (e.g. via a vision-capable Claude call on page images) for
  scanned reports
- Automatically chunk and summarize a full report section by section instead
  of a manual page range
- Get at least one native Yoruba and one native Hausa speaker to review
  output before treating it as deployable to a real community organization
- Add a minimal web interface so non-technical users aren't running a CLI
- Add basic tests around PDF extraction edge cases (empty pages, mixed
  languages, non-Latin scripts in source PDFs)

## History

An earlier version of this project summarized only the IPCC homepage using
the OpenAI API. This version reads actual report content from PDFs and uses
Claude instead.
