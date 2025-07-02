# IPCC Web Summarizer & Nigerian Language Translator

## Project Overview

`IPCC-Web-Summarizer-Naija-Lang` is a Python-based project designed to make crucial climate change information from the Intergovernmental Panel on Climate Change (IPCC) website more accessible. It achieves this by:

1.  Web scraping the main content of the IPCC homepage.
2.  Utilizing a Large Language Model (LLM) to generate a concise summary of the website's purpose, activities, and recent news in English.
3.  Translating this English summary into two major Nigerian languages: Yoruba and Hausa, leveraging the LLM's multilingual capabilities.

This tool aims to bridge language barriers and disseminate vital climate science information to broader audiences in Nigeria.

## Key Features

* **Web Scraping:** Fetches and cleans content from specified URLs (currently IPCC homepage).
* **LLM-Powered Summarization:** Generates concise summaries of complex web content in English.
* **Multilingual Translation:** Translates the summaries into Yoruba and Hausa.
* **User-Agent Handling:** Includes a `User-Agent` header for robust web scraping.
* **OpenAI API Integration:** Uses the OpenAI API (GPT-4o-mini) for LLM functionalities.
* **Markdown Output:** Presents summaries in a clean, readable Markdown format.

## How It Works (High-Level)

1.  **Initialization:** Sets up the OpenAI API client and loads the API key from environment variables.
2.  **Web Scraping:** The `Website` class fetches the HTML content of the target URL, extracts the page title, and cleans the main text by removing scripts, styles, and other irrelevant tags.
3.  **Prompt Construction:** A user prompt is constructed, feeding the scraped website content to the LLM. A system prompt guides the LLM to act as a Climate assistant, summarize in English, and then translate into Yoruba and Hausa, ignoring navigation text.
4.  **LLM Inference:** The combined prompts are sent to the OpenAI `gpt-4o-mini` model.
5.  **Output:** The LLM returns the multilingual summary in Markdown format, which is then displayed.

## Setup Instructions

