<div class="wrapper">
{% include nav.html %}
<div class="container">
<div class="collapsible-code">
<button type="button">Environment Setup</button>
<div class="language-python highlighter-rouge"><pre class="highlight"><code><span class="c1"># Setup the notebook based on running environment.
</span><span class="kn">import</span> <span class="n">os</span>
<span class="c1"># Optional: Enable telemetry in browser_use and chromadb.
</span><span class="n">os</span><span class="p">.</span><span class="n">environ</span><span class="p">[</span><span class="sh">"</span><span class="s">ANONYMIZED_TELEMETRY</span><span class="sh">"</span><span class="p">]</span> <span class="o">=</span> <span class="sh">"</span><span class="s">false</span><span class="sh">"</span>
<span class="c1"># Check for kaggle environment.
</span><span class="k">if</span> <span class="n">os</span><span class="p">.</span><span class="nf">getenv</span><span class="p">(</span><span class="sh">"</span><span class="s">KAGGLE_KERNEL_RUN_TYPE</span><span class="sh">"</span><span class="p">):</span>
    <span class="c1"># Kaggle Run: update the system.
</span>    <span class="err">!</span><span class="n">pip</span> <span class="n">uninstall</span> <span class="o">-</span><span class="n">qqy</span> <span class="n">google</span><span class="o">-</span><span class="n">ai</span><span class="o">-</span><span class="n">generativelanguage</span> <span class="n">pydrive2</span> <span class="n">tensorflow</span> <span class="n">tensorflow</span><span class="o">-</span><span class="n">decision</span><span class="o">-</span><span class="n">forests</span> <span class="n">cryptography</span> <span class="n">pyOpenSSL</span> <span class="n">langchain</span> <span class="n">langchain</span><span class="o">-</span><span class="n">core</span> <span class="n">nltk</span> <span class="n">ray</span> <span class="n">click</span> <span class="n">google</span><span class="o">-</span><span class="n">generativeai</span> <span class="n">google</span><span class="o">-</span><span class="n">cloud</span><span class="o">-</span><span class="n">translate</span> <span class="n">datasets</span> <span class="n">cesium</span> <span class="n">bigframes</span> <span class="n">plotnine</span> <span class="n">mlxtend</span> <span class="n">fastai</span> <span class="n">spacy</span> <span class="n">thinc</span> <span class="n">google</span><span class="o">-</span><span class="n">colab</span> <span class="n">gcsfs</span> <span class="n">jupyter</span><span class="o">-</span><span class="n">kernel</span><span class="o">-</span><span class="n">gateway</span> <span class="n">nltk</span> <span class="n">preprocessing</span>
    <span class="err">!</span><span class="n">pip</span> <span class="n">install</span> <span class="o">-</span><span class="n">qU</span> <span class="n">posthog</span>\<span class="o">&lt;</span><span class="mf">6.0</span><span class="p">.</span><span class="mi">0</span> <span class="n">google</span><span class="o">-</span><span class="n">genai</span><span class="o">==</span><span class="mf">1.50</span><span class="p">.</span><span class="mi">0</span> <span class="n">chromadb</span><span class="o">==</span><span class="mf">0.6</span><span class="p">.</span><span class="mi">3</span> <span class="n">opentelemetry</span><span class="o">-</span><span class="n">proto</span><span class="o">==</span><span class="mf">1.37</span><span class="p">.</span><span class="mi">0</span>
    <span class="err">!</span><span class="n">pip</span> <span class="n">install</span> <span class="o">-</span><span class="n">qU</span> <span class="n">langchain</span><span class="o">-</span><span class="n">community</span> <span class="n">langchain</span><span class="o">-</span><span class="n">text</span><span class="o">-</span><span class="n">splitters</span> <span class="n">wikipedia</span> <span class="n">lmnr</span><span class="p">[</span><span class="nb">all</span><span class="p">]</span> <span class="n">google</span><span class="o">-</span><span class="n">adk</span> <span class="n">google</span><span class="o">-</span><span class="n">adk</span><span class="p">[</span><span class="nb">eval</span><span class="p">]</span> <span class="n">google</span><span class="o">-</span><span class="n">cloud</span><span class="o">-</span><span class="n">translate</span>
    <span class="kn">from</span> <span class="n">kaggle_secrets</span> <span class="kn">import</span> <span class="n">UserSecretsClient</span> <span class="c1"># type: ignore
</span>    <span class="kn">from</span> <span class="n">jupyter_server.serverapp</span> <span class="kn">import</span> <span class="n">list_running_servers</span> <span class="c1"># type: ignore
</span><span class="k">else</span><span class="p">:</span>
    <span class="c1"># Mock the kaggle secrets client.
</span>    <span class="k">class</span> <span class="nc">UserSecretsClient</span><span class="p">:</span>
        <span class="nd">@classmethod</span>
        <span class="k">def</span> <span class="nf">set_secret</span><span class="p">(</span><span class="n">cls</span><span class="p">,</span> <span class="nb">id</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">value</span><span class="p">:</span> <span class="nb">str</span><span class="p">):</span>
            <span class="n">os</span><span class="p">.</span><span class="n">environ</span><span class="p">[</span><span class="nb">id</span><span class="p">]</span> <span class="o">=</span> <span class="n">value</span>
        <span class="nd">@classmethod</span>
        <span class="k">def</span> <span class="nf">get_secret</span><span class="p">(</span><span class="n">cls</span><span class="p">,</span> <span class="nb">id</span><span class="p">:</span> <span class="nb">str</span><span class="p">):</span>
            <span class="k">try</span><span class="p">:</span>
                <span class="k">return</span> <span class="n">os</span><span class="p">.</span><span class="n">environ</span><span class="p">[</span><span class="nb">id</span><span class="p">]</span>
            <span class="k">except</span> <span class="nb">KeyError</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
                <span class="nf">print</span><span class="p">(</span><span class="sa">f</span><span class="sh">"</span><span class="s">KeyError: authentication token for </span><span class="si">{</span><span class="nb">id</span><span class="si">}</span><span class="s"> is undefined</span><span class="sh">"</span><span class="p">)</span>
    <span class="c1"># Local Run: update the venv.
</span>    <span class="o">%</span><span class="n">pip</span> <span class="n">install</span> <span class="o">-</span><span class="n">qU</span> <span class="n">posthog</span>\<span class="o">&lt;</span><span class="mf">6.0</span><span class="p">.</span><span class="mi">0</span> <span class="n">google</span><span class="o">-</span><span class="n">genai</span><span class="o">==</span><span class="mf">1.50</span><span class="p">.</span><span class="mi">0</span> <span class="n">chromadb</span><span class="o">==</span><span class="mf">0.6</span><span class="p">.</span><span class="mi">3</span> <span class="n">opentelemetry</span><span class="o">-</span><span class="n">proto</span><span class="o">==</span><span class="mf">1.37</span><span class="p">.</span><span class="mi">0</span>
    <span class="o">%</span><span class="n">pip</span> <span class="n">install</span> <span class="o">-</span><span class="n">qU</span> <span class="n">langchain</span><span class="o">-</span><span class="n">community</span> <span class="n">langchain</span><span class="o">-</span><span class="n">text</span><span class="o">-</span><span class="n">splitters</span> <span class="n">wikipedia</span> <span class="n">pandas</span> <span class="n">google</span><span class="o">-</span><span class="n">api</span><span class="o">-</span><span class="n">core</span> <span class="sh">"</span><span class="s">lmnr[all]</span><span class="sh">"</span> <span class="n">browser</span><span class="o">-</span><span class="n">use</span> <span class="n">ollama</span> <span class="n">google</span><span class="o">-</span><span class="n">adk</span> <span class="sh">"</span><span class="s">google-adk[eval]</span><span class="sh">"</span>
    <span class="kn">from</span> <span class="n">browser_use</span> <span class="kn">import</span> <span class="n">Agent</span> <span class="k">as</span> <span class="n">BrowserAgent</span>

<span class="kn">import</span> <span class="n">ast</span><span class="p">,</span> <span class="n">chromadb</span><span class="p">,</span> <span class="n">json</span><span class="p">,</span> <span class="n">logging</span><span class="p">,</span> <span class="n">pandas</span><span class="p">,</span> <span class="n">platform</span><span class="p">,</span> <span class="n">pytz</span><span class="p">,</span> <span class="n">re</span><span class="p">,</span> <span class="n">requests</span><span class="p">,</span> <span class="n">sys</span><span class="p">,</span> <span class="n">threading</span><span class="p">,</span> <span class="n">time</span><span class="p">,</span> <span class="n">warnings</span><span class="p">,</span> <span class="n">wikipedia</span>
<span class="kn">from</span> <span class="n">bs4</span> <span class="kn">import</span> <span class="n">Tag</span>
<span class="kn">from</span> <span class="n">chromadb</span> <span class="kn">import</span> <span class="n">Documents</span><span class="p">,</span> <span class="n">Embeddings</span>
<span class="kn">from</span> <span class="n">datetime</span> <span class="kn">import</span> <span class="n">datetime</span><span class="p">,</span> <span class="n">timedelta</span>
<span class="kn">from</span> <span class="n">dateutil.parser</span> <span class="kn">import</span> <span class="n">parse</span>
<span class="kn">from</span> <span class="n">enum</span> <span class="kn">import</span> <span class="n">Enum</span>
<span class="kn">from</span> <span class="n">google.adk.apps.app</span> <span class="kn">import</span> <span class="n">App</span>
<span class="kn">from</span> <span class="n">google.adk.sessions</span> <span class="kn">import</span> <span class="n">InMemorySessionService</span><span class="p">,</span> <span class="n">BaseSessionService</span> <span class="k">as</span> <span class="n">SessionService</span><span class="p">,</span> <span class="n">Session</span>
<span class="kn">from</span> <span class="n">google.adk.runners</span> <span class="kn">import</span> <span class="n">Runner</span><span class="p">,</span> <span class="n">Event</span>
<span class="kn">from</span> <span class="n">google</span> <span class="kn">import</span> <span class="n">genai</span>
<span class="kn">from</span> <span class="n">google.api_core</span> <span class="kn">import</span> <span class="n">retry</span><span class="p">,</span> <span class="n">exceptions</span>
<span class="kn">from</span> <span class="n">google.genai.models</span> <span class="kn">import</span> <span class="n">Models</span>
<span class="kn">from</span> <span class="n">google.genai</span> <span class="kn">import</span> <span class="n">types</span><span class="p">,</span> <span class="n">errors</span>
<span class="kn">from</span> <span class="n">IPython.display</span> <span class="kn">import</span> <span class="n">Markdown</span><span class="p">,</span> <span class="n">display</span><span class="p">,</span> <span class="n">HTML</span>
<span class="kn">from</span> <span class="n">langchain_community.document_loaders.csv_loader</span> <span class="kn">import</span> <span class="n">CSVLoader</span>
<span class="kn">from</span> <span class="n">langchain_text_splitters.html</span> <span class="kn">import</span> <span class="n">HTMLSemanticPreservingSplitter</span>
<span class="kn">from</span> <span class="n">langchain_text_splitters.json</span> <span class="kn">import</span> <span class="n">RecursiveJsonSplitter</span>
<span class="kn">from</span> <span class="n">lmnr</span> <span class="kn">import</span> <span class="n">Laminar</span>
<span class="kn">from</span> <span class="n">math</span> <span class="kn">import</span> <span class="n">inf</span>
<span class="kn">from</span> <span class="n">pydantic</span> <span class="kn">import</span> <span class="n">BaseModel</span><span class="p">,</span> <span class="n">field_validator</span>
<span class="kn">from</span> <span class="n">threading</span> <span class="kn">import</span> <span class="n">Timer</span>
<span class="kn">from</span> <span class="n">tqdm</span> <span class="kn">import</span> <span class="n">tqdm</span>
<span class="kn">from</span> <span class="n">typing</span> <span class="kn">import</span> <span class="n">Optional</span><span class="p">,</span> <span class="n">Callable</span><span class="p">,</span> <span class="n">NewType</span><span class="p">,</span> <span class="n">NamedTuple</span>
<span class="kn">from</span> <span class="n">wikipedia.exceptions</span> <span class="kn">import</span> <span class="n">DisambiguationError</span><span class="p">,</span> <span class="n">PageError</span>
</code></pre></div></div>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>Note: you may need to restart the kernel to use updated packages.
Note: you may need to restart the kernel to use updated packages.
</code></pre></div></div>

<div class="collapsible-code">
<button type="button">Prepare the Gemini API</button>
<div class="language-python highlighter-rouge"><pre class="highlight"><code><span class="c1"># Prepare the Gemini api for use.
# Setup a retry helper for generation not run through the below api-helper.
</span><span class="n">is_retriable</span> <span class="o">=</span> <span class="k">lambda</span> <span class="n">e</span><span class="p">:</span> <span class="p">(</span><span class="nf">isinstance</span><span class="p">(</span><span class="n">e</span><span class="p">,</span> <span class="n">errors</span><span class="p">.</span><span class="n">APIError</span><span class="p">)</span> <span class="ow">and</span> <span class="n">e</span><span class="p">.</span><span class="n">code</span> <span class="ow">in</span> <span class="p">{</span><span class="mi">429</span><span class="p">,</span> <span class="mi">503</span><span class="p">,</span> <span class="mi">500</span><span class="p">})</span>
<span class="n">Models</span><span class="p">.</span><span class="n">generate_content</span> <span class="o">=</span> <span class="n">retry</span><span class="p">.</span><span class="nc">Retry</span><span class="p">(</span><span class="n">predicate</span><span class="o">=</span><span class="n">is_retriable</span><span class="p">)(</span><span class="n">Models</span><span class="p">.</span><span class="n">generate_content</span><span class="p">)</span>
<span class="n">Models</span><span class="p">.</span><span class="n">embed_content</span> <span class="o">=</span> <span class="n">retry</span><span class="p">.</span><span class="nc">Retry</span><span class="p">(</span><span class="n">predicate</span><span class="o">=</span><span class="n">is_retriable</span><span class="p">)(</span><span class="n">Models</span><span class="p">.</span><span class="n">embed_content</span><span class="p">)</span>

<span class="c1"># Activate Laminar auto-instrumentation.
</span><span class="k">try</span><span class="p">:</span>
    <span class="n">Laminar</span><span class="p">.</span><span class="nf">initialize</span><span class="p">(</span><span class="n">project_api_key</span><span class="o">=</span><span class="nc">UserSecretsClient</span><span class="p">().</span><span class="nf">get_secret</span><span class="p">(</span><span class="sh">"</span><span class="s">LMNR_PROJECT_API_KEY</span><span class="sh">"</span><span class="p">))</span>
<span class="k">except</span><span class="p">:</span>
    <span class="nf">print</span><span class="p">(</span><span class="sh">"</span><span class="s">Skipping Laminar.initialize()</span><span class="sh">"</span><span class="p">)</span>

<span class="k">class</span> <span class="nc">GeminiModel</span><span class="p">:</span>
    <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="n">self</span><span class="p">,</span> <span class="n">rpm</span><span class="p">:</span> <span class="nb">list</span><span class="p">,</span> <span class="n">tpm</span><span class="p">:</span> <span class="nb">list</span><span class="p">,</span> <span class="n">rpd</span><span class="p">:</span> <span class="nb">list</span><span class="p">):</span>
        <span class="n">self</span><span class="p">.</span><span class="n">rpm</span> <span class="o">=</span> <span class="n">rpm</span> <span class="c1"># requests per minute
</span>        <span class="n">self</span><span class="p">.</span><span class="n">tpm</span> <span class="o">=</span> <span class="n">tpm</span> <span class="c1"># tokens per minute in millions
</span>        <span class="n">self</span><span class="p">.</span><span class="n">rpd</span> <span class="o">=</span> <span class="n">rpd</span> <span class="c1"># requests per day
</span>        <span class="n">self</span><span class="p">.</span><span class="n">err</span> <span class="o">=</span> <span class="p">[</span><span class="mi">0</span><span class="p">,</span><span class="mi">0</span><span class="p">]</span> <span class="c1"># validation, api_related
</span>
<span class="c1"># A python api-helper with model fail-over/chaining/retry support.
</span><span class="n">GeminiEmbedFunction</span> <span class="o">=</span> <span class="nc">NewType</span><span class="p">(</span><span class="sh">"</span><span class="s">GeminiEmbedFunction</span><span class="sh">"</span><span class="p">,</span> <span class="bp">None</span><span class="p">)</span> <span class="c1"># forward-decl
</span><span class="k">class</span> <span class="nc">Api</span><span class="p">:</span>
    <span class="n">gen_limit_in</span> <span class="o">=</span> <span class="mi">1048576</span>
    <span class="n">emb_limit_in</span> <span class="o">=</span> <span class="mi">2048</span>
    <span class="n">gen_model</span> <span class="o">=</span> <span class="p">{</span>
        <span class="sh">"</span><span class="s">gemini-2.5-flash</span><span class="sh">"</span><span class="p">:</span> <span class="nc">GeminiModel</span><span class="p">([</span><span class="mi">10</span><span class="p">,</span><span class="mi">1000</span><span class="p">,</span><span class="mi">2000</span><span class="p">,</span><span class="mi">10000</span><span class="p">],[.</span><span class="mi">25</span><span class="p">,</span><span class="mi">1</span><span class="p">,</span><span class="mi">3</span><span class="p">,</span><span class="mi">8</span><span class="p">],[</span><span class="mi">250</span><span class="p">,</span><span class="mi">10000</span><span class="p">,</span><span class="mi">100000</span><span class="p">,</span><span class="n">inf</span><span class="p">]),</span> <span class="c1"># stable: 10 RPM/250K TPM/250 RPD
</span>        <span class="sh">"</span><span class="s">gemini-2.5-flash-preview-09-2025</span><span class="sh">"</span><span class="p">:</span> <span class="nc">GeminiModel</span><span class="p">([</span><span class="mi">10</span><span class="p">,</span><span class="mi">1000</span><span class="p">,</span><span class="mi">2000</span><span class="p">,</span><span class="mi">10000</span><span class="p">],[.</span><span class="mi">25</span><span class="p">,</span><span class="mi">1</span><span class="p">,</span><span class="mi">3</span><span class="p">,</span><span class="mi">8</span><span class="p">],[</span><span class="mi">250</span><span class="p">,</span><span class="mi">10000</span><span class="p">,</span><span class="mi">100000</span><span class="p">,</span><span class="n">inf</span><span class="p">]),</span> <span class="c1"># exp: 10 RPM/250K TPM/250 RPD
</span>        <span class="sh">"</span><span class="s">gemini-2.0-flash-exp</span><span class="sh">"</span><span class="p">:</span> <span class="nc">GeminiModel</span><span class="p">([</span><span class="mi">10</span><span class="p">,</span><span class="mi">10</span><span class="p">,</span><span class="mi">10</span><span class="p">,</span><span class="mi">10</span><span class="p">],[.</span><span class="mi">25</span><span class="p">,.</span><span class="mi">25</span><span class="p">,.</span><span class="mi">25</span><span class="p">,.</span><span class="mi">25</span><span class="p">],[</span><span class="mi">200</span><span class="p">,</span><span class="mi">500</span><span class="p">,</span><span class="mi">500</span><span class="p">,</span><span class="mi">500</span><span class="p">]),</span> <span class="c1"># latest w/thinking: 10 RPM/250K TPM/200 RPD
</span>        <span class="sh">"</span><span class="s">gemini-2.0-flash</span><span class="sh">"</span><span class="p">:</span> <span class="nc">GeminiModel</span><span class="p">([</span><span class="mi">15</span><span class="p">,</span><span class="mi">2000</span><span class="p">,</span><span class="mi">10000</span><span class="p">,</span><span class="mi">30000</span><span class="p">],[</span><span class="mi">1</span><span class="p">,</span><span class="mi">4</span><span class="p">,</span><span class="mi">10</span><span class="p">,</span><span class="mi">30</span><span class="p">],[</span><span class="mi">200</span><span class="p">,</span><span class="n">inf</span><span class="p">,</span><span class="n">inf</span><span class="p">,</span><span class="n">inf</span><span class="p">]),</span> <span class="c1"># stable wo/thinking: 15 RPM/1M TPM/200 RPD
</span>        <span class="sh">"</span><span class="s">gemini-2.5-flash-lite</span><span class="sh">"</span><span class="p">:</span> <span class="nc">GeminiModel</span><span class="p">([</span><span class="mi">15</span><span class="p">,</span><span class="mi">4000</span><span class="p">,</span><span class="mi">10000</span><span class="p">,</span><span class="mi">30000</span><span class="p">],[.</span><span class="mi">25</span><span class="p">,</span><span class="mi">4</span><span class="p">,</span><span class="mi">10</span><span class="p">,</span><span class="mi">30</span><span class="p">],[</span><span class="mi">1000</span><span class="p">,</span><span class="n">inf</span><span class="p">,</span><span class="n">inf</span><span class="p">,</span><span class="n">inf</span><span class="p">]),</span> <span class="c1"># stable: 15 RPM/250K TPM/1K RPD
</span>        <span class="sh">"</span><span class="s">gemini-2.5-flash-lite-preview-09-2025</span><span class="sh">"</span><span class="p">:</span> <span class="nc">GeminiModel</span><span class="p">([</span><span class="mi">15</span><span class="p">,</span><span class="mi">4000</span><span class="p">,</span><span class="mi">10000</span><span class="p">,</span><span class="mi">30000</span><span class="p">],[.</span><span class="mi">25</span><span class="p">,</span><span class="mi">4</span><span class="p">,</span><span class="mi">10</span><span class="p">,</span><span class="mi">30</span><span class="p">],[</span><span class="mi">1000</span><span class="p">,</span><span class="n">inf</span><span class="p">,</span><span class="n">inf</span><span class="p">,</span><span class="n">inf</span><span class="p">]),</span> <span class="c1"># exp: 15 RPM/250K TPM/1K RPD
</span>        <span class="sh">"</span><span class="s">gemini-2.5-pro</span><span class="sh">"</span><span class="p">:</span> <span class="nc">GeminiModel</span><span class="p">([</span><span class="mi">5</span><span class="p">,</span><span class="mi">150</span><span class="p">,</span><span class="mi">1000</span><span class="p">,</span><span class="mi">2000</span><span class="p">],[.</span><span class="mi">125</span><span class="p">,</span><span class="mi">2</span><span class="p">,</span><span class="mi">5</span><span class="p">,</span><span class="mi">8</span><span class="p">],[</span><span class="mi">100</span><span class="p">,</span><span class="mi">10000</span><span class="p">,</span><span class="mi">50000</span><span class="p">,</span><span class="n">inf</span><span class="p">]),</span> <span class="c1"># stable: 5 RPM/250K TPM/100 RPD
</span>    <span class="p">}</span>
    <span class="n">gen_local</span> <span class="o">=</span> <span class="p">[</span><span class="sh">"</span><span class="s">gemma3n:e4b</span><span class="sh">"</span><span class="p">,</span><span class="sh">"</span><span class="s">gemma3:12b-it-qat</span><span class="sh">"</span><span class="p">]</span>
    <span class="n">default_local</span> <span class="o">=</span> <span class="mi">0</span>
    <span class="n">default_model</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="n">embed_model</span> <span class="o">=</span> <span class="sh">"</span><span class="s">gemini-embedding-001</span><span class="sh">"</span><span class="p">,</span> <span class="nc">GeminiModel</span><span class="p">([</span><span class="mi">100</span><span class="p">,</span><span class="mi">3000</span><span class="p">,</span><span class="mi">5000</span><span class="p">,</span><span class="mi">10000</span><span class="p">],[.</span><span class="mi">03</span><span class="p">,</span><span class="mi">1</span><span class="p">,</span><span class="mi">5</span><span class="p">,</span><span class="mi">10</span><span class="p">],[</span><span class="mi">1000</span><span class="p">,</span><span class="n">inf</span><span class="p">,</span><span class="n">inf</span><span class="p">,</span><span class="n">inf</span><span class="p">])</span> <span class="c1"># stable: 100 RPM/30K TPM/1000 RPD/100 per batch
</span>    <span class="n">embed_local</span> <span class="o">=</span> <span class="bp">False</span>
    <span class="n">error_total</span> <span class="o">=</span> <span class="mi">0</span>
    <span class="n">min_rpm</span> <span class="o">=</span> <span class="mi">3</span>
    <span class="n">min_tpm</span> <span class="o">=</span> <span class="mi">40000</span>
    <span class="n">dt_between</span> <span class="o">=</span> <span class="mf">2.0</span>
    <span class="n">errored</span> <span class="o">=</span> <span class="bp">False</span>
    <span class="n">running</span> <span class="o">=</span> <span class="bp">False</span>
    <span class="n">dt_err</span> <span class="o">=</span> <span class="mf">45.0</span>
    <span class="n">dt_rpm</span> <span class="o">=</span> <span class="mf">60.0</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">get</span><span class="p">(</span><span class="n">cls</span><span class="p">,</span> <span class="n">url</span><span class="p">:</span> <span class="nb">str</span><span class="p">):</span>
        <span class="c1"># Create a header matching the OS' tcp-stack fingerprint.
</span>        <span class="n">system_ua</span> <span class="o">=</span> <span class="bp">None</span>
        <span class="k">match</span> <span class="n">platform</span><span class="p">.</span><span class="nf">system</span><span class="p">():</span>
            <span class="k">case</span> <span class="sh">'</span><span class="s">Linux</span><span class="sh">'</span><span class="p">:</span>
                <span class="n">system_ua</span> <span class="o">=</span> <span class="sh">'</span><span class="s">Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36</span><span class="sh">'</span>
            <span class="k">case</span> <span class="sh">'</span><span class="s">Darwin</span><span class="sh">'</span><span class="p">:</span>
                <span class="n">system_ua</span> <span class="o">=</span> <span class="sh">'</span><span class="s">Mozilla/5.0 (Macintosh; Intel Mac OS X 15_7_2) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/26.0 Safari/605.1.15</span><span class="sh">'</span>
            <span class="k">case</span> <span class="sh">'</span><span class="s">Windows</span><span class="sh">'</span><span class="p">:</span>
                <span class="n">system_ua</span> <span class="o">=</span> <span class="sh">'</span><span class="s">Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36</span><span class="sh">'</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="n">request</span> <span class="o">=</span> <span class="n">requests</span><span class="p">.</span><span class="nf">get</span><span class="p">(</span><span class="n">url</span><span class="p">,</span> <span class="n">headers</span><span class="o">=</span><span class="p">{</span><span class="sh">'</span><span class="s">User-Agent</span><span class="sh">'</span><span class="p">:</span> <span class="n">system_ua</span><span class="p">})</span>
            <span class="k">if</span> <span class="n">request</span><span class="p">.</span><span class="n">status_code</span> <span class="o">!=</span> <span class="n">requests</span><span class="p">.</span><span class="n">codes</span><span class="p">.</span><span class="n">ok</span><span class="p">:</span>
                <span class="nf">print</span><span class="p">(</span><span class="sa">f</span><span class="sh">"</span><span class="s">Api.get() returned status </span><span class="si">{</span><span class="n">request</span><span class="p">.</span><span class="n">status_code</span><span class="si">}</span><span class="sh">"</span><span class="p">)</span>
            <span class="k">return</span> <span class="n">request</span><span class="p">.</span><span class="n">text</span>
        <span class="k">except</span> <span class="nb">Exception</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
            <span class="k">raise</span> <span class="n">e</span>

    <span class="k">class</span> <span class="nc">Limit</span><span class="p">(</span><span class="n">Enum</span><span class="p">):</span>
        <span class="n">FREE</span> <span class="o">=</span> <span class="mi">0</span>
        <span class="n">TIER_1</span> <span class="o">=</span> <span class="mi">1</span>
        <span class="n">TIER_2</span> <span class="o">=</span> <span class="mi">2</span>
        <span class="n">TIER_3</span> <span class="o">=</span> <span class="mi">3</span>
    
    <span class="k">class</span> <span class="nc">Model</span><span class="p">(</span><span class="n">Enum</span><span class="p">):</span>
        <span class="n">GEN</span> <span class="o">=</span> <span class="mi">1</span>
        <span class="n">EMB</span> <span class="o">=</span> <span class="mi">2</span>
        <span class="n">LOC</span> <span class="o">=</span> <span class="mi">3</span>

    <span class="k">class</span> <span class="nc">Const</span><span class="p">(</span><span class="n">Enum</span><span class="p">):</span>
        <span class="n">STOP</span> <span class="o">=</span> <span class="sh">"</span><span class="s">I don</span><span class="sh">'</span><span class="s">t know.</span><span class="sh">"</span>
        <span class="n">METRIC_BATCH</span> <span class="o">=</span> <span class="mi">20</span>
        <span class="n">SERIES_BATCH</span> <span class="o">=</span> <span class="mi">40</span>
        <span class="n">EMBED_BATCH</span> <span class="o">=</span> <span class="mi">100</span>
        <span class="n">CHUNK_MAX</span> <span class="o">=</span> <span class="mi">1500</span>

        <span class="nd">@classmethod</span>
        <span class="k">def</span> <span class="nf">Stop</span><span class="p">(</span><span class="n">cls</span><span class="p">):</span>
            <span class="k">return</span> <span class="n">cls</span><span class="p">.</span><span class="n">STOP</span><span class="p">.</span><span class="n">value</span>

        <span class="nd">@classmethod</span>
        <span class="k">def</span> <span class="nf">MetricBatch</span><span class="p">(</span><span class="n">cls</span><span class="p">):</span>
            <span class="k">return</span> <span class="n">cls</span><span class="p">.</span><span class="n">METRIC_BATCH</span><span class="p">.</span><span class="n">value</span>

        <span class="nd">@classmethod</span>
        <span class="k">def</span> <span class="nf">SeriesBatch</span><span class="p">(</span><span class="n">cls</span><span class="p">):</span>
            <span class="k">return</span> <span class="n">cls</span><span class="p">.</span><span class="n">SERIES_BATCH</span><span class="p">.</span><span class="n">value</span>

        <span class="nd">@classmethod</span>
        <span class="k">def</span> <span class="nf">EmbedBatch</span><span class="p">(</span><span class="n">cls</span><span class="p">):</span>
            <span class="k">return</span> <span class="n">cls</span><span class="p">.</span><span class="n">EMBED_BATCH</span><span class="p">.</span><span class="n">value</span>

        <span class="nd">@classmethod</span>
        <span class="k">def</span> <span class="nf">ChunkMax</span><span class="p">(</span><span class="n">cls</span><span class="p">):</span>
            <span class="k">return</span> <span class="n">cls</span><span class="p">.</span><span class="n">CHUNK_MAX</span><span class="p">.</span><span class="n">value</span>
    
    <span class="k">class</span> <span class="nc">Env</span><span class="p">(</span><span class="n">NamedTuple</span><span class="p">):</span> <span class="c1"># Make init args immutable.
</span>        <span class="n">CLIENT</span><span class="p">:</span> <span class="n">genai</span><span class="p">.</span><span class="n">Client</span>
        <span class="n">API_LIMIT</span><span class="p">:</span> <span class="nb">int</span>
        <span class="n">GEN_DEFAULT</span><span class="p">:</span> <span class="nb">str</span>

    <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="n">self</span><span class="p">,</span> <span class="n">with_limit</span><span class="p">:</span> <span class="n">Limit</span> <span class="o">|</span> <span class="nb">int</span><span class="p">,</span> <span class="n">default_model</span><span class="p">:</span> <span class="nb">str</span><span class="p">):</span>
        <span class="k">if</span> <span class="n">default_model</span> <span class="ow">in</span> <span class="n">self</span><span class="p">.</span><span class="n">gen_model</span><span class="p">.</span><span class="nf">keys</span><span class="p">():</span>
            <span class="n">self</span><span class="p">.</span><span class="n">write_lock</span> <span class="o">=</span> <span class="n">threading</span><span class="p">.</span><span class="nc">RLock</span><span class="p">()</span>
            <span class="k">try</span><span class="p">:</span>
                <span class="k">if</span> <span class="nf">isinstance</span><span class="p">(</span><span class="n">with_limit</span><span class="p">,</span> <span class="nb">int</span><span class="p">)</span> <span class="ow">and</span> <span class="n">with_limit</span> <span class="ow">in</span> <span class="p">[</span><span class="nb">id</span><span class="p">.</span><span class="n">value</span> <span class="k">for</span> <span class="nb">id</span> <span class="ow">in</span> <span class="n">Api</span><span class="p">.</span><span class="n">Limit</span><span class="p">]:</span>
                    <span class="n">limit</span> <span class="o">=</span> <span class="n">with_limit</span>
                <span class="k">else</span><span class="p">:</span>
                    <span class="n">limit</span> <span class="o">=</span> <span class="n">with_limit</span><span class="p">.</span><span class="n">value</span>
            <span class="k">except</span> <span class="nb">Exception</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
                <span class="nf">print</span><span class="p">(</span><span class="sa">f</span><span class="sh">"</span><span class="s">Api.__init__: </span><span class="si">{</span><span class="n">with_limit</span><span class="si">}</span><span class="s"> is not a valid limit</span><span class="sh">"</span><span class="p">)</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="n">self</span><span class="p">.</span><span class="n">args</span> <span class="o">=</span> <span class="n">Api</span><span class="p">.</span><span class="nc">Env</span><span class="p">(</span>
                    <span class="n">genai</span><span class="p">.</span><span class="nc">Client</span><span class="p">(</span><span class="n">api_key</span><span class="o">=</span><span class="nc">UserSecretsClient</span><span class="p">().</span><span class="nf">get_secret</span><span class="p">(</span><span class="sh">"</span><span class="s">GOOGLE_API_KEY</span><span class="sh">"</span><span class="p">)),</span>
                    <span class="n">limit</span><span class="p">,</span> <span class="n">default_model</span><span class="p">)</span>
            <span class="n">self</span><span class="p">.</span><span class="n">m_id</span> <span class="o">=</span> <span class="nf">list</span><span class="p">(</span><span class="n">self</span><span class="p">.</span><span class="n">gen_model</span><span class="p">.</span><span class="nf">keys</span><span class="p">()).</span><span class="nf">index</span><span class="p">(</span><span class="n">default_model</span><span class="p">)</span>
            <span class="n">self</span><span class="p">.</span><span class="n">default_model</span><span class="p">.</span><span class="nf">append</span><span class="p">(</span><span class="n">default_model</span><span class="p">)</span>
            <span class="n">self</span><span class="p">.</span><span class="nf">update_quota</span><span class="p">()</span>
            <span class="n">self</span><span class="p">.</span><span class="n">s_embed</span> <span class="o">=</span> <span class="nc">GeminiEmbedFunction</span><span class="p">(</span><span class="n">self</span><span class="p">.</span><span class="n">args</span><span class="p">.</span><span class="n">CLIENT</span><span class="p">,</span> <span class="n">semantic_mode</span> <span class="o">=</span> <span class="bp">True</span><span class="p">)</span> <span class="c1"># type: ignore
</span>            <span class="n">logging</span><span class="p">.</span><span class="nf">getLogger</span><span class="p">(</span><span class="sh">"</span><span class="s">google_genai</span><span class="sh">"</span><span class="p">).</span><span class="nf">setLevel</span><span class="p">(</span><span class="n">logging</span><span class="p">.</span><span class="n">WARNING</span><span class="p">)</span> <span class="c1"># suppress info on generate
</span>        <span class="k">else</span><span class="p">:</span>
            <span class="nf">print</span><span class="p">(</span><span class="sa">f</span><span class="sh">"</span><span class="s">Api.__init__: </span><span class="si">{</span><span class="n">default_model</span><span class="si">}</span><span class="s"> not found in gen_model.keys()</span><span class="sh">"</span><span class="p">)</span>
        

    <span class="k">def</span> <span class="nf">__call__</span><span class="p">(</span><span class="n">self</span><span class="p">,</span> <span class="n">model</span><span class="p">:</span> <span class="n">Model</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="k">if</span> <span class="n">model</span> <span class="o">==</span> <span class="n">self</span><span class="p">.</span><span class="n">Model</span><span class="p">.</span><span class="n">GEN</span><span class="p">:</span>
            <span class="k">return</span> <span class="sh">"</span><span class="s">models/</span><span class="sh">"</span> <span class="o">+</span> <span class="nf">list</span><span class="p">(</span><span class="n">self</span><span class="p">.</span><span class="n">gen_model</span><span class="p">.</span><span class="nf">keys</span><span class="p">())[</span><span class="n">self</span><span class="p">.</span><span class="n">m_id</span><span class="p">]</span>
        <span class="k">elif</span> <span class="n">model</span> <span class="o">==</span> <span class="n">self</span><span class="p">.</span><span class="n">Model</span><span class="p">.</span><span class="n">LOC</span><span class="p">:</span>
            <span class="k">return</span> <span class="n">self</span><span class="p">.</span><span class="n">gen_local</span><span class="p">[</span><span class="n">self</span><span class="p">.</span><span class="n">default_local</span><span class="p">]</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="k">return</span> <span class="sh">"</span><span class="s">models/</span><span class="sh">"</span> <span class="o">+</span> <span class="n">self</span><span class="p">.</span><span class="n">embed_model</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="k">if</span> <span class="ow">not</span> <span class="n">self</span><span class="p">.</span><span class="n">embed_local</span> <span class="k">else</span> <span class="sh">"</span><span class="s">embeddinggemma:latest</span><span class="sh">"</span>

    <span class="k">def</span> <span class="nf">push_default_model</span><span class="p">(</span><span class="n">self</span><span class="p">,</span> <span class="n">model_id</span><span class="p">:</span> <span class="nb">str</span><span class="p">):</span>
        <span class="k">if</span> <span class="n">model_id</span> <span class="ow">in</span> <span class="n">self</span><span class="p">.</span><span class="n">gen_model</span><span class="p">.</span><span class="nf">keys</span><span class="p">():</span>
            <span class="n">self</span><span class="p">.</span><span class="n">write_lock</span><span class="p">.</span><span class="nf">acquire</span><span class="p">()</span>
            <span class="n">self</span><span class="p">.</span><span class="nf">stop_running</span><span class="p">()</span>
            <span class="n">self</span><span class="p">.</span><span class="n">default_model</span><span class="p">.</span><span class="nf">append</span><span class="p">(</span><span class="n">model_id</span><span class="p">)</span>
            <span class="n">self</span><span class="p">.</span><span class="n">m_id</span> <span class="o">=</span> <span class="nf">list</span><span class="p">(</span><span class="n">self</span><span class="p">.</span><span class="n">gen_model</span><span class="p">.</span><span class="nf">keys</span><span class="p">()).</span><span class="nf">index</span><span class="p">(</span><span class="n">model_id</span><span class="p">)</span>
            <span class="n">self</span><span class="p">.</span><span class="n">write_lock</span><span class="p">.</span><span class="nf">release</span><span class="p">()</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="nf">print</span><span class="p">(</span><span class="sa">f</span><span class="sh">"</span><span class="si">{</span><span class="n">model_id</span><span class="si">}</span><span class="s"> not found in gen_model.keys()</span><span class="sh">"</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">pop_default_model</span><span class="p">(</span><span class="n">self</span><span class="p">):</span>
        <span class="k">if</span> <span class="nf">len</span><span class="p">(</span><span class="n">self</span><span class="p">.</span><span class="n">default_model</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mi">1</span><span class="p">:</span>
            <span class="n">self</span><span class="p">.</span><span class="n">write_lock</span><span class="p">.</span><span class="nf">acquire</span><span class="p">()</span>
            <span class="n">self</span><span class="p">.</span><span class="nf">stop_running</span><span class="p">()</span>
            <span class="n">self</span><span class="p">.</span><span class="n">default_model</span><span class="p">.</span><span class="nf">pop</span><span class="p">(</span><span class="o">-</span><span class="mi">1</span><span class="p">)</span>
            <span class="n">self</span><span class="p">.</span><span class="n">m_id</span> <span class="o">=</span> <span class="nf">list</span><span class="p">(</span><span class="n">self</span><span class="p">.</span><span class="n">gen_model</span><span class="p">.</span><span class="nf">keys</span><span class="p">()).</span><span class="nf">index</span><span class="p">(</span><span class="n">self</span><span class="p">.</span><span class="n">default_model</span><span class="p">[</span><span class="o">-</span><span class="mi">1</span><span class="p">])</span>
            <span class="n">self</span><span class="p">.</span><span class="n">write_lock</span><span class="p">.</span><span class="nf">release</span><span class="p">()</span>

    <span class="k">def</span> <span class="nf">retriable</span><span class="p">(</span><span class="n">self</span><span class="p">,</span> <span class="n">retry_fn</span><span class="p">:</span> <span class="n">Callable</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
        <span class="n">tries</span> <span class="o">=</span> <span class="mi">3</span><span class="o">*</span><span class="nf">len</span><span class="p">(</span><span class="n">self</span><span class="p">.</span><span class="n">gen_model</span><span class="p">.</span><span class="nf">keys</span><span class="p">())</span>
        <span class="k">for</span> <span class="n">attempt</span> <span class="ow">in</span> <span class="nf">range</span><span class="p">(</span><span class="n">tries</span><span class="p">):</span>
            <span class="k">try</span><span class="p">:</span>
                <span class="n">self</span><span class="p">.</span><span class="n">write_lock</span><span class="p">.</span><span class="nf">acquire</span><span class="p">()</span>
                <span class="n">token_use</span> <span class="o">=</span> <span class="n">self</span><span class="p">.</span><span class="nf">token_count</span><span class="p">(</span><span class="n">kwargs</span><span class="p">[</span><span class="sh">"</span><span class="s">contents</span><span class="sh">"</span><span class="p">])</span>
                <span class="k">if</span> <span class="n">self</span><span class="p">.</span><span class="n">gen_rpm</span> <span class="o">&gt;</span> <span class="n">self</span><span class="p">.</span><span class="n">min_rpm</span> <span class="ow">and</span> <span class="n">token_use</span> <span class="o">&lt;=</span> <span class="n">self</span><span class="p">.</span><span class="n">token_quota</span> <span class="ow">and</span> <span class="n">self</span><span class="p">.</span><span class="n">token_quota</span> <span class="o">&gt;</span> <span class="n">self</span><span class="p">.</span><span class="n">min_tpm</span><span class="p">:</span>
                    <span class="n">self</span><span class="p">.</span><span class="n">token_quota</span> <span class="o">-=</span> <span class="n">token_use</span>
                    <span class="n">self</span><span class="p">.</span><span class="n">gen_rpm</span> <span class="o">-=</span> <span class="mi">1</span>
                <span class="k">else</span><span class="p">:</span>
                    <span class="n">self</span><span class="p">.</span><span class="nf">on_error</span><span class="p">(</span><span class="n">kwargs</span><span class="p">)</span>
                <span class="k">if</span> <span class="ow">not</span> <span class="n">self</span><span class="p">.</span><span class="n">running</span> <span class="ow">and</span> <span class="ow">not</span> <span class="n">self</span><span class="p">.</span><span class="n">errored</span><span class="p">:</span>
                    <span class="n">self</span><span class="p">.</span><span class="n">rpm_timer</span> <span class="o">=</span> <span class="nc">Timer</span><span class="p">(</span><span class="n">self</span><span class="p">.</span><span class="n">dt_rpm</span><span class="p">,</span> <span class="n">self</span><span class="p">.</span><span class="n">refill_rpm</span><span class="p">)</span>
                    <span class="n">self</span><span class="p">.</span><span class="n">rpm_timer</span><span class="p">.</span><span class="nf">start</span><span class="p">()</span>
                    <span class="n">self</span><span class="p">.</span><span class="n">running</span> <span class="o">=</span> <span class="bp">True</span>
                <span class="k">return</span> <span class="nf">retry_fn</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span>
            <span class="nf">except </span><span class="p">(</span><span class="n">errors</span><span class="p">.</span><span class="n">APIError</span><span class="p">,</span> <span class="n">exceptions</span><span class="p">.</span><span class="n">RetryError</span><span class="p">)</span> <span class="k">as</span> <span class="n">api_error</span><span class="p">:</span>
                <span class="k">if</span> <span class="nf">isinstance</span><span class="p">(</span><span class="n">api_error</span><span class="p">,</span> <span class="n">errors</span><span class="p">.</span><span class="n">APIError</span><span class="p">):</span>
                    <span class="n">is_retry</span> <span class="o">=</span> <span class="n">api_error</span><span class="p">.</span><span class="n">code</span> <span class="ow">in</span> <span class="p">{</span><span class="mi">429</span><span class="p">,</span> <span class="mi">503</span><span class="p">,</span> <span class="mi">500</span><span class="p">,</span> <span class="mi">400</span><span class="p">}</span> <span class="c1"># code 400 when TPM exceeded
</span>                    <span class="k">if</span> <span class="n">api_error</span><span class="p">.</span><span class="n">code</span> <span class="o">==</span> <span class="mi">400</span><span class="p">:</span>
                        <span class="nf">print</span><span class="p">(</span><span class="sa">f</span><span class="sh">"</span><span class="s">retriable.api_error: token limit exceeded (</span><span class="si">{</span><span class="n">token_use</span><span class="si">}</span><span class="s">)</span><span class="sh">"</span><span class="p">)</span>
                    <span class="k">else</span><span class="p">:</span>
                        <span class="nf">print</span><span class="p">(</span><span class="sa">f</span><span class="sh">"</span><span class="s">retriable.api_error(</span><span class="si">{</span><span class="n">api_error</span><span class="p">.</span><span class="n">code</span><span class="si">}</span><span class="s">): </span><span class="si">{</span><span class="nf">str</span><span class="p">(</span><span class="n">api_error</span><span class="p">)</span><span class="si">}</span><span class="sh">"</span><span class="p">)</span>
                    <span class="k">if</span> <span class="ow">not</span> <span class="n">is_retry</span> <span class="ow">or</span> <span class="n">attempt</span> <span class="o">==</span> <span class="n">tries</span><span class="p">:</span>
                        <span class="k">raise</span> <span class="n">api_error</span>
                <span class="n">self</span><span class="p">.</span><span class="nf">on_error</span><span class="p">(</span><span class="n">kwargs</span><span class="p">)</span>
            <span class="k">except</span> <span class="nb">Exception</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
                <span class="nf">print</span><span class="p">(</span><span class="sa">f</span><span class="sh">"</span><span class="s">retriable.exception: </span><span class="si">{</span><span class="nf">str</span><span class="p">(</span><span class="n">e</span><span class="p">)</span><span class="si">}</span><span class="sh">"</span><span class="p">)</span>
                <span class="n">self</span><span class="p">.</span><span class="nf">on_error</span><span class="p">(</span><span class="n">kwargs</span><span class="p">)</span>
            <span class="k">finally</span><span class="p">:</span>
                <span class="n">self</span><span class="p">.</span><span class="n">write_lock</span><span class="p">.</span><span class="nf">release</span><span class="p">()</span>

    <span class="k">def</span> <span class="nf">on_error</span><span class="p">(</span><span class="n">self</span><span class="p">,</span> <span class="n">kwargs</span><span class="p">):</span>
        <span class="n">self</span><span class="p">.</span><span class="nf">generation_fail</span><span class="p">()</span>
        <span class="n">kwargs</span><span class="p">[</span><span class="sh">"</span><span class="s">model</span><span class="sh">"</span><span class="p">]</span> <span class="o">=</span> <span class="nf">self</span><span class="p">(</span><span class="n">Api</span><span class="p">.</span><span class="n">Model</span><span class="p">.</span><span class="n">GEN</span><span class="p">)</span>
        <span class="n">time</span><span class="p">.</span><span class="nf">sleep</span><span class="p">(</span><span class="n">self</span><span class="p">.</span><span class="n">dt_between</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">stop_running</span><span class="p">(</span><span class="n">self</span><span class="p">):</span>
        <span class="k">if</span> <span class="n">self</span><span class="p">.</span><span class="n">running</span><span class="p">:</span>
            <span class="n">self</span><span class="p">.</span><span class="n">rpm_timer</span><span class="p">.</span><span class="nf">cancel</span><span class="p">()</span>
            <span class="n">self</span><span class="p">.</span><span class="n">running</span> <span class="o">=</span> <span class="bp">False</span>

    <span class="k">def</span> <span class="nf">validation_fail</span><span class="p">(</span><span class="n">self</span><span class="p">):</span>
        <span class="nf">list</span><span class="p">(</span><span class="n">self</span><span class="p">.</span><span class="n">gen_model</span><span class="p">.</span><span class="nf">values</span><span class="p">())[</span><span class="n">self</span><span class="p">.</span><span class="n">m_id</span><span class="p">].</span><span class="n">err</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span> <span class="o">+=</span> <span class="mi">1</span>
        <span class="n">self</span><span class="p">.</span><span class="n">error_total</span> <span class="o">+=</span> <span class="mi">1</span>

    <span class="k">def</span> <span class="nf">generation_fail</span><span class="p">(</span><span class="n">self</span><span class="p">):</span>
        <span class="n">self</span><span class="p">.</span><span class="nf">stop_running</span><span class="p">()</span>
        <span class="n">self</span><span class="p">.</span><span class="nf">save_error</span><span class="p">()</span>
        <span class="n">self</span><span class="p">.</span><span class="nf">next_model</span><span class="p">()</span>
        <span class="nf">print</span><span class="p">(</span><span class="sh">"</span><span class="s">Api.generation_fail.next_model: model is now</span><span class="sh">"</span><span class="p">,</span> <span class="nf">list</span><span class="p">(</span><span class="n">self</span><span class="p">.</span><span class="n">gen_model</span><span class="p">.</span><span class="nf">keys</span><span class="p">())[</span><span class="n">self</span><span class="p">.</span><span class="n">m_id</span><span class="p">])</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="n">self</span><span class="p">.</span><span class="n">errored</span><span class="p">:</span>
            <span class="n">self</span><span class="p">.</span><span class="n">error_timer</span> <span class="o">=</span> <span class="nc">Timer</span><span class="p">(</span><span class="n">self</span><span class="p">.</span><span class="n">dt_err</span><span class="p">,</span> <span class="n">self</span><span class="p">.</span><span class="n">zero_error</span><span class="p">)</span>
            <span class="n">self</span><span class="p">.</span><span class="n">error_timer</span><span class="p">.</span><span class="nf">start</span><span class="p">()</span>
            <span class="n">self</span><span class="p">.</span><span class="n">errored</span> <span class="o">=</span> <span class="bp">True</span>

    <span class="k">def</span> <span class="nf">save_error</span><span class="p">(</span><span class="n">self</span><span class="p">):</span>
        <span class="nf">list</span><span class="p">(</span><span class="n">self</span><span class="p">.</span><span class="n">gen_model</span><span class="p">.</span><span class="nf">values</span><span class="p">())[</span><span class="n">self</span><span class="p">.</span><span class="n">m_id</span><span class="p">].</span><span class="n">err</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span> <span class="o">+=</span> <span class="mi">1</span>
        <span class="n">self</span><span class="p">.</span><span class="n">error_total</span> <span class="o">+=</span> <span class="mi">1</span>

    <span class="k">def</span> <span class="nf">next_model</span><span class="p">(</span><span class="n">self</span><span class="p">):</span>
        <span class="n">self</span><span class="p">.</span><span class="n">m_id</span> <span class="o">=</span> <span class="p">(</span><span class="n">self</span><span class="p">.</span><span class="n">m_id</span><span class="o">+</span><span class="mi">1</span><span class="p">)</span><span class="o">%</span><span class="nf">len</span><span class="p">(</span><span class="n">self</span><span class="p">.</span><span class="n">gen_model</span><span class="p">.</span><span class="nf">keys</span><span class="p">())</span>
        <span class="n">self</span><span class="p">.</span><span class="nf">update_quota</span><span class="p">()</span>

    <span class="k">def</span> <span class="nf">refill_rpm</span><span class="p">(</span><span class="n">self</span><span class="p">):</span>
        <span class="n">self</span><span class="p">.</span><span class="n">running</span> <span class="o">=</span> <span class="bp">False</span>
        <span class="n">self</span><span class="p">.</span><span class="nf">update_quota</span><span class="p">()</span>
        <span class="nf">print</span><span class="p">(</span><span class="sh">"</span><span class="s">Api.refill_rpm</span><span class="sh">"</span><span class="p">,</span> <span class="n">self</span><span class="p">.</span><span class="n">gen_rpm</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">zero_error</span><span class="p">(</span><span class="n">self</span><span class="p">):</span>
        <span class="n">self</span><span class="p">.</span><span class="n">errored</span> <span class="o">=</span> <span class="bp">False</span>
        <span class="n">self</span><span class="p">.</span><span class="n">m_id</span> <span class="o">=</span> <span class="nf">list</span><span class="p">(</span><span class="n">self</span><span class="p">.</span><span class="n">gen_model</span><span class="p">.</span><span class="nf">keys</span><span class="p">()).</span><span class="nf">index</span><span class="p">(</span><span class="n">self</span><span class="p">.</span><span class="n">default_model</span><span class="p">[</span><span class="o">-</span><span class="mi">1</span><span class="p">])</span>
        <span class="n">self</span><span class="p">.</span><span class="nf">update_quota</span><span class="p">()</span>
        <span class="nf">print</span><span class="p">(</span><span class="sh">"</span><span class="s">Api.zero_error: model is now</span><span class="sh">"</span><span class="p">,</span> <span class="nf">list</span><span class="p">(</span><span class="n">self</span><span class="p">.</span><span class="n">gen_model</span><span class="p">.</span><span class="nf">keys</span><span class="p">())[</span><span class="n">self</span><span class="p">.</span><span class="n">m_id</span><span class="p">])</span>

    <span class="k">def</span> <span class="nf">update_quota</span><span class="p">(</span><span class="n">self</span><span class="p">):</span>
        <span class="n">self</span><span class="p">.</span><span class="n">gen_rpm</span> <span class="o">=</span> <span class="nf">list</span><span class="p">(</span><span class="n">self</span><span class="p">.</span><span class="n">gen_model</span><span class="p">.</span><span class="nf">values</span><span class="p">())[</span><span class="n">self</span><span class="p">.</span><span class="n">m_id</span><span class="p">].</span><span class="n">rpm</span><span class="p">[</span><span class="n">self</span><span class="p">.</span><span class="n">args</span><span class="p">.</span><span class="n">API_LIMIT</span><span class="p">]</span>
        <span class="n">self</span><span class="p">.</span><span class="n">token_quota</span> <span class="o">=</span> <span class="nf">list</span><span class="p">(</span><span class="n">self</span><span class="p">.</span><span class="n">gen_model</span><span class="p">.</span><span class="nf">values</span><span class="p">())[</span><span class="n">self</span><span class="p">.</span><span class="n">m_id</span><span class="p">].</span><span class="n">tpm</span><span class="p">[</span><span class="n">self</span><span class="p">.</span><span class="n">args</span><span class="p">.</span><span class="n">API_LIMIT</span><span class="p">]</span><span class="o">*</span><span class="mi">1_000_000</span>

    <span class="k">def</span> <span class="nf">token_count</span><span class="p">(</span><span class="n">self</span><span class="p">,</span> <span class="n">expr</span><span class="p">:</span> <span class="nb">str</span> <span class="o">|</span> <span class="nb">list</span><span class="p">):</span>
        <span class="n">count</span> <span class="o">=</span> <span class="n">self</span><span class="p">.</span><span class="n">args</span><span class="p">.</span><span class="n">CLIENT</span><span class="p">.</span><span class="n">models</span><span class="p">.</span><span class="nf">count_tokens</span><span class="p">(</span>
            <span class="n">model</span><span class="o">=</span><span class="nf">self</span><span class="p">(</span><span class="n">Api</span><span class="p">.</span><span class="n">Model</span><span class="p">.</span><span class="n">GEN</span><span class="p">),</span>
            <span class="n">contents</span><span class="o">=</span><span class="n">json</span><span class="p">.</span><span class="nf">dumps</span><span class="p">(</span><span class="n">expr</span><span class="p">)</span> <span class="k">if</span> <span class="nf">isinstance</span><span class="p">(</span><span class="n">expr</span><span class="p">,</span> <span class="nb">str</span><span class="p">)</span> <span class="k">else</span> <span class="nf">str</span><span class="p">(</span><span class="n">expr</span><span class="p">))</span>
        <span class="k">return</span> <span class="n">count</span><span class="p">.</span><span class="n">total_tokens</span>

    <span class="k">def</span> <span class="nf">errors</span><span class="p">(</span><span class="n">self</span><span class="p">):</span>
        <span class="n">errors</span> <span class="o">=</span> <span class="p">{</span><span class="sh">"</span><span class="s">total</span><span class="sh">"</span><span class="p">:</span> <span class="n">self</span><span class="p">.</span><span class="n">error_total</span><span class="p">,</span> <span class="sh">"</span><span class="s">by_model</span><span class="sh">"</span><span class="p">:</span> <span class="p">{}}</span>
        <span class="k">for</span> <span class="n">m_code</span><span class="p">,</span> <span class="n">m</span> <span class="ow">in</span> <span class="n">self</span><span class="p">.</span><span class="n">gen_model</span><span class="p">.</span><span class="nf">items</span><span class="p">():</span>
            <span class="n">errors</span><span class="p">[</span><span class="sh">"</span><span class="s">by_model</span><span class="sh">"</span><span class="p">].</span><span class="nf">update</span><span class="p">({</span>
                <span class="n">m_code</span><span class="p">:</span> <span class="p">{</span>
                    <span class="sh">"</span><span class="s">api_related</span><span class="sh">"</span><span class="p">:</span> <span class="n">m</span><span class="p">.</span><span class="n">err</span><span class="p">[</span><span class="mi">1</span><span class="p">],</span>
                    <span class="sh">"</span><span class="s">validation</span><span class="sh">"</span><span class="p">:</span> <span class="n">m</span><span class="p">.</span><span class="n">err</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>
                <span class="p">}})</span>
        <span class="k">return</span> <span class="n">errors</span>

    <span class="nd">@retry.Retry</span><span class="p">(</span>
        <span class="n">predicate</span><span class="o">=</span><span class="n">is_retriable</span><span class="p">,</span>
        <span class="n">initial</span><span class="o">=</span><span class="mf">2.0</span><span class="p">,</span>
        <span class="n">maximum</span><span class="o">=</span><span class="mf">64.0</span><span class="p">,</span>
        <span class="n">multiplier</span><span class="o">=</span><span class="mf">2.0</span><span class="p">,</span>
        <span class="n">timeout</span><span class="o">=</span><span class="mi">600</span><span class="p">,</span>
    <span class="p">)</span>
    <span class="k">def</span> <span class="nf">similarity</span><span class="p">(</span><span class="n">self</span><span class="p">,</span> <span class="n">content</span><span class="p">:</span> <span class="nb">list</span><span class="p">):</span>
        <span class="k">return</span> <span class="n">self</span><span class="p">.</span><span class="n">s_embed</span><span class="p">.</span><span class="nf">sts</span><span class="p">(</span><span class="n">content</span><span class="p">)</span> <span class="c1"># type: ignore
</span></code></pre></div></div>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>KeyError: authentication token for LMNR_PROJECT_API_KEY is undefined
Skipping Laminar.initialize()
</code></pre></div></div>

<div class="collapsible-code">
<button type="button">Define the Embedding Function</button>
<div class="language-python highlighter-rouge"><pre class="highlight"><code><span class="c1"># Define the embedding function.
</span><span class="n">api</span> <span class="o">=</span> <span class="nc">NewType</span><span class="p">(</span><span class="sh">"</span><span class="s">api</span><span class="sh">"</span><span class="p">,</span> <span class="n">Api</span><span class="p">)</span> <span class="c1"># type: ignore (forward-decl)
</span><span class="k">class</span> <span class="nc">GeminiEmbedFunction</span><span class="p">:</span>
    <span class="n">document_mode</span> <span class="o">=</span> <span class="bp">True</span>  <span class="c1"># Generate embeddings for documents (T,F), or queries (F,F).
</span>    <span class="n">semantic_mode</span> <span class="o">=</span> <span class="bp">False</span> <span class="c1"># Semantic text similarity mode is exclusive (F,T).
</span>    
    <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="n">self</span><span class="p">,</span> <span class="n">genai_client</span><span class="p">,</span> <span class="n">semantic_mode</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="bp">False</span><span class="p">):</span>
        <span class="n">self</span><span class="p">.</span><span class="n">client</span> <span class="o">=</span> <span class="n">genai_client</span>
        <span class="k">if</span> <span class="n">semantic_mode</span><span class="p">:</span>
            <span class="n">self</span><span class="p">.</span><span class="n">document_mode</span> <span class="o">=</span> <span class="bp">False</span>
            <span class="n">self</span><span class="p">.</span><span class="n">semantic_mode</span> <span class="o">=</span> <span class="bp">True</span>

    <span class="nd">@retry.Retry</span><span class="p">(</span>
        <span class="n">predicate</span><span class="o">=</span><span class="n">is_retriable</span><span class="p">,</span>
        <span class="n">initial</span><span class="o">=</span><span class="mf">2.0</span><span class="p">,</span>
        <span class="n">maximum</span><span class="o">=</span><span class="mf">64.0</span><span class="p">,</span>
        <span class="n">multiplier</span><span class="o">=</span><span class="mf">2.0</span><span class="p">,</span>
        <span class="n">timeout</span><span class="o">=</span><span class="mi">600</span><span class="p">,</span>
    <span class="p">)</span>
    <span class="k">def</span> <span class="nf">__embed__</span><span class="p">(</span><span class="n">self</span><span class="p">,</span> <span class="nb">input</span><span class="p">:</span> <span class="n">Documents</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Embeddings</span><span class="p">:</span>
        <span class="k">if</span> <span class="n">self</span><span class="p">.</span><span class="n">document_mode</span><span class="p">:</span>
            <span class="n">embedding_task</span> <span class="o">=</span> <span class="sh">"</span><span class="s">retrieval_document</span><span class="sh">"</span>
        <span class="k">elif</span> <span class="ow">not</span> <span class="n">self</span><span class="p">.</span><span class="n">document_mode</span> <span class="ow">and</span> <span class="ow">not</span> <span class="n">self</span><span class="p">.</span><span class="n">semantic_mode</span><span class="p">:</span>
            <span class="n">embedding_task</span> <span class="o">=</span> <span class="sh">"</span><span class="s">retrieval_query</span><span class="sh">"</span>
        <span class="k">elif</span> <span class="ow">not</span> <span class="n">self</span><span class="p">.</span><span class="n">document_mode</span> <span class="ow">and</span> <span class="n">self</span><span class="p">.</span><span class="n">semantic_mode</span><span class="p">:</span>
            <span class="n">embedding_task</span> <span class="o">=</span> <span class="sh">"</span><span class="s">semantic_similarity</span><span class="sh">"</span>
        <span class="n">partial</span> <span class="o">=</span> <span class="n">self</span><span class="p">.</span><span class="n">client</span><span class="p">.</span><span class="n">models</span><span class="p">.</span><span class="nf">embed_content</span><span class="p">(</span>
            <span class="n">model</span><span class="o">=</span><span class="nf">api</span><span class="p">(</span><span class="n">Api</span><span class="p">.</span><span class="n">Model</span><span class="p">.</span><span class="n">EMB</span><span class="p">),</span>
            <span class="n">contents</span><span class="o">=</span><span class="nb">input</span><span class="p">,</span>
            <span class="n">config</span><span class="o">=</span><span class="n">types</span><span class="p">.</span><span class="nc">EmbedContentConfig</span><span class="p">(</span><span class="n">task_type</span><span class="o">=</span><span class="n">embedding_task</span><span class="p">))</span> <span class="c1"># type: ignore
</span>        <span class="k">return</span> <span class="p">[</span><span class="n">e</span><span class="p">.</span><span class="n">values</span> <span class="k">for</span> <span class="n">e</span> <span class="ow">in</span> <span class="n">partial</span><span class="p">.</span><span class="n">embeddings</span><span class="p">]</span>
    
    <span class="nd">@retry.Retry</span><span class="p">(</span>
        <span class="n">predicate</span><span class="o">=</span><span class="n">is_retriable</span><span class="p">,</span>
        <span class="n">initial</span><span class="o">=</span><span class="mf">2.0</span><span class="p">,</span>
        <span class="n">maximum</span><span class="o">=</span><span class="mf">64.0</span><span class="p">,</span>
        <span class="n">multiplier</span><span class="o">=</span><span class="mf">2.0</span><span class="p">,</span>
        <span class="n">timeout</span><span class="o">=</span><span class="mi">600</span><span class="p">,</span>
    <span class="p">)</span>
    <span class="k">def</span> <span class="nf">__call__</span><span class="p">(</span><span class="n">self</span><span class="p">,</span> <span class="nb">input</span><span class="p">:</span> <span class="n">Documents</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Embeddings</span><span class="p">:</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="n">response</span> <span class="o">=</span> <span class="p">[]</span>
            <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nf">range</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="nf">len</span><span class="p">(</span><span class="nb">input</span><span class="p">),</span> <span class="n">Api</span><span class="p">.</span><span class="n">Const</span><span class="p">.</span><span class="nc">EmbedBatch</span><span class="p">()):</span>  <span class="c1"># Gemini max-batch-size is 100.
</span>                <span class="n">response</span> <span class="o">+=</span> <span class="n">self</span><span class="p">.</span><span class="nf">__embed__</span><span class="p">(</span><span class="nb">input</span><span class="p">[</span><span class="n">i</span><span class="p">:</span><span class="n">i</span> <span class="o">+</span> <span class="n">Api</span><span class="p">.</span><span class="n">Const</span><span class="p">.</span><span class="nc">EmbedBatch</span><span class="p">()])</span>
            <span class="k">return</span> <span class="n">response</span>
        <span class="k">except</span> <span class="nb">Exception</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
            <span class="nf">print</span><span class="p">(</span><span class="sa">f</span><span class="sh">"</span><span class="s">caught exception of type </span><span class="si">{</span><span class="nf">type</span><span class="p">(</span><span class="n">e</span><span class="p">)</span><span class="si">}</span><span class="se">\n</span><span class="si">{</span><span class="n">e</span><span class="si">}</span><span class="sh">"</span><span class="p">)</span>
            <span class="k">raise</span> <span class="n">e</span>

    <span class="k">def</span> <span class="nf">sts</span><span class="p">(</span><span class="n">self</span><span class="p">,</span> <span class="n">content</span><span class="p">:</span> <span class="nb">list</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">float</span><span class="p">:</span>
        <span class="n">df</span> <span class="o">=</span> <span class="n">pandas</span><span class="p">.</span><span class="nc">DataFrame</span><span class="p">(</span><span class="nf">self</span><span class="p">(</span><span class="n">content</span><span class="p">),</span> <span class="n">index</span><span class="o">=</span><span class="n">content</span><span class="p">)</span>
        <span class="n">score</span> <span class="o">=</span> <span class="n">df</span> <span class="o">@</span> <span class="n">df</span><span class="p">.</span><span class="n">T</span>
        <span class="k">return</span> <span class="n">score</span><span class="p">.</span><span class="n">iloc</span><span class="p">[</span><span class="mi">0</span><span class="p">].</span><span class="n">iloc</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span>
</code></pre></div></div>

<h3 id="set-gemini-api-limit">Set Gemini API Limit</h3>

<div class="collapsible-code">
<button type="button">Set API Limit</button>
<div class="language-python highlighter-rouge"><pre class="highlight"><code><span class="c1"># Instantiate the api-helper with usage limit =&gt; FREE.
# Optional: Set limit here to one of [FREE,TIER_1,TIER_2,TIER_3]
</span><span class="n">api</span> <span class="o">=</span> <span class="nc">Api</span><span class="p">(</span><span class="n">with_limit</span><span class="o">=</span><span class="n">Api</span><span class="p">.</span><span class="n">Limit</span><span class="p">.</span><span class="n">FREE</span><span class="p">,</span> <span class="n">default_model</span><span class="o">=</span><span class="sh">"</span><span class="s">gemini-2.5-flash</span><span class="sh">"</span><span class="p">)</span>
<span class="c1"># Export api environment for agent.
</span><span class="n">os</span><span class="p">.</span><span class="n">environ</span><span class="p">[</span><span class="sh">"</span><span class="s">API_LIMIT</span><span class="sh">"</span><span class="p">]</span><span class="o">=</span><span class="nf">str</span><span class="p">(</span><span class="n">api</span><span class="p">.</span><span class="n">args</span><span class="p">.</span><span class="n">API_LIMIT</span><span class="p">)</span>
<span class="n">os</span><span class="p">.</span><span class="n">environ</span><span class="p">[</span><span class="sh">"</span><span class="s">GEN_DEFAULT</span><span class="sh">"</span><span class="p">]</span><span class="o">=</span><span class="n">api</span><span class="p">.</span><span class="n">args</span><span class="p">.</span><span class="n">GEN_DEFAULT</span>
<span class="c1"># Cleanup old vector_db instances.
</span><span class="err">!</span><span class="n">rm</span> <span class="o">-</span><span class="n">rf</span> <span class="n">vector_db</span>
</code></pre></div></div>

<h1 id="stockchat-agents-edition"><strong>StockChat: Agents Edition</strong></h1>

<p>It was during Kaggle’s 5-day Generative AI course in 2025 that StockChat first existed as a simple search-connected LLM. There were two observations from that initial build. First being the need for a real-time source of grounding truth. Even with google-search data was more often incomplete. The second observation, which still exists today, is the tendency toward hallucinations in finance data. Ticker symbols can imitate the name of another company, and it also possible for the LLM to confuse a company name for a wrong symbol. This happens even when the context of the question matches the immediate discussion history and should be self-evident.</p>

<div class="language-python highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="n">response</span> <span class="o">=</span> <span class="n">chat</span><span class="p">.</span><span class="nf">send_message</span><span class="p">(</span><span class="sh">'''</span><span class="s">What is MGM Studio</span><span class="sh">'</span><span class="s">s stock ticker symbol?</span><span class="sh">'''</span><span class="p">)</span>
<span class="nc">Markdown</span><span class="p">(</span><span class="n">response</span><span class="p">.</span><span class="n">text</span><span class="p">)</span>
</code></pre></div></div>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>... (possibly useful content, often not)

It is important not to confuse MGM Studios with MGM Resorts International, which is a separate, publicly traded hospitality and casino entertainment company with the stock ticker symbol MGM on the New York Stock Exchange (NYSE).
</code></pre></div></div>

<p>Gemini is naturally chatty in a helpful way and this sometimes causes it to go off-topic. The inclusion of off-topic discussion requires that all output from the LLM be checked for topic deviations. Otherwise a backing RAG may store incorrect truths. It became a trade-off between restraining gemini output, and it’s usefulness, versus unrestrained with the hallucination caveat. So google-search was not the solution, and actually it was kind-of off-putting as a source of finance chat. Thus StockChat transformed into a huge monolithic agent with access to multiple finance api’s, and wikipedia/search to back it up.</p>

<div class="language-python highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="nf">send_message</span><span class="p">(</span><span class="sh">"</span><span class="s">What is MGM Studio</span><span class="sh">'</span><span class="s">s stock symbol?</span><span class="sh">"</span><span class="p">)</span>
</code></pre></div></div>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>MGM Studios (Metro-Goldwyn-Mayer Studios, Inc.) is a wholly-owned subsidiary of Amazon and is not publicly traded, so it does not have its own stock symbol.

The stock symbol for its parent company, Amazon, is AMZN.
</code></pre></div></div>

<p>While big and capable, StockChat (SC1) became limited by it’s single agent design.</p>
<ul>
  <li>There’s no parallelism or asynchronous operation because parallel function calling is agent-wide. Some of the functions may have unmet dependencies when run parallel (by an LLM). In other cases the degree of parallelism is determined by whether you have paid for finance api access. As I’m building a toy I wanted to keep free-tier as an option. Effectively SC1 is a big LLM-guided loop with serial operations, and a single rest api request at a time. It makes SC1 stable at the cost of performance.</li>
  <li>The lack of context management means it can handle months worth of pre-scored news data. As a synchronous operation.</li>
  <li>There’s a single vector store with all acquired data, requiring metadata management to compensate.</li>
  <li>It has no facility to determine user interest. It’s a giant cache of previously searched finance data.</li>
  <li>It has no systematic evaluation except to run baseline queries.</li>
</ul>

<p>With these issues in mind my goal during Kaggle’s 5-day Agents course was to apply Google’s agentic framework to free SC1 from these limitations.</p>
<ul>
  <li>SC2 uses async runners while maintaining some minimal thread synchronization on shared data.</li>
  <li>LLM-assisted context compaction runs at regular intervals.</li>
  <li>All the sub-tools have their own vector stores.</li>
  <li>A memory tool stores long-term memories with semantic meaning preserved, and tagged with date of creation.</li>
  <li>A user profile expert is added to extract user attributes for long-term memory.</li>
  <li>Session state keys are used to pass user interest along to other agents.</li>
  <li>A summary writing expert ensures large generations aren’t blemished by erratic markdown, currency or timestamp formatting.</li>
  <li>The ADK CLI is used to run an evaluation suite with LLM-as-judge.</li>
</ul>

<h2 id="setup-working-directory">Setup working directory</h2>

<p>On Kaggle the working directory for ADK runner’s differs from notebook location. To work around this I use git with spare-checkout to pull in SC2’s updated source. Then I setup the Kaggle runner environment and define the async runner.</p>

<div class="collapsible-code">
<button type="button">Setup working directory</button>
<div class="language-python highlighter-rouge"><pre class="highlight"><code><span class="c1"># Setup working directory on Kaggle.
</span><span class="k">if</span> <span class="n">os</span><span class="p">.</span><span class="nf">getenv</span><span class="p">(</span><span class="sh">"</span><span class="s">KAGGLE_KERNEL_RUN_TYPE</span><span class="sh">"</span><span class="p">):</span>
    <span class="k">if</span> <span class="ow">not</span> <span class="n">os</span><span class="p">.</span><span class="n">path</span><span class="p">.</span><span class="nf">isdir</span><span class="p">(</span><span class="sh">"</span><span class="s">sc2/</span><span class="sh">"</span><span class="p">):</span>
        <span class="err">!</span><span class="n">git</span> <span class="n">init</span> <span class="o">-</span><span class="n">b</span> <span class="n">main</span>
        <span class="err">!</span><span class="n">git</span> <span class="n">remote</span> <span class="n">add</span> <span class="n">origin</span> <span class="n">https</span><span class="p">:</span><span class="o">//</span><span class="n">github</span><span class="p">.</span><span class="n">com</span><span class="o">/</span><span class="n">lol</span><span class="o">-</span><span class="n">dungeonmaster</span><span class="o">/</span><span class="n">kaggle</span><span class="o">-</span><span class="n">agents</span><span class="o">-</span><span class="mf">2025.</span><span class="n">git</span>
        <span class="err">!</span><span class="n">git</span> <span class="n">config</span> <span class="n">core</span><span class="p">.</span><span class="n">sparseCheckout</span> <span class="n">true</span>
        <span class="err">!</span><span class="n">echo</span> <span class="sh">"</span><span class="s">sc2/</span><span class="sh">"</span> <span class="o">&gt;&gt;</span> <span class="p">.</span><span class="n">git</span><span class="o">/</span><span class="n">info</span><span class="o">/</span><span class="n">sparse</span><span class="o">-</span><span class="n">checkout</span>
        <span class="err">!</span><span class="n">git</span> <span class="n">pull</span> <span class="n">origin</span> <span class="n">main</span>
        <span class="k">for</span> <span class="n">api_key</span> <span class="ow">in</span> <span class="p">[</span><span class="sh">"</span><span class="s">GOOGLE_API_KEY</span><span class="sh">"</span><span class="p">,</span><span class="sh">"</span><span class="s">POLYGON_API_KEY</span><span class="sh">"</span><span class="p">,</span><span class="sh">"</span><span class="s">FINNHUB_API_KEY</span><span class="sh">"</span><span class="p">]:</span>
            <span class="n">env_key</span> <span class="o">=</span> <span class="nc">UserSecretsClient</span><span class="p">().</span><span class="nf">get_secret</span><span class="p">(</span><span class="n">api_key</span><span class="p">)</span>
            <span class="err">!</span><span class="n">echo</span> <span class="sh">"</span><span class="s">$api_key=$env_key</span><span class="sh">"</span> <span class="o">&gt;&gt;</span> <span class="n">sc2</span><span class="o">/</span><span class="p">.</span><span class="n">env</span> <span class="c1"># from .venv on local runs
</span>            <span class="n">os</span><span class="p">.</span><span class="n">environ</span><span class="p">[</span><span class="n">api_key</span><span class="p">]</span> <span class="o">=</span> <span class="nc">UserSecretsClient</span><span class="p">().</span><span class="nf">get_secret</span><span class="p">(</span><span class="n">api_key</span><span class="p">)</span> <span class="c1"># from .venv on local runs
</span></code></pre></div></div>

<div class="collapsible-code">
<button type="button">Define Async Runner</button>
<div class="language-python highlighter-rouge"><pre class="highlight"><code><span class="c1"># Define async runner and helper functions.
</span><span class="kn">from</span> <span class="n">sc2.agent</span> <span class="kn">import</span> <span class="n">app</span>
<span class="kn">from</span> <span class="n">sc2.src</span> <span class="kn">import</span> <span class="n">log</span>
<span class="c1"># Logger access not possible on Kaggle to prevent hiding errors.
# - The StderrToLog wrapper will not work as kaggle-docker makes the file-descriptor constant.
# - Redirect basic logger output on Kaggle using print().
</span><span class="k">if</span> <span class="n">os</span><span class="p">.</span><span class="nf">getenv</span><span class="p">(</span><span class="sh">"</span><span class="s">KAGGLE_KERNEL_RUN_TYPE</span><span class="sh">"</span><span class="p">):</span>
    <span class="n">log_info</span> <span class="o">=</span> <span class="k">print</span>
    <span class="n">log_warn</span> <span class="o">=</span> <span class="k">print</span>
    <span class="n">log_err</span> <span class="o">=</span> <span class="k">print</span>
<span class="k">else</span><span class="p">:</span>
    <span class="n">log_info</span> <span class="o">=</span> <span class="n">log</span><span class="p">.</span><span class="n">info</span>
    <span class="n">log_warn</span> <span class="o">=</span> <span class="n">log</span><span class="p">.</span><span class="n">warning</span>
    <span class="n">log_err</span> <span class="o">=</span> <span class="n">log</span><span class="p">.</span><span class="n">error</span>

<span class="c1"># Display the user query and response after the response is complete.
</span><span class="k">async</span> <span class="k">def</span> <span class="nf">on_event</span><span class="p">(</span><span class="n">e</span><span class="p">:</span> <span class="n">Event</span><span class="p">,</span> <span class="n">q</span><span class="p">:</span> <span class="nb">str</span><span class="p">):</span>
    <span class="k">try</span><span class="p">:</span>
        <span class="n">response</span> <span class="o">=</span> <span class="n">e</span><span class="p">.</span><span class="n">content</span><span class="p">.</span><span class="n">parts</span><span class="p">[</span><span class="mi">0</span><span class="p">].</span><span class="n">text</span>
        <span class="k">if</span> <span class="n">response</span> <span class="ow">and</span> <span class="n">response</span> <span class="o">!=</span> <span class="sh">"</span><span class="s">None</span><span class="sh">"</span><span class="p">:</span>
            <span class="nf">log_info</span><span class="p">(</span><span class="sa">f</span><span class="sh">"</span><span class="s">USER  &gt; </span><span class="si">{</span><span class="n">q</span><span class="si">}</span><span class="sh">"</span><span class="p">)</span>
            <span class="nf">log_info</span><span class="p">(</span><span class="sa">f</span><span class="sh">"</span><span class="s">MODEL &gt; </span><span class="si">{</span><span class="n">response</span><span class="si">}</span><span class="se">\n</span><span class="sh">"</span><span class="p">)</span>
    <span class="k">except</span> <span class="nb">Exception</span> <span class="k">as</span> <span class="n">err</span><span class="p">:</span>
        <span class="nf">log_err</span><span class="p">(</span><span class="sa">f</span><span class="sh">"</span><span class="s">on_event.exception: </span><span class="si">{</span><span class="nf">str</span><span class="p">(</span><span class="n">err</span><span class="p">)</span><span class="si">}</span><span class="sh">"</span><span class="p">)</span>

<span class="c1"># Run an App with the provided BaseSessionService and user queries list.
</span><span class="k">async</span> <span class="k">def</span> <span class="nf">run_queries</span><span class="p">(</span><span class="n">app</span><span class="p">:</span> <span class="n">App</span><span class="p">,</span> <span class="n">sessions</span><span class="p">:</span> <span class="n">SessionService</span><span class="p">,</span> <span class="n">queries</span><span class="p">:</span> <span class="nb">list</span><span class="p">[</span><span class="nb">str</span><span class="p">],</span>
                      <span class="n">session_id</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="sh">"</span><span class="s">default</span><span class="sh">"</span><span class="p">,</span> <span class="n">user_id</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="sh">"</span><span class="s">default</span><span class="sh">"</span><span class="p">):</span>
    <span class="n">runner</span> <span class="o">=</span> <span class="nc">Runner</span><span class="p">(</span><span class="n">app</span><span class="o">=</span><span class="n">app</span><span class="p">,</span> <span class="n">session_service</span><span class="o">=</span><span class="n">sessions</span><span class="p">)</span>
    <span class="k">try</span><span class="p">:</span>
        <span class="n">session</span> <span class="o">=</span> <span class="k">await</span> <span class="n">sessions</span><span class="p">.</span><span class="nf">create_session</span><span class="p">(</span>
            <span class="n">app_name</span><span class="o">=</span><span class="n">runner</span><span class="p">.</span><span class="n">app_name</span><span class="p">,</span> <span class="n">user_id</span><span class="o">=</span><span class="n">user_id</span><span class="p">,</span> <span class="n">session_id</span><span class="o">=</span><span class="n">session_id</span>
        <span class="p">)</span>
    <span class="k">except</span><span class="p">:</span>
        <span class="n">session</span> <span class="o">=</span> <span class="k">await</span> <span class="n">sessions</span><span class="p">.</span><span class="nf">get_session</span><span class="p">(</span>
            <span class="n">app_name</span><span class="o">=</span><span class="n">runner</span><span class="p">.</span><span class="n">app_name</span><span class="p">,</span> <span class="n">user_id</span><span class="o">=</span><span class="n">user_id</span><span class="p">,</span> <span class="n">session_id</span><span class="o">=</span><span class="n">session_id</span>
        <span class="p">)</span>
    <span class="k">finally</span><span class="p">:</span>
        <span class="nf">log_info</span><span class="p">(</span><span class="sa">f</span><span class="sh">"</span><span class="s">### Agent session: (uid=</span><span class="si">{</span><span class="n">user_id</span><span class="si">}</span><span class="s">) </span><span class="si">{</span><span class="n">session_id</span><span class="si">}</span><span class="se">\n</span><span class="sh">"</span><span class="p">)</span>
        <span class="k">for</span> <span class="n">query</span> <span class="ow">in</span> <span class="n">queries</span><span class="p">:</span>
            <span class="k">await</span> <span class="nf">try_run</span><span class="p">(</span><span class="n">runner</span><span class="p">,</span> <span class="n">session</span><span class="p">,</span> <span class="n">user_id</span><span class="p">,</span> <span class="n">query</span><span class="p">)</span>

<span class="c1"># Launch a runner with the provided session and user_id then respond to query.
# - retries on exceptions TypeError, KeyError, IndexError
</span><span class="k">async</span> <span class="k">def</span> <span class="nf">try_run</span><span class="p">(</span><span class="n">runner</span><span class="p">:</span> <span class="n">Runner</span><span class="p">,</span> <span class="n">session</span><span class="p">:</span> <span class="n">Session</span><span class="p">,</span> <span class="n">user_id</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">query</span><span class="p">:</span> <span class="nb">str</span><span class="p">):</span>
    <span class="k">try</span><span class="p">:</span>
        <span class="n">q</span> <span class="o">=</span> <span class="n">types</span><span class="p">.</span><span class="nc">Content</span><span class="p">(</span><span class="n">role</span><span class="o">=</span><span class="sh">"</span><span class="s">user</span><span class="sh">"</span><span class="p">,</span> <span class="n">parts</span><span class="o">=</span><span class="p">[</span><span class="n">types</span><span class="p">.</span><span class="nc">Part</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">query</span><span class="p">)])</span>
        <span class="k">async</span> <span class="k">for</span> <span class="n">response</span> <span class="ow">in</span> <span class="n">runner</span><span class="p">.</span><span class="nf">run_async</span><span class="p">(</span>
            <span class="n">user_id</span><span class="o">=</span><span class="n">user_id</span><span class="p">,</span> <span class="n">session_id</span><span class="o">=</span><span class="n">session</span><span class="p">.</span><span class="nb">id</span><span class="p">,</span> <span class="n">new_message</span><span class="o">=</span><span class="n">q</span>
        <span class="p">):</span> <span class="k">await</span> <span class="nf">on_event</span><span class="p">(</span><span class="n">response</span><span class="p">,</span> <span class="n">query</span><span class="p">)</span>
    <span class="k">except</span> <span class="nb">Exception</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
        <span class="n">q_id</span> <span class="o">=</span> <span class="sh">"</span><span class="s"> </span><span class="sh">"</span><span class="p">.</span><span class="nf">join</span><span class="p">(</span><span class="n">query</span><span class="p">.</span><span class="nf">split</span><span class="p">()[:</span><span class="mi">4</span><span class="p">])</span>
        <span class="k">if</span> <span class="nf">type</span><span class="p">(</span><span class="n">e</span><span class="p">)</span> <span class="ow">in</span> <span class="p">[</span><span class="nb">TypeError</span><span class="p">,</span> <span class="nb">KeyError</span><span class="p">,</span> <span class="nb">IndexError</span><span class="p">]:</span>
            <span class="nf">log_warn</span><span class="p">(</span><span class="sa">f</span><span class="sh">"</span><span class="s">try_run.run_async (q=</span><span class="si">{</span><span class="n">q_id</span><span class="si">}</span><span class="s">): retrying, generated </span><span class="si">{</span><span class="nf">type</span><span class="p">(</span><span class="n">e</span><span class="p">).</span><span class="n">__name__</span><span class="si">}</span><span class="se">\n</span><span class="sh">"</span><span class="p">)</span>
            <span class="n">time</span><span class="p">.</span><span class="nf">sleep</span><span class="p">(</span><span class="mf">15.0</span><span class="p">)</span>
            <span class="k">await</span> <span class="nf">try_run</span><span class="p">(</span><span class="n">runner</span><span class="p">,</span> <span class="n">session</span><span class="p">,</span> <span class="n">user_id</span><span class="p">,</span> <span class="n">query</span><span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="nf">log_warn</span><span class="p">(</span><span class="sa">f</span><span class="sh">"</span><span class="s">try_run.run_async (q=</span><span class="si">{</span><span class="n">q_id</span><span class="si">}</span><span class="s">): </span><span class="si">{</span><span class="nf">type</span><span class="p">(</span><span class="n">e</span><span class="p">).</span><span class="n">__name__</span><span class="si">}</span><span class="s"> - </span><span class="si">{</span><span class="nf">str</span><span class="p">(</span><span class="n">e</span><span class="p">)</span><span class="si">}</span><span class="se">\n</span><span class="sh">"</span><span class="p">)</span>

<span class="c1"># Check for compaction events in the provided BaseSessionService.
# - optionally also show the llm compacted output.
</span><span class="k">async</span> <span class="k">def</span> <span class="nf">check_compaction</span><span class="p">(</span><span class="n">sessions</span><span class="p">:</span> <span class="n">SessionService</span><span class="p">,</span> <span class="n">session_id</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="sh">"</span><span class="s">default</span><span class="sh">"</span><span class="p">,</span> 
                           <span class="n">user_id</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="sh">"</span><span class="s">default</span><span class="sh">"</span><span class="p">,</span> <span class="n">show_llm</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="bp">False</span><span class="p">):</span>
    <span class="n">n</span> <span class="o">=</span> <span class="mi">0</span>
    <span class="k">for</span> <span class="n">e</span> <span class="ow">in</span> <span class="p">(</span><span class="k">await</span> <span class="n">sessions</span><span class="p">.</span><span class="nf">get_session</span><span class="p">(</span>
        <span class="n">app_name</span><span class="o">=</span><span class="n">app</span><span class="p">.</span><span class="n">name</span><span class="p">,</span>
        <span class="n">user_id</span><span class="o">=</span><span class="n">user_id</span><span class="p">,</span>
        <span class="n">session_id</span><span class="o">=</span><span class="n">session_id</span><span class="p">,</span>
    <span class="p">)).</span><span class="n">events</span><span class="p">:</span>
        <span class="k">if</span> <span class="n">e</span><span class="p">.</span><span class="n">actions</span> <span class="ow">and</span> <span class="p">(</span><span class="n">llm_out</span> <span class="p">:</span><span class="o">=</span> <span class="n">e</span><span class="p">.</span><span class="n">actions</span><span class="p">.</span><span class="n">compaction</span><span class="p">):</span>
            <span class="n">n</span> <span class="o">+=</span> <span class="mi">1</span>
            <span class="k">if</span> <span class="n">show_llm</span><span class="p">:</span>
                <span class="nf">log_info</span><span class="p">(</span><span class="sa">f</span><span class="sh">"</span><span class="s">check_compaction.show_llm: </span><span class="si">{</span><span class="n">llm_out</span><span class="p">.</span><span class="n">compacted_content</span><span class="p">.</span><span class="n">parts</span><span class="p">[</span><span class="mi">0</span><span class="p">].</span><span class="n">text</span><span class="si">}</span><span class="se">\n</span><span class="sh">"</span><span class="p">)</span>
    <span class="nf">log_info</span><span class="p">(</span><span class="sa">f</span><span class="sh">"</span><span class="s">check_compaction: found (</span><span class="si">{</span><span class="n">n</span><span class="si">}</span><span class="s">) compaction event</span><span class="se">\n</span><span class="sh">"</span><span class="p">)</span>
</code></pre></div></div>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>WARNING  [root] KeyError: authentication token for LMNR_PROJECT_API_KEY is undefined
INFO     [root] Skipping Laminar.initialize()
INFO     [root] sc2.__init__: the api-helper is ready
Generate document embedding:   0%|          | 0/1 [00:00&lt;?, ?it/s]
Generate document embedding: 100%|##########| 1/1 [00:03&lt;00:00,  3.99s/it]
Generate document embedding: 100%|##########| 1/1 [00:04&lt;00:00,  4.13s/it]
INFO     [root] sc2.__init__: RestGroundingTool is ready
INFO     [root] sc2.__init__: SearchGroundingTool is ready
INFO     [root] sc2.__init__: WikiGroundingTool is ready
INFO     [root] sc2.__init__: MemoryService is ready
WARNING  [root] [EXPERIMENTAL] ReflectAndRetryToolPlugin: This feature is experimental and may change or be removed in future versions without notice. It may introduce breaking changes at any time.
  plugins=[ReflectAndRetryToolPlugin(max_retries=1)],
WARNING  [root] [EXPERIMENTAL] EventsCompactionConfig: This feature is experimental and may change or be removed in future versions without notice. It may introduce breaking changes at any time.
  events_compaction_config=EventsCompactionConfig(
</code></pre></div></div>

<h2 id="test-the-runner">Test the Runner</h2>

<p>The initial two-questions are used to test the agents self-awareness of tools. This was particularly problematic for the parallel <code class="language-plaintext highlighter-rouge">fncall_pipeline</code>. The goal is to have a parallel operating planner and executor of function calls. The function tool definition are tricky to access reliably when nested inside workflow agents like the ParallelAgent. In the end I exposed the planner and it’s containing pipeline, then told Gemini where to look.</p>

<p>My goal is ultimately to make SC2 a more capable assistant in addition to removing existing limits. To that end I also added a Terminology expert to make use of the built-in google-search. Meanwhile a user profile expert dynamically extracts preferences and user attributes. These two types of data are stored in long-term memory.</p>

<div class="language-python highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="c1"># Create a session service and run some test queries.
</span><span class="n">s_svc</span> <span class="o">=</span> <span class="nc">InMemorySessionService</span><span class="p">()</span>

<span class="k">await</span> <span class="nf">run_queries</span><span class="p">(</span>
    <span class="n">app</span><span class="o">=</span><span class="n">app</span><span class="p">,</span> <span class="n">sessions</span><span class="o">=</span><span class="n">s_svc</span><span class="p">,</span>
    <span class="n">queries</span><span class="o">=</span><span class="p">[</span>
        <span class="sh">"</span><span class="s">What tools do you know how to use?</span><span class="sh">"</span><span class="p">,</span>
        <span class="sh">"</span><span class="s">Tell me what functions `fncall_pipeline` knows by checking `sc2_fnplan`.</span><span class="sh">"</span><span class="p">,</span>
        <span class="sh">"</span><span class="s">What is a short trade?</span><span class="sh">"</span><span class="p">,</span>
        <span class="sh">"</span><span class="s">What is gambler</span><span class="sh">'</span><span class="s">s ruin?</span><span class="sh">"</span><span class="p">,</span>
        <span class="sh">"</span><span class="s">My local advisor is SC at JPMorgan Chase, 212-736-2001</span><span class="sh">"</span><span class="p">,</span>
        <span class="sh">"</span><span class="s">I live in Brooklyn, New York.</span><span class="sh">"</span><span class="p">])</span>
</code></pre></div></div>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>INFO     [root] ### Agent session: (uid=default) default

INFO     [root] USER  &gt; What tools do you know how to use?
INFO     [root] MODEL &gt; I can use the following tools:

*   `sc2_memory`: An expert writer of long-term memories.
*   `sc2_prefs`: An expert profile analyst in the field of finance, money, and stock markets.
*   `fncall_pipeline`: A function caller with functions defined in sub-agent `sc2_fnplan`.
*   `sc2_fnplan`: A highly intelligent FunctionTool call planner.
*   `sc2_terms`: An expert terminologist in the field of finance, money, and stock markets.
*   `sc2_summary`: An expert proof-reader and writer that knows HTML, JSON and Markdown.

INFO     [root] USER  &gt; Tell me what functions `fncall_pipeline` knows by checking `sc2_fnplan`.
INFO     [root] MODEL &gt; `fncall_pipeline` knows the following functions:

*   `get_symbol_1`
*   `get_symbols_1`
*   `get_name_1`
*   `get_symbol_quote_1`
*   `get_market_status_1`
*   `get_market_session_1`
*   `get_company_peers_1`
*   `get_local_datetime`
*   `get_last_market_close`
*   `get_exchange_codes_1`
*   `get_exchange_code_1`
*   `get_financials_1`
*   `get_daily_candlestick_2`
*   `get_custom_candlestick_2`
*   `get_ticker_overview_2`
*   `get_recommendation_trends_1`
*   `get_news_with_sentiment_2`
*   `get_wiki_grounding`
*   `get_search_grounding`

Generate memory embedding (Short Trade):   0%|          | 0/1 [00:00&lt;?, ?it/s]
Generate memory embedding (Short Trade): 100%|##########| 1/1 [00:00&lt;00:00,  1.47it/s]
Generate memory embedding (Short Trade): 100%|##########| 1/1 [00:00&lt;00:00,  1.40it/s]
INFO     [root] USER  &gt; What is a short trade?
INFO     [root] MODEL &gt; A short trade, also known as short selling, is a speculative strategy where an investor sells borrowed securities with the expectation of repurchasing them at a lower price. The objective is to profit from a decrease in the security's price. If the price declines, the investor can buy the shares at a reduced cost, return them to the lender, and gain the difference. Conversely, if the price increases, the investor must buy them back at a higher price, resulting in a loss.

Generate memory embedding (Gambler's ruin):   0%|          | 0/1 [00:00&lt;?, ?it/s]
Generate memory embedding (Gambler's ruin): 100%|##########| 1/1 [00:00&lt;00:00,  1.25it/s]
Generate memory embedding (Gambler's ruin): 100%|##########| 1/1 [00:00&lt;00:00,  1.20it/s]
INFO     [root] USER  &gt; What is gambler's ruin?
INFO     [root] MODEL &gt; Gambler's Ruin

Gambler's ruin is a concept within probability theory. It posits that a gambler possessing a finite sum of money, engaging in a game against an opponent with an effectively infinite amount of money, will inevitably deplete their entire funds. This outcome holds true regardless of whether the game is fair or if the odds are even slightly in the gambler's favor.


Generate memory embedding (local advisor):   0%|          | 0/1 [00:00&lt;?, ?it/s]
Generate memory embedding (local advisor): 100%|##########| 1/1 [00:00&lt;00:00,  1.82it/s]
Generate memory embedding (local advisor): 100%|##########| 1/1 [00:00&lt;00:00,  1.72it/s]
INFO     [root] USER  &gt; My local advisor is SC at JPMorgan Chase, 212-736-2001
INFO     [root] MODEL &gt; I've noted that your local advisor is SC at JPMorgan Chase, phone number 212-736-2001.

Generate memory embedding (User's residence):   0%|          | 0/1 [00:00&lt;?, ?it/s]
Generate memory embedding (User's residence): 100%|##########| 1/1 [00:01&lt;00:00,  1.62s/it]
Generate memory embedding (User's residence): 100%|##########| 1/1 [00:01&lt;00:00,  1.65s/it]
INFO     [root] USER  &gt; I live in Brooklyn, New York.
INFO     [root] MODEL &gt; Okay, I've noted that you live in Brooklyn, New York.
</code></pre></div></div>

<h2 id="test-long-term-memory">Test Long-term Memory</h2>

<p>Testing long-term memory is as easy as creating a new <code class="language-plaintext highlighter-rouge">BaseSessionService</code>. As this Memory is a custom implementation it must be specified as a tool during user query.</p>

<div class="language-python highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="c1"># Use long-term memory from a new session.
</span><span class="n">s_svc2</span> <span class="o">=</span> <span class="nc">InMemorySessionService</span><span class="p">()</span>

<span class="k">await</span> <span class="nf">run_queries</span><span class="p">(</span>
    <span class="n">app</span><span class="o">=</span><span class="n">app</span><span class="p">,</span> <span class="n">sessions</span><span class="o">=</span><span class="n">s_svc2</span><span class="p">,</span>
    <span class="n">queries</span><span class="o">=</span><span class="p">[</span>
        <span class="sh">"</span><span class="s">Check memory for where I live.</span><span class="sh">"</span><span class="p">,</span>
        <span class="sh">"</span><span class="s">Check memory for my local advisor SCs phone number.</span><span class="sh">"</span><span class="p">])</span>
</code></pre></div></div>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>INFO     [root] ### Agent session: (uid=default) default

INFO     [root] Api.refill_rpm 10
INFO     [root] USER  &gt; Check memory for where I live.
INFO     [root] MODEL &gt; You live in Brooklyn, New York.

INFO     [root] USER  &gt; Check memory for my local advisor SCs phone number.
INFO     [root] MODEL &gt; SC's phone number is 212-736-2001.
</code></pre></div></div>

<h2 id="check-for-compaction">Check for compaction</h2>

<p>One of the features of SC2 that I’m looking forward to working with more is the LLM-assisted context compaction. In this implementation I’ve opted for zero-overlap to avoid re-summarizing past events. At this point no events are dropped from the context. The LLM is known to become confused with statement repetition, so let’s avoid that complication. A delightful feature of LLM-compaction is the use of an LLM-as-judge to assess the summary quality with impartiality. It’ll note neat things for you like when the tools fail completely or when parts of a user query remain unanswered.</p>

<div class="language-python highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="c1"># Display context compaction output.
</span><span class="k">await</span> <span class="nf">check_compaction</span><span class="p">(</span><span class="n">s_svc</span><span class="p">,</span> <span class="n">show_llm</span><span class="o">=</span><span class="bp">True</span><span class="p">)</span>
</code></pre></div></div>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>INFO     [root] check_compaction.show_llm: The user initiated the conversation by asking about the AI's available tools. The AI listed its tools, including `sc2_memory`, `sc2_prefs`, `fncall_pipeline`, `sc2_fnplan`, `sc2_terms`, and `sc2_summary`, along with their brief descriptions.

Next, the user asked the AI to specify the functions available through `fncall_pipeline` by checking `sc2_fnplan`. The AI responded by listing 20 specific functions, predominantly related to financial data retrieval (e.g., `get_symbol_1`, `get_market_status_1`, `get_financials_1`, `get_news_with_sentiment_2`).

Finally, the user asked for a definition of "short trade." The AI provided a clear explanation, describing it as a speculative strategy where an investor sells borrowed securities with the expectation of repurchasing them at a lower price to profit from a price decrease.

**Key information and decisions made:**
*   The AI disclosed its capabilities in terms of tools and specific functions.
*   The AI provided a detailed definition of a financial term requested by the user.

**Unresolved questions or tasks:**
*   There are no explicit unresolved questions or tasks at the end of this conversation segment.

INFO     [root] check_compaction.show_llm: The conversation began with the user asking for a definition of "gambler's ruin," which the AI successfully provided. Subsequently, the user volunteered two pieces of personal information: their local advisor (SC at JPMorgan Chase, 212-736-2001) and their residence (Brooklyn, New York). The AI acknowledged and noted both details.

**Key Information &amp; Decisions:**
*   **Definition Provided:** The AI explained "gambler's ruin."
*   **Advisor Details Noted:** The AI recorded the user's advisor (SC, JPMorgan Chase, 212-736-2001).
*   **Residence Noted:** The AI recorded the user's residence (Brooklyn, New York).

**Unresolved Questions or Tasks:**
There are no unresolved questions or tasks in this segment of the conversation.

INFO     [root] check_compaction: found (2) compaction event
</code></pre></div></div>

<h2 id="evaluation-by-cli">Evaluation by CLI</h2>

<p>In SC1 evaluation didn’t happen systematically. As you can see from the appendix evaluation consists of manually checking the model output, or baseline. In leveraging the ADK CLI, SC2 gains an LLM-as-judge to systematically evaluate assistant output. A rubric is applied to check response quality and related tool use. Then a hallucination test is performed to ensure the agent has stayed on-topic.</p>

<div class="language-python highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="err">!</span><span class="n">adk</span> <span class="nb">eval</span> <span class="n">sc2</span> <span class="n">sc2</span><span class="o">/</span><span class="nb">eval</span><span class="o">/</span><span class="n">test_cases</span><span class="p">.</span><span class="n">json</span> <span class="o">--</span><span class="n">config_file_path</span><span class="o">=</span><span class="n">sc2</span><span class="o">/</span><span class="nb">eval</span><span class="o">/</span><span class="n">config</span><span class="p">.</span><span class="n">json</span> <span class="o">--</span><span class="n">print_detailed_results</span>
</code></pre></div></div>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>/home/sysop/Documents/kaggle-agents-2025/.venv/lib/python3.12/site-packages/google/adk/evaluation/metric_evaluator_registry.py:90: UserWarning: [EXPERIMENTAL] MetricEvaluatorRegistry: This feature is experimental and may change or be removed in future versions without notice. It may introduce breaking changes at any time.
  metric_evaluator_registry = MetricEvaluatorRegistry()
/home/sysop/Documents/kaggle-agents-2025/.venv/lib/python3.12/site-packages/google/adk/evaluation/local_eval_service.py:80: UserWarning: [EXPERIMENTAL] UserSimulatorProvider: This feature is experimental and may change or be removed in future versions without notice. It may introduce breaking changes at any time.
  user_simulator_provider: UserSimulatorProvider = UserSimulatorProvider(),
Using evaluation criteria: criteria={'rubric_based_final_response_quality_v1': BaseCriterion(threshold=0.8, judge_model_options={'judge_model': 'gemini-2.5-flash', 'num_samples': 1}, rubrics=[{'rubric_id': 'conciseness', 'rubric_content': {'text_property': "The agent's response is direct and to the point."}}, {'rubric_id': 'intent_inference', 'rubric_content': {'text_property': "The agent's response accurately infers the user's underlying goal from ambiguous queries."}}]), 'rubric_based_tool_use_quality_v1': BaseCriterion(threshold=1.0, judge_model_options={'judge_model': 'gemini-2.5-flash', 'num_samples': 1}, rubrics=[{'rubric_id': 'prefs_called', 'rubric_content': {'text_property': 'The agent calls `sc2_prefs` to store profile data when required.'}}, {'rubric_id': 'memory_called_before', 'rubric_content': {'text_property': 'The agent calls `sc2_memory` before `sc2_terms` or `fncall_pipeline`.'}}, {'rubric_id': 'memory_called_after', 'rubric_content': {'text_property': 'The agent calls `sc2_memory` after `sc2_terms` only for new memories.'}}, {'rubric_id': 'summary_called', 'rubric_content': {'text_property': 'The agent calls `sc2_summary` last when used.'}}, {'rubric_id': 'workflow_bypass', 'rubric_content': {'text_property': 'The agent can bypass the workflow for usage related questions.'}}]), 'hallucinations_v1': BaseCriterion(threshold=0.8, judge_model_options={'judge_model': 'gemini-2.5-flash'}, evaluate_intermediate_nl_responses=True)} user_simulator_config=None
2025-12-01 06:49:13,997 - WARNING - secret.py:13 - KeyError: authentication token for LMNR_PROJECT_API_KEY is undefined
2025-12-01 06:49:13,998 - INFO - __init__.py:54 - Skipping Laminar.initialize()
2025-12-01 06:49:14,229 - INFO - __init__.py:64 - sc2.__init__: the api-helper is ready
Generate document embedding:   0%|          | 0/1 [00:00&lt;?, ?it/s]
Generate document embedding: 100%|##########| 1/1 [00:03&lt;00:00,  3.71s/it]
Generate document embedding: 100%|##########| 1/1 [00:03&lt;00:00,  3.80s/it]
2025-12-01 06:49:18,839 - INFO - __init__.py:72 - sc2.__init__: RestGroundingTool is ready
2025-12-01 06:49:18,840 - INFO - __init__.py:74 - sc2.__init__: SearchGroundingTool is ready
2025-12-01 06:49:18,841 - INFO - __init__.py:76 - sc2.__init__: WikiGroundingTool is ready
2025-12-01 06:49:18,842 - INFO - __init__.py:78 - sc2.__init__: MemoryService is ready
2025-12-01 06:49:18,890 - WARNING - __init__.py:26 - [EXPERIMENTAL] ReflectAndRetryToolPlugin: This feature is experimental and may change or be removed in future versions without notice. It may introduce breaking changes at any time.
  plugins=[ReflectAndRetryToolPlugin(max_retries=1)],
2025-12-01 06:49:18,939 - WARNING - __init__.py:26 - [EXPERIMENTAL] EventsCompactionConfig: This feature is experimental and may change or be removed in future versions without notice. It may introduce breaking changes at any time.
  events_compaction_config=EventsCompactionConfig(
2025-12-01 06:49:18,939 - WARNING - __init__.py:26 - [EXPERIMENTAL] UserSimulatorProvider: This feature is experimental and may change or be removed in future versions without notice. It may introduce breaking changes at any time.
  user_simulator_provider = UserSimulatorProvider(
2025-12-01 06:49:18,940 - WARNING - __init__.py:26 - [EXPERIMENTAL] LocalEvalService: This feature is experimental and may change or be removed in future versions without notice. It may introduce breaking changes at any time.
  eval_service = LocalEvalService(
2025-12-01 06:49:18,941 - WARNING - __init__.py:26 - [EXPERIMENTAL] StaticUserSimulator: This feature is experimental and may change or be removed in future versions without notice. It may introduce breaking changes at any time.
  return StaticUserSimulator(static_conversation=eval_case.conversation)
2025-12-01 06:49:18,942 - WARNING - __init__.py:26 - [EXPERIMENTAL] UserSimulator: This feature is experimental and may change or be removed in future versions without notice. It may introduce breaking changes at any time.
  super().__init__(
2025-12-01 06:49:20,706 - WARNING - types.py:6334 - Warning: there are non-text parts in the response: ['function_call'], returning concatenated text result from text parts. Check the full candidates.content.parts accessor to get the full model response.
2025-12-01 06:49:20,804 - WARNING - types.py:6334 - Warning: there are non-text parts in the response: ['function_call'], returning concatenated text result from text parts. Check the full candidates.content.parts accessor to get the full model response.
2025-12-01 06:49:21,234 - WARNING - types.py:6334 - Warning: there are non-text parts in the response: ['function_call'], returning concatenated text result from text parts. Check the full candidates.content.parts accessor to get the full model response.
2025-12-01 06:49:21,335 - WARNING - types.py:6334 - Warning: there are non-text parts in the response: ['function_call'], returning concatenated text result from text parts. Check the full candidates.content.parts accessor to get the full model response.
2025-12-01 06:49:22,239 - WARNING - types.py:6334 - Warning: there are non-text parts in the response: ['function_call'], returning concatenated text result from text parts. Check the full candidates.content.parts accessor to get the full model response.
2025-12-01 06:49:22,288 - WARNING - types.py:6334 - Warning: there are non-text parts in the response: ['function_call'], returning concatenated text result from text parts. Check the full candidates.content.parts accessor to get the full model response.
2025-12-01 06:49:23,182 - WARNING - types.py:6334 - Warning: there are non-text parts in the response: ['function_call'], returning concatenated text result from text parts. Check the full candidates.content.parts accessor to get the full model response.
2025-12-01 06:49:25,574 - WARNING - types.py:6334 - Warning: there are non-text parts in the response: ['function_call'], returning concatenated text result from text parts. Check the full candidates.content.parts accessor to get the full model response.
2025-12-01 06:49:25,576 - WARNING - types.py:6334 - Warning: there are non-text parts in the response: ['function_call'], returning concatenated text result from text parts. Check the full candidates.content.parts accessor to get the full model response.
2025-12-01 06:49:25,577 - WARNING - types.py:6334 - Warning: there are non-text parts in the response: ['function_call'], returning concatenated text result from text parts. Check the full candidates.content.parts accessor to get the full model response.
2025-12-01 06:49:36,695 - WARNING - types.py:6334 - Warning: there are non-text parts in the response: ['function_call'], returning concatenated text result from text parts. Check the full candidates.content.parts accessor to get the full model response.
2025-12-01 06:49:38,488 - WARNING - types.py:6334 - Warning: there are non-text parts in the response: ['function_call'], returning concatenated text result from text parts. Check the full candidates.content.parts accessor to get the full model response.
2025-12-01 06:49:39,862 - WARNING - types.py:6334 - Warning: there are non-text parts in the response: ['function_call'], returning concatenated text result from text parts. Check the full candidates.content.parts accessor to get the full model response.
2025-12-01 06:49:46,575 - WARNING - __init__.py:26 - [EXPERIMENTAL] RubricBasedFinalResponseQualityV1Evaluator: This feature is experimental and may change or be removed in future versions without notice. It may introduce breaking changes at any time.
  return self._registry[eval_metric.metric_name][0](eval_metric=eval_metric)
2025-12-01 06:49:46,577 - WARNING - __init__.py:26 - [EXPERIMENTAL] RubricBasedEvaluator: This feature is experimental and may change or be removed in future versions without notice. It may introduce breaking changes at any time.
  super().__init__(
2025-12-01 06:49:46,580 - WARNING - __init__.py:26 - [EXPERIMENTAL] LlmAsJudge: This feature is experimental and may change or be removed in future versions without notice. It may introduce breaking changes at any time.
  super().__init__(
2025-12-01 06:49:51,285 - WARNING - __init__.py:26 - [EXPERIMENTAL] RubricBasedToolUseV1Evaluator: This feature is experimental and may change or be removed in future versions without notice. It may introduce breaking changes at any time.
  return self._registry[eval_metric.metric_name][0](eval_metric=eval_metric)
2025-12-01 06:49:51,288 - WARNING - __init__.py:26 - [EXPERIMENTAL] RubricBasedEvaluator: This feature is experimental and may change or be removed in future versions without notice. It may introduce breaking changes at any time.
  super().__init__(
INFO     [root] Api.refill_rpm 10
2025-12-01 06:50:07,623 - WARNING - __init__.py:26 - [EXPERIMENTAL] HallucinationsV1Evaluator: This feature is experimental and may change or be removed in future versions without notice. It may introduce breaking changes at any time.
  return self._registry[eval_metric.metric_name][0](eval_metric=eval_metric)
2025-12-01 06:50:16,247 - INFO - local_eval_set_results_manager.py:62 - Writing eval result to file: /home/sysop/Documents/kaggle-agents-2025/sc2/.adk/eval_history/sc2_sc2_eval_suite_1764589816.2472925.evalset_result.json
2025-12-01 06:50:18,639 - INFO - local_eval_set_results_manager.py:62 - Writing eval result to file: /home/sysop/Documents/kaggle-agents-2025/sc2/.adk/eval_history/sc2_sc2_eval_suite_1764589818.6387215.evalset_result.json
2025-12-01 06:50:20,395 - INFO - local_eval_set_results_manager.py:62 - Writing eval result to file: /home/sysop/Documents/kaggle-agents-2025/sc2/.adk/eval_history/sc2_sc2_eval_suite_1764589820.395301.evalset_result.json
2025-12-01 06:50:24,276 - INFO - api.py:225 - Api.refill_rpm 10
2025-12-01 06:50:29,980 - INFO - local_eval_set_results_manager.py:62 - Writing eval result to file: /home/sysop/Documents/kaggle-agents-2025/sc2/.adk/eval_history/sc2_sc2_eval_suite_1764589829.9797585.evalset_result.json
2025-12-01 06:50:39,274 - INFO - local_eval_set_results_manager.py:62 - Writing eval result to file: /home/sysop/Documents/kaggle-agents-2025/sc2/.adk/eval_history/sc2_sc2_eval_suite_1764589839.2740445.evalset_result.json
2025-12-01 06:50:40,440 - INFO - local_eval_set_results_manager.py:62 - Writing eval result to file: /home/sysop/Documents/kaggle-agents-2025/sc2/.adk/eval_history/sc2_sc2_eval_suite_1764589840.4402955.evalset_result.json
*********************************************************************
Eval Run Summary
sc2_eval_suite:
  Tests passed: 6
  Tests failed: 0
********************************************************************
Eval Set Id: sc2_eval_suite
Eval Id: create_memory_2
Overall Eval Status: PASSED
---------------------------------------------------------------------
Metric: rubric_based_final_response_quality_v1, Status: PASSED, Score: 1.0, Threshold: 0.8
Rubric Scores:
Rubric: The agent's response is direct and to the point., Score: 1.0, Reasoning: This is an aggregated score derived from individual entries. Please refer to individual entries in each invocation for actual rationale from the model.
Rubric: The agent's response accurately infers the user's underlying goal from ambiguous queries., Score: 1.0, Reasoning: This is an aggregated score derived from individual entries. Please refer to individual entries in each invocation for actual rationale from the model.
---------------------------------------------------------------------
Metric: rubric_based_tool_use_quality_v1, Status: PASSED, Score: 1.0, Threshold: 1.0
Rubric Scores:
Rubric: The agent calls `sc2_prefs` to store profile data when required., Score: 1.0, Reasoning: This is an aggregated score derived from individual entries. Please refer to individual entries in each invocation for actual rationale from the model.
Rubric: The agent calls `sc2_memory` before `sc2_terms` or `fncall_pipeline`., Score: 1.0, Reasoning: This is an aggregated score derived from individual entries. Please refer to individual entries in each invocation for actual rationale from the model.
Rubric: The agent calls `sc2_memory` after `sc2_terms` only for new memories., Score: 1.0, Reasoning: This is an aggregated score derived from individual entries. Please refer to individual entries in each invocation for actual rationale from the model.
Rubric: The agent calls `sc2_summary` last when used., Score: 1.0, Reasoning: This is an aggregated score derived from individual entries. Please refer to individual entries in each invocation for actual rationale from the model.
Rubric: The agent can bypass the workflow for usage related questions., Score: 1.0, Reasoning: This is an aggregated score derived from individual entries. Please refer to individual entries in each invocation for actual rationale from the model.
---------------------------------------------------------------------
Metric: hallucinations_v1, Status: PASSED, Score: 1.0, Threshold: 0.8
---------------------------------------------------------------------
Invocation Details:
+----+-------------------------+------------------------+---------------------------+-----------------------+---------------------------+------------------------------------------+------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+------------------------------------+----------------------------------------------------------------------------+---------------------------------------------------------------------------------+---------------------------------------------------------------------------------+---------------------------------------------------------+--------------------------------------------------------------------------+------------------------+
|    | prompt                  | expected_response      | actual_response           | expected_tool_calls   | actual_tool_calls         | rubric_based_final_response_quality_v1   | Rubric: The agent's response is direct and to the point.   | Rubric: The agent's response accurately infers the user's underlying goal from ambiguous queries.   | rubric_based_tool_use_quality_v1   | Rubric: The agent calls `sc2_prefs` to store profile data when required.   | Rubric: The agent calls `sc2_memory` before `sc2_terms` or `fncall_pipeline`.   | Rubric: The agent calls `sc2_memory` after `sc2_terms` only for new memories.   | Rubric: The agent calls `sc2_summary` last when used.   | Rubric: The agent can bypass the workflow for usage related questions.   | hallucinations_v1      |
+====+=========================+========================+===========================+=======================+===========================+==========================================+============================================================+=====================================================================================================+====================================+============================================================================+=================================================================================+=================================================================================+=========================================================+==========================================================================+========================+
|  0 | I live in Brooklyn, New | I have saved where you | It's great to know that   |                       | id='adk-0a21d28d-e189-43f | Status: PASSED, Score:                   | Reasoning: The final                                       | Reasoning: The user's                                                                               | Status: PASSED, Score:             | Reasoning: The user                                                        | Reasoning: The agent did                                                        | Reasoning: The agent did                                                        | Reasoning: The agent did                                | Reasoning: The user's                                                    | Status: PASSED, Score: |
|    | York.                   | live in memory.        | you live in Brooklyn, New |                       | 9-a917- 179ac463535c'     | 1.0                                      | answer directly addresses                                  | query "I live in                                                                                    | 1.0                                | provided profile                                                           | not call `sc2_memory`,                                                          | not call `sc2_memory` or                                                        | not call `sc2_summary` in                               | prompt ("I live in                                                       | 1.0                    |
|    |                         |                        | York! I've saved this     |                       | args={'request': 'The     |                                          | the user's input by                                        | Brooklyn, New York" is a                                                                            |                                    | information ("I live in                                                    | `sc2_terms`, or                                                                 | `sc2_terms` in its                                                              | its response., Score: 1.0                               | Brooklyn, New York") is                                                  |                        |
|    |                         |                        | information to your       |                       | user lives in Brooklyn,   |                                          | acknowledging the                                          | direct statement of fact                                                                            |                                    | Brooklyn, New York"), and                                                  | `fncall_pipeline` in its                                                        | response, so the                                                                |                                                         | not a usage- related                                                     |                        |
|    |                         |                        | profile. If you have any  |                       | New York.'}               |                                          | information, stating it                                    | and is not ambiguous. The                                                                           |                                    | the agent correctly used                                                   | response, so the                                                                | condition for this                                                              |                                                         | question. Therefore, this                                                |                        |
|    |                         |                        | questions about finance,  |                       | name='sc2_prefs'          |                                          | has been saved, and                                        | agent correctly                                                                                     |                                    | the `sc2_prefs` tool to                                                    | condition for this                                                              | ordering property was not                                                       |                                                         | property is not                                                          |                        |
|    |                         |                        | money, or the stock       |                       |                           |                                          | offering further                                           | identified this as                                                                                  |                                    | process and store this                                                     | ordering property was not                                                       | met., Score: 1.0                                                                |                                                         | applicable to the current                                                |                        |
|    |                         |                        | market, feel free to ask. |                       |                           |                                          | assistance, without any                                    | "profile data" as per the                                                                           |                                    | information, as indicated                                                  | met., Score: 1.0                                                                |                                                                                 |                                                         | interaction., Score: 1.0                                                 |                        |
|    |                         |                        |                           |                       |                           |                                          | unnecessary information                                    | developer instructions                                                                              |                                    | by the tool call                                                           |                                                                                 |                                                                                 |                                                         |                                                                          |                        |
|    |                         |                        |                           |                       |                           |                                          | or digression. This is a                                   | and used the appropriate                                                                            |                                    | `sc2_prefs(request='The                                                    |                                                                                 |                                                                                 |                                                         |                                                                          |                        |
|    |                         |                        |                           |                       |                           |                                          | direct and appropriate                                     | `sc2_prefs` tool to store                                                                           |                                    | user lives in Brooklyn,                                                    |                                                                                 |                                                                                 |                                                         |                                                                          |                        |
|    |                         |                        |                           |                       |                           |                                          | response given the user's                                  | it, successfully                                                                                    |                                    | New York.')` and the                                                       |                                                                                 |                                                                                 |                                                         |                                                                          |                        |
|    |                         |                        |                           |                       |                           |                                          | statement., Score: 1.0                                     | fulfilling the implicit                                                                             |                                    | tool's description as a                                                    |                                                                                 |                                                                                 |                                                         |                                                                          |                        |
|    |                         |                        |                           |                       |                           |                                          |                                                            | goal of saving this                                                                                 |                                    | profile analyst., Score:                                                   |                                                                                 |                                                                                 |                                                         |                                                                          |                        |
|    |                         |                        |                           |                       |                           |                                          |                                                            | information., Score: 1.0                                                                            |                                    | 1.0                                                                        |                                                                                 |                                                                                 |                                                         |                                                                          |                        |
+----+-------------------------+------------------------+---------------------------+-----------------------+---------------------------+------------------------------------------+------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+------------------------------------+----------------------------------------------------------------------------+---------------------------------------------------------------------------------+---------------------------------------------------------------------------------+---------------------------------------------------------+--------------------------------------------------------------------------+------------------------+



********************************************************************
Eval Set Id: sc2_eval_suite
Eval Id: term_discovery_1
Overall Eval Status: PASSED
---------------------------------------------------------------------
Metric: rubric_based_final_response_quality_v1, Status: PASSED, Score: 1.0, Threshold: 0.8
Rubric Scores:
Rubric: The agent's response is direct and to the point., Score: 1.0, Reasoning: This is an aggregated score derived from individual entries. Please refer to individual entries in each invocation for actual rationale from the model.
Rubric: The agent's response accurately infers the user's underlying goal from ambiguous queries., Score: 1.0, Reasoning: This is an aggregated score derived from individual entries. Please refer to individual entries in each invocation for actual rationale from the model.
---------------------------------------------------------------------
Metric: rubric_based_tool_use_quality_v1, Status: PASSED, Score: 1.0, Threshold: 1.0
Rubric Scores:
Rubric: The agent calls `sc2_prefs` to store profile data when required., Score: 1.0, Reasoning: This is an aggregated score derived from individual entries. Please refer to individual entries in each invocation for actual rationale from the model.
Rubric: The agent calls `sc2_memory` before `sc2_terms` or `fncall_pipeline`., Score: 1.0, Reasoning: This is an aggregated score derived from individual entries. Please refer to individual entries in each invocation for actual rationale from the model.
Rubric: The agent calls `sc2_memory` after `sc2_terms` only for new memories., Score: 1.0, Reasoning: This is an aggregated score derived from individual entries. Please refer to individual entries in each invocation for actual rationale from the model.
Rubric: The agent calls `sc2_summary` last when used., Score: 1.0, Reasoning: This is an aggregated score derived from individual entries. Please refer to individual entries in each invocation for actual rationale from the model.
Rubric: The agent can bypass the workflow for usage related questions., Score: 1.0, Reasoning: This is an aggregated score derived from individual entries. Please refer to individual entries in each invocation for actual rationale from the model.
---------------------------------------------------------------------
Metric: hallucinations_v1, Status: PASSED, Score: 1.0, Threshold: 0.8
---------------------------------------------------------------------
Invocation Details:
+----+------------------------+---------------------------+---------------------------+-----------------------+---------------------------+------------------------------------------+------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+------------------------------------+----------------------------------------------------------------------------+---------------------------------------------------------------------------------+---------------------------------------------------------------------------------+---------------------------------------------------------+--------------------------------------------------------------------------+------------------------+
|    | prompt                 | expected_response         | actual_response           | expected_tool_calls   | actual_tool_calls         | rubric_based_final_response_quality_v1   | Rubric: The agent's response is direct and to the point.   | Rubric: The agent's response accurately infers the user's underlying goal from ambiguous queries.   | rubric_based_tool_use_quality_v1   | Rubric: The agent calls `sc2_prefs` to store profile data when required.   | Rubric: The agent calls `sc2_memory` before `sc2_terms` or `fncall_pipeline`.   | Rubric: The agent calls `sc2_memory` after `sc2_terms` only for new memories.   | Rubric: The agent calls `sc2_summary` last when used.   | Rubric: The agent can bypass the workflow for usage related questions.   | hallucinations_v1      |
+====+========================+===========================+===========================+=======================+===========================+==========================================+============================================================+=====================================================================================================+====================================+============================================================================+=================================================================================+=================================================================================+=========================================================+==========================================================================+========================+
|  0 | What is a short trade? | A short trade, also known | A short trade, also known |                       | id='adk-06b2c5a6-06c7-47e | Status: PASSED, Score:                   | Reasoning: The user asked                                  | Reasoning: The user's                                                                               | Status: PASSED, Score:             | Reasoning: The agent did                                                   | Reasoning: The agent                                                            | Reasoning: The tool                                                             | Reasoning: `sc2_summary`                                | Reasoning: The user                                                      | Status: PASSED, Score: |
|    |                        | as short- selling or      | as short selling or       |                       | 6-8d26- f53c99aec3f9'     | 1.0                                      | for a definition of a                                      | query "What is a short                                                                              | 1.0                                | not call `sc2_prefs`. The                                                  | called `sc2_memory` at                                                          | `sc2_terms` was not                                                             | was called at step 1,                                   | prompt "What is a short                                                  | 1.0                    |
|    |                        | going-short is an         | shorting, is a            |                       | args={'request': 'What is |                                          | "short trade." The                                         | trade?" is a direct and                                                                             |                                    | user's prompt, "What is a                                                  | step 0. Neither                                                                 | called in the response.                                                         | which is the last step in                               | trade?" is not a usage-                                                  |                        |
|    |                        | investment strategy where | speculative trading       |                       | a short trade?'}          |                                          | agent's final answer                                       | unambiguous question                                                                                |                                    | short trade?", is a                                                        | `sc2_terms` nor                                                                 | Therefore, the condition                                                        | the sequence of tool                                    | related question. The                                                    |                        |
|    |                        | an investor anticipates a | strategy. In this         |                       | name='sc2_memory' id='a d |                                          | directly provides this                                     | asking for a definition.                                                                            |                                    | request for information                                                    | `fncall_pipeline` were                                                          | of `sc2_memory` being                                                           | calls (the only other                                   | agent correctly did not                                                  |                        |
|    |                        | decline in the price of   | strategy, an investor     |                       | k-5ad53614-23dc-46a6-820c |                                          | definition without any                                     | Therefore, the condition                                                                            |                                    | and does not require                                                       | called in the response,                                                         | called *after*                                                                  | call was `sc2_memory` at                                | bypass the workflow,                                                     |                        |
|    |                        | an asset, typically a     | sells borrowed securities |                       | -3210edbb95e1'            |                                          | extraneous information,                                    | for this property to be                                                                             |                                    | storing profile data.                                                      | thus `sc2_memory`                                                               | `sc2_terms` is not                                                              | step 0)., Score: 1.0                                    | using `sc2_memory` and                                                   |                        |
|    |                        | stock.                    | with the expectation of   |                       | args={'request': "A short |                                          | conversational filler, or                                  | applicable (an ambiguous                                                                            |                                    | Therefore, the tool was                                                    | implicitly occurs before                                                        | applicable., Score: 1.0                                                         |                                                         | `sc2_summary` to provide                                                 |                        |
|    |                        |                           | buying them back later at |                       | trade, also known as      |                                          | unnecessary preamble. The                                  | query) is not met.,                                                                                 |                                    | not required and                                                           | them., Score: 1.0                                                               |                                                                                 |                                                         | an answer, which aligns                                                  |                        |
|    |                        |                           | a lower price, aiming to  |                       | short selling or          |                                          | information provided is                                    | Score: 1.0                                                                                          |                                    | correctly not called.,                                                     |                                                                                 |                                                                                 |                                                         | with the property's                                                      |                        |
|    |                        |                           | profit from a decline in  |                       | shorting, is a            |                                          | relevant and concise.,                                     |                                                                                                     |                                    | Score: 1.0                                                                 |                                                                                 |                                                                                 |                                                         | implication that it *can*                                                |                        |
|    |                        |                           | the security's price. If  |                       | speculative trading       |                                          | Score: 1.0                                                 |                                                                                                     |                                    |                                                                            |                                                                                 |                                                                                 |                                                         | bypass for usage                                                         |                        |
|    |                        |                           | the price of the security |                       | strategy where an         |                                          |                                                            |                                                                                                     |                                    |                                                                            |                                                                                 |                                                                                 |                                                         | questions, but                                                           |                        |
|    |                        |                           | falls, the investor buys  |                       | investor sells borrowed   |                                          |                                                            |                                                                                                     |                                    |                                                                            |                                                                                 |                                                                                 |                                                         | *shouldn't* for others.,                                                 |                        |
|    |                        |                           | the shares back at a      |                       | securities with the       |                                          |                                                            |                                                                                                     |                                    |                                                                            |                                                                                 |                                                                                 |                                                         | Score: 1.0                                                               |                        |
|    |                        |                           | lower price, returns them |                       | expectation of buying     |                                          |                                                            |                                                                                                     |                                    |                                                                            |                                                                                 |                                                                                 |                                                         |                                                                          |                        |
|    |                        |                           | to the lender, and keeps  |                       | them back later at a      |                                          |                                                            |                                                                                                     |                                    |                                                                            |                                                                                 |                                                                                 |                                                         |                                                                          |                        |
|    |                        |                           | the difference as profit. |                       | lower price. The goal is  |                                          |                                                            |                                                                                                     |                                    |                                                                            |                                                                                 |                                                                                 |                                                         |                                                                          |                        |
|    |                        |                           | However, if the price of  |                       | to profit from a decline  |                                          |                                                            |                                                                                                     |                                    |                                                                            |                                                                                 |                                                                                 |                                                         |                                                                          |                        |
|    |                        |                           | the security rises, the   |                       | in the security's price.  |                                          |                                                            |                                                                                                     |                                    |                                                                            |                                                                                 |                                                                                 |                                                         |                                                                          |                        |
|    |                        |                           | investor must buy them    |                       | If the price falls, the   |                                          |                                                            |                                                                                                     |                                    |                                                                            |                                                                                 |                                                                                 |                                                         |                                                                          |                        |
|    |                        |                           | back at a higher price,   |                       | investor buys the shares  |                                          |                                                            |                                                                                                     |                                    |                                                                            |                                                                                 |                                                                                 |                                                         |                                                                          |                        |
|    |                        |                           | which results in a loss.  |                       | back at a lower price,    |                                          |                                                            |                                                                                                     |                                    |                                                                            |                                                                                 |                                                                                 |                                                         |                                                                          |                        |
|    |                        |                           |                           |                       | returns them to the       |                                          |                                                            |                                                                                                     |                                    |                                                                            |                                                                                 |                                                                                 |                                                         |                                                                          |                        |
|    |                        |                           |                           |                       | lender, and keeps the     |                                          |                                                            |                                                                                                     |                                    |                                                                            |                                                                                 |                                                                                 |                                                         |                                                                          |                        |
|    |                        |                           |                           |                       | difference as profit.     |                                          |                                                            |                                                                                                     |                                    |                                                                            |                                                                                 |                                                                                 |                                                         |                                                                          |                        |
|    |                        |                           |                           |                       | Conversely, if the price  |                                          |                                                            |                                                                                                     |                                    |                                                                            |                                                                                 |                                                                                 |                                                         |                                                                          |                        |
|    |                        |                           |                           |                       | rises, the investor must  |                                          |                                                            |                                                                                                     |                                    |                                                                            |                                                                                 |                                                                                 |                                                         |                                                                          |                        |
|    |                        |                           |                           |                       | buy them back at a higher |                                          |                                                            |                                                                                                     |                                    |                                                                            |                                                                                 |                                                                                 |                                                         |                                                                          |                        |
|    |                        |                           |                           |                       | price, resulting in a     |                                          |                                                            |                                                                                                     |                                    |                                                                            |                                                                                 |                                                                                 |                                                         |                                                                          |                        |
|    |                        |                           |                           |                       | loss."}                   |                                          |                                                            |                                                                                                     |                                    |                                                                            |                                                                                 |                                                                                 |                                                         |                                                                          |                        |
|    |                        |                           |                           |                       | name='sc2_summary'        |                                          |                                                            |                                                                                                     |                                    |                                                                            |                                                                                 |                                                                                 |                                                         |                                                                          |                        |
+----+------------------------+---------------------------+---------------------------+-----------------------+---------------------------+------------------------------------------+------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+------------------------------------+----------------------------------------------------------------------------+---------------------------------------------------------------------------------+---------------------------------------------------------------------------------+---------------------------------------------------------+--------------------------------------------------------------------------+------------------------+



********************************************************************
Eval Set Id: sc2_eval_suite
Eval Id: term_discovery_2
Overall Eval Status: PASSED
---------------------------------------------------------------------
Metric: rubric_based_final_response_quality_v1, Status: PASSED, Score: 1.0, Threshold: 0.8
Rubric Scores:
Rubric: The agent's response is direct and to the point., Score: 1.0, Reasoning: This is an aggregated score derived from individual entries. Please refer to individual entries in each invocation for actual rationale from the model.
Rubric: The agent's response accurately infers the user's underlying goal from ambiguous queries., Score: 1.0, Reasoning: This is an aggregated score derived from individual entries. Please refer to individual entries in each invocation for actual rationale from the model.
---------------------------------------------------------------------
Metric: rubric_based_tool_use_quality_v1, Status: PASSED, Score: 1.0, Threshold: 1.0
Rubric Scores:
Rubric: The agent calls `sc2_prefs` to store profile data when required., Score: 1.0, Reasoning: This is an aggregated score derived from individual entries. Please refer to individual entries in each invocation for actual rationale from the model.
Rubric: The agent calls `sc2_memory` before `sc2_terms` or `fncall_pipeline`., Score: 1.0, Reasoning: This is an aggregated score derived from individual entries. Please refer to individual entries in each invocation for actual rationale from the model.
Rubric: The agent calls `sc2_memory` after `sc2_terms` only for new memories., Score: 1.0, Reasoning: This is an aggregated score derived from individual entries. Please refer to individual entries in each invocation for actual rationale from the model.
Rubric: The agent calls `sc2_summary` last when used., Score: 1.0, Reasoning: This is an aggregated score derived from individual entries. Please refer to individual entries in each invocation for actual rationale from the model.
Rubric: The agent can bypass the workflow for usage related questions., Score: 1.0, Reasoning: This is an aggregated score derived from individual entries. Please refer to individual entries in each invocation for actual rationale from the model.
---------------------------------------------------------------------
Metric: hallucinations_v1, Status: PASSED, Score: 1.0, Threshold: 0.8
---------------------------------------------------------------------
Invocation Details:
+----+-------------------------+---------------------------+---------------------------+-----------------------+---------------------------+------------------------------------------+------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+------------------------------------+----------------------------------------------------------------------------+---------------------------------------------------------------------------------+---------------------------------------------------------------------------------+---------------------------------------------------------+--------------------------------------------------------------------------+------------------------+
|    | prompt                  | expected_response         | actual_response           | expected_tool_calls   | actual_tool_calls         | rubric_based_final_response_quality_v1   | Rubric: The agent's response is direct and to the point.   | Rubric: The agent's response accurately infers the user's underlying goal from ambiguous queries.   | rubric_based_tool_use_quality_v1   | Rubric: The agent calls `sc2_prefs` to store profile data when required.   | Rubric: The agent calls `sc2_memory` before `sc2_terms` or `fncall_pipeline`.   | Rubric: The agent calls `sc2_memory` after `sc2_terms` only for new memories.   | Rubric: The agent calls `sc2_summary` last when used.   | Rubric: The agent can bypass the workflow for usage related questions.   | hallucinations_v1      |
+====+=========================+===========================+===========================+=======================+===========================+==========================================+============================================================+=====================================================================================================+====================================+============================================================================+=================================================================================+=================================================================================+=========================================================+==========================================================================+========================+
|  0 | What is gambler's ruin? | Gambler's Ruin is a       | Gambler's Ruin is a       |                       | id='adk-63f4407e-52fc-455 | Status: PASSED, Score:                   | Reasoning: The final                                       | Reasoning: The user's                                                                               | Status: PASSED, Score:             | Reasoning: The agent did                                                   | Reasoning: The agent                                                            | Reasoning: The tool                                                             | Reasoning: The agent                                    | Reasoning: The user                                                      | Status: PASSED, Score: |
|    |                         | concept in probability    | concept in probability    |                       | f-9d59- 628f36394236'     | 1.0                                      | answer directly addresses                                  | query "What is gambler's                                                                            | 1.0                                | not call `sc2_prefs`. The                                                  | called `sc2_memory` as                                                          | `sc2_terms` was not                                                             | called `sc2_summary` at                                 | prompt "What is gambler's                                                | 1.0                    |
|    |                         | theory. It describes a    | theory. It posits that a  |                       | args={'request': "What is |                                          | the user's question by                                     | ruin?" is not an                                                                                    |                                    | user prompt "What is                                                       | the first step (step 0).                                                        | called by the agent.                                                            | step 1, which is the last                               | ruin?" is a factual                                                      |                        |
|    |                         | scenario where a gambler, | gambler possessing a      |                       | gambler's ruin?"}         |                                          | providing a clear                                          | ambiguous query; it is a                                                                            |                                    | gambler's ruin?" does not                                                  | The tools `sc2_terms` and                                                       | Since `sc2_terms` was not                                                       | step in the                                             | question, not a usage-                                                   |                        |
|    |                         | beginning with a finite   | finite sum of money,      |                       | name='sc2_memory'         |                                          | definition of "gambler's                                   | direct question asking                                                                              |                                    | require the storage of                                                     | `fncall_pipeline` were                                                          | called, the condition for                                                       | `tool_calls_and_response`                               | related question. The                                                    |                        |
|    |                         | sum of money, will        | engaged in a game against |                       | id='adk- bf19929c-3381-4a |                                          | ruin" without any                                          | for a definition.                                                                                   |                                    | profile data, so the                                                       | not called at all in the                                                        | `sc2_memory` to be called                                                       | sequence., Score: 1.0                                   | agent correctly executed                                                 |                        |
|    |                         | inevitably lose all of    | an opponent with an       |                       | b1-80b6-62b327127e4d'     |                                          | extraneous conversational                                  | Therefore, the condition                                                                            |                                    | `sc2_prefs` tool was not                                                   | response. Therefore,                                                            | *after* `sc2_terms` did                                                         |                                                         | a workflow for a factual                                                 |                        |
|    |                         | their funds.              | infinite amount of        |                       | args={'request':          |                                          | elements or irrelevant                                     | for evaluating inference                                                                            |                                    | required to be called.,                                                    | `sc2_memory` was called                                                         | not occur, and thus the                                                         |                                                         | query rather than                                                        |                        |
|    |                         |                           | capital, will inevitably  |                       | "Gambler's ruin is a      |                                          | information., Score: 1.0                                   | from *ambiguous* queries                                                                            |                                    | Score: 1.0                                                                 | before either of them.,                                                         | constraint "only for new                                                        |                                                         | bypassing it, which                                                      |                        |
|    |                         |                           | deplete their entire      |                       | concept in probability    |                                          |                                                            | is not applicable. The                                                                              |                                    |                                                                            | Score: 1.0                                                                      | memories" was not                                                               |                                                         | demonstrates its ability                                                 |                        |
|    |                         |                           | fortune. This outcome is  |                       | theory. It states that a  |                                          |                                                            | agent accurately inferred                                                                           |                                    |                                                                            |                                                                                 | violated., Score: 1.0                                                           |                                                         | to discern when to apply                                                 |                        |
|    |                         |                           | irrespective of whether   |                       | gambler with a finite     |                                          |                                                            | the explicit goal of the                                                                            |                                    |                                                                            |                                                                                 |                                                                                 |                                                         | its standard workflow                                                    |                        |
|    |                         |                           | the game is fair or even  |                       | amount of money, playing  |                                          |                                                            | user, which was to get a                                                                            |                                    |                                                                            |                                                                                 |                                                                                 |                                                         | versus when a bypass (for                                                |                        |
|    |                         |                           | if it offers a slight     |                       | against an opponent with  |                                          |                                                            | definition. Since the                                                                               |                                    |                                                                            |                                                                                 |                                                                                 |                                                         | usage questions) might be                                                |                        |
|    |                         |                           | advantage to the gambler. |                       | an infinite amount of     |                                          |                                                            | property's specific                                                                                 |                                    |                                                                            |                                                                                 |                                                                                 |                                                         | appropriate., Score: 1.0                                                 |                        |
|    |                         |                           |                           |                       | money, will eventually    |                                          |                                                            | condition (ambiguous                                                                                |                                    |                                                                            |                                                                                 |                                                                                 |                                                         |                                                                          |                        |
|    |                         |                           |                           |                       | lose all of their money.  |                                          |                                                            | queries) was not met, the                                                                           |                                    |                                                                            |                                                                                 |                                                                                 |                                                         |                                                                          |                        |
|    |                         |                           |                           |                       | This outcome occurs even  |                                          |                                                            | property is considered                                                                              |                                    |                                                                            |                                                                                 |                                                                                 |                                                         |                                                                          |                        |
|    |                         |                           |                           |                       | in a fair game or a game  |                                          |                                                            | fulfilled., Score: 1.0                                                                              |                                    |                                                                            |                                                                                 |                                                                                 |                                                         |                                                                          |                        |
|    |                         |                           |                           |                       | biased in the gambler's   |                                          |                                                            |                                                                                                     |                                    |                                                                            |                                                                                 |                                                                                 |                                                         |                                                                          |                        |
|    |                         |                           |                           |                       | favor."}                  |                                          |                                                            |                                                                                                     |                                    |                                                                            |                                                                                 |                                                                                 |                                                         |                                                                          |                        |
|    |                         |                           |                           |                       | name='sc2_summary'        |                                          |                                                            |                                                                                                     |                                    |                                                                            |                                                                                 |                                                                                 |                                                         |                                                                          |                        |
+----+-------------------------+---------------------------+---------------------------+-----------------------+---------------------------+------------------------------------------+------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+------------------------------------+----------------------------------------------------------------------------+---------------------------------------------------------------------------------+---------------------------------------------------------------------------------+---------------------------------------------------------+--------------------------------------------------------------------------+------------------------+



********************************************************************
Eval Set Id: sc2_eval_suite
Eval Id: function_aware
Overall Eval Status: PASSED
---------------------------------------------------------------------
Metric: rubric_based_final_response_quality_v1, Status: PASSED, Score: 1.0, Threshold: 0.8
Rubric Scores:
Rubric: The agent's response is direct and to the point., Score: 1.0, Reasoning: This is an aggregated score derived from individual entries. Please refer to individual entries in each invocation for actual rationale from the model.
Rubric: The agent's response accurately infers the user's underlying goal from ambiguous queries., Score: 1.0, Reasoning: This is an aggregated score derived from individual entries. Please refer to individual entries in each invocation for actual rationale from the model.
---------------------------------------------------------------------
Metric: rubric_based_tool_use_quality_v1, Status: PASSED, Score: 1.0, Threshold: 1.0
Rubric Scores:
Rubric: The agent calls `sc2_prefs` to store profile data when required., Score: 1.0, Reasoning: This is an aggregated score derived from individual entries. Please refer to individual entries in each invocation for actual rationale from the model.
Rubric: The agent calls `sc2_memory` before `sc2_terms` or `fncall_pipeline`., Score: 1.0, Reasoning: This is an aggregated score derived from individual entries. Please refer to individual entries in each invocation for actual rationale from the model.
Rubric: The agent calls `sc2_memory` after `sc2_terms` only for new memories., Score: 1.0, Reasoning: This is an aggregated score derived from individual entries. Please refer to individual entries in each invocation for actual rationale from the model.
Rubric: The agent calls `sc2_summary` last when used., Score: 1.0, Reasoning: This is an aggregated score derived from individual entries. Please refer to individual entries in each invocation for actual rationale from the model.
Rubric: The agent can bypass the workflow for usage related questions., Score: 1.0, Reasoning: This is an aggregated score derived from individual entries. Please refer to individual entries in each invocation for actual rationale from the model.
---------------------------------------------------------------------
Metric: hallucinations_v1, Status: PASSED, Score: 1.0, Threshold: 0.8
---------------------------------------------------------------------
Invocation Details:
+----+---------------------------+---------------------------+---------------------------+-----------------------+---------------------------+------------------------------------------+------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+------------------------------------+----------------------------------------------------------------------------+---------------------------------------------------------------------------------+---------------------------------------------------------------------------------+---------------------------------------------------------+--------------------------------------------------------------------------+------------------------+
|    | prompt                    | expected_response         | actual_response           | expected_tool_calls   | actual_tool_calls         | rubric_based_final_response_quality_v1   | Rubric: The agent's response is direct and to the point.   | Rubric: The agent's response accurately infers the user's underlying goal from ambiguous queries.   | rubric_based_tool_use_quality_v1   | Rubric: The agent calls `sc2_prefs` to store profile data when required.   | Rubric: The agent calls `sc2_memory` before `sc2_terms` or `fncall_pipeline`.   | Rubric: The agent calls `sc2_memory` after `sc2_terms` only for new memories.   | Rubric: The agent calls `sc2_summary` last when used.   | Rubric: The agent can bypass the workflow for usage related questions.   | hallucinations_v1      |
+====+===========================+===========================+===========================+=======================+===========================+==========================================+============================================================+=====================================================================================================+====================================+============================================================================+=================================================================================+=================================================================================+=========================================================+==========================================================================+========================+
|  0 | Tell me what functions    | `fncall_pipeline` knows   | `fncall_pipeline` can     |                       | id='adk-66d3704a-e420-4cf | Status: PASSED, Score:                   | Reasoning: The final                                       | Reasoning: The user's                                                                               | Status: PASSED, Score:             | Reasoning: The agent's                                                     | Reasoning: The agent did                                                        | Reasoning: The agent did                                                        | Reasoning: The agent did                                | Reasoning: The user's                                                    | Status: PASSED, Score: |
|    | `fncall_pipeline` knows   | the following functions:  | access the following      |                       | e-85ac- 2529f03068f3'     | 1.0                                      | answer directly provides                                   | query is direct and                                                                                 | 1.0                                | response does not include                                                  | not call `sc2_memory`,                                                          | not call `sc2_memory` or                                                        | not call `sc2_summary` in                               | prompt is a direct usage-                                                | 1.0                    |
|    | by checking `sc2_fnplan`. | get_symbol_1,             | functions:  *             |                       | args={'request': 'List    |                                          | the requested list of                                      | unambiguous, explicitly                                                                             |                                    | a call to `sc2_prefs`.                                                     | `sc2_terms`, or                                                                 | `sc2_terms` in its                                                              | its response. Since                                     | related question about                                                   |                        |
|    |                           | get_symbols_1,            | `get_symbol_1` *          |                       | all functions defined     |                                          | functions without                                          | asking for a list of                                                                                |                                    | The user's prompt is a                                                     | `fncall_pipeline` in its                                                        | response, nor did the                                                           | `sc2_summary` was not                                   | tool functionality. The                                                  |                        |
|    |                           | get_name_1,               | `get_symbols_1` *         |                       | within sc2_fnplan'}       |                                          | additional text or                                         | functions and specifying                                                                            |                                    | question about tool                                                        | response. Since the                                                             | user's prompt involve new                                                       | used, the condition of                                  | agent responded by                                                       |                        |
|    |                           | get_symbol_quote_1,       | `get_name_1` *            |                       | name='sc2_fnplan'         |                                          | conversational fluff,                                      | the tool to check                                                                                   |                                    | functionality and does                                                     | premise for the ordering                                                        | memories. Therefore, the                                                        | the property is not met,                                | directly invoking the                                                    |                        |
|    |                           | get_market_status_1,      | `get_symbol_quote_1` *    |                       |                           |                                          | making it direct and to                                    | (`sc2_fnplan`).                                                                                     |                                    | not require storing                                                        | condition is not met, the                                                       | property is not                                                                 | and thus it is not                                      | specified tool,                                                          |                        |
|    |                           | get_market_session_1,     | `get_market_status_1` *   |                       |                           |                                          | the point., Score: 1.0                                     | Therefore, there was no                                                                             |                                    | profile data. Thus,                                                        | property is not                                                                 | applicable., Score: 1.0                                                         | applicable., Score: 1.0                                 | `sc2_fnplan`, without                                                    |                        |
|    |                           | get_company_peers_1,      | `get_market_session_1` *  |                       |                           |                                          |                                                            | need for the agent to                                                                               |                                    | `sc2_prefs` was not                                                        | applicable in a violating                                                       |                                                                                 |                                                         | engaging in any                                                          |                        |
|    |                           | get_local_datetime,       | `get_company_peers_1` *   |                       |                           |                                          |                                                            | infer an underlying goal                                                                            |                                    | called when it was not                                                     | sense., Score: 1.0                                                              |                                                                                 |                                                         | extraneous steps that                                                    |                        |
|    |                           | get_last_market_close,    | `get_local_datetime` *    |                       |                           |                                          |                                                            | from an ambiguous query.,                                                                           |                                    | required, fulfilling the                                                   |                                                                                 |                                                                                 |                                                         | might be part of a                                                       |                        |
|    |                           | get_exchange_codes_1,     | `get_last_market_close` * |                       |                           |                                          |                                                            | Score: 1.0                                                                                          |                                    | property., Score: 1.0                                                      |                                                                                 |                                                                                 |                                                         | broader workflow, thus                                                   |                        |
|    |                           | get_exchange_code_1,      | `get_exchange_codes_1` *  |                       |                           |                                          |                                                            |                                                                                                     |                                    |                                                                            |                                                                                 |                                                                                 |                                                         | demonstrating its ability                                                |                        |
|    |                           | get_financials_1,         | `get_exchange_code_1` *   |                       |                           |                                          |                                                            |                                                                                                     |                                    |                                                                            |                                                                                 |                                                                                 |                                                         | to bypass such a workflow                                                |                        |
|    |                           | get_daily_candlestick_2,  | `get_financials_1` *      |                       |                           |                                          |                                                            |                                                                                                     |                                    |                                                                            |                                                                                 |                                                                                 |                                                         | for direct usage                                                         |                        |
|    |                           | get_custom_candlestick_2, | `get_daily_candlestick_2` |                       |                           |                                          |                                                            |                                                                                                     |                                    |                                                                            |                                                                                 |                                                                                 |                                                         | inquiries., Score: 1.0                                                   |                        |
|    |                           | get_ticker_overview_2, ge | * `get_custom_candlestick |                       |                           |                                          |                                                            |                                                                                                     |                                    |                                                                            |                                                                                 |                                                                                 |                                                         |                                                                          |                        |
|    |                           | t_recommendation_trends_1 | _2` *                     |                       |                           |                                          |                                                            |                                                                                                     |                                    |                                                                            |                                                                                 |                                                                                 |                                                         |                                                                          |                        |
|    |                           | , get_news_with_sentiment | `get_ticker_overview_2` * |                       |                           |                                          |                                                            |                                                                                                     |                                    |                                                                            |                                                                                 |                                                                                 |                                                         |                                                                          |                        |
|    |                           | _2, get_wiki_grounding,   | `get_recommendation_trend |                       |                           |                                          |                                                            |                                                                                                     |                                    |                                                                            |                                                                                 |                                                                                 |                                                         |                                                                          |                        |
|    |                           | get_search_grounding.     | s_1` * `get_news_with_sen |                       |                           |                                          |                                                            |                                                                                                     |                                    |                                                                            |                                                                                 |                                                                                 |                                                         |                                                                          |                        |
|    |                           |                           | timent_2` *               |                       |                           |                                          |                                                            |                                                                                                     |                                    |                                                                            |                                                                                 |                                                                                 |                                                         |                                                                          |                        |
|    |                           |                           | `get_wiki_grounding` *    |                       |                           |                                          |                                                            |                                                                                                     |                                    |                                                                            |                                                                                 |                                                                                 |                                                         |                                                                          |                        |
|    |                           |                           | `get_search_grounding`    |                       |                           |                                          |                                                            |                                                                                                     |                                    |                                                                            |                                                                                 |                                                                                 |                                                         |                                                                          |                        |
+----+---------------------------+---------------------------+---------------------------+-----------------------+---------------------------+------------------------------------------+------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+------------------------------------+----------------------------------------------------------------------------+---------------------------------------------------------------------------------+---------------------------------------------------------------------------------+---------------------------------------------------------+--------------------------------------------------------------------------+------------------------+



********************************************************************
Eval Set Id: sc2_eval_suite
Eval Id: tool_aware
Overall Eval Status: PASSED
---------------------------------------------------------------------
Metric: rubric_based_final_response_quality_v1, Status: PASSED, Score: 1.0, Threshold: 0.8
Rubric Scores:
Rubric: The agent's response is direct and to the point., Score: 1.0, Reasoning: This is an aggregated score derived from individual entries. Please refer to individual entries in each invocation for actual rationale from the model.
Rubric: The agent's response accurately infers the user's underlying goal from ambiguous queries., Score: 1.0, Reasoning: This is an aggregated score derived from individual entries. Please refer to individual entries in each invocation for actual rationale from the model.
---------------------------------------------------------------------
Metric: rubric_based_tool_use_quality_v1, Status: PASSED, Score: 1.0, Threshold: 1.0
Rubric Scores:
Rubric: The agent calls `sc2_prefs` to store profile data when required., Score: 1.0, Reasoning: This is an aggregated score derived from individual entries. Please refer to individual entries in each invocation for actual rationale from the model.
Rubric: The agent calls `sc2_memory` before `sc2_terms` or `fncall_pipeline`., Score: 1.0, Reasoning: This is an aggregated score derived from individual entries. Please refer to individual entries in each invocation for actual rationale from the model.
Rubric: The agent calls `sc2_memory` after `sc2_terms` only for new memories., Score: 1.0, Reasoning: This is an aggregated score derived from individual entries. Please refer to individual entries in each invocation for actual rationale from the model.
Rubric: The agent calls `sc2_summary` last when used., Score: 1.0, Reasoning: This is an aggregated score derived from individual entries. Please refer to individual entries in each invocation for actual rationale from the model.
Rubric: The agent can bypass the workflow for usage related questions., Score: 1.0, Reasoning: This is an aggregated score derived from individual entries. Please refer to individual entries in each invocation for actual rationale from the model.
---------------------------------------------------------------------
Metric: hallucinations_v1, Status: PASSED, Score: 1.0, Threshold: 0.8
---------------------------------------------------------------------
Invocation Details:
+----+------------------------+-------------------------+-----------------------+-----------------------+---------------------+------------------------------------------+------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+------------------------------------+----------------------------------------------------------------------------+---------------------------------------------------------------------------------+---------------------------------------------------------------------------------+---------------------------------------------------------+--------------------------------------------------------------------------+------------------------+
|    | prompt                 | expected_response       | actual_response       | expected_tool_calls   | actual_tool_calls   | rubric_based_final_response_quality_v1   | Rubric: The agent's response is direct and to the point.   | Rubric: The agent's response accurately infers the user's underlying goal from ambiguous queries.   | rubric_based_tool_use_quality_v1   | Rubric: The agent calls `sc2_prefs` to store profile data when required.   | Rubric: The agent calls `sc2_memory` before `sc2_terms` or `fncall_pipeline`.   | Rubric: The agent calls `sc2_memory` after `sc2_terms` only for new memories.   | Rubric: The agent calls `sc2_summary` last when used.   | Rubric: The agent can bypass the workflow for usage related questions.   | hallucinations_v1      |
+====+========================+=========================+=======================+=======================+=====================+==========================================+============================================================+=====================================================================================================+====================================+============================================================================+=================================================================================+=================================================================================+=========================================================+==========================================================================+========================+
|  0 | What tools do you know | I can use the following | I know how to use the |                       |                     | Status: PASSED, Score:                   | Reasoning: The agent's                                     | Reasoning: The user's                                                                               | Status: PASSED, Score:             | Reasoning: The user's                                                      | Reasoning: The agent did                                                        | Reasoning: The agent did                                                        | Reasoning: The agent did                                | Reasoning: The user's                                                    | Status: PASSED, Score: |
|    | how to use?            | tools: sc2_memory,      | following tools:      |                       |                     | 1.0                                      | response directly answers                                  | query "What tools do you                                                                            | 1.0                                | prompt was a question                                                      | not make any tool calls.                                                        | not make any tool calls.                                                        | not make any tool calls,                                | prompt was a usage-                                                      | 1.0                    |
|    |                        | sc2_prefs,              | `sc2_memory`,         |                       |                     |                                          | the user's question by                                     | know how to use?" is a                                                                              |                                    | about the agent's                                                          | Therefore, the condition                                                        | Therefore, the condition                                                        | which means `sc2_summary`                               | related question. The                                                    |                        |
|    |                        | fncall_pipeline,        | `sc2_prefs`,          |                       |                     |                                          | listing the tools it                                       | direct and unambiguous                                                                              |                                    | capabilities, not a                                                        | of calling `sc2_memory`                                                         | of calling `sc2_memory`                                                         | was not used. Therefore,                                | agent's response, "No                                                    |                        |
|    |                        | sc2_fnplan, sc2_terms,  | `fncall_pipeline`,    |                       |                     |                                          | knows how to use, without                                  | question. There is no                                                                               |                                    | request to store profile                                                   | before `sc2_terms` or                                                           | after `sc2_terms` is not                                                        | the condition that it is                                | intermediate steps were                                                  |                        |
|    |                        | sc2_summary.            | `sc2_fnplan`,         |                       |                     |                                          | any additional                                             | underlying goal to infer                                                                            |                                    | data. Therefore, calling                                                   | `fncall_pipeline` is not                                                        | applicable as neither of                                                        | called last "when used"                                 | taken," indicates that it                                                |                        |
|    |                        |                         | `sc2_terms`, and      |                       |                     |                                          | elaboration or                                             | beyond directly answering                                                                           |                                    | `sc2_prefs` was not                                                        | applicable as none of                                                           | these tools were used.,                                                         | is satisfied as it was                                  | bypassed any complex                                                     |                        |
|    |                        |                         | `sc2_summary`.        |                       |                     |                                          | unnecessary information.,                                  | the question. Therefore,                                                                            |                                    | required. The agent did                                                    | these tools were used.,                                                         | Score: 1.0                                                                      | not used at all., Score:                                | workflow that might                                                      |                        |
|    |                        |                         |                       |                       |                     |                                          | Score: 1.0                                                 | the condition for this                                                                              |                                    | not call any tools, which                                                  | Score: 1.0                                                                      |                                                                                 | 1.0                                                     | involve tool calls or                                                    |                        |
|    |                        |                         |                       |                       |                     |                                          |                                                            | property (an ambiguous                                                                              |                                    | aligns with not calling                                                    |                                                                                 |                                                                                 |                                                         | planning, directly                                                       |                        |
|    |                        |                         |                       |                       |                     |                                          |                                                            | query) was not met.,                                                                                |                                    | `sc2_prefs` when not                                                       |                                                                                 |                                                                                 |                                                         | addressing the nature of                                                 |                        |
|    |                        |                         |                       |                       |                     |                                          |                                                            | Score: 1.0                                                                                          |                                    | required., Score: 1.0                                                      |                                                                                 |                                                                                 |                                                         | the question., Score: 1.0                                                |                        |
+----+------------------------+-------------------------+-----------------------+-----------------------+---------------------+------------------------------------------+------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+------------------------------------+----------------------------------------------------------------------------+---------------------------------------------------------------------------------+---------------------------------------------------------------------------------+---------------------------------------------------------+--------------------------------------------------------------------------+------------------------+



********************************************************************
Eval Set Id: sc2_eval_suite
Eval Id: create_memory_1
Overall Eval Status: PASSED
---------------------------------------------------------------------
Metric: rubric_based_final_response_quality_v1, Status: PASSED, Score: 1.0, Threshold: 0.8
Rubric Scores:
Rubric: The agent's response is direct and to the point., Score: 1.0, Reasoning: This is an aggregated score derived from individual entries. Please refer to individual entries in each invocation for actual rationale from the model.
Rubric: The agent's response accurately infers the user's underlying goal from ambiguous queries., Score: 1.0, Reasoning: This is an aggregated score derived from individual entries. Please refer to individual entries in each invocation for actual rationale from the model.
---------------------------------------------------------------------
Metric: rubric_based_tool_use_quality_v1, Status: PASSED, Score: 1.0, Threshold: 1.0
Rubric Scores:
Rubric: The agent calls `sc2_prefs` to store profile data when required., Score: 1.0, Reasoning: This is an aggregated score derived from individual entries. Please refer to individual entries in each invocation for actual rationale from the model.
Rubric: The agent calls `sc2_memory` before `sc2_terms` or `fncall_pipeline`., Score: 1.0, Reasoning: This is an aggregated score derived from individual entries. Please refer to individual entries in each invocation for actual rationale from the model.
Rubric: The agent calls `sc2_memory` after `sc2_terms` only for new memories., Score: 1.0, Reasoning: This is an aggregated score derived from individual entries. Please refer to individual entries in each invocation for actual rationale from the model.
Rubric: The agent calls `sc2_summary` last when used., Score: 1.0, Reasoning: This is an aggregated score derived from individual entries. Please refer to individual entries in each invocation for actual rationale from the model.
Rubric: The agent can bypass the workflow for usage related questions., Score: 1.0, Reasoning: This is an aggregated score derived from individual entries. Please refer to individual entries in each invocation for actual rationale from the model.
---------------------------------------------------------------------
Metric: hallucinations_v1, Status: PASSED, Score: 1.0, Threshold: 0.8
---------------------------------------------------------------------
Invocation Details:
+----+---------------------------+--------------------------+---------------------------+-----------------------+---------------------------+------------------------------------------+------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+------------------------------------+----------------------------------------------------------------------------+---------------------------------------------------------------------------------+---------------------------------------------------------------------------------+---------------------------------------------------------+--------------------------------------------------------------------------+------------------------+
|    | prompt                    | expected_response        | actual_response           | expected_tool_calls   | actual_tool_calls         | rubric_based_final_response_quality_v1   | Rubric: The agent's response is direct and to the point.   | Rubric: The agent's response accurately infers the user's underlying goal from ambiguous queries.   | rubric_based_tool_use_quality_v1   | Rubric: The agent calls `sc2_prefs` to store profile data when required.   | Rubric: The agent calls `sc2_memory` before `sc2_terms` or `fncall_pipeline`.   | Rubric: The agent calls `sc2_memory` after `sc2_terms` only for new memories.   | Rubric: The agent calls `sc2_summary` last when used.   | Rubric: The agent can bypass the workflow for usage related questions.   | hallucinations_v1      |
+====+===========================+==========================+===========================+=======================+===========================+==========================================+============================================================+=====================================================================================================+====================================+============================================================================+=================================================================================+=================================================================================+=========================================================+==========================================================================+========================+
|  0 | My local advisor is SC at | I have stored your local | I already know that the   |                       | id='adk-9aaffd5a-287d-48d | Status: PASSED, Score:                   | Reasoning: The final                                       | Reasoning: The user's                                                                               | Status: PASSED, Score:             | Reasoning: The user                                                        | Reasoning: The agent's                                                          | Reasoning: The agent's                                                          | Reasoning: The agent's                                  | Reasoning: The user                                                      | Status: PASSED, Score: |
|    | JPMorgan Chase,           | advisor's information.   | local advisor is SC at    |                       | a-9a62- 4e346e31cb20'     | 1.0                                      | answer directly addresses                                  | query is a clear                                                                                    | 1.0                                | prompt contained profile                                                   | response did not include                                                        | response did not include                                                        | response did not include                                | prompt was not a "usage                                                  | 1.0                    |
|    | 212-736-2001.             |                          | JPMorgan Chase, and their |                       | args={'request': 'My      |                                          | the user's statement                                       | statement of profile                                                                                |                                    | data (advisor name,                                                        | calls to `sc2_memory`,                                                          | calls to `sc2_memory` or                                                        | a call to `sc2_summary`.                                | related question," so                                                    |                        |
|    |                           |                          | phone number is           |                       | local advisor is SC at    |                                          | without any extraneous                                     | data, not an ambiguous                                                                              |                                    | company, phone number),                                                    | `sc2_terms`, or                                                                 | `sc2_terms`. Therefore,                                                         | Therefore, the property                                 | this property is not                                                     |                        |
|    |                           |                          | 212-736-2001.             |                       | JPMorgan Chase,           |                                          | information or                                             | query. The agent                                                                                    |                                    | and the agent                                                              | `fncall_pipeline`.                                                              | the property is not                                                             | is not applicable.,                                     | applicable to the current                                                |                        |
|    |                           |                          |                           |                       | 212-736-2001.'}           |                                          | conversational filler. It                                  | correctly inferred the                                                                              |                                    | appropriately called                                                       | Therefore, the property                                                         | applicable., Score: 1.0                                                         | Score: 1.0                                              | interaction., Score: 1.0                                                 |                        |
|    |                           |                          |                           |                       | name='sc2_prefs'          |                                          | confirms the information                                   | user's goal was to                                                                                  |                                    | `sc2_prefs` to handle                                                      | is not applicable.,                                                             |                                                                                 |                                                         |                                                                          |                        |
|    |                           |                          |                           |                       |                           |                                          | provided by the user.,                                     | provide profile data, as                                                                            |                                    | this information., Score:                                                  | Score: 1.0                                                                      |                                                                                 |                                                         |                                                                          |                        |
|    |                           |                          |                           |                       |                           |                                          | Score: 1.0                                                 | evidenced by its use of                                                                             |                                    | 1.0                                                                        |                                                                                 |                                                                                 |                                                         |                                                                          |                        |
|    |                           |                          |                           |                       |                           |                                          |                                                            | the `sc2_prefs` tool,                                                                               |                                    |                                                                            |                                                                                 |                                                                                 |                                                         |                                                                          |                        |
|    |                           |                          |                           |                       |                           |                                          |                                                            | which is designed for                                                                               |                                    |                                                                            |                                                                                 |                                                                                 |                                                         |                                                                          |                        |
|    |                           |                          |                           |                       |                           |                                          |                                                            | storing profile data                                                                                |                                    |                                                                            |                                                                                 |                                                                                 |                                                         |                                                                          |                        |
|    |                           |                          |                           |                       |                           |                                          |                                                            | according to the                                                                                    |                                    |                                                                            |                                                                                 |                                                                                 |                                                         |                                                                          |                        |
|    |                           |                          |                           |                       |                           |                                          |                                                            | instructions. The                                                                                   |                                    |                                                                            |                                                                                 |                                                                                 |                                                         |                                                                          |                        |
|    |                           |                          |                           |                       |                           |                                          |                                                            | response then confirms                                                                              |                                    |                                                                            |                                                                                 |                                                                                 |                                                         |                                                                          |                        |
|    |                           |                          |                           |                       |                           |                                          |                                                            | the data., Score: 1.0                                                                               |                                    |                                                                            |                                                                                 |                                                                                 |                                                         |                                                                          |                        |
+----+---------------------------+--------------------------+---------------------------+-----------------------+---------------------------+------------------------------------------+------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+------------------------------------+----------------------------------------------------------------------------+---------------------------------------------------------------------------------+---------------------------------------------------------------------------------+---------------------------------------------------------+--------------------------------------------------------------------------+------------------------+



2025-12-01 06:50:40,922 - ERROR - base_events.py:1821 - Unclosed client session
client_session: &lt;aiohttp.client.ClientSession object at 0x7b392c0e12b0&gt;
2025-12-01 06:50:40,922 - ERROR - base_events.py:1821 - Unclosed connector
connections: ['deque([(&lt;aiohttp.client_proto.ResponseHandler object at 0x7b392aed7410&gt;, 163304.64493107), (&lt;aiohttp.client_proto.ResponseHandler object at 0x7b392aed7230&gt;, 163307.551887757), (&lt;aiohttp.client_proto.ResponseHandler object at 0x7b392aed7890&gt;, 163311.3517091)])']
connector: &lt;aiohttp.connector.TCPConnector object at 0x7b392c0e1370&gt;
2025-12-01 06:50:40,924 - ERROR - base_events.py:1821 - Unclosed client session
client_session: &lt;aiohttp.client.ClientSession object at 0x7b392a7ae420&gt;
2025-12-01 06:50:40,924 - ERROR - base_events.py:1821 - Unclosed connector
connections: ['deque([(&lt;aiohttp.client_proto.ResponseHandler object at 0x7b392aed7050&gt;, 163304.441401676)])']
connector: &lt;aiohttp.connector.TCPConnector object at 0x7b392a7aca70&gt;
2025-12-01 06:50:40,925 - ERROR - base_events.py:1821 - Unclosed client session
client_session: &lt;aiohttp.client.ClientSession object at 0x7b3929b58c20&gt;
2025-12-01 06:50:40,925 - ERROR - base_events.py:1821 - Unclosed connector
connections: ['deque([(&lt;aiohttp.client_proto.ResponseHandler object at 0x7b392aed7d70&gt;, 163300.374662593), (&lt;aiohttp.client_proto.ResponseHandler object at 0x7b392a760170&gt;, 163301.411946312)])']
connector: &lt;aiohttp.connector.TCPConnector object at 0x7b3929b58b60&gt;
2025-12-01 06:50:40,927 - ERROR - base_events.py:1821 - Unclosed client session
client_session: &lt;aiohttp.client.ClientSession object at 0x7b392a778f50&gt;
2025-12-01 06:50:40,927 - ERROR - base_events.py:1821 - Unclosed connector
connections: ['deque([(&lt;aiohttp.client_proto.ResponseHandler object at 0x7b392aed7ef0&gt;, 163299.872841362), (&lt;aiohttp.client_proto.ResponseHandler object at 0x7b392a761130&gt;, 163300.01212217), (&lt;aiohttp.client_proto.ResponseHandler object at 0x7b392a760a10&gt;, 163300.013835746), (&lt;aiohttp.client_proto.ResponseHandler object at 0x7b392a760770&gt;, 163301.746375534)])']
connector: &lt;aiohttp.connector.TCPConnector object at 0x7b392a778e90&gt;
</code></pre></div></div>

<h2 id="conclusion">Conclusion</h2>

<p>In applying Google’s ADK to SC1, the result is a more capable SC2 which is ready to grow beyond it’s first edition roots. Unresolved issues from SC1 remain. Parallelism will enable large work loads, like a stack of news requiring analysis, or background processes to drive self-improvement. This will enable a better user experience when locally running models are later employed to scale further. With the addition of agentic capabilities StockChat has room to grow again.</p>

<p><strong>I hope you’ll stick around to see how far the project gets! Thanks for taking the time to check out my notebook!</strong></p>

<h1 id="appendix"><strong>Appendix</strong></h1>

<h2 id="gemini-baseline-check">Gemini Baseline Check</h2>

<div class="language-python highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="c1"># This is an accurate retelling of events. 
</span><span class="n">config_with_search</span> <span class="o">=</span> <span class="n">types</span><span class="p">.</span><span class="nc">GenerateContentConfig</span><span class="p">(</span>
    <span class="n">tools</span><span class="o">=</span><span class="p">[</span><span class="n">types</span><span class="p">.</span><span class="nc">Tool</span><span class="p">(</span><span class="n">google_search</span><span class="o">=</span><span class="n">types</span><span class="p">.</span><span class="nc">GoogleSearch</span><span class="p">())],</span>
    <span class="n">temperature</span><span class="o">=</span><span class="mf">0.0</span>
<span class="p">)</span>

<span class="n">chat</span> <span class="o">=</span> <span class="n">api</span><span class="p">.</span><span class="n">args</span><span class="p">.</span><span class="n">CLIENT</span><span class="p">.</span><span class="n">chats</span><span class="p">.</span><span class="nf">create</span><span class="p">(</span>
    <span class="n">model</span><span class="o">=</span><span class="nf">api</span><span class="p">(</span><span class="n">Api</span><span class="p">.</span><span class="n">Model</span><span class="p">.</span><span class="n">GEN</span><span class="p">),</span>
    <span class="n">config</span><span class="o">=</span><span class="n">config_with_search</span><span class="p">,</span>
    <span class="n">history</span><span class="o">=</span><span class="p">[])</span> <span class="c1"># Ignoring the part about dark elves, and tengwar.
</span>
<span class="n">response</span> <span class="o">=</span> <span class="n">chat</span><span class="p">.</span><span class="nf">send_message</span><span class="p">(</span><span class="sh">'</span><span class="s">Do you know anything about the stock market?</span><span class="sh">'</span><span class="p">)</span>
<span class="nc">Markdown</span><span class="p">(</span><span class="n">response</span><span class="p">.</span><span class="n">text</span><span class="p">)</span>
</code></pre></div></div>

<p>The stock market is a global network of exchanges and over-the-counter (OTC) marketplaces where investors buy and sell shares of publicly traded companies. These shares, also known as equities, represent fractional ownership in a company.</p>

<p><strong>Purpose of the Stock Market</strong>
The stock market serves two primary functions:</p>
<ul>
  <li><strong>For Companies:</strong> It allows companies to raise capital (money) by issuing shares to the public through a process called an Initial Public Offering (IPO). This capital can then be used to fund and expand their businesses.</li>
  <li><strong>For Investors:</strong> It provides individuals and institutions with an opportunity to invest in businesses and potentially grow their wealth over time. Investors can profit through dividends (a share of the company’s profits) or by selling their shares at a higher price than they bought them for (capital gains).</li>
</ul>

<p><strong>How the Stock Market Works</strong>
The stock market operates through two main types of markets:</p>
<ul>
  <li><strong>Primary Market:</strong> This is where new stocks are first issued. When a private company decides to go public, it lists its shares on an exchange through an IPO, selling them directly to investors to raise capital.</li>
  <li><strong>Secondary Market:</strong> After the initial issuance, these shares are traded among investors on stock exchanges (like the New York Stock Exchange or Nasdaq). The company is not directly involved in these subsequent transactions.</li>
</ul>

<p>Stock prices are primarily determined by the forces of supply and demand. If more investors want to buy a stock than sell it, the price tends to rise, and vice versa. This process is known as price discovery.</p>

<p><strong>Key Components and Participants</strong></p>
<ul>
  <li><strong>Stock Exchanges:</strong> These are organized and regulated platforms (often virtual) where stocks and other securities are bought and sold.</li>
  <li><strong>Brokers:</strong> These are intermediaries who execute buy and sell orders on behalf of investors.</li>
  <li><strong>Investors and Traders:</strong> Participants range from individual retail investors to large institutional investors like pension funds, mutual funds, insurance companies, and hedge funds.</li>
</ul>

<p><strong>Types of Investments in the Stock Market</strong>
Beyond just common stocks, the stock market offers various investment instruments:</p>
<ul>
  <li><strong>Stocks (Equities):</strong>
    <ul>
      <li><strong>Common Stock:</strong> Represents partial ownership, gives voting rights on corporate decisions, and offers potential for higher returns, but also higher risk.</li>
      <li><strong>Preferred Stock:</strong> Typically offers fixed dividend payments before common stockholders receive theirs, but usually does not come with voting rights.</li>
      <li><strong>Categorized by Market Capitalization:</strong> Large-cap (companies with market capitalization of $10 billion or more, generally stable), Mid-cap ($2 billion to $10 billion), and Small-cap (less than $2 billion, higher growth potential but riskier).</li>
      <li><strong>Categorized by Investment Style:</strong> Growth stocks (companies with strong potential for rapid growth), Value stocks (undervalued companies that investors believe will rise in price), and Income stocks (companies that pay regular, often higher-than-average, dividends).</li>
    </ul>
  </li>
  <li><strong>Bonds:</strong> These are debt securities where investors essentially lend money to governments or corporations for a set period, receiving regular interest payments.</li>
  <li><strong>Mutual Funds:</strong> These pool money from many investors to invest in a diversified portfolio of stocks, bonds, or other securities, managed by a professional fund manager.</li>
  <li><strong>Exchange-Traded Funds (ETFs):</strong> Similar to mutual funds, but they trade like individual stocks on exchanges throughout the day.</li>
  <li><strong>Derivatives:</strong> Complex financial instruments whose value is derived from an underlying asset, such as stocks. These are generally considered high-risk and not recommended for beginners.</li>
</ul>

<p><strong>Factors Influencing Stock Prices</strong>
Stock market movements are influenced by a variety of factors, including company performance (earnings reports, product launches), macroeconomic indicators (interest rates, inflation, GDP growth), political events, international trade policies, and overall investor sentiment.</p>

<div class="language-python highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="n">response</span> <span class="o">=</span> <span class="n">chat</span><span class="p">.</span><span class="nf">send_message</span><span class="p">(</span><span class="sh">'</span><span class="s">I have an interest in AMZN stock</span><span class="sh">'</span><span class="p">)</span>
<span class="nc">Markdown</span><span class="p">(</span><span class="n">response</span><span class="p">.</span><span class="n">text</span><span class="p">)</span>
</code></pre></div></div>
<p>Amazon.com Inc. (NASDAQ: AMZN) is a widely followed stock, known for its dominant presence in e-commerce, cloud computing (Amazon Web Services - AWS), and digital advertising.</p>

<p>Here’s a snapshot of AMZN stock as of December 1, 2025:</p>

<p><strong>Current Price and Performance:</strong></p>
<ul>
  <li>The current price of AMZN stock is approximately $233.22 USD.</li>
  <li>It has seen a 1.77% increase in the past 24 hours.</li>
  <li>Over the past week, AMZN stock has risen by 7.80%, and over the last year, it has shown a 12.68% increase.</li>
  <li>The stock’s 52-week high is $258.60 and its 52-week low is $161.38.</li>
</ul>

<p><strong>Key Financials and Metrics:</strong></p>
<ul>
  <li>Amazon’s market capitalization is approximately $2.49 trillion.</li>
  <li>The company’s Price-to-Earnings (P/E) ratio is around 32.95.</li>
  <li>Amazon does not currently pay dividends to shareholders, as it reinvests earnings into growth areas.</li>
  <li>AMZN stock has a beta coefficient of 1.41, indicating its volatility.</li>
</ul>

<p><strong>Analyst Outlook:</strong></p>
<ul>
  <li>The overall consensus from 34 analysts over the last three months is a “Strong Buy” for AMZN.</li>
  <li>The average price target for Amazon.com Inc. is around $298.13, with a maximum estimate of $360.00 and a minimum estimate of $250.00. Oppenheimer recently raised its price target to $305.00 from $290.00, maintaining an “Outperform” rating.</li>
</ul>

<p><strong>Business Segments and Growth Drivers:</strong></p>
<ul>
  <li>Amazon’s revenue primarily comes from its retail operations (approximately 74%), followed by Amazon Web Services (AWS) (17%), and advertising services (9%).</li>
  <li>AWS is a significant growth driver, with its revenue growing by 20.2% year-over-year in the third quarter of 2025 and a reported $200 billion backlog.</li>
  <li>The company continues to expand in areas such as artificial intelligence (AI), cloud computing, global e-commerce, streaming, and logistics automation.</li>
</ul>

<p><strong>Recent News and Influencing Factors:</strong></p>
<ul>
  <li>Amazon Web Services recently launched a new multicloud service to enhance data movement with Google Cloud, following an outage in October that caused significant losses for U.S. companies.</li>
  <li>Amazon is participating in a $400 billion investment in AI by 2025, which is expected to significantly impact the U.S. economy.</li>
  <li>AI shopping tools, including Amazon’s Rufus, are projected to boost traffic to U.S. retail sites by 670% this holiday season compared to last year.</li>
  <li>Oppenheimer’s analysis suggests significant upside potential for AWS through 2027, with plans to double its capacity.</li>
  <li>Amazon’s stock price can be influenced by quarterly earnings, changes in cloud computing demand, consumer spending trends, new business initiatives, and broader economic conditions like inflation and interest rates.</li>
</ul>

<p><strong>Historical Context:</strong></p>
<ul>
  <li>AMZN reached its all-time high on November 2, 2025, with a price of $258.60 USD.</li>
  <li>The company conducted a 20-for-1 stock split in June 2022 to make shares more accessible to retail investors.</li>
</ul>

<div class="language-python highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="n">response</span> <span class="o">=</span> <span class="n">chat</span><span class="p">.</span><span class="nf">send_message</span><span class="p">(</span><span class="sh">'''</span><span class="s">Tell me about AMZN current share price, short-term trends, and bullish versus bearish predictions</span><span class="sh">'''</span><span class="p">)</span>
<span class="nc">Markdown</span><span class="p">(</span><span class="n">response</span><span class="p">.</span><span class="n">text</span><span class="p">)</span>
</code></pre></div></div>
<p>Amazon.com Inc. (NASDAQ: AMZN) is currently trading at approximately $233.22 USD as of December 1, 2025. The stock has shown an increase of 1.77% in the past 24 hours, a 7.80% rise over the last week, and a 0.67% increase over the past month. Over the last year, AMZN has seen a 12.68% increase. The stock’s 52-week high is $258.60, and its 52-week low is $161.38.</p>

<p><strong>Short-Term Trends</strong></p>

<p>In the short term, AMZN stock is exhibiting signs of strength. It has risen by 7.39% since a pivot bottom point on Thursday, November 20, 2025, with further increases indicated until a new top pivot is found. The stock holds buy signals from both short and long-term Moving Averages, suggesting a positive forecast. Technical analysis indicates that AMZN is breaking out above a horizontal support zone and shows enough bullish momentum for a break-in above its ascending Fibonacci Retracement Fan. The Bull Bear Power Indicator has also turned bullish with an ascending trendline, and average bullish trading volumes have been higher than bearish trading volumes over the past week.</p>

<p>However, some short-term forecasts suggest potential minor fluctuations. One prediction indicates that the value of AMZN shares could drop by -2.60% to $227.12 per share by December 30, 2025. Another short-term forecast suggests a slight decrease to $230.68 by December 2, 2025, and $229.65 by December 3, 2025, before potentially rising to $233.80 by December 5, 2025. Despite these minor predicted dips, the overall sentiment based on technical indicators is bullish.</p>

<p><strong>Bullish Versus Bearish Predictions</strong></p>

<p>The overwhelming sentiment from analysts regarding AMZN stock is bullish. A consensus of 43 analysts over the last three months rates AMZN as a “Strong Buy,” with 41 assigning a “Buy” rating and two a “Hold” rating. The average price target from 44 Wall Street analysts for the next 12 months is around $295.23, representing a potential upside of 28.83% from the current price, with a high forecast of $340.00 and a low forecast of $250.00. Other analyst targets range from an average of $282.48 to $298.13, all suggesting significant upside potential.</p>

<p>Key drivers for these bullish predictions include:</p>
<ul>
  <li><strong>Accelerated AWS Growth:</strong> Amazon Web Services (AWS) revenue accelerated to 20.2% year-over-year growth in the third quarter of 2025, up from 17.5% in the second quarter. AWS also has a reported $200 billion backlog. Analysts project AWS revenue to reach $128.1 billion in 2025, growing to $348.5 billion in 2030.</li>
  <li><strong>AI Demand:</strong> Amazon is well-positioned amid surging AI demand and cloud infrastructure growth. The company’s recent multi-year deal with OpenAI, involving a $38 billion commitment for OpenAI to leverage AWS compute, further highlights its role in the AI space. AWS’s Trainium chips business is also experiencing rapid growth.</li>
  <li><strong>E-commerce and Advertising:</strong> Amazon’s retail operations continue to be a primary revenue source, and its advertising business is expected to continue outperforming expectations.</li>
  <li><strong>Warehouse Automation:</strong> Robotics deployment across fulfillment centers is expected to deliver substantial cost savings and improve fulfillment costs by 20% to 40%.</li>
</ul>

<p>While the overall outlook is strongly bullish, some potential bearish considerations exist. Concerns about the company’s enormous AI capital expenditures remain. Additionally, while AWS growth is strong, it may not be as fast as competing cloud services like Microsoft Azure and Google Cloud, posing a risk of market share losses before 2030 if Amazon cannot maintain its competitive edge. Some short-term technical indicators have also shown a “general sell signal” from the relation between long-term and short-term moving averages, where the long-term average is above the short-term average. However, this is largely overshadowed by other positive signals.</p>

<div class="language-python highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="n">response</span> <span class="o">=</span> <span class="n">chat</span><span class="p">.</span><span class="nf">send_message</span><span class="p">(</span><span class="sh">'''</span><span class="s">What is mgm studio</span><span class="sh">'</span><span class="s">s stock ticker symbol?</span><span class="sh">'''</span><span class="p">)</span>
<span class="nc">Markdown</span><span class="p">(</span><span class="n">response</span><span class="p">.</span><span class="n">text</span><span class="p">)</span>
</code></pre></div></div>
<p>MGM Studios, as an independent entity, does not have a publicly traded stock ticker symbol. MGM Holdings, the parent company of MGM Studios, was acquired by Amazon in 2022. Therefore, MGM Studios is now part of Amazon, and its financial performance is reflected within Amazon’s overall operations (NASDAQ: AMZN).</p>

<p>However, there is a publicly traded company called <strong>MGM Resorts International</strong>, which operates casinos and resorts and uses the stock ticker symbol <strong>MGM</strong> on the New York Stock Exchange (NYSE). This company is distinct from the film and television studio.</p>

<div class="language-python highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="n">response</span> <span class="o">=</span> <span class="n">chat</span><span class="p">.</span><span class="nf">send_message</span><span class="p">(</span><span class="sh">'''</span><span class="s">What was the last open,close,high,low data for AMZN again?</span><span class="sh">'''</span><span class="p">)</span>
<span class="nc">Markdown</span><span class="p">(</span><span class="n">response</span><span class="p">.</span><span class="n">text</span><span class="p">)</span>
</code></pre></div></div>
<p>As of Friday, November 28, 2025, the last recorded trading day, Amazon (AMZN) stock had the following data:</p>

<ul>
  <li><strong>Close/Last Price:</strong> $233.22</li>
  <li><strong>Open Price:</strong> $231.24</li>
  <li><strong>High Price:</strong> $233.28</li>
  <li><strong>Low Price:</strong> $230.22</li>
</ul>

<div class="language-python highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="n">response</span> <span class="o">=</span> <span class="n">chat</span><span class="p">.</span><span class="nf">send_message</span><span class="p">(</span><span class="sh">'''</span><span class="s">What is AMZN open,close,high,low data for the past month? 
Present the data with multiple columns for display in markdown.</span><span class="sh">'''</span><span class="p">)</span>
<span class="nc">Markdown</span><span class="p">(</span><span class="n">response</span><span class="p">.</span><span class="n">text</span><span class="p">)</span>
</code></pre></div></div>
<p>Here is the open, close, high, and low data for Amazon (AMZN) stock for the past month, from October 31, 2025, to November 28, 2025:</p>

<table>
  <thead>
    <tr>
      <th style="text-align: left">Date</th>
      <th style="text-align: left">Open (USD)</th>
      <th style="text-align: left">Close (USD)</th>
      <th style="text-align: left">High (USD)</th>
      <th style="text-align: left">Low (USD)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align: left">Nov 28, 2025</td>
      <td style="text-align: left">$231.24</td>
      <td style="text-align: left">$233.22</td>
      <td style="text-align: left">$233.28</td>
      <td style="text-align: left">$230.22</td>
    </tr>
    <tr>
      <td style="text-align: left">Nov 26, 2025</td>
      <td style="text-align: left">$230.74</td>
      <td style="text-align: left">$229.16</td>
      <td style="text-align: left">$231.75</td>
      <td style="text-align: left">$228.77</td>
    </tr>
    <tr>
      <td style="text-align: left">Nov 25, 2025</td>
      <td style="text-align: left">$226.38</td>
      <td style="text-align: left">$229.67</td>
      <td style="text-align: left">$230.52</td>
      <td style="text-align: left">$223.80</td>
    </tr>
    <tr>
      <td style="text-align: left">Nov 24, 2025</td>
      <td style="text-align: left">$222.56</td>
      <td style="text-align: left">$226.28</td>
      <td style="text-align: left">$227.33</td>
      <td style="text-align: left">$222.27</td>
    </tr>
    <tr>
      <td style="text-align: left">Nov 21, 2025</td>
      <td style="text-align: left">$216.34</td>
      <td style="text-align: left">$220.69</td>
      <td style="text-align: left">$222.21</td>
      <td style="text-align: left">$215.18</td>
    </tr>
    <tr>
      <td style="text-align: left">Nov 20, 2025</td>
      <td style="text-align: left">$227.05</td>
      <td style="text-align: left">$217.14</td>
      <td style="text-align: left">$227.41</td>
      <td style="text-align: left">$216.74</td>
    </tr>
    <tr>
      <td style="text-align: left">Nov 19, 2025</td>
      <td style="text-align: left">$223.74</td>
      <td style="text-align: left">$222.69</td>
      <td style="text-align: left">$223.74</td>
      <td style="text-align: left">$218.52</td>
    </tr>
    <tr>
      <td style="text-align: left">Nov 18, 2025</td>
      <td style="text-align: left">$228.10</td>
      <td style="text-align: left">$222.55</td>
      <td style="text-align: left">$230.20</td>
      <td style="text-align: left">$222.42</td>
    </tr>
    <tr>
      <td style="text-align: left">Nov 17, 2025</td>
      <td style="text-align: left">$233.25</td>
      <td style="text-align: left">$232.87</td>
      <td style="text-align: left">$234.60</td>
      <td style="text-align: left">$229.19</td>
    </tr>
    <tr>
      <td style="text-align: left">Nov 14, 2025</td>
      <td style="text-align: left">$235.06</td>
      <td style="text-align: left">$234.69</td>
      <td style="text-align: left">$238.73</td>
      <td style="text-align: left">$232.89</td>
    </tr>
    <tr>
      <td style="text-align: left">Nov 13, 2025</td>
      <td style="text-align: left">$243.05</td>
      <td style="text-align: left">$237.58</td>
      <td style="text-align: left">$243.75</td>
      <td style="text-align: left">$236.50</td>
    </tr>
    <tr>
      <td style="text-align: left">Nov 12, 2025</td>
      <td style="text-align: left">$250.24</td>
      <td style="text-align: left">$244.20</td>
      <td style="text-align: left">$250.37</td>
      <td style="text-align: left">$243.75</td>
    </tr>
    <tr>
      <td style="text-align: left">Nov 11, 2025</td>
      <td style="text-align: left">$248.41</td>
      <td style="text-align: left">$249.10</td>
      <td style="text-align: left">$249.75</td>
      <td style="text-align: left">$247.23</td>
    </tr>
    <tr>
      <td style="text-align: left">Nov 10, 2025</td>
      <td style="text-align: left">$248.34</td>
      <td style="text-align: left">$248.40</td>
      <td style="text-align: left">$251.75</td>
      <td style="text-align: left">$245.59</td>
    </tr>
    <tr>
      <td style="text-align: left">Nov 07, 2025</td>
      <td style="text-align: left">$242.90</td>
      <td style="text-align: left">$244.41</td>
      <td style="text-align: left">$244.90</td>
      <td style="text-align: left">$238.49</td>
    </tr>
    <tr>
      <td style="text-align: left">Nov 06, 2025</td>
      <td style="text-align: left">$249.16</td>
      <td style="text-align: left">$243.04</td>
      <td style="text-align: left">$250.38</td>
      <td style="text-align: left">$242.17</td>
    </tr>
    <tr>
      <td style="text-align: left">Nov 05, 2025</td>
      <td style="text-align: left">$249.03</td>
      <td style="text-align: left">$250.20</td>
      <td style="text-align: left">$251.00</td>
      <td style="text-align: left">$246.16</td>
    </tr>
    <tr>
      <td style="text-align: left">Nov 04, 2025</td>
      <td style="text-align: left">$250.38</td>
      <td style="text-align: left">$249.32</td>
      <td style="text-align: left">$257.01</td>
      <td style="text-align: left">$248.66</td>
    </tr>
    <tr>
      <td style="text-align: left">Nov 03, 2025</td>
      <td style="text-align: left">$255.36</td>
      <td style="text-align: left">$254.00</td>
      <td style="text-align: left">$258.60</td>
      <td style="text-align: left">$252.90</td>
    </tr>
    <tr>
      <td style="text-align: left">Oct 31, 2025</td>
      <td style="text-align: left">$250.10</td>
      <td style="text-align: left">$244.22</td>
      <td style="text-align: left">$250.50</td>
      <td style="text-align: left">$243.98</td>
    </tr>
    <tr>
      <td style="text-align: left">Oct 30, 2025</td>
      <td style="text-align: left">$227.06</td>
      <td style="text-align: left">$222.86</td>
      <td style="text-align: left">$228.44</td>
      <td style="text-align: left">$222.75</td>
    </tr>
    <tr>
      <td style="text-align: left">Oct 29, 2025</td>
      <td style="text-align: left">$231.67</td>
      <td style="text-align: left">$230.30</td>
      <td style="text-align: left">$231.67</td>
      <td style="text-align: left">$228.22</td>
    </tr>
    <tr>
      <td style="text-align: left">Oct 28, 2025</td>
      <td style="text-align: left">$228.22</td>
      <td style="text-align: left">$229.25</td>
      <td style="text-align: left">$231.49</td>
      <td style="text-align: left">$226.21</td>
    </tr>
    <tr>
      <td style="text-align: left">Oct 27, 2025</td>
      <td style="text-align: left">$227.66</td>
      <td style="text-align: left">$226.97</td>
      <td style="text-align: left">$228.40</td>
      <td style="text-align: left">$225.54</td>
    </tr>
    <tr>
      <td style="text-align: left">Oct 26, 2025</td>
      <td style="text-align: left">$221.09</td>
      <td style="text-align: left">$224.21</td>
      <td style="text-align: left">$224.21</td>
      <td style="text-align: left">$221.09</td>
    </tr>
  </tbody>
</table>

<p>Please note that stock market data can fluctuate rapidly, and the prices provided are based on the last available information from the specified dates.</p>

<h2 id="previously-on-kaggle-stockchat-10">Previously on Kaggle: StockChat 1.0</h2>

<h3 id="validation-basemodels">Validation BaseModels</h3>

<div class="language-python highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="c1"># Validation BaseModels in pydantic schema.
</span><span class="k">class</span> <span class="nc">RestStatus</span><span class="p">(</span><span class="n">Enum</span><span class="p">):</span>
    <span class="n">OK</span> <span class="o">=</span> <span class="sh">"</span><span class="s">OK</span><span class="sh">"</span>
    <span class="n">DELAY</span> <span class="o">=</span> <span class="sh">"</span><span class="s">DELAYED</span><span class="sh">"</span>
    <span class="n">NONE</span> <span class="o">=</span> <span class="sh">"</span><span class="s">NOT_FOUND</span><span class="sh">"</span>
    <span class="n">AUTH</span> <span class="o">=</span> <span class="sh">"</span><span class="s">NOT_AUTHORIZED</span><span class="sh">"</span>

<span class="k">class</span> <span class="nc">StopGeneration</span><span class="p">(</span><span class="n">BaseModel</span><span class="p">):</span>
    <span class="n">result</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="n">Api</span><span class="p">.</span><span class="n">Const</span><span class="p">.</span><span class="nc">Stop</span><span class="p">()</span>

<span class="k">class</span> <span class="nc">RestResultPoly</span><span class="p">(</span><span class="n">BaseModel</span><span class="p">):</span>
    <span class="n">request_id</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="bp">None</span>
    <span class="n">count</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="bp">None</span>
    <span class="n">next_url</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="bp">None</span>
    <span class="n">status</span><span class="p">:</span> <span class="n">RestStatus</span>  

<span class="k">class</span> <span class="nc">MarketSession</span><span class="p">(</span><span class="n">Enum</span><span class="p">):</span>
    <span class="n">PRE</span> <span class="o">=</span> <span class="sh">"</span><span class="s">pre-market</span><span class="sh">"</span>
    <span class="n">REG</span> <span class="o">=</span> <span class="sh">"</span><span class="s">regular</span><span class="sh">"</span>
    <span class="n">POST</span> <span class="o">=</span> <span class="sh">"</span><span class="s">post-market</span><span class="sh">"</span>
    <span class="n">CLOSED</span> <span class="o">=</span> <span class="sh">"</span><span class="s">closed</span><span class="sh">"</span>
    <span class="n">NA</span> <span class="o">=</span> <span class="sh">"</span><span class="s">not applicable</span><span class="sh">"</span>

<span class="k">class</span> <span class="nc">MarketEvent</span><span class="p">(</span><span class="n">Enum</span><span class="p">):</span>
    <span class="n">PRE_OPEN</span> <span class="o">=</span> <span class="mi">0</span>
    <span class="n">REG_OPEN</span> <span class="o">=</span> <span class="mi">1</span>
    <span class="n">REG_CLOSE</span> <span class="o">=</span> <span class="mi">2</span>
    <span class="n">POST_CLOSE</span> <span class="o">=</span> <span class="mi">3</span>
    <span class="n">LAST_CLOSE</span> <span class="o">=</span> <span class="mi">4</span>

<span class="k">class</span> <span class="nc">AssetClass</span><span class="p">(</span><span class="n">Enum</span><span class="p">):</span>
    <span class="n">STOCKS</span> <span class="o">=</span> <span class="sh">"</span><span class="s">stocks</span><span class="sh">"</span>
    <span class="n">OPTION</span> <span class="o">=</span> <span class="sh">"</span><span class="s">options</span><span class="sh">"</span>
    <span class="n">CRYPTO</span> <span class="o">=</span> <span class="sh">"</span><span class="s">crypto</span><span class="sh">"</span>
    <span class="n">FOREX</span> <span class="o">=</span> <span class="sh">"</span><span class="s">fx</span><span class="sh">"</span>
    <span class="n">INDEX</span> <span class="o">=</span> <span class="sh">"</span><span class="s">indices</span><span class="sh">"</span>
    <span class="n">OTC</span> <span class="o">=</span> <span class="sh">"</span><span class="s">otc</span><span class="sh">"</span>

<span class="k">class</span> <span class="nc">SymbolType</span><span class="p">(</span><span class="n">Enum</span><span class="p">):</span>
    <span class="n">COMMON</span> <span class="o">=</span> <span class="sh">"</span><span class="s">Common Stock</span><span class="sh">"</span>
    <span class="n">ETP</span> <span class="o">=</span> <span class="sh">"</span><span class="s">ETP</span><span class="sh">"</span>
    <span class="n">ADR</span> <span class="o">=</span> <span class="sh">"</span><span class="s">ADR</span><span class="sh">"</span>
    <span class="n">REIT</span> <span class="o">=</span> <span class="sh">"</span><span class="s">REIT</span><span class="sh">"</span>
    <span class="n">DELISTED</span> <span class="o">=</span> <span class="sh">""</span>
    <span class="n">CEF</span> <span class="o">=</span> <span class="sh">"</span><span class="s">Closed-End Fund</span><span class="sh">"</span>
    <span class="n">UNIT</span> <span class="o">=</span> <span class="sh">"</span><span class="s">Unit</span><span class="sh">"</span>
    <span class="n">RIGHT</span> <span class="o">=</span> <span class="sh">"</span><span class="s">Right</span><span class="sh">"</span>
    <span class="n">EQUITY</span> <span class="o">=</span> <span class="sh">"</span><span class="s">Equity WRT</span><span class="sh">"</span>
    <span class="n">GDR</span> <span class="o">=</span> <span class="sh">"</span><span class="s">GDR</span><span class="sh">"</span>
    <span class="n">PREF</span> <span class="o">=</span> <span class="sh">"</span><span class="s">Preference</span><span class="sh">"</span>
    <span class="n">CDI</span> <span class="o">=</span> <span class="sh">"</span><span class="s">CDI</span><span class="sh">"</span>
    <span class="n">NVDR</span> <span class="o">=</span> <span class="sh">"</span><span class="s">NVDR</span><span class="sh">"</span>
    <span class="n">REG</span> <span class="o">=</span> <span class="sh">"</span><span class="s">NY Reg Shrs</span><span class="sh">"</span>
    <span class="n">MLP</span> <span class="o">=</span> <span class="sh">"</span><span class="s">MLP</span><span class="sh">"</span>
    <span class="n">MUTUAL</span> <span class="o">=</span> <span class="sh">"</span><span class="s">Mutual Fund</span><span class="sh">"</span>

<span class="k">class</span> <span class="nc">Locale</span><span class="p">(</span><span class="n">Enum</span><span class="p">):</span>
    <span class="n">US</span> <span class="o">=</span> <span class="sh">"</span><span class="s">us</span><span class="sh">"</span>
    <span class="n">GLOBAL</span> <span class="o">=</span> <span class="sh">"</span><span class="s">global</span><span class="sh">"</span>

<span class="k">class</span> <span class="nc">Sentiment</span><span class="p">(</span><span class="n">Enum</span><span class="p">):</span>
    <span class="n">V_POS</span> <span class="o">=</span> <span class="sh">"</span><span class="s">very positive</span><span class="sh">"</span>
    <span class="n">POSITIVE</span> <span class="o">=</span> <span class="sh">"</span><span class="s">positive</span><span class="sh">"</span>
    <span class="n">NEUTRAL_P</span> <span class="o">=</span> <span class="sh">"</span><span class="s">neutral/positive</span><span class="sh">"</span>
    <span class="n">NEUTRAL_SP</span> <span class="o">=</span> <span class="sh">"</span><span class="s">neutral/slightly positive</span><span class="sh">"</span>
    <span class="n">NEUTRAL</span> <span class="o">=</span> <span class="sh">"</span><span class="s">neutral</span><span class="sh">"</span>
    <span class="n">NEUTRAL_SN</span> <span class="o">=</span> <span class="sh">"</span><span class="s">neutral/slightly negative</span><span class="sh">"</span>
    <span class="n">NEUTRAL_N</span> <span class="o">=</span> <span class="sh">"</span><span class="s">neutral/negative</span><span class="sh">"</span>
    <span class="n">MIXED</span> <span class="o">=</span> <span class="sh">"</span><span class="s">mixed</span><span class="sh">"</span>
    <span class="n">NEGATIVE</span> <span class="o">=</span> <span class="sh">"</span><span class="s">negative</span><span class="sh">"</span>
    <span class="n">V_NEG</span> <span class="o">=</span> <span class="sh">"</span><span class="s">very negative</span><span class="sh">"</span>

<span class="k">class</span> <span class="nc">Trend</span><span class="p">(</span><span class="n">Enum</span><span class="p">):</span>
    <span class="n">S_BUY</span> <span class="o">=</span> <span class="sh">"</span><span class="s">strong-buy</span><span class="sh">"</span>
    <span class="n">BUY</span> <span class="o">=</span> <span class="sh">"</span><span class="s">buy</span><span class="sh">"</span>
    <span class="n">HOLD</span> <span class="o">=</span> <span class="sh">"</span><span class="s">hold</span><span class="sh">"</span>
    <span class="n">SELL</span> <span class="o">=</span> <span class="sh">"</span><span class="s">sell</span><span class="sh">"</span>
    <span class="n">S_SELL</span> <span class="o">=</span> <span class="sh">"</span><span class="s">strong-sell</span><span class="sh">"</span>

<span class="k">class</span> <span class="nc">MarketCondition</span><span class="p">(</span><span class="n">Enum</span><span class="p">):</span>
    <span class="n">BULL</span> <span class="o">=</span> <span class="sh">"</span><span class="s">bullish</span><span class="sh">"</span>
    <span class="n">BULLN</span> <span class="o">=</span> <span class="sh">"</span><span class="s">cautiously bullish</span><span class="sh">"</span>
    <span class="n">HOLD</span> <span class="o">=</span> <span class="sh">"</span><span class="s">hold</span><span class="sh">"</span>
    <span class="n">BEARN</span> <span class="o">=</span> <span class="sh">"</span><span class="s">cautiously bearish</span><span class="sh">"</span>
    <span class="n">BEAR</span> <span class="o">=</span> <span class="sh">"</span><span class="s">bearish</span><span class="sh">"</span>

<span class="k">class</span> <span class="nc">GeneratedEvent</span><span class="p">(</span><span class="n">BaseModel</span><span class="p">):</span>
    <span class="n">last_close</span><span class="p">:</span> <span class="nb">str</span>
    <span class="n">pre_open</span><span class="p">:</span> <span class="nb">str</span>
    <span class="n">reg_open</span><span class="p">:</span> <span class="nb">str</span>
    <span class="n">reg_close</span><span class="p">:</span> <span class="nb">str</span>
    <span class="n">post_close</span><span class="p">:</span> <span class="nb">str</span>
    <span class="n">timestamp</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="bp">None</span>
    <span class="n">is_holiday</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">bool</span><span class="p">]</span> <span class="o">=</span> <span class="bp">None</span>

    <span class="k">def</span> <span class="nf">model_post_init</span><span class="p">(</span><span class="n">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="bp">None</span><span class="p">:</span>
        <span class="k">if</span> <span class="n">self</span><span class="p">.</span><span class="n">timestamp</span> <span class="ow">is</span> <span class="bp">None</span><span class="p">:</span>
            <span class="n">self</span><span class="p">.</span><span class="n">timestamp</span> <span class="o">=</span> <span class="n">datetime</span><span class="p">.</span><span class="nf">now</span><span class="p">(</span><span class="n">self</span><span class="p">.</span><span class="nf">tz</span><span class="p">()).</span><span class="nf">strftime</span><span class="p">(</span><span class="sh">'</span><span class="s">%c</span><span class="sh">'</span><span class="p">)</span>
        <span class="k">if</span> <span class="n">self</span><span class="p">.</span><span class="n">is_holiday</span> <span class="ow">is</span> <span class="bp">None</span><span class="p">:</span>
            <span class="n">self</span><span class="p">.</span><span class="n">is_holiday</span> <span class="o">=</span> <span class="bp">False</span>

    <span class="k">def</span> <span class="nf">session</span><span class="p">(</span><span class="n">self</span><span class="p">,</span> <span class="n">with_date</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="bp">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">MarketSession</span><span class="p">:</span>
        <span class="k">if</span> <span class="n">with_date</span> <span class="ow">is</span> <span class="bp">None</span><span class="p">:</span>
            <span class="n">with_date</span> <span class="o">=</span> <span class="n">datetime</span><span class="p">.</span><span class="nf">now</span><span class="p">(</span><span class="n">self</span><span class="p">.</span><span class="nf">tz</span><span class="p">()).</span><span class="nf">strftime</span><span class="p">(</span><span class="sh">'</span><span class="s">%c</span><span class="sh">'</span><span class="p">)</span>
        <span class="n">compare</span> <span class="o">=</span> <span class="nf">parse</span><span class="p">(</span><span class="n">with_date</span><span class="p">)</span>
        <span class="k">if</span> <span class="n">self</span><span class="p">.</span><span class="n">is_holiday</span> <span class="ow">or</span> <span class="n">compare</span><span class="p">.</span><span class="nf">weekday</span><span class="p">()</span> <span class="o">&gt;</span> <span class="mi">4</span><span class="p">:</span> <span class="c1"># weekend
</span>            <span class="k">return</span> <span class="n">MarketSession</span><span class="p">.</span><span class="n">CLOSED</span>
        <span class="n">events</span> <span class="o">=</span> <span class="p">[</span><span class="nf">parse</span><span class="p">(</span><span class="n">event</span><span class="p">).</span><span class="nf">time</span><span class="p">()</span> <span class="k">for</span> <span class="n">event</span> <span class="ow">in</span> <span class="p">[</span><span class="n">self</span><span class="p">.</span><span class="n">pre_open</span><span class="p">,</span><span class="n">self</span><span class="p">.</span><span class="n">reg_open</span><span class="p">,</span><span class="n">self</span><span class="p">.</span><span class="n">reg_close</span><span class="p">,</span><span class="n">self</span><span class="p">.</span><span class="n">post_close</span><span class="p">]]</span>
        <span class="k">if</span> <span class="n">compare</span><span class="p">.</span><span class="nf">time</span><span class="p">()</span> <span class="o">&lt;</span> <span class="n">events</span><span class="p">[</span><span class="mi">0</span><span class="p">]:</span>
            <span class="k">return</span> <span class="n">MarketSession</span><span class="p">.</span><span class="n">CLOSED</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">session</span> <span class="o">=</span> <span class="n">MarketSession</span><span class="p">.</span><span class="n">NA</span>
            <span class="k">if</span> <span class="n">compare</span><span class="p">.</span><span class="nf">time</span><span class="p">()</span> <span class="o">&gt;=</span> <span class="n">events</span><span class="p">[</span><span class="mi">0</span><span class="p">]:</span>
                <span class="n">session</span> <span class="o">=</span> <span class="n">MarketSession</span><span class="p">.</span><span class="n">PRE</span>
            <span class="k">if</span> <span class="n">compare</span><span class="p">.</span><span class="nf">time</span><span class="p">()</span> <span class="o">&gt;=</span> <span class="n">events</span><span class="p">[</span><span class="mi">1</span><span class="p">]:</span>
                <span class="n">session</span> <span class="o">=</span> <span class="n">MarketSession</span><span class="p">.</span><span class="n">REG</span>
            <span class="k">if</span> <span class="n">compare</span><span class="p">.</span><span class="nf">time</span><span class="p">()</span> <span class="o">&gt;=</span> <span class="n">events</span><span class="p">[</span><span class="mi">2</span><span class="p">]:</span>
                <span class="n">session</span> <span class="o">=</span> <span class="n">MarketSession</span><span class="p">.</span><span class="n">POST</span>
            <span class="k">if</span> <span class="n">compare</span><span class="p">.</span><span class="nf">time</span><span class="p">()</span> <span class="o">&gt;=</span> <span class="n">events</span><span class="p">[</span><span class="mi">3</span><span class="p">]:</span>
                <span class="n">session</span> <span class="o">=</span> <span class="n">MarketSession</span><span class="p">.</span><span class="n">CLOSED</span>
        <span class="k">return</span> <span class="n">session</span>

    <span class="k">def</span> <span class="nf">is_open</span><span class="p">(</span><span class="n">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
        <span class="k">return</span> <span class="n">self</span><span class="p">.</span><span class="nf">session</span><span class="p">()</span> <span class="o">!=</span> <span class="n">MarketSession</span><span class="p">.</span><span class="n">CLOSED</span>

    <span class="k">def</span> <span class="nf">has_update</span><span class="p">(</span><span class="n">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
        <span class="n">datetime_now</span> <span class="o">=</span> <span class="n">datetime</span><span class="p">.</span><span class="nf">now</span><span class="p">(</span><span class="n">self</span><span class="p">.</span><span class="nf">tz</span><span class="p">())</span>
        <span class="n">self_ts</span> <span class="o">=</span> <span class="nf">parse</span><span class="p">(</span><span class="n">self</span><span class="p">.</span><span class="n">timestamp</span><span class="p">)</span>
        <span class="c1"># Re-generate events for a new day.
</span>        <span class="k">if</span> <span class="n">datetime_now</span><span class="p">.</span><span class="n">day</span> <span class="o">&gt;</span> <span class="n">self_ts</span><span class="p">.</span><span class="n">day</span><span class="p">:</span>
            <span class="k">return</span> <span class="bp">True</span>
        <span class="c1"># No updates on holidays or when generated after post_close.
</span>        <span class="k">if</span> <span class="n">self</span><span class="p">.</span><span class="n">is_holiday</span> <span class="ow">or</span> <span class="n">self_ts</span><span class="p">.</span><span class="nf">time</span><span class="p">()</span> <span class="o">&gt;=</span> <span class="nf">parse</span><span class="p">(</span><span class="n">self</span><span class="p">.</span><span class="n">post_close</span><span class="p">).</span><span class="nf">time</span><span class="p">():</span>
            <span class="k">return</span> <span class="bp">False</span>
        <span class="c1"># Compare current time to generated event times.
</span>        <span class="k">for</span> <span class="n">event</span> <span class="ow">in</span> <span class="p">[</span><span class="n">self</span><span class="p">.</span><span class="n">pre_open</span><span class="p">,</span><span class="n">self</span><span class="p">.</span><span class="n">reg_open</span><span class="p">,</span><span class="n">self</span><span class="p">.</span><span class="n">reg_close</span><span class="p">]:</span>
            <span class="k">if</span> <span class="n">datetime_now</span><span class="p">.</span><span class="nf">time</span><span class="p">()</span> <span class="o">&gt;</span> <span class="nf">parse</span><span class="p">(</span><span class="n">event</span><span class="p">).</span><span class="nf">time</span><span class="p">():</span>
                <span class="k">return</span> <span class="bp">True</span>
        <span class="c1"># Current time is before pre_open.
</span>        <span class="k">return</span> <span class="bp">False</span>

    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">tz</span><span class="p">(</span><span class="n">cls</span><span class="p">):</span>
        <span class="k">return</span> <span class="n">pytz</span><span class="p">.</span><span class="nf">timezone</span><span class="p">(</span><span class="sh">'</span><span class="s">US/Eastern</span><span class="sh">'</span><span class="p">)</span> <span class="c1"># Exchanges data is in eastern time.
</span>    
    <span class="nd">@classmethod</span>
    <span class="k">def</span> <span class="nf">apply_fix</span><span class="p">(</span><span class="n">cls</span><span class="p">,</span> <span class="n">value</span><span class="p">,</span> <span class="n">fix</span><span class="p">:</span> <span class="n">datetime</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">tuple</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">datetime</span><span class="p">]:</span>
        <span class="n">api</span><span class="p">.</span><span class="nf">validation_fail</span><span class="p">()</span>
        <span class="n">value</span> <span class="o">=</span> <span class="n">fix</span><span class="p">.</span><span class="nf">strftime</span><span class="p">(</span><span class="sh">'</span><span class="s">%c</span><span class="sh">'</span><span class="p">)</span>
        <span class="k">return</span> <span class="n">value</span><span class="p">,</span> <span class="n">fix</span>
    
    <span class="nd">@field_validator</span><span class="p">(</span><span class="sh">"</span><span class="s">last_close</span><span class="sh">"</span><span class="p">)</span>
    <span class="k">def</span> <span class="nf">valid_close</span><span class="p">(</span><span class="n">cls</span><span class="p">,</span> <span class="n">value</span><span class="p">):</span>
        <span class="n">date_gen</span> <span class="o">=</span> <span class="nf">parse</span><span class="p">(</span><span class="n">value</span><span class="p">)</span> <span class="c1"># Generated close is in eastern time and tzinfo naive.
</span>        <span class="n">date_now</span> <span class="o">=</span> <span class="nf">parse</span><span class="p">(</span><span class="n">datetime</span><span class="p">.</span><span class="nf">now</span><span class="p">(</span><span class="n">cls</span><span class="p">.</span><span class="nf">tz</span><span class="p">()).</span><span class="nf">strftime</span><span class="p">(</span><span class="sh">'</span><span class="s">%c</span><span class="sh">'</span><span class="p">))</span> <span class="c1"># Need now in same format as generated.
</span>        <span class="c1"># Soft-pass: when actual session is closed after post-market
</span>        <span class="k">if</span> <span class="n">date_now</span><span class="p">.</span><span class="n">day</span> <span class="o">==</span> <span class="n">date_gen</span><span class="p">.</span><span class="n">day</span><span class="o">+</span><span class="mi">1</span> <span class="ow">and</span> <span class="n">date_now</span><span class="p">.</span><span class="nf">weekday</span><span class="p">()</span> <span class="o">&lt;=</span> <span class="mi">4</span><span class="p">:</span>
            <span class="n">date_fix</span> <span class="o">=</span> <span class="n">date_gen</span><span class="p">.</span><span class="nf">replace</span><span class="p">(</span><span class="n">day</span><span class="o">=</span><span class="n">date_now</span><span class="p">.</span><span class="n">day</span><span class="p">)</span>
            <span class="k">if</span> <span class="n">date_fix</span><span class="p">.</span><span class="nf">timestamp</span><span class="p">()</span> <span class="o">&lt;</span> <span class="n">date_now</span><span class="p">.</span><span class="nf">timestamp</span><span class="p">():</span>
                <span class="n">value</span><span class="p">,</span> <span class="n">date_gen</span> <span class="o">=</span> <span class="n">cls</span><span class="p">.</span><span class="nf">apply_fix</span><span class="p">(</span><span class="n">value</span><span class="p">,</span> <span class="n">date_fix</span><span class="p">)</span> <span class="c1"># soft-pass: use today's close
</span>        <span class="c1"># Soft-pass: when actual session is open post-market
</span>        <span class="k">if</span> <span class="n">date_now</span><span class="p">.</span><span class="n">day</span> <span class="o">==</span> <span class="n">date_gen</span><span class="p">.</span><span class="n">day</span> <span class="ow">and</span> <span class="n">date_now</span><span class="p">.</span><span class="nf">timestamp</span><span class="p">()</span> <span class="o">&lt;</span> <span class="n">date_gen</span><span class="p">.</span><span class="nf">timestamp</span><span class="p">():</span>
            <span class="k">if</span> <span class="n">date_now</span><span class="p">.</span><span class="nf">weekday</span><span class="p">()</span> <span class="o">&gt;</span> <span class="mi">0</span><span class="p">:</span>
                <span class="n">date_fix</span> <span class="o">=</span> <span class="n">date_gen</span><span class="p">.</span><span class="nf">replace</span><span class="p">(</span><span class="n">day</span><span class="o">=</span><span class="n">date_now</span><span class="p">.</span><span class="n">day</span><span class="o">-</span><span class="mi">1</span><span class="p">)</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="n">date_fix</span> <span class="o">=</span> <span class="n">date_gen</span><span class="p">.</span><span class="nf">replace</span><span class="p">(</span><span class="n">day</span><span class="o">=</span><span class="n">date_now</span><span class="p">.</span><span class="n">day</span><span class="o">-</span><span class="mi">3</span><span class="p">)</span>
            <span class="k">if</span> <span class="n">date_now</span><span class="p">.</span><span class="nf">timestamp</span><span class="p">()</span> <span class="o">&gt;</span> <span class="n">date_fix</span><span class="p">.</span><span class="nf">timestamp</span><span class="p">():</span>
                <span class="n">value</span><span class="p">,</span> <span class="n">date_gen</span> <span class="o">=</span> <span class="n">cls</span><span class="p">.</span><span class="nf">apply_fix</span><span class="p">(</span><span class="n">value</span><span class="p">,</span> <span class="n">date_fix</span><span class="p">)</span> <span class="c1"># soft-pass: use previous close
</span>        <span class="k">if</span> <span class="n">date_now</span><span class="p">.</span><span class="nf">weekday</span><span class="p">()</span> <span class="o">==</span> <span class="mi">0</span> <span class="ow">or</span> <span class="n">date_now</span><span class="p">.</span><span class="nf">weekday</span><span class="p">()</span> <span class="o">==</span> <span class="mi">1</span> <span class="ow">and</span> <span class="n">date_gen</span><span class="p">.</span><span class="nf">weekday</span><span class="p">()</span> <span class="o">&lt;=</span> <span class="mi">4</span><span class="p">:</span> <span class="c1"># 0=monday, 4=friday
</span>            <span class="k">return</span> <span class="n">value</span> <span class="c1"># pass: generated thurs/friday on a monday/tues
</span>        <span class="k">elif</span> <span class="n">date_now</span><span class="p">.</span><span class="nf">weekday</span><span class="p">()</span> <span class="o">&gt;</span> <span class="mi">0</span> <span class="ow">and</span> <span class="n">date_now</span><span class="p">.</span><span class="nf">weekday</span><span class="p">()</span> <span class="o">&lt;=</span> <span class="mi">4</span> <span class="ow">and</span> <span class="n">date_gen</span><span class="p">.</span><span class="nf">weekday</span><span class="p">()</span> <span class="o">&lt;=</span> <span class="n">date_now</span><span class="p">.</span><span class="nf">weekday</span><span class="p">()</span><span class="o">-</span><span class="mi">1</span><span class="p">:</span>
            <span class="k">return</span> <span class="n">value</span> <span class="c1"># pass: generated yesterday/prior on a tues-fri
</span>        <span class="k">elif</span> <span class="n">date_now</span><span class="p">.</span><span class="nf">weekday</span><span class="p">()</span> <span class="o">&gt;</span> <span class="mi">4</span> <span class="ow">and</span> <span class="n">date_gen</span><span class="p">.</span><span class="nf">weekday</span><span class="p">()</span> <span class="o">&lt;=</span> <span class="mi">4</span><span class="p">:</span>
            <span class="k">return</span> <span class="n">value</span> <span class="c1"># pass: generated thurs/friday on a weekend
</span>        <span class="k">elif</span> <span class="n">date_now</span><span class="p">.</span><span class="n">day</span> <span class="o">==</span> <span class="n">date_gen</span><span class="p">.</span><span class="n">day</span> <span class="ow">and</span> <span class="n">date_now</span><span class="p">.</span><span class="nf">timestamp</span><span class="p">()</span> <span class="o">&gt;</span> <span class="n">date_gen</span><span class="p">.</span><span class="nf">timestamp</span><span class="p">():</span>
            <span class="k">return</span> <span class="n">value</span> <span class="c1"># pass: generated today after closed
</span>        <span class="k">elif</span> <span class="n">date_now</span><span class="p">.</span><span class="nf">timestamp</span><span class="p">()</span> <span class="o">&lt;</span> <span class="n">date_gen</span><span class="p">.</span><span class="nf">timestamp</span><span class="p">():</span>
            <span class="k">raise</span> <span class="nc">ValueError</span><span class="p">(</span><span class="sh">"</span><span class="s">last close cannot be a future value</span><span class="sh">"</span><span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="k">raise</span> <span class="nc">ValueError</span><span class="p">(</span><span class="sh">"</span><span class="s">generated invalid last close</span><span class="sh">"</span><span class="p">)</span>
        <span class="n">api</span><span class="p">.</span><span class="nf">validation_fail</span><span class="p">()</span>

<span class="k">class</span> <span class="nc">VectorStoreResult</span><span class="p">(</span><span class="n">BaseModel</span><span class="p">):</span>
    <span class="n">docs</span><span class="p">:</span> <span class="nb">str</span>
    <span class="n">dist</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">float</span><span class="p">]</span> <span class="c1"># requires query
</span>    <span class="n">meta</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">dict</span><span class="p">]</span>  <span class="c1"># requires get or query
</span>    <span class="n">store_id</span><span class="p">:</span> <span class="nb">str</span>

<span class="k">class</span> <span class="nc">Aggregate</span><span class="p">(</span><span class="n">RestResultPoly</span><span class="p">):</span>
    <span class="n">symbol</span><span class="p">:</span> <span class="nb">str</span>
    <span class="nb">open</span><span class="p">:</span> <span class="nb">float</span>
    <span class="n">high</span><span class="p">:</span> <span class="nb">float</span>
    <span class="n">low</span><span class="p">:</span> <span class="nb">float</span>
    <span class="n">close</span><span class="p">:</span> <span class="nb">float</span>
    <span class="n">volume</span><span class="p">:</span> <span class="nb">int</span>
    <span class="n">otc</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">bool</span><span class="p">]</span> <span class="o">=</span> <span class="bp">None</span>
    <span class="n">preMarket</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">float</span><span class="p">]</span> <span class="o">=</span> <span class="bp">None</span>
    <span class="n">afterHours</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">float</span><span class="p">]</span> <span class="o">=</span> <span class="bp">None</span>

<span class="k">class</span> <span class="nc">DailyCandle</span><span class="p">(</span><span class="n">Aggregate</span><span class="p">):</span>
    <span class="n">from_date</span><span class="p">:</span> <span class="nb">str</span>

<span class="k">class</span> <span class="nc">AggregateWindow</span><span class="p">(</span><span class="n">BaseModel</span><span class="p">):</span>
    <span class="n">o</span><span class="p">:</span> <span class="nb">float</span>
    <span class="n">h</span><span class="p">:</span> <span class="nb">float</span>
    <span class="n">l</span><span class="p">:</span> <span class="nb">float</span>
    <span class="n">c</span><span class="p">:</span> <span class="nb">float</span>
    <span class="n">v</span><span class="p">:</span> <span class="nb">int</span> <span class="c1"># traded volume
</span>    <span class="n">n</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="bp">None</span> <span class="c1"># transaction count
</span>    <span class="n">vw</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">float</span><span class="p">]</span> <span class="o">=</span> <span class="bp">None</span> <span class="c1"># volume weighted average price
</span>    <span class="n">otc</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">bool</span><span class="p">]</span> <span class="o">=</span> <span class="bp">None</span>
    <span class="n">t</span><span class="p">:</span> <span class="nb">int</span>

    <span class="nd">@field_validator</span><span class="p">(</span><span class="sh">"</span><span class="s">t</span><span class="sh">"</span><span class="p">)</span>
    <span class="k">def</span> <span class="nf">valid_t</span><span class="p">(</span><span class="n">cls</span><span class="p">,</span> <span class="n">value</span><span class="p">):</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="n">value</span> <span class="o">&gt;</span> <span class="mi">0</span><span class="p">:</span>
            <span class="k">raise</span> <span class="nc">ValueError</span><span class="p">(</span><span class="sh">"</span><span class="s">invalid timestamp</span><span class="sh">"</span><span class="p">)</span>
        <span class="k">if</span> <span class="nf">len</span><span class="p">(</span><span class="nf">str</span><span class="p">(</span><span class="n">value</span><span class="p">))</span> <span class="o">==</span> <span class="mi">13</span><span class="p">:</span>
            <span class="k">return</span> <span class="nf">int</span><span class="p">(</span><span class="n">value</span><span class="o">/</span><span class="mi">1000</span><span class="p">)</span>
        <span class="k">return</span> <span class="n">value</span>

<span class="k">class</span> <span class="nc">CustomCandle</span><span class="p">(</span><span class="n">RestResultPoly</span><span class="p">):</span> 
    <span class="n">ticker</span><span class="p">:</span> <span class="nb">str</span>
    <span class="n">adjusted</span><span class="p">:</span> <span class="nb">bool</span>
    <span class="n">queryCount</span><span class="p">:</span> <span class="nb">int</span>
    <span class="n">resultsCount</span><span class="p">:</span> <span class="nb">int</span>
    <span class="n">results</span><span class="p">:</span> <span class="nb">list</span><span class="p">[</span><span class="n">AggregateWindow</span><span class="p">]</span>

    <span class="k">def</span> <span class="nf">model_post_init</span><span class="p">(</span><span class="n">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="bp">None</span><span class="p">:</span>
        <span class="n">self</span><span class="p">.</span><span class="n">count</span> <span class="o">=</span> <span class="nf">len</span><span class="p">(</span><span class="n">self</span><span class="p">.</span><span class="n">results</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">get</span><span class="p">(</span><span class="n">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">list</span><span class="p">[</span><span class="n">AggregateWindow</span><span class="p">]:</span>
        <span class="k">return</span> <span class="n">self</span><span class="p">.</span><span class="n">results</span>
    
<span class="k">class</span> <span class="nc">MarketStatus</span><span class="p">(</span><span class="n">BaseModel</span><span class="p">):</span>
    <span class="n">exchange</span><span class="p">:</span> <span class="nb">str</span>
    <span class="n">holiday</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="bp">None</span>
    <span class="n">isOpen</span><span class="p">:</span> <span class="nb">bool</span>
    <span class="n">session</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">MarketSession</span><span class="p">]</span> <span class="o">=</span> <span class="bp">None</span>
    <span class="n">t</span><span class="p">:</span> <span class="nb">int</span>
    <span class="n">timezone</span><span class="p">:</span> <span class="nb">str</span>

    <span class="k">def</span> <span class="nf">model_post_init</span><span class="p">(</span><span class="n">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="bp">None</span><span class="p">:</span>
        <span class="k">if</span> <span class="n">self</span><span class="p">.</span><span class="n">session</span> <span class="ow">is</span> <span class="bp">None</span><span class="p">:</span>
            <span class="n">self</span><span class="p">.</span><span class="n">session</span> <span class="o">=</span> <span class="n">MarketSession</span><span class="p">.</span><span class="n">CLOSED</span>
        <span class="k">if</span> <span class="n">self</span><span class="p">.</span><span class="n">holiday</span> <span class="ow">is</span> <span class="bp">None</span><span class="p">:</span>
            <span class="n">self</span><span class="p">.</span><span class="n">holiday</span> <span class="o">=</span> <span class="n">MarketSession</span><span class="p">.</span><span class="n">NA</span><span class="p">.</span><span class="n">value</span>

<span class="k">class</span> <span class="nc">MarketStatusResult</span><span class="p">(</span><span class="n">BaseModel</span><span class="p">):</span>
    <span class="n">results</span><span class="p">:</span> <span class="n">MarketStatus</span>

    <span class="k">def</span> <span class="nf">get</span><span class="p">(</span><span class="n">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">MarketStatus</span><span class="p">:</span>
        <span class="k">return</span> <span class="n">self</span><span class="p">.</span><span class="n">results</span>

<span class="k">class</span> <span class="nc">Symbol</span><span class="p">(</span><span class="n">BaseModel</span><span class="p">):</span>
    <span class="n">description</span><span class="p">:</span> <span class="nb">str</span>
    <span class="n">displaySymbol</span><span class="p">:</span> <span class="nb">str</span>
    <span class="n">symbol</span><span class="p">:</span> <span class="nb">str</span>
    <span class="nb">type</span><span class="p">:</span> <span class="n">SymbolType</span>

<span class="k">class</span> <span class="nc">SymbolResult</span><span class="p">(</span><span class="n">BaseModel</span><span class="p">):</span>
    <span class="n">count</span><span class="p">:</span> <span class="nb">int</span>
    <span class="n">result</span><span class="p">:</span> <span class="nb">list</span><span class="p">[</span><span class="n">Symbol</span><span class="p">]</span>

    <span class="k">def</span> <span class="nf">model_post_init</span><span class="p">(</span><span class="n">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="bp">None</span><span class="p">:</span>
        <span class="n">self</span><span class="p">.</span><span class="n">count</span> <span class="o">=</span> <span class="nf">len</span><span class="p">(</span><span class="n">self</span><span class="p">.</span><span class="n">result</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">get</span><span class="p">(</span><span class="n">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">list</span><span class="p">[</span><span class="n">Symbol</span><span class="p">]:</span>
        <span class="k">return</span> <span class="n">self</span><span class="p">.</span><span class="n">result</span>

<span class="k">class</span> <span class="nc">Quote</span><span class="p">(</span><span class="n">BaseModel</span><span class="p">):</span>
    <span class="n">c</span><span class="p">:</span> <span class="nb">float</span>
    <span class="n">d</span><span class="p">:</span> <span class="nb">float</span>
    <span class="n">dp</span><span class="p">:</span> <span class="nb">float</span>
    <span class="n">h</span><span class="p">:</span> <span class="nb">float</span>
    <span class="n">l</span><span class="p">:</span> <span class="nb">float</span>
    <span class="n">o</span><span class="p">:</span> <span class="nb">float</span>
    <span class="n">pc</span><span class="p">:</span> <span class="nb">float</span>
    <span class="n">t</span><span class="p">:</span> <span class="nb">int</span>

    <span class="nd">@field_validator</span><span class="p">(</span><span class="sh">"</span><span class="s">t</span><span class="sh">"</span><span class="p">)</span>
    <span class="k">def</span> <span class="nf">valid_t</span><span class="p">(</span><span class="n">cls</span><span class="p">,</span> <span class="n">value</span><span class="p">):</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="n">value</span> <span class="o">&gt;</span> <span class="mi">0</span><span class="p">:</span>
            <span class="k">raise</span> <span class="nc">ValueError</span><span class="p">(</span><span class="sh">"</span><span class="s">invalid timestamp</span><span class="sh">"</span><span class="p">)</span>
        <span class="k">return</span> <span class="n">value</span>

<span class="k">class</span> <span class="nc">PeersResult</span><span class="p">(</span><span class="n">BaseModel</span><span class="p">):</span>
    <span class="n">results</span><span class="p">:</span> <span class="nb">list</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span>
    <span class="n">count</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="bp">None</span>

    <span class="k">def</span> <span class="nf">model_post_init</span><span class="p">(</span><span class="n">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="bp">None</span><span class="p">:</span>
        <span class="n">self</span><span class="p">.</span><span class="n">count</span> <span class="o">=</span> <span class="nf">len</span><span class="p">(</span><span class="n">self</span><span class="p">.</span><span class="n">results</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">get</span><span class="p">(</span><span class="n">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">list</span><span class="p">[</span><span class="nb">str</span><span class="p">]:</span>
        <span class="k">return</span> <span class="n">self</span><span class="p">.</span><span class="n">results</span>

<span class="k">class</span> <span class="nc">BasicFinancials</span><span class="p">(</span><span class="n">BaseModel</span><span class="p">):</span>
    <span class="n">metric</span><span class="p">:</span> <span class="nb">dict</span>
    <span class="n">metricType</span><span class="p">:</span> <span class="nb">str</span>
    <span class="n">series</span><span class="p">:</span> <span class="nb">dict</span>
    <span class="n">symbol</span><span class="p">:</span> <span class="nb">str</span>

<span class="k">class</span> <span class="nc">Insight</span><span class="p">(</span><span class="n">BaseModel</span><span class="p">):</span>
    <span class="n">sentiment</span><span class="p">:</span> <span class="n">Sentiment</span><span class="o">|</span><span class="n">MarketCondition</span>
    <span class="n">sentiment_reasoning</span><span class="p">:</span> <span class="nb">str</span>
    <span class="n">ticker</span><span class="p">:</span> <span class="nb">str</span>

<span class="k">class</span> <span class="nc">Publisher</span><span class="p">(</span><span class="n">BaseModel</span><span class="p">):</span>
    <span class="n">favicon_url</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span>
    <span class="n">homepage_url</span><span class="p">:</span> <span class="nb">str</span>
    <span class="n">logo_url</span><span class="p">:</span> <span class="nb">str</span>
    <span class="n">name</span><span class="p">:</span> <span class="nb">str</span>

<span class="k">class</span> <span class="nc">NewsSummary</span><span class="p">(</span><span class="n">BaseModel</span><span class="p">):</span>
    <span class="n">title</span><span class="p">:</span> <span class="nb">str</span>
    <span class="n">summary</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span>
    <span class="n">insights</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">list</span><span class="p">[</span><span class="n">Insight</span><span class="p">]]</span>
    <span class="n">published_utc</span><span class="p">:</span> <span class="nb">str</span>

<span class="k">class</span> <span class="nc">NewsTypePoly</span><span class="p">(</span><span class="n">BaseModel</span><span class="p">):</span>
    <span class="n">amp_url</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="bp">None</span>
    <span class="n">article_url</span><span class="p">:</span> <span class="nb">str</span>
    <span class="n">title</span><span class="p">:</span> <span class="nb">str</span>
    <span class="n">author</span><span class="p">:</span> <span class="nb">str</span>
    <span class="n">description</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="bp">None</span>
    <span class="nb">id</span><span class="p">:</span> <span class="nb">str</span>
    <span class="n">image_url</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="bp">None</span>
    <span class="n">insights</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">list</span><span class="p">[</span><span class="n">Insight</span><span class="p">]]</span> <span class="o">=</span> <span class="bp">None</span>
    <span class="n">keywords</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">list</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="bp">None</span>
    <span class="n">published_utc</span><span class="p">:</span> <span class="nb">str</span>
    <span class="n">publisher</span><span class="p">:</span> <span class="n">Publisher</span>
    <span class="n">tickers</span><span class="p">:</span> <span class="nb">list</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span>

    <span class="k">def</span> <span class="nf">summary</span><span class="p">(</span><span class="n">self</span><span class="p">):</span>
        <span class="k">return</span> <span class="nc">NewsSummary</span><span class="p">(</span><span class="n">title</span><span class="o">=</span><span class="n">self</span><span class="p">.</span><span class="n">title</span><span class="p">,</span>
                           <span class="n">summary</span><span class="o">=</span><span class="n">self</span><span class="p">.</span><span class="n">description</span><span class="p">,</span>
                           <span class="n">insights</span><span class="o">=</span><span class="n">self</span><span class="p">.</span><span class="n">insights</span><span class="p">,</span>
                           <span class="n">published_utc</span><span class="o">=</span><span class="n">self</span><span class="p">.</span><span class="n">published_utc</span><span class="p">)</span>

<span class="k">class</span> <span class="nc">NewsResultPoly</span><span class="p">(</span><span class="n">RestResultPoly</span><span class="p">):</span>
    <span class="n">results</span><span class="p">:</span> <span class="nb">list</span><span class="p">[</span><span class="n">NewsTypePoly</span><span class="p">]</span>

    <span class="k">def</span> <span class="nf">model_post_init</span><span class="p">(</span><span class="n">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="bp">None</span><span class="p">:</span>
        <span class="n">self</span><span class="p">.</span><span class="n">count</span> <span class="o">=</span> <span class="nf">len</span><span class="p">(</span><span class="n">self</span><span class="p">.</span><span class="n">results</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">get</span><span class="p">(</span><span class="n">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">list</span><span class="p">[</span><span class="n">NewsTypePoly</span><span class="p">]:</span>
        <span class="k">return</span> <span class="n">self</span><span class="p">.</span><span class="n">results</span>

<span class="k">class</span> <span class="nc">NewsTypeFinn</span><span class="p">(</span><span class="n">BaseModel</span><span class="p">):</span>
    <span class="n">category</span><span class="p">:</span> <span class="nb">str</span>
    <span class="n">datetime</span><span class="p">:</span> <span class="nb">int</span>
    <span class="n">headline</span><span class="p">:</span> <span class="nb">str</span>
    <span class="nb">id</span><span class="p">:</span> <span class="nb">int</span>
    <span class="n">image</span><span class="p">:</span> <span class="nb">str</span>
    <span class="n">related</span><span class="p">:</span> <span class="nb">str</span> <span class="c1"># symbol
</span>    <span class="n">source</span><span class="p">:</span> <span class="nb">str</span>
    <span class="n">summary</span><span class="p">:</span> <span class="nb">str</span>
    <span class="n">url</span><span class="p">:</span> <span class="nb">str</span>

    <span class="k">def</span> <span class="nf">summary</span><span class="p">(</span><span class="n">self</span><span class="p">):</span>
        <span class="k">return</span> <span class="nc">NewsSummary</span><span class="p">(</span><span class="n">title</span><span class="o">=</span><span class="n">self</span><span class="p">.</span><span class="n">headline</span><span class="p">,</span>
                           <span class="n">summary</span><span class="o">=</span><span class="n">self</span><span class="p">.</span><span class="n">summary</span><span class="p">,</span>
                           <span class="n">insights</span><span class="o">=</span><span class="bp">None</span><span class="p">,</span>
                           <span class="n">published_utc</span><span class="o">=</span><span class="n">self</span><span class="p">.</span><span class="n">datetime</span><span class="p">)</span>

<span class="k">class</span> <span class="nc">NewsResultFinn</span><span class="p">(</span><span class="n">BaseModel</span><span class="p">):</span>
    <span class="n">results</span><span class="p">:</span> <span class="nb">list</span><span class="p">[</span><span class="n">NewsTypeFinn</span><span class="p">]</span>
    <span class="n">count</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="bp">None</span>

    <span class="k">def</span> <span class="nf">model_post_init</span><span class="p">(</span><span class="n">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="bp">None</span><span class="p">:</span>
        <span class="n">self</span><span class="p">.</span><span class="n">count</span> <span class="o">=</span> <span class="nf">len</span><span class="p">(</span><span class="n">self</span><span class="p">.</span><span class="n">results</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">get</span><span class="p">(</span><span class="n">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">list</span><span class="p">[</span><span class="n">NewsTypeFinn</span><span class="p">]:</span>
        <span class="k">return</span> <span class="n">self</span><span class="p">.</span><span class="n">results</span>

<span class="k">class</span> <span class="nc">NewsTypeGenerated</span><span class="p">(</span><span class="n">BaseModel</span><span class="p">):</span>
    <span class="n">title</span><span class="p">:</span> <span class="nb">str</span>
    <span class="n">summary</span><span class="p">:</span> <span class="nb">str</span>
    <span class="n">insights</span><span class="p">:</span> <span class="nb">list</span><span class="p">[</span><span class="n">Insight</span><span class="p">]</span>
    <span class="n">keywords</span><span class="p">:</span> <span class="nb">list</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span>
    <span class="n">source</span><span class="p">:</span> <span class="n">Publisher</span>
    <span class="n">published_utc</span><span class="p">:</span> <span class="nb">str</span>
    <span class="n">tickers</span><span class="p">:</span> <span class="nb">list</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span>
    <span class="n">url</span><span class="p">:</span> <span class="nb">str</span>

    <span class="k">def</span> <span class="nf">summary</span><span class="p">(</span><span class="n">self</span><span class="p">):</span>
        <span class="k">return</span> <span class="nc">NewsSummary</span><span class="p">(</span><span class="n">title</span><span class="o">=</span><span class="n">self</span><span class="p">.</span><span class="n">title</span><span class="p">,</span>
                           <span class="n">summary</span><span class="o">=</span><span class="n">self</span><span class="p">.</span><span class="n">summary</span><span class="p">,</span>
                           <span class="n">insights</span><span class="o">=</span><span class="n">self</span><span class="p">.</span><span class="n">insights</span><span class="p">,</span>
                           <span class="n">published_utc</span><span class="o">=</span><span class="n">self</span><span class="p">.</span><span class="n">published_utc</span><span class="p">)</span>

<span class="k">class</span> <span class="nc">TickerOverview</span><span class="p">(</span><span class="n">BaseModel</span><span class="p">):</span>
    <span class="n">ticker</span><span class="p">:</span> <span class="nb">str</span>
    <span class="n">name</span><span class="p">:</span> <span class="nb">str</span>
    <span class="n">market</span><span class="p">:</span> <span class="n">AssetClass</span>
    <span class="n">locale</span><span class="p">:</span> <span class="n">Locale</span>
    <span class="n">primary_exchange</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="bp">None</span>
    <span class="n">active</span><span class="p">:</span> <span class="nb">bool</span>
    <span class="n">currency_name</span><span class="p">:</span> <span class="nb">str</span>
    <span class="n">cik</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="bp">None</span>
    <span class="n">composite_figi</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="bp">None</span>
    <span class="n">share_class_figi</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="bp">None</span>
    <span class="n">market_cap</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="o">|</span><span class="nb">float</span><span class="p">]</span> <span class="o">=</span> <span class="bp">None</span>
    <span class="n">phone_number</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="bp">None</span>
    <span class="n">address</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">dict</span><span class="p">]</span> <span class="o">=</span> <span class="bp">None</span>
    <span class="n">description</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="bp">None</span>
    <span class="n">sic_code</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="bp">None</span>
    <span class="n">sic_description</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="bp">None</span>
    <span class="n">ticker_root</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="bp">None</span>
    <span class="n">homepage_url</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="bp">None</span>
    <span class="n">total_employees</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="bp">None</span>
    <span class="n">list_date</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="bp">None</span>
    <span class="n">branding</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">dict</span><span class="p">]</span> <span class="o">=</span> <span class="bp">None</span>
    <span class="n">share_class_shares_outstanding</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="bp">None</span>
    <span class="n">weighted_shares_outstanding</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="bp">None</span>
    <span class="n">round_lot</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="bp">None</span>

<span class="k">class</span> <span class="nc">OverviewResult</span><span class="p">(</span><span class="n">RestResultPoly</span><span class="p">):</span>
    <span class="n">results</span><span class="p">:</span> <span class="n">TickerOverview</span>

    <span class="k">def</span> <span class="nf">get</span><span class="p">(</span><span class="n">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">TickerOverview</span><span class="p">:</span>
        <span class="k">return</span> <span class="n">self</span><span class="p">.</span><span class="n">results</span>

<span class="k">class</span> <span class="nc">RecommendationTrend</span><span class="p">(</span><span class="n">BaseModel</span><span class="p">):</span>
    <span class="n">buy</span><span class="p">:</span> <span class="nb">int</span>
    <span class="n">hold</span><span class="p">:</span> <span class="nb">int</span>
    <span class="n">period</span><span class="p">:</span> <span class="nb">str</span>
    <span class="n">sell</span><span class="p">:</span> <span class="nb">int</span>
    <span class="n">strongBuy</span><span class="p">:</span> <span class="nb">int</span>
    <span class="n">strongSell</span><span class="p">:</span> <span class="nb">int</span>
    <span class="n">symbol</span><span class="p">:</span> <span class="nb">str</span>

<span class="k">class</span> <span class="nc">TrendsResult</span><span class="p">(</span><span class="n">BaseModel</span><span class="p">):</span>
    <span class="n">results</span><span class="p">:</span> <span class="nb">list</span><span class="p">[</span><span class="n">RecommendationTrend</span><span class="p">]</span>
    <span class="n">count</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">int</span><span class="p">]</span> <span class="o">=</span> <span class="bp">None</span>

    <span class="k">def</span> <span class="nf">model_post_init</span><span class="p">(</span><span class="n">self</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="bp">None</span><span class="p">:</span>
        <span class="n">self</span><span class="p">.</span><span class="n">count</span> <span class="o">=</span> <span class="nf">len</span><span class="p">(</span><span class="n">self</span><span class="p">.</span><span class="n">results</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">get</span><span class="p">(</span><span class="n">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">list</span><span class="p">[</span><span class="n">RecommendationTrend</span><span class="p">]:</span>
        <span class="k">return</span> <span class="n">self</span><span class="p">.</span><span class="n">results</span>
</code></pre></div></div>

<h3 id="contents-memory">Contents Memory</h3>

<div class="language-python highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="c1"># A contents-memory object.
</span><span class="k">class</span> <span class="nc">Memory</span><span class="p">:</span>
    <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="n">self</span><span class="p">):</span>
        <span class="n">self</span><span class="p">.</span><span class="n">system</span> <span class="o">=</span> <span class="sa">f</span><span class="sh">"""</span><span class="s">Give a concise, and detailed summary. Use information that you learn from the API responses.
        Use your tools and function calls according to the rules. Convert any all-upper case identifiers
        to proper case in your response. Convert any abbreviated or shortened identifiers to their full forms.
        Convert timestamps according to the rules before including them. Think step by step.
        </span><span class="sh">"""</span>
        <span class="n">self</span><span class="p">.</span><span class="n">revery</span> <span class="o">=</span> <span class="p">{}</span>
        <span class="n">self</span><span class="p">.</span><span class="n">contents</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="n">self</span><span class="p">.</span><span class="n">prompt</span> <span class="o">=</span> <span class="bp">None</span>
        <span class="n">self</span><span class="p">.</span><span class="n">summary</span> <span class="o">=</span> <span class="bp">None</span>
        <span class="n">self</span><span class="p">.</span><span class="n">response</span> <span class="o">=</span> <span class="bp">None</span>
    
    <span class="k">def</span> <span class="nf">set_prompt</span><span class="p">(</span><span class="n">self</span><span class="p">,</span> <span class="n">prompt</span><span class="p">):</span>
        <span class="n">self</span><span class="p">.</span><span class="n">prompt</span> <span class="o">=</span> <span class="sa">f</span><span class="sh">"""</span><span class="s">
        The current date and time is: </span><span class="si">{</span><span class="n">datetime</span><span class="p">.</span><span class="nf">now</span><span class="p">(</span><span class="n">GeneratedEvent</span><span class="p">.</span><span class="nf">tz</span><span class="p">()).</span><span class="nf">strftime</span><span class="p">(</span><span class="sh">'</span><span class="s">%c</span><span class="sh">'</span><span class="p">)</span><span class="si">}</span><span class="s">
        
        </span><span class="si">{</span><span class="n">prompt</span><span class="si">}</span><span class="s">
        </span><span class="sh">"""</span>
        <span class="n">self</span><span class="p">.</span><span class="n">contents</span> <span class="o">=</span> <span class="p">[</span><span class="n">types</span><span class="p">.</span><span class="nc">Content</span><span class="p">(</span><span class="n">role</span><span class="o">=</span><span class="sh">"</span><span class="s">user</span><span class="sh">"</span><span class="p">,</span> <span class="n">parts</span><span class="o">=</span><span class="p">[</span><span class="n">types</span><span class="p">.</span><span class="nc">Part</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">self</span><span class="p">.</span><span class="n">prompt</span><span class="p">)])]</span>

    <span class="k">def</span> <span class="nf">set_reason</span><span class="p">(</span><span class="n">self</span><span class="p">,</span> <span class="n">step</span><span class="p">):</span>
        <span class="c1"># Append the model's reasoning part.
</span>        <span class="n">self</span><span class="p">.</span><span class="n">contents</span><span class="p">.</span><span class="nf">append</span><span class="p">(</span><span class="n">types</span><span class="p">.</span><span class="nc">Content</span><span class="p">(</span><span class="n">role</span><span class="o">=</span><span class="sh">"</span><span class="s">model</span><span class="sh">"</span><span class="p">,</span> <span class="n">parts</span><span class="o">=</span><span class="p">[</span><span class="n">types</span><span class="p">.</span><span class="nc">Part</span><span class="p">(</span><span class="n">thought</span><span class="o">=</span><span class="bp">True</span><span class="p">,</span><span class="n">text</span><span class="o">=</span><span class="n">step</span><span class="p">)]))</span>

    <span class="k">def</span> <span class="nf">append_code</span><span class="p">(</span><span class="n">self</span><span class="p">,</span> <span class="n">prompt</span><span class="p">,</span> <span class="n">code_response_parts</span><span class="p">):</span>
        <span class="n">subroutine_content</span> <span class="o">=</span> <span class="p">[</span><span class="n">types</span><span class="p">.</span><span class="nc">Content</span><span class="p">(</span><span class="n">role</span><span class="o">=</span><span class="sh">"</span><span class="s">user</span><span class="sh">"</span><span class="p">,</span> <span class="n">parts</span><span class="o">=</span><span class="p">[</span><span class="n">types</span><span class="p">.</span><span class="nc">Part</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">prompt</span><span class="p">)]),</span>
                              <span class="n">types</span><span class="p">.</span><span class="nc">Content</span><span class="p">(</span><span class="n">role</span><span class="o">=</span><span class="sh">"</span><span class="s">model</span><span class="sh">"</span><span class="p">,</span> <span class="n">parts</span><span class="o">=</span><span class="n">code_response_parts</span><span class="p">)]</span>
        <span class="c1"># Append the model's generated code and execution result.
</span>        <span class="n">self</span><span class="p">.</span><span class="n">revery</span><span class="p">[</span><span class="n">datetime</span><span class="p">.</span><span class="nf">now</span><span class="p">(</span><span class="n">GeneratedEvent</span><span class="p">.</span><span class="nf">tz</span><span class="p">()).</span><span class="nf">strftime</span><span class="p">(</span><span class="sh">'</span><span class="s">%c</span><span class="sh">'</span><span class="p">)]</span> <span class="o">=</span> <span class="p">{</span> 
            <span class="sh">"</span><span class="s">contents</span><span class="sh">"</span><span class="p">:</span> <span class="n">subroutine_content</span>
        <span class="p">}</span>

    <span class="k">def</span> <span class="nf">update_contents</span><span class="p">(</span><span class="n">self</span><span class="p">,</span> <span class="n">function_call</span><span class="p">,</span> <span class="n">api_response_part</span><span class="p">):</span>
        <span class="c1"># Append the model's function call part.
</span>        <span class="n">self</span><span class="p">.</span><span class="n">contents</span><span class="p">.</span><span class="nf">append</span><span class="p">(</span><span class="n">types</span><span class="p">.</span><span class="nc">Content</span><span class="p">(</span><span class="n">role</span><span class="o">=</span><span class="sh">"</span><span class="s">model</span><span class="sh">"</span><span class="p">,</span> <span class="n">parts</span><span class="o">=</span><span class="p">[</span><span class="n">types</span><span class="p">.</span><span class="nc">Part</span><span class="p">(</span><span class="n">function_call</span><span class="o">=</span><span class="n">function_call</span><span class="p">)]))</span> 
        <span class="c1"># Append the api response part.
</span>        <span class="n">self</span><span class="p">.</span><span class="n">contents</span><span class="p">.</span><span class="nf">append</span><span class="p">(</span><span class="n">types</span><span class="p">.</span><span class="nc">Content</span><span class="p">(</span><span class="n">role</span><span class="o">=</span><span class="sh">"</span><span class="s">user</span><span class="sh">"</span><span class="p">,</span> <span class="n">parts</span><span class="o">=</span><span class="p">[</span><span class="n">api_response_part</span><span class="p">]))</span>

    <span class="k">def</span> <span class="nf">set_summary</span><span class="p">(</span><span class="n">self</span><span class="p">,</span> <span class="n">summary</span><span class="p">):</span>
        <span class="n">self</span><span class="p">.</span><span class="n">summary</span> <span class="o">=</span> <span class="n">summary</span>
        <span class="n">self</span><span class="p">.</span><span class="n">contents</span><span class="p">.</span><span class="nf">append</span><span class="p">(</span><span class="n">types</span><span class="p">.</span><span class="nc">Content</span><span class="p">(</span><span class="n">role</span><span class="o">=</span><span class="sh">"</span><span class="s">model</span><span class="sh">"</span><span class="p">,</span> <span class="n">parts</span><span class="o">=</span><span class="p">[</span><span class="n">types</span><span class="p">.</span><span class="nc">Part</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">summary</span><span class="p">)]))</span>
        <span class="n">self</span><span class="p">.</span><span class="n">revery</span><span class="p">[</span><span class="n">datetime</span><span class="p">.</span><span class="nf">now</span><span class="p">(</span><span class="n">GeneratedEvent</span><span class="p">.</span><span class="nf">tz</span><span class="p">()).</span><span class="nf">strftime</span><span class="p">(</span><span class="sh">'</span><span class="s">%c</span><span class="sh">'</span><span class="p">)]</span> <span class="o">=</span> <span class="p">{</span>
            <span class="sh">"</span><span class="s">prompt</span><span class="sh">"</span><span class="p">:</span> <span class="n">self</span><span class="p">.</span><span class="n">prompt</span><span class="p">,</span> 
            <span class="sh">"</span><span class="s">summary</span><span class="sh">"</span><span class="p">:</span> <span class="n">self</span><span class="p">.</span><span class="n">summary</span><span class="p">,</span> 
            <span class="sh">"</span><span class="s">contents</span><span class="sh">"</span><span class="p">:</span> <span class="n">self</span><span class="p">.</span><span class="n">contents</span>
        <span class="p">}</span>
        <span class="n">self</span><span class="p">.</span><span class="n">contents</span> <span class="o">=</span> <span class="p">[]</span>

<span class="n">memory</span> <span class="o">=</span> <span class="nc">Memory</span><span class="p">()</span>
</code></pre></div></div>

<h3 id="retrieval-augmented-generation">Retrieval-Augmented Generation</h3>

<div class="language-python highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="c1"># Define tool: retrieval-augmented generation.
# - using Chroma and text-embedding-004 for storage and retrieval
# - using gemini-2.0-flash for augmented generation
</span><span class="k">class</span> <span class="nc">RetrievalAugmentedGenerator</span><span class="p">:</span>
    <span class="n">chroma_client</span> <span class="o">=</span> <span class="n">chromadb</span><span class="p">.</span><span class="nc">PersistentClient</span><span class="p">(</span><span class="n">path</span><span class="o">=</span><span class="sh">"</span><span class="s">vector_db</span><span class="sh">"</span><span class="p">)</span>
    <span class="n">config_temp</span> <span class="o">=</span> <span class="n">types</span><span class="p">.</span><span class="nc">GenerateContentConfig</span><span class="p">(</span><span class="n">temperature</span><span class="o">=</span><span class="mf">0.0</span><span class="p">)</span>
    <span class="n">exchange_codes</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">dict</span><span class="p">]</span> <span class="o">=</span> <span class="bp">None</span>
    <span class="n">exchange_lists</span><span class="p">:</span> <span class="nb">dict</span> <span class="o">=</span> <span class="p">{}</span>
    <span class="n">events</span><span class="p">:</span> <span class="nb">dict</span> <span class="o">=</span> <span class="p">{}</span>
    <span class="n">holidays</span><span class="p">:</span> <span class="nb">dict</span> <span class="o">=</span> <span class="p">{}</span>

    <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="n">self</span><span class="p">,</span> <span class="n">genai_client</span><span class="p">,</span> <span class="n">collection_name</span><span class="p">):</span>
        <span class="n">self</span><span class="p">.</span><span class="n">client</span> <span class="o">=</span> <span class="n">genai_client</span>
        <span class="n">self</span><span class="p">.</span><span class="n">embed_fn</span> <span class="o">=</span> <span class="nc">GeminiEmbedFunction</span><span class="p">(</span><span class="n">genai_client</span><span class="p">)</span>
        <span class="n">self</span><span class="p">.</span><span class="n">db</span> <span class="o">=</span> <span class="n">self</span><span class="p">.</span><span class="n">chroma_client</span><span class="p">.</span><span class="nf">get_or_create_collection</span><span class="p">(</span>
            <span class="n">name</span><span class="o">=</span><span class="n">collection_name</span><span class="p">,</span> 
            <span class="n">embedding_function</span><span class="o">=</span><span class="n">self</span><span class="p">.</span><span class="n">embed_fn</span><span class="p">,</span>  <span class="c1"># type: ignore
</span>            <span class="n">metadata</span><span class="o">=</span><span class="p">{</span><span class="sh">"</span><span class="s">hnsw:space</span><span class="sh">"</span><span class="p">:</span> <span class="sh">"</span><span class="s">cosine</span><span class="sh">"</span><span class="p">})</span>
        <span class="n">logging</span><span class="p">.</span><span class="nf">getLogger</span><span class="p">(</span><span class="sh">"</span><span class="s">chromadb</span><span class="sh">"</span><span class="p">).</span><span class="nf">setLevel</span><span class="p">(</span><span class="n">logging</span><span class="p">.</span><span class="n">ERROR</span><span class="p">)</span> <span class="c1"># suppress warning on existing id
</span>        <span class="n">self</span><span class="p">.</span><span class="nf">set_holidays</span><span class="p">(</span><span class="sh">"</span><span class="s">US</span><span class="sh">"</span><span class="p">,</span> <span class="p">[</span><span class="sh">"</span><span class="s">09-01-2025</span><span class="sh">"</span><span class="p">,</span><span class="sh">"</span><span class="s">10-13-2025</span><span class="sh">"</span><span class="p">,</span><span class="sh">"</span><span class="s">11-11-2025</span><span class="sh">"</span><span class="p">,</span><span class="sh">"</span><span class="s">11-27-2025</span><span class="sh">"</span><span class="p">,</span><span class="sh">"</span><span class="s">12-25-2025</span><span class="sh">"</span><span class="p">])</span>
        <span class="c1">#self.generated_events("US")
</span>
    <span class="k">def</span> <span class="nf">set_holidays</span><span class="p">(</span><span class="n">self</span><span class="p">,</span> <span class="n">exchange_code</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">holidays</span><span class="p">:</span> <span class="nb">list</span><span class="p">):</span>
        <span class="n">self</span><span class="p">.</span><span class="n">holidays</span><span class="p">[</span><span class="n">exchange_code</span><span class="p">]</span> <span class="o">=</span> <span class="p">[</span><span class="n">datetime</span><span class="p">.</span><span class="nf">strptime</span><span class="p">(</span><span class="n">h</span><span class="p">,</span> <span class="sh">"</span><span class="s">%m-%d-%Y</span><span class="sh">"</span><span class="p">).</span><span class="nf">date</span><span class="p">()</span> <span class="k">for</span> <span class="n">h</span> <span class="ow">in</span> <span class="n">holidays</span><span class="p">]</span>

    <span class="k">def</span> <span class="nf">get_exchange_codes</span><span class="p">(</span><span class="n">self</span><span class="p">,</span> <span class="n">with_query</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="bp">None</span><span class="p">):</span>
        <span class="n">gen</span> <span class="o">=</span> <span class="bp">None</span>
        <span class="k">if</span> <span class="n">with_query</span> <span class="ow">and</span> <span class="n">with_query</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">self</span><span class="p">.</span><span class="n">exchange_lists</span><span class="p">.</span><span class="nf">keys</span><span class="p">():</span>
            <span class="n">gen</span> <span class="o">=</span> <span class="nf">tqdm</span><span class="p">(</span><span class="n">total</span><span class="o">=</span><span class="mi">1</span><span class="p">,</span> <span class="n">desc</span><span class="o">=</span><span class="sh">"</span><span class="s">Generate exchange codes with_query</span><span class="sh">"</span><span class="p">)</span>
            <span class="n">data</span> <span class="o">=</span> <span class="n">self</span><span class="p">.</span><span class="nf">get_exchanges_csv</span><span class="p">(</span>
                <span class="sa">f</span><span class="sh">"""</span><span class="s">What is the </span><span class="si">{</span><span class="n">with_query</span><span class="si">}</span><span class="s"> exchange code? Return only the exchange codes 
                as a list in string form. Just the list string. 
                Omit all other information or details. Do not chat or use sentences.</span><span class="sh">"""</span><span class="p">).</span><span class="n">candidates</span><span class="p">[</span><span class="mi">0</span><span class="p">].</span><span class="n">content</span>
            <span class="n">self</span><span class="p">.</span><span class="n">exchange_lists</span><span class="p">[</span><span class="n">with_query</span><span class="p">]</span> <span class="o">=</span> <span class="n">ast</span><span class="p">.</span><span class="nf">literal_eval</span><span class="p">(</span><span class="n">data</span><span class="p">.</span><span class="n">parts</span><span class="p">[</span><span class="o">-</span><span class="mi">1</span><span class="p">].</span><span class="n">text</span><span class="p">)</span>
        <span class="k">elif</span> <span class="n">with_query</span> <span class="ow">is</span> <span class="bp">None</span> <span class="ow">and</span> <span class="n">self</span><span class="p">.</span><span class="n">exchange_codes</span> <span class="ow">is</span> <span class="bp">None</span><span class="p">:</span>
            <span class="n">gen</span> <span class="o">=</span> <span class="nf">tqdm</span><span class="p">(</span><span class="n">total</span><span class="o">=</span><span class="mi">1</span><span class="p">,</span> <span class="n">desc</span><span class="o">=</span><span class="sh">"</span><span class="s">Generate exchange codes</span><span class="sh">"</span><span class="p">)</span>
            <span class="n">data</span> <span class="o">=</span> <span class="n">self</span><span class="p">.</span><span class="nf">get_exchanges_csv</span><span class="p">(</span>
                <span class="sh">"""</span><span class="s">Give me a dictionary in string form. It must contain key:value pairs 
                mapping exchange code to name. Just the dictionary string. 
                Omit all other information or details. Do not chat or use sentences.</span><span class="sh">"""</span><span class="p">).</span><span class="n">candidates</span><span class="p">[</span><span class="mi">0</span><span class="p">].</span><span class="n">content</span>
            <span class="n">self</span><span class="p">.</span><span class="n">exchange_codes</span> <span class="o">=</span> <span class="n">ast</span><span class="p">.</span><span class="nf">literal_eval</span><span class="p">(</span><span class="n">data</span><span class="p">.</span><span class="n">parts</span><span class="p">[</span><span class="o">-</span><span class="mi">1</span><span class="p">].</span><span class="n">text</span><span class="p">.</span><span class="nf">strip</span><span class="p">(</span><span class="sh">"</span><span class="se">\\</span><span class="s">`</span><span class="sh">"</span><span class="p">))</span>
        <span class="k">if</span> <span class="n">gen</span><span class="p">:</span>
            <span class="n">gen</span><span class="p">.</span><span class="nf">update</span><span class="p">(</span><span class="mi">1</span><span class="p">)</span>
        <span class="k">return</span> <span class="n">self</span><span class="p">.</span><span class="n">exchange_lists</span><span class="p">[</span><span class="n">with_query</span><span class="p">]</span> <span class="k">if</span> <span class="n">with_query</span> <span class="k">else</span> <span class="n">self</span><span class="p">.</span><span class="n">exchange_codes</span>

    <span class="k">def</span> <span class="nf">get_event_date</span><span class="p">(</span><span class="n">self</span><span class="p">,</span> <span class="n">event_t</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">exchange_code</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">event</span><span class="p">:</span> <span class="n">MarketEvent</span><span class="p">):</span>
        <span class="n">current_dt_str</span> <span class="o">=</span> <span class="n">datetime</span><span class="p">.</span><span class="nf">now</span><span class="p">(</span><span class="n">GeneratedEvent</span><span class="p">.</span><span class="nf">tz</span><span class="p">()).</span><span class="nf">strftime</span><span class="p">(</span><span class="sh">'</span><span class="s">%c</span><span class="sh">'</span><span class="p">)</span>
        <span class="n">current_dt</span> <span class="o">=</span> <span class="n">datetime</span><span class="p">.</span><span class="nf">strptime</span><span class="p">(</span><span class="n">current_dt_str</span><span class="p">,</span> <span class="sh">"</span><span class="s">%a %b %d %H:%M:%S %Y</span><span class="sh">"</span><span class="p">)</span>
        <span class="n">current_t_str</span> <span class="o">=</span> <span class="n">datetime</span><span class="p">.</span><span class="nf">now</span><span class="p">(</span><span class="n">GeneratedEvent</span><span class="p">.</span><span class="nf">tz</span><span class="p">()).</span><span class="nf">strftime</span><span class="p">(</span><span class="sh">'</span><span class="s">%H:%M:%S</span><span class="sh">'</span><span class="p">)</span>
        <span class="n">current_t</span> <span class="o">=</span> <span class="n">datetime</span><span class="p">.</span><span class="nf">strptime</span><span class="p">(</span><span class="n">current_t_str</span><span class="p">,</span> <span class="sh">"</span><span class="s">%H:%M:%S</span><span class="sh">"</span><span class="p">).</span><span class="nf">time</span><span class="p">()</span>
        <span class="n">event_time</span> <span class="o">=</span> <span class="nf">parse</span><span class="p">(</span><span class="n">event_t</span><span class="p">).</span><span class="nf">time</span><span class="p">()</span>
        <span class="n">gen_datetime</span> <span class="o">=</span> <span class="bp">None</span>
        <span class="k">if</span> <span class="n">event</span> <span class="ow">is</span> <span class="n">MarketEvent</span><span class="p">.</span><span class="n">LAST_CLOSE</span><span class="p">:</span>
            <span class="n">last_close_day</span> <span class="o">=</span> <span class="n">current_dt</span><span class="p">.</span><span class="nf">date</span><span class="p">()</span> <span class="o">-</span> <span class="nf">timedelta</span><span class="p">(</span><span class="n">days</span><span class="o">=</span><span class="mi">0</span> <span class="k">if</span> <span class="n">current_t</span> <span class="o">&gt;</span> <span class="n">event_time</span> <span class="k">else</span> <span class="mi">1</span><span class="p">)</span>
            <span class="c1"># Loop backwards to find the last valid trading day (not a weekend or holiday).
</span>            <span class="k">while</span> <span class="n">last_close_day</span><span class="p">.</span><span class="nf">weekday</span><span class="p">()</span> <span class="o">&gt;=</span> <span class="mi">5</span> <span class="ow">or</span> <span class="n">last_close_day</span> <span class="ow">in</span> <span class="n">self</span><span class="p">.</span><span class="n">holidays</span><span class="p">[</span><span class="n">exchange_code</span><span class="p">]:</span> <span class="c1"># 5 = Sat, 6 = Sun
</span>                <span class="n">last_close_day</span> <span class="o">-=</span> <span class="nf">timedelta</span><span class="p">(</span><span class="n">days</span><span class="o">=</span><span class="mi">1</span><span class="p">)</span>
            <span class="c1"># Combine the date and time.
</span>            <span class="n">gen_datetime</span> <span class="o">=</span> <span class="n">datetime</span><span class="p">.</span><span class="nf">combine</span><span class="p">(</span><span class="n">last_close_day</span><span class="p">,</span> <span class="n">event_time</span><span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">next_event_day</span> <span class="o">=</span> <span class="n">current_dt</span><span class="p">.</span><span class="nf">date</span><span class="p">()</span> <span class="o">+</span> <span class="nf">timedelta</span><span class="p">(</span><span class="n">days</span><span class="o">=</span><span class="mi">0</span> <span class="k">if</span> <span class="n">current_t</span> <span class="o">&lt;</span> <span class="n">event_time</span> <span class="k">else</span> <span class="mi">1</span><span class="p">)</span>
            <span class="c1"># Loop forward to find the next valid trading day (not a weekend or holiday).
</span>            <span class="k">while</span> <span class="n">next_event_day</span><span class="p">.</span><span class="nf">weekday</span><span class="p">()</span> <span class="o">&gt;=</span> <span class="mi">5</span> <span class="ow">or</span> <span class="n">next_event_day</span> <span class="ow">in</span> <span class="n">self</span><span class="p">.</span><span class="n">holidays</span><span class="p">[</span><span class="n">exchange_code</span><span class="p">]:</span> <span class="c1"># 5 = Sat, 6 = Sun
</span>                <span class="n">next_event_day</span> <span class="o">+=</span> <span class="nf">timedelta</span><span class="p">(</span><span class="n">days</span><span class="o">=</span><span class="mi">1</span><span class="p">)</span>
            <span class="c1"># Combine date and time.
</span>            <span class="n">gen_datetime</span> <span class="o">=</span> <span class="n">datetime</span><span class="p">.</span><span class="nf">combine</span><span class="p">(</span><span class="n">next_event_day</span><span class="p">,</span> <span class="n">event_time</span><span class="p">)</span>
        <span class="c1"># Format the result as requested.
</span>        <span class="k">return</span> <span class="n">gen_datetime</span><span class="p">.</span><span class="nf">strftime</span><span class="p">(</span><span class="sh">'</span><span class="s">%a %b %d %X %Y</span><span class="sh">'</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">generate_event</span><span class="p">(</span><span class="n">self</span><span class="p">,</span> <span class="n">exchange_code</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">event</span><span class="p">:</span> <span class="n">MarketEvent</span><span class="p">):</span>
        <span class="k">if</span> <span class="n">event</span> <span class="ow">is</span> <span class="n">MarketEvent</span><span class="p">.</span><span class="n">LAST_CLOSE</span> <span class="ow">or</span> <span class="n">event</span> <span class="ow">is</span> <span class="n">MarketEvent</span><span class="p">.</span><span class="n">POST_CLOSE</span><span class="p">:</span>
            <span class="n">prompt</span> <span class="o">=</span> <span class="sa">f</span><span class="sh">"""</span><span class="s">What is the closing time including post_market hours.</span><span class="sh">"""</span>
        <span class="k">elif</span> <span class="n">event</span> <span class="ow">is</span> <span class="n">MarketEvent</span><span class="p">.</span><span class="n">PRE_OPEN</span> <span class="ow">or</span> <span class="n">event</span> <span class="ow">is</span> <span class="n">MarketEvent</span><span class="p">.</span><span class="n">REG_OPEN</span><span class="p">:</span>
            <span class="n">is_pre</span> <span class="o">=</span> <span class="sh">"</span><span class="s">including</span><span class="sh">"</span> <span class="k">if</span> <span class="n">event</span> <span class="ow">is</span> <span class="n">MarketEvent</span><span class="p">.</span><span class="n">PRE_OPEN</span> <span class="k">else</span> <span class="sh">"</span><span class="s">excluding</span><span class="sh">"</span>
            <span class="n">prompt</span> <span class="o">=</span> <span class="sa">f</span><span class="sh">"""</span><span class="s">What is the opening time </span><span class="si">{</span><span class="n">is_pre</span><span class="si">}</span><span class="s"> pre_market hours.</span><span class="sh">"""</span>
        <span class="k">elif</span> <span class="n">event</span> <span class="ow">is</span> <span class="n">MarketEvent</span><span class="p">.</span><span class="n">REG_CLOSE</span><span class="p">:</span>
            <span class="n">prompt</span> <span class="o">=</span> <span class="sa">f</span><span class="sh">"""</span><span class="s">What is the closing time excluding post_market hours.</span><span class="sh">"""</span>
        <span class="n">prompt</span> <span class="o">=</span> <span class="sa">f</span><span class="sh">"""</span><span class="s">Answer based on your knowledge of exchange operating hours.
            Do not answer in full sentences. Omit all chat and provide the answer only.
            The fields pre_market and post_market both represent extended operating hours.

            The current date and time: </span><span class="si">{</span><span class="n">datetime</span><span class="p">.</span><span class="nf">now</span><span class="p">(</span><span class="n">GeneratedEvent</span><span class="p">.</span><span class="nf">tz</span><span class="p">()).</span><span class="nf">strftime</span><span class="p">(</span><span class="sh">'</span><span class="s">%c</span><span class="sh">'</span><span class="p">)</span><span class="si">}</span><span class="s">
            
            Consider the </span><span class="si">{</span><span class="n">exchange_code</span><span class="si">}</span><span class="s"> exchange</span><span class="sh">'</span><span class="s">s operating hours.
            </span><span class="si">{</span><span class="n">prompt</span><span class="si">}</span><span class="s">
            
            Answer with the time in this format: </span><span class="sh">'</span><span class="s">%H:%M:%S</span><span class="sh">'</span><span class="s">.
            Omit all other chat and details. Do not use sentences.</span><span class="sh">"""</span>
        <span class="n">progress</span> <span class="o">=</span> <span class="nf">tqdm</span><span class="p">(</span><span class="n">total</span><span class="o">=</span><span class="mi">1</span><span class="p">,</span> <span class="n">desc</span><span class="o">=</span><span class="sa">f</span><span class="sh">"</span><span class="s">Generate </span><span class="si">{</span><span class="n">exchange_code</span><span class="si">}</span><span class="s">-&gt;</span><span class="si">{</span><span class="n">event</span><span class="si">}</span><span class="sh">"</span><span class="p">)</span>
        <span class="n">response</span> <span class="o">=</span> <span class="n">self</span><span class="p">.</span><span class="nf">get_exchanges_csv</span><span class="p">(</span><span class="n">prompt</span><span class="p">).</span><span class="n">candidates</span><span class="p">[</span><span class="mi">0</span><span class="p">].</span><span class="n">content</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="k">if</span> <span class="n">Api</span><span class="p">.</span><span class="n">Const</span><span class="p">.</span><span class="nc">Stop</span><span class="p">()</span> <span class="ow">in</span> <span class="sa">f</span><span class="sh">"</span><span class="si">{</span><span class="n">response</span><span class="p">.</span><span class="n">parts</span><span class="p">[</span><span class="o">-</span><span class="mi">1</span><span class="p">].</span><span class="n">text</span><span class="si">}</span><span class="sh">"</span><span class="p">:</span>
                <span class="n">self</span><span class="p">.</span><span class="nf">generate_event_failed</span><span class="p">(</span><span class="n">progress</span><span class="p">,</span> <span class="n">exchange_code</span><span class="p">,</span> <span class="n">event</span><span class="p">)</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="n">response</span> <span class="o">=</span> <span class="n">self</span><span class="p">.</span><span class="nf">get_event_date</span><span class="p">(</span><span class="n">response</span><span class="p">.</span><span class="n">parts</span><span class="p">[</span><span class="o">-</span><span class="mi">1</span><span class="p">].</span><span class="n">text</span><span class="p">,</span> <span class="n">exchange_code</span><span class="p">,</span> <span class="n">event</span><span class="p">)</span>
                <span class="n">progress</span><span class="p">.</span><span class="nf">update</span><span class="p">(</span><span class="mi">1</span><span class="p">)</span>
                <span class="k">return</span> <span class="n">response</span>
        <span class="k">except</span> <span class="nb">Exception</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
            <span class="n">self</span><span class="p">.</span><span class="nf">generate_event_failed</span><span class="p">(</span><span class="n">progress</span><span class="p">,</span> <span class="n">exchange_code</span><span class="p">,</span> <span class="n">event</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">generate_event_failed</span><span class="p">(</span><span class="n">self</span><span class="p">,</span> <span class="n">progress</span><span class="p">:</span> <span class="n">tqdm</span><span class="p">,</span> <span class="n">exchange_code</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">event</span><span class="p">:</span> <span class="n">MarketEvent</span><span class="p">):</span>
        <span class="n">progress</span><span class="p">.</span><span class="nf">close</span><span class="p">()</span>
        <span class="n">api</span><span class="p">.</span><span class="nf">generation_fail</span><span class="p">()</span>
        <span class="n">time</span><span class="p">.</span><span class="nf">sleep</span><span class="p">(</span><span class="n">api</span><span class="p">.</span><span class="n">dt_between</span><span class="p">)</span>
        <span class="k">return</span> <span class="n">self</span><span class="p">.</span><span class="nf">generate_event</span><span class="p">(</span><span class="n">exchange_code</span><span class="p">,</span> <span class="n">event</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">generated_events</span><span class="p">(</span><span class="n">self</span><span class="p">,</span> <span class="n">exchange_code</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">GeneratedEvent</span><span class="p">:</span>
        <span class="c1"># Check for an existing GeneratedEvent object having updates.
</span>        <span class="k">if</span> <span class="n">exchange_code</span> <span class="ow">in</span> <span class="n">self</span><span class="p">.</span><span class="n">events</span><span class="p">.</span><span class="nf">keys</span><span class="p">()</span> <span class="ow">and</span> <span class="n">self</span><span class="p">.</span><span class="n">events</span><span class="p">[</span><span class="n">exchange_code</span><span class="p">].</span><span class="nf">has_update</span><span class="p">():</span>
            <span class="n">event_obj</span> <span class="o">=</span> <span class="n">self</span><span class="p">.</span><span class="n">events</span><span class="p">[</span><span class="n">exchange_code</span><span class="p">]</span>
            <span class="n">event_state</span> <span class="o">=</span> <span class="p">[(</span><span class="n">event_obj</span><span class="p">.</span><span class="n">pre_open</span><span class="p">,</span> <span class="n">MarketEvent</span><span class="p">.</span><span class="n">PRE_OPEN</span><span class="p">),</span>
                           <span class="p">(</span><span class="n">event_obj</span><span class="p">.</span><span class="n">reg_open</span><span class="p">,</span> <span class="n">MarketEvent</span><span class="p">.</span><span class="n">REG_OPEN</span><span class="p">),</span>
                           <span class="p">(</span><span class="n">event_obj</span><span class="p">.</span><span class="n">reg_close</span><span class="p">,</span> <span class="n">MarketEvent</span><span class="p">.</span><span class="n">REG_CLOSE</span><span class="p">),</span>
                           <span class="p">(</span><span class="n">event_obj</span><span class="p">.</span><span class="n">post_close</span><span class="p">,</span> <span class="n">MarketEvent</span><span class="p">.</span><span class="n">POST_CLOSE</span><span class="p">)]</span>
            <span class="c1"># Need now in same format as generated.
</span>            <span class="n">datetime_now</span> <span class="o">=</span> <span class="nf">parse</span><span class="p">(</span><span class="n">datetime</span><span class="p">.</span><span class="nf">now</span><span class="p">(</span><span class="n">event_obj</span><span class="p">.</span><span class="nf">tz</span><span class="p">()).</span><span class="nf">strftime</span><span class="p">(</span><span class="sh">'</span><span class="s">%c</span><span class="sh">'</span><span class="p">))</span>
            <span class="n">gen_ts</span> <span class="o">=</span> <span class="nf">parse</span><span class="p">(</span><span class="n">event_obj</span><span class="p">.</span><span class="n">timestamp</span><span class="p">)</span>
            <span class="c1"># Re-generate events when day changes.
</span>            <span class="k">if</span> <span class="n">datetime_now</span><span class="p">.</span><span class="n">day</span> <span class="o">&gt;</span> <span class="n">gen_ts</span><span class="p">.</span><span class="n">day</span><span class="p">:</span>
                <span class="k">del</span> <span class="n">self</span><span class="p">.</span><span class="n">events</span><span class="p">[</span><span class="n">exchange_code</span><span class="p">]</span>
                <span class="k">return</span> <span class="n">self</span><span class="p">.</span><span class="nf">generated_events</span><span class="p">(</span><span class="n">exchange_code</span><span class="p">)</span>
            <span class="c1"># Update changed events on trading days.
</span>            <span class="k">for</span> <span class="n">e</span> <span class="ow">in</span> <span class="n">event_state</span><span class="p">:</span>
                <span class="k">if</span> <span class="n">datetime_now</span> <span class="o">&gt;</span> <span class="nf">parse</span><span class="p">(</span><span class="n">e</span><span class="p">[</span><span class="mi">0</span><span class="p">]):</span>
                    <span class="n">event_dt</span> <span class="o">=</span> <span class="n">self</span><span class="p">.</span><span class="nf">generate_event</span><span class="p">(</span><span class="n">exchange_code</span><span class="p">,</span> <span class="n">e</span><span class="p">[</span><span class="mi">1</span><span class="p">])</span>
                    <span class="k">match</span> <span class="n">e</span><span class="p">[</span><span class="mi">1</span><span class="p">]:</span>
                        <span class="k">case</span> <span class="n">MarketEvent</span><span class="p">.</span><span class="n">PRE_OPEN</span><span class="p">:</span>
                            <span class="n">event_obj</span><span class="p">.</span><span class="n">pre_open</span> <span class="o">=</span> <span class="n">event_dt</span>
                        <span class="k">case</span> <span class="n">MarketEvent</span><span class="p">.</span><span class="n">REG_OPEN</span><span class="p">:</span>
                            <span class="n">event_obj</span><span class="p">.</span><span class="n">reg_open</span> <span class="o">=</span> <span class="n">event_dt</span>
                        <span class="k">case</span> <span class="n">MarketEvent</span><span class="p">.</span><span class="n">REG_CLOSE</span><span class="p">:</span>
                            <span class="n">event_obj</span><span class="p">.</span><span class="n">reg_close</span> <span class="o">=</span> <span class="n">event_dt</span>
                        <span class="k">case</span> <span class="n">MarketEvent</span><span class="p">.</span><span class="n">POST_CLOSE</span><span class="p">:</span>
                            <span class="n">event_obj</span><span class="p">.</span><span class="n">post_close</span> <span class="o">=</span> <span class="n">event_dt</span>
            <span class="n">event_obj</span><span class="p">.</span><span class="n">timestamp</span> <span class="o">=</span> <span class="n">datetime</span><span class="p">.</span><span class="nf">now</span><span class="p">(</span><span class="n">event_obj</span><span class="p">.</span><span class="nf">tz</span><span class="p">()).</span><span class="nf">strftime</span><span class="p">(</span><span class="sh">'</span><span class="s">%c</span><span class="sh">'</span><span class="p">)</span>
            <span class="n">self</span><span class="p">.</span><span class="n">events</span><span class="p">[</span><span class="n">exchange_code</span><span class="p">]</span> <span class="o">=</span> <span class="n">event_obj</span>
        <span class="c1"># Generate events for an exchange code not in cache.
</span>        <span class="k">elif</span> <span class="n">exchange_code</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">self</span><span class="p">.</span><span class="n">events</span><span class="p">.</span><span class="nf">keys</span><span class="p">():</span>
            <span class="n">self</span><span class="p">.</span><span class="n">events</span><span class="p">[</span><span class="n">exchange_code</span><span class="p">]</span> <span class="o">=</span> <span class="nc">GeneratedEvent</span><span class="p">(</span>
                <span class="n">last_close</span><span class="o">=</span><span class="n">self</span><span class="p">.</span><span class="nf">generate_event</span><span class="p">(</span><span class="n">exchange_code</span><span class="p">,</span> <span class="n">MarketEvent</span><span class="p">.</span><span class="n">LAST_CLOSE</span><span class="p">),</span>
                <span class="n">pre_open</span><span class="o">=</span><span class="n">self</span><span class="p">.</span><span class="nf">generate_event</span><span class="p">(</span><span class="n">exchange_code</span><span class="p">,</span> <span class="n">MarketEvent</span><span class="p">.</span><span class="n">PRE_OPEN</span><span class="p">),</span>
                <span class="n">reg_open</span><span class="o">=</span><span class="n">self</span><span class="p">.</span><span class="nf">generate_event</span><span class="p">(</span><span class="n">exchange_code</span><span class="p">,</span> <span class="n">MarketEvent</span><span class="p">.</span><span class="n">REG_OPEN</span><span class="p">),</span>
                <span class="n">reg_close</span><span class="o">=</span><span class="n">self</span><span class="p">.</span><span class="nf">generate_event</span><span class="p">(</span><span class="n">exchange_code</span><span class="p">,</span> <span class="n">MarketEvent</span><span class="p">.</span><span class="n">REG_CLOSE</span><span class="p">),</span>
                <span class="n">post_close</span><span class="o">=</span><span class="n">self</span><span class="p">.</span><span class="nf">generate_event</span><span class="p">(</span><span class="n">exchange_code</span><span class="p">,</span> <span class="n">MarketEvent</span><span class="p">.</span><span class="n">POST_CLOSE</span><span class="p">),</span>
                <span class="n">is_holiday</span><span class="o">=</span><span class="n">datetime</span><span class="p">.</span><span class="nf">now</span><span class="p">().</span><span class="nf">date</span><span class="p">()</span> <span class="ow">in</span> <span class="n">self</span><span class="p">.</span><span class="n">holidays</span><span class="p">[</span><span class="n">exchange_code</span><span class="p">])</span>
        <span class="k">return</span> <span class="n">self</span><span class="p">.</span><span class="n">events</span><span class="p">[</span><span class="n">exchange_code</span><span class="p">]</span>

    <span class="k">def</span> <span class="nf">set_holiday_event</span><span class="p">(</span><span class="n">self</span><span class="p">,</span> <span class="n">exchange_code</span><span class="p">:</span> <span class="nb">str</span><span class="p">):</span>
        <span class="n">self</span><span class="p">.</span><span class="nf">generated_events</span><span class="p">(</span><span class="n">exchange_code</span><span class="p">).</span><span class="n">is_holiday</span> <span class="o">=</span> <span class="bp">True</span>

    <span class="k">def</span> <span class="nf">last_market_close</span><span class="p">(</span><span class="n">self</span><span class="p">,</span> <span class="n">exchange_code</span><span class="p">:</span> <span class="nb">str</span><span class="p">):</span>
        <span class="k">return</span> <span class="n">self</span><span class="p">.</span><span class="nf">generated_events</span><span class="p">(</span><span class="n">exchange_code</span><span class="p">).</span><span class="n">last_close</span>

    <span class="k">def</span> <span class="nf">add_documents_list</span><span class="p">(</span><span class="n">self</span><span class="p">,</span> <span class="n">docs</span><span class="p">:</span> <span class="nb">list</span><span class="p">):</span>
        <span class="n">self</span><span class="p">.</span><span class="n">embed_fn</span><span class="p">.</span><span class="n">document_mode</span> <span class="o">=</span> <span class="bp">True</span> <span class="c1"># Switch to document mode.
</span>        <span class="n">ids</span> <span class="o">=</span> <span class="nf">list</span><span class="p">(</span><span class="nf">map</span><span class="p">(</span><span class="nb">str</span><span class="p">,</span> <span class="nf">range</span><span class="p">(</span><span class="n">self</span><span class="p">.</span><span class="n">db</span><span class="p">.</span><span class="nf">count</span><span class="p">(),</span> <span class="n">self</span><span class="p">.</span><span class="n">db</span><span class="p">.</span><span class="nf">count</span><span class="p">()</span><span class="o">+</span><span class="nf">len</span><span class="p">(</span><span class="n">docs</span><span class="p">))))</span>
        <span class="n">metas</span><span class="o">=</span><span class="p">[{</span><span class="sh">"</span><span class="s">source</span><span class="sh">"</span><span class="p">:</span> <span class="n">doc</span><span class="p">.</span><span class="n">metadata</span><span class="p">[</span><span class="sh">"</span><span class="s">source</span><span class="sh">"</span><span class="p">]}</span> <span class="k">for</span> <span class="n">doc</span> <span class="ow">in</span> <span class="n">docs</span><span class="p">]</span>
        <span class="n">content</span><span class="o">=</span><span class="p">[</span><span class="n">doc</span><span class="p">.</span><span class="n">page_content</span> <span class="k">for</span> <span class="n">doc</span> <span class="ow">in</span> <span class="n">docs</span><span class="p">]</span>
        <span class="nf">tqdm</span><span class="p">(</span><span class="n">self</span><span class="p">.</span><span class="n">db</span><span class="p">.</span><span class="nf">add</span><span class="p">(</span><span class="n">ids</span><span class="o">=</span><span class="n">ids</span><span class="p">,</span> <span class="n">documents</span><span class="o">=</span><span class="n">content</span><span class="p">,</span> <span class="n">metadatas</span><span class="o">=</span><span class="n">metas</span><span class="p">),</span> <span class="n">desc</span><span class="o">=</span><span class="sh">"</span><span class="s">Generate document embedding</span><span class="sh">"</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">add_api_document</span><span class="p">(</span><span class="n">self</span><span class="p">,</span> <span class="n">query</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">api_response</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">topic</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">source</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="sh">"</span><span class="s">add_api_document</span><span class="sh">"</span><span class="p">):</span>
        <span class="n">self</span><span class="p">.</span><span class="n">embed_fn</span><span class="p">.</span><span class="n">document_mode</span> <span class="o">=</span> <span class="bp">True</span> <span class="c1"># Switch to document mode.
</span>        <span class="n">splitter</span> <span class="o">=</span> <span class="nc">RecursiveJsonSplitter</span><span class="p">(</span><span class="n">max_chunk_size</span><span class="o">=</span><span class="n">Api</span><span class="p">.</span><span class="n">Const</span><span class="p">.</span><span class="nc">ChunkMax</span><span class="p">())</span>
        <span class="n">docs</span> <span class="o">=</span> <span class="n">splitter</span><span class="p">.</span><span class="nf">create_documents</span><span class="p">(</span><span class="n">texts</span><span class="o">=</span><span class="p">[</span><span class="n">api_response</span><span class="p">],</span> <span class="n">convert_lists</span><span class="o">=</span><span class="bp">True</span><span class="p">)</span>
        <span class="n">ids</span> <span class="o">=</span> <span class="nf">list</span><span class="p">(</span><span class="nf">map</span><span class="p">(</span><span class="nb">str</span><span class="p">,</span> <span class="nf">range</span><span class="p">(</span><span class="n">self</span><span class="p">.</span><span class="n">db</span><span class="p">.</span><span class="nf">count</span><span class="p">(),</span> <span class="n">self</span><span class="p">.</span><span class="n">db</span><span class="p">.</span><span class="nf">count</span><span class="p">()</span><span class="o">+</span><span class="nf">len</span><span class="p">(</span><span class="n">docs</span><span class="p">))))</span>
        <span class="n">content</span> <span class="o">=</span> <span class="p">[</span><span class="n">json</span><span class="p">.</span><span class="nf">dumps</span><span class="p">(</span><span class="n">doc</span><span class="p">.</span><span class="n">page_content</span><span class="p">)</span> <span class="k">for</span> <span class="n">doc</span> <span class="ow">in</span> <span class="n">docs</span><span class="p">]</span>
        <span class="n">metas</span> <span class="o">=</span> <span class="p">[{</span><span class="sh">"</span><span class="s">source</span><span class="sh">"</span><span class="p">:</span> <span class="n">source</span><span class="p">,</span> <span class="sh">"</span><span class="s">topic</span><span class="sh">"</span><span class="p">:</span> <span class="n">topic</span><span class="p">}]</span><span class="o">*</span><span class="nf">len</span><span class="p">(</span><span class="n">docs</span><span class="p">)</span>
        <span class="nf">tqdm</span><span class="p">(</span><span class="n">self</span><span class="p">.</span><span class="n">db</span><span class="p">.</span><span class="nf">add</span><span class="p">(</span><span class="n">ids</span><span class="o">=</span><span class="n">ids</span><span class="p">,</span> <span class="n">documents</span><span class="o">=</span><span class="n">content</span><span class="p">,</span> <span class="n">metadatas</span><span class="o">=</span><span class="n">metas</span><span class="p">),</span> <span class="n">desc</span><span class="o">=</span><span class="sh">"</span><span class="s">Generate api embedding</span><span class="sh">"</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">add_peers_document</span><span class="p">(</span><span class="n">self</span><span class="p">,</span> <span class="n">query</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">names</span><span class="p">:</span> <span class="nb">list</span><span class="p">,</span> <span class="n">topic</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">source</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">group</span><span class="p">:</span> <span class="nb">str</span><span class="p">):</span>
        <span class="n">self</span><span class="p">.</span><span class="n">embed_fn</span><span class="p">.</span><span class="n">document_mode</span> <span class="o">=</span> <span class="bp">True</span> <span class="c1"># Switch to document mode.
</span>        <span class="n">peers</span> <span class="o">=</span> <span class="p">{</span><span class="sh">"</span><span class="s">symbol</span><span class="sh">"</span><span class="p">:</span> <span class="n">topic</span><span class="p">,</span> <span class="sh">"</span><span class="s">peers</span><span class="sh">"</span><span class="p">:</span> <span class="n">names</span><span class="p">}</span>
        <span class="nf">tqdm</span><span class="p">(</span><span class="n">self</span><span class="p">.</span><span class="n">db</span><span class="p">.</span><span class="nf">add</span><span class="p">(</span><span class="n">ids</span><span class="o">=</span><span class="nf">str</span><span class="p">(</span><span class="n">self</span><span class="p">.</span><span class="n">db</span><span class="p">.</span><span class="nf">count</span><span class="p">()),</span>
                         <span class="n">documents</span><span class="o">=</span><span class="p">[</span><span class="n">json</span><span class="p">.</span><span class="nf">dumps</span><span class="p">(</span><span class="n">peers</span><span class="p">)],</span>
                         <span class="n">metadatas</span><span class="o">=</span><span class="p">[{</span><span class="sh">"</span><span class="s">source</span><span class="sh">"</span><span class="p">:</span> <span class="n">source</span><span class="p">,</span> <span class="sh">"</span><span class="s">topic</span><span class="sh">"</span><span class="p">:</span> <span class="n">topic</span><span class="p">,</span> <span class="sh">"</span><span class="s">group</span><span class="sh">"</span><span class="p">:</span> <span class="n">group</span><span class="p">}]),</span>
             <span class="n">desc</span><span class="o">=</span><span class="sh">"</span><span class="s">Generate peers embedding</span><span class="sh">"</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">get_peers_document</span><span class="p">(</span><span class="n">self</span><span class="p">,</span> <span class="n">query</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">topic</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">group</span><span class="p">:</span> <span class="nb">str</span><span class="p">):</span>
        <span class="k">return</span> <span class="n">self</span><span class="p">.</span><span class="nf">get_documents_list</span><span class="p">(</span><span class="n">query</span><span class="p">,</span> <span class="n">where</span><span class="o">=</span><span class="p">{</span><span class="sh">"</span><span class="s">$and</span><span class="sh">"</span><span class="p">:</span> <span class="p">[{</span><span class="sh">"</span><span class="s">group</span><span class="sh">"</span><span class="p">:</span> <span class="n">group</span><span class="p">},</span> <span class="p">{</span><span class="sh">"</span><span class="s">topic</span><span class="sh">"</span><span class="p">:</span> <span class="n">topic</span><span class="p">}]})</span>

    <span class="k">def</span> <span class="nf">add_rest_chunks</span><span class="p">(</span><span class="n">self</span><span class="p">,</span> <span class="n">chunks</span><span class="p">:</span> <span class="nb">list</span><span class="p">,</span> <span class="n">topic</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">source</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">ids</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">list</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="bp">None</span><span class="p">,</span>
                        <span class="n">meta_opt</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">list</span><span class="p">[</span><span class="nb">dict</span><span class="p">]]</span> <span class="o">=</span> <span class="bp">None</span><span class="p">,</span> <span class="n">is_update</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="bp">True</span><span class="p">):</span>
        <span class="n">self</span><span class="p">.</span><span class="n">embed_fn</span><span class="p">.</span><span class="n">document_mode</span> <span class="o">=</span> <span class="bp">True</span> <span class="c1"># Switch to document mode
</span>        <span class="k">if</span> <span class="n">ids</span> <span class="ow">is</span> <span class="bp">None</span><span class="p">:</span>
            <span class="n">ids</span> <span class="o">=</span> <span class="nf">list</span><span class="p">(</span><span class="nf">map</span><span class="p">(</span><span class="nb">str</span><span class="p">,</span> <span class="nf">range</span><span class="p">(</span><span class="n">self</span><span class="p">.</span><span class="n">db</span><span class="p">.</span><span class="nf">count</span><span class="p">(),</span> <span class="n">self</span><span class="p">.</span><span class="n">db</span><span class="p">.</span><span class="nf">count</span><span class="p">()</span><span class="o">+</span><span class="nf">len</span><span class="p">(</span><span class="n">chunks</span><span class="p">))))</span>
        <span class="k">if</span> <span class="nf">isinstance</span><span class="p">(</span><span class="n">chunks</span><span class="p">[</span><span class="mi">0</span><span class="p">],</span> <span class="n">BaseModel</span><span class="p">):</span>
            <span class="n">docs</span> <span class="o">=</span> <span class="p">[</span><span class="n">model</span><span class="p">.</span><span class="nf">model_dump_json</span><span class="p">()</span> <span class="k">for</span> <span class="n">model</span> <span class="ow">in</span> <span class="n">chunks</span><span class="p">]</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">docs</span> <span class="o">=</span> <span class="p">[</span><span class="n">json</span><span class="p">.</span><span class="nf">dumps</span><span class="p">(</span><span class="n">obj</span><span class="p">)</span> <span class="k">for</span> <span class="n">obj</span> <span class="ow">in</span> <span class="n">chunks</span><span class="p">]</span>
        <span class="n">meta_base</span> <span class="o">=</span> <span class="p">{</span><span class="sh">"</span><span class="s">source</span><span class="sh">"</span><span class="p">:</span> <span class="n">source</span><span class="p">,</span> <span class="sh">"</span><span class="s">topic</span><span class="sh">"</span><span class="p">:</span> <span class="n">topic</span><span class="p">}</span>
        <span class="k">if</span> <span class="n">meta_opt</span> <span class="ow">is</span> <span class="ow">not</span> <span class="bp">None</span><span class="p">:</span>
            <span class="k">for</span> <span class="n">m</span> <span class="ow">in</span> <span class="n">meta_opt</span><span class="p">:</span>
                <span class="n">m</span><span class="p">.</span><span class="nf">update</span><span class="p">(</span><span class="n">meta_base</span><span class="p">)</span>
        <span class="n">metas</span> <span class="o">=</span> <span class="p">[</span><span class="n">meta_base</span><span class="p">]</span><span class="o">*</span><span class="nf">len</span><span class="p">(</span><span class="n">chunks</span><span class="p">)</span> <span class="k">if</span> <span class="n">meta_opt</span> <span class="ow">is</span> <span class="bp">None</span> <span class="k">else</span> <span class="n">meta_opt</span>
        <span class="k">if</span> <span class="n">is_update</span><span class="p">:</span>
            <span class="nf">tqdm</span><span class="p">(</span><span class="n">self</span><span class="p">.</span><span class="n">db</span><span class="p">.</span><span class="nf">upsert</span><span class="p">(</span><span class="n">ids</span><span class="o">=</span><span class="n">ids</span><span class="p">,</span> <span class="n">documents</span><span class="o">=</span><span class="n">docs</span><span class="p">,</span> <span class="n">metadatas</span><span class="o">=</span><span class="n">metas</span><span class="p">),</span> <span class="n">desc</span><span class="o">=</span><span class="sh">"</span><span class="s">Upsert chunks embedding</span><span class="sh">"</span><span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="nf">tqdm</span><span class="p">(</span><span class="n">self</span><span class="p">.</span><span class="n">db</span><span class="p">.</span><span class="nf">add</span><span class="p">(</span><span class="n">ids</span><span class="o">=</span><span class="n">ids</span><span class="p">,</span> <span class="n">documents</span><span class="o">=</span><span class="n">docs</span><span class="p">,</span> <span class="n">metadatas</span><span class="o">=</span><span class="n">metas</span><span class="p">),</span> <span class="n">desc</span><span class="o">=</span><span class="sh">"</span><span class="s">Add chunks embedding</span><span class="sh">"</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">get_market_status</span><span class="p">(</span><span class="n">self</span><span class="p">,</span> <span class="n">exchange_code</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">tuple</span><span class="p">[</span><span class="nb">list</span><span class="p">[</span><span class="n">VectorStoreResult</span><span class="p">],</span> <span class="nb">bool</span><span class="p">]:</span> <span class="c1"># result, has rest update
</span>        <span class="n">self</span><span class="p">.</span><span class="n">embed_fn</span><span class="p">.</span><span class="n">document_mode</span> <span class="o">=</span> <span class="bp">False</span> <span class="c1"># Switch to query mode.
</span>        <span class="n">stored</span> <span class="o">=</span> <span class="n">self</span><span class="p">.</span><span class="nf">stored_result</span><span class="p">(</span><span class="n">self</span><span class="p">.</span><span class="n">db</span><span class="p">.</span><span class="nf">get</span><span class="p">(</span><span class="n">where</span><span class="o">=</span><span class="p">{</span>
            <span class="sh">"</span><span class="s">$and</span><span class="sh">"</span><span class="p">:</span> <span class="p">[{</span><span class="sh">"</span><span class="s">exchange</span><span class="sh">"</span><span class="p">:</span> <span class="n">exchange_code</span><span class="p">},</span> <span class="p">{</span><span class="sh">"</span><span class="s">topic</span><span class="sh">"</span><span class="p">:</span> <span class="sh">"</span><span class="s">market_status</span><span class="sh">"</span><span class="p">}]}))</span>
        <span class="k">if</span> <span class="nf">len</span><span class="p">(</span><span class="n">stored</span><span class="p">)</span> <span class="o">==</span> <span class="mi">0</span><span class="p">:</span>
            <span class="k">return</span> <span class="n">stored</span><span class="p">,</span> <span class="bp">True</span>
        <span class="c1"># Check for a daily market status update.
</span>        <span class="n">status</span> <span class="o">=</span> <span class="n">json</span><span class="p">.</span><span class="nf">loads</span><span class="p">(</span><span class="n">stored</span><span class="p">[</span><span class="mi">0</span><span class="p">].</span><span class="n">docs</span><span class="p">)</span>
        <span class="n">gen_day</span> <span class="o">=</span> <span class="nf">parse</span><span class="p">(</span><span class="n">self</span><span class="p">.</span><span class="nf">generated_events</span><span class="p">(</span><span class="n">exchange_code</span><span class="p">).</span><span class="n">timestamp</span><span class="p">).</span><span class="n">day</span>
        <span class="n">store_day</span> <span class="o">=</span> <span class="nf">parse</span><span class="p">(</span><span class="n">stored</span><span class="p">[</span><span class="mi">0</span><span class="p">].</span><span class="n">meta</span><span class="p">[</span><span class="sh">'</span><span class="s">timestamp</span><span class="sh">'</span><span class="p">]).</span><span class="n">day</span>
        <span class="k">if</span> <span class="n">status</span><span class="p">[</span><span class="sh">"</span><span class="s">holiday</span><span class="sh">"</span><span class="p">]</span> <span class="o">!=</span> <span class="n">MarketSession</span><span class="p">.</span><span class="n">NA</span><span class="p">.</span><span class="n">value</span> <span class="ow">and</span> <span class="n">gen_day</span> <span class="o">==</span> <span class="n">store_day</span><span class="p">:</span>
            <span class="k">return</span> <span class="n">stored</span><span class="p">,</span> <span class="bp">False</span>
        <span class="k">elif</span> <span class="n">gen_day</span> <span class="o">&gt;</span> <span class="n">store_day</span><span class="p">:</span>
            <span class="k">return</span> <span class="n">stored</span><span class="p">,</span> <span class="bp">True</span>
        <span class="c1"># Update with generated events to avoid rest api requests.
</span>        <span class="n">status</span><span class="p">[</span><span class="sh">"</span><span class="s">session</span><span class="sh">"</span><span class="p">]</span> <span class="o">=</span> <span class="n">self</span><span class="p">.</span><span class="nf">generated_events</span><span class="p">(</span><span class="n">exchange_code</span><span class="p">).</span><span class="nf">session</span><span class="p">().</span><span class="n">value</span>
        <span class="n">status</span><span class="p">[</span><span class="sh">"</span><span class="s">isOpen</span><span class="sh">"</span><span class="p">]</span> <span class="o">=</span> <span class="n">self</span><span class="p">.</span><span class="nf">generated_events</span><span class="p">(</span><span class="n">exchange_code</span><span class="p">).</span><span class="nf">is_open</span><span class="p">()</span>
        <span class="n">stored</span><span class="p">[</span><span class="mi">0</span><span class="p">].</span><span class="n">docs</span> <span class="o">=</span> <span class="n">json</span><span class="p">.</span><span class="nf">dumps</span><span class="p">(</span><span class="n">status</span><span class="p">)</span>
        <span class="k">return</span> <span class="n">stored</span><span class="p">,</span> <span class="bp">False</span>

    <span class="k">def</span> <span class="nf">get_basic_financials</span><span class="p">(</span><span class="n">self</span><span class="p">,</span> <span class="n">query</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">topic</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">source</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="sh">"</span><span class="s">get_financials_1</span><span class="sh">"</span><span class="p">):</span>
        <span class="k">return</span> <span class="n">self</span><span class="p">.</span><span class="nf">get_documents_list</span><span class="p">(</span>
            <span class="n">query</span><span class="p">,</span> <span class="n">max_sources</span><span class="o">=</span><span class="mi">200</span><span class="p">,</span> <span class="n">where</span><span class="o">=</span><span class="p">{</span><span class="sh">"</span><span class="s">$and</span><span class="sh">"</span><span class="p">:</span> <span class="p">[{</span><span class="sh">"</span><span class="s">source</span><span class="sh">"</span><span class="p">:</span> <span class="n">source</span><span class="p">},</span> <span class="p">{</span><span class="sh">"</span><span class="s">topic</span><span class="sh">"</span><span class="p">:</span> <span class="n">topic</span><span class="p">}]})</span>

    <span class="k">def</span> <span class="nf">add_quote_document</span><span class="p">(</span><span class="n">self</span><span class="p">,</span> <span class="n">query</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">quote</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">topic</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">timestamp</span><span class="p">:</span> <span class="nb">int</span><span class="p">,</span> <span class="n">source</span><span class="p">:</span> <span class="nb">str</span><span class="p">):</span>
        <span class="n">self</span><span class="p">.</span><span class="n">embed_fn</span><span class="p">.</span><span class="n">document_mode</span> <span class="o">=</span> <span class="bp">True</span> <span class="c1"># Switch to document mode.
</span>        <span class="nf">tqdm</span><span class="p">(</span><span class="n">self</span><span class="p">.</span><span class="n">db</span><span class="p">.</span><span class="nf">add</span><span class="p">(</span><span class="n">ids</span><span class="o">=</span><span class="nf">str</span><span class="p">(</span><span class="n">self</span><span class="p">.</span><span class="n">db</span><span class="p">.</span><span class="nf">count</span><span class="p">()),</span> 
                             <span class="n">documents</span><span class="o">=</span><span class="p">[</span><span class="n">quote</span><span class="p">],</span> 
                             <span class="n">metadatas</span><span class="o">=</span><span class="p">[{</span><span class="sh">"</span><span class="s">source</span><span class="sh">"</span><span class="p">:</span> <span class="n">source</span><span class="p">,</span> <span class="sh">"</span><span class="s">topic</span><span class="sh">"</span><span class="p">:</span> <span class="n">topic</span><span class="p">,</span> <span class="sh">"</span><span class="s">timestamp</span><span class="sh">"</span><span class="p">:</span> <span class="n">timestamp</span><span class="p">}]),</span> 
             <span class="n">desc</span><span class="o">=</span><span class="sh">"</span><span class="s">Generate quote embedding</span><span class="sh">"</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">get_api_documents</span><span class="p">(</span><span class="n">self</span><span class="p">,</span> <span class="n">query</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">topic</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">source</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="sh">"</span><span class="s">add_api_document</span><span class="sh">"</span><span class="p">,</span> 
                          <span class="n">meta_opt</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">list</span><span class="p">[</span><span class="nb">dict</span><span class="p">]]</span> <span class="o">=</span> <span class="bp">None</span><span class="p">):</span>
        <span class="n">where</span> <span class="o">=</span> <span class="p">[{</span><span class="sh">"</span><span class="s">source</span><span class="sh">"</span><span class="p">:</span> <span class="n">source</span><span class="p">},</span> <span class="p">{</span><span class="sh">"</span><span class="s">topic</span><span class="sh">"</span><span class="p">:</span> <span class="n">topic</span><span class="p">}]</span>
        <span class="k">if</span> <span class="n">meta_opt</span> <span class="ow">is</span> <span class="bp">None</span><span class="p">:</span>
            <span class="k">return</span> <span class="n">self</span><span class="p">.</span><span class="nf">get_documents_list</span><span class="p">(</span><span class="n">query</span><span class="p">,</span> <span class="n">where</span><span class="o">=</span><span class="p">{</span><span class="sh">"</span><span class="s">$and</span><span class="sh">"</span><span class="p">:</span> <span class="n">where</span><span class="p">})</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="k">for</span> <span class="n">meta</span> <span class="ow">in</span> <span class="n">meta_opt</span><span class="p">:</span>
                <span class="k">for</span> <span class="n">k</span><span class="p">,</span><span class="n">v</span> <span class="ow">in</span> <span class="n">meta</span><span class="p">.</span><span class="nf">items</span><span class="p">():</span>
                    <span class="n">where</span><span class="p">.</span><span class="nf">append</span><span class="p">({</span><span class="n">k</span><span class="p">:</span> <span class="n">v</span><span class="p">})</span>
            <span class="k">return</span> <span class="n">self</span><span class="p">.</span><span class="nf">get_documents_list</span><span class="p">(</span><span class="n">query</span><span class="p">,</span> <span class="n">where</span><span class="o">=</span><span class="p">{</span><span class="sh">"</span><span class="s">$and</span><span class="sh">"</span><span class="p">:</span> <span class="n">where</span><span class="p">})</span>

    <span class="k">def</span> <span class="nf">query_api_documents</span><span class="p">(</span><span class="n">self</span><span class="p">,</span> <span class="n">query</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">topic</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">source</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="sh">"</span><span class="s">add_api_document</span><span class="sh">"</span><span class="p">):</span>
        <span class="k">return</span> <span class="n">self</span><span class="p">.</span><span class="nf">generate_answer</span><span class="p">(</span><span class="n">query</span><span class="p">,</span> <span class="n">where</span><span class="o">=</span><span class="p">{</span><span class="sh">"</span><span class="s">$and</span><span class="sh">"</span><span class="p">:</span> <span class="p">[{</span><span class="sh">"</span><span class="s">source</span><span class="sh">"</span><span class="p">:</span> <span class="n">source</span><span class="p">},</span> <span class="p">{</span><span class="sh">"</span><span class="s">topic</span><span class="sh">"</span><span class="p">:</span> <span class="n">topic</span><span class="p">}]})</span>

    <span class="k">def</span> <span class="nf">add_grounded_document</span><span class="p">(</span><span class="n">self</span><span class="p">,</span> <span class="n">query</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">topic</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">result</span><span class="p">):</span>
        <span class="n">self</span><span class="p">.</span><span class="n">embed_fn</span><span class="p">.</span><span class="n">document_mode</span> <span class="o">=</span> <span class="bp">True</span> <span class="c1"># Switch to document mode.
</span>        <span class="n">chunks</span> <span class="o">=</span> <span class="n">result</span><span class="p">.</span><span class="n">candidates</span><span class="p">[</span><span class="mi">0</span><span class="p">].</span><span class="n">grounding_metadata</span><span class="p">.</span><span class="n">grounding_chunks</span>
        <span class="n">supports</span> <span class="o">=</span> <span class="n">result</span><span class="p">.</span><span class="n">candidates</span><span class="p">[</span><span class="mi">0</span><span class="p">].</span><span class="n">grounding_metadata</span><span class="p">.</span><span class="n">grounding_supports</span>
        <span class="k">if</span> <span class="n">supports</span> <span class="ow">is</span> <span class="ow">not</span> <span class="bp">None</span><span class="p">:</span> <span class="c1"># Only add grounded documents which have supports
</span>            <span class="n">grounded_text</span> <span class="o">=</span> <span class="p">[</span><span class="sa">f</span><span class="sh">"</span><span class="si">{</span><span class="n">s</span><span class="p">.</span><span class="n">segment</span><span class="p">.</span><span class="n">text</span><span class="si">}</span><span class="sh">"</span> <span class="k">for</span> <span class="n">s</span> <span class="ow">in</span> <span class="n">supports</span><span class="p">]</span>
            <span class="n">source</span> <span class="o">=</span> <span class="p">[</span><span class="sa">f</span><span class="sh">"</span><span class="si">{</span><span class="n">c</span><span class="p">.</span><span class="n">web</span><span class="p">.</span><span class="n">title</span><span class="si">}</span><span class="sh">"</span> <span class="k">for</span> <span class="n">c</span> <span class="ow">in</span> <span class="n">chunks</span><span class="p">]</span>
            <span class="n">score</span> <span class="o">=</span> <span class="p">[</span><span class="sa">f</span><span class="sh">"</span><span class="si">{</span><span class="n">s</span><span class="p">.</span><span class="n">confidence_scores</span><span class="si">}</span><span class="sh">"</span> <span class="k">for</span> <span class="n">s</span> <span class="ow">in</span> <span class="n">supports</span><span class="p">]</span>
            <span class="nf">tqdm</span><span class="p">(</span><span class="n">self</span><span class="p">.</span><span class="n">db</span><span class="p">.</span><span class="nf">add</span><span class="p">(</span><span class="n">ids</span><span class="o">=</span><span class="nf">str</span><span class="p">(</span><span class="n">self</span><span class="p">.</span><span class="n">db</span><span class="p">.</span><span class="nf">count</span><span class="p">()),</span>
                             <span class="n">documents</span><span class="o">=</span><span class="n">json</span><span class="p">.</span><span class="nf">dumps</span><span class="p">(</span><span class="n">grounded_text</span><span class="p">),</span>
                             <span class="n">metadatas</span><span class="o">=</span><span class="p">[{</span><span class="sh">"</span><span class="s">source</span><span class="sh">"</span><span class="p">:</span> <span class="sh">"</span><span class="s">, </span><span class="sh">"</span><span class="p">.</span><span class="nf">join</span><span class="p">(</span><span class="n">source</span><span class="p">),</span>
                                         <span class="sh">"</span><span class="s">confidence_score</span><span class="sh">"</span><span class="p">:</span> <span class="sh">"</span><span class="s">, </span><span class="sh">"</span><span class="p">.</span><span class="nf">join</span><span class="p">(</span><span class="n">score</span><span class="p">),</span>
                                         <span class="sh">"</span><span class="s">topic</span><span class="sh">"</span><span class="p">:</span> <span class="n">topic</span><span class="p">,</span>
                                         <span class="sh">"</span><span class="s">question</span><span class="sh">"</span><span class="p">:</span> <span class="n">query</span><span class="p">}]),</span>
                 <span class="n">desc</span><span class="o">=</span><span class="sh">"</span><span class="s">Generate grounding embedding</span><span class="sh">"</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">get_grounding_documents</span><span class="p">(</span><span class="n">self</span><span class="p">,</span> <span class="n">query</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">topic</span><span class="p">:</span> <span class="nb">str</span><span class="p">):</span>
        <span class="n">self</span><span class="p">.</span><span class="n">embed_fn</span><span class="p">.</span><span class="n">document_mode</span> <span class="o">=</span> <span class="bp">False</span> <span class="c1"># Switch to query mode.
</span>        <span class="k">return</span> <span class="n">self</span><span class="p">.</span><span class="nf">stored_result</span><span class="p">(</span><span class="n">self</span><span class="p">.</span><span class="n">db</span><span class="p">.</span><span class="nf">get</span><span class="p">(</span><span class="n">where</span><span class="o">=</span><span class="p">{</span><span class="sh">"</span><span class="s">$and</span><span class="sh">"</span><span class="p">:</span> <span class="p">[{</span><span class="sh">"</span><span class="s">question</span><span class="sh">"</span><span class="p">:</span> <span class="n">query</span><span class="p">},</span> <span class="p">{</span><span class="sh">"</span><span class="s">topic</span><span class="sh">"</span><span class="p">:</span> <span class="n">topic</span><span class="p">}]}))</span>
            
    <span class="k">def</span> <span class="nf">add_wiki_documents</span><span class="p">(</span><span class="n">self</span><span class="p">,</span> <span class="n">title</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">wiki_chunks</span><span class="p">:</span> <span class="nb">list</span><span class="p">):</span>
        <span class="n">self</span><span class="p">.</span><span class="n">embed_fn</span><span class="p">.</span><span class="n">document_mode</span> <span class="o">=</span> <span class="bp">True</span> <span class="c1"># Switch to document mode.
</span>        <span class="n">result</span> <span class="o">=</span> <span class="n">self</span><span class="p">.</span><span class="nf">get_wiki_documents</span><span class="p">(</span><span class="n">title</span><span class="p">)</span>
        <span class="k">if</span> <span class="nf">len</span><span class="p">(</span><span class="n">result</span><span class="p">)</span> <span class="o">==</span> <span class="mi">0</span><span class="p">:</span>
            <span class="n">ids</span> <span class="o">=</span> <span class="nf">list</span><span class="p">(</span><span class="nf">map</span><span class="p">(</span><span class="nb">str</span><span class="p">,</span> <span class="nf">range</span><span class="p">(</span><span class="n">self</span><span class="p">.</span><span class="n">db</span><span class="p">.</span><span class="nf">count</span><span class="p">(),</span> <span class="n">self</span><span class="p">.</span><span class="n">db</span><span class="p">.</span><span class="nf">count</span><span class="p">()</span><span class="o">+</span><span class="nf">len</span><span class="p">(</span><span class="n">wiki_chunks</span><span class="p">))))</span>
            <span class="n">metas</span><span class="o">=</span><span class="p">[{</span><span class="sh">"</span><span class="s">title</span><span class="sh">"</span><span class="p">:</span> <span class="n">title</span><span class="p">,</span> <span class="sh">"</span><span class="s">source</span><span class="sh">"</span><span class="p">:</span> <span class="sh">"</span><span class="s">add_wiki_documents</span><span class="sh">"</span><span class="p">}]</span><span class="o">*</span><span class="nf">len</span><span class="p">(</span><span class="n">wiki_chunks</span><span class="p">)</span>
            <span class="nf">tqdm</span><span class="p">(</span><span class="n">self</span><span class="p">.</span><span class="n">db</span><span class="p">.</span><span class="nf">add</span><span class="p">(</span><span class="n">ids</span><span class="o">=</span><span class="n">ids</span><span class="p">,</span> <span class="n">documents</span><span class="o">=</span><span class="n">wiki_chunks</span><span class="p">,</span> <span class="n">metadatas</span><span class="o">=</span><span class="n">metas</span><span class="p">),</span> <span class="n">desc</span><span class="o">=</span><span class="sh">"</span><span class="s">Generate wiki embeddings</span><span class="sh">"</span><span class="p">)</span>

    <span class="nd">@retry.Retry</span><span class="p">(</span>
        <span class="n">predicate</span><span class="o">=</span><span class="n">is_retriable</span><span class="p">,</span>
        <span class="n">initial</span><span class="o">=</span><span class="mf">2.0</span><span class="p">,</span>
        <span class="n">maximum</span><span class="o">=</span><span class="mf">64.0</span><span class="p">,</span>
        <span class="n">multiplier</span><span class="o">=</span><span class="mf">2.0</span><span class="p">,</span>
        <span class="n">timeout</span><span class="o">=</span><span class="mi">600</span><span class="p">,</span>
    <span class="p">)</span>
    <span class="k">def</span> <span class="nf">generate_with_wiki_passages</span><span class="p">(</span><span class="n">self</span><span class="p">,</span> <span class="n">query</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">title</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">passages</span><span class="p">:</span> <span class="nb">list</span><span class="p">[</span><span class="nb">str</span><span class="p">]):</span>
        <span class="k">return</span> <span class="n">self</span><span class="p">.</span><span class="nf">generate_answer</span><span class="p">(</span><span class="n">query</span><span class="p">,</span> <span class="n">where</span><span class="o">=</span><span class="p">{</span><span class="sh">"</span><span class="s">title</span><span class="sh">"</span><span class="p">:</span> <span class="n">title</span><span class="p">},</span> <span class="n">passages</span><span class="o">=</span><span class="n">passages</span><span class="p">)</span>
    
    <span class="k">def</span> <span class="nf">get_wiki_documents</span><span class="p">(</span><span class="n">self</span><span class="p">,</span> <span class="n">title</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="bp">None</span><span class="p">):</span>
        <span class="n">self</span><span class="p">.</span><span class="n">embed_fn</span><span class="p">.</span><span class="n">document_mode</span> <span class="o">=</span> <span class="bp">False</span> <span class="c1"># Switch to query mode.
</span>        <span class="k">if</span> <span class="n">title</span> <span class="ow">is</span> <span class="bp">None</span><span class="p">:</span>
            <span class="k">return</span> <span class="n">self</span><span class="p">.</span><span class="nf">stored_result</span><span class="p">(</span><span class="n">self</span><span class="p">.</span><span class="n">db</span><span class="p">.</span><span class="nf">get</span><span class="p">(</span><span class="n">where</span><span class="o">=</span><span class="p">{</span><span class="sh">"</span><span class="s">source</span><span class="sh">"</span><span class="p">:</span> <span class="sh">"</span><span class="s">add_wiki_document</span><span class="sh">"</span><span class="p">}))</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="k">return</span> <span class="n">self</span><span class="p">.</span><span class="nf">stored_result</span><span class="p">(</span><span class="n">self</span><span class="p">.</span><span class="n">db</span><span class="p">.</span><span class="nf">get</span><span class="p">(</span><span class="n">where</span><span class="o">=</span><span class="p">{</span><span class="sh">"</span><span class="s">title</span><span class="sh">"</span><span class="p">:</span> <span class="n">title</span><span class="p">}))</span>

    <span class="nd">@retry.Retry</span><span class="p">(</span>
        <span class="n">predicate</span><span class="o">=</span><span class="n">is_retriable</span><span class="p">,</span>
        <span class="n">initial</span><span class="o">=</span><span class="mf">2.0</span><span class="p">,</span>
        <span class="n">maximum</span><span class="o">=</span><span class="mf">64.0</span><span class="p">,</span>
        <span class="n">multiplier</span><span class="o">=</span><span class="mf">2.0</span><span class="p">,</span>
        <span class="n">timeout</span><span class="o">=</span><span class="mi">600</span><span class="p">,</span>
    <span class="p">)</span>
    <span class="k">def</span> <span class="nf">get_documents_list</span><span class="p">(</span><span class="n">self</span><span class="p">,</span> <span class="n">query</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">max_sources</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">5000</span><span class="p">,</span> <span class="n">where</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">dict</span><span class="p">]</span> <span class="o">=</span> <span class="bp">None</span><span class="p">):</span>
        <span class="n">self</span><span class="p">.</span><span class="n">embed_fn</span><span class="p">.</span><span class="n">document_mode</span> <span class="o">=</span> <span class="bp">False</span> <span class="c1"># Switch to query mode.
</span>        <span class="k">return</span> <span class="n">self</span><span class="p">.</span><span class="nf">stored_result</span><span class="p">(</span>
            <span class="n">self</span><span class="p">.</span><span class="n">db</span><span class="p">.</span><span class="nf">query</span><span class="p">(</span><span class="n">query_texts</span><span class="o">=</span><span class="p">[</span><span class="n">query</span><span class="p">],</span> 
                          <span class="n">n_results</span><span class="o">=</span><span class="n">max_sources</span><span class="p">,</span> 
                          <span class="n">where</span><span class="o">=</span><span class="n">where</span><span class="p">),</span> 
            <span class="n">is_query</span> <span class="o">=</span> <span class="bp">True</span><span class="p">)</span>

    <span class="nd">@retry.Retry</span><span class="p">(</span>
        <span class="n">predicate</span><span class="o">=</span><span class="n">is_retriable</span><span class="p">,</span>
        <span class="n">initial</span><span class="o">=</span><span class="mf">2.0</span><span class="p">,</span>
        <span class="n">maximum</span><span class="o">=</span><span class="mf">64.0</span><span class="p">,</span>
        <span class="n">multiplier</span><span class="o">=</span><span class="mf">2.0</span><span class="p">,</span>
        <span class="n">timeout</span><span class="o">=</span><span class="mi">600</span><span class="p">,</span>
    <span class="p">)</span>
    <span class="k">def</span> <span class="nf">get_exchanges_csv</span><span class="p">(</span><span class="n">self</span><span class="p">,</span> <span class="n">query</span><span class="p">:</span> <span class="nb">str</span><span class="p">):</span>
        <span class="k">return</span> <span class="n">self</span><span class="p">.</span><span class="nf">generate_answer</span><span class="p">(</span><span class="n">query</span><span class="p">,</span> <span class="n">max_sources</span><span class="o">=</span><span class="mi">100</span><span class="p">,</span> <span class="n">where</span><span class="o">=</span><span class="p">{</span><span class="sh">"</span><span class="s">source</span><span class="sh">"</span><span class="p">:</span> <span class="sh">"</span><span class="s">exchanges.csv</span><span class="sh">"</span><span class="p">})</span>

    <span class="nd">@retry.Retry</span><span class="p">(</span>
        <span class="n">predicate</span><span class="o">=</span><span class="n">is_retriable</span><span class="p">,</span>
        <span class="n">initial</span><span class="o">=</span><span class="mf">2.0</span><span class="p">,</span>
        <span class="n">maximum</span><span class="o">=</span><span class="mf">64.0</span><span class="p">,</span>
        <span class="n">multiplier</span><span class="o">=</span><span class="mf">2.0</span><span class="p">,</span>
        <span class="n">timeout</span><span class="o">=</span><span class="mi">600</span><span class="p">,</span>
    <span class="p">)</span>
    <span class="k">def</span> <span class="nf">generate_answer</span><span class="p">(</span><span class="n">self</span><span class="p">,</span> <span class="n">query</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">max_sources</span><span class="p">:</span> <span class="nb">int</span> <span class="o">=</span> <span class="mi">10</span><span class="p">,</span> 
                        <span class="n">where</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">dict</span><span class="p">]</span> <span class="o">=</span> <span class="bp">None</span><span class="p">,</span> <span class="n">passages</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">list</span><span class="p">[</span><span class="nb">str</span><span class="p">]]</span> <span class="o">=</span> <span class="bp">None</span><span class="p">):</span>
        <span class="n">stored</span> <span class="o">=</span> <span class="n">self</span><span class="p">.</span><span class="nf">get_documents_list</span><span class="p">(</span><span class="n">query</span><span class="p">,</span> <span class="n">max_sources</span><span class="p">,</span> <span class="n">where</span><span class="p">)</span>
        <span class="n">query_oneline</span> <span class="o">=</span> <span class="n">query</span><span class="p">.</span><span class="nf">replace</span><span class="p">(</span><span class="sh">"</span><span class="se">\n</span><span class="sh">"</span><span class="p">,</span> <span class="sh">"</span><span class="s"> </span><span class="sh">"</span><span class="p">)</span>
        <span class="n">prompt</span> <span class="o">=</span> <span class="sa">f</span><span class="sh">"""</span><span class="s">You</span><span class="sh">'</span><span class="s">re an expert writer. You understand how to interpret html and markdown. You will accept the
        question below and answer based only on the passages. Never mention the passages in your answers. Be sure to 
        respond in concise sentences. Include all relevant background information when possible. If a passage is not 
        relevant to the answer you must ignore it. If no passage answers the question respond with: I don</span><span class="sh">'</span><span class="s">t know.

        QUESTION: </span><span class="si">{</span><span class="n">query_oneline</span><span class="si">}</span><span class="s">
        
        </span><span class="sh">"""</span>
        <span class="c1"># Add the retrieved documents to the prompt.
</span>        <span class="n">stored_docs</span> <span class="o">=</span> <span class="p">[</span><span class="n">passage</span><span class="p">.</span><span class="n">docs</span> <span class="k">for</span> <span class="n">passage</span> <span class="ow">in</span> <span class="n">stored</span><span class="p">]</span>
        <span class="k">for</span> <span class="n">passage</span> <span class="ow">in</span> <span class="n">stored_docs</span> <span class="k">if</span> <span class="n">passages</span> <span class="ow">is</span> <span class="bp">None</span> <span class="k">else</span> <span class="n">stored_docs</span> <span class="o">+</span> <span class="n">passages</span><span class="p">:</span>
            <span class="n">passage_oneline</span> <span class="o">=</span> <span class="n">passage</span><span class="p">.</span><span class="nf">replace</span><span class="p">(</span><span class="sh">"</span><span class="se">\n</span><span class="sh">"</span><span class="p">,</span> <span class="sh">"</span><span class="s"> </span><span class="sh">"</span><span class="p">)</span>
            <span class="n">prompt</span> <span class="o">+=</span> <span class="sa">f</span><span class="sh">"</span><span class="s">PASSAGE: </span><span class="si">{</span><span class="n">passage_oneline</span><span class="si">}</span><span class="se">\n</span><span class="sh">"</span>
        <span class="c1"># Generate the response.
</span>        <span class="n">response</span> <span class="o">=</span> <span class="n">api</span><span class="p">.</span><span class="nf">retriable</span><span class="p">(</span>
            <span class="n">self</span><span class="p">.</span><span class="n">client</span><span class="p">.</span><span class="n">models</span><span class="p">.</span><span class="n">generate_content</span><span class="p">,</span>
            <span class="n">model</span><span class="o">=</span><span class="nf">api</span><span class="p">(</span><span class="n">Api</span><span class="p">.</span><span class="n">Model</span><span class="p">.</span><span class="n">GEN</span><span class="p">),</span>
            <span class="n">config</span><span class="o">=</span><span class="n">self</span><span class="p">.</span><span class="n">config_temp</span><span class="p">,</span>
            <span class="n">contents</span><span class="o">=</span><span class="n">prompt</span><span class="p">)</span>
        <span class="c1"># Check for generated code and store in memory.
</span>        <span class="n">content</span> <span class="o">=</span> <span class="n">response</span><span class="p">.</span><span class="n">candidates</span><span class="p">[</span><span class="mi">0</span><span class="p">].</span><span class="n">content</span>
        <span class="k">if</span> <span class="nf">len</span><span class="p">(</span><span class="n">content</span><span class="p">.</span><span class="n">parts</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mi">1</span> <span class="ow">and</span> <span class="n">content</span><span class="p">.</span><span class="n">parts</span><span class="p">[</span><span class="mi">0</span><span class="p">].</span><span class="n">executable_code</span><span class="p">:</span>
            <span class="n">memory</span><span class="p">.</span><span class="nf">append_code</span><span class="p">(</span><span class="n">prompt</span><span class="p">,</span> <span class="n">content</span><span class="p">.</span><span class="n">parts</span><span class="p">)</span>
        <span class="k">return</span> <span class="n">response</span>

    <span class="k">def</span> <span class="nf">stored_result</span><span class="p">(</span><span class="n">self</span><span class="p">,</span> <span class="n">result</span><span class="p">,</span> <span class="n">is_query</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="bp">False</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">list</span><span class="p">[</span><span class="n">VectorStoreResult</span><span class="p">]:</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="n">results</span> <span class="o">=</span> <span class="p">[]</span>
            <span class="k">if</span> <span class="nf">len</span><span class="p">(</span><span class="n">result</span><span class="p">[</span><span class="sh">"</span><span class="s">documents</span><span class="sh">"</span><span class="p">])</span> <span class="o">==</span> <span class="mi">0</span><span class="p">:</span>
                <span class="k">return</span> <span class="n">results</span>
            <span class="k">if</span> <span class="nf">isinstance</span><span class="p">(</span><span class="n">result</span><span class="p">[</span><span class="sh">"</span><span class="s">documents</span><span class="sh">"</span><span class="p">][</span><span class="mi">0</span><span class="p">],</span> <span class="nb">list</span><span class="p">):</span>
                <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nf">range</span><span class="p">(</span><span class="nf">len</span><span class="p">(</span><span class="n">result</span><span class="p">[</span><span class="sh">"</span><span class="s">documents</span><span class="sh">"</span><span class="p">][</span><span class="mi">0</span><span class="p">])):</span>
                    <span class="n">obj</span> <span class="o">=</span> <span class="nc">VectorStoreResult</span><span class="p">(</span><span class="n">docs</span><span class="o">=</span><span class="n">result</span><span class="p">[</span><span class="sh">"</span><span class="s">documents</span><span class="sh">"</span><span class="p">][</span><span class="mi">0</span><span class="p">][</span><span class="n">i</span><span class="p">],</span>
                                            <span class="n">dist</span><span class="o">=</span><span class="n">result</span><span class="p">[</span><span class="sh">"</span><span class="s">distances</span><span class="sh">"</span><span class="p">][</span><span class="mi">0</span><span class="p">][</span><span class="n">i</span><span class="p">]</span> <span class="k">if</span> <span class="n">is_query</span> <span class="k">else</span> <span class="bp">None</span><span class="p">,</span>
                                            <span class="n">meta</span><span class="o">=</span><span class="n">result</span><span class="p">[</span><span class="sh">"</span><span class="s">metadatas</span><span class="sh">"</span><span class="p">][</span><span class="mi">0</span><span class="p">][</span><span class="n">i</span><span class="p">],</span>
                                            <span class="n">store_id</span><span class="o">=</span><span class="n">result</span><span class="p">[</span><span class="sh">"</span><span class="s">ids</span><span class="sh">"</span><span class="p">][</span><span class="mi">0</span><span class="p">][</span><span class="n">i</span><span class="p">])</span>
                    <span class="n">results</span><span class="p">.</span><span class="nf">append</span><span class="p">(</span><span class="n">obj</span><span class="p">)</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="n">results</span><span class="p">.</span><span class="nf">append</span><span class="p">(</span>
                    <span class="nc">VectorStoreResult</span><span class="p">(</span><span class="n">docs</span><span class="o">=</span><span class="n">result</span><span class="p">[</span><span class="sh">"</span><span class="s">documents</span><span class="sh">"</span><span class="p">][</span><span class="mi">0</span><span class="p">],</span>
                                      <span class="n">dist</span><span class="o">=</span><span class="n">result</span><span class="p">[</span><span class="sh">"</span><span class="s">distances</span><span class="sh">"</span><span class="p">][</span><span class="mi">0</span><span class="p">]</span> <span class="k">if</span> <span class="n">is_query</span> <span class="k">else</span> <span class="bp">None</span><span class="p">,</span>
                                      <span class="n">meta</span><span class="o">=</span><span class="n">result</span><span class="p">[</span><span class="sh">"</span><span class="s">metadatas</span><span class="sh">"</span><span class="p">][</span><span class="mi">0</span><span class="p">],</span>
                                      <span class="n">store_id</span><span class="o">=</span><span class="n">result</span><span class="p">[</span><span class="sh">"</span><span class="s">ids</span><span class="sh">"</span><span class="p">][</span><span class="mi">0</span><span class="p">]))</span>
            <span class="k">return</span> <span class="n">results</span>
        <span class="k">except</span> <span class="nb">Exception</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
            <span class="k">raise</span> <span class="n">e</span>
</code></pre></div></div>

<h3 id="wiki-grounding">Wiki Grounding</h3>

<div class="language-python highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="c1"># Define tool: wiki-grounding generation.
# - using gemini-2.0-flash for response generation
# - using a RAG-implementation to store groundings
# - create new groundings by similarity to topic
# - retrieve existing groundings by similarity to topic
</span><span class="k">class</span> <span class="nc">WikiGroundingGenerator</span><span class="p">:</span>   
    <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="n">self</span><span class="p">,</span> <span class="n">genai_client</span><span class="p">,</span> <span class="n">rag_impl</span><span class="p">):</span>
        <span class="n">self</span><span class="p">.</span><span class="n">client</span> <span class="o">=</span> <span class="n">genai_client</span>
        <span class="n">self</span><span class="p">.</span><span class="n">rag</span> <span class="o">=</span> <span class="n">rag_impl</span>
        <span class="k">with</span> <span class="n">warnings</span><span class="p">.</span><span class="nf">catch_warnings</span><span class="p">():</span>
            <span class="n">warnings</span><span class="p">.</span><span class="nf">simplefilter</span><span class="p">(</span><span class="sh">"</span><span class="s">ignore</span><span class="sh">"</span><span class="p">)</span> <span class="c1"># suppress beta-warning
</span>            <span class="n">self</span><span class="p">.</span><span class="n">splitter</span> <span class="o">=</span> <span class="nc">HTMLSemanticPreservingSplitter</span><span class="p">(</span>
                <span class="n">headers_to_split_on</span><span class="o">=</span><span class="p">[(</span><span class="sh">"</span><span class="s">h2</span><span class="sh">"</span><span class="p">,</span> <span class="sh">"</span><span class="s">Main Topic</span><span class="sh">"</span><span class="p">),</span> <span class="p">(</span><span class="sh">"</span><span class="s">h3</span><span class="sh">"</span><span class="p">,</span> <span class="sh">"</span><span class="s">Sub Topic</span><span class="sh">"</span><span class="p">)],</span>
                <span class="n">separators</span><span class="o">=</span><span class="p">[</span><span class="sh">"</span><span class="se">\n\n</span><span class="sh">"</span><span class="p">,</span> <span class="sh">"</span><span class="se">\n</span><span class="sh">"</span><span class="p">,</span> <span class="sh">"</span><span class="s">. </span><span class="sh">"</span><span class="p">,</span> <span class="sh">"</span><span class="s">! </span><span class="sh">"</span><span class="p">,</span> <span class="sh">"</span><span class="s">? </span><span class="sh">"</span><span class="p">],</span>
                <span class="n">max_chunk_size</span><span class="o">=</span><span class="n">Api</span><span class="p">.</span><span class="n">Const</span><span class="p">.</span><span class="nc">ChunkMax</span><span class="p">(),</span>
                <span class="n">chunk_overlap</span><span class="o">=</span><span class="mi">50</span><span class="p">,</span>
                <span class="n">preserve_links</span><span class="o">=</span><span class="bp">True</span><span class="p">,</span>
                <span class="n">preserve_images</span><span class="o">=</span><span class="bp">True</span><span class="p">,</span>
                <span class="n">preserve_videos</span><span class="o">=</span><span class="bp">True</span><span class="p">,</span>
                <span class="n">preserve_audio</span><span class="o">=</span><span class="bp">True</span><span class="p">,</span>
                <span class="n">elements_to_preserve</span><span class="o">=</span><span class="p">[</span><span class="sh">"</span><span class="s">table</span><span class="sh">"</span><span class="p">,</span> <span class="sh">"</span><span class="s">ul</span><span class="sh">"</span><span class="p">,</span> <span class="sh">"</span><span class="s">ol</span><span class="sh">"</span><span class="p">,</span> <span class="sh">"</span><span class="s">code</span><span class="sh">"</span><span class="p">],</span>
                <span class="n">denylist_tags</span><span class="o">=</span><span class="p">[</span><span class="sh">"</span><span class="s">script</span><span class="sh">"</span><span class="p">,</span> <span class="sh">"</span><span class="s">style</span><span class="sh">"</span><span class="p">,</span> <span class="sh">"</span><span class="s">head</span><span class="sh">"</span><span class="p">],</span>
                <span class="n">custom_handlers</span><span class="o">=</span><span class="p">{</span><span class="sh">"</span><span class="s">code</span><span class="sh">"</span><span class="p">:</span> <span class="n">self</span><span class="p">.</span><span class="n">code_handler</span><span class="p">},</span>
            <span class="p">)</span>

    <span class="k">def</span> <span class="nf">generate_answer</span><span class="p">(</span><span class="n">self</span><span class="p">,</span> <span class="n">query</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">topic</span><span class="p">:</span> <span class="nb">str</span><span class="p">):</span>
        <span class="n">stored</span> <span class="o">=</span> <span class="n">self</span><span class="p">.</span><span class="n">rag</span><span class="p">.</span><span class="nf">get_wiki_documents</span><span class="p">(</span><span class="n">topic</span><span class="p">)</span>
        <span class="k">if</span> <span class="nf">len</span><span class="p">(</span><span class="n">stored</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mi">0</span><span class="p">:</span>
            <span class="k">return</span> <span class="n">self</span><span class="p">.</span><span class="n">rag</span><span class="p">.</span><span class="nf">generate_with_wiki_passages</span><span class="p">(</span><span class="n">query</span><span class="p">,</span> <span class="n">topic</span><span class="p">,</span> <span class="p">[</span><span class="n">chunk</span><span class="p">.</span><span class="n">docs</span> <span class="k">for</span> <span class="n">chunk</span> <span class="ow">in</span> <span class="n">stored</span><span class="p">]).</span><span class="n">text</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">pages</span> <span class="o">=</span> <span class="n">wikipedia</span><span class="p">.</span><span class="nf">search</span><span class="p">(</span><span class="n">topic</span> <span class="o">+</span> <span class="sh">"</span><span class="s"> company</span><span class="sh">"</span><span class="p">)</span>
            <span class="k">if</span> <span class="nf">len</span><span class="p">(</span><span class="n">pages</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mi">0</span><span class="p">:</span>
                <span class="n">p_topic_match</span> <span class="o">=</span> <span class="mf">0.80</span>
                <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nf">range</span><span class="p">(</span><span class="nf">len</span><span class="p">(</span><span class="n">pages</span><span class="p">)):</span>
                    <span class="k">if</span> <span class="nf">tqdm</span><span class="p">(</span><span class="n">api</span><span class="p">.</span><span class="nf">similarity</span><span class="p">([</span><span class="n">topic</span> <span class="o">+</span> <span class="sh">"</span><span class="s"> company</span><span class="sh">"</span><span class="p">,</span> <span class="n">pages</span><span class="p">[</span><span class="n">i</span><span class="p">]])</span> <span class="o">&gt;</span> <span class="n">p_topic_match</span><span class="p">,</span> 
                            <span class="n">desc</span><span class="o">=</span> <span class="sh">"</span><span class="s">Score wiki search by similarity to topic</span><span class="sh">"</span><span class="p">):</span>
                        <span class="n">page_html</span> <span class="o">=</span> <span class="n">Api</span><span class="p">.</span><span class="nf">get</span><span class="p">(</span><span class="sa">f</span><span class="sh">"</span><span class="s">https://en.wikipedia.org/wiki/</span><span class="si">{</span><span class="n">pages</span><span class="p">[</span><span class="n">i</span><span class="p">]</span><span class="si">}</span><span class="sh">"</span><span class="p">)</span>
                        <span class="n">chunks</span> <span class="o">=</span> <span class="p">[</span><span class="n">chunk</span><span class="p">.</span><span class="n">page_content</span> <span class="k">for</span> <span class="n">chunk</span> <span class="ow">in</span> <span class="n">self</span><span class="p">.</span><span class="n">splitter</span><span class="p">.</span><span class="nf">split_text</span><span class="p">(</span><span class="n">page_html</span><span class="p">)]</span>
                        <span class="n">self</span><span class="p">.</span><span class="n">rag</span><span class="p">.</span><span class="nf">add_wiki_documents</span><span class="p">(</span><span class="n">topic</span><span class="p">,</span> <span class="n">chunks</span><span class="p">)</span>
                        <span class="k">return</span> <span class="n">self</span><span class="p">.</span><span class="n">rag</span><span class="p">.</span><span class="nf">generate_with_wiki_passages</span><span class="p">(</span><span class="n">query</span><span class="p">,</span> <span class="n">topic</span><span class="p">,</span> <span class="n">chunks</span><span class="p">).</span><span class="n">text</span>
            <span class="k">return</span> <span class="n">Api</span><span class="p">.</span><span class="n">Const</span><span class="p">.</span><span class="nc">Stop</span><span class="p">()</span>

    <span class="k">def</span> <span class="nf">code_handler</span><span class="p">(</span><span class="n">self</span><span class="p">,</span> <span class="n">element</span><span class="p">:</span> <span class="n">Tag</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="n">data_lang</span> <span class="o">=</span> <span class="n">element</span><span class="p">.</span><span class="nf">get</span><span class="p">(</span><span class="sh">"</span><span class="s">data-lang</span><span class="sh">"</span><span class="p">)</span>
        <span class="n">code_format</span> <span class="o">=</span> <span class="sa">f</span><span class="sh">"</span><span class="s">&lt;code:</span><span class="si">{</span><span class="n">data_lang</span><span class="si">}</span><span class="s">&gt;</span><span class="si">{</span><span class="n">element</span><span class="p">.</span><span class="nf">get_text</span><span class="p">()</span><span class="si">}</span><span class="s">&lt;/code&gt;</span><span class="sh">"</span>
        <span class="k">return</span> <span class="n">code_format</span>
</code></pre></div></div>

<h3 id="search-grounding">Search Grounding</h3>

<div class="language-python highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="c1"># Define tool: search-grounding generation.
# - using gemini-2.0-flash with GoogleSearch tool for response generation
# - using a RAG-implementation to store groundings
# - create new groundings by exact match to topic
# - retrieve existing groundings by similarity to topic
</span><span class="k">class</span> <span class="nc">SearchGroundingGenerator</span><span class="p">:</span>
    <span class="n">config_ground</span> <span class="o">=</span> <span class="n">types</span><span class="p">.</span><span class="nc">GenerateContentConfig</span><span class="p">(</span>
        <span class="n">tools</span><span class="o">=</span><span class="p">[</span><span class="n">types</span><span class="p">.</span><span class="nc">Tool</span><span class="p">(</span><span class="n">google_search</span><span class="o">=</span><span class="n">types</span><span class="p">.</span><span class="nc">GoogleSearch</span><span class="p">())],</span>
        <span class="n">temperature</span><span class="o">=</span><span class="mf">0.0</span>
    <span class="p">)</span>
    
    <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="n">self</span><span class="p">,</span> <span class="n">genai_client</span><span class="p">,</span> <span class="n">rag_impl</span><span class="p">):</span>
        <span class="n">self</span><span class="p">.</span><span class="n">client</span> <span class="o">=</span> <span class="n">genai_client</span>
        <span class="n">self</span><span class="p">.</span><span class="n">rag</span> <span class="o">=</span> <span class="n">rag_impl</span>

    <span class="k">def</span> <span class="nf">generate_answer</span><span class="p">(</span><span class="n">self</span><span class="p">,</span> <span class="n">query</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">topic</span><span class="p">:</span> <span class="nb">str</span><span class="p">):</span>
        <span class="n">stored</span> <span class="o">=</span> <span class="n">self</span><span class="p">.</span><span class="n">rag</span><span class="p">.</span><span class="nf">get_grounding_documents</span><span class="p">(</span><span class="n">query</span><span class="p">,</span> <span class="n">topic</span><span class="p">)</span>
        <span class="k">if</span> <span class="nf">len</span><span class="p">(</span><span class="n">stored</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mi">0</span><span class="p">:</span>
            <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nf">range</span><span class="p">(</span><span class="nf">len</span><span class="p">(</span><span class="n">stored</span><span class="p">)):</span>
                <span class="n">meta_q</span> <span class="o">=</span> <span class="n">stored</span><span class="p">[</span><span class="n">i</span><span class="p">].</span><span class="n">meta</span><span class="p">[</span><span class="sh">"</span><span class="s">question</span><span class="sh">"</span><span class="p">]</span>
                <span class="n">p_ground_match</span> <span class="o">=</span> <span class="mf">0.95</span> <span class="c1"># This can be really high ~ 95-97%
</span>                <span class="k">if</span> <span class="nf">tqdm</span><span class="p">(</span><span class="n">api</span><span class="p">.</span><span class="nf">similarity</span><span class="p">([</span><span class="n">query</span><span class="p">,</span> <span class="n">meta_q</span><span class="p">])</span> <span class="o">&gt;</span> <span class="n">p_ground_match</span><span class="p">,</span>
                        <span class="n">desc</span><span class="o">=</span><span class="sh">"</span><span class="s">Score similarity to stored grounding</span><span class="sh">"</span><span class="p">):</span>
                    <span class="k">return</span> <span class="n">ast</span><span class="p">.</span><span class="nf">literal_eval</span><span class="p">(</span><span class="n">stored</span><span class="p">[</span><span class="n">i</span><span class="p">].</span><span class="n">docs</span><span class="p">)</span>
        <span class="k">return</span> <span class="n">self</span><span class="p">.</span><span class="nf">get_grounding</span><span class="p">(</span><span class="n">query</span><span class="p">,</span> <span class="n">topic</span><span class="p">)</span>

    <span class="nd">@retry.Retry</span><span class="p">(</span>
        <span class="n">predicate</span><span class="o">=</span><span class="n">is_retriable</span><span class="p">,</span>
        <span class="n">initial</span><span class="o">=</span><span class="mf">2.0</span><span class="p">,</span>
        <span class="n">maximum</span><span class="o">=</span><span class="mf">64.0</span><span class="p">,</span>
        <span class="n">multiplier</span><span class="o">=</span><span class="mf">2.0</span><span class="p">,</span>
        <span class="n">timeout</span><span class="o">=</span><span class="mi">600</span><span class="p">,</span>
    <span class="p">)</span>
    <span class="k">def</span> <span class="nf">get_grounding</span><span class="p">(</span><span class="n">self</span><span class="p">,</span> <span class="n">query</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">topic</span><span class="p">:</span> <span class="nb">str</span><span class="p">):</span>
        <span class="n">contents</span> <span class="o">=</span> <span class="p">[</span><span class="n">types</span><span class="p">.</span><span class="nc">Content</span><span class="p">(</span><span class="n">role</span><span class="o">=</span><span class="sh">"</span><span class="s">user</span><span class="sh">"</span><span class="p">,</span> <span class="n">parts</span><span class="o">=</span><span class="p">[</span><span class="n">types</span><span class="p">.</span><span class="nc">Part</span><span class="p">(</span><span class="n">text</span><span class="o">=</span><span class="n">query</span><span class="p">)])]</span>
        <span class="n">contents</span> <span class="o">+=</span> <span class="sa">f</span><span class="sh">"""</span><span class="s">
        You</span><span class="sh">'</span><span class="s">re a search assistant that provides answers to questions about </span><span class="si">{</span><span class="n">topic</span><span class="si">}</span><span class="s">.
        Do not discuss alternative topics of interest. Do not discuss similar topics.
        You will provide answers that discuss only </span><span class="si">{</span><span class="n">topic</span><span class="si">}</span><span class="s">. 
        You may discuss the owner or parent of </span><span class="si">{</span><span class="n">topic</span><span class="si">}</span><span class="s"> when no other answer is possible.
        Otherwise respond with: I don</span><span class="sh">'</span><span class="s">t know.</span><span class="sh">"""</span>
        <span class="n">response</span> <span class="o">=</span> <span class="n">api</span><span class="p">.</span><span class="nf">retriable</span><span class="p">(</span><span class="n">self</span><span class="p">.</span><span class="n">client</span><span class="p">.</span><span class="n">models</span><span class="p">.</span><span class="n">generate_content</span><span class="p">,</span> 
                                 <span class="n">model</span><span class="o">=</span><span class="nf">api</span><span class="p">(</span><span class="n">Api</span><span class="p">.</span><span class="n">Model</span><span class="p">.</span><span class="n">GEN</span><span class="p">),</span> 
                                 <span class="n">config</span><span class="o">=</span><span class="n">self</span><span class="p">.</span><span class="n">config_ground</span><span class="p">,</span> 
                                 <span class="n">contents</span><span class="o">=</span><span class="n">contents</span><span class="p">)</span>
        <span class="k">if</span> <span class="n">response</span><span class="p">.</span><span class="n">candidates</span><span class="p">[</span><span class="mi">0</span><span class="p">].</span><span class="n">grounding_metadata</span><span class="p">.</span><span class="n">grounding_supports</span> <span class="ow">is</span> <span class="ow">not</span> <span class="bp">None</span><span class="p">:</span>
            <span class="k">if</span> <span class="n">self</span><span class="p">.</span><span class="nf">is_consistent</span><span class="p">(</span><span class="n">query</span><span class="p">,</span> <span class="n">topic</span><span class="p">,</span> <span class="n">response</span><span class="p">.</span><span class="n">text</span><span class="p">):</span>
                <span class="n">self</span><span class="p">.</span><span class="n">rag</span><span class="p">.</span><span class="nf">add_grounded_document</span><span class="p">(</span><span class="n">query</span><span class="p">,</span> <span class="n">topic</span><span class="p">,</span> <span class="n">response</span><span class="p">)</span>
                <span class="k">return</span> <span class="n">response</span><span class="p">.</span><span class="n">text</span> 
        <span class="k">return</span> <span class="n">Api</span><span class="p">.</span><span class="n">Const</span><span class="p">.</span><span class="nc">Stop</span><span class="p">()</span> <span class="c1"># Empty grounding supports or not consistent in response
</span>
    <span class="k">def</span> <span class="nf">is_consistent</span><span class="p">(</span><span class="n">self</span><span class="p">,</span> <span class="n">query</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">topic</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">model_response</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">bool</span><span class="p">:</span>
        <span class="n">topic</span> <span class="o">=</span> <span class="n">topic</span><span class="p">.</span><span class="nf">replace</span><span class="p">(</span><span class="sh">"'"</span><span class="p">,</span> <span class="sh">""</span><span class="p">)</span>
        <span class="n">id_strs</span> <span class="o">=</span> <span class="n">topic</span><span class="p">.</span><span class="nf">split</span><span class="p">()</span>
        <span class="k">if</span> <span class="nf">len</span><span class="p">(</span><span class="n">id_strs</span><span class="p">)</span> <span class="o">==</span> <span class="mi">1</span><span class="p">:</span>
            <span class="n">matches</span> <span class="o">=</span> <span class="n">re</span><span class="p">.</span><span class="nf">findall</span><span class="p">(</span><span class="sa">rf</span><span class="sh">"</span><span class="si">{</span><span class="n">id_strs</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="si">}</span><span class="s">[\s,.]+\S+</span><span class="sh">"</span><span class="p">,</span> <span class="n">query</span><span class="p">)</span>
            <span class="k">if</span> <span class="nf">len</span><span class="p">(</span><span class="n">matches</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mi">0</span><span class="p">:</span>
                <span class="n">topic</span> <span class="o">=</span> <span class="n">matches</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>
        <span class="n">compound_match</span> <span class="o">=</span> <span class="n">re</span><span class="p">.</span><span class="nf">findall</span><span class="p">(</span><span class="sa">rf</span><span class="sh">"</span><span class="si">{</span><span class="n">id_strs</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="si">}</span><span class="s">[\s,.]+\S+</span><span class="sh">"</span><span class="p">,</span> <span class="n">model_response</span><span class="p">)</span>
        <span class="n">model_response</span> <span class="o">=</span> <span class="n">model_response</span><span class="p">.</span><span class="nf">replace</span><span class="p">(</span><span class="sh">"'"</span><span class="p">,</span> <span class="sh">""</span><span class="p">)</span>
        <span class="k">if</span> <span class="nf">len</span><span class="p">(</span><span class="n">compound_match</span><span class="p">)</span> <span class="o">==</span> <span class="mi">0</span> <span class="ow">and</span> <span class="n">topic</span> <span class="ow">in</span> <span class="n">model_response</span><span class="p">:</span>
            <span class="k">return</span> <span class="bp">True</span> <span class="c1"># not a compound topic id and exact topic match
</span>        <span class="k">for</span> <span class="k">match</span> <span class="ow">in</span> <span class="n">compound_match</span><span class="p">:</span>
            <span class="k">if</span> <span class="n">topic</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">match</span><span class="p">:</span>
                <span class="k">return</span> <span class="bp">False</span>
        <span class="k">return</span> <span class="bp">True</span> <span class="c1"># all prefix matches contained topic
</span></code></pre></div></div>

<h3 id="rest-grounding">Rest Grounding</h3>

<div class="language-python highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="c1"># Rest api-helpers to manage request-per-minute limits.
# - define an entry for each endpoint limit
# - init rest tool with limits to create blocking queues
# - apply a limit to requests with rest_tool.try_url
</span><span class="k">class</span> <span class="nc">ApiLimit</span><span class="p">(</span><span class="n">Enum</span><span class="p">):</span>
    <span class="n">FINN</span> <span class="o">=</span> <span class="sh">"</span><span class="s">finnhub.io</span><span class="sh">"</span><span class="p">,</span><span class="mi">50</span>
    <span class="n">POLY</span> <span class="o">=</span> <span class="sh">"</span><span class="s">polygon.io</span><span class="sh">"</span><span class="p">,</span><span class="mi">4</span> <span class="c1"># (id_url,rpm)
</span>
<span class="k">class</span> <span class="nc">BlockingUrlQueue</span><span class="p">:</span>
    <span class="n">on_cooldown</span> <span class="o">=</span> <span class="bp">False</span>
    <span class="n">cooldown</span> <span class="o">=</span> <span class="bp">None</span>
    <span class="n">cooldown_start</span> <span class="o">=</span> <span class="bp">None</span>
    
    <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="n">self</span><span class="p">,</span> <span class="n">rest_fn</span><span class="p">:</span> <span class="n">Callable</span><span class="p">,</span> <span class="n">per_minute</span><span class="p">:</span> <span class="nb">int</span><span class="p">):</span>
        <span class="n">self</span><span class="p">.</span><span class="n">per_minute_max</span> <span class="o">=</span> <span class="n">per_minute</span>
        <span class="n">self</span><span class="p">.</span><span class="n">quota</span> <span class="o">=</span> <span class="n">per_minute</span>
        <span class="n">self</span><span class="p">.</span><span class="n">rest_fn</span> <span class="o">=</span> <span class="n">rest_fn</span>

    <span class="k">def</span> <span class="nf">push</span><span class="p">(</span><span class="n">self</span><span class="p">,</span> <span class="n">rest_url</span><span class="p">:</span> <span class="nb">str</span><span class="p">):</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="n">self</span><span class="p">.</span><span class="n">on_cooldown</span><span class="p">:</span>
            <span class="n">self</span><span class="p">.</span><span class="n">cooldown</span> <span class="o">=</span> <span class="nc">Timer</span><span class="p">(</span><span class="mi">60</span><span class="p">,</span> <span class="n">self</span><span class="p">.</span><span class="n">reset_quota</span><span class="p">)</span>
            <span class="n">self</span><span class="p">.</span><span class="n">cooldown</span><span class="p">.</span><span class="nf">start</span><span class="p">()</span>
            <span class="n">self</span><span class="p">.</span><span class="n">cooldown_start</span> <span class="o">=</span> <span class="n">time</span><span class="p">.</span><span class="nf">time</span><span class="p">()</span>
            <span class="n">self</span><span class="p">.</span><span class="n">on_cooldown</span> <span class="o">=</span> <span class="bp">True</span>
        <span class="k">if</span> <span class="n">self</span><span class="p">.</span><span class="n">quota</span> <span class="o">&gt;</span> <span class="mi">0</span><span class="p">:</span>
            <span class="n">self</span><span class="p">.</span><span class="n">quota</span> <span class="o">-=</span> <span class="mi">1</span>
            <span class="n">time</span><span class="p">.</span><span class="nf">sleep</span><span class="p">(</span><span class="mf">0.034</span><span class="p">)</span> <span class="c1"># ~30 requests per second
</span>            <span class="k">return</span> <span class="n">self</span><span class="p">.</span><span class="nf">rest_fn</span><span class="p">(</span><span class="n">rest_url</span><span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="nf">print</span><span class="p">(</span><span class="sa">f</span><span class="sh">"</span><span class="s">limited </span><span class="si">{</span><span class="n">self</span><span class="p">.</span><span class="n">per_minute_max</span><span class="si">}</span><span class="s">/min, waiting </span><span class="si">{</span><span class="n">self</span><span class="p">.</span><span class="nf">limit_expiry</span><span class="p">()</span><span class="si">}</span><span class="s">s</span><span class="sh">"</span><span class="p">)</span>
            <span class="n">time</span><span class="p">.</span><span class="nf">sleep</span><span class="p">(</span><span class="nf">max</span><span class="p">(</span><span class="n">self</span><span class="p">.</span><span class="nf">limit_expiry</span><span class="p">(),</span><span class="mf">0.5</span><span class="p">))</span>
            <span class="k">return</span> <span class="n">self</span><span class="p">.</span><span class="nf">push</span><span class="p">(</span><span class="n">rest_url</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">reset_quota</span><span class="p">(</span><span class="n">self</span><span class="p">):</span>
        <span class="n">self</span><span class="p">.</span><span class="n">quota</span> <span class="o">=</span> <span class="n">self</span><span class="p">.</span><span class="n">per_minute_max</span>
        <span class="n">self</span><span class="p">.</span><span class="n">on_cooldown</span> <span class="o">=</span> <span class="bp">False</span>
        <span class="n">self</span><span class="p">.</span><span class="n">cooldown_start</span> <span class="o">=</span> <span class="bp">None</span>

    <span class="k">def</span> <span class="nf">limit_expiry</span><span class="p">(</span><span class="n">self</span><span class="p">):</span>
        <span class="k">if</span> <span class="n">self</span><span class="p">.</span><span class="n">cooldown_start</span><span class="p">:</span>
            <span class="k">return</span> <span class="nf">max</span><span class="p">(</span><span class="mi">60</span><span class="o">-</span><span class="p">(</span><span class="n">time</span><span class="p">.</span><span class="nf">time</span><span class="p">()</span><span class="o">-</span><span class="n">self</span><span class="p">.</span><span class="n">cooldown_start</span><span class="p">),</span><span class="mi">0</span><span class="p">)</span>
        <span class="k">return</span> <span class="mi">0</span>
</code></pre></div></div>

<div class="language-python highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="c1"># Define tool: rest-grounding generation.
# - using gemini-2.0-flash for response generation
# - using a RAG-implementation to store groundings
# - reduce long-context by chunked pre-processing
</span><span class="k">class</span> <span class="nc">RestGroundingGenerator</span><span class="p">:</span>    
    <span class="n">limits</span> <span class="o">=</span> <span class="bp">None</span>

    <span class="k">def</span> <span class="nf">__init__</span><span class="p">(</span><span class="n">self</span><span class="p">,</span> <span class="n">rag_impl</span><span class="p">,</span> <span class="n">with_limits</span><span class="p">:</span> <span class="nb">bool</span><span class="p">):</span>
        <span class="n">self</span><span class="p">.</span><span class="n">rag</span> <span class="o">=</span> <span class="n">rag_impl</span>
        <span class="k">if</span> <span class="n">with_limits</span><span class="p">:</span>
            <span class="n">self</span><span class="p">.</span><span class="n">limits</span> <span class="o">=</span> <span class="p">{}</span>
            <span class="k">for</span> <span class="n">rest_api</span> <span class="ow">in</span> <span class="n">ApiLimit</span><span class="p">:</span>
                <span class="n">self</span><span class="p">.</span><span class="n">limits</span><span class="p">[</span><span class="n">rest_api</span><span class="p">.</span><span class="n">value</span><span class="p">[</span><span class="mi">0</span><span class="p">]]</span> <span class="o">=</span> <span class="nc">BlockingUrlQueue</span><span class="p">(</span><span class="n">Api</span><span class="p">.</span><span class="n">get</span><span class="p">,</span> <span class="n">rest_api</span><span class="p">.</span><span class="n">value</span><span class="p">[</span><span class="mi">1</span><span class="p">])</span>

    <span class="k">def</span> <span class="nf">get_limit</span><span class="p">(</span><span class="n">self</span><span class="p">,</span> <span class="n">rest_api</span><span class="p">:</span> <span class="n">ApiLimit</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="n">BlockingUrlQueue</span><span class="p">]:</span>
        <span class="k">return</span> <span class="n">self</span><span class="p">.</span><span class="n">limits</span><span class="p">[</span><span class="n">rest_api</span><span class="p">.</span><span class="n">value</span><span class="p">[</span><span class="mi">0</span><span class="p">]]</span> <span class="k">if</span> <span class="n">self</span><span class="p">.</span><span class="n">limits</span> <span class="k">else</span> <span class="bp">None</span>

    <span class="k">def</span> <span class="nf">basemodel</span><span class="p">(</span><span class="n">self</span><span class="p">,</span> <span class="n">data</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">schema</span><span class="p">:</span> <span class="n">BaseModel</span><span class="p">,</span> <span class="n">from_lambda</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="bp">False</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="n">BaseModel</span><span class="p">]:</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="k">if</span> <span class="n">from_lambda</span><span class="p">:</span>
                <span class="k">return</span> <span class="nf">schema</span><span class="p">(</span><span class="n">results</span><span class="o">=</span><span class="n">json</span><span class="p">.</span><span class="nf">loads</span><span class="p">(</span><span class="n">data</span><span class="p">))</span>
            <span class="k">return</span> <span class="n">schema</span><span class="p">.</span><span class="nf">model_validate_json</span><span class="p">(</span><span class="n">data</span><span class="p">)</span>
        <span class="k">except</span> <span class="nb">Exception</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
            <span class="k">raise</span> <span class="n">e</span>

    <span class="k">def</span> <span class="nf">dailycandle</span><span class="p">(</span><span class="n">self</span><span class="p">,</span> <span class="n">data</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Optional</span><span class="p">[</span><span class="n">DailyCandle</span><span class="p">]:</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="n">candle</span> <span class="o">=</span> <span class="n">json</span><span class="p">.</span><span class="nf">loads</span><span class="p">(</span><span class="n">data</span><span class="p">)</span>
            <span class="k">if</span> <span class="sh">"</span><span class="s">from</span><span class="sh">"</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">candle</span><span class="p">:</span>
                <span class="k">raise</span> <span class="nc">ValueError</span><span class="p">(</span><span class="sh">"</span><span class="s">not a dailycandle / missing value for date</span><span class="sh">"</span><span class="p">)</span>
            <span class="n">agg</span> <span class="o">=</span> <span class="n">self</span><span class="p">.</span><span class="nf">basemodel</span><span class="p">(</span><span class="n">data</span><span class="p">,</span> <span class="n">Aggregate</span><span class="p">)</span>
            <span class="k">return</span> <span class="nc">DailyCandle</span><span class="p">(</span><span class="n">from_date</span><span class="o">=</span><span class="n">candle</span><span class="p">[</span><span class="sh">"</span><span class="s">from</span><span class="sh">"</span><span class="p">],</span> 
                               <span class="n">status</span><span class="o">=</span><span class="n">agg</span><span class="p">.</span><span class="n">status</span><span class="p">.</span><span class="n">value</span><span class="p">,</span> 
                               <span class="n">symbol</span><span class="o">=</span><span class="n">agg</span><span class="p">.</span><span class="n">symbol</span><span class="p">,</span> 
                               <span class="nb">open</span><span class="o">=</span><span class="n">agg</span><span class="p">.</span><span class="nb">open</span><span class="p">,</span> 
                               <span class="n">high</span><span class="o">=</span><span class="n">agg</span><span class="p">.</span><span class="n">high</span><span class="p">,</span> 
                               <span class="n">low</span><span class="o">=</span><span class="n">agg</span><span class="p">.</span><span class="n">low</span><span class="p">,</span> 
                               <span class="n">close</span><span class="o">=</span><span class="n">agg</span><span class="p">.</span><span class="n">close</span><span class="p">,</span> 
                               <span class="n">volume</span><span class="o">=</span><span class="n">agg</span><span class="p">.</span><span class="n">volume</span><span class="p">,</span> 
                               <span class="n">otc</span><span class="o">=</span><span class="n">agg</span><span class="p">.</span><span class="n">otc</span><span class="p">,</span> 
                               <span class="n">preMarket</span><span class="o">=</span><span class="n">agg</span><span class="p">.</span><span class="n">preMarket</span><span class="p">,</span> 
                               <span class="n">afterHours</span><span class="o">=</span><span class="n">agg</span><span class="p">.</span><span class="n">afterHours</span><span class="p">)</span>
        <span class="k">except</span> <span class="nb">Exception</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
            <span class="k">raise</span> <span class="n">e</span>

    <span class="nd">@retry.Retry</span><span class="p">(</span><span class="n">timeout</span><span class="o">=</span><span class="mi">600</span><span class="p">)</span>
    <span class="k">def</span> <span class="nf">try_url</span><span class="p">(</span><span class="n">self</span><span class="p">,</span> <span class="n">url</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">schema</span><span class="p">:</span> <span class="n">BaseModel</span><span class="p">,</span> <span class="n">as_lambda</span><span class="p">:</span> <span class="nb">bool</span><span class="p">,</span> <span class="n">with_limit</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">BlockingUrlQueue</span><span class="p">],</span>
                <span class="n">success_fn</span><span class="p">:</span> <span class="n">Callable</span><span class="p">,</span> <span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">):</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="k">if</span> <span class="n">self</span><span class="p">.</span><span class="n">limits</span> <span class="ow">is</span> <span class="bp">None</span><span class="p">:</span>
                <span class="n">data</span> <span class="o">=</span> <span class="n">Api</span><span class="p">.</span><span class="nf">get</span><span class="p">(</span><span class="n">url</span><span class="p">)</span>
            <span class="k">elif</span> <span class="n">with_limit</span><span class="p">:</span>
                <span class="n">data</span> <span class="o">=</span> <span class="n">with_limit</span><span class="p">.</span><span class="nf">push</span><span class="p">(</span><span class="n">url</span><span class="p">)</span>
            <span class="k">if</span> <span class="n">schema</span> <span class="ow">is</span> <span class="n">DailyCandle</span><span class="p">:</span>
                <span class="n">model</span> <span class="o">=</span> <span class="n">self</span><span class="p">.</span><span class="nf">dailycandle</span><span class="p">(</span><span class="n">data</span><span class="p">)</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="n">model</span> <span class="o">=</span> <span class="n">self</span><span class="p">.</span><span class="nf">basemodel</span><span class="p">(</span><span class="n">data</span><span class="p">,</span> <span class="n">schema</span><span class="p">,</span> <span class="n">as_lambda</span><span class="p">)</span>
        <span class="k">except</span> <span class="nb">Exception</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
            <span class="k">try</span><span class="p">:</span>
                <span class="nf">print</span><span class="p">(</span><span class="sa">f</span><span class="sh">"</span><span class="s">try_url exception: </span><span class="si">{</span><span class="n">e</span><span class="si">}</span><span class="sh">"</span><span class="p">)</span>
                <span class="k">if</span> <span class="nf">issubclass</span><span class="p">(</span><span class="n">schema</span><span class="p">,</span> <span class="n">RestResultPoly</span><span class="p">):</span>
                    <span class="k">return</span> <span class="nf">success_fn</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">,</span> <span class="n">result</span><span class="o">=</span><span class="n">self</span><span class="p">.</span><span class="nf">basemodel</span><span class="p">(</span><span class="n">data</span><span class="p">,</span> <span class="n">RestResultPoly</span><span class="p">))</span>
            <span class="k">except</span> <span class="nb">Exception</span> <span class="k">as</span> <span class="n">not_a_result</span><span class="p">:</span>
                <span class="nf">print</span><span class="p">(</span><span class="n">not_a_result</span><span class="p">)</span>
            <span class="k">return</span> <span class="nc">StopGeneration</span><span class="p">()</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="k">return</span> <span class="nf">success_fn</span><span class="p">(</span><span class="o">*</span><span class="n">args</span><span class="p">,</span> <span class="o">**</span><span class="n">kwargs</span><span class="p">,</span> <span class="n">model</span><span class="o">=</span><span class="n">model</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">get_symbol_matches</span><span class="p">(</span><span class="n">self</span><span class="p">,</span> <span class="n">with_content</span><span class="p">,</span> <span class="n">by_name</span><span class="p">:</span> <span class="nb">bool</span><span class="p">,</span> <span class="n">model</span><span class="p">:</span> <span class="n">SymbolResult</span><span class="p">):</span>
        <span class="n">matches</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="n">max_failed_match</span> <span class="o">=</span> <span class="n">model</span><span class="p">.</span><span class="n">count</span> <span class="k">if</span> <span class="ow">not</span> <span class="n">by_name</span> <span class="k">else</span> <span class="mi">3</span>
        <span class="n">p_desc_match</span> <span class="o">=</span> <span class="mf">0.92</span>
        <span class="n">p_symb_match</span> <span class="o">=</span> <span class="mf">0.95</span>
        <span class="k">if</span> <span class="n">model</span><span class="p">.</span><span class="n">count</span> <span class="o">&gt;</span> <span class="mi">0</span><span class="p">:</span>
            <span class="k">for</span> <span class="n">obj</span> <span class="ow">in</span> <span class="nf">tqdm</span><span class="p">(</span><span class="n">model</span><span class="p">.</span><span class="nf">get</span><span class="p">(),</span> <span class="n">desc</span><span class="o">=</span><span class="sh">"</span><span class="s">Score similarity to query</span><span class="sh">"</span><span class="p">):</span>
                <span class="k">if</span> <span class="n">max_failed_match</span> <span class="o">&gt;</span> <span class="mi">0</span><span class="p">:</span>
                    <span class="n">desc</span> <span class="o">=</span> <span class="p">[</span><span class="n">with_content</span><span class="p">[</span><span class="sh">"</span><span class="s">q</span><span class="sh">"</span><span class="p">].</span><span class="nf">upper</span><span class="p">(),</span> <span class="n">obj</span><span class="p">.</span><span class="n">description</span><span class="p">.</span><span class="nf">split</span><span class="p">(</span><span class="sh">"</span><span class="s">-</span><span class="sh">"</span><span class="p">,</span> <span class="o">-</span><span class="mi">1</span><span class="p">)[</span><span class="mi">0</span><span class="p">]]</span>
                    <span class="n">symb</span> <span class="o">=</span> <span class="p">[</span><span class="n">with_content</span><span class="p">[</span><span class="sh">"</span><span class="s">q</span><span class="sh">"</span><span class="p">].</span><span class="nf">upper</span><span class="p">(),</span> <span class="n">obj</span><span class="p">.</span><span class="n">symbol</span><span class="p">]</span>
                    <span class="k">if</span> <span class="n">by_name</span> <span class="ow">and</span> <span class="n">api</span><span class="p">.</span><span class="nf">similarity</span><span class="p">(</span><span class="n">desc</span><span class="p">)</span> <span class="o">&gt;</span> <span class="n">p_desc_match</span><span class="p">:</span> 
                        <span class="n">matches</span><span class="p">.</span><span class="nf">append</span><span class="p">(</span><span class="n">obj</span><span class="p">.</span><span class="n">symbol</span><span class="p">)</span>
                    <span class="k">elif</span> <span class="ow">not</span> <span class="n">by_name</span> <span class="ow">and</span> <span class="n">api</span><span class="p">.</span><span class="nf">similarity</span><span class="p">(</span><span class="n">symb</span><span class="p">)</span> <span class="o">&gt;</span> <span class="n">p_symb_match</span><span class="p">:</span>
                        <span class="n">matches</span><span class="p">.</span><span class="nf">append</span><span class="p">(</span><span class="n">obj</span><span class="p">.</span><span class="n">description</span><span class="p">)</span>
                        <span class="n">max_failed_match</span> <span class="o">=</span> <span class="mi">0</span>
                    <span class="k">else</span><span class="p">:</span>
                        <span class="n">max_failed_match</span> <span class="o">-=</span> <span class="mi">1</span>
        <span class="k">if</span> <span class="nf">len</span><span class="p">(</span><span class="n">matches</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mi">0</span><span class="p">:</span>
            <span class="n">self</span><span class="p">.</span><span class="n">rag</span><span class="p">.</span><span class="nf">add_api_document</span><span class="p">(</span><span class="n">with_content</span><span class="p">[</span><span class="sh">"</span><span class="s">query</span><span class="sh">"</span><span class="p">],</span> <span class="n">matches</span><span class="p">,</span> <span class="n">with_content</span><span class="p">[</span><span class="sh">"</span><span class="s">q</span><span class="sh">"</span><span class="p">],</span> <span class="sh">"</span><span class="s">get_symbol_1</span><span class="sh">"</span><span class="p">)</span>
            <span class="k">return</span> <span class="n">matches</span>
        <span class="k">return</span> <span class="n">Api</span><span class="p">.</span><span class="n">Const</span><span class="p">.</span><span class="nc">Stop</span><span class="p">()</span>

    <span class="k">def</span> <span class="nf">get_quote</span><span class="p">(</span><span class="n">self</span><span class="p">,</span> <span class="n">with_content</span><span class="p">,</span> <span class="n">model</span><span class="p">:</span> <span class="n">Quote</span><span class="p">):</span>
        <span class="n">quote</span> <span class="o">=</span> <span class="n">model</span><span class="p">.</span><span class="nf">model_dump_json</span><span class="p">()</span>
        <span class="n">self</span><span class="p">.</span><span class="n">rag</span><span class="p">.</span><span class="nf">add_quote_document</span><span class="p">(</span><span class="n">with_content</span><span class="p">[</span><span class="sh">"</span><span class="s">query</span><span class="sh">"</span><span class="p">],</span> <span class="n">quote</span><span class="p">,</span> <span class="n">with_content</span><span class="p">[</span><span class="sh">"</span><span class="s">symbol</span><span class="sh">"</span><span class="p">],</span> <span class="n">model</span><span class="p">.</span><span class="n">t</span><span class="p">,</span> <span class="sh">"</span><span class="s">get_quote_1</span><span class="sh">"</span><span class="p">)</span>
        <span class="k">return</span> <span class="n">quote</span>

    <span class="k">def</span> <span class="nf">parse_financials</span><span class="p">(</span><span class="n">self</span><span class="p">,</span> <span class="n">with_content</span><span class="p">,</span> <span class="n">model</span><span class="p">:</span> <span class="n">BasicFinancials</span><span class="p">):</span>
        <span class="n">metric</span> <span class="o">=</span> <span class="nf">list</span><span class="p">(</span><span class="n">model</span><span class="p">.</span><span class="n">metric</span><span class="p">.</span><span class="nf">items</span><span class="p">())</span>
        <span class="n">chunks</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="c1"># Chunk the metric data.
</span>        <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nf">range</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="nf">len</span><span class="p">(</span><span class="n">metric</span><span class="p">),</span> <span class="n">Api</span><span class="p">.</span><span class="n">Const</span><span class="p">.</span><span class="nc">MetricBatch</span><span class="p">()):</span>
            <span class="n">batch</span> <span class="o">=</span> <span class="n">metric</span><span class="p">[</span><span class="n">i</span><span class="p">:</span><span class="n">i</span> <span class="o">+</span> <span class="n">Api</span><span class="p">.</span><span class="n">Const</span><span class="p">.</span><span class="nc">MetricBatch</span><span class="p">()]</span>
            <span class="n">chunks</span><span class="p">.</span><span class="nf">append</span><span class="p">({</span><span class="sh">"</span><span class="s">question</span><span class="sh">"</span><span class="p">:</span> <span class="n">with_content</span><span class="p">[</span><span class="sh">"</span><span class="s">query</span><span class="sh">"</span><span class="p">],</span> <span class="sh">"</span><span class="s">answer</span><span class="sh">"</span><span class="p">:</span> <span class="n">batch</span><span class="p">})</span>
        <span class="c1"># Chunk the series data.
</span>        <span class="k">for</span> <span class="n">key</span> <span class="ow">in</span> <span class="n">model</span><span class="p">.</span><span class="n">series</span><span class="p">.</span><span class="nf">keys</span><span class="p">():</span>
            <span class="n">series</span> <span class="o">=</span> <span class="nf">list</span><span class="p">(</span><span class="n">model</span><span class="p">.</span><span class="n">series</span><span class="p">[</span><span class="n">key</span><span class="p">].</span><span class="nf">items</span><span class="p">())</span>
            <span class="k">for</span> <span class="n">s</span> <span class="ow">in</span> <span class="n">series</span><span class="p">:</span>
                <span class="k">if</span> <span class="n">api</span><span class="p">.</span><span class="nf">token_count</span><span class="p">(</span><span class="n">s</span><span class="p">)</span> <span class="o">&lt;=</span> <span class="n">Api</span><span class="p">.</span><span class="n">Const</span><span class="p">.</span><span class="nc">ChunkMax</span><span class="p">():</span>
                    <span class="n">chunks</span><span class="p">.</span><span class="nf">append</span><span class="p">({</span><span class="sh">"</span><span class="s">question</span><span class="sh">"</span><span class="p">:</span> <span class="n">with_content</span><span class="p">[</span><span class="sh">"</span><span class="s">query</span><span class="sh">"</span><span class="p">],</span> <span class="sh">"</span><span class="s">answer</span><span class="sh">"</span><span class="p">:</span> <span class="n">s</span><span class="p">})</span>
                <span class="k">else</span><span class="p">:</span>
                    <span class="n">k</span> <span class="o">=</span> <span class="n">s</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>
                    <span class="n">v</span> <span class="o">=</span> <span class="n">s</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span>
                    <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nf">range</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="nf">len</span><span class="p">(</span><span class="n">v</span><span class="p">),</span> <span class="n">Api</span><span class="p">.</span><span class="n">Const</span><span class="p">.</span><span class="nc">SeriesBatch</span><span class="p">()):</span>
                        <span class="n">batch</span> <span class="o">=</span> <span class="n">v</span><span class="p">[</span><span class="n">i</span><span class="p">:</span><span class="n">i</span> <span class="o">+</span> <span class="n">Api</span><span class="p">.</span><span class="n">Const</span><span class="p">.</span><span class="nc">SeriesBatch</span><span class="p">()]</span>
                        <span class="n">chunks</span><span class="p">.</span><span class="nf">append</span><span class="p">({</span><span class="sh">"</span><span class="s">question</span><span class="sh">"</span><span class="p">:</span> <span class="n">with_content</span><span class="p">[</span><span class="sh">"</span><span class="s">query</span><span class="sh">"</span><span class="p">],</span> <span class="sh">"</span><span class="s">answer</span><span class="sh">"</span><span class="p">:</span> <span class="p">{</span><span class="n">k</span><span class="p">:</span> <span class="n">batch</span><span class="p">}})</span>
        <span class="n">self</span><span class="p">.</span><span class="n">rag</span><span class="p">.</span><span class="nf">add_rest_chunks</span><span class="p">(</span><span class="n">chunks</span><span class="p">,</span> <span class="n">topic</span><span class="o">=</span><span class="n">with_content</span><span class="p">[</span><span class="sh">"</span><span class="s">symbol</span><span class="sh">"</span><span class="p">],</span> <span class="n">source</span><span class="o">=</span><span class="sh">"</span><span class="s">get_financials_1</span><span class="sh">"</span><span class="p">)</span>
        <span class="k">return</span> <span class="n">chunks</span>

    <span class="k">def</span> <span class="nf">parse_news</span><span class="p">(</span><span class="n">self</span><span class="p">,</span> <span class="n">with_content</span><span class="p">,</span> <span class="n">model</span><span class="p">:</span> <span class="n">NewsResultFinn</span><span class="p">):</span>
        <span class="k">if</span> <span class="n">model</span><span class="p">.</span><span class="n">count</span> <span class="o">&gt;</span> <span class="mi">0</span><span class="p">:</span>
            <span class="n">metas</span> <span class="o">=</span> <span class="p">[]</span>
            <span class="k">for</span> <span class="n">digest</span> <span class="ow">in</span> <span class="n">model</span><span class="p">.</span><span class="nf">get</span><span class="p">():</span>
                <span class="n">pub_date</span> <span class="o">=</span> <span class="n">datetime</span><span class="p">.</span><span class="nf">fromtimestamp</span><span class="p">(</span><span class="n">digest</span><span class="p">.</span><span class="n">datetime</span><span class="p">,</span> <span class="n">tz</span><span class="o">=</span><span class="n">GeneratedEvent</span><span class="p">.</span><span class="nf">tz</span><span class="p">()).</span><span class="nf">strftime</span><span class="p">(</span><span class="sh">"</span><span class="s">%Y-%m-%d</span><span class="sh">"</span><span class="p">)</span>
                <span class="n">metas</span><span class="p">.</span><span class="nf">append</span><span class="p">({</span><span class="sh">"</span><span class="s">publisher</span><span class="sh">"</span><span class="p">:</span> <span class="n">digest</span><span class="p">.</span><span class="n">source</span><span class="p">,</span>
                              <span class="sh">"</span><span class="s">published_est</span><span class="sh">"</span><span class="p">:</span> <span class="nf">parse</span><span class="p">(</span><span class="n">pub_date</span><span class="p">).</span><span class="nf">timestamp</span><span class="p">(),</span>
                              <span class="sh">"</span><span class="s">news_id</span><span class="sh">"</span><span class="p">:</span> <span class="n">digest</span><span class="p">.</span><span class="nb">id</span><span class="p">,</span>
                              <span class="sh">"</span><span class="s">related</span><span class="sh">"</span><span class="p">:</span> <span class="n">digest</span><span class="p">.</span><span class="n">related</span><span class="p">})</span>
            <span class="n">self</span><span class="p">.</span><span class="n">rag</span><span class="p">.</span><span class="nf">add_rest_chunks</span><span class="p">(</span><span class="n">model</span><span class="p">.</span><span class="nf">get</span><span class="p">(),</span> <span class="n">topic</span><span class="o">=</span><span class="n">with_content</span><span class="p">[</span><span class="sh">"</span><span class="s">symbol</span><span class="sh">"</span><span class="p">],</span> <span class="n">source</span><span class="o">=</span><span class="sh">"</span><span class="s">get_news_1</span><span class="sh">"</span><span class="p">,</span>
                                     <span class="n">ids</span><span class="o">=</span><span class="p">[</span><span class="sa">f</span><span class="sh">"</span><span class="si">{</span><span class="n">digest</span><span class="p">.</span><span class="nb">id</span><span class="si">}</span><span class="s">+news</span><span class="sh">"</span> <span class="k">for</span> <span class="n">digest</span> <span class="ow">in</span> <span class="n">model</span><span class="p">.</span><span class="nf">get</span><span class="p">()],</span>
                                     <span class="n">meta_opt</span><span class="o">=</span><span class="n">metas</span><span class="p">,</span> <span class="n">is_update</span><span class="o">=</span><span class="bp">False</span><span class="p">)</span>
            <span class="k">return</span> <span class="p">[</span><span class="n">digest</span><span class="p">.</span><span class="nf">summary</span><span class="p">().</span><span class="nf">model_dump_json</span><span class="p">()</span> <span class="k">for</span> <span class="n">digest</span> <span class="ow">in</span> <span class="n">model</span><span class="p">.</span><span class="nf">get</span><span class="p">()]</span>
        <span class="k">return</span> <span class="n">Api</span><span class="p">.</span><span class="n">Const</span><span class="p">.</span><span class="nc">Stop</span><span class="p">()</span>

    <span class="k">def</span> <span class="nf">parse_news</span><span class="p">(</span><span class="n">self</span><span class="p">,</span> <span class="n">with_content</span><span class="p">,</span> <span class="n">model</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">NewsResultPoly</span><span class="p">]</span> <span class="o">=</span> <span class="bp">None</span><span class="p">,</span>
                   <span class="n">result</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">RestResultPoly</span><span class="p">]</span> <span class="o">=</span> <span class="bp">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">tuple</span><span class="p">[</span><span class="nb">list</span><span class="p">,</span> <span class="nb">str</span><span class="p">]:</span> <span class="c1"># list of summary, next list url
</span>        <span class="k">if</span> <span class="n">model</span> <span class="ow">and</span> <span class="n">model</span><span class="p">.</span><span class="n">status</span> <span class="ow">in</span> <span class="p">[</span><span class="n">RestStatus</span><span class="p">.</span><span class="n">OK</span><span class="p">,</span> <span class="n">RestStatus</span><span class="p">.</span><span class="n">DELAY</span><span class="p">]:</span>
            <span class="n">metas</span> <span class="o">=</span> <span class="p">[]</span>
            <span class="k">for</span> <span class="n">news</span> <span class="ow">in</span> <span class="n">model</span><span class="p">.</span><span class="nf">get</span><span class="p">():</span>
                <span class="n">pub_date</span> <span class="o">=</span> <span class="nf">parse</span><span class="p">(</span><span class="n">news</span><span class="p">.</span><span class="n">published_utc</span><span class="p">).</span><span class="nf">strftime</span><span class="p">(</span><span class="sh">"</span><span class="s">%Y-%m-%d</span><span class="sh">"</span><span class="p">)</span>
                <span class="n">metas</span><span class="p">.</span><span class="nf">append</span><span class="p">({</span><span class="sh">"</span><span class="s">publisher</span><span class="sh">"</span><span class="p">:</span> <span class="n">news</span><span class="p">.</span><span class="n">publisher</span><span class="p">.</span><span class="n">name</span><span class="p">,</span>
                              <span class="sh">"</span><span class="s">published_utc</span><span class="sh">"</span><span class="p">:</span> <span class="nf">parse</span><span class="p">(</span><span class="n">pub_date</span><span class="p">).</span><span class="nf">timestamp</span><span class="p">(),</span>
                              <span class="sh">"</span><span class="s">news_id</span><span class="sh">"</span><span class="p">:</span> <span class="n">news</span><span class="p">.</span><span class="nb">id</span><span class="p">,</span>
                              <span class="sh">"</span><span class="s">related</span><span class="sh">"</span><span class="p">:</span> <span class="n">json</span><span class="p">.</span><span class="nf">dumps</span><span class="p">(</span><span class="n">news</span><span class="p">.</span><span class="n">tickers</span><span class="p">),</span>
                              <span class="sh">"</span><span class="s">keywords</span><span class="sh">"</span><span class="p">:</span> <span class="n">json</span><span class="p">.</span><span class="nf">dumps</span><span class="p">(</span><span class="n">news</span><span class="p">.</span><span class="n">keywords</span><span class="p">)})</span>
            <span class="n">self</span><span class="p">.</span><span class="n">rag</span><span class="p">.</span><span class="nf">add_rest_chunks</span><span class="p">(</span><span class="n">model</span><span class="p">.</span><span class="nf">get</span><span class="p">(),</span> <span class="n">topic</span><span class="o">=</span><span class="n">with_content</span><span class="p">[</span><span class="sh">"</span><span class="s">ticker</span><span class="sh">"</span><span class="p">],</span> <span class="n">source</span><span class="o">=</span><span class="sh">"</span><span class="s">get_news_2</span><span class="sh">"</span><span class="p">,</span>
                                     <span class="n">ids</span><span class="o">=</span><span class="p">[</span><span class="n">news</span><span class="p">.</span><span class="nb">id</span> <span class="k">for</span> <span class="n">news</span> <span class="ow">in</span> <span class="n">model</span><span class="p">.</span><span class="nf">get</span><span class="p">()],</span>
                                     <span class="n">meta_opt</span><span class="o">=</span><span class="n">metas</span><span class="p">,</span> <span class="n">is_update</span><span class="o">=</span><span class="bp">False</span><span class="p">)</span>
            <span class="k">return</span> <span class="p">[</span><span class="n">news</span><span class="p">.</span><span class="nf">summary</span><span class="p">().</span><span class="nf">model_dump_json</span><span class="p">()</span> <span class="k">for</span> <span class="n">news</span> <span class="ow">in</span> <span class="n">model</span><span class="p">.</span><span class="nf">get</span><span class="p">()],</span> <span class="n">model</span><span class="p">.</span><span class="n">next_url</span>
        <span class="k">elif</span> <span class="n">result</span><span class="p">:</span>
            <span class="k">return</span> <span class="n">result</span><span class="p">.</span><span class="nf">model_dump_json</span><span class="p">()</span>

    <span class="k">def</span> <span class="nf">parse_daily_candle</span><span class="p">(</span><span class="n">self</span><span class="p">,</span> <span class="n">with_content</span><span class="p">,</span> <span class="n">model</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">DailyCandle</span><span class="p">]</span> <span class="o">=</span> <span class="bp">None</span><span class="p">,</span>
                           <span class="n">result</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">RestResultPoly</span><span class="p">]</span> <span class="o">=</span> <span class="bp">None</span><span class="p">):</span>
        <span class="k">if</span> <span class="n">model</span> <span class="ow">and</span> <span class="n">model</span><span class="p">.</span><span class="n">status</span> <span class="ow">in</span> <span class="p">[</span><span class="n">RestStatus</span><span class="p">.</span><span class="n">OK</span><span class="p">,</span> <span class="n">RestStatus</span><span class="p">.</span><span class="n">DELAY</span><span class="p">]:</span>
            <span class="n">self</span><span class="p">.</span><span class="n">rag</span><span class="p">.</span><span class="nf">add_rest_chunks</span><span class="p">(</span>
                <span class="n">chunks</span><span class="o">=</span><span class="p">[</span><span class="n">model</span><span class="p">],</span>
                <span class="n">topic</span><span class="o">=</span><span class="n">with_content</span><span class="p">[</span><span class="sh">"</span><span class="s">stocksTicker</span><span class="sh">"</span><span class="p">],</span>
                <span class="n">source</span><span class="o">=</span><span class="sh">"</span><span class="s">daily_candle_2</span><span class="sh">"</span><span class="p">,</span>
                <span class="n">meta_opt</span><span class="o">=</span><span class="p">[{</span><span class="sh">"</span><span class="s">from_date</span><span class="sh">"</span><span class="p">:</span> <span class="n">model</span><span class="p">.</span><span class="n">from_date</span><span class="p">,</span> <span class="sh">"</span><span class="s">adjusted</span><span class="sh">"</span><span class="p">:</span> <span class="n">with_content</span><span class="p">[</span><span class="sh">"</span><span class="s">adjusted</span><span class="sh">"</span><span class="p">]}])</span>
            <span class="k">return</span> <span class="n">model</span>
        <span class="k">elif</span> <span class="n">result</span><span class="p">:</span>
            <span class="k">return</span> <span class="n">result</span>

    <span class="k">def</span> <span class="nf">parse_custom_candle</span><span class="p">(</span><span class="n">self</span><span class="p">,</span> <span class="n">with_content</span><span class="p">,</span> <span class="n">model</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">CustomCandle</span><span class="p">]</span> <span class="o">=</span> <span class="bp">None</span><span class="p">,</span>
                            <span class="n">result</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="n">RestResultPoly</span><span class="p">]</span> <span class="o">=</span> <span class="bp">None</span><span class="p">):</span>
        <span class="k">if</span> <span class="n">model</span> <span class="ow">and</span> <span class="n">model</span><span class="p">.</span><span class="n">status</span> <span class="ow">in</span> <span class="p">[</span><span class="n">RestStatus</span><span class="p">.</span><span class="n">OK</span><span class="p">,</span> <span class="n">RestStatus</span><span class="p">.</span><span class="n">DELAY</span><span class="p">]:</span>
            <span class="n">metas</span> <span class="o">=</span> <span class="p">[{</span>
                <span class="sh">"</span><span class="s">timespan</span><span class="sh">"</span><span class="p">:</span> <span class="n">with_content</span><span class="p">[</span><span class="sh">"</span><span class="s">timespan</span><span class="sh">"</span><span class="p">],</span>
                <span class="sh">"</span><span class="s">adjusted</span><span class="sh">"</span><span class="p">:</span> <span class="n">with_content</span><span class="p">[</span><span class="sh">"</span><span class="s">adjusted</span><span class="sh">"</span><span class="p">],</span>
                <span class="sh">"</span><span class="s">from</span><span class="sh">"</span><span class="p">:</span> <span class="n">with_content</span><span class="p">[</span><span class="sh">"</span><span class="s">from</span><span class="sh">"</span><span class="p">],</span>
                <span class="sh">"</span><span class="s">to</span><span class="sh">"</span><span class="p">:</span> <span class="n">with_content</span><span class="p">[</span><span class="sh">"</span><span class="s">to</span><span class="sh">"</span><span class="p">]}]</span><span class="o">*</span><span class="n">model</span><span class="p">.</span><span class="n">count</span>
            <span class="n">candles</span> <span class="o">=</span> <span class="p">[</span><span class="n">candle</span><span class="p">.</span><span class="nf">model_dump_json</span><span class="p">()</span> <span class="k">for</span> <span class="n">candle</span> <span class="ow">in</span> <span class="n">model</span><span class="p">.</span><span class="nf">get</span><span class="p">()]</span>
            <span class="n">self</span><span class="p">.</span><span class="n">rag</span><span class="p">.</span><span class="nf">add_rest_chunks</span><span class="p">(</span>
                <span class="n">chunks</span><span class="o">=</span><span class="n">candles</span><span class="p">,</span>
                <span class="n">topic</span><span class="o">=</span><span class="n">with_content</span><span class="p">[</span><span class="sh">"</span><span class="s">stocksTicker</span><span class="sh">"</span><span class="p">],</span>
                <span class="n">source</span><span class="o">=</span><span class="sh">"</span><span class="s">custom_candle_2</span><span class="sh">"</span><span class="p">,</span>
                <span class="n">meta_opt</span><span class="o">=</span><span class="n">metas</span><span class="p">)</span>
            <span class="k">return</span> <span class="n">candles</span>
        <span class="k">elif</span> <span class="n">result</span><span class="p">:</span>
            <span class="k">return</span> <span class="n">result</span><span class="p">.</span><span class="nf">model_dump_json</span><span class="p">()</span>

    <span class="k">def</span> <span class="nf">parse_overview</span><span class="p">(</span><span class="n">self</span><span class="p">,</span> <span class="n">with_content</span><span class="p">,</span> <span class="n">model</span><span class="p">:</span> <span class="n">OverviewResult</span><span class="p">):</span>
        <span class="n">overview</span> <span class="o">=</span> <span class="p">[</span><span class="n">model</span><span class="p">.</span><span class="nf">get</span><span class="p">().</span><span class="nf">model_dump_json</span><span class="p">()]</span>
        <span class="n">self</span><span class="p">.</span><span class="n">rag</span><span class="p">.</span><span class="nf">add_rest_chunks</span><span class="p">(</span><span class="n">chunks</span><span class="o">=</span><span class="n">overview</span><span class="p">,</span> <span class="n">topic</span><span class="o">=</span><span class="n">with_content</span><span class="p">[</span><span class="sh">"</span><span class="s">ticker</span><span class="sh">"</span><span class="p">],</span> <span class="n">source</span><span class="o">=</span><span class="sh">"</span><span class="s">ticker_overview_2</span><span class="sh">"</span><span class="p">)</span>
        <span class="k">return</span> <span class="n">overview</span>

    <span class="k">def</span> <span class="nf">parse_trends</span><span class="p">(</span><span class="n">self</span><span class="p">,</span> <span class="n">with_content</span><span class="p">,</span> <span class="n">model</span><span class="p">:</span> <span class="n">TrendsResult</span><span class="p">):</span>
        <span class="k">if</span> <span class="n">model</span><span class="p">.</span><span class="n">count</span> <span class="o">&gt;</span> <span class="mi">0</span><span class="p">:</span>
            <span class="n">metas</span> <span class="o">=</span> <span class="p">[{</span><span class="sh">"</span><span class="s">period</span><span class="sh">"</span><span class="p">:</span> <span class="n">trend</span><span class="p">.</span><span class="n">period</span><span class="p">}</span> <span class="k">for</span> <span class="n">trend</span> <span class="ow">in</span> <span class="n">model</span><span class="p">.</span><span class="nf">get</span><span class="p">()]</span>
            <span class="n">trends</span> <span class="o">=</span> <span class="p">[</span><span class="n">trend</span><span class="p">.</span><span class="nf">model_dump_json</span><span class="p">()</span> <span class="k">for</span> <span class="n">trend</span> <span class="ow">in</span> <span class="n">model</span><span class="p">.</span><span class="nf">get</span><span class="p">()]</span>
            <span class="n">self</span><span class="p">.</span><span class="n">rag</span><span class="p">.</span><span class="nf">add_rest_chunks</span><span class="p">(</span><span class="n">trends</span><span class="p">,</span> <span class="n">topic</span><span class="o">=</span><span class="n">with_content</span><span class="p">[</span><span class="sh">"</span><span class="s">symbol</span><span class="sh">"</span><span class="p">],</span> <span class="n">source</span><span class="o">=</span><span class="sh">"</span><span class="s">trends_1</span><span class="sh">"</span><span class="p">,</span> <span class="n">meta_opt</span><span class="o">=</span><span class="n">metas</span><span class="p">)</span>
            <span class="k">return</span> <span class="n">trends</span>
        <span class="k">return</span> <span class="n">Api</span><span class="p">.</span><span class="n">Const</span><span class="p">.</span><span class="nc">Stop</span><span class="p">()</span>

    <span class="k">def</span> <span class="nf">augment_market_status</span><span class="p">(</span><span class="n">self</span><span class="p">,</span> <span class="n">with_id</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">],</span> <span class="n">model</span><span class="p">:</span> <span class="n">MarketStatusResult</span><span class="p">):</span>
        <span class="k">if</span> <span class="n">model</span><span class="p">.</span><span class="nf">get</span><span class="p">().</span><span class="n">holiday</span> <span class="o">!=</span> <span class="n">MarketSession</span><span class="p">.</span><span class="n">NA</span><span class="p">.</span><span class="n">value</span><span class="p">:</span>
            <span class="n">self</span><span class="p">.</span><span class="n">rag</span><span class="p">.</span><span class="nf">set_holiday_event</span><span class="p">(</span><span class="n">model</span><span class="p">.</span><span class="nf">get</span><span class="p">().</span><span class="n">exchange</span><span class="p">)</span>
        <span class="n">events</span> <span class="o">=</span> <span class="n">self</span><span class="p">.</span><span class="n">rag</span><span class="p">.</span><span class="nf">generated_events</span><span class="p">(</span><span class="n">model</span><span class="p">.</span><span class="nf">get</span><span class="p">().</span><span class="n">exchange</span><span class="p">)</span>
        <span class="n">model</span><span class="p">.</span><span class="nf">get</span><span class="p">().</span><span class="n">session</span> <span class="o">=</span> <span class="n">events</span><span class="p">.</span><span class="nf">session</span><span class="p">()</span>
        <span class="n">model</span><span class="p">.</span><span class="nf">get</span><span class="p">().</span><span class="n">isOpen</span> <span class="o">=</span> <span class="n">events</span><span class="p">.</span><span class="nf">is_open</span><span class="p">()</span>
        <span class="n">meta</span> <span class="o">=</span> <span class="p">{</span><span class="sh">"</span><span class="s">exchange</span><span class="sh">"</span><span class="p">:</span> <span class="n">model</span><span class="p">.</span><span class="nf">get</span><span class="p">().</span><span class="n">exchange</span><span class="p">,</span>
                <span class="sh">"</span><span class="s">last_close</span><span class="sh">"</span><span class="p">:</span> <span class="n">events</span><span class="p">.</span><span class="n">last_close</span><span class="p">,</span>
                <span class="sh">"</span><span class="s">pre_open</span><span class="sh">"</span><span class="p">:</span> <span class="n">events</span><span class="p">.</span><span class="n">pre_open</span><span class="p">,</span>
                <span class="sh">"</span><span class="s">reg_open</span><span class="sh">"</span><span class="p">:</span> <span class="n">events</span><span class="p">.</span><span class="n">reg_open</span><span class="p">,</span>
                <span class="sh">"</span><span class="s">reg_close</span><span class="sh">"</span><span class="p">:</span> <span class="n">events</span><span class="p">.</span><span class="n">reg_close</span><span class="p">,</span>
                <span class="sh">"</span><span class="s">post_close</span><span class="sh">"</span><span class="p">:</span> <span class="n">events</span><span class="p">.</span><span class="n">post_close</span><span class="p">,</span>
                <span class="sh">"</span><span class="s">timestamp</span><span class="sh">"</span><span class="p">:</span> <span class="n">events</span><span class="p">.</span><span class="n">timestamp</span> <span class="p">}</span>
        <span class="n">self</span><span class="p">.</span><span class="n">rag</span><span class="p">.</span><span class="nf">add_rest_chunks</span><span class="p">([</span><span class="n">model</span><span class="p">.</span><span class="nf">get</span><span class="p">()],</span>
                                 <span class="n">topic</span><span class="o">=</span><span class="sh">"</span><span class="s">market_status</span><span class="sh">"</span><span class="p">,</span>
                                 <span class="n">source</span><span class="o">=</span><span class="sh">"</span><span class="s">get_market_status_1</span><span class="sh">"</span><span class="p">,</span>
                                 <span class="n">ids</span><span class="o">=</span><span class="p">[</span><span class="n">with_id</span><span class="p">]</span> <span class="k">if</span> <span class="n">with_id</span> <span class="k">else</span> <span class="bp">None</span><span class="p">,</span>
                                 <span class="n">meta_opt</span><span class="o">=</span><span class="p">[</span><span class="n">meta</span><span class="p">])</span>
        <span class="k">return</span> <span class="n">model</span><span class="p">.</span><span class="nf">get</span><span class="p">().</span><span class="nf">model_dump_json</span><span class="p">()</span>

    <span class="k">def</span> <span class="nf">get_symbol</span><span class="p">(</span><span class="n">self</span><span class="p">,</span> <span class="n">content</span><span class="p">,</span> <span class="n">by_name</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="bp">True</span><span class="p">):</span>
        <span class="k">return</span> <span class="n">self</span><span class="p">.</span><span class="nf">try_url</span><span class="p">(</span>
            <span class="sa">f</span><span class="sh">"</span><span class="s">https://finnhub.io/api/v1/search?q=</span><span class="si">{</span><span class="n">content</span><span class="p">[</span><span class="sh">'</span><span class="s">q</span><span class="sh">'</span><span class="p">]</span><span class="si">}</span><span class="s">&amp;exchange=</span><span class="si">{</span><span class="n">content</span><span class="p">[</span><span class="sh">'</span><span class="s">exchange</span><span class="sh">'</span><span class="p">]</span><span class="si">}</span><span class="s">&amp;token=</span><span class="si">{</span><span class="n">FINNHUB_API_KEY</span><span class="si">}</span><span class="sh">"</span><span class="p">,</span>
            <span class="n">schema</span><span class="o">=</span><span class="n">SymbolResult</span><span class="p">,</span>
            <span class="n">as_lambda</span><span class="o">=</span><span class="bp">False</span><span class="p">,</span>
            <span class="n">with_limit</span><span class="o">=</span><span class="n">self</span><span class="p">.</span><span class="nf">get_limit</span><span class="p">(</span><span class="n">ApiLimit</span><span class="p">.</span><span class="n">FINN</span><span class="p">),</span>
            <span class="n">success_fn</span><span class="o">=</span><span class="n">self</span><span class="p">.</span><span class="n">get_symbol_matches</span><span class="p">,</span>
            <span class="n">with_content</span><span class="o">=</span><span class="n">content</span><span class="p">,</span>
            <span class="n">by_name</span><span class="o">=</span><span class="n">by_name</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">get_current_price</span><span class="p">(</span><span class="n">self</span><span class="p">,</span> <span class="n">content</span><span class="p">):</span>
        <span class="k">return</span> <span class="n">self</span><span class="p">.</span><span class="nf">try_url</span><span class="p">(</span>
            <span class="sa">f</span><span class="sh">"</span><span class="s">https://finnhub.io/api/v1/quote?symbol=</span><span class="si">{</span><span class="n">content</span><span class="p">[</span><span class="sh">'</span><span class="s">symbol</span><span class="sh">'</span><span class="p">]</span><span class="si">}</span><span class="s">&amp;token=</span><span class="si">{</span><span class="n">FINNHUB_API_KEY</span><span class="si">}</span><span class="sh">"</span><span class="p">,</span>
            <span class="n">schema</span><span class="o">=</span><span class="n">Quote</span><span class="p">,</span>
            <span class="n">as_lambda</span><span class="o">=</span><span class="bp">False</span><span class="p">,</span>
            <span class="n">with_limit</span><span class="o">=</span><span class="n">self</span><span class="p">.</span><span class="nf">get_limit</span><span class="p">(</span><span class="n">ApiLimit</span><span class="p">.</span><span class="n">FINN</span><span class="p">),</span>
            <span class="n">success_fn</span><span class="o">=</span><span class="n">self</span><span class="p">.</span><span class="n">get_quote</span><span class="p">,</span>
            <span class="n">with_content</span><span class="o">=</span><span class="n">content</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">get_market_status</span><span class="p">(</span><span class="n">self</span><span class="p">,</span> <span class="n">content</span><span class="p">,</span> <span class="n">store_id</span><span class="p">:</span> <span class="n">Optional</span><span class="p">[</span><span class="nb">str</span><span class="p">]</span> <span class="o">=</span> <span class="bp">None</span><span class="p">):</span>
        <span class="k">return</span> <span class="n">self</span><span class="p">.</span><span class="nf">try_url</span><span class="p">(</span>
            <span class="sa">f</span><span class="sh">"</span><span class="s">https://finnhub.io/api/v1/stock/market-status?exchange=</span><span class="si">{</span><span class="n">content</span><span class="p">[</span><span class="sh">'</span><span class="s">exchange</span><span class="sh">'</span><span class="p">]</span><span class="si">}</span><span class="s">&amp;token=</span><span class="si">{</span><span class="n">FINNHUB_API_KEY</span><span class="si">}</span><span class="sh">"</span><span class="p">,</span>
            <span class="n">schema</span><span class="o">=</span><span class="n">MarketStatusResult</span><span class="p">,</span>
            <span class="n">as_lambda</span><span class="o">=</span><span class="bp">True</span><span class="p">,</span>
            <span class="n">with_limit</span><span class="o">=</span><span class="n">self</span><span class="p">.</span><span class="nf">get_limit</span><span class="p">(</span><span class="n">ApiLimit</span><span class="p">.</span><span class="n">FINN</span><span class="p">),</span>
            <span class="n">success_fn</span><span class="o">=</span><span class="n">self</span><span class="p">.</span><span class="n">augment_market_status</span><span class="p">,</span>
            <span class="n">with_id</span><span class="o">=</span><span class="n">store_id</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">get_peers</span><span class="p">(</span><span class="n">self</span><span class="p">,</span> <span class="n">content</span><span class="p">):</span>
        <span class="k">return</span> <span class="n">self</span><span class="p">.</span><span class="nf">try_url</span><span class="p">(</span>
            <span class="sa">f</span><span class="sh">"</span><span class="s">https://finnhub.io/api/v1/stock/peers?symbol=</span><span class="si">{</span><span class="n">content</span><span class="p">[</span><span class="sh">'</span><span class="s">symbol</span><span class="sh">'</span><span class="p">]</span><span class="si">}</span><span class="s">&amp;grouping=</span><span class="si">{</span><span class="n">content</span><span class="p">[</span><span class="sh">'</span><span class="s">grouping</span><span class="sh">'</span><span class="p">]</span><span class="si">}</span><span class="s">&amp;token=</span><span class="si">{</span><span class="n">FINNHUB_API_KEY</span><span class="si">}</span><span class="sh">"</span><span class="p">,</span>
            <span class="n">schema</span><span class="o">=</span><span class="n">PeersResult</span><span class="p">,</span>
            <span class="n">as_lambda</span><span class="o">=</span><span class="bp">True</span><span class="p">,</span>
            <span class="n">with_limit</span><span class="o">=</span><span class="n">self</span><span class="p">.</span><span class="nf">get_limit</span><span class="p">(</span><span class="n">ApiLimit</span><span class="p">.</span><span class="n">FINN</span><span class="p">),</span>
            <span class="n">success_fn</span><span class="o">=</span><span class="k">lambda</span> <span class="n">model</span><span class="p">:</span> <span class="n">model</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">get_basic_financials</span><span class="p">(</span><span class="n">self</span><span class="p">,</span> <span class="n">content</span><span class="p">):</span>
        <span class="k">return</span> <span class="n">self</span><span class="p">.</span><span class="nf">try_url</span><span class="p">(</span>
            <span class="sa">f</span><span class="sh">"</span><span class="s">https://finnhub.io/api/v1/stock/metric?symbol=</span><span class="si">{</span><span class="n">content</span><span class="p">[</span><span class="sh">'</span><span class="s">symbol</span><span class="sh">'</span><span class="p">]</span><span class="si">}</span><span class="s">&amp;metric=</span><span class="si">{</span><span class="n">content</span><span class="p">[</span><span class="sh">'</span><span class="s">metric</span><span class="sh">'</span><span class="p">]</span><span class="si">}</span><span class="s">&amp;token=</span><span class="si">{</span><span class="n">FINNHUB_API_KEY</span><span class="si">}</span><span class="sh">"</span><span class="p">,</span>
            <span class="n">schema</span><span class="o">=</span><span class="n">BasicFinancials</span><span class="p">,</span>
            <span class="n">as_lambda</span><span class="o">=</span><span class="bp">False</span><span class="p">,</span>
            <span class="n">with_limit</span><span class="o">=</span><span class="n">self</span><span class="p">.</span><span class="nf">get_limit</span><span class="p">(</span><span class="n">ApiLimit</span><span class="p">.</span><span class="n">FINN</span><span class="p">),</span>
            <span class="n">success_fn</span><span class="o">=</span><span class="n">self</span><span class="p">.</span><span class="n">parse_financials</span><span class="p">,</span>
            <span class="n">with_content</span><span class="o">=</span><span class="n">content</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">get_news_simple</span><span class="p">(</span><span class="n">self</span><span class="p">,</span> <span class="n">content</span><span class="p">):</span>
        <span class="k">return</span> <span class="n">self</span><span class="p">.</span><span class="nf">try_url</span><span class="p">(</span>
            <span class="sa">f</span><span class="sh">"</span><span class="s">https://finnhub.io/api/v1/company-news?symbol=</span><span class="si">{</span><span class="n">content</span><span class="p">[</span><span class="sh">'</span><span class="s">symbol</span><span class="sh">'</span><span class="p">]</span><span class="si">}</span><span class="s">&amp;from=</span><span class="si">{</span><span class="n">content</span><span class="p">[</span><span class="sh">'</span><span class="s">from</span><span class="sh">'</span><span class="p">]</span><span class="si">}</span><span class="s">&amp;to=</span><span class="si">{</span><span class="n">content</span><span class="p">[</span><span class="sh">'</span><span class="s">to</span><span class="sh">'</span><span class="p">]</span><span class="si">}</span><span class="s">&amp;token=</span><span class="si">{</span><span class="n">FINNHUB_API_KEY</span><span class="si">}</span><span class="sh">"</span><span class="p">,</span>
            <span class="n">schema</span><span class="o">=</span><span class="n">NewsResultFinn</span><span class="p">,</span>
            <span class="n">as_lambda</span><span class="o">=</span><span class="bp">True</span><span class="p">,</span>
            <span class="n">with_limit</span><span class="o">=</span><span class="n">self</span><span class="p">.</span><span class="nf">get_limit</span><span class="p">(</span><span class="n">ApiLimit</span><span class="p">.</span><span class="n">FINN</span><span class="p">),</span>
            <span class="n">success_fn</span><span class="o">=</span><span class="n">self</span><span class="p">.</span><span class="n">parse_news</span><span class="p">,</span>
            <span class="n">with_content</span><span class="o">=</span><span class="n">content</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">get_news_tagged</span><span class="p">(</span><span class="n">self</span><span class="p">,</span> <span class="n">content</span><span class="p">):</span>
        <span class="n">next_url</span> <span class="o">=</span> <span class="sa">f</span><span class="sh">"</span><span class="s">https://api.polygon.io/v2/reference/news?ticker=</span><span class="si">{</span><span class="n">content</span><span class="p">[</span><span class="sh">'</span><span class="s">ticker</span><span class="sh">'</span><span class="p">]</span><span class="si">}</span><span class="s">&amp;published_utc.gte=</span><span class="si">{</span><span class="n">content</span><span class="p">[</span><span class="sh">'</span><span class="s">published_utc.gte</span><span class="sh">'</span><span class="p">]</span><span class="si">}</span><span class="s">&amp;published_utc.lte=</span><span class="si">{</span><span class="n">content</span><span class="p">[</span><span class="sh">'</span><span class="s">published_utc.lte</span><span class="sh">'</span><span class="p">]</span><span class="si">}</span><span class="s">&amp;order=</span><span class="si">{</span><span class="n">content</span><span class="p">[</span><span class="sh">'</span><span class="s">order</span><span class="sh">'</span><span class="p">]</span><span class="si">}</span><span class="s">&amp;limit=</span><span class="si">{</span><span class="n">content</span><span class="p">[</span><span class="sh">'</span><span class="s">limit</span><span class="sh">'</span><span class="p">]</span><span class="si">}</span><span class="s">&amp;sort=</span><span class="si">{</span><span class="n">content</span><span class="p">[</span><span class="sh">'</span><span class="s">sort</span><span class="sh">'</span><span class="p">]</span><span class="si">}</span><span class="s">&amp;apiKey=</span><span class="si">{</span><span class="n">POLYGON_API_KEY</span><span class="si">}</span><span class="sh">"</span>
        <span class="n">news</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">while</span> <span class="bp">True</span><span class="p">:</span>
            <span class="n">news_list</span><span class="p">,</span> <span class="n">next_url</span> <span class="o">=</span> <span class="n">self</span><span class="p">.</span><span class="nf">try_url</span><span class="p">(</span>
                <span class="n">next_url</span><span class="p">,</span>
                <span class="n">schema</span><span class="o">=</span><span class="n">NewsResultPoly</span><span class="p">,</span>
                <span class="n">as_lambda</span><span class="o">=</span><span class="bp">False</span><span class="p">,</span>
                <span class="n">with_limit</span><span class="o">=</span><span class="n">self</span><span class="p">.</span><span class="nf">get_limit</span><span class="p">(</span><span class="n">ApiLimit</span><span class="p">.</span><span class="n">POLY</span><span class="p">),</span>
                <span class="n">success_fn</span><span class="o">=</span><span class="n">self</span><span class="p">.</span><span class="n">parse_news</span><span class="p">,</span>
                <span class="n">with_content</span><span class="o">=</span><span class="n">content</span><span class="p">)</span>
            <span class="n">news</span> <span class="o">+=</span> <span class="n">news_list</span>
            <span class="k">if</span> <span class="n">next_url</span> <span class="ow">is</span> <span class="bp">None</span><span class="p">:</span>
                <span class="k">break</span>
            <span class="n">next_url</span> <span class="o">+=</span> <span class="sa">f</span><span class="sh">"</span><span class="s">&amp;apiKey=</span><span class="si">{</span><span class="n">POLYGON_API_KEY</span><span class="si">}</span><span class="sh">"</span>
        <span class="k">return</span> <span class="n">news</span>

    <span class="k">def</span> <span class="nf">get_daily_candle</span><span class="p">(</span><span class="n">self</span><span class="p">,</span> <span class="n">content</span><span class="p">):</span>
        <span class="k">return</span> <span class="n">self</span><span class="p">.</span><span class="nf">try_url</span><span class="p">(</span>
            <span class="sa">f</span><span class="sh">"</span><span class="s">https://api.polygon.io/v1/open-close/</span><span class="si">{</span><span class="n">content</span><span class="p">[</span><span class="sh">'</span><span class="s">stocksTicker</span><span class="sh">'</span><span class="p">]</span><span class="si">}</span><span class="s">/</span><span class="si">{</span><span class="n">content</span><span class="p">[</span><span class="sh">'</span><span class="s">date</span><span class="sh">'</span><span class="p">]</span><span class="si">}</span><span class="s">?adjusted=</span><span class="si">{</span><span class="n">content</span><span class="p">[</span><span class="sh">'</span><span class="s">adjusted</span><span class="sh">'</span><span class="p">]</span><span class="si">}</span><span class="s">&amp;apiKey=</span><span class="si">{</span><span class="n">POLYGON_API_KEY</span><span class="si">}</span><span class="sh">"</span><span class="p">,</span>
            <span class="n">schema</span><span class="o">=</span><span class="n">DailyCandle</span><span class="p">,</span>
            <span class="n">as_lambda</span><span class="o">=</span><span class="bp">False</span><span class="p">,</span>
            <span class="n">with_limit</span><span class="o">=</span><span class="n">self</span><span class="p">.</span><span class="nf">get_limit</span><span class="p">(</span><span class="n">ApiLimit</span><span class="p">.</span><span class="n">POLY</span><span class="p">),</span>
            <span class="n">success_fn</span><span class="o">=</span><span class="n">self</span><span class="p">.</span><span class="n">parse_daily_candle</span><span class="p">,</span>
            <span class="n">with_content</span><span class="o">=</span><span class="n">content</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">get_custom_candle</span><span class="p">(</span><span class="n">self</span><span class="p">,</span> <span class="n">content</span><span class="p">):</span>
        <span class="k">return</span> <span class="n">self</span><span class="p">.</span><span class="nf">try_url</span><span class="p">(</span>
            <span class="sa">f</span><span class="sh">"</span><span class="s">https://api.polygon.io/v2/aggs/ticker/</span><span class="si">{</span><span class="n">content</span><span class="p">[</span><span class="sh">'</span><span class="s">stocksTicker</span><span class="sh">'</span><span class="p">]</span><span class="si">}</span><span class="s">/range/</span><span class="si">{</span><span class="n">content</span><span class="p">[</span><span class="sh">'</span><span class="s">multiplier</span><span class="sh">'</span><span class="p">]</span><span class="si">}</span><span class="s">/</span><span class="si">{</span><span class="n">content</span><span class="p">[</span><span class="sh">'</span><span class="s">timespan</span><span class="sh">'</span><span class="p">]</span><span class="si">}</span><span class="s">/</span><span class="si">{</span><span class="n">content</span><span class="p">[</span><span class="sh">'</span><span class="s">from</span><span class="sh">'</span><span class="p">]</span><span class="si">}</span><span class="s">/</span><span class="si">{</span><span class="n">content</span><span class="p">[</span><span class="sh">'</span><span class="s">to</span><span class="sh">'</span><span class="p">]</span><span class="si">}</span><span class="s">?adjusted=</span><span class="si">{</span><span class="n">content</span><span class="p">[</span><span class="sh">'</span><span class="s">adjusted</span><span class="sh">'</span><span class="p">]</span><span class="si">}</span><span class="s">&amp;sort=</span><span class="si">{</span><span class="n">content</span><span class="p">[</span><span class="sh">'</span><span class="s">sort</span><span class="sh">'</span><span class="p">]</span><span class="si">}</span><span class="s">&amp;limit=</span><span class="si">{</span><span class="n">content</span><span class="p">[</span><span class="sh">'</span><span class="s">limit</span><span class="sh">'</span><span class="p">]</span><span class="si">}</span><span class="s">&amp;apiKey=</span><span class="si">{</span><span class="n">POLYGON_API_KEY</span><span class="si">}</span><span class="sh">"</span><span class="p">,</span>
            <span class="n">schema</span><span class="o">=</span><span class="n">CustomCandle</span><span class="p">,</span>
            <span class="n">as_lambda</span><span class="o">=</span><span class="bp">False</span><span class="p">,</span>
            <span class="n">with_limit</span><span class="o">=</span><span class="n">self</span><span class="p">.</span><span class="nf">get_limit</span><span class="p">(</span><span class="n">ApiLimit</span><span class="p">.</span><span class="n">POLY</span><span class="p">),</span>
            <span class="n">success_fn</span><span class="o">=</span><span class="n">self</span><span class="p">.</span><span class="n">parse_custom_candle</span><span class="p">,</span>
            <span class="n">with_content</span><span class="o">=</span><span class="n">content</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">get_overview</span><span class="p">(</span><span class="n">self</span><span class="p">,</span> <span class="n">content</span><span class="p">):</span>
        <span class="k">return</span> <span class="n">self</span><span class="p">.</span><span class="nf">try_url</span><span class="p">(</span>
            <span class="sa">f</span><span class="sh">"</span><span class="s">https://api.polygon.io/v3/reference/tickers/</span><span class="si">{</span><span class="n">content</span><span class="p">[</span><span class="sh">'</span><span class="s">ticker</span><span class="sh">'</span><span class="p">]</span><span class="si">}</span><span class="s">?apiKey=</span><span class="si">{</span><span class="n">POLYGON_API_KEY</span><span class="si">}</span><span class="sh">"</span><span class="p">,</span>
            <span class="n">schema</span><span class="o">=</span><span class="n">OverviewResult</span><span class="p">,</span>
            <span class="n">as_lambda</span><span class="o">=</span><span class="bp">False</span><span class="p">,</span>
            <span class="n">with_limit</span><span class="o">=</span><span class="n">self</span><span class="p">.</span><span class="nf">get_limit</span><span class="p">(</span><span class="n">ApiLimit</span><span class="p">.</span><span class="n">POLY</span><span class="p">),</span>
            <span class="n">success_fn</span><span class="o">=</span><span class="n">self</span><span class="p">.</span><span class="n">parse_overview</span><span class="p">,</span>
            <span class="n">with_content</span><span class="o">=</span><span class="n">content</span><span class="p">)</span>

    <span class="k">def</span> <span class="nf">get_trends_simple</span><span class="p">(</span><span class="n">self</span><span class="p">,</span> <span class="n">content</span><span class="p">):</span>
        <span class="k">return</span> <span class="n">self</span><span class="p">.</span><span class="nf">try_url</span><span class="p">(</span>
            <span class="sa">f</span><span class="sh">"</span><span class="s">https://finnhub.io/api/v1/stock/recommendation?symbol=</span><span class="si">{</span><span class="n">content</span><span class="p">[</span><span class="sh">'</span><span class="s">symbol</span><span class="sh">'</span><span class="p">]</span><span class="si">}</span><span class="s">&amp;token=</span><span class="si">{</span><span class="n">FINNHUB_API_KEY</span><span class="si">}</span><span class="sh">"</span><span class="p">,</span>
            <span class="n">schema</span><span class="o">=</span><span class="n">TrendsResult</span><span class="p">,</span>
            <span class="n">as_lambda</span><span class="o">=</span><span class="bp">True</span><span class="p">,</span>
            <span class="n">with_limit</span><span class="o">=</span><span class="n">self</span><span class="p">.</span><span class="nf">get_limit</span><span class="p">(</span><span class="n">ApiLimit</span><span class="p">.</span><span class="n">FINN</span><span class="p">),</span>
            <span class="n">success_fn</span><span class="o">=</span><span class="n">self</span><span class="p">.</span><span class="n">parse_trends</span><span class="p">,</span>
            <span class="n">with_content</span><span class="o">=</span><span class="n">content</span><span class="p">)</span>
</code></pre></div></div>

<h3 id="callable-functions">Callable Functions</h3>

<div class="language-python highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="c1"># Callable functions in openapi schema.
</span><span class="n">decl_get_symbol_1</span> <span class="o">=</span> <span class="n">types</span><span class="p">.</span><span class="nc">FunctionDeclaration</span><span class="p">(</span>
    <span class="n">name</span><span class="o">=</span><span class="sh">"</span><span class="s">get_symbol_1</span><span class="sh">"</span><span class="p">,</span>
    <span class="n">description</span><span class="o">=</span><span class="sh">"""</span><span class="s">Search for the stock ticker symbol of a given company, security, isin or cusip. Each ticker
                   entry provides a description, symbol, and asset type. If this doesn</span><span class="sh">'</span><span class="s">t help you should try 
                   calling get_wiki_tool_response next.</span><span class="sh">"""</span><span class="p">,</span>
    <span class="n">parameters</span><span class="o">=</span><span class="p">{</span>
        <span class="sh">"</span><span class="s">type</span><span class="sh">"</span><span class="p">:</span> <span class="sh">"</span><span class="s">object</span><span class="sh">"</span><span class="p">,</span>
        <span class="sh">"</span><span class="s">properties</span><span class="sh">"</span><span class="p">:</span> <span class="p">{</span>
            <span class="sh">"</span><span class="s">q</span><span class="sh">"</span><span class="p">:</span> <span class="p">{</span>
                <span class="sh">"</span><span class="s">type</span><span class="sh">"</span><span class="p">:</span> <span class="sh">"</span><span class="s">string</span><span class="sh">"</span><span class="p">,</span>
                <span class="sh">"</span><span class="s">description</span><span class="sh">"</span><span class="p">:</span> <span class="sh">"""</span><span class="s">A ticker symbol to search for.</span><span class="sh">"""</span>
            <span class="p">},</span>
            <span class="sh">"</span><span class="s">exchange</span><span class="sh">"</span><span class="p">:</span> <span class="p">{</span>
                <span class="sh">"</span><span class="s">type</span><span class="sh">"</span><span class="p">:</span> <span class="sh">"</span><span class="s">string</span><span class="sh">"</span><span class="p">,</span>
                <span class="sh">"</span><span class="s">description</span><span class="sh">"</span><span class="p">:</span> <span class="sh">"""</span><span class="s">The exchange code used to filter results. When not specified the default exchange 
                                  code you should use is </span><span class="sh">'</span><span class="s">US</span><span class="sh">'</span><span class="s"> for the US exchanges. A dictionary mapping all supported 
                                  exchange codes to their names be retrieved by calling get_exchange_codes_1. 
                                  Search for an exchange code to use by calling get_exchange_code_1, specifying the
                                  exchange code to search for.</span><span class="sh">"""</span>
            <span class="p">},</span>
            <span class="sh">"</span><span class="s">query</span><span class="sh">"</span><span class="p">:</span> <span class="p">{</span>
                <span class="sh">"</span><span class="s">type</span><span class="sh">"</span><span class="p">:</span> <span class="sh">"</span><span class="s">string</span><span class="sh">"</span><span class="p">,</span>
                <span class="sh">"</span><span class="s">description</span><span class="sh">"</span><span class="p">:</span> <span class="sh">"</span><span class="s">The question you</span><span class="sh">'</span><span class="s">re attempting to answer.</span><span class="sh">"</span>
            <span class="p">}</span>
        <span class="p">},</span>
        <span class="sh">"</span><span class="s">required</span><span class="sh">"</span><span class="p">:</span> <span class="p">[</span><span class="sh">"</span><span class="s">q</span><span class="sh">"</span><span class="p">,</span> <span class="sh">"</span><span class="s">exchange</span><span class="sh">"</span><span class="p">,</span> <span class="sh">"</span><span class="s">query</span><span class="sh">"</span><span class="p">]</span>
    <span class="p">}</span>
<span class="p">)</span>

<span class="n">decl_get_symbols_1</span> <span class="o">=</span> <span class="n">types</span><span class="p">.</span><span class="nc">FunctionDeclaration</span><span class="p">(</span>
    <span class="n">name</span><span class="o">=</span><span class="sh">"</span><span class="s">get_symbols_1</span><span class="sh">"</span><span class="p">,</span>
    <span class="n">description</span><span class="o">=</span><span class="sh">"""</span><span class="s">List all supported symbols and tickers. The results are filtered by exchange code.</span><span class="sh">"""</span><span class="p">,</span>
    <span class="n">parameters</span><span class="o">=</span><span class="p">{</span>
        <span class="sh">"</span><span class="s">type</span><span class="sh">"</span><span class="p">:</span> <span class="sh">"</span><span class="s">object</span><span class="sh">"</span><span class="p">,</span>
        <span class="sh">"</span><span class="s">properties</span><span class="sh">"</span><span class="p">:</span> <span class="p">{</span>
            <span class="sh">"</span><span class="s">exchange</span><span class="sh">"</span><span class="p">:</span> <span class="p">{</span>
                <span class="sh">"</span><span class="s">type</span><span class="sh">"</span><span class="p">:</span> <span class="sh">"</span><span class="s">string</span><span class="sh">"</span><span class="p">,</span>
                <span class="sh">"</span><span class="s">description</span><span class="sh">"</span><span class="p">:</span> <span class="sh">"""</span><span class="s">The exchange code used to filter the results.</span><span class="sh">"""</span>
            <span class="p">},</span>
            <span class="sh">"</span><span class="s">query</span><span class="sh">"</span><span class="p">:</span> <span class="p">{</span>
                <span class="sh">"</span><span class="s">type</span><span class="sh">"</span><span class="p">:</span> <span class="sh">"</span><span class="s">string</span><span class="sh">"</span><span class="p">,</span>
                <span class="sh">"</span><span class="s">description</span><span class="sh">"</span><span class="p">:</span> <span class="sh">"</span><span class="s">The question you</span><span class="sh">'</span><span class="s">re attempting to answer.</span><span class="sh">"</span>
            <span class="p">}</span>
        <span class="p">},</span>
        <span class="sh">"</span><span class="s">required</span><span class="sh">"</span><span class="p">:</span> <span class="p">[</span><span class="sh">"</span><span class="s">exchange</span><span class="sh">"</span><span class="p">,</span> <span class="sh">"</span><span class="s">query</span><span class="sh">"</span><span class="p">]</span>
    <span class="p">}</span>
<span class="p">)</span>

<span class="n">decl_get_name_1</span> <span class="o">=</span> <span class="n">types</span><span class="p">.</span><span class="nc">FunctionDeclaration</span><span class="p">(</span>
    <span class="n">name</span><span class="o">=</span><span class="sh">"</span><span class="s">get_name_1</span><span class="sh">"</span><span class="p">,</span>
    <span class="n">description</span><span class="o">=</span><span class="sh">"""</span><span class="s">Search for the name associated with a stock ticker or symbol</span><span class="sh">'</span><span class="s">s company, security, isin or cusip. 
    Each ticker entry provides a description, matching symbol, and asset type.</span><span class="sh">"""</span><span class="p">,</span>
    <span class="n">parameters</span><span class="o">=</span><span class="p">{</span>
        <span class="sh">"</span><span class="s">type</span><span class="sh">"</span><span class="p">:</span> <span class="sh">"</span><span class="s">object</span><span class="sh">"</span><span class="p">,</span>
        <span class="sh">"</span><span class="s">properties</span><span class="sh">"</span><span class="p">:</span> <span class="p">{</span>
            <span class="sh">"</span><span class="s">q</span><span class="sh">"</span><span class="p">:</span> <span class="p">{</span>
                <span class="sh">"</span><span class="s">type</span><span class="sh">"</span><span class="p">:</span> <span class="sh">"</span><span class="s">string</span><span class="sh">"</span><span class="p">,</span>
                <span class="sh">"</span><span class="s">description</span><span class="sh">"</span><span class="p">:</span> <span class="sh">"""</span><span class="s">The symbol or ticker to search for.</span><span class="sh">"""</span>
            <span class="p">},</span>
            <span class="sh">"</span><span class="s">exchange</span><span class="sh">"</span><span class="p">:</span> <span class="p">{</span>
                <span class="sh">"</span><span class="s">type</span><span class="sh">"</span><span class="p">:</span> <span class="sh">"</span><span class="s">string</span><span class="sh">"</span><span class="p">,</span>
                <span class="sh">"</span><span class="s">description</span><span class="sh">"</span><span class="p">:</span> <span class="sh">"""</span><span class="s">The exchange code used to filter results. When not specified the default exchange 
                                  code you should use is </span><span class="sh">'</span><span class="s">US</span><span class="sh">'</span><span class="s"> for the US exchanges. A dictionary mapping all supported 
                                  exchange codes to their names be retrieved by calling get_exchange_codes_1. 
                                  Search for an exchange code to use by calling get_exchange_code_1, specifying the
                                  exchange code to search for.</span><span class="sh">"""</span>
            <span class="p">},</span>
            <span class="sh">"</span><span class="s">query</span><span class="sh">"</span><span class="p">:</span> <span class="p">{</span>
                <span class="sh">"</span><span class="s">type</span><span class="sh">"</span><span class="p">:</span> <span class="sh">"</span><span class="s">string</span><span class="sh">"</span><span class="p">,</span>
                <span class="sh">"</span><span class="s">description</span><span class="sh">"</span><span class="p">:</span> <span class="sh">"</span><span class="s">The question you</span><span class="sh">'</span><span class="s">re attempting to answer.</span><span class="sh">"</span>
            <span class="p">},</span>
            <span class="sh">"</span><span class="s">company</span><span class="sh">"</span><span class="p">:</span> <span class="p">{</span>
                <span class="sh">"</span><span class="s">type</span><span class="sh">"</span><span class="p">:</span> <span class="sh">"</span><span class="s">string</span><span class="sh">"</span><span class="p">,</span>
                <span class="sh">"</span><span class="s">description</span><span class="sh">"</span><span class="p">:</span> <span class="sh">"</span><span class="s">The company you</span><span class="sh">'</span><span class="s">re searching for.</span><span class="sh">"</span>
            <span class="p">}</span>
        <span class="p">},</span>
        <span class="sh">"</span><span class="s">required</span><span class="sh">"</span><span class="p">:</span> <span class="p">[</span><span class="sh">"</span><span class="s">q</span><span class="sh">"</span><span class="p">,</span> <span class="sh">"</span><span class="s">exchange</span><span class="sh">"</span><span class="p">,</span> <span class="sh">"</span><span class="s">query</span><span class="sh">"</span><span class="p">,</span> <span class="sh">"</span><span class="s">company</span><span class="sh">"</span><span class="p">]</span>
    <span class="p">}</span>
<span class="p">)</span>

<span class="n">decl_get_symbol_quote_1</span> <span class="o">=</span> <span class="n">types</span><span class="p">.</span><span class="nc">FunctionDeclaration</span><span class="p">(</span>
    <span class="n">name</span><span class="o">=</span><span class="sh">"</span><span class="s">get_symbol_quote_1</span><span class="sh">"</span><span class="p">,</span>
    <span class="n">description</span><span class="o">=</span><span class="sh">"""</span><span class="s">Search for the current price or quote of a stock ticker or symbol. The response is
                   provided in json format. Each response contains the following key-value pairs:
                   
                   c: Current price,
                   d: Change,
                  dp: Percent change,
                   h: High price of the day,
                   l: Low price of the day,
                   o: Open price of the day,
                  pc: Previous close price,
                   t: Epoch timestamp of price in seconds.

                   Parse the response and respond according to this information.</span><span class="sh">"""</span><span class="p">,</span>
    <span class="n">parameters</span><span class="o">=</span><span class="p">{</span>
        <span class="sh">"</span><span class="s">type</span><span class="sh">"</span><span class="p">:</span> <span class="sh">"</span><span class="s">object</span><span class="sh">"</span><span class="p">,</span>
        <span class="sh">"</span><span class="s">properties</span><span class="sh">"</span><span class="p">:</span> <span class="p">{</span>
            <span class="sh">"</span><span class="s">symbol</span><span class="sh">"</span><span class="p">:</span> <span class="p">{</span>
                <span class="sh">"</span><span class="s">type</span><span class="sh">"</span><span class="p">:</span> <span class="sh">"</span><span class="s">string</span><span class="sh">"</span><span class="p">,</span>
                <span class="sh">"</span><span class="s">description</span><span class="sh">"</span><span class="p">:</span> <span class="sh">"</span><span class="s">The stock ticker symbol for a company, security, isin, or cusip.</span><span class="sh">"</span> 
            <span class="p">},</span>
            <span class="sh">"</span><span class="s">query</span><span class="sh">"</span><span class="p">:</span> <span class="p">{</span>
                <span class="sh">"</span><span class="s">type</span><span class="sh">"</span><span class="p">:</span> <span class="sh">"</span><span class="s">string</span><span class="sh">"</span><span class="p">,</span>
                <span class="sh">"</span><span class="s">description</span><span class="sh">"</span><span class="p">:</span> <span class="sh">"</span><span class="s">The question you</span><span class="sh">'</span><span class="s">re attempting to answer.</span><span class="sh">"</span>
            <span class="p">},</span>
            <span class="sh">"</span><span class="s">exchange</span><span class="sh">"</span><span class="p">:</span> <span class="p">{</span>
                <span class="sh">"</span><span class="s">type</span><span class="sh">"</span><span class="p">:</span> <span class="sh">"</span><span class="s">string</span><span class="sh">"</span><span class="p">,</span>
                <span class="sh">"</span><span class="s">description</span><span class="sh">"</span><span class="p">:</span> <span class="sh">"</span><span class="s">The exchange code used to filter quotes. This must always be </span><span class="sh">'</span><span class="s">US</span><span class="sh">'</span><span class="s">.</span><span class="sh">"</span>
            <span class="p">}</span>
        <span class="p">},</span>
        <span class="sh">"</span><span class="s">required</span><span class="sh">"</span><span class="p">:</span> <span class="p">[</span><span class="sh">"</span><span class="s">symbol</span><span class="sh">"</span><span class="p">,</span> <span class="sh">"</span><span class="s">query</span><span class="sh">"</span><span class="p">,</span> <span class="sh">"</span><span class="s">exchange</span><span class="sh">"</span><span class="p">]</span>
    <span class="p">}</span>
<span class="p">)</span>

<span class="n">decl_get_local_datetime</span> <span class="o">=</span> <span class="n">types</span><span class="p">.</span><span class="nc">FunctionDeclaration</span><span class="p">(</span>
    <span class="n">name</span><span class="o">=</span><span class="sh">"</span><span class="s">get_local_datetime</span><span class="sh">"</span><span class="p">,</span>
    <span class="n">description</span><span class="o">=</span><span class="sh">"""</span><span class="s">Converts an array of timestamps from epoch time to the local timezone format. The result is an array
                   of date and time in locale appropriate format. Suitable for use in a locale appropriate response.
                   Treat this function as a vector function. Always prefer to batch timestamps for conversion. Use this
                   function to format date and time in your responses.</span><span class="sh">"""</span><span class="p">,</span>
    <span class="n">parameters</span><span class="o">=</span><span class="p">{</span>
        <span class="sh">"</span><span class="s">type</span><span class="sh">"</span><span class="p">:</span> <span class="sh">"</span><span class="s">object</span><span class="sh">"</span><span class="p">,</span>
        <span class="sh">"</span><span class="s">properties</span><span class="sh">"</span><span class="p">:</span> <span class="p">{</span>
            <span class="sh">"</span><span class="s">t</span><span class="sh">"</span><span class="p">:</span> <span class="p">{</span>
                <span class="sh">"</span><span class="s">type</span><span class="sh">"</span><span class="p">:</span> <span class="sh">"</span><span class="s">array</span><span class="sh">"</span><span class="p">,</span>
                <span class="sh">"</span><span class="s">description</span><span class="sh">"</span><span class="p">:</span> <span class="sh">"""</span><span class="s">An array of timestamps in seconds since epoch to be converted. The order of
                                  timestamps matches the order of conversion.</span><span class="sh">"""</span><span class="p">,</span>
                <span class="sh">"</span><span class="s">items</span><span class="sh">"</span><span class="p">:</span> <span class="p">{</span>
                    <span class="sh">"</span><span class="s">type</span><span class="sh">"</span><span class="p">:</span> <span class="sh">"</span><span class="s">integer</span><span class="sh">"</span>
                <span class="p">}</span>
            <span class="p">}</span>
        <span class="p">},</span>
        <span class="sh">"</span><span class="s">required</span><span class="sh">"</span><span class="p">:</span> <span class="p">[</span><span class="sh">"</span><span class="s">t</span><span class="sh">"</span><span class="p">]</span>
    <span class="p">}</span>
<span class="p">)</span>

<span class="n">decl_get_market_status_1</span> <span class="o">=</span> <span class="n">types</span><span class="p">.</span><span class="nc">FunctionDeclaration</span><span class="p">(</span>
    <span class="n">name</span><span class="o">=</span><span class="sh">"</span><span class="s">get_market_status_1</span><span class="sh">"</span><span class="p">,</span>
    <span class="n">description</span><span class="o">=</span><span class="sh">"""</span><span class="s">Get the current market status of global exchanges. Includes whether exchanges are open or closed.  
                   Also includes holiday details if applicable. The response is provided in json format. Each response 
                   contains the following key-value pairs:

                   exchange: Exchange code,
                   timezone: Timezone of the exchange,
                    holiday: Holiday event name, or null if it</span><span class="sh">'</span><span class="s">s not a holiday,
                     isOpen: Whether the market is open at the moment,
                          t: Epoch timestamp of status in seconds (Eastern Time),
                    session: The market session can be 1 of the following values: 
                    
                    pre-market,regular,post-market when open, or null if closed.
                    
                    Parse the response and respond according to this information.</span><span class="sh">"""</span><span class="p">,</span>
    <span class="n">parameters</span><span class="o">=</span><span class="p">{</span>
        <span class="sh">"</span><span class="s">type</span><span class="sh">"</span><span class="p">:</span> <span class="sh">"</span><span class="s">object</span><span class="sh">"</span><span class="p">,</span>
        <span class="sh">"</span><span class="s">properties</span><span class="sh">"</span><span class="p">:</span> <span class="p">{</span>
            <span class="sh">"</span><span class="s">exchange</span><span class="sh">"</span><span class="p">:</span> <span class="p">{</span>
                <span class="sh">"</span><span class="s">type</span><span class="sh">"</span><span class="p">:</span> <span class="sh">"</span><span class="s">string</span><span class="sh">"</span><span class="p">,</span>
                <span class="sh">"</span><span class="s">description</span><span class="sh">"</span><span class="p">:</span> <span class="sh">"""</span><span class="s">The exchange code used to filter results. When not specified the default exchange 
                                  code you should use is </span><span class="sh">'</span><span class="s">US</span><span class="sh">'</span><span class="s"> for the US exchanges. A dictionary mapping all supported 
                                  exchange codes to their names be retrieved by calling get_exchange_codes_1. 
                                  Search for an exchange code to use by calling get_exchange_code_1, specifying the
                                  exchange code to search for.</span><span class="sh">"""</span>
            <span class="p">}</span>
        <span class="p">},</span>
        <span class="sh">"</span><span class="s">required</span><span class="sh">"</span><span class="p">:</span> <span class="p">[</span><span class="sh">"</span><span class="s">exchange</span><span class="sh">"</span><span class="p">]</span>
    <span class="p">}</span>
<span class="p">)</span>

<span class="n">decl_get_market_session_1</span> <span class="o">=</span> <span class="n">types</span><span class="p">.</span><span class="nc">FunctionDeclaration</span><span class="p">(</span>
    <span class="n">name</span><span class="o">=</span><span class="sh">"</span><span class="s">get_market_session_1</span><span class="sh">"</span><span class="p">,</span>
    <span class="n">description</span><span class="o">=</span><span class="sh">"</span><span class="s">Get the current market session of global exchanges.</span><span class="sh">"</span><span class="p">,</span>
    <span class="n">parameters</span><span class="o">=</span><span class="p">{</span>
        <span class="sh">"</span><span class="s">type</span><span class="sh">"</span><span class="p">:</span> <span class="sh">"</span><span class="s">object</span><span class="sh">"</span><span class="p">,</span>
        <span class="sh">"</span><span class="s">properties</span><span class="sh">"</span><span class="p">:</span> <span class="p">{</span>
            <span class="sh">"</span><span class="s">exchange</span><span class="sh">"</span><span class="p">:</span> <span class="p">{</span>
                <span class="sh">"</span><span class="s">type</span><span class="sh">"</span><span class="p">:</span> <span class="sh">"</span><span class="s">string</span><span class="sh">"</span><span class="p">,</span>
                <span class="sh">"</span><span class="s">description</span><span class="sh">"</span><span class="p">:</span> <span class="sh">"""</span><span class="s">The exchange code used to filter results. When not specified the default exchange 
                                  code you should use is </span><span class="sh">'</span><span class="s">US</span><span class="sh">'</span><span class="s"> for the US exchanges. A dictionary mapping all supported 
                                  exchange codes to their names be retrieved by calling get_exchange_codes_1. 
                                  Search for an exchange code to use by calling get_exchange_code_1, specifying the
                                  exchange code to search for.</span><span class="sh">"""</span>
            <span class="p">}</span>
        <span class="p">},</span>
        <span class="sh">"</span><span class="s">required</span><span class="sh">"</span><span class="p">:</span> <span class="p">[</span><span class="sh">"</span><span class="s">exchange</span><span class="sh">"</span><span class="p">]</span>
    <span class="p">}</span>
<span class="p">)</span>

<span class="n">decl_get_company_peers_1</span> <span class="o">=</span> <span class="n">types</span><span class="p">.</span><span class="nc">FunctionDeclaration</span><span class="p">(</span>
    <span class="n">name</span><span class="o">=</span><span class="sh">"</span><span class="s">get_company_peers_1</span><span class="sh">"</span><span class="p">,</span>
    <span class="n">description</span><span class="o">=</span><span class="sh">"""</span><span class="s">Search for a company</span><span class="sh">'</span><span class="s">s peers. Returns a list of peers operating in the same country and in the same
                   sector, industry, or subIndustry. Each response contains the following key-value pairs: 
                   
                   symbol: The company</span><span class="sh">'</span><span class="s">s stock ticker symbol, 
                   peers: A list containing the peers.
                   
                   Each peers entry contains the following key-value pairs:
                   
                   symbol: The peer company</span><span class="sh">'</span><span class="s">s stock ticker symbol, 
                   name: The peer company</span><span class="sh">'</span><span class="s">s name.
                   
                   Parse the response and respond according to this information.</span><span class="sh">"""</span><span class="p">,</span>
    <span class="n">parameters</span><span class="o">=</span><span class="p">{</span>
        <span class="sh">"</span><span class="s">type</span><span class="sh">"</span><span class="p">:</span> <span class="sh">"</span><span class="s">object</span><span class="sh">"</span><span class="p">,</span>
        <span class="sh">"</span><span class="s">properties</span><span class="sh">"</span><span class="p">:</span> <span class="p">{</span>
            <span class="sh">"</span><span class="s">symbol</span><span class="sh">"</span><span class="p">:</span> <span class="p">{</span>
                <span class="sh">"</span><span class="s">type</span><span class="sh">"</span><span class="p">:</span> <span class="sh">"</span><span class="s">string</span><span class="sh">"</span><span class="p">,</span>
                <span class="sh">"</span><span class="s">description</span><span class="sh">"</span><span class="p">:</span> <span class="sh">"</span><span class="s">The stock ticker symbol of a company to obtain peers.</span><span class="sh">"</span>
            <span class="p">},</span>
            <span class="sh">"</span><span class="s">grouping</span><span class="sh">"</span><span class="p">:</span> <span class="p">{</span>
                <span class="sh">"</span><span class="s">type</span><span class="sh">"</span><span class="p">:</span> <span class="sh">"</span><span class="s">string</span><span class="sh">"</span><span class="p">,</span>
                <span class="sh">"</span><span class="s">description</span><span class="sh">"</span><span class="p">:</span> <span class="sh">"""</span><span class="s">This parameter may be one of the following values: sector, industry, subIndustry.
                                  Always use subIndustry unless told otherwise.</span><span class="sh">"""</span>
            <span class="p">},</span>
            <span class="sh">"</span><span class="s">exchange</span><span class="sh">"</span><span class="p">:</span> <span class="p">{</span>
                <span class="sh">"</span><span class="s">type</span><span class="sh">"</span><span class="p">:</span> <span class="sh">"</span><span class="s">string</span><span class="sh">"</span><span class="p">,</span>
                <span class="sh">"</span><span class="s">description</span><span class="sh">"</span><span class="p">:</span> <span class="sh">"""</span><span class="s">The exchange code used to filter results. When not specified the default exchange 
                                  code you should use is </span><span class="sh">'</span><span class="s">US</span><span class="sh">'</span><span class="s"> for the US exchanges. A dictionary mapping all supported 
                                  exchange codes to their names be retrieved by calling get_exchange_codes_1. 
                                  Search for an exchange code to use by calling get_exchange_code_1, specifying the
                                  exchange code to search for.</span><span class="sh">"""</span>
            <span class="p">},</span>
            <span class="sh">"</span><span class="s">query</span><span class="sh">"</span><span class="p">:</span> <span class="p">{</span>
                <span class="sh">"</span><span class="s">type</span><span class="sh">"</span><span class="p">:</span> <span class="sh">"</span><span class="s">string</span><span class="sh">"</span><span class="p">,</span>
                <span class="sh">"</span><span class="s">description</span><span class="sh">"</span><span class="p">:</span> <span class="sh">"</span><span class="s">The question you</span><span class="sh">'</span><span class="s">re attempting to answer.</span><span class="sh">"</span>
            <span class="p">}</span>
        <span class="p">},</span>
        <span class="sh">"</span><span class="s">required</span><span class="sh">"</span><span class="p">:</span> <span class="p">[</span><span class="sh">"</span><span class="s">symbol</span><span class="sh">"</span><span class="p">,</span> <span class="sh">"</span><span class="s">grouping</span><span class="sh">"</span><span class="p">,</span> <span class="sh">"</span><span class="s">exchange</span><span class="sh">"</span><span class="p">,</span> <span class="sh">"</span><span class="s">query</span><span class="sh">"</span><span class="p">]</span>
    <span class="p">}</span>
<span class="p">)</span>

<span class="n">decl_get_exchange_codes_1</span> <span class="o">=</span> <span class="n">types</span><span class="p">.</span><span class="nc">FunctionDeclaration</span><span class="p">(</span>
    <span class="n">name</span><span class="o">=</span><span class="sh">"</span><span class="s">get_exchange_codes_1</span><span class="sh">"</span><span class="p">,</span>
    <span class="n">description</span><span class="o">=</span><span class="sh">"""</span><span class="s">Get a dictionary mapping all supported exchange codes to their names.</span><span class="sh">"""</span>
<span class="p">)</span>

<span class="n">decl_get_exchange_code_1</span> <span class="o">=</span> <span class="n">types</span><span class="p">.</span><span class="nc">FunctionDeclaration</span><span class="p">(</span>
    <span class="n">name</span><span class="o">=</span><span class="sh">"</span><span class="s">get_exchange_code_1</span><span class="sh">"</span><span class="p">,</span>
    <span class="n">description</span><span class="o">=</span><span class="sh">"""</span><span class="s">Search for the exchange code to use when filtering by exchange. The result will be one or
                   more exchange codes provided as a comma-separated string value.</span><span class="sh">"""</span><span class="p">,</span>
    <span class="n">parameters</span><span class="o">=</span><span class="p">{</span>
        <span class="sh">"</span><span class="s">type</span><span class="sh">"</span><span class="p">:</span> <span class="sh">"</span><span class="s">object</span><span class="sh">"</span><span class="p">,</span>
        <span class="sh">"</span><span class="s">properties</span><span class="sh">"</span><span class="p">:</span> <span class="p">{</span>
            <span class="sh">"</span><span class="s">q</span><span class="sh">"</span><span class="p">:</span> <span class="p">{</span>
                <span class="sh">"</span><span class="s">type</span><span class="sh">"</span><span class="p">:</span> <span class="sh">"</span><span class="s">string</span><span class="sh">"</span><span class="p">,</span>
                <span class="sh">"</span><span class="s">description</span><span class="sh">"</span><span class="p">:</span> <span class="sh">"</span><span class="s">Specifies which exchange code to search for.</span><span class="sh">"</span>
            <span class="p">}</span>
        <span class="p">},</span>
        <span class="sh">"</span><span class="s">required</span><span class="sh">"</span><span class="p">:</span> <span class="p">[</span><span class="sh">"</span><span class="s">q</span><span class="sh">"</span><span class="p">]</span>
    <span class="p">}</span>
<span class="p">)</span>

<span class="n">decl_get_financials_1</span> <span class="o">=</span> <span class="n">types</span><span class="p">.</span><span class="nc">FunctionDeclaration</span><span class="p">(</span>
    <span class="n">name</span><span class="o">=</span><span class="sh">"</span><span class="s">get_financials_1</span><span class="sh">"</span><span class="p">,</span>
    <span class="n">description</span><span class="o">=</span><span class="sh">"""</span><span class="s">Get company basic financials such as margin, P/E ratio, 52-week high/low, etc. Parse the response for 
                   key-value pairs in json format and interpret their meaning as stock market financial indicators.</span><span class="sh">"""</span><span class="p">,</span>
    <span class="n">parameters</span><span class="o">=</span><span class="p">{</span>
        <span class="sh">"</span><span class="s">type</span><span class="sh">"</span><span class="p">:</span> <span class="sh">"</span><span class="s">object</span><span class="sh">"</span><span class="p">,</span>
        <span class="sh">"</span><span class="s">properties</span><span class="sh">"</span><span class="p">:</span> <span class="p">{</span>
            <span class="sh">"</span><span class="s">symbol</span><span class="sh">"</span><span class="p">:</span> <span class="p">{</span>
                <span class="sh">"</span><span class="s">type</span><span class="sh">"</span><span class="p">:</span> <span class="sh">"</span><span class="s">string</span><span class="sh">"</span><span class="p">,</span>
                <span class="sh">"</span><span class="s">description</span><span class="sh">"</span><span class="p">:</span> <span class="sh">"</span><span class="s">Stock ticker symbol for a company.</span><span class="sh">"</span>
            <span class="p">},</span>
            <span class="sh">"</span><span class="s">metric</span><span class="sh">"</span><span class="p">:</span> <span class="p">{</span>
                <span class="sh">"</span><span class="s">type</span><span class="sh">"</span><span class="p">:</span> <span class="sh">"</span><span class="s">string</span><span class="sh">"</span><span class="p">,</span>
                <span class="sh">"</span><span class="s">description</span><span class="sh">"</span><span class="p">:</span> <span class="sh">"</span><span class="s">It must always be declared as the value </span><span class="sh">'</span><span class="s">all</span><span class="sh">'"</span>
            <span class="p">},</span>
            <span class="sh">"</span><span class="s">query</span><span class="sh">"</span><span class="p">:</span> <span class="p">{</span>
                <span class="sh">"</span><span class="s">type</span><span class="sh">"</span><span class="p">:</span> <span class="sh">"</span><span class="s">string</span><span class="sh">"</span><span class="p">,</span>
                <span class="sh">"</span><span class="s">description</span><span class="sh">"</span><span class="p">:</span> <span class="sh">"</span><span class="s">The question you</span><span class="sh">'</span><span class="s">re attempting to answer.</span><span class="sh">"</span>
            <span class="p">}</span>
        <span class="p">},</span>
        <span class="sh">"</span><span class="s">required</span><span class="sh">"</span><span class="p">:</span> <span class="p">[</span><span class="sh">"</span><span class="s">symbol</span><span class="sh">"</span><span class="p">,</span> <span class="sh">"</span><span class="s">metric</span><span class="sh">"</span><span class="p">,</span> <span class="sh">"</span><span class="s">query</span><span class="sh">"</span><span class="p">]</span>
    <span class="p">}</span>
<span class="p">)</span>

<span class="n">decl_get_daily_candlestick_2</span> <span class="o">=</span> <span class="n">types</span><span class="p">.</span><span class="nc">FunctionDeclaration</span><span class="p">(</span>
    <span class="n">name</span><span class="o">=</span><span class="sh">"</span><span class="s">get_daily_candlestick_2</span><span class="sh">"</span><span class="p">,</span>
    <span class="n">description</span><span class="o">=</span><span class="sh">"""</span><span class="s">Get a historical daily stock ticker candlestick / aggregate bar (OHLC). 
                   Includes historical daily open, high, low, and close prices. Also includes historical daily trade
                   volume and pre-market/after-hours trade prices. It provides the last trading days</span><span class="sh">'</span><span class="s"> data after 
                   11:59PM Eastern Time.</span><span class="sh">"""</span><span class="p">,</span>
    <span class="n">parameters</span><span class="o">=</span><span class="p">{</span>
        <span class="sh">"</span><span class="s">type</span><span class="sh">"</span><span class="p">:</span> <span class="sh">"</span><span class="s">object</span><span class="sh">"</span><span class="p">,</span>
        <span class="sh">"</span><span class="s">properties</span><span class="sh">"</span><span class="p">:</span> <span class="p">{</span>
            <span class="sh">"</span><span class="s">stocksTicker</span><span class="sh">"</span><span class="p">:</span> <span class="p">{</span>
                <span class="sh">"</span><span class="s">type</span><span class="sh">"</span><span class="p">:</span> <span class="sh">"</span><span class="s">string</span><span class="sh">"</span><span class="p">,</span>
                <span class="sh">"</span><span class="s">description</span><span class="sh">"</span><span class="p">:</span> <span class="sh">"</span><span class="s">The stock ticker symbol of a company to search for.</span><span class="sh">"</span><span class="p">,</span>
            <span class="p">},</span>
            <span class="sh">"</span><span class="s">date</span><span class="sh">"</span><span class="p">:</span> <span class="p">{</span>
                <span class="sh">"</span><span class="s">type</span><span class="sh">"</span><span class="p">:</span> <span class="sh">"</span><span class="s">string</span><span class="sh">"</span><span class="p">,</span>
                <span class="sh">"</span><span class="s">format</span><span class="sh">"</span><span class="p">:</span> <span class="sh">"</span><span class="s">date-time</span><span class="sh">"</span><span class="p">,</span>
                <span class="sh">"</span><span class="s">description</span><span class="sh">"</span><span class="p">:</span> <span class="sh">"""</span><span class="s">The date of the requested candlestick in format YYYY-MM-DD.</span><span class="sh">"""</span>
            <span class="p">},</span>
            <span class="sh">"</span><span class="s">adjusted</span><span class="sh">"</span><span class="p">:</span> <span class="p">{</span>
                <span class="sh">"</span><span class="s">type</span><span class="sh">"</span><span class="p">:</span> <span class="sh">"</span><span class="s">string</span><span class="sh">"</span><span class="p">,</span>
                <span class="sh">"</span><span class="s">description</span><span class="sh">"</span><span class="p">:</span> <span class="sh">"""</span><span class="s">May be true or false. Indicates if the results should be adjusted for splits.
                                  Use true unless told otherwise.</span><span class="sh">"""</span>
            <span class="p">},</span>
            <span class="sh">"</span><span class="s">exchange</span><span class="sh">"</span><span class="p">:</span> <span class="p">{</span>
                <span class="sh">"</span><span class="s">type</span><span class="sh">"</span><span class="p">:</span> <span class="sh">"</span><span class="s">string</span><span class="sh">"</span><span class="p">,</span>
                <span class="sh">"</span><span class="s">description</span><span class="sh">"</span><span class="p">:</span> <span class="sh">"""</span><span class="s">The exchange code used to filter results. When not specified the default exchange 
                                  code you should use is </span><span class="sh">'</span><span class="s">US</span><span class="sh">'</span><span class="s"> for the US exchanges. A dictionary mapping all supported 
                                  exchange codes to their names be retrieved by calling get_exchange_codes_1. 
                                  Search for an exchange code to use by calling get_exchange_code_1, specifying the
                                  exchange code to search for.</span><span class="sh">"""</span>
            <span class="p">},</span>
            <span class="sh">"</span><span class="s">query</span><span class="sh">"</span><span class="p">:</span> <span class="p">{</span>
                <span class="sh">"</span><span class="s">type</span><span class="sh">"</span><span class="p">:</span> <span class="sh">"</span><span class="s">string</span><span class="sh">"</span><span class="p">,</span>
                <span class="sh">"</span><span class="s">description</span><span class="sh">"</span><span class="p">:</span> <span class="sh">"</span><span class="s">The question you</span><span class="sh">'</span><span class="s">re attempting to answer.</span><span class="sh">"</span>
            <span class="p">}</span>
        <span class="p">},</span>
        <span class="sh">"</span><span class="s">required</span><span class="sh">"</span><span class="p">:</span> <span class="p">[</span><span class="sh">"</span><span class="s">stocksTicker</span><span class="sh">"</span><span class="p">,</span> <span class="sh">"</span><span class="s">date</span><span class="sh">"</span><span class="p">,</span> <span class="sh">"</span><span class="s">adjusted</span><span class="sh">"</span><span class="p">,</span> <span class="sh">"</span><span class="s">exchange</span><span class="sh">"</span><span class="p">,</span> <span class="sh">"</span><span class="s">query</span><span class="sh">"</span><span class="p">]</span>
    <span class="p">},</span>
<span class="p">)</span>

<span class="n">decl_get_company_news_1</span> <span class="o">=</span> <span class="n">types</span><span class="p">.</span><span class="nc">FunctionDeclaration</span><span class="p">(</span>
    <span class="n">name</span><span class="o">=</span><span class="sh">"</span><span class="s">get_company_news_1</span><span class="sh">"</span><span class="p">,</span>
    <span class="n">description</span><span class="o">=</span><span class="sh">"</span><span class="s">Retrieve the most recent news articles related to a specified ticker.</span><span class="sh">"</span><span class="p">,</span>
    <span class="n">parameters</span><span class="o">=</span><span class="p">{</span>
        <span class="sh">"</span><span class="s">type</span><span class="sh">"</span><span class="p">:</span> <span class="sh">"</span><span class="s">object</span><span class="sh">"</span><span class="p">,</span>
        <span class="sh">"</span><span class="s">properties</span><span class="sh">"</span><span class="p">:</span> <span class="p">{</span>
            <span class="sh">"</span><span class="s">symbol</span><span class="sh">"</span><span class="p">:</span> <span class="p">{</span>
                <span class="sh">"</span><span class="s">type</span><span class="sh">"</span><span class="p">:</span> <span class="sh">"</span><span class="s">string</span><span class="sh">"</span><span class="p">,</span>
                <span class="sh">"</span><span class="s">description</span><span class="sh">"</span><span class="p">:</span> <span class="sh">"</span><span class="s">Stock ticker symbol for a company.</span><span class="sh">"</span><span class="p">,</span>
            <span class="p">},</span>
            <span class="sh">"</span><span class="s">from</span><span class="sh">"</span><span class="p">:</span> <span class="p">{</span>
                <span class="sh">"</span><span class="s">type</span><span class="sh">"</span><span class="p">:</span> <span class="sh">"</span><span class="s">string</span><span class="sh">"</span><span class="p">,</span>
                <span class="sh">"</span><span class="s">format</span><span class="sh">"</span><span class="p">:</span> <span class="sh">"</span><span class="s">date-time</span><span class="sh">"</span><span class="p">,</span>
                <span class="sh">"</span><span class="s">description</span><span class="sh">"</span><span class="p">:</span> <span class="sh">"""</span><span class="s">A date in format YYYY-MM-DD. It must be older than the parameter </span><span class="sh">'</span><span class="s">to</span><span class="sh">'</span><span class="s">.</span><span class="sh">"""</span>
            <span class="p">},</span>
            <span class="sh">"</span><span class="s">to</span><span class="sh">"</span><span class="p">:</span> <span class="p">{</span>
                <span class="sh">"</span><span class="s">type</span><span class="sh">"</span><span class="p">:</span> <span class="sh">"</span><span class="s">string</span><span class="sh">"</span><span class="p">,</span>
                <span class="sh">"</span><span class="s">format</span><span class="sh">"</span><span class="p">:</span> <span class="sh">"</span><span class="s">date-time</span><span class="sh">"</span><span class="p">,</span>
                <span class="sh">"</span><span class="s">description</span><span class="sh">"</span><span class="p">:</span> <span class="sh">"""</span><span class="s">A date in format YYYY-MM-DD. It must be more recent than the parameter </span><span class="sh">'</span><span class="s">from</span><span class="sh">'</span><span class="s">. The
                                  default value is today</span><span class="sh">'</span><span class="s">s date.</span><span class="sh">"""</span>
            <span class="p">},</span>
            <span class="sh">"</span><span class="s">query</span><span class="sh">"</span><span class="p">:</span> <span class="p">{</span>
                <span class="sh">"</span><span class="s">type</span><span class="sh">"</span><span class="p">:</span> <span class="sh">"</span><span class="s">string</span><span class="sh">"</span><span class="p">,</span>
                <span class="sh">"</span><span class="s">description</span><span class="sh">"</span><span class="p">:</span> <span class="sh">"</span><span class="s">The question you</span><span class="sh">'</span><span class="s">re attempting to answer.</span><span class="sh">"</span>
            <span class="p">}</span>
        <span class="p">},</span>
        <span class="sh">"</span><span class="s">required</span><span class="sh">"</span><span class="p">:</span> <span class="p">[</span><span class="sh">"</span><span class="s">symbol</span><span class="sh">"</span><span class="p">,</span> <span class="sh">"</span><span class="s">from</span><span class="sh">"</span><span class="p">,</span> <span class="sh">"</span><span class="s">to</span><span class="sh">"</span><span class="p">,</span> <span class="sh">"</span><span class="s">query</span><span class="sh">"</span><span class="p">]</span>
    <span class="p">},</span>
<span class="p">)</span>

<span class="n">decl_get_custom_candlestick_2</span> <span class="o">=</span> <span class="n">types</span><span class="p">.</span><span class="nc">FunctionDeclaration</span><span class="p">(</span>
    <span class="n">name</span><span class="o">=</span><span class="sh">"</span><span class="s">get_custom_candlestick_2</span><span class="sh">"</span><span class="p">,</span>
    <span class="n">description</span><span class="o">=</span><span class="sh">"""</span><span class="s">Get a historical stock ticker candlestick / aggregate bar (OHLC) over a custom date range and 
                   time interval in Eastern Time. Includes historical open, high, low, and close prices. Also 
                   includes historical daily trade volume and pre-market/after-hours trade prices. It includes 
                   the last trading days</span><span class="sh">'</span><span class="s"> data after 11:59PM Eastern Time.</span><span class="sh">"""</span><span class="p">,</span>
    <span class="n">parameters</span><span class="o">=</span><span class="p">{</span>
        <span class="sh">"</span><span class="s">type</span><span class="sh">"</span><span class="p">:</span> <span class="sh">"</span><span class="s">object</span><span class="sh">"</span><span class="p">,</span>
        <span class="sh">"</span><span class="s">properties</span><span class="sh">"</span><span class="p">:</span> <span class="p">{</span>
            <span class="sh">"</span><span class="s">stocksTicker</span><span class="sh">"</span><span class="p">:</span> <span class="p">{</span>
                <span class="sh">"</span><span class="s">type</span><span class="sh">"</span><span class="p">:</span> <span class="sh">"</span><span class="s">string</span><span class="sh">"</span><span class="p">,</span>
                <span class="sh">"</span><span class="s">description</span><span class="sh">"</span><span class="p">:</span> <span class="sh">"</span><span class="s">The stock ticker symbol of a company to search for.</span><span class="sh">"</span><span class="p">,</span>
            <span class="p">},</span>
            <span class="sh">"</span><span class="s">multiplier</span><span class="sh">"</span><span class="p">:</span> <span class="p">{</span>
                <span class="sh">"</span><span class="s">type</span><span class="sh">"</span><span class="p">:</span> <span class="sh">"</span><span class="s">integer</span><span class="sh">"</span><span class="p">,</span>
                <span class="sh">"</span><span class="s">description</span><span class="sh">"</span><span class="p">:</span> <span class="sh">"</span><span class="s">This must be included and equal to 1 unless told otherwise.</span><span class="sh">"</span>
            <span class="p">},</span>
            <span class="sh">"</span><span class="s">timespan</span><span class="sh">"</span><span class="p">:</span> <span class="p">{</span>
                <span class="sh">"</span><span class="s">type</span><span class="sh">"</span><span class="p">:</span> <span class="sh">"</span><span class="s">string</span><span class="sh">"</span><span class="p">,</span>
                <span class="sh">"</span><span class="s">description</span><span class="sh">"</span><span class="p">:</span> <span class="sh">"""</span><span class="s">The size of the candlestick</span><span class="sh">'</span><span class="s">s time window. This is allowed to be one of the following:
                                  second, minute, hour, day, week, month, quarter, or year. The default value is day.</span><span class="sh">"""</span>
            <span class="p">},</span>
            <span class="sh">"</span><span class="s">from</span><span class="sh">"</span><span class="p">:</span> <span class="p">{</span>
                <span class="sh">"</span><span class="s">type</span><span class="sh">"</span><span class="p">:</span> <span class="sh">"</span><span class="s">string</span><span class="sh">"</span><span class="p">,</span>
                <span class="sh">"</span><span class="s">format</span><span class="sh">"</span><span class="p">:</span> <span class="sh">"</span><span class="s">date-time</span><span class="sh">"</span><span class="p">,</span>
                <span class="sh">"</span><span class="s">description</span><span class="sh">"</span><span class="p">:</span> <span class="sh">"""</span><span class="s">A date in format YYYY-MM-DD must be older than the parameter </span><span class="sh">'</span><span class="s">to</span><span class="sh">'</span><span class="s">.</span><span class="sh">"""</span>
            <span class="p">},</span>
            <span class="sh">"</span><span class="s">to</span><span class="sh">"</span><span class="p">:</span> <span class="p">{</span>
                <span class="sh">"</span><span class="s">type</span><span class="sh">"</span><span class="p">:</span> <span class="sh">"</span><span class="s">string</span><span class="sh">"</span><span class="p">,</span>
                <span class="sh">"</span><span class="s">format</span><span class="sh">"</span><span class="p">:</span> <span class="sh">"</span><span class="s">date-time</span><span class="sh">"</span><span class="p">,</span>
                <span class="sh">"</span><span class="s">description</span><span class="sh">"</span><span class="p">:</span> <span class="sh">"""</span><span class="s">A date in format YYYY-MM-DD must be more recent than the parameter </span><span class="sh">'</span><span class="s">from</span><span class="sh">'</span><span class="s">. The 
                                  default is one weekday before get_last_market_close.
                                  Replace more recent dates with the default.</span><span class="sh">"""</span>
            <span class="p">},</span>
            <span class="sh">"</span><span class="s">adjusted</span><span class="sh">"</span><span class="p">:</span> <span class="p">{</span>
                <span class="sh">"</span><span class="s">type</span><span class="sh">"</span><span class="p">:</span> <span class="sh">"</span><span class="s">string</span><span class="sh">"</span><span class="p">,</span>
                <span class="sh">"</span><span class="s">description</span><span class="sh">"</span><span class="p">:</span> <span class="sh">"""</span><span class="s">May be true or false. Indicates if the results should be adjusted for splits.
                                  Use true unless told otherwise.</span><span class="sh">"""</span>
            <span class="p">},</span>
            <span class="sh">"</span><span class="s">sort</span><span class="sh">"</span><span class="p">:</span> <span class="p">{</span>
                <span class="sh">"</span><span class="s">type</span><span class="sh">"</span><span class="p">:</span> <span class="sh">"</span><span class="s">string</span><span class="sh">"</span><span class="p">,</span>
                <span class="sh">"</span><span class="s">description</span><span class="sh">"</span><span class="p">:</span> <span class="sh">"""</span><span class="s">This must be included. May be one of asc or desc. asc will sort by timestmap in 
                                  ascending order. desc will sort by timestamp in descending order.</span><span class="sh">"""</span>
            <span class="p">},</span>
            <span class="sh">"</span><span class="s">limit</span><span class="sh">"</span><span class="p">:</span> <span class="p">{</span>
                <span class="sh">"</span><span class="s">type</span><span class="sh">"</span><span class="p">:</span> <span class="sh">"</span><span class="s">integer</span><span class="sh">"</span><span class="p">,</span>
                <span class="sh">"</span><span class="s">description</span><span class="sh">"</span><span class="p">:</span> <span class="sh">"""</span><span class="s">Set the number of base aggregates used to create this candlestick. This must be 5000 
                                  unless told to limit base aggregates to something else.</span><span class="sh">"""</span>
            <span class="p">},</span>
            <span class="sh">"</span><span class="s">query</span><span class="sh">"</span><span class="p">:</span> <span class="p">{</span>
                <span class="sh">"</span><span class="s">type</span><span class="sh">"</span><span class="p">:</span> <span class="sh">"</span><span class="s">string</span><span class="sh">"</span><span class="p">,</span>
                <span class="sh">"</span><span class="s">description</span><span class="sh">"</span><span class="p">:</span> <span class="sh">"</span><span class="s">The question you</span><span class="sh">'</span><span class="s">re attempting to answer.</span><span class="sh">"</span>
            <span class="p">}</span>
        <span class="p">},</span>
        <span class="sh">"</span><span class="s">required</span><span class="sh">"</span><span class="p">:</span> <span class="p">[</span><span class="sh">"</span><span class="s">stocksTicker</span><span class="sh">"</span><span class="p">,</span> <span class="sh">"</span><span class="s">multiplier</span><span class="sh">"</span><span class="p">,</span> <span class="sh">"</span><span class="s">timespan</span><span class="sh">"</span><span class="p">,</span> <span class="sh">"</span><span class="s">from</span><span class="sh">"</span><span class="p">,</span> <span class="sh">"</span><span class="s">to</span><span class="sh">"</span><span class="p">,</span> <span class="sh">"</span><span class="s">adjusted</span><span class="sh">"</span><span class="p">,</span> <span class="sh">"</span><span class="s">sort</span><span class="sh">"</span><span class="p">,</span> <span class="sh">"</span><span class="s">limit</span><span class="sh">"</span><span class="p">,</span> <span class="sh">"</span><span class="s">query</span><span class="sh">"</span><span class="p">]</span>
    <span class="p">},</span>
<span class="p">)</span>

<span class="n">decl_get_last_market_close</span> <span class="o">=</span> <span class="n">types</span><span class="p">.</span><span class="nc">FunctionDeclaration</span><span class="p">(</span>
    <span class="n">name</span><span class="o">=</span><span class="sh">"</span><span class="s">get_last_market_close</span><span class="sh">"</span><span class="p">,</span>
    <span class="n">description</span><span class="o">=</span><span class="sh">"""</span><span class="s">Get the last market close of the specified exchange in Eastern Time. The response has already
                   been converted by get_local_datetime so this step should be skipped.</span><span class="sh">"""</span><span class="p">,</span>
    <span class="n">parameters</span><span class="o">=</span><span class="p">{</span>
        <span class="sh">"</span><span class="s">type</span><span class="sh">"</span><span class="p">:</span> <span class="sh">"</span><span class="s">object</span><span class="sh">"</span><span class="p">,</span>
        <span class="sh">"</span><span class="s">properties</span><span class="sh">"</span><span class="p">:</span> <span class="p">{</span>
            <span class="sh">"</span><span class="s">exchange</span><span class="sh">"</span><span class="p">:</span> <span class="p">{</span>
                <span class="sh">"</span><span class="s">type</span><span class="sh">"</span><span class="p">:</span> <span class="sh">"</span><span class="s">string</span><span class="sh">"</span><span class="p">,</span>
                <span class="sh">"</span><span class="s">description</span><span class="sh">"</span><span class="p">:</span> <span class="sh">"""</span><span class="s">The exchange code used to filter results. When not specified the default exchange 
                                  code you should use is </span><span class="sh">'</span><span class="s">US</span><span class="sh">'</span><span class="s"> for the US exchanges. A dictionary mapping all supported 
                                  exchange codes to their names be retrieved by calling get_exchange_codes_1. 
                                  Search for an exchange code to use by calling get_exchange_code_1, specifying the
                                  exchange code to search for.</span><span class="sh">"""</span>
            <span class="p">}</span>
        <span class="p">},</span>
        <span class="sh">"</span><span class="s">required</span><span class="sh">"</span><span class="p">:</span> <span class="p">[</span><span class="sh">"</span><span class="s">exchange</span><span class="sh">"</span><span class="p">]</span>
    <span class="p">}</span>
<span class="p">)</span>

<span class="n">decl_get_ticker_overview_2</span> <span class="o">=</span> <span class="n">types</span><span class="p">.</span><span class="nc">FunctionDeclaration</span><span class="p">(</span>
    <span class="n">name</span><span class="o">=</span><span class="sh">"</span><span class="s">get_ticker_overview_2</span><span class="sh">"</span><span class="p">,</span>
    <span class="n">description</span><span class="o">=</span><span class="sh">"""</span><span class="s">Retrieve comprehensive details for a single ticker symbol. It</span><span class="sh">'</span><span class="s">s a deep look into a company’s 
    fundamental attributes, including its primary exchange, standardized identifiers (CIK, composite FIGI, 
    share class FIGI), market capitalization, industry classification, and key dates. Also includes branding assets in
    the form of icons and logos.
    </span><span class="sh">"""</span><span class="p">,</span>
    <span class="n">parameters</span><span class="o">=</span><span class="p">{</span>
        <span class="sh">"</span><span class="s">type</span><span class="sh">"</span><span class="p">:</span> <span class="sh">"</span><span class="s">object</span><span class="sh">"</span><span class="p">,</span>
        <span class="sh">"</span><span class="s">properties</span><span class="sh">"</span><span class="p">:</span> <span class="p">{</span>
            <span class="sh">"</span><span class="s">ticker</span><span class="sh">"</span><span class="p">:</span> <span class="p">{</span>
                <span class="sh">"</span><span class="s">type</span><span class="sh">"</span><span class="p">:</span> <span class="sh">"</span><span class="s">string</span><span class="sh">"</span><span class="p">,</span>
                <span class="sh">"</span><span class="s">description</span><span class="sh">"</span><span class="p">:</span> <span class="sh">"</span><span class="s">Stock ticker symbol of a company.</span><span class="sh">"</span>
            <span class="p">},</span>
            <span class="sh">"</span><span class="s">query</span><span class="sh">"</span><span class="p">:</span> <span class="p">{</span>
                <span class="sh">"</span><span class="s">type</span><span class="sh">"</span><span class="p">:</span> <span class="sh">"</span><span class="s">string</span><span class="sh">"</span><span class="p">,</span>
                <span class="sh">"</span><span class="s">description</span><span class="sh">"</span><span class="p">:</span> <span class="sh">"</span><span class="s">The question you</span><span class="sh">'</span><span class="s">re attempting to answer.</span><span class="sh">"</span>
            <span class="p">}</span>
        <span class="p">},</span>
        <span class="sh">"</span><span class="s">required</span><span class="sh">"</span><span class="p">:</span> <span class="p">[</span><span class="sh">"</span><span class="s">ticker</span><span class="sh">"</span><span class="p">,</span> <span class="sh">"</span><span class="s">query</span><span class="sh">"</span><span class="p">]</span>
    <span class="p">}</span>
<span class="p">)</span>

<span class="n">decl_get_recommendation_trends_1</span> <span class="o">=</span> <span class="n">types</span><span class="p">.</span><span class="nc">FunctionDeclaration</span><span class="p">(</span>
    <span class="n">name</span><span class="o">=</span><span class="sh">"</span><span class="s">get_recommendation_trends_1</span><span class="sh">"</span><span class="p">,</span>
    <span class="n">description</span><span class="o">=</span><span class="sh">"""</span><span class="s">Get the latest analyst recommendation trends for a company.
                The data includes the latest recommendations as well as historical
                recommendation data for each month. The data is classified according
                to these categories: strongBuy, buy, hold, sell, and strongSell.
                The date of a recommendation indicated by the value of </span><span class="sh">'</span><span class="s">period</span><span class="sh">'</span><span class="s">.</span><span class="sh">"""</span><span class="p">,</span>
    <span class="n">parameters</span><span class="o">=</span><span class="p">{</span>
        <span class="sh">"</span><span class="s">type</span><span class="sh">"</span><span class="p">:</span> <span class="sh">"</span><span class="s">object</span><span class="sh">"</span><span class="p">,</span>
        <span class="sh">"</span><span class="s">properties</span><span class="sh">"</span><span class="p">:</span> <span class="p">{</span>
            <span class="sh">"</span><span class="s">symbol</span><span class="sh">"</span><span class="p">:</span> <span class="p">{</span>
                <span class="sh">"</span><span class="s">type</span><span class="sh">"</span><span class="p">:</span> <span class="sh">"</span><span class="s">string</span><span class="sh">"</span><span class="p">,</span>
                <span class="sh">"</span><span class="s">description</span><span class="sh">"</span><span class="p">:</span> <span class="sh">"</span><span class="s">Stock ticker symbol for a company.</span><span class="sh">"</span>
            <span class="p">},</span>
            <span class="sh">"</span><span class="s">query</span><span class="sh">"</span><span class="p">:</span> <span class="p">{</span>
                <span class="sh">"</span><span class="s">type</span><span class="sh">"</span><span class="p">:</span> <span class="sh">"</span><span class="s">string</span><span class="sh">"</span><span class="p">,</span>
                <span class="sh">"</span><span class="s">description</span><span class="sh">"</span><span class="p">:</span> <span class="sh">"</span><span class="s">The question you</span><span class="sh">'</span><span class="s">re attempting to answer.</span><span class="sh">"</span>
            <span class="p">}</span>
        <span class="p">},</span>
        <span class="sh">"</span><span class="s">required</span><span class="sh">"</span><span class="p">:</span> <span class="p">[</span><span class="sh">"</span><span class="s">symbol</span><span class="sh">"</span><span class="p">,</span> <span class="sh">"</span><span class="s">query</span><span class="sh">"</span><span class="p">]</span>
    <span class="p">}</span>
<span class="p">)</span>

<span class="n">decl_get_news_with_sentiment_2</span> <span class="o">=</span> <span class="n">types</span><span class="p">.</span><span class="nc">FunctionDeclaration</span><span class="p">(</span>
    <span class="n">name</span><span class="o">=</span><span class="sh">"</span><span class="s">get_news_with_sentiment_2</span><span class="sh">"</span><span class="p">,</span>
    <span class="n">description</span><span class="o">=</span><span class="sh">"""</span><span class="s">Retrieve the most recent news articles related to a specified ticker. Each article includes 
                   comprehensive coverage. Including a summary, publisher information, article metadata, 
                   and sentiment analysis.</span><span class="sh">"""</span><span class="p">,</span>
    <span class="n">parameters</span><span class="o">=</span><span class="p">{</span>
        <span class="sh">"</span><span class="s">type</span><span class="sh">"</span><span class="p">:</span> <span class="sh">"</span><span class="s">object</span><span class="sh">"</span><span class="p">,</span>
        <span class="sh">"</span><span class="s">properties</span><span class="sh">"</span><span class="p">:</span> <span class="p">{</span>
            <span class="sh">"</span><span class="s">ticker</span><span class="sh">"</span><span class="p">:</span> <span class="p">{</span>
                <span class="sh">"</span><span class="s">type</span><span class="sh">"</span><span class="p">:</span> <span class="sh">"</span><span class="s">string</span><span class="sh">"</span><span class="p">,</span>
                <span class="sh">"</span><span class="s">description</span><span class="sh">"</span><span class="p">:</span> <span class="sh">"</span><span class="s">Stock ticker symbol for a company.</span><span class="sh">"</span>
            <span class="p">},</span>
            <span class="sh">"</span><span class="s">published_utc.gte</span><span class="sh">"</span><span class="p">:</span> <span class="p">{</span>
                <span class="sh">"</span><span class="s">type</span><span class="sh">"</span><span class="p">:</span> <span class="sh">"</span><span class="s">string</span><span class="sh">"</span><span class="p">,</span>
                <span class="sh">"</span><span class="s">format</span><span class="sh">"</span><span class="p">:</span> <span class="sh">"</span><span class="s">date-time</span><span class="sh">"</span><span class="p">,</span>
                <span class="sh">"</span><span class="s">description</span><span class="sh">"</span><span class="p">:</span> <span class="sh">"""</span><span class="s">A date in format YYYY-MM-DD must be older than the parameter </span><span class="sh">'</span><span class="s">published_utc.lte</span><span class="sh">'</span><span class="s">. 
                                  The default value is one-month ago from today</span><span class="sh">'</span><span class="s">s date.</span><span class="sh">"""</span>
            <span class="p">},</span>
            <span class="sh">"</span><span class="s">published_utc.lte</span><span class="sh">"</span><span class="p">:</span> <span class="p">{</span>
                <span class="sh">"</span><span class="s">type</span><span class="sh">"</span><span class="p">:</span> <span class="sh">"</span><span class="s">string</span><span class="sh">"</span><span class="p">,</span>
                <span class="sh">"</span><span class="s">format</span><span class="sh">"</span><span class="p">:</span> <span class="sh">"</span><span class="s">date-time</span><span class="sh">"</span><span class="p">,</span>
                <span class="sh">"</span><span class="s">description</span><span class="sh">"</span><span class="p">:</span> <span class="sh">"""</span><span class="s">A date in format YYYY-MM-DD must be more recent than the parameter </span><span class="sh">'</span><span class="s">published_utc.gte</span><span class="sh">'</span><span class="s">.
                                  The default is one weekday prior to get_last_market_close (excluding weekends).
                                  Replace more recent dates with the default.</span><span class="sh">"""</span>
            <span class="p">},</span>
            <span class="sh">"</span><span class="s">order</span><span class="sh">"</span><span class="p">:</span> <span class="p">{</span>
                <span class="sh">"</span><span class="s">type</span><span class="sh">"</span><span class="p">:</span> <span class="sh">"</span><span class="s">string</span><span class="sh">"</span><span class="p">,</span>
                <span class="sh">"</span><span class="s">description</span><span class="sh">"</span><span class="p">:</span> <span class="sh">"""</span><span class="s">Must be desc for descending order, or asc for ascending order.
                                  When order is not specified the default is descending order.
                                  Ordering will be based on the parameter </span><span class="sh">'</span><span class="s">sort</span><span class="sh">'</span><span class="s">.</span><span class="sh">"""</span>
            <span class="p">},</span>
            <span class="sh">"</span><span class="s">limit</span><span class="sh">"</span><span class="p">:</span> <span class="p">{</span>
                <span class="sh">"</span><span class="s">type</span><span class="sh">"</span><span class="p">:</span> <span class="sh">"</span><span class="s">integer</span><span class="sh">"</span><span class="p">,</span>
                <span class="sh">"</span><span class="s">description</span><span class="sh">"</span><span class="p">:</span> <span class="sh">"""</span><span class="s">This must be included and equal to 1000 unless told otherwise.</span><span class="sh">"""</span>
            <span class="p">},</span>
            <span class="sh">"</span><span class="s">sort</span><span class="sh">"</span><span class="p">:</span> <span class="p">{</span>
                <span class="sh">"</span><span class="s">type</span><span class="sh">"</span><span class="p">:</span> <span class="sh">"</span><span class="s">string</span><span class="sh">"</span><span class="p">,</span>
                <span class="sh">"</span><span class="s">description</span><span class="sh">"</span><span class="p">:</span> <span class="sh">"""</span><span class="s">The sort field used for ordering. This value must
                                  always be published_utc.</span><span class="sh">"""</span>
            <span class="p">},</span>
            <span class="sh">"</span><span class="s">query</span><span class="sh">"</span><span class="p">:</span> <span class="p">{</span>
                <span class="sh">"</span><span class="s">type</span><span class="sh">"</span><span class="p">:</span> <span class="sh">"</span><span class="s">string</span><span class="sh">"</span><span class="p">,</span>
                <span class="sh">"</span><span class="s">description</span><span class="sh">"</span><span class="p">:</span> <span class="sh">"</span><span class="s">The question you</span><span class="sh">'</span><span class="s">re attempting to answer.</span><span class="sh">"</span>
            <span class="p">}</span>
        <span class="p">},</span>
        <span class="sh">"</span><span class="s">required</span><span class="sh">"</span><span class="p">:</span> <span class="p">[</span><span class="sh">"</span><span class="s">limit</span><span class="sh">"</span><span class="p">,</span> <span class="sh">"</span><span class="s">ticker</span><span class="sh">"</span><span class="p">,</span> <span class="sh">"</span><span class="s">published_utc.gte</span><span class="sh">"</span><span class="p">,</span> <span class="sh">"</span><span class="s">published_utc.lte</span><span class="sh">"</span><span class="p">,</span> <span class="sh">"</span><span class="s">order</span><span class="sh">"</span><span class="p">,</span> <span class="sh">"</span><span class="s">sort</span><span class="sh">"</span><span class="p">,</span> <span class="sh">"</span><span class="s">query</span><span class="sh">"</span><span class="p">]</span>
    <span class="p">}</span>
<span class="p">)</span>

<span class="n">decl_get_rag_tool_response</span> <span class="o">=</span> <span class="n">types</span><span class="p">.</span><span class="nc">FunctionDeclaration</span><span class="p">(</span>
    <span class="n">name</span><span class="o">=</span><span class="sh">"</span><span class="s">get_rag_tool_response</span><span class="sh">"</span><span class="p">,</span>
    <span class="n">description</span><span class="o">=</span><span class="sh">"""</span><span class="s">A database containing useful financial information. Always check here for answers first.</span><span class="sh">"""</span><span class="p">,</span>
    <span class="n">parameters</span><span class="o">=</span><span class="p">{</span>
        <span class="sh">"</span><span class="s">type</span><span class="sh">"</span><span class="p">:</span> <span class="sh">"</span><span class="s">object</span><span class="sh">"</span><span class="p">,</span>
        <span class="sh">"</span><span class="s">properties</span><span class="sh">"</span><span class="p">:</span> <span class="p">{</span>
            <span class="sh">"</span><span class="s">question</span><span class="sh">"</span><span class="p">:</span> <span class="p">{</span>
                <span class="sh">"</span><span class="s">type</span><span class="sh">"</span><span class="p">:</span> <span class="sh">"</span><span class="s">string</span><span class="sh">"</span><span class="p">,</span>
                <span class="sh">"</span><span class="s">description</span><span class="sh">"</span><span class="p">:</span> <span class="sh">"</span><span class="s">A question needing an answer. Asked as a simple string.</span><span class="sh">"</span>
            <span class="p">}</span>
        <span class="p">}</span>
    <span class="p">}</span>
<span class="p">)</span>

<span class="n">decl_get_wiki_tool_response</span> <span class="o">=</span> <span class="n">types</span><span class="p">.</span><span class="nc">FunctionDeclaration</span><span class="p">(</span>
    <span class="n">name</span><span class="o">=</span><span class="sh">"</span><span class="s">get_wiki_tool_response</span><span class="sh">"</span><span class="p">,</span>
    <span class="n">description</span><span class="o">=</span><span class="sh">"""</span><span class="s">Answers questions that still have unknown answers. Retrieve a wiki page related to a company, 
                   product, or service. Each web page includes detailed company information, financial indicators, 
                   tickers, symbols, history, and products and services.</span><span class="sh">"""</span><span class="p">,</span>
    <span class="n">parameters</span><span class="o">=</span><span class="p">{</span>
        <span class="sh">"</span><span class="s">type</span><span class="sh">"</span><span class="p">:</span> <span class="sh">"</span><span class="s">object</span><span class="sh">"</span><span class="p">,</span>
        <span class="sh">"</span><span class="s">properties</span><span class="sh">"</span><span class="p">:</span> <span class="p">{</span>
            <span class="sh">"</span><span class="s">id</span><span class="sh">"</span><span class="p">:</span> <span class="p">{</span>
                <span class="sh">"</span><span class="s">type</span><span class="sh">"</span><span class="p">:</span> <span class="sh">"</span><span class="s">string</span><span class="sh">"</span><span class="p">,</span>
                <span class="sh">"</span><span class="s">description</span><span class="sh">"</span><span class="p">:</span> <span class="sh">"</span><span class="s">The question</span><span class="sh">'</span><span class="s">s company or product. Just the name and no other details.</span><span class="sh">"</span>
            <span class="p">},</span>
            <span class="sh">"</span><span class="s">q</span><span class="sh">"</span><span class="p">:</span> <span class="p">{</span>
                <span class="sh">"</span><span class="s">type</span><span class="sh">"</span><span class="p">:</span> <span class="sh">"</span><span class="s">string</span><span class="sh">"</span><span class="p">,</span>
                <span class="sh">"</span><span class="s">description</span><span class="sh">"</span><span class="p">:</span> <span class="sh">"</span><span class="s">The complete, unaltered, query string.</span><span class="sh">"</span>
            <span class="p">}</span>
        <span class="p">},</span>
        <span class="sh">"</span><span class="s">required</span><span class="sh">"</span><span class="p">:</span> <span class="p">[</span><span class="sh">"</span><span class="s">id</span><span class="sh">"</span><span class="p">,</span> <span class="sh">"</span><span class="s">q</span><span class="sh">"</span><span class="p">]</span>
    <span class="p">}</span>
<span class="p">)</span>

<span class="n">decl_get_search_tool_response</span> <span class="o">=</span> <span class="n">types</span><span class="p">.</span><span class="nc">FunctionDeclaration</span><span class="p">(</span>
    <span class="n">name</span><span class="o">=</span><span class="sh">"</span><span class="s">get_search_tool_response</span><span class="sh">"</span><span class="p">,</span>
    <span class="n">description</span><span class="o">=</span><span class="sh">"</span><span class="s">Answers questions that still have unknown answers. Use it after checking all your other tools.</span><span class="sh">"</span><span class="p">,</span>
    <span class="n">parameters</span><span class="o">=</span><span class="p">{</span>
        <span class="sh">"</span><span class="s">type</span><span class="sh">"</span><span class="p">:</span> <span class="sh">"</span><span class="s">object</span><span class="sh">"</span><span class="p">,</span>
        <span class="sh">"</span><span class="s">properties</span><span class="sh">"</span><span class="p">:</span> <span class="p">{</span>
            <span class="sh">"</span><span class="s">q</span><span class="sh">"</span><span class="p">:</span> <span class="p">{</span>
                <span class="sh">"</span><span class="s">type</span><span class="sh">"</span><span class="p">:</span> <span class="sh">"</span><span class="s">string</span><span class="sh">"</span><span class="p">,</span>
                <span class="sh">"</span><span class="s">description</span><span class="sh">"</span><span class="p">:</span> <span class="sh">"</span><span class="s">The question needing an answer. Asked as a simple string.</span><span class="sh">"</span>
            <span class="p">},</span>
            <span class="sh">"</span><span class="s">id</span><span class="sh">"</span><span class="p">:</span> <span class="p">{</span>
                <span class="sh">"</span><span class="s">type</span><span class="sh">"</span><span class="p">:</span> <span class="sh">"</span><span class="s">string</span><span class="sh">"</span><span class="p">,</span>
                <span class="sh">"</span><span class="s">description</span><span class="sh">"</span><span class="p">:</span> <span class="sh">"</span><span class="s">The question</span><span class="sh">'</span><span class="s">s company or product. In one word. Just the name and no other details.</span><span class="sh">"</span>
            <span class="p">}</span>
        <span class="p">},</span>
        <span class="sh">"</span><span class="s">required</span><span class="sh">"</span><span class="p">:</span> <span class="p">[</span><span class="sh">"</span><span class="s">q</span><span class="sh">"</span><span class="p">,</span> <span class="sh">"</span><span class="s">id</span><span class="sh">"</span><span class="p">]</span>
    <span class="p">}</span>
<span class="p">)</span>
</code></pre></div></div>

<div class="language-python highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="c1"># Import the finance api secret keys.
</span>
<span class="n">POLYGON_API_KEY</span> <span class="o">=</span> <span class="nc">UserSecretsClient</span><span class="p">().</span><span class="nf">get_secret</span><span class="p">(</span><span class="sh">"</span><span class="s">POLYGON_API_KEY</span><span class="sh">"</span><span class="p">)</span>
<span class="n">FINNHUB_API_KEY</span> <span class="o">=</span> <span class="nc">UserSecretsClient</span><span class="p">().</span><span class="nf">get_secret</span><span class="p">(</span><span class="sh">"</span><span class="s">FINNHUB_API_KEY</span><span class="sh">"</span><span class="p">)</span>
</code></pre></div></div>

<div class="language-python highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="c1"># Instantiate tools and load the exchange data from source csv.
# - Identifies exchanges by a 1-2 letter code which can be used to filter response data.
# - Also maps the exchange code to exchange details.
</span><span class="k">try</span><span class="p">:</span>
    <span class="n">df</span> <span class="o">=</span> <span class="n">pandas</span><span class="p">.</span><span class="nf">read_csv</span><span class="p">(</span><span class="sh">"</span><span class="s">/kaggle/input/exchanges/exchanges_src.csv</span><span class="sh">"</span><span class="p">)</span>
<span class="k">except</span> <span class="nb">FileNotFoundError</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
    <span class="n">df</span> <span class="o">=</span> <span class="n">pandas</span><span class="p">.</span><span class="nf">read_csv</span><span class="p">(</span><span class="sh">"</span><span class="s">exchanges_src.csv</span><span class="sh">"</span><span class="p">)</span> <span class="c1"># local run
</span><span class="n">df</span> <span class="o">=</span> <span class="n">df</span><span class="p">.</span><span class="nf">drop</span><span class="p">([</span><span class="sh">"</span><span class="s">close_date</span><span class="sh">"</span><span class="p">],</span> <span class="n">axis</span><span class="o">=</span><span class="mi">1</span><span class="p">).</span><span class="nf">fillna</span><span class="p">(</span><span class="sh">""</span><span class="p">)</span>
<span class="n">df</span><span class="p">.</span><span class="nf">to_csv</span><span class="p">(</span><span class="sh">"</span><span class="s">exchanges.csv</span><span class="sh">"</span><span class="p">,</span> <span class="n">index</span><span class="o">=</span><span class="bp">False</span><span class="p">)</span>
<span class="n">exchanges</span> <span class="o">=</span> <span class="nc">CSVLoader</span><span class="p">(</span><span class="n">file_path</span><span class="o">=</span><span class="sh">"</span><span class="s">exchanges.csv</span><span class="sh">"</span><span class="p">,</span> <span class="n">encoding</span><span class="o">=</span><span class="sh">"</span><span class="s">utf-8</span><span class="sh">"</span><span class="p">,</span> <span class="n">csv_args</span><span class="o">=</span><span class="p">{</span><span class="sh">"</span><span class="s">delimiter</span><span class="sh">"</span><span class="p">:</span> <span class="sh">"</span><span class="s">,</span><span class="sh">"</span><span class="p">}).</span><span class="nf">load</span><span class="p">()</span>

<span class="c1"># Prepare a RAG tool for use and add the exchange data.
</span><span class="n">tool_rag</span> <span class="o">=</span> <span class="nc">RetrievalAugmentedGenerator</span><span class="p">(</span><span class="n">api</span><span class="p">.</span><span class="n">args</span><span class="p">.</span><span class="n">CLIENT</span><span class="p">,</span> <span class="sh">"</span><span class="s">finance</span><span class="sh">"</span><span class="p">)</span>
<span class="n">tool_rag</span><span class="p">.</span><span class="nf">add_documents_list</span><span class="p">(</span><span class="n">exchanges</span><span class="p">)</span>

<span class="c1"># Prepare a the grounding tools for use.
</span><span class="n">tool_wiki</span> <span class="o">=</span> <span class="nc">WikiGroundingGenerator</span><span class="p">(</span><span class="n">api</span><span class="p">.</span><span class="n">args</span><span class="p">.</span><span class="n">CLIENT</span><span class="p">,</span> <span class="n">tool_rag</span><span class="p">)</span>
<span class="n">tool_ground</span> <span class="o">=</span> <span class="nc">SearchGroundingGenerator</span><span class="p">(</span><span class="n">api</span><span class="p">.</span><span class="n">args</span><span class="p">.</span><span class="n">CLIENT</span><span class="p">,</span> <span class="n">tool_rag</span><span class="p">)</span>
<span class="n">tool_rest</span> <span class="o">=</span> <span class="nc">RestGroundingGenerator</span><span class="p">(</span><span class="n">tool_rag</span><span class="p">,</span> <span class="n">with_limits</span><span class="o">=</span><span class="bp">True</span><span class="p">)</span>
</code></pre></div></div>

<h3 id="function-calling-expert">Function Calling Expert</h3>

<div class="language-python highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="c1"># Implement the callable functions and function handler.
</span>
<span class="k">def</span> <span class="nf">ask_rag_tool</span><span class="p">(</span><span class="n">content</span><span class="p">):</span>
    <span class="k">return</span> <span class="n">tool_rag</span><span class="p">.</span><span class="nf">generate_answer</span><span class="p">(</span><span class="n">content</span><span class="p">[</span><span class="sh">"</span><span class="s">question</span><span class="sh">"</span><span class="p">]).</span><span class="n">text</span>

<span class="k">def</span> <span class="nf">ask_wiki_tool</span><span class="p">(</span><span class="n">content</span><span class="p">):</span>
    <span class="k">return</span> <span class="n">tool_wiki</span><span class="p">.</span><span class="nf">generate_answer</span><span class="p">(</span><span class="n">content</span><span class="p">[</span><span class="sh">"</span><span class="s">q</span><span class="sh">"</span><span class="p">],</span> <span class="n">content</span><span class="p">[</span><span class="sh">"</span><span class="s">id</span><span class="sh">"</span><span class="p">])</span>

<span class="k">def</span> <span class="nf">ask_search_tool</span><span class="p">(</span><span class="n">content</span><span class="p">):</span>
    <span class="k">return</span> <span class="n">tool_ground</span><span class="p">.</span><span class="nf">generate_answer</span><span class="p">(</span><span class="n">content</span><span class="p">[</span><span class="sh">"</span><span class="s">q</span><span class="sh">"</span><span class="p">],</span> <span class="n">content</span><span class="p">[</span><span class="sh">"</span><span class="s">id</span><span class="sh">"</span><span class="p">])</span>

<span class="k">def</span> <span class="nf">get_exchange_codes_1</span><span class="p">(</span><span class="n">content</span><span class="p">):</span>
    <span class="k">return</span> <span class="n">tool_rag</span><span class="p">.</span><span class="nf">get_exchange_codes</span><span class="p">()</span>

<span class="k">def</span> <span class="nf">get_exchange_code_1</span><span class="p">(</span><span class="n">content</span><span class="p">):</span>
    <span class="k">return</span> <span class="n">tool_rag</span><span class="p">.</span><span class="nf">get_exchange_codes</span><span class="p">(</span><span class="n">with_query</span><span class="o">=</span><span class="n">content</span><span class="p">)</span>
    
<span class="k">def</span> <span class="nf">last_market_close</span><span class="p">(</span><span class="n">content</span><span class="p">):</span>
    <span class="k">return</span> <span class="n">tool_rag</span><span class="p">.</span><span class="nf">last_market_close</span><span class="p">(</span><span class="n">content</span><span class="p">[</span><span class="sh">"</span><span class="s">exchange</span><span class="sh">"</span><span class="p">])</span>
    
<span class="k">def</span> <span class="nf">get_symbol_1</span><span class="p">(</span><span class="n">content</span><span class="p">,</span> <span class="n">by_name</span><span class="p">:</span> <span class="nb">bool</span> <span class="o">=</span> <span class="bp">True</span><span class="p">):</span>
    <span class="n">stored</span> <span class="o">=</span> <span class="n">tool_rag</span><span class="p">.</span><span class="nf">get_api_documents</span><span class="p">(</span><span class="n">content</span><span class="p">[</span><span class="sh">"</span><span class="s">query</span><span class="sh">"</span><span class="p">],</span> <span class="n">content</span><span class="p">[</span><span class="sh">"</span><span class="s">q</span><span class="sh">"</span><span class="p">],</span> <span class="sh">"</span><span class="s">get_symbol_1</span><span class="sh">"</span><span class="p">)</span>
    <span class="k">if</span> <span class="nf">len</span><span class="p">(</span><span class="n">stored</span><span class="p">)</span> <span class="o">==</span> <span class="mi">0</span><span class="p">:</span>
        <span class="k">return</span> <span class="n">tool_rest</span><span class="p">.</span><span class="nf">get_symbol</span><span class="p">(</span><span class="n">content</span><span class="p">,</span> <span class="n">by_name</span><span class="p">)</span>
    <span class="k">return</span> <span class="n">json</span><span class="p">.</span><span class="nf">loads</span><span class="p">(</span><span class="n">stored</span><span class="p">[</span><span class="mi">0</span><span class="p">].</span><span class="n">docs</span><span class="p">)</span>

<span class="k">def</span> <span class="nf">get_symbols_1</span><span class="p">(</span><span class="n">content</span><span class="p">):</span>
    <span class="k">return</span> <span class="bp">None</span> <span class="c1"># todo
</span>
<span class="k">def</span> <span class="nf">get_name_1</span><span class="p">(</span><span class="n">content</span><span class="p">):</span>
    <span class="k">return</span> <span class="nf">get_symbol_1</span><span class="p">(</span><span class="n">content</span><span class="p">,</span> <span class="n">by_name</span> <span class="o">=</span> <span class="bp">False</span><span class="p">)</span>

<span class="k">def</span> <span class="nf">get_quote_1</span><span class="p">(</span><span class="n">content</span><span class="p">):</span>
    <span class="n">stored</span> <span class="o">=</span> <span class="n">tool_rag</span><span class="p">.</span><span class="nf">get_api_documents</span><span class="p">(</span><span class="n">content</span><span class="p">[</span><span class="sh">"</span><span class="s">query</span><span class="sh">"</span><span class="p">],</span> <span class="n">content</span><span class="p">[</span><span class="sh">"</span><span class="s">symbol</span><span class="sh">"</span><span class="p">],</span> <span class="sh">"</span><span class="s">get_quote_1</span><span class="sh">"</span><span class="p">)</span>
    <span class="k">if</span> <span class="n">tool_rag</span><span class="p">.</span><span class="nf">generated_events</span><span class="p">(</span><span class="n">content</span><span class="p">[</span><span class="sh">"</span><span class="s">exchange</span><span class="sh">"</span><span class="p">]).</span><span class="nf">is_open</span><span class="p">():</span>
        <span class="k">return</span> <span class="nf">get_current_price_1</span><span class="p">(</span><span class="n">content</span><span class="p">)</span>
    <span class="k">elif</span> <span class="nf">len</span><span class="p">(</span><span class="n">stored</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mi">0</span><span class="p">:</span>
        <span class="n">last_close</span> <span class="o">=</span> <span class="nf">parse</span><span class="p">(</span><span class="n">tool_rag</span><span class="p">.</span><span class="nf">last_market_close</span><span class="p">(</span><span class="n">content</span><span class="p">[</span><span class="sh">"</span><span class="s">exchange</span><span class="sh">"</span><span class="p">])).</span><span class="nf">timestamp</span><span class="p">()</span>
        <span class="k">for</span> <span class="n">quote</span> <span class="ow">in</span> <span class="n">stored</span><span class="p">:</span>
            <span class="k">if</span> <span class="n">quote</span><span class="p">.</span><span class="n">meta</span><span class="p">[</span><span class="sh">"</span><span class="s">timestamp</span><span class="sh">"</span><span class="p">]</span> <span class="o">&gt;=</span> <span class="n">last_close</span><span class="p">:</span>
                <span class="k">return</span> <span class="p">[</span><span class="n">quote</span><span class="p">.</span><span class="n">docs</span> <span class="k">for</span> <span class="n">quote</span> <span class="ow">in</span> <span class="n">stored</span><span class="p">]</span>
    <span class="k">return</span> <span class="nf">get_current_price_1</span><span class="p">(</span><span class="n">content</span><span class="p">)</span>

<span class="k">def</span> <span class="nf">get_current_price_1</span><span class="p">(</span><span class="n">content</span><span class="p">):</span>
    <span class="k">return</span> <span class="n">tool_rest</span><span class="p">.</span><span class="nf">get_current_price</span><span class="p">(</span><span class="n">content</span><span class="p">)</span>

<span class="k">def</span> <span class="nf">get_market_status_1</span><span class="p">(</span><span class="n">content</span><span class="p">):</span>
    <span class="n">stored</span><span class="p">,</span> <span class="n">has_update</span> <span class="o">=</span> <span class="n">tool_rag</span><span class="p">.</span><span class="nf">get_market_status</span><span class="p">(</span><span class="n">content</span><span class="p">[</span><span class="sh">'</span><span class="s">exchange</span><span class="sh">'</span><span class="p">])</span>
    <span class="k">if</span> <span class="n">has_update</span><span class="p">:</span>
        <span class="n">with_id</span> <span class="o">=</span> <span class="n">stored</span><span class="p">[</span><span class="mi">0</span><span class="p">].</span><span class="n">store_id</span> <span class="k">if</span> <span class="nf">len</span><span class="p">(</span><span class="n">stored</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mi">0</span> <span class="k">else</span> <span class="bp">None</span>
        <span class="k">return</span> <span class="n">tool_rest</span><span class="p">.</span><span class="nf">get_market_status</span><span class="p">(</span><span class="n">content</span><span class="p">,</span> <span class="n">with_id</span><span class="p">)</span>
    <span class="k">return</span> <span class="n">stored</span><span class="p">[</span><span class="mi">0</span><span class="p">].</span><span class="n">docs</span>

<span class="k">def</span> <span class="nf">get_session_1</span><span class="p">(</span><span class="n">content</span><span class="p">):</span>
    <span class="k">return</span> <span class="n">json</span><span class="p">.</span><span class="nf">loads</span><span class="p">(</span><span class="nf">get_market_status_1</span><span class="p">(</span><span class="n">content</span><span class="p">))[</span><span class="sh">"</span><span class="s">session</span><span class="sh">"</span><span class="p">]</span>

<span class="k">def</span> <span class="nf">get_peers_1</span><span class="p">(</span><span class="n">content</span><span class="p">):</span>
    <span class="n">stored</span> <span class="o">=</span> <span class="n">tool_rag</span><span class="p">.</span><span class="nf">get_peers_document</span><span class="p">(</span><span class="n">content</span><span class="p">[</span><span class="sh">"</span><span class="s">query</span><span class="sh">"</span><span class="p">],</span> <span class="n">content</span><span class="p">[</span><span class="sh">"</span><span class="s">symbol</span><span class="sh">"</span><span class="p">],</span> <span class="n">content</span><span class="p">[</span><span class="sh">'</span><span class="s">grouping</span><span class="sh">'</span><span class="p">])</span>
    <span class="k">if</span> <span class="nf">len</span><span class="p">(</span><span class="n">stored</span><span class="p">)</span> <span class="o">==</span> <span class="mi">0</span><span class="p">:</span>
        <span class="n">peers</span> <span class="o">=</span> <span class="n">tool_rest</span><span class="p">.</span><span class="nf">get_peers</span><span class="p">(</span><span class="n">content</span><span class="p">)</span>
        <span class="k">if</span> <span class="n">peers</span><span class="p">.</span><span class="n">count</span> <span class="o">&gt;</span> <span class="mi">0</span><span class="p">:</span>
            <span class="n">names</span> <span class="o">=</span> <span class="p">[]</span>
            <span class="k">for</span> <span class="n">peer</span> <span class="ow">in</span> <span class="n">peers</span><span class="p">.</span><span class="nf">get</span><span class="p">():</span>
                <span class="k">if</span> <span class="n">peer</span> <span class="o">==</span> <span class="n">content</span><span class="p">[</span><span class="sh">"</span><span class="s">symbol</span><span class="sh">"</span><span class="p">]:</span>
                    <span class="k">continue</span> <span class="c1"># skip including the query symbol in peers
</span>                <span class="n">name</span> <span class="o">=</span> <span class="nf">get_name_1</span><span class="p">(</span><span class="nf">dict</span><span class="p">(</span><span class="n">q</span><span class="o">=</span><span class="n">peer</span><span class="p">,</span> <span class="n">exchange</span><span class="o">=</span><span class="n">content</span><span class="p">[</span><span class="sh">"</span><span class="s">exchange</span><span class="sh">"</span><span class="p">],</span> <span class="n">query</span><span class="o">=</span><span class="n">content</span><span class="p">[</span><span class="sh">"</span><span class="s">query</span><span class="sh">"</span><span class="p">]))</span>
                <span class="k">if</span> <span class="n">name</span> <span class="o">!=</span> <span class="n">Api</span><span class="p">.</span><span class="n">Const</span><span class="p">.</span><span class="nc">Stop</span><span class="p">():</span>
                    <span class="n">data</span> <span class="o">=</span> <span class="p">{</span><span class="sh">"</span><span class="s">symbol</span><span class="sh">"</span><span class="p">:</span> <span class="n">peer</span><span class="p">,</span> <span class="sh">"</span><span class="s">name</span><span class="sh">"</span><span class="p">:</span> <span class="n">name</span><span class="p">}</span>
                    <span class="n">names</span><span class="p">.</span><span class="nf">append</span><span class="p">(</span><span class="n">data</span><span class="p">)</span>
            <span class="n">tool_rag</span><span class="p">.</span><span class="nf">add_peers_document</span><span class="p">(</span><span class="n">content</span><span class="p">[</span><span class="sh">"</span><span class="s">query</span><span class="sh">"</span><span class="p">],</span> <span class="n">names</span><span class="p">,</span> <span class="n">content</span><span class="p">[</span><span class="sh">"</span><span class="s">symbol</span><span class="sh">"</span><span class="p">],</span> <span class="sh">"</span><span class="s">get_peers_1</span><span class="sh">"</span><span class="p">,</span> <span class="n">content</span><span class="p">[</span><span class="sh">'</span><span class="s">grouping</span><span class="sh">'</span><span class="p">])</span>
            <span class="k">return</span> <span class="n">names</span>
        <span class="k">return</span> <span class="n">Api</span><span class="p">.</span><span class="n">Const</span><span class="p">.</span><span class="nc">Stop</span><span class="p">()</span>
    <span class="k">return</span> <span class="n">json</span><span class="p">.</span><span class="nf">loads</span><span class="p">(</span><span class="n">stored</span><span class="p">[</span><span class="mi">0</span><span class="p">].</span><span class="n">docs</span><span class="p">)[</span><span class="sh">"</span><span class="s">peers</span><span class="sh">"</span><span class="p">]</span>

<span class="k">def</span> <span class="nf">local_datetime</span><span class="p">(</span><span class="n">content</span><span class="p">):</span>
    <span class="n">local_t</span> <span class="o">=</span> <span class="p">[]</span>
    <span class="k">for</span> <span class="n">timestamp</span> <span class="ow">in</span> <span class="n">content</span><span class="p">[</span><span class="sh">"</span><span class="s">t</span><span class="sh">"</span><span class="p">]:</span>
        <span class="n">local_t</span><span class="p">.</span><span class="nf">append</span><span class="p">(</span><span class="nf">local_date_from_epoch</span><span class="p">(</span><span class="n">timestamp</span><span class="p">))</span>
    <span class="k">return</span> <span class="n">local_t</span>

<span class="k">def</span> <span class="nf">local_date_from_epoch</span><span class="p">(</span><span class="n">timestamp</span><span class="p">):</span>
    <span class="k">if</span> <span class="nf">len</span><span class="p">(</span><span class="nf">str</span><span class="p">(</span><span class="n">timestamp</span><span class="p">))</span> <span class="o">==</span> <span class="mi">13</span><span class="p">:</span>
        <span class="k">return</span> <span class="n">datetime</span><span class="p">.</span><span class="nf">fromtimestamp</span><span class="p">(</span><span class="n">timestamp</span><span class="o">/</span><span class="mi">1000</span><span class="p">,</span> <span class="n">tz</span><span class="o">=</span><span class="n">GeneratedEvent</span><span class="p">.</span><span class="nf">tz</span><span class="p">()).</span><span class="nf">strftime</span><span class="p">(</span><span class="sh">'</span><span class="s">%c</span><span class="sh">'</span><span class="p">)</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="k">return</span> <span class="n">datetime</span><span class="p">.</span><span class="nf">fromtimestamp</span><span class="p">(</span><span class="n">timestamp</span><span class="p">,</span> <span class="n">tz</span><span class="o">=</span><span class="n">GeneratedEvent</span><span class="p">.</span><span class="nf">tz</span><span class="p">()).</span><span class="nf">strftime</span><span class="p">(</span><span class="sh">'</span><span class="s">%c</span><span class="sh">'</span><span class="p">)</span>

<span class="k">def</span> <span class="nf">get_financials_1</span><span class="p">(</span><span class="n">content</span><span class="p">):</span>
    <span class="n">stored</span> <span class="o">=</span> <span class="n">tool_rag</span><span class="p">.</span><span class="nf">get_basic_financials</span><span class="p">(</span><span class="n">content</span><span class="p">[</span><span class="sh">"</span><span class="s">query</span><span class="sh">"</span><span class="p">],</span> <span class="n">content</span><span class="p">[</span><span class="sh">"</span><span class="s">symbol</span><span class="sh">"</span><span class="p">],</span> <span class="sh">"</span><span class="s">get_financials_1</span><span class="sh">"</span><span class="p">)</span>
    <span class="k">if</span> <span class="nf">len</span><span class="p">(</span><span class="n">stored</span><span class="p">)</span> <span class="o">==</span> <span class="mi">0</span><span class="p">:</span>
        <span class="k">return</span> <span class="n">tool_rest</span><span class="p">.</span><span class="nf">get_basic_financials</span><span class="p">(</span><span class="n">content</span><span class="p">)</span>
    <span class="k">return</span> <span class="p">[</span><span class="n">chunk</span><span class="p">.</span><span class="n">docs</span> <span class="k">for</span> <span class="n">chunk</span> <span class="ow">in</span> <span class="n">stored</span><span class="p">]</span>

<span class="k">def</span> <span class="nf">get_news_1</span><span class="p">(</span><span class="n">content</span><span class="p">):</span>
    <span class="n">stored</span> <span class="o">=</span> <span class="n">tool_rag</span><span class="p">.</span><span class="nf">get_api_documents</span><span class="p">(</span><span class="n">content</span><span class="p">[</span><span class="sh">"</span><span class="s">query</span><span class="sh">"</span><span class="p">],</span> <span class="n">content</span><span class="p">[</span><span class="sh">"</span><span class="s">symbol</span><span class="sh">"</span><span class="p">],</span> <span class="sh">"</span><span class="s">get_news_1</span><span class="sh">"</span><span class="p">)</span>
    <span class="k">if</span> <span class="nf">len</span><span class="p">(</span><span class="n">stored</span><span class="p">)</span> <span class="o">==</span> <span class="mi">0</span><span class="p">:</span>
        <span class="k">return</span> <span class="n">tool_rest</span><span class="p">.</span><span class="nf">get_news_simple</span><span class="p">(</span><span class="n">content</span><span class="p">)</span>
    <span class="k">return</span> <span class="p">[</span><span class="n">NewsTypeFinn</span><span class="p">.</span><span class="nf">model_validate_json</span><span class="p">(</span><span class="n">news</span><span class="p">.</span><span class="n">docs</span><span class="p">).</span><span class="nf">summary</span><span class="p">().</span><span class="nf">model_dump_json</span><span class="p">()</span> <span class="k">for</span> <span class="n">news</span> <span class="ow">in</span> <span class="n">stored</span><span class="p">]</span>

<span class="k">def</span> <span class="nf">get_daily_candle_2</span><span class="p">(</span><span class="n">content</span><span class="p">):</span>
    <span class="n">stored</span> <span class="o">=</span> <span class="n">tool_rag</span><span class="p">.</span><span class="nf">get_api_documents</span><span class="p">(</span>
        <span class="n">query</span><span class="o">=</span><span class="n">content</span><span class="p">[</span><span class="sh">"</span><span class="s">query</span><span class="sh">"</span><span class="p">],</span> <span class="n">topic</span><span class="o">=</span><span class="n">content</span><span class="p">[</span><span class="sh">"</span><span class="s">stocksTicker</span><span class="sh">"</span><span class="p">],</span> <span class="n">source</span><span class="o">=</span><span class="sh">"</span><span class="s">daily_candle_2</span><span class="sh">"</span><span class="p">,</span> 
        <span class="n">meta_opt</span><span class="o">=</span><span class="p">[{</span><span class="sh">"</span><span class="s">from_date</span><span class="sh">"</span><span class="p">:</span> <span class="n">content</span><span class="p">[</span><span class="sh">"</span><span class="s">date</span><span class="sh">"</span><span class="p">],</span> <span class="sh">"</span><span class="s">adjusted</span><span class="sh">"</span><span class="p">:</span> <span class="n">content</span><span class="p">[</span><span class="sh">"</span><span class="s">adjusted</span><span class="sh">"</span><span class="p">]}])</span>
    <span class="k">if</span> <span class="nf">len</span><span class="p">(</span><span class="n">stored</span><span class="p">)</span> <span class="o">==</span> <span class="mi">0</span><span class="p">:</span>
        <span class="n">candle</span> <span class="o">=</span> <span class="n">tool_rest</span><span class="p">.</span><span class="nf">get_daily_candle</span><span class="p">(</span><span class="n">content</span><span class="p">)</span>
        <span class="c1"># Attempt to recover from choosing a holiday.
</span>        <span class="n">candle_date</span> <span class="o">=</span> <span class="nf">parse</span><span class="p">(</span><span class="n">content</span><span class="p">[</span><span class="sh">"</span><span class="s">date</span><span class="sh">"</span><span class="p">])</span>
        <span class="k">if</span> <span class="n">candle</span><span class="p">.</span><span class="n">status</span> <span class="ow">is</span> <span class="n">RestStatus</span><span class="p">.</span><span class="n">NONE</span> <span class="ow">and</span> <span class="n">candle_date</span><span class="p">.</span><span class="nf">weekday</span><span class="p">()</span> <span class="o">==</span> <span class="mi">0</span> <span class="ow">or</span> <span class="n">candle_date</span><span class="p">.</span><span class="nf">weekday</span><span class="p">()</span> <span class="o">==</span> <span class="mi">4</span><span class="p">:</span>
            <span class="k">if</span> <span class="n">candle_date</span><span class="p">.</span><span class="nf">weekday</span><span class="p">()</span> <span class="o">==</span> <span class="mi">0</span><span class="p">:</span> <span class="c1"># index 0 is monday, index 4 is friday
</span>                <span class="n">content</span><span class="p">[</span><span class="sh">"</span><span class="s">date</span><span class="sh">"</span><span class="p">]</span> <span class="o">=</span> <span class="n">candle_date</span><span class="p">.</span><span class="nf">replace</span><span class="p">(</span><span class="n">day</span><span class="o">=</span><span class="n">candle_date</span><span class="p">.</span><span class="n">day</span><span class="o">-</span><span class="mi">3</span><span class="p">).</span><span class="nf">strftime</span><span class="p">(</span><span class="sh">"</span><span class="s">%Y-%m-%d</span><span class="sh">"</span><span class="p">)</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="n">content</span><span class="p">[</span><span class="sh">"</span><span class="s">date</span><span class="sh">"</span><span class="p">]</span> <span class="o">=</span> <span class="n">candle_date</span><span class="p">.</span><span class="nf">replace</span><span class="p">(</span><span class="n">day</span><span class="o">=</span><span class="n">candle_date</span><span class="p">.</span><span class="n">day</span><span class="o">-</span><span class="mi">1</span><span class="p">).</span><span class="nf">strftime</span><span class="p">(</span><span class="sh">"</span><span class="s">%Y-%m-%d</span><span class="sh">"</span><span class="p">)</span>
            <span class="k">return</span> <span class="nf">get_daily_candle_2</span><span class="p">(</span><span class="n">content</span><span class="p">)</span>
        <span class="k">return</span> <span class="n">candle</span><span class="p">.</span><span class="nf">model_dump_json</span><span class="p">()</span>
    <span class="k">return</span> <span class="p">[</span><span class="n">json</span><span class="p">.</span><span class="nf">loads</span><span class="p">(</span><span class="n">candle</span><span class="p">.</span><span class="n">docs</span><span class="p">)</span> <span class="k">for</span> <span class="n">candle</span> <span class="ow">in</span> <span class="n">stored</span><span class="p">]</span>

<span class="k">def</span> <span class="nf">get_custom_candle_2</span><span class="p">(</span><span class="n">content</span><span class="p">):</span>
    <span class="n">stored</span> <span class="o">=</span> <span class="n">tool_rag</span><span class="p">.</span><span class="nf">get_api_documents</span><span class="p">(</span>
        <span class="n">query</span><span class="o">=</span><span class="n">content</span><span class="p">[</span><span class="sh">"</span><span class="s">query</span><span class="sh">"</span><span class="p">],</span> <span class="n">topic</span><span class="o">=</span><span class="n">content</span><span class="p">[</span><span class="sh">"</span><span class="s">stocksTicker</span><span class="sh">"</span><span class="p">],</span> <span class="n">source</span><span class="o">=</span><span class="sh">"</span><span class="s">custom_candle_2</span><span class="sh">"</span><span class="p">,</span> 
        <span class="n">meta_opt</span><span class="o">=</span><span class="p">[{</span>
            <span class="sh">"</span><span class="s">timespan</span><span class="sh">"</span><span class="p">:</span> <span class="n">content</span><span class="p">[</span><span class="sh">"</span><span class="s">timespan</span><span class="sh">"</span><span class="p">],</span>
            <span class="sh">"</span><span class="s">adjusted</span><span class="sh">"</span><span class="p">:</span> <span class="n">content</span><span class="p">[</span><span class="sh">"</span><span class="s">adjusted</span><span class="sh">"</span><span class="p">],</span>
            <span class="sh">"</span><span class="s">from</span><span class="sh">"</span><span class="p">:</span> <span class="n">content</span><span class="p">[</span><span class="sh">"</span><span class="s">from</span><span class="sh">"</span><span class="p">],</span>
            <span class="sh">"</span><span class="s">to</span><span class="sh">"</span><span class="p">:</span> <span class="n">content</span><span class="p">[</span><span class="sh">"</span><span class="s">to</span><span class="sh">"</span><span class="p">]}])</span>
    <span class="k">if</span> <span class="nf">len</span><span class="p">(</span><span class="n">stored</span><span class="p">)</span> <span class="o">==</span> <span class="mi">0</span><span class="p">:</span>
        <span class="k">return</span> <span class="n">tool_rest</span><span class="p">.</span><span class="nf">get_custom_candle</span><span class="p">(</span><span class="n">content</span><span class="p">)</span>
    <span class="k">return</span> <span class="p">[</span><span class="n">json</span><span class="p">.</span><span class="nf">loads</span><span class="p">(</span><span class="n">candle</span><span class="p">.</span><span class="n">docs</span><span class="p">)</span> <span class="k">for</span> <span class="n">candle</span> <span class="ow">in</span> <span class="n">stored</span><span class="p">]</span>

<span class="k">def</span> <span class="nf">get_overview_2</span><span class="p">(</span><span class="n">content</span><span class="p">):</span>
    <span class="n">stored</span> <span class="o">=</span> <span class="n">tool_rag</span><span class="p">.</span><span class="nf">get_api_documents</span><span class="p">(</span><span class="n">content</span><span class="p">[</span><span class="sh">"</span><span class="s">query</span><span class="sh">"</span><span class="p">],</span> <span class="n">content</span><span class="p">[</span><span class="sh">"</span><span class="s">ticker</span><span class="sh">"</span><span class="p">],</span> <span class="sh">"</span><span class="s">ticker_overview_2</span><span class="sh">"</span><span class="p">)</span>
    <span class="k">if</span> <span class="nf">len</span><span class="p">(</span><span class="n">stored</span><span class="p">)</span> <span class="o">==</span> <span class="mi">0</span><span class="p">:</span>
        <span class="k">return</span> <span class="n">tool_rest</span><span class="p">.</span><span class="nf">get_overview</span><span class="p">(</span><span class="n">content</span><span class="p">)</span>
    <span class="k">return</span> <span class="n">json</span><span class="p">.</span><span class="nf">loads</span><span class="p">(</span><span class="n">stored</span><span class="p">[</span><span class="mi">0</span><span class="p">].</span><span class="n">docs</span><span class="p">)</span>

<span class="k">def</span> <span class="nf">get_trends_1</span><span class="p">(</span><span class="n">content</span><span class="p">):</span>
    <span class="n">stored</span> <span class="o">=</span> <span class="n">tool_rag</span><span class="p">.</span><span class="nf">get_api_documents</span><span class="p">(</span><span class="n">content</span><span class="p">[</span><span class="sh">"</span><span class="s">query</span><span class="sh">"</span><span class="p">],</span> <span class="n">content</span><span class="p">[</span><span class="sh">"</span><span class="s">symbol</span><span class="sh">"</span><span class="p">],</span> <span class="sh">"</span><span class="s">trends_1</span><span class="sh">"</span><span class="p">)</span>
    <span class="k">if</span> <span class="nf">len</span><span class="p">(</span><span class="n">stored</span><span class="p">)</span> <span class="o">==</span> <span class="mi">0</span><span class="p">:</span>
        <span class="k">return</span> <span class="n">tool_rest</span><span class="p">.</span><span class="nf">get_trends_simple</span><span class="p">(</span><span class="n">content</span><span class="p">)</span>
    <span class="k">return</span> <span class="p">[</span><span class="n">json</span><span class="p">.</span><span class="nf">loads</span><span class="p">(</span><span class="n">trend</span><span class="p">.</span><span class="n">docs</span><span class="p">)</span> <span class="k">for</span> <span class="n">trend</span> <span class="ow">in</span> <span class="n">stored</span><span class="p">]</span>

<span class="k">def</span> <span class="nf">get_news_2</span><span class="p">(</span><span class="n">content</span><span class="p">):</span>
    <span class="n">timestamp_from</span> <span class="o">=</span> <span class="nf">parse</span><span class="p">(</span><span class="n">content</span><span class="p">[</span><span class="sh">"</span><span class="s">published_utc.gte</span><span class="sh">"</span><span class="p">]).</span><span class="nf">timestamp</span><span class="p">()</span>
    <span class="n">timestamp_to</span> <span class="o">=</span> <span class="nf">parse</span><span class="p">(</span><span class="n">content</span><span class="p">[</span><span class="sh">"</span><span class="s">published_utc.lte</span><span class="sh">"</span><span class="p">]).</span><span class="nf">timestamp</span><span class="p">()</span>
    <span class="n">news_from</span> <span class="o">=</span> <span class="n">tool_rag</span><span class="p">.</span><span class="nf">get_api_documents</span><span class="p">(</span>
        <span class="n">content</span><span class="p">[</span><span class="sh">"</span><span class="s">query</span><span class="sh">"</span><span class="p">],</span> <span class="n">content</span><span class="p">[</span><span class="sh">"</span><span class="s">ticker</span><span class="sh">"</span><span class="p">],</span> <span class="sh">"</span><span class="s">get_news_2</span><span class="sh">"</span><span class="p">,</span> <span class="p">[{</span><span class="sh">"</span><span class="s">published_utc</span><span class="sh">"</span><span class="p">:</span> <span class="n">timestamp_from</span><span class="p">}])</span>
    <span class="n">news_to</span> <span class="o">=</span> <span class="n">tool_rag</span><span class="p">.</span><span class="nf">get_api_documents</span><span class="p">(</span>
        <span class="n">content</span><span class="p">[</span><span class="sh">"</span><span class="s">query</span><span class="sh">"</span><span class="p">],</span> <span class="n">content</span><span class="p">[</span><span class="sh">"</span><span class="s">ticker</span><span class="sh">"</span><span class="p">],</span> <span class="sh">"</span><span class="s">get_news_2</span><span class="sh">"</span><span class="p">,</span> <span class="p">[{</span><span class="sh">"</span><span class="s">published_utc</span><span class="sh">"</span><span class="p">:</span> <span class="n">timestamp_to</span><span class="p">}])</span>
    <span class="k">if</span> <span class="nf">len</span><span class="p">(</span><span class="n">news_from</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mi">0</span> <span class="ow">and</span> <span class="nf">len</span><span class="p">(</span><span class="n">news_to</span><span class="p">)</span> <span class="o">&gt;</span> <span class="mi">0</span><span class="p">:</span>
        <span class="n">stored</span> <span class="o">=</span> <span class="n">tool_rag</span><span class="p">.</span><span class="nf">get_api_documents</span><span class="p">(</span>
            <span class="n">content</span><span class="p">[</span><span class="sh">"</span><span class="s">query</span><span class="sh">"</span><span class="p">],</span> <span class="n">content</span><span class="p">[</span><span class="sh">"</span><span class="s">ticker</span><span class="sh">"</span><span class="p">],</span> <span class="sh">"</span><span class="s">get_news_2</span><span class="sh">"</span><span class="p">,</span>
            <span class="p">[{</span><span class="sh">"</span><span class="s">published_utc</span><span class="sh">"</span><span class="p">:</span> <span class="p">{</span><span class="sh">"</span><span class="s">$gte</span><span class="sh">"</span><span class="p">:</span> <span class="n">timestamp_from</span><span class="p">}},</span>
             <span class="p">{</span><span class="sh">"</span><span class="s">published_utc</span><span class="sh">"</span><span class="p">:</span> <span class="p">{</span><span class="sh">"</span><span class="s">$lte</span><span class="sh">"</span><span class="p">:</span> <span class="n">timestamp_to</span><span class="p">}}])</span>
        <span class="k">return</span> <span class="p">[</span><span class="n">NewsTypePoly</span><span class="p">.</span><span class="nf">model_validate_json</span><span class="p">(</span><span class="n">news</span><span class="p">.</span><span class="n">docs</span><span class="p">).</span><span class="nf">summary</span><span class="p">().</span><span class="nf">model_dump_json</span><span class="p">()</span> <span class="k">for</span> <span class="n">news</span> <span class="ow">in</span> <span class="n">stored</span><span class="p">]</span>
    <span class="k">return</span> <span class="n">tool_rest</span><span class="p">.</span><span class="nf">get_news_tagged</span><span class="p">(</span><span class="n">content</span><span class="p">)</span>
        
<span class="n">finance_tool</span> <span class="o">=</span> <span class="n">types</span><span class="p">.</span><span class="nc">Tool</span><span class="p">(</span>
    <span class="n">function_declarations</span><span class="o">=</span><span class="p">[</span>
        <span class="n">decl_get_symbol_1</span><span class="p">,</span>
        <span class="n">decl_get_symbols_1</span><span class="p">,</span>
        <span class="n">decl_get_name_1</span><span class="p">,</span>
        <span class="n">decl_get_symbol_quote_1</span><span class="p">,</span>
        <span class="n">decl_get_market_status_1</span><span class="p">,</span>
        <span class="n">decl_get_market_session_1</span><span class="p">,</span>
        <span class="n">decl_get_company_peers_1</span><span class="p">,</span>
        <span class="n">decl_get_local_datetime</span><span class="p">,</span>
        <span class="n">decl_get_last_market_close</span><span class="p">,</span>
        <span class="n">decl_get_exchange_codes_1</span><span class="p">,</span>
        <span class="n">decl_get_exchange_code_1</span><span class="p">,</span>
        <span class="n">decl_get_financials_1</span><span class="p">,</span>
        <span class="n">decl_get_daily_candlestick_2</span><span class="p">,</span>
        <span class="n">decl_get_custom_candlestick_2</span><span class="p">,</span>
        <span class="n">decl_get_ticker_overview_2</span><span class="p">,</span>
        <span class="n">decl_get_recommendation_trends_1</span><span class="p">,</span>
        <span class="n">decl_get_news_with_sentiment_2</span><span class="p">,</span>
        <span class="n">decl_get_rag_tool_response</span><span class="p">,</span>
        <span class="n">decl_get_wiki_tool_response</span><span class="p">,</span>
        <span class="n">decl_get_search_tool_response</span>
    <span class="p">]</span>
<span class="p">)</span>

<span class="n">function_handler</span> <span class="o">=</span> <span class="p">{</span>
    <span class="sh">"</span><span class="s">get_symbol_1</span><span class="sh">"</span><span class="p">:</span> <span class="n">get_symbol_1</span><span class="p">,</span>
    <span class="sh">"</span><span class="s">get_symbols_1</span><span class="sh">"</span><span class="p">:</span> <span class="n">get_symbols_1</span><span class="p">,</span>
    <span class="sh">"</span><span class="s">get_name_1</span><span class="sh">"</span><span class="p">:</span> <span class="n">get_name_1</span><span class="p">,</span>
    <span class="sh">"</span><span class="s">get_symbol_quote_1</span><span class="sh">"</span><span class="p">:</span> <span class="n">get_quote_1</span><span class="p">,</span>
    <span class="sh">"</span><span class="s">get_market_status_1</span><span class="sh">"</span><span class="p">:</span> <span class="n">get_market_status_1</span><span class="p">,</span>
    <span class="sh">"</span><span class="s">get_market_session_1</span><span class="sh">"</span><span class="p">:</span> <span class="n">get_session_1</span><span class="p">,</span>
    <span class="sh">"</span><span class="s">get_company_peers_1</span><span class="sh">"</span><span class="p">:</span> <span class="n">get_peers_1</span><span class="p">,</span>
    <span class="sh">"</span><span class="s">get_local_datetime</span><span class="sh">"</span><span class="p">:</span> <span class="n">local_datetime</span><span class="p">,</span>
    <span class="sh">"</span><span class="s">get_last_market_close</span><span class="sh">"</span><span class="p">:</span> <span class="n">last_market_close</span><span class="p">,</span>
    <span class="sh">"</span><span class="s">get_exchange_codes_1</span><span class="sh">"</span><span class="p">:</span> <span class="n">get_exchange_codes_1</span><span class="p">,</span>
    <span class="sh">"</span><span class="s">get_exchange_code_1</span><span class="sh">"</span><span class="p">:</span> <span class="n">get_exchange_code_1</span><span class="p">,</span>
    <span class="sh">"</span><span class="s">get_financials_1</span><span class="sh">"</span><span class="p">:</span> <span class="n">get_financials_1</span><span class="p">,</span>
    <span class="sh">"</span><span class="s">get_daily_candlestick_2</span><span class="sh">"</span><span class="p">:</span> <span class="n">get_daily_candle_2</span><span class="p">,</span>
    <span class="sh">"</span><span class="s">get_custom_candlestick_2</span><span class="sh">"</span><span class="p">:</span> <span class="n">get_custom_candle_2</span><span class="p">,</span>
    <span class="sh">"</span><span class="s">get_ticker_overview_2</span><span class="sh">"</span><span class="p">:</span> <span class="n">get_overview_2</span><span class="p">,</span>
    <span class="sh">"</span><span class="s">get_recommendation_trends_1</span><span class="sh">"</span><span class="p">:</span> <span class="n">get_trends_1</span><span class="p">,</span>
    <span class="sh">"</span><span class="s">get_news_with_sentiment_2</span><span class="sh">"</span><span class="p">:</span> <span class="n">get_news_2</span><span class="p">,</span>
    <span class="sh">"</span><span class="s">get_rag_tool_response</span><span class="sh">"</span><span class="p">:</span> <span class="n">ask_rag_tool</span><span class="p">,</span>
    <span class="sh">"</span><span class="s">get_wiki_tool_response</span><span class="sh">"</span><span class="p">:</span> <span class="n">ask_wiki_tool</span><span class="p">,</span>
    <span class="sh">"</span><span class="s">get_search_tool_response</span><span class="sh">"</span><span class="p">:</span> <span class="n">ask_search_tool</span>
<span class="p">}</span>
</code></pre></div></div>

<div class="language-python highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="c1"># Implement the function calling expert.
# Define the system prompt.
</span><span class="n">instruction</span> <span class="o">=</span> <span class="sa">f</span><span class="sh">"""</span><span class="s">You are a helpful and informative bot that answers finance and stock market questions. 
Only answer the question asked and do not change topic. While the answer is still
unknown you must follow these rules for predicting function call order:

RULE#1: Always consult your other functions before get_search_tool_response.
RULE#2: Always consult get_wiki_tool_response before get_search_tool_response.
RULE#3: Always consult get_search_tool_response last.
RULE#4: Always convert timestamps with get_local_datetime and use the converted date/time in your response.
RULE#5: Always incorporate as much useful information from tools and functions in your response.</span><span class="sh">"""</span>

<span class="k">def</span> <span class="nf">get_response</span><span class="p">():</span>
    <span class="c1"># Enable system prompt, function calling and minimum-randomness.
</span>    <span class="n">config_fncall</span> <span class="o">=</span> <span class="n">types</span><span class="p">.</span><span class="nc">GenerateContentConfig</span><span class="p">(</span>
        <span class="n">system_instruction</span><span class="o">=</span><span class="n">instruction</span><span class="p">,</span>
        <span class="n">tools</span><span class="o">=</span><span class="p">[</span><span class="n">finance_tool</span><span class="p">],</span>
        <span class="n">temperature</span><span class="o">=</span><span class="mf">0.0</span>
    <span class="p">)</span>
    <span class="n">memory</span><span class="p">.</span><span class="n">response</span> <span class="o">=</span> <span class="n">api</span><span class="p">.</span><span class="nf">retriable</span><span class="p">(</span>
        <span class="n">api</span><span class="p">.</span><span class="n">args</span><span class="p">.</span><span class="n">CLIENT</span><span class="p">.</span><span class="n">models</span><span class="p">.</span><span class="n">generate_content</span><span class="p">,</span>
        <span class="n">model</span><span class="o">=</span><span class="nf">api</span><span class="p">(</span><span class="n">Api</span><span class="p">.</span><span class="n">Model</span><span class="p">.</span><span class="n">GEN</span><span class="p">),</span>
        <span class="n">config</span><span class="o">=</span><span class="n">config_fncall</span><span class="p">,</span>
        <span class="n">contents</span><span class="o">=</span><span class="n">memory</span><span class="p">.</span><span class="n">contents</span><span class="p">)</span>

<span class="k">def</span> <span class="nf">retry_last_send</span><span class="p">():</span>
    <span class="n">api</span><span class="p">.</span><span class="nf">generation_fail</span><span class="p">()</span>
    <span class="n">time</span><span class="p">.</span><span class="nf">sleep</span><span class="p">(</span><span class="n">api</span><span class="p">.</span><span class="n">dt_between</span><span class="p">)</span>
    <span class="nf">get_response</span><span class="p">()</span>

<span class="nd">@retry.Retry</span><span class="p">(</span>
    <span class="n">predicate</span><span class="o">=</span><span class="n">is_retriable</span><span class="p">,</span>
    <span class="n">initial</span><span class="o">=</span><span class="mf">2.0</span><span class="p">,</span>
    <span class="n">maximum</span><span class="o">=</span><span class="mf">64.0</span><span class="p">,</span>
    <span class="n">multiplier</span><span class="o">=</span><span class="mf">2.0</span><span class="p">,</span>
    <span class="n">timeout</span><span class="o">=</span><span class="mi">600</span><span class="p">,</span>
<span class="p">)</span>
<span class="k">def</span> <span class="nf">send_message</span><span class="p">(</span><span class="n">prompt</span><span class="p">):</span>
    <span class="c1">#display(Markdown("#### Prompt"))
</span>    <span class="c1">#print(prompt, "\n")
</span>    <span class="n">memory</span><span class="p">.</span><span class="nf">set_prompt</span><span class="p">(</span><span class="n">prompt</span><span class="p">)</span>
    <span class="c1"># Handle cases with multiple chained function calls.
</span>    <span class="n">function_calling_in_process</span> <span class="o">=</span> <span class="bp">True</span>
    <span class="c1"># Send the initial user prompt and function declarations.
</span>    <span class="nf">get_response</span><span class="p">()</span>
    <span class="k">while</span> <span class="n">function_calling_in_process</span><span class="p">:</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="n">response_parts</span> <span class="o">=</span> <span class="n">memory</span><span class="p">.</span><span class="n">response</span><span class="p">.</span><span class="n">candidates</span><span class="p">[</span><span class="mi">0</span><span class="p">].</span><span class="n">content</span><span class="p">.</span><span class="n">parts</span>
            <span class="c1"># A summary response never includes function calls.
</span>            <span class="k">if</span> <span class="ow">not</span> <span class="nf">any</span><span class="p">(</span><span class="n">part</span><span class="p">.</span><span class="n">function_call</span> <span class="k">for</span> <span class="n">part</span> <span class="ow">in</span> <span class="n">response_parts</span><span class="p">):</span>
                <span class="n">memory</span><span class="p">.</span><span class="nf">set_summary</span><span class="p">(</span><span class="sh">"</span><span class="se">\n</span><span class="sh">"</span><span class="p">.</span><span class="nf">join</span><span class="p">(</span><span class="n">e</span><span class="p">.</span><span class="n">text</span> <span class="k">for</span> <span class="n">e</span> <span class="ow">in</span> <span class="n">response_parts</span><span class="p">))</span>
                <span class="n">function_calling_in_process</span> <span class="o">=</span> <span class="bp">False</span>
                <span class="k">break</span> <span class="c1"># The function calling chain is complete.
</span>            <span class="k">else</span><span class="p">:</span>
                <span class="c1"># A part can be a function call or reasoning-step.
</span>                <span class="k">for</span> <span class="n">part</span> <span class="ow">in</span> <span class="n">response_parts</span><span class="p">:</span>
                    <span class="k">if</span> <span class="n">function_call</span> <span class="p">:</span><span class="o">=</span> <span class="n">part</span><span class="p">.</span><span class="n">function_call</span><span class="p">:</span>
                        <span class="c1"># Extract the function call.
</span>                        <span class="n">fn_name</span> <span class="o">=</span> <span class="n">function_call</span><span class="p">.</span><span class="n">name</span>
                        <span class="c1">#display(Markdown("#### Predicted function name"))
</span>                        <span class="c1">#print(fn_name, "\n")
</span>                        <span class="c1"># Extract the function call arguments.
</span>                        <span class="n">fn_args</span> <span class="o">=</span> <span class="p">{</span><span class="n">key</span><span class="p">:</span> <span class="n">value</span> <span class="k">for</span> <span class="n">key</span><span class="p">,</span> <span class="n">value</span> <span class="ow">in</span> <span class="n">function_call</span><span class="p">.</span><span class="n">args</span><span class="p">.</span><span class="nf">items</span><span class="p">()}</span>
                        <span class="c1">#display(Markdown("#### Predicted function arguments"))
</span>                        <span class="c1">#print(fn_args, "\n")
</span>                        <span class="c1"># Call the predicted function.
</span>                        <span class="nf">print</span><span class="p">(</span><span class="sh">"</span><span class="s">send_message: get function response</span><span class="sh">"</span><span class="p">)</span>
                        <span class="n">api_response</span> <span class="o">=</span> <span class="n">function_handler</span><span class="p">[</span><span class="n">fn_name</span><span class="p">](</span><span class="n">fn_args</span><span class="p">)[:</span><span class="mi">20000</span><span class="p">]</span> <span class="c1"># Stay within the input token limit
</span>                        <span class="c1">#display(Markdown("#### API response"))
</span>                        <span class="c1">#print(api_response[:500], "...", "\n")
</span>                        <span class="c1"># Create an API response part.
</span>                        <span class="n">api_response_part</span> <span class="o">=</span> <span class="n">types</span><span class="p">.</span><span class="n">Part</span><span class="p">.</span><span class="nf">from_function_response</span><span class="p">(</span>
                            <span class="n">name</span><span class="o">=</span><span class="n">fn_name</span><span class="p">,</span>
                            <span class="n">response</span><span class="o">=</span><span class="p">{</span><span class="sh">"</span><span class="s">content</span><span class="sh">"</span><span class="p">:</span> <span class="n">api_response</span><span class="p">},</span>
                        <span class="p">)</span>
                        <span class="n">memory</span><span class="p">.</span><span class="nf">update_contents</span><span class="p">(</span><span class="n">function_call</span><span class="p">,</span> <span class="n">api_response_part</span><span class="p">)</span>
                    <span class="k">else</span><span class="p">:</span>
                        <span class="c1">#display(Markdown("#### Natural language reasoning step"))
</span>                        <span class="c1">#print(part.text)
</span>                        <span class="n">memory</span><span class="p">.</span><span class="nf">set_reason</span><span class="p">(</span><span class="n">part</span><span class="p">.</span><span class="n">text</span><span class="p">)</span>
                <span class="nf">print</span><span class="p">(</span><span class="sh">"</span><span class="s">send_message: updating state</span><span class="sh">"</span><span class="p">)</span>
                <span class="nf">get_response</span><span class="p">()</span> <span class="c1"># Send the updated prompt.
</span>                <span class="nf">print</span><span class="p">(</span><span class="sh">"</span><span class="s">send_message: got a response</span><span class="sh">"</span><span class="p">)</span>
        <span class="k">except</span> <span class="nb">Exception</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
            <span class="k">if</span> <span class="nf">isinstance</span><span class="p">(</span><span class="n">response_parts</span><span class="p">,</span> <span class="nb">list</span><span class="p">):</span>
                <span class="nf">print</span><span class="p">(</span><span class="sh">"</span><span class="s">send_message: generated wrong function arguments</span><span class="sh">"</span><span class="p">)</span>
            <span class="nf">retry_last_send</span><span class="p">()</span>
            
    <span class="c1"># Show the final natural language summary.
</span>    <span class="nf">display</span><span class="p">(</span><span class="nc">Markdown</span><span class="p">(</span><span class="sh">"</span><span class="s">#### Natural language response</span><span class="sh">"</span><span class="p">))</span>
    <span class="nf">display</span><span class="p">(</span><span class="nc">Markdown</span><span class="p">(</span><span class="n">memory</span><span class="p">.</span><span class="n">summary</span><span class="p">))</span>
</code></pre></div></div>

<h2 id="rag-baseline-check">RAG Baseline Check</h2>

<div class="language-python highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="n">response</span> <span class="o">=</span> <span class="n">tool_rag</span><span class="p">.</span><span class="nf">get_exchanges_csv</span><span class="p">(</span>
    <span class="sh">"""</span><span class="s">Give me a dictionary in string form. It must contain key:value pairs mapping 
    exchange code to name. Just the dictionary string in pretty form.</span><span class="sh">"""</span><span class="p">)</span>
<span class="nf">print</span><span class="p">(</span><span class="n">response</span><span class="p">.</span><span class="n">candidates</span><span class="p">[</span><span class="mi">0</span><span class="p">].</span><span class="n">content</span><span class="p">.</span><span class="n">parts</span><span class="p">[</span><span class="o">-</span><span class="mi">1</span><span class="p">].</span><span class="n">text</span><span class="p">)</span>

<span class="n">response</span> <span class="o">=</span> <span class="n">tool_rag</span><span class="p">.</span><span class="nf">get_exchanges_csv</span><span class="p">(</span>
    <span class="sh">"""</span><span class="s">What is the Germany exchange code? Return only the exchange codes as a simple 
    comma separated value that I can copy.</span><span class="sh">"""</span><span class="p">)</span>
<span class="nf">print</span><span class="p">(</span><span class="n">response</span><span class="p">.</span><span class="n">candidates</span><span class="p">[</span><span class="mi">0</span><span class="p">].</span><span class="n">content</span><span class="p">.</span><span class="n">parts</span><span class="p">[</span><span class="o">-</span><span class="mi">1</span><span class="p">].</span><span class="n">text</span><span class="p">,</span> <span class="sh">"</span><span class="se">\n</span><span class="sh">"</span><span class="p">)</span>

<span class="n">response</span> <span class="o">=</span> <span class="n">tool_rag</span><span class="p">.</span><span class="nf">get_exchanges_csv</span><span class="p">(</span><span class="sh">"</span><span class="s">What are the Germany exchanges and thier corresponding exchange codes?</span><span class="sh">"</span><span class="p">)</span>
<span class="nf">print</span><span class="p">(</span><span class="n">response</span><span class="p">.</span><span class="n">text</span><span class="p">,</span> <span class="sh">"</span><span class="se">\n</span><span class="sh">"</span><span class="p">)</span>

<span class="n">response</span> <span class="o">=</span> <span class="n">tool_rag</span><span class="p">.</span><span class="nf">generate_answer</span><span class="p">(</span><span class="sh">"</span><span class="s">What are Google</span><span class="sh">'</span><span class="s">s stock ticker symbols?</span><span class="sh">"</span><span class="p">)</span>
<span class="nf">print</span><span class="p">(</span><span class="n">response</span><span class="p">.</span><span class="n">text</span><span class="p">,</span> <span class="sh">"</span><span class="se">\n</span><span class="sh">"</span><span class="p">)</span>

<span class="n">response</span> <span class="o">=</span> <span class="n">tool_rag</span><span class="p">.</span><span class="nf">generate_answer</span><span class="p">(</span><span class="sh">"</span><span class="s">What is Facebook</span><span class="sh">'</span><span class="s">s stock ticker symbol?</span><span class="sh">"</span><span class="p">)</span>
<span class="nf">print</span><span class="p">(</span><span class="n">response</span><span class="p">.</span><span class="n">text</span><span class="p">,</span> <span class="sh">"</span><span class="se">\n</span><span class="sh">"</span><span class="p">)</span>

<span class="n">response</span> <span class="o">=</span> <span class="n">tool_rag</span><span class="p">.</span><span class="nf">get_exchanges_csv</span><span class="p">(</span><span class="sh">"</span><span class="s">What are the US exchange operating hours?</span><span class="sh">"</span><span class="p">)</span>
<span class="nf">print</span><span class="p">(</span><span class="n">response</span><span class="p">.</span><span class="n">text</span><span class="p">,</span> <span class="sh">"</span><span class="se">\n</span><span class="sh">"</span><span class="p">)</span>

<span class="n">response</span> <span class="o">=</span> <span class="n">tool_rag</span><span class="p">.</span><span class="nf">get_exchanges_csv</span><span class="p">(</span>
    <span class="sa">f</span><span class="sh">"""</span><span class="s">Answer based on your knowledge of exchange operating hours.
    Do not answer in full sentences. Omit all chat and provide the answer only.
    The fields pre_market and post_market both represent extended operating hours.

    The current date and time: </span><span class="si">{</span><span class="n">datetime</span><span class="p">.</span><span class="nf">now</span><span class="p">(</span><span class="n">GeneratedEvent</span><span class="p">.</span><span class="nf">tz</span><span class="p">()).</span><span class="nf">strftime</span><span class="p">(</span><span class="sh">'</span><span class="s">%c</span><span class="sh">'</span><span class="p">)</span><span class="si">}</span><span class="s">

    Weekdays are: Mon, Tue, Wed, Thu, Fri.
    On weekdays all exchanges open after pre-market and regular hours.
    On weekdays all exchanges close after regular and post-market hours.
    
    Weekends are: Sat, Sun.
    Always exclude weekends from exchange operating hours.
    A list of holidays in date format mm-dd-yyyy: </span><span class="si">{</span><span class="n">tool_rag</span><span class="p">.</span><span class="n">holidays</span><span class="p">[</span><span class="sh">"</span><span class="s">US</span><span class="sh">"</span><span class="p">]</span><span class="si">}</span><span class="s">
    Always exclude holidays from exchange operating hours.
    When the answer is a holiday use the prior weekday for close.
    When the answer is a holiday use the next weekday for open.
    
    Consider the US exchange</span><span class="sh">'</span><span class="s">s operating hours.
    Provide the most recent weekday</span><span class="sh">'</span><span class="s">s close including post_market hours.
    
    Answer with a date that uses this format: </span><span class="sh">'</span><span class="s">%a %b %d %X %Y</span><span class="sh">'</span><span class="s">.</span><span class="sh">"""</span><span class="p">)</span>
<span class="nf">print</span><span class="p">(</span><span class="n">response</span><span class="p">.</span><span class="n">candidates</span><span class="p">[</span><span class="mi">0</span><span class="p">].</span><span class="n">content</span><span class="p">.</span><span class="n">parts</span><span class="p">[</span><span class="o">-</span><span class="mi">1</span><span class="p">].</span><span class="n">text</span><span class="p">)</span>
</code></pre></div></div>

<div class="language-plaintext highlighter-rouge"><div class="highlight"><pre class="highlight"><code>{
    "VN": "Vietnam exchanges including HOSE, HNX and UPCOM",
    "AD": "ABU DHABI SECURITIES EXCHANGE",
    "US": "US exchanges (NYSE, Nasdaq)",
    "CO": "OMX NORDIC EXCHANGE COPENHAGEN A/S",
    "QA": "QATAR EXCHANGE",
    "BA": "BOLSA DE COMERCIO DE BUENOS AIRES",
    "MX": "BOLSA MEXICANA DE VALORES (MEXICAN STOCK EXCHANGE)",
    "PR": "PRAGUE STOCK EXCHANGE",
    "HK": "HONG KONG EXCHANGES AND CLEARING LTD",
    "CA": "Egyptian Stock Exchange",
    "AX": "ASX - ALL MARKETS",
    "SX": "DEUTSCHE BOERSE Stoxx",
    "KQ": "KOREA EXCHANGE (KOSDAQ)",
    "DB": "DUBAI FINANCIAL MARKET",
    "PM": "Philippine Stock Exchange",
    "KS": "KOREA EXCHANGE (STOCK MARKET)",
    "ST": "NASDAQ OMX NORDIC STOCKHOLM",
    "DU": "BOERSE DUESSELDORF",
    "TL": "NASDAQ OMX TALLINN",
    "AT": "ATHENS EXCHANGE S.A. CASH MARKET",
    "SW": "SWISS EXCHANGE",
    "LS": "NYSE EURONEXT - EURONEXT LISBON",
    "SI": "SINGAPORE EXCHANGE",
    "RG": "NASDAQ OMX RIGA",
    "CR": "CARACAS STOCK EXCHANGE",
    "SA": "Brazil Bolsa - Sao Paolo",
    "BH": "BAHRAIN BOURSE",
    "NZ": "NEW ZEALAND EXCHANGE LTD",
    "L": "LONDON STOCK EXCHANGE",
    "SZ": "SHENZHEN STOCK EXCHANGE",
    "IC": "NASDAQ OMX ICELAND",
    "KW": "Kuwait Stock Exchange",
    "JK": "INDONESIA STOCK EXCHANGE",
    "BE": "BOERSE BERLIN",
    "TA": "TEL AVIV STOCK EXCHANGE",
    "PA": "NYSE EURONEXT - MARCHE LIBRE PARIS",
    "V": "TSX VENTURE EXCHANGE - NEX",
    "SN": "SANTIAGO STOCK EXCHANGE",
    "BD": "BUDAPEST STOCK EXCHANGE",
    "KL": "BURSA MALAYSIA",
    "CN": "CANADIAN NATIONAL STOCK EXCHANGE",
    "VS": "NASDAQ OMX VILNIUS",
    "ME": "MOSCOW EXCHANGE",
    "CS": "CASABLANCA STOCK EXCHANGE",
    "NL": "Nigerian Stock Exchange",
    "BR": "NYSE EURONEXT - EURONEXT BRUSSELS",
    "NS": "NATIONAL STOCK EXCHANGE OF INDIA",
    "DE": "XETRA",
    "WA": "WARSAW STOCK EXCHANGE/EQUITIES/MAIN MARKET",
    "AS": "NYSE EURONEXT - EURONEXT AMSTERDAM",
    "TG": "DEUTSCHE BOERSE TradeGate",
    "IR": "IRISH STOCK EXCHANGE - ALL MARKET",
    "OL": "OSLO BORS ASA",
    "BO": "BSE LTD",
    "MT": "MALTA STOCK EXCHANGE",
    "BC": "BOLSA DE VALORES DE COLOMBIA",
    "F": "DEUTSCHE BOERSE AG",
    "HE": "NASDAQ OMX HELSINKI LTD",
    "MU": "BOERSE MUENCHEN",
    "IS": "BORSA ISTANBUL",
    "SR": "SAUDI STOCK EXCHANGE",
    "NE": "AEQUITAS NEO EXCHANGE",
    "MI": "Italian Stock Exchange",
    "SS": "SHANGHAI STOCK EXCHANGE",
    "MC": "BOLSA DE MADRID",
    "HA": "Hanover Stock Exchange",
    "VI": "Vienna Stock Exchange",
    "TWO": "TPEx",
    "HM": "HANSEATISCHE WERTPAPIERBOERSE HAMBURG",
    "TW": "TAIWAN STOCK EXCHANGE",
    "TO": "TORONTO STOCK EXCHANGE",
    "SC": "BOERSE_FRANKFURT_ZERTIFIKATE",
    "JO": "JOHANNESBURG STOCK EXCHANGE",
    "SG": "BOERSE STUTTGART",
    "RO": "BUCHAREST STOCK EXCHANGE",
    "T": "TOKYO STOCK EXCHANGE-TOKYO PRO MARKET",
    "BK": "STOCK EXCHANGE OF THAILAND"
}
</code></pre></div></div>
<p>DE, F, TG, SX, BE, DU, HA, HM, MU, SC, SG</p>

<p>The Germany exchanges and their corresponding exchange codes are: XETRA (DE), DEUTSCHE BOERSE AG (F), Hanover Stock Exchange (HA), DEUTSCHE BOERSE TradeGate (TG), BOERSE BERLIN (BE), BOERSE DUESSELDORF (DU), HANSEATISCHE WERTPAPIERBOERSE HAMBURG (HM), BOERSE MUENCHEN (MU), DEUTSCHE BOERSE Stoxx (SX), BOERSE_FRANKFURT_ZERTIFIKATE (SC), and BOERSE STUTTGART (SG).</p>

<p>I don’t know.</p>

<p>I don’t know.</p>

<p>US exchanges, including NYSE and Nasdaq, operate from 09:30 to 16:00 in the America/New_York timezone.</p>

<p>Fri Nov 28 20:00:00 2025</p>

<h2 id="sc1-baseline-check">SC1 Baseline Check</h2>

<div class="language-python highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="c1"># Wait 59s for rate-limits to reset on FREE-tier.
</span><span class="k">if</span> <span class="n">api</span><span class="p">.</span><span class="n">args</span><span class="p">.</span><span class="n">API_LIMIT</span> <span class="ow">is</span> <span class="n">Api</span><span class="p">.</span><span class="n">Limit</span><span class="p">.</span><span class="n">FREE</span><span class="p">.</span><span class="n">value</span><span class="p">:</span>
    <span class="nf">print</span><span class="p">(</span><span class="sh">"</span><span class="s">Gemini API limit is FREE. Waiting 59s...</span><span class="sh">"</span><span class="p">)</span>
    <span class="n">time</span><span class="p">.</span><span class="nf">sleep</span><span class="p">(</span><span class="mi">59</span><span class="p">)</span>
</code></pre></div></div>

<p>Gemini API limit is FREE. Waiting 59s…
Api.refill_rpm 10</p>

<div class="language-python highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="nf">send_message</span><span class="p">(</span><span class="sh">"</span><span class="s">What is the current session for US exchanges?</span><span class="sh">"</span><span class="p">)</span>
</code></pre></div></div>

<p>The US market is currently <strong>open</strong> for the <strong>regular</strong> session.</p>

<p>The current market status was last updated on <strong>Mon Dec 1 11:35:58 2025</strong> (Eastern Time). There are no holidays affecting the market today.</p>

<div class="language-python highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="nf">send_message</span><span class="p">(</span><span class="sh">"</span><span class="s">What is the US market status?</span><span class="sh">"</span><span class="p">)</span>
</code></pre></div></div>

<p>The US market is currently <strong>open</strong> for the <strong>regular</strong> session.</p>

<p>The current market status was last updated on <strong>Mon Dec 1 11:35:58 2025</strong> (Eastern Time). There are no holidays affecting the market today.</p>

<div class="language-python highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="nf">send_message</span><span class="p">(</span><span class="sh">"</span><span class="s">When was the last US market close?</span><span class="sh">"</span><span class="p">)</span>
</code></pre></div></div>

<p>The last US market close was on Friday, November 28, 2025, at 8:00:00 PM.</p>

<div class="language-python highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="nf">send_message</span><span class="p">(</span><span class="sh">"</span><span class="s">What is Apple</span><span class="sh">'</span><span class="s">s stock ticker?</span><span class="sh">"</span><span class="p">)</span>
</code></pre></div></div>

<p>Apple’s stock ticker symbol is AAPL.</p>

<div class="language-python highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="nf">send_message</span><span class="p">(</span><span class="sh">"</span><span class="s">What is the current price of Amazon stock? Display the result as a json string in markdown.</span><span class="sh">"</span><span class="p">)</span>
</code></pre></div></div>

<div class="language-json highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="p">{</span><span class="w">
</span><span class="nl">"c"</span><span class="p">:</span><span class="w"> </span><span class="mf">234.125</span><span class="p">,</span><span class="w">
</span><span class="nl">"d"</span><span class="p">:</span><span class="w"> </span><span class="mf">0.905</span><span class="p">,</span><span class="w">
</span><span class="nl">"dp"</span><span class="p">:</span><span class="w"> </span><span class="mf">0.388</span><span class="p">,</span><span class="w">
</span><span class="nl">"h"</span><span class="p">:</span><span class="w"> </span><span class="mf">235.797</span><span class="p">,</span><span class="w">
</span><span class="nl">"l"</span><span class="p">:</span><span class="w"> </span><span class="mf">231.88</span><span class="p">,</span><span class="w">
</span><span class="nl">"o"</span><span class="p">:</span><span class="w"> </span><span class="mf">231.88</span><span class="p">,</span><span class="w">
</span><span class="nl">"pc"</span><span class="p">:</span><span class="w"> </span><span class="mf">233.22</span><span class="p">,</span><span class="w">
</span><span class="nl">"t"</span><span class="p">:</span><span class="w"> </span><span class="mi">1764606938</span><span class="w">
</span><span class="p">}</span><span class="w">
</span></code></pre></div></div>

<div class="language-python highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="nf">send_message</span><span class="p">(</span><span class="sh">"""</span><span class="s">Show me Apple</span><span class="sh">'</span><span class="s">s basic financials and help me understand key performance metrics. 
How has the stock performed?</span><span class="sh">"""</span><span class="p">)</span>
</code></pre></div></div>

<p>Here’s an overview of Apple’s financials and stock performance based on the data from 2025:</p>

<p><strong>Financial Highlights:</strong></p>

<ul>
  <li><strong>Revenue Growth:</strong> Apple has demonstrated strong revenue growth with a TTM YoY growth of 6.43%.</li>
  <li><strong>Profitability:</strong> The company maintains a high level of profitability, with a TTM Net Profit Margin of 26.92%.</li>
  <li><strong>Gross Margin:</strong> Apple’s gross margin is also strong, with a TTM of 46.91%.</li>
  <li><strong>Earnings Per Share (EPS):</strong> Apple’s EPS has grown significantly, with a TTM EPS Excl. Extra Items of 7.4593, reflecting a growth of 22.89% YoY.</li>
  <li><strong>P/E Ratio:</strong> The trailing twelve months (TTM) Price-to-Earnings (P/E) ratio is 36.7859. The forward P/E ratio is 33.6884.</li>
  <li><strong>Dividends:</strong> Apple pays a dividend, with a current dividend yield of 0.3743%. The dividend per share TTM is $1.0318.</li>
  <li><strong>Return on Equity (ROE):</strong> Apple’s ROE is very high, with a TTM value of 164.05%.</li>
  <li><strong>52-Week Performance:</strong> The 52 week high is 280.38, reached on 2025-11-25, and the 52 week low is 169.2101, reached on 2025-04-08.</li>
  <li><strong>Stock Performance:</strong>
    <ul>
      <li>The stock has a 5-Day Price Return Daily of 2.711%.</li>
      <li>The Month-to-Date Price Return Daily is 3.1364%.</li>
      <li>The Year-to-Date Price Return Daily is 11.3529%.</li>
      <li>The 52-Week Price Return Daily is 18.6293%.</li>
      <li>The 13-Week Price Return Daily is 19.9045%.</li>
      <li>The 26-Week Price Return Daily is 39.2788%.</li>
    </ul>
  </li>
</ul>

<p><strong>Key Performance Metrics:</strong></p>

<ul>
  <li><strong>Beta:</strong> The beta is 1.0957, indicating that the stock is slightly more volatile than the market.</li>
  <li><strong>PEG Ratio:</strong> The PEG ratio is 1.6255, which is above 1, suggesting that the stock may be overvalued relative to its earnings growth.</li>
</ul>

<p><strong>Financial Health:</strong></p>

<ul>
  <li><strong>Current Ratio:</strong> The current ratio is 0.8933, which is below 1, suggesting that the company may have some liquidity issues.</li>
  <li><strong>Debt-to-Equity Ratio:</strong> The Long Term Debt to Equity Annual is 1.0623, indicating a moderate level of debt relative to equity.</li>
</ul>

<p><strong>Valuation:</strong></p>

<ul>
  <li><strong>Price-to-Book Ratio (P/B):</strong> The P/B ratio is 55.8825, which is very high, suggesting that the stock may be overvalued.</li>
  <li><strong>Price-to-Sales Ratio (P/S):</strong> The P/S ratio is 9.9009.</li>
</ul>

<p><strong>Additional Indicators:</strong></p>

<ul>
  <li><strong>Price Relative to S&amp;P 500:</strong>
    <ul>
      <li>Price Relative to S&amp;P 500 13 Week: 14.5926</li>
    </ul>
  </li>
  <li><strong>Price Relative to S&amp;P 500 26 Week:</strong> 23.6753</li>
  <li><strong>Price Relative to S&amp;P 500 52 Week:</strong> 4.8542</li>
</ul>

<div class="language-python highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="nf">send_message</span><span class="p">(</span><span class="sh">"</span><span class="s">I need Apple</span><span class="sh">'</span><span class="s">s daily candlestick from 2025-05-05</span><span class="sh">"</span><span class="p">)</span>
</code></pre></div></div>

<p>Here is Apple’s daily candlestick data for 2025-05-05:</p>

<ul>
  <li><strong>Symbol:</strong> AAPL</li>
  <li><strong>Open:</strong> 203.1</li>
  <li><strong>High:</strong> 204.1</li>
  <li><strong>Low:</strong> 198.21</li>
  <li><strong>Close:</strong> 198.89</li>
  <li><strong>Volume:</strong> 69018452</li>
  <li><strong>Pre-market:</strong> 205.0</li>
  <li><strong>After-hours:</strong> 198.6</li>
</ul>

<div class="language-python highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="nf">send_message</span><span class="p">(</span><span class="sh">"</span><span class="s">Tell me who are Apple</span><span class="sh">'</span><span class="s">s peers?</span><span class="sh">"</span><span class="p">)</span>
</code></pre></div></div>

<p>Apple’s peers are: DELL TECHNOLOGIES -C (DELL), WESTERN DIGITAL CORP (WDC), SANDISK CORP (SNDK), HEWLETT PACKARD ENTERPRISE (HPE), PURE STORAGE INC - CLASS A (PSTG), HP INC (HPQ), NETAPP INC (NTAP), SUPER MICRO COMPUTER INC (SMCI), IONQ INC (IONQ), QUANTUM COMPUTING INC (QUBT), COMPOSECURE INC-A (CMPO).</p>

<div class="language-python highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="nf">send_message</span><span class="p">(</span><span class="sh">"</span><span class="s">Tell me who are Amazon</span><span class="sh">'</span><span class="s">s peers?</span><span class="sh">"</span><span class="p">)</span>
</code></pre></div></div>

<p>Amazon’s peers include Coupang Inc (CPNG), eBay Inc (EBAY), Dillard’s Inc-CL A (DDS), Ollie’s Bargain Outlet Holdings (OLLI), Macy’s Inc (M), Etsy Inc (ETSY), Kohl’s Corp (KSS), Pattern Group Inc-CL A (PTRN), Savers Value Village Inc (SVV), and Groupon Inc (GRPN).</p>

<div class="language-python highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="nf">send_message</span><span class="p">(</span><span class="sh">"""</span><span class="s">Locate Apple</span><span class="sh">'</span><span class="s">s stock ticker, then download recommendation trends of all Apple</span><span class="sh">'</span><span class="s">s peers by sub-industry, 
and then finally compare them.</span><span class="sh">"""</span><span class="p">)</span>
</code></pre></div></div>

<p>Apple’s stock ticker is <strong>AAPL</strong>.</p>

<p>Here is a comparison of the latest analyst recommendation trends for Apple and its peers in the sub-industry, based on data as of <strong>Sun Dec 1 00:00:00 2024</strong>:</p>

<table>
  <thead>
    <tr>
      <th style="text-align: left">Company (Ticker)</th>
      <th style="text-align: left">Strong Buy</th>
      <th style="text-align: left">Buy</th>
      <th style="text-align: left">Hold</th>
      <th style="text-align: left">Sell</th>
      <th style="text-align: left">Strong Sell</th>
      <th style="text-align: left">Total Recommendations</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align: left"><strong>Apple (AAPL)</strong></td>
      <td style="text-align: left">15</td>
      <td style="text-align: left">23</td>
      <td style="text-align: left">16</td>
      <td style="text-align: left">2</td>
      <td style="text-align: left">0</td>
      <td style="text-align: left">56</td>
    </tr>
    <tr>
      <td style="text-align: left"><strong>DELL TECHNOLOGIES -C (DELL)</strong></td>
      <td style="text-align: left">8</td>
      <td style="text-align: left">16</td>
      <td style="text-align: left">7</td>
      <td style="text-align: left">1</td>
      <td style="text-align: left">0</td>
      <td style="text-align: left">32</td>
    </tr>
    <tr>
      <td style="text-align: left"><strong>WESTERN DIGITAL CORP (WDC)</strong></td>
      <td style="text-align: left">6</td>
      <td style="text-align: left">19</td>
      <td style="text-align: left">6</td>
      <td style="text-align: left">0</td>
      <td style="text-align: left">0</td>
      <td style="text-align: left">31</td>
    </tr>
    <tr>
      <td style="text-align: left"><strong>SANDISK CORP (SNDK)</strong></td>
      <td style="text-align: left">7</td>
      <td style="text-align: left">11</td>
      <td style="text-align: left">6</td>
      <td style="text-align: left">0</td>
      <td style="text-align: left">0</td>
      <td style="text-align: left">24</td>
    </tr>
    <tr>
      <td style="text-align: left"><strong>HEWLETT PACKARD ENTERPRISE (HPE)</strong></td>
      <td style="text-align: left">6</td>
      <td style="text-align: left">7</td>
      <td style="text-align: left">13</td>
      <td style="text-align: left">0</td>
      <td style="text-align: left">0</td>
      <td style="text-align: left">26</td>
    </tr>
    <tr>
      <td style="text-align: left"><strong>PURE STORAGE INC - CLASS A (PSTG)</strong></td>
      <td style="text-align: left">7</td>
      <td style="text-align: left">13</td>
      <td style="text-align: left">6</td>
      <td style="text-align: left">1</td>
      <td style="text-align: left">0</td>
      <td style="text-align: left">27</td>
    </tr>
    <tr>
      <td style="text-align: left"><strong>HP INC (HPQ)</strong></td>
      <td style="text-align: left">1</td>
      <td style="text-align: left">1</td>
      <td style="text-align: left">16</td>
      <td style="text-align: left">6</td>
      <td style="text-align: left">1</td>
      <td style="text-align: left">25</td>
    </tr>
    <tr>
      <td style="text-align: left"><strong>NETAPP INC (NTAP)</strong></td>
      <td style="text-align: left">3</td>
      <td style="text-align: left">10</td>
      <td style="text-align: left">14</td>
      <td style="text-align: left">0</td>
      <td style="text-align: left">0</td>
      <td style="text-align: left">27</td>
    </tr>
    <tr>
      <td style="text-align: left"><strong>SUPER MICRO COMPUTER INC (SMCI)</strong></td>
      <td style="text-align: left">4</td>
      <td style="text-align: left">10</td>
      <td style="text-align: left">9</td>
      <td style="text-align: left">3</td>
      <td style="text-align: left">0</td>
      <td style="text-align: left">26</td>
    </tr>
    <tr>
      <td style="text-align: left"><strong>IONQ INC (IONQ)</strong></td>
      <td style="text-align: left">2</td>
      <td style="text-align: left">10</td>
      <td style="text-align: left">4</td>
      <td style="text-align: left">0</td>
      <td style="text-align: left">0</td>
      <td style="text-align: left">16</td>
    </tr>
    <tr>
      <td style="text-align: left"><strong>QUANTUM COMPUTING INC (QUBT)</strong></td>
      <td style="text-align: left">2</td>
      <td style="text-align: left">5</td>
      <td style="text-align: left">2</td>
      <td style="text-align: left">0</td>
      <td style="text-align: left">0</td>
      <td style="text-align: left">9</td>
    </tr>
    <tr>
      <td style="text-align: left"><strong>COMPOSECURE INC-A (CMPO)</strong></td>
      <td style="text-align: left">2</td>
      <td style="text-align: left">8</td>
      <td style="text-align: left">2</td>
      <td style="text-align: left">0</td>
      <td style="text-align: left">0</td>
      <td style="text-align: left">12</td>
    </tr>
  </tbody>
</table>

<h3 id="key-observations">Key Observations:</h3>

<ul>
  <li><strong>Apple (AAPL)</strong> has the highest number of total recommendations (56) and a strong overall positive sentiment, with 38 “Buy” or “Strong Buy” ratings compared to 18 “Hold” or “Sell” ratings.</li>
  <li><strong>WESTERN DIGITAL CORP (WDC)</strong> has the highest proportion of “Buy” ratings among its peers, with 19 “Buy” and 6 “Strong Buy” ratings, and no “Sell” or “Strong Sell” ratings.</li>
  <li><strong>HP INC (HPQ)</strong> stands out with the most cautious outlook, having the highest number of “Hold” (16) and “Sell” (6) ratings, and the lowest number of “Strong Buy” ratings (1) among the group.</li>
  <li><strong>NETAPP INC (NTAP)</strong> and <strong>HEWLETT PACKARD ENTERPRISE (HPE)</strong> have a higher concentration of “Hold” ratings, suggesting analysts are taking a more neutral stance on these companies.</li>
  <li>Smaller companies like <strong>IONQ INC (IONQ)</strong>, <strong>QUANTUM COMPUTING INC (QUBT)</strong>, and <strong>COMPOSECURE INC-A (CMPO)</strong> have fewer total recommendations, but generally maintain a positive to neutral outlook.</li>
</ul>

<div class="language-python highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="nf">send_message</span><span class="p">(</span><span class="sh">"""</span><span class="s">Tell me Amazon</span><span class="sh">'</span><span class="s">s current share price and provide candlestick data for the past month. 
Sort the data in descending order by date. Format the prices consistently as currency. 
Round prices to two decimal places. 
Present the data with multiple columns for display in markdown. 
Discuss and provide details about any patterns you notice in the price data. 
Correlate recent patterns with news over the same date range.</span><span class="sh">"""</span><span class="p">)</span>
</code></pre></div></div>

<p>Amazon’s (AMZN) current share price is $234.17, with a change of $0.95 and a percentage change of 0.4073%. The high price of the day was $235.797, the low price was $231.88, and the open price was $231.88. The previous close price was $233.22. This information is as of Mon Dec 1 11:37:16 2025.</p>

<p>Here is the candlestick data for Amazon (AMZN) for the past month, sorted in descending order by date:</p>

<table>
  <thead>
    <tr>
      <th>Date</th>
      <th>Open</th>
      <th>High</th>
      <th>Low</th>
      <th>Close</th>
      <th>Volume</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Fri Nov 28 00:00:00 2025</td>
      <td>$231.24</td>
      <td>$233.29</td>
      <td>$230.22</td>
      <td>$233.22</td>
      <td>20,250,425</td>
    </tr>
    <tr>
      <td>Wed Nov 26 00:00:00 2025</td>
      <td>$230.74</td>
      <td>$231.75</td>
      <td>$228.77</td>
      <td>$229.16</td>
      <td>38,497,719</td>
    </tr>
    <tr>
      <td>Tue Nov 25 00:00:00 2025</td>
      <td>$226.38</td>
      <td>$230.52</td>
      <td>$223.80</td>
      <td>$229.67</td>
      <td>39,379,339</td>
    </tr>
    <tr>
      <td>Mon Nov 24 00:00:00 2025</td>
      <td>$222.56</td>
      <td>$227.33</td>
      <td>$222.27</td>
      <td>$226.28</td>
      <td>54,318,223</td>
    </tr>
    <tr>
      <td>Fri Nov 21 00:00:00 2025</td>
      <td>$216.34</td>
      <td>$222.21</td>
      <td>$215.18</td>
      <td>$220.69</td>
      <td>68,490,453</td>
    </tr>
    <tr>
      <td>Thu Nov 20 00:00:00 2025</td>
      <td>$227.05</td>
      <td>$227.41</td>
      <td>$216.74</td>
      <td>$217.14</td>
      <td>50,308,862</td>
    </tr>
    <tr>
      <td>Wed Nov 19 00:00:00 2025</td>
      <td>$223.74</td>
      <td>$223.74</td>
      <td>$218.52</td>
      <td>$222.69</td>
      <td>58,335,353</td>
    </tr>
    <tr>
      <td>Tue Nov 18 00:00:00 2025</td>
      <td>$228.10</td>
      <td>$230.20</td>
      <td>$222.42</td>
      <td>$222.55</td>
      <td>60,608,442</td>
    </tr>
    <tr>
      <td>Mon Nov 17 00:00:00 2025</td>
      <td>$233.25</td>
      <td>$234.60</td>
      <td>$229.19</td>
      <td>$232.87</td>
      <td>59,918,908</td>
    </tr>
    <tr>
      <td>Fri Nov 14 00:00:00 2025</td>
      <td>$235.06</td>
      <td>$238.73</td>
      <td>$232.89</td>
      <td>$234.69</td>
      <td>38,956,619</td>
    </tr>
    <tr>
      <td>Thu Nov 13 00:00:00 2025</td>
      <td>$243.05</td>
      <td>$243.75</td>
      <td>$236.50</td>
      <td>$237.58</td>
      <td>41,401,638</td>
    </tr>
    <tr>
      <td>Wed Nov 12 00:00:00 2025</td>
      <td>$250.24</td>
      <td>$250.37</td>
      <td>$243.75</td>
      <td>$244.20</td>
      <td>31,190,063</td>
    </tr>
    <tr>
      <td>Tue Nov 11 00:00:00 2025</td>
      <td>$248.41</td>
      <td>$249.75</td>
      <td>$247.23</td>
      <td>$249.10</td>
      <td>23,563,960</td>
    </tr>
    <tr>
      <td>Mon Nov 10 00:00:00 2025</td>
      <td>$248.34</td>
      <td>$251.75</td>
      <td>$245.59</td>
      <td>$248.40</td>
      <td>36,476,474</td>
    </tr>
    <tr>
      <td>Fri Nov 7 00:00:00 2025</td>
      <td>$242.90</td>
      <td>$244.90</td>
      <td>$238.49</td>
      <td>$244.41</td>
      <td>46,374,294</td>
    </tr>
    <tr>
      <td>Thu Nov 6 00:00:00 2025</td>
      <td>$249.15</td>
      <td>$250.38</td>
      <td>$242.17</td>
      <td>$243.04</td>
      <td>46,004,201</td>
    </tr>
    <tr>
      <td>Wed Nov 5 00:00:00 2025</td>
      <td>$249.03</td>
      <td>$251.00</td>
      <td>$246.16</td>
      <td>$250.20</td>
      <td>40,610,602</td>
    </tr>
    <tr>
      <td>Tue Nov 4 00:00:00 2025</td>
      <td>$250.38</td>
      <td>$257.01</td>
      <td>$248.66</td>
      <td>$249.32</td>
      <td>51,546,311</td>
    </tr>
    <tr>
      <td>Mon Nov 3 00:00:00 2025</td>
      <td>$255.36</td>
      <td>$258.60</td>
      <td>$252.90</td>
      <td>$254.00</td>
      <td>95,997,714</td>
    </tr>
  </tbody>
</table>

<p><strong>Price Data Patterns and Correlation with News:</strong></p>

<p>Looking at the candlestick data for Amazon (AMZN) over the past month, several patterns emerge:</p>

<ul>
  <li>
    <p><strong>Early November Surge and Mid-Month Dip:</strong> The stock started November strong, reaching a high of $258.60 on Mon Nov 3 2025. This initial surge aligns with news from early November, where Amazon announced a significant $38 billion cloud computing services deal with OpenAI, which was seen as a major positive for its AWS segment and AI growth. Several articles from Nov 3rd and 4th highlight this deal and its positive impact on Amazon’s stock.</p>

    <p>However, the price then experienced a noticeable dip, falling to a low of $215.18 on Fri Nov 21 2025. This decline coincides with news around Nov 13th-19th, where concerns about AI investment returns, potential market bubbles, and aggressive capital expenditures by tech giants were widely discussed. Articles from Nov 13th and 14th mention a tech stock selloff and Amazon’s stock shedding market value. Additionally, news on Nov 19th highlighted Amazon selling shares of quantum computing and AI stocks (IonQ and AMD), potentially taking profits amid valuation concerns.</p>
  </li>
  <li>
    <p><strong>Late November Recovery:</strong> Towards the end of November, the stock showed signs of recovery, closing at $233.22 on Fri Nov 28 2025. This recovery aligns with a renewed positive sentiment around Amazon’s AI initiatives and its strong position in e-commerce and cloud computing. News from Nov 25th-30th consistently highlights Amazon’s strong AWS cloud computing business, its AI growth engine, and its potential to reach a $3 trillion market cap. Several articles also mention Amazon’s legal victory in New York and its strong performance during Black Friday.</p>
  </li>
  <li>
    <p><strong>Volume Fluctuations:</strong> The trading volume was notably high at the beginning of November (95,997,714 on Nov 3rd) during the initial price surge, indicating strong investor interest. Volume remained relatively high during the mid-month dip, suggesting active trading during the period of uncertainty. Towards the end of the month, as the stock recovered, the volume was still substantial, but not as high as the initial surge.</p>
  </li>
</ul>

<p>In summary, Amazon’s stock performance in November 2025 appears to be heavily influenced by news and sentiment surrounding its AI investments and cloud computing business. Initial excitement over a major OpenAI deal drove the stock up, while broader market concerns about AI valuations and Amazon’s capital expenditures led to a mid-month correction. The stock then recovered as positive news about its AI growth engine, e-commerce strength, and legal victories re-emerged.</p>

<div class="language-python highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="nf">send_message</span><span class="p">(</span><span class="sh">"</span><span class="s">What is Apple</span><span class="sh">'</span><span class="s">s ticker overview</span><span class="sh">"</span><span class="p">)</span>
</code></pre></div></div>

<p>Apple Inc. (AAPL) is a technology company based in Cupertino, CA. Their address is ONE APPLE PARK WAY, CUPERTINO, CA, 95014, and their phone number is (408) 996-1010. Apple was listed on December 12, 1980. They have 166,000 employees and a market cap of $4,120,386,034,050.00. Their primary exchange is XNAS. Apple’s description states: “Apple is among the largest companies in the world, with a broad portfolio of hardware and software products targeted at consumers and businesses. Apple’s iPhone makes up a majority of the firm sales, and Apple’s other products like Mac, iPad, and Watch are designed around the iPhone as the focal point of an expansive software ecosystem. Apple has progressively worked to add new applications, like streaming video, subscription bundles, and augmented reality. The firm designs its own software and semiconductors while working with subcontractors like Foxconn and TSMC to build its products and chips. Slightly less than half of Apple’s sales come directly through its flagship stores, with a majority of sales coming indirectly through partnerships and distribution.”</p>

<div class="language-python highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="nf">send_message</span><span class="p">(</span><span class="sh">"</span><span class="s">What is Google</span><span class="sh">'</span><span class="s">s stock ticker symbol?</span><span class="sh">"</span><span class="p">)</span>
</code></pre></div></div>

<p>Google is listed on the NASDAQ stock exchange under the ticker symbols <strong>GOOGL</strong> (Class A shares) and <strong>GOOG</strong> (Class C shares). These symbols now represent Alphabet Inc., Google’s holding company.</p>

<p>Google is also listed on the Frankfurt Stock Exchange under the ticker symbol <strong>GGQ1</strong>.</p>

<div class="language-python highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="nf">send_message</span><span class="p">(</span><span class="sh">"</span><span class="s">What is MGM Studio</span><span class="sh">'</span><span class="s">s stock symbol?</span><span class="sh">"</span><span class="p">)</span>
</code></pre></div></div>

<p>I am unable to find the stock symbol for MGM Studios.</p>

<div class="language-python highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="nf">send_message</span><span class="p">(</span><span class="sh">"</span><span class="s">What is MGM Studio</span><span class="sh">'</span><span class="s">s owner company stock symbol?</span><span class="sh">"</span><span class="p">)</span>
</code></pre></div></div>

<p>MGM Studios is owned by Amazon, and Amazon’s stock symbol is AMZN.</p>

<div class="language-python highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="nf">send_message</span><span class="p">(</span><span class="sh">"</span><span class="s">What is Facebook</span><span class="sh">'</span><span class="s">s stock ticker symbol?</span><span class="sh">"</span><span class="p">)</span>
</code></pre></div></div>

<p>Facebook’s stock ticker symbol is META.</p>

<div class="language-python highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="nf">send_message</span><span class="p">(</span><span class="sh">"""</span><span class="s">Compare Amazon</span><span class="sh">'</span><span class="s">s bullish versus bearish predictions from Oct 01 2025 until today. 
Include a discussion of recommendation trends, and sentiment analysis of news from the same dates. 
Discuss any patterns or correlations you find.</span><span class="sh">"""</span><span class="p">)</span>
</code></pre></div></div>

<p>From October 1, 2025, until today, December 1, 2025, Amazon (AMZN) has consistently received a strong bullish outlook from analysts, while news sentiment has been more mixed, reflecting both significant growth opportunities and some operational challenges.</p>

<p><strong>Recommendation Trends (October 1, 2025 - December 1, 2025):</strong>
Analyst recommendations for Amazon have been overwhelmingly positive throughout this period:</p>
<ul>
  <li><strong>October 1, 2025:</strong> 52 “buy” recommendations, 3 “hold,” and 23 “strongBuy.”</li>
  <li><strong>November 1, 2025:</strong> 54 “buy” recommendations, 2 “hold,” and 22 “strongBuy.”</li>
  <li><strong>December 1, 2025:</strong> 52 “buy” recommendations, 5 “hold,” and 21 “strongBuy.”</li>
</ul>

<p>Notably, there were no “sell” or “strongSell” recommendations during these months, indicating a consistently bullish sentiment from financial analysts.</p>

<p><strong>Sentiment Analysis of News (October 1, 2025 - December 1, 2025):</strong></p>

<p><strong>Bullish/Positive Sentiment:</strong></p>
<ul>
  <li><strong>AWS Dominance and AI Leadership:</strong> Numerous articles highlight the accelerating growth of Amazon Web Services (AWS), Amazon’s cloud computing division, with reported 20% year-over-year revenue increases. Significant investments in AI infrastructure, custom AI chips (Trainium, Inferentia), and strategic partnerships with companies like OpenAI (including a $38 billion cloud infrastructure deal) and Anthropic are consistently cited as major drivers for future growth and profitability. Amazon’s role as a key player in the AI revolution and its potential to reach a $3-4 trillion market capitalization are frequently emphasized.</li>
  <li><strong>E-commerce Strength and Efficiency:</strong> Amazon’s strong market share in e-commerce, improvements in operational efficiency through robotics and AI-driven logistics, and expanding delivery networks contribute to positive sentiment.</li>
  <li><strong>Diversified Business Model:</strong> The company’s diverse revenue streams, spanning e-commerce, cloud computing, advertising, and emerging technologies like satellite internet, are seen as providing resilience and multiple avenues for growth.</li>
  <li><strong>Analyst Confidence:</strong> Many news pieces report positive analyst ratings, increased price targets (e.g., Wedbush raising to $340), and a general belief that Amazon is an attractive long-term investment.</li>
</ul>

<p><strong>Bearish/Negative Sentiment:</strong></p>
<ul>
  <li><strong>Job Cuts and Restructuring:</strong> Several articles report significant corporate layoffs, including up to 30,000 jobs and 15% of the HR staff. While sometimes framed as strategic restructuring for the AI era and cost-cutting measures, these are also viewed as indicators of potential workforce instability and operational challenges.</li>
  <li><strong>High Capital Expenditures:</strong> Concerns are raised about Amazon’s aggressive capital expenditures in AI infrastructure (e.g., $125 billion planned investment), with some analysts questioning the immediate return on investment and potential impact on free cash flow.</li>
  <li><strong>Competition and Market Share:</strong> While a leader, Amazon faces intense competition in cloud computing (from Microsoft Azure and Google Cloud) and digital advertising (from Google and Meta). Some articles note instances where Amazon’s stock has underperformed the broader S&amp;P 500 or other “Magnificent Seven” stocks.</li>
  <li><strong>Operational Issues:</strong> A major global AWS outage due to a software bug was reported in late October, leading to negative sentiment regarding service reliability.</li>
  <li><strong>Partnership Shifts:</strong> UPS is strategically reducing its shipping volumes with Amazon due to lower margins, indicating a shift in that business relationship.</li>
</ul>

<p><strong>Patterns and Correlations:</strong></p>

<ol>
  <li><strong>AI as a Central Theme:</strong> AI is the most prominent theme, acting as both a significant bullish catalyst and a source of some bearish concerns. The market is excited about Amazon’s AI potential, particularly through AWS, but also watchful of the massive investments required and their impact on profitability and workforce.</li>
  <li><strong>AWS Performance is Key:</strong> The performance and strategic moves of AWS are consistently highlighted as critical to Amazon’s overall financial health and investor sentiment. Positive news about AWS directly correlates with bullish sentiment for the company.</li>
  <li><strong>Analyst Optimism vs. News Nuance:</strong> There’s a clear divergence between the consistently strong bullish analyst recommendations and the more nuanced, sometimes cautionary, tone of news articles. Analysts appear to be focusing on the long-term strategic advantages and growth potential, while news reports cover both the positive developments and the immediate operational challenges.</li>
  <li><strong>Market Concentration:</strong> Amazon is frequently discussed within the context of the “Magnificent Seven” tech stocks, which have largely driven market performance. This highlights Amazon’s systemic importance but also raises broader market concerns about concentration risk and potential overvaluation in the tech sector.</li>
</ol>

<p>In conclusion, Amazon’s bullish predictions are strongly supported by its leadership in cloud computing, aggressive AI investments, and diversified business model. Bearish sentiments are primarily linked to large-scale layoffs and the financial implications of massive AI capital expenditures. The overarching pattern is that the market views Amazon’s strategic positioning in AI and cloud as a powerful long-term growth engine, despite short-term operational adjustments and competitive pressures.</p>

<div class="language-python highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="nf">send_message</span><span class="p">(</span><span class="sh">"""</span><span class="s">Compare Google</span><span class="sh">'</span><span class="s">s bullish versus bearish predictions from Oct 01 2025 until today. 
Include a discussion of recommendation trends, and sentiment analysis of news from the same dates. 
Discuss any patterns or correlations you find.</span><span class="sh">"""</span><span class="p">)</span>
</code></pre></div></div>

<p>Based on the analysis of analyst recommendations and news sentiment for Alphabet Inc. (GOOGL/GOOG) from <strong>October 1, 2025, until today, December 1, 2025</strong>, the overall prediction for the company is overwhelmingly <strong>bullish</strong>.</p>

<p>The market’s confidence is driven almost entirely by the company’s successful execution of its Artificial Intelligence (AI) strategy, which has translated into strong financial performance and strategic investments.</p>

<hr />

<h3 id="1-recommendation-trends-bullish-vs-bearish">1. Recommendation Trends (Bullish vs. Bearish)</h3>

<p>Analyst sentiment for Alphabet Inc. (GOOGL) remained highly bullish throughout the period, with a notable increase in conviction.</p>

<table>
  <thead>
    <tr>
      <th style="text-align: left">Period</th>
      <th style="text-align: left">Strong Buy</th>
      <th style="text-align: left">Buy</th>
      <th style="text-align: left">Hold</th>
      <th style="text-align: left">Sell</th>
      <th style="text-align: left">Strong Sell</th>
      <th style="text-align: left">Total Bullish (Strong Buy + Buy)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td style="text-align: left"><strong>Dec 1, 2025</strong></td>
      <td style="text-align: left">20</td>
      <td style="text-align: left">43</td>
      <td style="text-align: left">10</td>
      <td style="text-align: left">0</td>
      <td style="text-align: left">0</td>
      <td style="text-align: left"><strong>63 (86.3%)</strong></td>
    </tr>
    <tr>
      <td style="text-align: left"><strong>Nov 1, 2025</strong></td>
      <td style="text-align: left">21</td>
      <td style="text-align: left">41</td>
      <td style="text-align: left">12</td>
      <td style="text-align: left">0</td>
      <td style="text-align: left">0</td>
      <td style="text-align: left"><strong>62 (83.8%)</strong></td>
    </tr>
    <tr>
      <td style="text-align: left"><strong>Oct 1, 2025</strong></td>
      <td style="text-align: left">21</td>
      <td style="text-align: left">39</td>
      <td style="text-align: left">13</td>
      <td style="text-align: left">0</td>
      <td style="text-align: left">0</td>
      <td style="text-align: left"><strong>60 (82.2%)</strong></td>
    </tr>
  </tbody>
</table>

<ul>
  <li><strong>Bullish Prediction:</strong> The number of analysts recommending a <strong>“Buy”</strong> or <strong>“Strong Buy”</strong> increased from 60 to 63, raising the overall bullish percentage from 82.2% to 86.3%.</li>
  <li><strong>Bearish Prediction:</strong> There were <strong>zero “Sell” or “Strong Sell”</strong> recommendations in any month, indicating a complete absence of bearish conviction among major analysts. The slight decrease in total recommendations from November to December is due to a few analysts shifting from a neutral “Hold” rating to a more positive “Buy” rating.</li>
</ul>

<hr />

<h3 id="2-sentiment-analysis-of-news-october-1-2025--november-28-2025">2. Sentiment Analysis of News (October 1, 2025 – November 28, 2025)</h3>

<p>News sentiment during this period was overwhelmingly positive, focusing on AI-driven growth and financial strength.</p>

<h4 id="bullish-drivers-positive-sentiment">Bullish Drivers (Positive Sentiment)</h4>

<p>The primary bullish narrative centers on Alphabet’s AI leadership and financial execution:</p>

<ul>
  <li><strong>AI Dominance and Innovation:</strong> The launch and success of the <strong>Gemini 3 AI model</strong> and its integration across Google Search, YouTube, and Google Cloud were consistently highlighted. News articles praised Alphabet’s vertically integrated AI stack, including its custom <strong>Tensor Processing Units (TPUs)</strong>, which are seen as a cost-effective challenge to Nvidia’s GPU dominance.</li>
  <li><strong>Record Financial Performance:</strong> The company reported its <strong>first $100 billion quarterly revenue</strong>, driven by strong growth in Google Services (advertising) and <strong>Google Cloud (34% YoY growth)</strong>. Analysts frequently noted the company’s strong cash flow and relatively attractive valuation (low P/E ratio) compared to other “Magnificent Seven” stocks.</li>
  <li><strong>Strategic Investor Confidence:</strong> A major bullish catalyst was the disclosure of a <strong>$4-5 billion investment by Warren Buffett’s Berkshire Hathaway</strong> in Q3, signaling confidence from a prominent value investor in Alphabet’s long-term growth and stability.</li>
  <li><strong>Massive Infrastructure Investment:</strong> Alphabet announced significant capital expenditure plans, including a <strong>$40 billion investment in Texas</strong> by 2027 for cloud and AI infrastructure, and a <strong>$6.4 billion expansion in Germany</strong>, reinforcing its commitment to the AI race.</li>
</ul>

<h4 id="bearish-and-neutral-factors">Bearish and Neutral Factors</h4>

<p>The few negative or cautionary themes were generally overshadowed by the positive AI narrative:</p>

<ul>
  <li><strong>Competitive Threats:</strong> The launch of <strong>OpenAI’s ChatGPT Atlas browser</strong> caused a minor, short-term stock drop (approx. 2%), raising concerns about a potential challenge to Google’s search and Chrome dominance. However, this was quickly mitigated by news of Google’s own AI integration into Chrome.</li>
  <li><strong>Regulatory/Legal Issues:</strong> The company was named in a <strong>NYC lawsuit over child social media addiction</strong> (alongside Meta and Snap), and faced ongoing, though less prominent, geopolitical concerns about moving production out of China.</li>
  <li><strong>Market Bubble Caution:</strong> Several articles warned of a potential <strong>“AI bubble”</strong> or market overvaluation, but often positioned Alphabet as the “least overvalued” or a “safer” long-term AI play due to its diversified, profitable core business.</li>
</ul>

<hr />

<h3 id="3-patterns-and-correlations">3. Patterns and Correlations</h3>

<p>A clear and strong correlation exists between the news sentiment and analyst recommendations:</p>

<ol>
  <li><strong>AI Success Drives Bullish Consensus:</strong> The consistent stream of positive news regarding Alphabet’s AI execution (Gemini, TPUs, Cloud growth) directly correlated with the increase in “Buy” ratings and the complete absence of “Sell” ratings. The market views Alphabet’s AI strategy as a successful, revenue-generating endeavor, unlike competitors whose AI spending is sometimes viewed with skepticism (e.g., Meta’s stock drop after announcing high AI CapEx).</li>
  <li><strong>Value and Growth Alignment:</strong> The news frequently highlighted Alphabet’s dual appeal as both a <strong>high-growth AI leader</strong> and a <strong>value stock</strong> (low P/E ratio). This combination attracted both growth investors (driven by AI) and value investors (like Buffett), creating a powerful, sustained bullish momentum that shrugged off minor competitive and regulatory risks.</li>
  <li><strong>Resilience to Disruption:</strong> The pattern shows that while new competitors (like ChatGPT Atlas) can cause temporary stock dips, the market quickly reverts to focusing on Alphabet’s core strengths: its massive cash flow, dominant search market, and profitable cloud business, all of which are being successfully fortified by AI.</li>
</ol>

<div class="language-python highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="nf">send_message</span><span class="p">(</span><span class="sh">"""</span><span class="s">How is the outlook for Apple based on trends and news sentiment from July 01 2025 until today? 
Perform the same analysis on all peers by sub-industry. Then compare Apple result to it</span><span class="sh">'</span><span class="s">s peers.</span><span class="sh">"""</span><span class="p">)</span>
</code></pre></div></div>

<p>Here’s an outlook for Apple and its sub-industry peers based on recommendation trends and news sentiment from July 1, 2025, until today, December 1, 2025:</p>

<p><strong>Apple (AAPL) Outlook:</strong></p>

<ul>
  <li><strong>Recommendation Trends:</strong> As of December 1, 2025, Apple has a generally positive outlook from analysts, with 15 “Strong Buy” and 23 “Buy” recommendations, compared to 16 “Hold” and 2 “Sell” recommendations.</li>
  <li><strong>News Sentiment (July 1, 2025 - December 1, 2025):</strong>
    <ul>
      <li><strong>Positive:</strong> News highlights Apple’s strong iPhone sales, particularly the iPhone 17 series, and the continued growth of its high-margin services segment. Strategic investments in AI (including partnerships with Google for Siri and MP Materials for rare earth magnets) and manufacturing diversification to India are seen as positive moves to mitigate risks and drive future growth. FDA approval for hypertension alerts on Apple Watch also contributes to a positive health tech narrative. Warren Buffett’s continued, albeit sometimes trimmed, investment in Apple is also noted positively.</li>
      <li><strong>Neutral:</strong> Several articles discuss Apple’s stock trading near 52-week highs, prompting questions about its valuation and the pace of its AI strategy compared to competitors. Warren Buffett’s trimming of his stake is viewed as a strategic portfolio adjustment rather than a negative signal about the company itself.</li>
      <li><strong>Negative:</strong> Recurring themes include Apple’s perceived lag in AI innovation compared to other tech giants, slower revenue growth in some areas, and ongoing regulatory pressures (antitrust lawsuits in India and the EU, and class-action lawsuits regarding Siri’s AI capabilities). Some analysts predict that competitors with stronger AI strategies might surpass Apple’s market capitalization.</li>
    </ul>
  </li>
</ul>

<p><strong>Apple’s Sub-Industry Peers Outlook:</strong></p>

<p>Apple’s sub-industry peers include companies involved in computer hardware, storage, and quantum computing. Here’s a summary of their outlooks:</p>

<ul>
  <li><strong>Dell Technologies (DELL):</strong>
    <ul>
      <li><strong>Recommendation Trends:</strong> Very positive, with 8 “Strong Buy” and 16 “Buy” recommendations.</li>
      <li><strong>News Sentiment:</strong> Highly positive, driven by strong demand for AI servers, record AI server shipments, optimistic fiscal 2026 guidance, and strategic partnerships with Nvidia and Broadcom. Dell is seen as an undervalued AI infrastructure play, though some analysts note potential margin pressures from rising memory costs.</li>
    </ul>
  </li>
  <li><strong>Western Digital (WDC):</strong>
    <ul>
      <li><strong>Recommendation Trends:</strong> Very positive, with 6 “Strong Buy” and 19 “Buy” recommendations.</li>
      <li><strong>News Sentiment:</strong> Highly positive, recognized as a top S&amp;P 500 performer in 2025 with significant stock returns and dividend increases. Strong demand for data storage from AI companies and expansion of its System Integration and Test (SIT) Lab for AI are key drivers.</li>
    </ul>
  </li>
  <li><strong>Hewlett Packard Enterprise (HPE):</strong>
    <ul>
      <li><strong>Recommendation Trends:</strong> More balanced, with 6 “Strong Buy” and 7 “Buy” recommendations, alongside 13 “Hold.”</li>
      <li><strong>News Sentiment:</strong> Positive, following the successful $14 billion acquisition of Juniper Networks, which is expected to double its networking business and provide AI networking solutions. Collaborations on 5G and sovereign AI supercomputers are also positive. However, strategic restructuring costs have impacted profit margins.</li>
    </ul>
  </li>
  <li><strong>Pure Storage Inc - Class A (PSTG):</strong>
    <ul>
      <li><strong>Recommendation Trends:</strong> Positive, with 7 “Strong Buy” and 13 “Buy” recommendations.</li>
      <li><strong>News Sentiment:</strong> Positive, outperforming Nvidia in 2025 with strong annual recurring revenue growth and key clients in the AI sector.</li>
    </ul>
  </li>
  <li><strong>HP Inc (HPQ):</strong>
    <ul>
      <li><strong>Recommendation Trends:</strong> More negative/hold, with 1 “Strong Buy” and 1 “Buy” against 16 “Hold” and 6 “Sell.”</li>
      <li><strong>News Sentiment:</strong> Mixed. While there are positive developments in AI-powered gaming hardware and sustainable products, the company has faced workforce reductions and missed revenue forecasts.</li>
    </ul>
  </li>
  <li><strong>NetApp Inc (NTAP):</strong>
    <ul>
      <li><strong>Recommendation Trends:</strong> More balanced, leaning towards “Hold,” with 3 “Strong Buy” and 10 “Buy” recommendations, and 14 “Hold.”</li>
      <li><strong>News Sentiment:</strong> Positive, aligning with Broadcom’s quantum-safe SAN switch portfolio and focusing on infrastructure modernization and data protection.</li>
    </ul>
  </li>
  <li><strong>Super Micro Computer Inc (SMCI):</strong>
    <ul>
      <li><strong>Recommendation Trends:</strong> Mixed to positive, with 4 “Strong Buy” and 10 “Buy” recommendations, but also 9 “Hold” and 3 “Sell.”</li>
      <li><strong>News Sentiment:</strong> Mixed. Positive sentiment stems from launching Nvidia Blackwell Ultra solutions, strong AI order backlogs, and institutional interest. However, negative sentiment arises from missing revenue expectations, stock declines due to weak guidance, and past fraud allegations.</li>
    </ul>
  </li>
  <li><strong>IonQ Inc (IONQ):</strong>
    <ul>
      <li><strong>Recommendation Trends:</strong> Positive, with 2 “Strong Buy” and 10 “Buy” recommendations.</li>
      <li><strong>News Sentiment:</strong> Highly speculative. While showing strong revenue growth and strategic acquisitions in quantum computing, it faces high valuations, significant net losses, and is considered a risky investment. Amazon notably sold its entire stake.</li>
    </ul>
  </li>
  <li><strong>Quantum Computing Inc (QUBT):</strong>
    <ul>
      <li><strong>Recommendation Trends:</strong> Positive, with 2 “Strong Buy” and 5 “Buy” recommendations.</li>
      <li><strong>News Sentiment:</strong> Highly speculative. Despite strong Q3 earnings and a substantial capital raise, the company has minimal sales, high operating expenses, and an expensive valuation. It’s considered a high-risk investment.</li>
    </ul>
  </li>
  <li><strong>CompoSecure Inc-A (CMPO):</strong>
    <ul>
      <li><strong>Recommendation Trends:</strong> Positive, with 2 “Strong Buy” and 8 “Buy” recommendations.</li>
      <li><strong>News Sentiment:</strong> Positive, with plans for a business combination and ongoing management fee generation.</li>
    </ul>
  </li>
</ul>

<p><strong>Comparison of Apple to its Peers:</strong></p>

<ul>
  <li><strong>AI Leadership:</strong> Many of Apple’s peers, particularly Dell, Western Digital, Pure Storage, and Super Micro Computer, are seen as directly benefiting from and leading in the AI infrastructure and data storage boom. Apple, while making AI investments and partnerships, is often perceived as lagging in groundbreaking AI innovation compared to these specialized AI-focused companies.</li>
  <li><strong>Growth Drivers:</strong> Apple’s growth is primarily driven by its established iPhone ecosystem and expanding services. Its peers are seeing significant growth from the broader AI revolution, data center expansion, and specialized technological advancements in areas like quantum computing and rare earth materials.</li>
  <li><strong>Valuation &amp; Risk:</strong> Apple’s valuation is a point of discussion, with some analysts questioning if it’s justified given its slower AI progress. While some peers like Dell and Pure Storage are seen as undervalued, the quantum computing pure-plays (IonQ, QUBT) carry extremely high valuations and significant speculative risk, making them much riskier investments than Apple.</li>
  <li><strong>Analyst Sentiment:</strong> While Apple generally has a positive analyst sentiment, some of its peers, particularly Western Digital and Dell, show even stronger “Buy” recommendations, reflecting their more direct and impactful involvement in the current AI-driven market surge.</li>
</ul>

<p><strong>Overall Conclusion:</strong></p>

<p>Apple’s outlook is stable and positive, supported by its strong brand, loyal customer base, and growing services revenue. It is actively working to integrate AI into its ecosystem and diversify its manufacturing. However, it is currently perceived as playing catch-up in the AI race compared to some of its peers who are directly building the foundational AI infrastructure.</p>

<p>Many of Apple’s peers, especially those in AI hardware and data storage, are experiencing more explosive growth and stronger positive sentiment due to the immense demand for AI technologies. The quantum computing peers, while highly speculative, represent a high-risk, high-reward segment of the tech industry.</p>

<p>In essence, Apple is a robust and profitable company with a solid future, but its growth trajectory is currently more measured compared to the rapid expansion seen in some of its more specialized, AI-centric peers.</p>

<div class="language-python highlighter-rouge"><div class="highlight"><pre class="highlight"><code><span class="nf">send_message</span><span class="p">(</span><span class="sh">"""</span><span class="s">What does the recent news say about Apple and the impact of tariffs? From 2025-09-01 up to today. 
Also locate candlestick data for the same dates. 
Discuss in detail any correlations in patterns between the candlestick and news data. Ignore duplicate news entry.</span><span class="sh">"""</span><span class="p">)</span>
</code></pre></div></div>

<p>From September 1, 2025, to December 1, 2025, Apple’s stock (AAPL) experienced a general upward trend, with some periods of volatility. The news during this period highlighted several factors, including the impact of tariffs, which showed a correlation with the stock’s movements.</p>

<p><strong>Impact of Tariffs:</strong></p>

<ul>
  <li><strong>Negative Correlation:</strong> News directly related to President Trump’s tariff threats and Apple’s reported tariff-related cost increases often coincided with periods of stock price decline or stagnation. For instance, on <strong>October 10, 2025</strong>, news broke about “Trump Shocks Markets: VIX Spikes 25%, S&amp;P 500 Eyes Worst Day Since April,” explicitly stating that Apple experienced a significant stock price decline due to renewed tariff threats against China. Similarly, on <strong>November 18, 2025</strong>, “The Stock Market Flashes a Warning as Investors Get Bad News About President Trump’s Tariffs” reported Apple facing $1.1 billion in tariff-related cost increases, which could have contributed to downward pressure. On <strong>October 26, 2025</strong>, an article titled “Is Apple Going to Be Hit Hard by President Trump’s Tariffs?” highlighted potential significant challenges from US-China trade tensions and rare earth element export restrictions.</li>
  <li><strong>Positive/Mitigating Correlation:</strong> Conversely, news detailing Apple’s strategies to mitigate tariff impacts was often met with positive or neutral sentiment, potentially cushioning negative market reactions. For example, on <strong>October 28, 2025</strong>, “Top 3 Stocks Powering Through Trump’s Tariff Policies” noted that Apple successfully avoided arduous tariffs through strategic U.S. investments, relocated iPhone production, and achieved exemptions. This positive news could have contributed to a stock recovery after earlier tariff-related dips. Furthermore, Apple’s strategic investments in rare earth materials, such as the $500 million investment in MP Materials for recycling facility development (reported on <strong>October 31, 2025</strong>, and <strong>September 4, 6, 12, 30, November 2, 15, 17, 19, 26, 29, 30, December 1</strong>), were seen as proactive measures to address supply chain risks stemming from China’s export controls, which likely instilled investor confidence. The news on <strong>September 17, 2025</strong>, about Apple investing in Vietnam for supply chain diversification also falls into this category.</li>
</ul>

<p><strong>Other Significant News and Candlestick Correlations:</strong></p>

<ul>
  <li><strong>Early September (around $225-$245):</strong> The stock showed an upward trend, coinciding with several positive news items. Notably, favorable Google antitrust rulings (reported on <strong>September 3, 4, 5, 7, 8, 9, 11, 12</strong>) preserved Apple’s significant annual revenue from Google, providing a strong positive impetus. News about Apple’s AI future and strategic investments also contributed to this positive sentiment.</li>
  <li><strong>Mid-September to Early October (fluctuating in $245-$260):</strong> This period saw mixed news. While some reports indicated an “underwhelming” iPhone 17 launch (<strong>September 12, 14, 15</strong>) and concerns about Apple’s AI progress (<strong>September 28, October 8</strong>), positive news about strong iPhone 17 pre-order demand in China (<strong>September 22</strong>) and positive analyst upgrades (<strong>October 2</strong>) helped to balance the sentiment, leading to fluctuating but generally stable prices.</li>
  <li><strong>Mid-October to Early November (fluctuating in $255-$275):</strong> This period included the negative tariff news mentioned above, which likely caused some dips. However, positive news about strong iPhone 17 sales (<strong>October 23, 24, 30</strong>) and Apple being a top holding in various ETFs (<strong>October 14, 19, 22, 25, 27, 28, 29, 30, 31, November 2, 3, 4, 5, 8, 10, 11, 12, 14, 17, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, December 1</strong>) indicated continued investor confidence.</li>
  <li><strong>Late November to December 1 (upward trend towards $277-$279):</strong> The stock showed a strong upward movement. This aligns with continued positive news regarding strong iPhone sales (<strong>November 25, 28</strong>), strategic partnerships, and Apple being a significant holding in various investment funds. Despite some negative news like new antitrust lawsuits in India and a class-action lawsuit over AI training (<strong>November 27, 14</strong>), the overall positive sentiment from product demand and strategic positioning seemed to drive the stock higher.</li>
</ul>

<p><strong>In conclusion:</strong> Apple’s stock performance during this period was a complex interplay of various factors. While tariff-related news introduced volatility and sometimes downward pressure, Apple’s proactive strategies to mitigate these risks, coupled with strong iPhone sales, favorable legal outcomes (like the Google antitrust case), and ongoing AI investments, generally contributed to a positive overall trend in its stock price. The candlestick data reflects these shifts in market sentiment, with dips often correlating with negative news and rallies aligning with positive developments.</p>

{% include nav-footer.html %}
