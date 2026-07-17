# IPCC Report Summarizer & Nigerian Language Translator

Makes IPCC climate report content accessible to non-technical readers by
generating a plain-language English summary, plus Yoruba and Hausa
translations of that summary, using Claude.

Available two ways: a command-line script and a Gradio web app, both running
the same underlying pipeline.

## Background: what is the IPCC, and why does this matter

The **Intergovernmental Panel on Climate Change (IPCC)** is the United
Nations body responsible for assessing the science of climate change. It
doesn't run its own experiments — instead, it reviews and synthesizes
thousands of existing peer-reviewed studies into periodic assessment
reports that inform government policy worldwide, including national
climate commitments and adaptation planning.

The problem this project addresses: IPCC reports are long, dense, and
written for policymakers and scientists — a Summary for Policymakers alone
can run dozens of pages of technical language. For the general public,
and especially for communities who don't read English as a first
language, that's a real access barrier to understanding climate risks
that affect them directly. Nigeria, for example, faces significant
climate exposure — flooding, shifting rainfall patterns, and coastal
risk — but Yoruba and Hausa speakers without strong English fluency have
limited direct access to what the IPCC's own findings say about it.

This project is a small step toward closing that gap: taking real IPCC
report content and making it readable in plain language, in two of
Nigeria's major languages.

## What this actually does

Give it a real IPCC report PDF (e.g. a Summary for Policymakers) and a page
range, and it will:

1. Extract the text from those pages
2. Ask Claude to produce a plain-language, jargon-free summary in English
3. Ask Claude to translate that summary into Yoruba and Hausa
4. List any technical terms that were simplified or dropped, so a reader who
   wants more detail knows what to look up

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
- **Not deployed publicly yet.** The web app (`app.py`) runs locally. It's
  built to be deployable to a free host like Hugging Face Spaces, but that
  deployment step hasn't happened yet.

## Setup

```bash
git clone https://github.com/Bayo-sb/Bayo-sb-LLM-climate-website-summarize-and-translating.git
cd Bayo-sb-LLM-climate-website-summarize-and-translating
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
# edit .env and add your own ANTHROPIC_API_KEY
```

## Usage

### Command line

```bash
# Summarize pages 1-5 of a report, print to terminal
python summarize_report.py path/to/report.pdf --pages 1-5

# Save output to a file instead
python summarize_report.py path/to/report.pdf --pages 1-5 --out summary.md
```

### Web app (local)

```bash
python app.py
```

This starts a local Gradio interface (URL printed in the terminal, typically
`http://127.0.0.1:7860`). Upload a PDF, set a page range, and click
"Generate summary" — same underlying pipeline as the CLI, with a simple
upload-and-view interface instead of flags and a terminal.

## Roadmap / what I'd do differently or next

- Deploy the web app to a free host (Hugging Face Spaces) so it's usable
  without cloning the repo
- Add OCR fallback (e.g. via a vision-capable Claude call on page images) for
  scanned reports
- Automatically chunk and summarize a full report section by section instead
  of a manual page range
- Get at least one native Yoruba and one native Hausa speaker to review
  output before treating it as deployable to a real community organization
- Add basic tests around PDF extraction edge cases (empty pages, mixed
  languages, non-Latin scripts in source PDFs)

## History

An earlier version of this project summarized only the IPCC homepage using
the OpenAI API. This version reads actual report content from PDFs and uses
Claude instead, and adds a web app on top of the original command-line
script.