To run this project, you'll need Python installed, along with the required libraries and an OpenAI API key.

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/Bayo-sb/IPCC-Web-Summarizer-Naija-Lang.git](https://github.com/Bayo-sb/IPCC-Web-Summarizer-Naija-Lang.git)
    cd IPCC-Web-Summarizer-Naija-Lang
    ```
2.  **Install Python dependencies:**
    It's recommended to use a virtual environment.
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: `venv\Scripts\activate`
    pip install -r requirements.txt
    ```
    (You will need to create a `requirements.txt` file containing the following:
    ```
    requests
    beautifulsoup4
    python-dotenv
    openai
    ipython # if running in Jupyter/Colab
    ```
    )

3.  **Set up OpenAI API Key:**
    * Obtain an API key from [OpenAI](https://platform.openai.com/account/api-keys).
    * Create a `.env` file in the project's root directory.
    * Add your API key to the `.env` file:
        ```
        OPENAI_API_KEY='sk-proj-YOUR_ACTUAL_API_KEY_HERE'
        ```

4.  **Run the Jupyter Notebook:**
    ```bash
    jupyter notebook Summarizing_IPCC_Website.ipynb
    ```
    (Or upload `Summarizing_IPCC_Website.ipynb` to Google Colab and run cells sequentially.)

## Usage

Open the `Summarizing_IPCC_Website.ipynb` notebook and execute the cells sequentially. The notebook will:

* Initialize the OpenAI client.
* Scrape the IPCC website (`https://www.ipcc.ch/`).
* Generate and display a multilingual summary of the website.

## Example Output

Here's an example of the generated summary:

```markdown
# Summary of IPCC Website

The **Intergovernmental Panel on Climate Change (IPCC)** is a United Nations body responsible for assessing the science related to climate change. It provides policymakers with scientific assessments on climate change implications and potential future risks, as well as strategies for adaptation and mitigation. It prepares comprehensive reports that include the latest scientific findings, impacts, and mitigation strategies related to climate change.

### Key Components:
- **Reports**: The IPCC publishes assessment reports, special reports, and methodology reports.
- **Working Groups**: There are three Working Groups focusing on various aspects of climate change:
  - **WG I**: Physical Science Basis
  - **WG II**: Impacts, Adaptation, and Vulnerability
  - **WG III**: Mitigation of Climate Change
- **Upcoming Initiatives**: The IPCC is calling for nominations for workshops on engaging diverse knowledge systems and methods of assessment. Additionally, it is looking for authors for the Seventh Assessment Report.

### Recent Announcements:
- **Nominations for Workshops**: Invitation for participants to engage in workshops scheduled for 2026.
- **Obituary**: The passing of Dr. Mannava V.K. Sivakumar, a respected member of the IPCC, was announced.
- **Lead Author Meeting**: Over 100 experts convened for the first lead author meeting related to the 2027 methodology report.

---

## Yoruba Summary

**IPCC** jẹ́ àjọ tó dá lórí àjọ UN tó ń ṣe àyẹ̀wò ìmọ̀ nípa àwọn ìyípadà ìjìnlẹ̀ ayé, àwọn ìpamọ́ rẹ̀, àti ewu to lè jẹ́. Àjọ náà fi àwọn ìwádìí wọn ṣe àfihàn, ṣùgbọ́n kì í ṣe àmúyẹ́ ìwádìí tirẹ̀. IPCC ń kọ́ àwọn iṣẹ́ àṣeyọrí, àwọn ìpèníjà, àti awọn ìwé ìlànà fún imulẹ̀ àwọn gàsì ti ilẹ̀.

### Àwọn kókó pàtàkì:
- **Àwọn Iṣẹ́**: IPCC fi àwọn ìwé àyẹ̀wò, àwọn ìwé àṣeyọrí, àwọn ìwé ìlànà tọ́ka sí.
- **Àwọn Ẹgbẹ́ Iṣẹ́**: Ẹgbẹ́ mẹta lo wa tí ó ń ṣiṣẹ́ lórí àwọn apá oriṣiriṣi ti ìyípadà ayé.
- **Àwọn Ìpèníjà Tó Nbọ**: IPCC n pe fún ìtọ́kasí àwọn olùkópa ṣe nípá ọkọ ayẹwoàpè ní 2026.

### Àwọn ìkìlọ̀ tuntun:
- **Ìtọ́kasí fún Àwọn Workshop**: Àpèjọ áti ohun èlò yíyọrisi nẹtiwọki.
- **Ikú Dr. Mannava V.K. Sivakumar**: Ikú olóòtú tó jẹ̀ alákóso kan ni IPCC.
- **Ìpàdé Àkọ́kọ́ fún Ìròyìn 2027**: Akẹ́kọ̀ọ́ mẹ́rìndínlọ́gọ́rin kópọ̀ jọ fún ìpàdé ikọ̀ ìkọ̀ wíwà.

---

## Hausa Summary

**IPCC** kungiya ce ta Majalisar Dinkin Duniya da ke nazarin kimiyyar canjin yanayi, illolinsa, da hargitsi da zai iya bayyana. IPCC tana bayar da rahotanni masu ma'ana ga masu yanke hukunci amma ba ta gudanar da bincike na kanta ba. Hakanan tana shirya rahotanni masu zurfi akan canjin yanayi.

### Muhimman Abubuwan:
- **Rahotanni**: IPCC tana fitar da rahotanni na nazari, rahotanni na musamman da rahotanni na hanyoyi gami da sabunta bayanai.
- **Kungiyoyi**: Akwai kungiyoyi guda uku da suka mai da hankali kan bangarori masu zaman kansu na canjin yanayi:
  - **Kungiya ta I**: Asalin Kimiyyar Jiki
  - **Kungiya ta II**: Illoli, Tausayi, da Jurewa
  - **Kungiya ta III**: Rage juyin halitta
- **Shirye-shiryen Gaba**: IPCC tana neman sunayen mahalarta taron karatu da kuma marubuta don rahoton kimiyyar nazari na bakwai.

### Labarai na kwanan nan:
- **Neman Sunaye don Taruka**: An gayyaci mahalarta domin taron daga 2026.
- **Kasuwa**: Kasuwancin Dr. Mannava V.K. Sivakumar an sanar.
- **Taron Marubuta**: Masana sama da 100 sun taru don taron marubuta na rahoton 2027.
