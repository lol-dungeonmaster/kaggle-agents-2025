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

    Note: you may need to restart the kernel to use updated packages.
    Note: you may need to restart the kernel to use updated packages.

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

    KeyError: authentication token for LMNR_PROJECT_API_KEY is undefined
    Skipping Laminar.initialize()

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

### Set Gemini API Limit

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

# __StockChat: Agents Edition__

It was during Kaggle's 5-day Generative AI course in 2025 that StockChat first existed as a simple search-connected LLM. There were two observations from that initial build. First being the need for a real-time source of grounding truth. Even with google-search data was more often incomplete. The second observation, which still exists today, is the tendency toward hallucinations in finance data. Ticker symbols can imitate the name of another company, and it also possible for the LLM to confuse a company name for a wrong symbol. This happens even when the context of the question matches the immediate discussion history and should be self-evident.

```python
response = chat.send_message('''What is MGM Studio's stock ticker symbol?''')
Markdown(response.text)
```

```
... (possibly useful content, often not)

It is important not to confuse MGM Studios with MGM Resorts International, which is a separate, publicly traded hospitality and casino entertainment company with the stock ticker symbol MGM on the New York Stock Exchange (NYSE).
```

Gemini is naturally chatty in a helpful way and this sometimes causes it to go off-topic. The inclusion of off-topic discussion requires that all output from the LLM be checked for topic deviations. Otherwise a backing RAG may store incorrect truths. It became a trade-off between restraining gemini output, and it's usefulness, versus unrestrained with the hallucination caveat. So google-search was not the solution, and actually it was kind-of off-putting as a source of finance chat. Thus StockChat transformed into a huge monolithic agent with access to multiple finance api's, and wikipedia/search to back it up.

```python
send_message("What is MGM Studio's stock symbol?")
```

```
MGM Studios (Metro-Goldwyn-Mayer Studios, Inc.) is a wholly-owned subsidiary of Amazon and is not publicly traded, so it does not have its own stock symbol.

The stock symbol for its parent company, Amazon, is AMZN.
```

While big and capable, StockChat (SC1) became limited by it's single agent design.
- There's no parallelism or asynchronous operation because parallel function calling is agent-wide. Some of the functions may have unmet dependencies when run parallel (by an LLM). In other cases the degree of parallelism is determined by whether you have paid for finance api access. As I'm building a toy I wanted to keep free-tier as an option. Effectively SC1 is a big LLM-guided loop with serial operations, and a single rest api request at a time. It makes SC1 stable at the cost of performance.
- The lack of context management means it can handle months worth of pre-scored news data. As a synchronous operation.
- There's a single vector store with all acquired data, requiring metadata management to compensate.
- It has no facility to determine user interest. It's a giant cache of previously searched finance data.
- It has no systematic evaluation except to run baseline queries.

With these issues in mind my goal during Kaggle's 5-day Agents course was to apply Google's agentic framework to free SC1 from these limitations.
- SC2 uses async runners while maintaining some minimal thread synchronization on shared data.
- LLM-assisted context compaction runs at regular intervals.
- All the sub-tools have their own vector stores.
- A memory tool stores long-term memories with semantic meaning preserved, and tagged with date of creation.
- A user profile expert is added to extract user attributes for long-term memory.
- Session state keys are used to pass user interest along to other agents.
- A summary writing expert ensures large generations aren't blemished by erratic markdown, currency or timestamp formatting.
- The ADK CLI is used to run an evaluation suite with LLM-as-judge.

## Setup working directory

On Kaggle the working directory for ADK runner's differs from notebook location. To work around this I use git with spare-checkout to pull in SC2's updated source. Then I setup the Kaggle runner environment and define the async runner.

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

    WARNING  [root] KeyError: authentication token for LMNR_PROJECT_API_KEY is undefined
    INFO     [root] Skipping Laminar.initialize()
    INFO     [root] sc2.__init__: the api-helper is ready
    Generate document embedding:   0%|          | 0/1 [00:00<?, ?it/s]
    Generate document embedding: 100%|##########| 1/1 [00:03<00:00,  3.99s/it]
    Generate document embedding: 100%|##########| 1/1 [00:04<00:00,  4.13s/it]
    INFO     [root] sc2.__init__: RestGroundingTool is ready
    INFO     [root] sc2.__init__: SearchGroundingTool is ready
    INFO     [root] sc2.__init__: WikiGroundingTool is ready
    INFO     [root] sc2.__init__: MemoryService is ready
    WARNING  [root] [EXPERIMENTAL] ReflectAndRetryToolPlugin: This feature is experimental and may change or be removed in future versions without notice. It may introduce breaking changes at any time.
      plugins=[ReflectAndRetryToolPlugin(max_retries=1)],
    WARNING  [root] [EXPERIMENTAL] EventsCompactionConfig: This feature is experimental and may change or be removed in future versions without notice. It may introduce breaking changes at any time.
      events_compaction_config=EventsCompactionConfig(


## Test the Runner

The initial two-questions are used to test the agents self-awareness of tools. This was particularly problematic for the parallel `fncall_pipeline`. The goal is to have a parallel operating planner and executor of function calls. The function tool definition are tricky to access reliably when nested inside workflow agents like the ParallelAgent. In the end I exposed the planner and it's containing pipeline, then told Gemini where to look.

My goal is ultimately to make SC2 a more capable assistant in addition to removing existing limits. To that end I also added a Terminology expert to make use of the built-in google-search. Meanwhile a user profile expert dynamically extracts preferences and user attributes. These two types of data are stored in long-term memory.


```python
# Create a session service and run some test queries.
s_svc = InMemorySessionService()

await run_queries(
    app=app, sessions=s_svc,
    queries=[
        "What tools do you know how to use?",
        "Tell me what functions `fncall_pipeline` knows by checking `sc2_fnplan`.",
        "What is a short trade?",
        "What is gambler's ruin?",
        "My local advisor is SC at JPMorgan Chase, 212-736-2001",
        "I live in Brooklyn, New York."])
```

    INFO     [root] ### Agent session: (uid=default) default
    
    INFO     [root] USER  > What tools do you know how to use?
    INFO     [root] MODEL > I can use the following tools:
    
    *   `sc2_memory`: An expert writer of long-term memories.
    *   `sc2_prefs`: An expert profile analyst in the field of finance, money, and stock markets.
    *   `fncall_pipeline`: A function caller with functions defined in sub-agent `sc2_fnplan`.
    *   `sc2_fnplan`: A highly intelligent FunctionTool call planner.
    *   `sc2_terms`: An expert terminologist in the field of finance, money, and stock markets.
    *   `sc2_summary`: An expert proof-reader and writer that knows HTML, JSON and Markdown.
    
    INFO     [root] USER  > Tell me what functions `fncall_pipeline` knows by checking `sc2_fnplan`.
    INFO     [root] MODEL > `fncall_pipeline` knows the following functions:
    
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
    
    Generate memory embedding (Short Trade):   0%|          | 0/1 [00:00<?, ?it/s]
    Generate memory embedding (Short Trade): 100%|##########| 1/1 [00:00<00:00,  1.47it/s]
    Generate memory embedding (Short Trade): 100%|##########| 1/1 [00:00<00:00,  1.40it/s]
    INFO     [root] USER  > What is a short trade?
    INFO     [root] MODEL > A short trade, also known as short selling, is a speculative strategy where an investor sells borrowed securities with the expectation of repurchasing them at a lower price. The objective is to profit from a decrease in the security's price. If the price declines, the investor can buy the shares at a reduced cost, return them to the lender, and gain the difference. Conversely, if the price increases, the investor must buy them back at a higher price, resulting in a loss.
    
    Generate memory embedding (Gambler's ruin):   0%|          | 0/1 [00:00<?, ?it/s]
    Generate memory embedding (Gambler's ruin): 100%|##########| 1/1 [00:00<00:00,  1.25it/s]
    Generate memory embedding (Gambler's ruin): 100%|##########| 1/1 [00:00<00:00,  1.20it/s]
    INFO     [root] USER  > What is gambler's ruin?
    INFO     [root] MODEL > Gambler's Ruin
    
    Gambler's ruin is a concept within probability theory. It posits that a gambler possessing a finite sum of money, engaging in a game against an opponent with an effectively infinite amount of money, will inevitably deplete their entire funds. This outcome holds true regardless of whether the game is fair or if the odds are even slightly in the gambler's favor.
    
    
    Generate memory embedding (local advisor):   0%|          | 0/1 [00:00<?, ?it/s]
    Generate memory embedding (local advisor): 100%|##########| 1/1 [00:00<00:00,  1.82it/s]
    Generate memory embedding (local advisor): 100%|##########| 1/1 [00:00<00:00,  1.72it/s]
    INFO     [root] USER  > My local advisor is SC at JPMorgan Chase, 212-736-2001
    INFO     [root] MODEL > I've noted that your local advisor is SC at JPMorgan Chase, phone number 212-736-2001.
    
    Generate memory embedding (User's residence):   0%|          | 0/1 [00:00<?, ?it/s]
    Generate memory embedding (User's residence): 100%|##########| 1/1 [00:01<00:00,  1.62s/it]
    Generate memory embedding (User's residence): 100%|##########| 1/1 [00:01<00:00,  1.65s/it]
    INFO     [root] USER  > I live in Brooklyn, New York.
    INFO     [root] MODEL > Okay, I've noted that you live in Brooklyn, New York.
    


## Test Long-term Memory

Testing long-term memory is as easy as creating a new `BaseSessionService`. As this Memory is a custom implementation it must be specified as a tool during user query.


```python
# Use long-term memory from a new session.
s_svc2 = InMemorySessionService()

await run_queries(
    app=app, sessions=s_svc2,
    queries=[
        "Check memory for where I live.",
        "Check memory for my local advisor SCs phone number."])
```

    INFO     [root] ### Agent session: (uid=default) default
    
    INFO     [root] Api.refill_rpm 10
    INFO     [root] USER  > Check memory for where I live.
    INFO     [root] MODEL > You live in Brooklyn, New York.
    
    INFO     [root] USER  > Check memory for my local advisor SCs phone number.
    INFO     [root] MODEL > SC's phone number is 212-736-2001.
    


## Check for compaction

One of the features of SC2 that I'm looking forward to working with more is the LLM-assisted context compaction. In this implementation I've opted for zero-overlap to avoid re-summarizing past events. At this point no events are dropped from the context. The LLM is known to become confused with statement repetition, so let's avoid that complication. A delightful feature of LLM-compaction is the use of an LLM-as-judge to assess the summary quality with impartiality. It'll note neat things for you like when the tools fail completely or when parts of a user query remain unanswered.


```python
# Display context compaction output.
await check_compaction(s_svc, show_llm=True)
```

    INFO     [root] check_compaction.show_llm: The user initiated the conversation by asking about the AI's available tools. The AI listed its tools, including `sc2_memory`, `sc2_prefs`, `fncall_pipeline`, `sc2_fnplan`, `sc2_terms`, and `sc2_summary`, along with their brief descriptions.
    
    Next, the user asked the AI to specify the functions available through `fncall_pipeline` by checking `sc2_fnplan`. The AI responded by listing 20 specific functions, predominantly related to financial data retrieval (e.g., `get_symbol_1`, `get_market_status_1`, `get_financials_1`, `get_news_with_sentiment_2`).
    
    Finally, the user asked for a definition of "short trade." The AI provided a clear explanation, describing it as a speculative strategy where an investor sells borrowed securities with the expectation of repurchasing them at a lower price to profit from a price decrease.
    
    **Key information and decisions made:**
    *   The AI disclosed its capabilities in terms of tools and specific functions.
    *   The AI provided a detailed definition of a financial term requested by the user.
    
    **Unresolved questions or tasks:**
    *   There are no explicit unresolved questions or tasks at the end of this conversation segment.
    
    INFO     [root] check_compaction.show_llm: The conversation began with the user asking for a definition of "gambler's ruin," which the AI successfully provided. Subsequently, the user volunteered two pieces of personal information: their local advisor (SC at JPMorgan Chase, 212-736-2001) and their residence (Brooklyn, New York). The AI acknowledged and noted both details.
    
    **Key Information & Decisions:**
    *   **Definition Provided:** The AI explained "gambler's ruin."
    *   **Advisor Details Noted:** The AI recorded the user's advisor (SC, JPMorgan Chase, 212-736-2001).
    *   **Residence Noted:** The AI recorded the user's residence (Brooklyn, New York).
    
    **Unresolved Questions or Tasks:**
    There are no unresolved questions or tasks in this segment of the conversation.
    
    INFO     [root] check_compaction: found (2) compaction event
    


## Evaluation by CLI

In SC1 evaluation didn't happen systematically. As you can see from the appendix evaluation consists of manually checking the model output, or baseline. In leveraging the ADK CLI, SC2 gains an LLM-as-judge to systematically evaluate assistant output. A rubric is applied to check response quality and related tool use. Then a hallucination test is performed to ensure the agent has stayed on-topic.


```python
!adk eval sc2 sc2/eval/test_cases.json --config_file_path=sc2/eval/config.json --print_detailed_results
```

    /home/sysop/Documents/kaggle-agents-2025/.venv/lib/python3.12/site-packages/google/adk/evaluation/metric_evaluator_registry.py:90: UserWarning: [EXPERIMENTAL] MetricEvaluatorRegistry: This feature is experimental and may change or be removed in future versions without notice. It may introduce breaking changes at any time.
      metric_evaluator_registry = MetricEvaluatorRegistry()
    /home/sysop/Documents/kaggle-agents-2025/.venv/lib/python3.12/site-packages/google/adk/evaluation/local_eval_service.py:80: UserWarning: [EXPERIMENTAL] UserSimulatorProvider: This feature is experimental and may change or be removed in future versions without notice. It may introduce breaking changes at any time.
      user_simulator_provider: UserSimulatorProvider = UserSimulatorProvider(),
    Using evaluation criteria: criteria={'rubric_based_final_response_quality_v1': BaseCriterion(threshold=0.8, judge_model_options={'judge_model': 'gemini-2.5-flash', 'num_samples': 1}, rubrics=[{'rubric_id': 'conciseness', 'rubric_content': {'text_property': "The agent's response is direct and to the point."}}, {'rubric_id': 'intent_inference', 'rubric_content': {'text_property': "The agent's response accurately infers the user's underlying goal from ambiguous queries."}}]), 'rubric_based_tool_use_quality_v1': BaseCriterion(threshold=1.0, judge_model_options={'judge_model': 'gemini-2.5-flash', 'num_samples': 1}, rubrics=[{'rubric_id': 'prefs_called', 'rubric_content': {'text_property': 'The agent calls `sc2_prefs` to store profile data when required.'}}, {'rubric_id': 'memory_called_before', 'rubric_content': {'text_property': 'The agent calls `sc2_memory` before `sc2_terms` or `fncall_pipeline`.'}}, {'rubric_id': 'memory_called_after', 'rubric_content': {'text_property': 'The agent calls `sc2_memory` after `sc2_terms` only for new memories.'}}, {'rubric_id': 'summary_called', 'rubric_content': {'text_property': 'The agent calls `sc2_summary` last when used.'}}, {'rubric_id': 'workflow_bypass', 'rubric_content': {'text_property': 'The agent can bypass the workflow for usage related questions.'}}]), 'hallucinations_v1': BaseCriterion(threshold=0.8, judge_model_options={'judge_model': 'gemini-2.5-flash'}, evaluate_intermediate_nl_responses=True)} user_simulator_config=None
    2025-12-01 06:49:13,997 - WARNING - secret.py:13 - KeyError: authentication token for LMNR_PROJECT_API_KEY is undefined
    2025-12-01 06:49:13,998 - INFO - __init__.py:54 - Skipping Laminar.initialize()
    2025-12-01 06:49:14,229 - INFO - __init__.py:64 - sc2.__init__: the api-helper is ready
    Generate document embedding:   0%|          | 0/1 [00:00<?, ?it/s]
    Generate document embedding: 100%|##########| 1/1 [00:03<00:00,  3.71s/it]
    Generate document embedding: 100%|##########| 1/1 [00:03<00:00,  3.80s/it]
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
    client_session: <aiohttp.client.ClientSession object at 0x7b392c0e12b0>
    2025-12-01 06:50:40,922 - ERROR - base_events.py:1821 - Unclosed connector
    connections: ['deque([(<aiohttp.client_proto.ResponseHandler object at 0x7b392aed7410>, 163304.64493107), (<aiohttp.client_proto.ResponseHandler object at 0x7b392aed7230>, 163307.551887757), (<aiohttp.client_proto.ResponseHandler object at 0x7b392aed7890>, 163311.3517091)])']
    connector: <aiohttp.connector.TCPConnector object at 0x7b392c0e1370>
    2025-12-01 06:50:40,924 - ERROR - base_events.py:1821 - Unclosed client session
    client_session: <aiohttp.client.ClientSession object at 0x7b392a7ae420>
    2025-12-01 06:50:40,924 - ERROR - base_events.py:1821 - Unclosed connector
    connections: ['deque([(<aiohttp.client_proto.ResponseHandler object at 0x7b392aed7050>, 163304.441401676)])']
    connector: <aiohttp.connector.TCPConnector object at 0x7b392a7aca70>
    2025-12-01 06:50:40,925 - ERROR - base_events.py:1821 - Unclosed client session
    client_session: <aiohttp.client.ClientSession object at 0x7b3929b58c20>
    2025-12-01 06:50:40,925 - ERROR - base_events.py:1821 - Unclosed connector
    connections: ['deque([(<aiohttp.client_proto.ResponseHandler object at 0x7b392aed7d70>, 163300.374662593), (<aiohttp.client_proto.ResponseHandler object at 0x7b392a760170>, 163301.411946312)])']
    connector: <aiohttp.connector.TCPConnector object at 0x7b3929b58b60>
    2025-12-01 06:50:40,927 - ERROR - base_events.py:1821 - Unclosed client session
    client_session: <aiohttp.client.ClientSession object at 0x7b392a778f50>
    2025-12-01 06:50:40,927 - ERROR - base_events.py:1821 - Unclosed connector
    connections: ['deque([(<aiohttp.client_proto.ResponseHandler object at 0x7b392aed7ef0>, 163299.872841362), (<aiohttp.client_proto.ResponseHandler object at 0x7b392a761130>, 163300.01212217), (<aiohttp.client_proto.ResponseHandler object at 0x7b392a760a10>, 163300.013835746), (<aiohttp.client_proto.ResponseHandler object at 0x7b392a760770>, 163301.746375534)])']
    connector: <aiohttp.connector.TCPConnector object at 0x7b392a778e90>


## Conclusion

In applying Google's ADK to SC1, the result is a more capable SC2 which is ready to grow beyond it's first edition roots. Unresolved issues from SC1 remain. Parallelism will enable large work loads, like a stack of news requiring analysis, or background processes to drive self-improvement. This will enable a better user experience when locally running models are later employed to scale further. With the addition of agentic capabilities StockChat has room to grow again.

__I hope you'll stick around to see how far the project gets! Thanks for taking the time to check out my notebook!__

# __Appendix__

## Gemini Baseline Check


```python
# This is an accurate retelling of events. 
config_with_search = types.GenerateContentConfig(
    tools=[types.Tool(google_search=types.GoogleSearch())],
    temperature=0.0
)

chat = api.args.CLIENT.chats.create(
    model=api(Api.Model.GEN),
    config=config_with_search,
    history=[]) # Ignoring the part about dark elves, and tengwar.

response = chat.send_message('Do you know anything about the stock market?')
Markdown(response.text)
```

The stock market is a global network of exchanges and over-the-counter (OTC) marketplaces where investors buy and sell shares of publicly traded companies. These shares, also known as equities, represent fractional ownership in a company.

**Purpose of the Stock Market**
The stock market serves two primary functions:
*   **For Companies:** It allows companies to raise capital (money) by issuing shares to the public through a process called an Initial Public Offering (IPO). This capital can then be used to fund and expand their businesses.
*   **For Investors:** It provides individuals and institutions with an opportunity to invest in businesses and potentially grow their wealth over time. Investors can profit through dividends (a share of the company's profits) or by selling their shares at a higher price than they bought them for (capital gains).

**How the Stock Market Works**
The stock market operates through two main types of markets:
*   **Primary Market:** This is where new stocks are first issued. When a private company decides to go public, it lists its shares on an exchange through an IPO, selling them directly to investors to raise capital.
*   **Secondary Market:** After the initial issuance, these shares are traded among investors on stock exchanges (like the New York Stock Exchange or Nasdaq). The company is not directly involved in these subsequent transactions.

Stock prices are primarily determined by the forces of supply and demand. If more investors want to buy a stock than sell it, the price tends to rise, and vice versa. This process is known as price discovery.

**Key Components and Participants**
*   **Stock Exchanges:** These are organized and regulated platforms (often virtual) where stocks and other securities are bought and sold.
*   **Brokers:** These are intermediaries who execute buy and sell orders on behalf of investors.
*   **Investors and Traders:** Participants range from individual retail investors to large institutional investors like pension funds, mutual funds, insurance companies, and hedge funds.

**Types of Investments in the Stock Market**
Beyond just common stocks, the stock market offers various investment instruments:
*   **Stocks (Equities):**
    *   **Common Stock:** Represents partial ownership, gives voting rights on corporate decisions, and offers potential for higher returns, but also higher risk.
    *   **Preferred Stock:** Typically offers fixed dividend payments before common stockholders receive theirs, but usually does not come with voting rights.
    *   **Categorized by Market Capitalization:** Large-cap (companies with market capitalization of $10 billion or more, generally stable), Mid-cap ($2 billion to $10 billion), and Small-cap (less than $2 billion, higher growth potential but riskier).
    *   **Categorized by Investment Style:** Growth stocks (companies with strong potential for rapid growth), Value stocks (undervalued companies that investors believe will rise in price), and Income stocks (companies that pay regular, often higher-than-average, dividends).
*   **Bonds:** These are debt securities where investors essentially lend money to governments or corporations for a set period, receiving regular interest payments.
*   **Mutual Funds:** These pool money from many investors to invest in a diversified portfolio of stocks, bonds, or other securities, managed by a professional fund manager.
*   **Exchange-Traded Funds (ETFs):** Similar to mutual funds, but they trade like individual stocks on exchanges throughout the day.
*   **Derivatives:** Complex financial instruments whose value is derived from an underlying asset, such as stocks. These are generally considered high-risk and not recommended for beginners.

**Factors Influencing Stock Prices**
Stock market movements are influenced by a variety of factors, including company performance (earnings reports, product launches), macroeconomic indicators (interest rates, inflation, GDP growth), political events, international trade policies, and overall investor sentiment.

```python
response = chat.send_message('I have an interest in AMZN stock')
Markdown(response.text)
```
Amazon.com Inc. (NASDAQ: AMZN) is a widely followed stock, known for its dominant presence in e-commerce, cloud computing (Amazon Web Services - AWS), and digital advertising.

Here's a snapshot of AMZN stock as of December 1, 2025:

**Current Price and Performance:**
*   The current price of AMZN stock is approximately $233.22 USD.
*   It has seen a 1.77% increase in the past 24 hours.
*   Over the past week, AMZN stock has risen by 7.80%, and over the last year, it has shown a 12.68% increase.
*   The stock's 52-week high is $258.60 and its 52-week low is $161.38.

**Key Financials and Metrics:**
*   Amazon's market capitalization is approximately $2.49 trillion.
*   The company's Price-to-Earnings (P/E) ratio is around 32.95.
*   Amazon does not currently pay dividends to shareholders, as it reinvests earnings into growth areas.
*   AMZN stock has a beta coefficient of 1.41, indicating its volatility.

**Analyst Outlook:**
*   The overall consensus from 34 analysts over the last three months is a "Strong Buy" for AMZN.
*   The average price target for Amazon.com Inc. is around $298.13, with a maximum estimate of $360.00 and a minimum estimate of $250.00. Oppenheimer recently raised its price target to $305.00 from $290.00, maintaining an "Outperform" rating.

**Business Segments and Growth Drivers:**
*   Amazon's revenue primarily comes from its retail operations (approximately 74%), followed by Amazon Web Services (AWS) (17%), and advertising services (9%).
*   AWS is a significant growth driver, with its revenue growing by 20.2% year-over-year in the third quarter of 2025 and a reported $200 billion backlog.
*   The company continues to expand in areas such as artificial intelligence (AI), cloud computing, global e-commerce, streaming, and logistics automation.

**Recent News and Influencing Factors:**
*   Amazon Web Services recently launched a new multicloud service to enhance data movement with Google Cloud, following an outage in October that caused significant losses for U.S. companies.
*   Amazon is participating in a $400 billion investment in AI by 2025, which is expected to significantly impact the U.S. economy.
*   AI shopping tools, including Amazon's Rufus, are projected to boost traffic to U.S. retail sites by 670% this holiday season compared to last year.
*   Oppenheimer's analysis suggests significant upside potential for AWS through 2027, with plans to double its capacity.
*   Amazon's stock price can be influenced by quarterly earnings, changes in cloud computing demand, consumer spending trends, new business initiatives, and broader economic conditions like inflation and interest rates.

**Historical Context:**
*   AMZN reached its all-time high on November 2, 2025, with a price of $258.60 USD.
*   The company conducted a 20-for-1 stock split in June 2022 to make shares more accessible to retail investors.

```python
response = chat.send_message('''Tell me about AMZN current share price, short-term trends, and bullish versus bearish predictions''')
Markdown(response.text)
```
Amazon.com Inc. (NASDAQ: AMZN) is currently trading at approximately $233.22 USD as of December 1, 2025. The stock has shown an increase of 1.77% in the past 24 hours, a 7.80% rise over the last week, and a 0.67% increase over the past month. Over the last year, AMZN has seen a 12.68% increase. The stock's 52-week high is $258.60, and its 52-week low is $161.38.

**Short-Term Trends**

In the short term, AMZN stock is exhibiting signs of strength. It has risen by 7.39% since a pivot bottom point on Thursday, November 20, 2025, with further increases indicated until a new top pivot is found. The stock holds buy signals from both short and long-term Moving Averages, suggesting a positive forecast. Technical analysis indicates that AMZN is breaking out above a horizontal support zone and shows enough bullish momentum for a break-in above its ascending Fibonacci Retracement Fan. The Bull Bear Power Indicator has also turned bullish with an ascending trendline, and average bullish trading volumes have been higher than bearish trading volumes over the past week.

However, some short-term forecasts suggest potential minor fluctuations. One prediction indicates that the value of AMZN shares could drop by -2.60% to $227.12 per share by December 30, 2025. Another short-term forecast suggests a slight decrease to $230.68 by December 2, 2025, and $229.65 by December 3, 2025, before potentially rising to $233.80 by December 5, 2025. Despite these minor predicted dips, the overall sentiment based on technical indicators is bullish.

**Bullish Versus Bearish Predictions**

The overwhelming sentiment from analysts regarding AMZN stock is bullish. A consensus of 43 analysts over the last three months rates AMZN as a "Strong Buy," with 41 assigning a "Buy" rating and two a "Hold" rating. The average price target from 44 Wall Street analysts for the next 12 months is around $295.23, representing a potential upside of 28.83% from the current price, with a high forecast of $340.00 and a low forecast of $250.00. Other analyst targets range from an average of $282.48 to $298.13, all suggesting significant upside potential.

Key drivers for these bullish predictions include:
*   **Accelerated AWS Growth:** Amazon Web Services (AWS) revenue accelerated to 20.2% year-over-year growth in the third quarter of 2025, up from 17.5% in the second quarter. AWS also has a reported $200 billion backlog. Analysts project AWS revenue to reach $128.1 billion in 2025, growing to $348.5 billion in 2030.
*   **AI Demand:** Amazon is well-positioned amid surging AI demand and cloud infrastructure growth. The company's recent multi-year deal with OpenAI, involving a $38 billion commitment for OpenAI to leverage AWS compute, further highlights its role in the AI space. AWS's Trainium chips business is also experiencing rapid growth.
*   **E-commerce and Advertising:** Amazon's retail operations continue to be a primary revenue source, and its advertising business is expected to continue outperforming expectations.
*   **Warehouse Automation:** Robotics deployment across fulfillment centers is expected to deliver substantial cost savings and improve fulfillment costs by 20% to 40%.

While the overall outlook is strongly bullish, some potential bearish considerations exist. Concerns about the company's enormous AI capital expenditures remain. Additionally, while AWS growth is strong, it may not be as fast as competing cloud services like Microsoft Azure and Google Cloud, posing a risk of market share losses before 2030 if Amazon cannot maintain its competitive edge. Some short-term technical indicators have also shown a "general sell signal" from the relation between long-term and short-term moving averages, where the long-term average is above the short-term average. However, this is largely overshadowed by other positive signals.

```python
response = chat.send_message('''What is mgm studio's stock ticker symbol?''')
Markdown(response.text)
```
MGM Studios, as an independent entity, does not have a publicly traded stock ticker symbol. MGM Holdings, the parent company of MGM Studios, was acquired by Amazon in 2022. Therefore, MGM Studios is now part of Amazon, and its financial performance is reflected within Amazon's overall operations (NASDAQ: AMZN).

However, there is a publicly traded company called **MGM Resorts International**, which operates casinos and resorts and uses the stock ticker symbol **MGM** on the New York Stock Exchange (NYSE). This company is distinct from the film and television studio.

```python
response = chat.send_message('''What was the last open,close,high,low data for AMZN again?''')
Markdown(response.text)
```
As of Friday, November 28, 2025, the last recorded trading day, Amazon (AMZN) stock had the following data:

*   **Close/Last Price:** $233.22
*   **Open Price:** $231.24
*   **High Price:** $233.28
*   **Low Price:** $230.22

```python
response = chat.send_message('''What is AMZN open,close,high,low data for the past month? 
Present the data with multiple columns for display in markdown.''')
Markdown(response.text)
```
Here is the open, close, high, and low data for Amazon (AMZN) stock for the past month, from October 31, 2025, to November 28, 2025:

| Date         | Open (USD) | Close (USD) | High (USD) | Low (USD) |
| :----------- | :--------- | :---------- | :--------- | :-------- |
| Nov 28, 2025 | $231.24    | $233.22     | $233.28    | $230.22   |
| Nov 26, 2025 | $230.74    | $229.16     | $231.75    | $228.77   |
| Nov 25, 2025 | $226.38    | $229.67     | $230.52    | $223.80   |
| Nov 24, 2025 | $222.56    | $226.28     | $227.33    | $222.27   |
| Nov 21, 2025 | $216.34    | $220.69     | $222.21    | $215.18   |
| Nov 20, 2025 | $227.05    | $217.14     | $227.41    | $216.74   |
| Nov 19, 2025 | $223.74    | $222.69     | $223.74    | $218.52   |
| Nov 18, 2025 | $228.10    | $222.55     | $230.20    | $222.42   |
| Nov 17, 2025 | $233.25    | $232.87     | $234.60    | $229.19   |
| Nov 14, 2025 | $235.06    | $234.69     | $238.73    | $232.89   |
| Nov 13, 2025 | $243.05    | $237.58     | $243.75    | $236.50   |
| Nov 12, 2025 | $250.24    | $244.20     | $250.37    | $243.75   |
| Nov 11, 2025 | $248.41    | $249.10     | $249.75    | $247.23   |
| Nov 10, 2025 | $248.34    | $248.40     | $251.75    | $245.59   |
| Nov 07, 2025 | $242.90    | $244.41     | $244.90    | $238.49   |
| Nov 06, 2025 | $249.16    | $243.04     | $250.38    | $242.17   |
| Nov 05, 2025 | $249.03    | $250.20     | $251.00    | $246.16   |
| Nov 04, 2025 | $250.38    | $249.32     | $257.01    | $248.66   |
| Nov 03, 2025 | $255.36    | $254.00     | $258.60    | $252.90   |
| Oct 31, 2025 | $250.10    | $244.22     | $250.50    | $243.98   |
| Oct 30, 2025 | $227.06    | $222.86     | $228.44    | $222.75   |
| Oct 29, 2025 | $231.67    | $230.30     | $231.67    | $228.22   |
| Oct 28, 2025 | $228.22    | $229.25     | $231.49    | $226.21   |
| Oct 27, 2025 | $227.66    | $226.97     | $228.40    | $225.54   |
| Oct 26, 2025 | $221.09    | $224.21     | $224.21    | $221.09   |

Please note that stock market data can fluctuate rapidly, and the prices provided are based on the last available information from the specified dates.

## Previously on Kaggle: StockChat 1.0

### Validation BaseModels


```python
# Validation BaseModels in pydantic schema.
class RestStatus(Enum):
    OK = "OK"
    DELAY = "DELAYED"
    NONE = "NOT_FOUND"
    AUTH = "NOT_AUTHORIZED"

class StopGeneration(BaseModel):
    result: str = Api.Const.Stop()

class RestResultPoly(BaseModel):
    request_id: Optional[str] = None
    count: Optional[int] = None
    next_url: Optional[str] = None
    status: RestStatus  

class MarketSession(Enum):
    PRE = "pre-market"
    REG = "regular"
    POST = "post-market"
    CLOSED = "closed"
    NA = "not applicable"

class MarketEvent(Enum):
    PRE_OPEN = 0
    REG_OPEN = 1
    REG_CLOSE = 2
    POST_CLOSE = 3
    LAST_CLOSE = 4

class AssetClass(Enum):
    STOCKS = "stocks"
    OPTION = "options"
    CRYPTO = "crypto"
    FOREX = "fx"
    INDEX = "indices"
    OTC = "otc"

class SymbolType(Enum):
    COMMON = "Common Stock"
    ETP = "ETP"
    ADR = "ADR"
    REIT = "REIT"
    DELISTED = ""
    CEF = "Closed-End Fund"
    UNIT = "Unit"
    RIGHT = "Right"
    EQUITY = "Equity WRT"
    GDR = "GDR"
    PREF = "Preference"
    CDI = "CDI"
    NVDR = "NVDR"
    REG = "NY Reg Shrs"
    MLP = "MLP"
    MUTUAL = "Mutual Fund"

class Locale(Enum):
    US = "us"
    GLOBAL = "global"

class Sentiment(Enum):
    V_POS = "very positive"
    POSITIVE = "positive"
    NEUTRAL_P = "neutral/positive"
    NEUTRAL_SP = "neutral/slightly positive"
    NEUTRAL = "neutral"
    NEUTRAL_SN = "neutral/slightly negative"
    NEUTRAL_N = "neutral/negative"
    MIXED = "mixed"
    NEGATIVE = "negative"
    V_NEG = "very negative"

class Trend(Enum):
    S_BUY = "strong-buy"
    BUY = "buy"
    HOLD = "hold"
    SELL = "sell"
    S_SELL = "strong-sell"

class MarketCondition(Enum):
    BULL = "bullish"
    BULLN = "cautiously bullish"
    HOLD = "hold"
    BEARN = "cautiously bearish"
    BEAR = "bearish"

class GeneratedEvent(BaseModel):
    last_close: str
    pre_open: str
    reg_open: str
    reg_close: str
    post_close: str
    timestamp: Optional[str] = None
    is_holiday: Optional[bool] = None

    def model_post_init(self, *args, **kwargs) -> None:
        if self.timestamp is None:
            self.timestamp = datetime.now(self.tz()).strftime('%c')
        if self.is_holiday is None:
            self.is_holiday = False

    def session(self, with_date: Optional[str] = None) -> MarketSession:
        if with_date is None:
            with_date = datetime.now(self.tz()).strftime('%c')
        compare = parse(with_date)
        if self.is_holiday or compare.weekday() > 4: # weekend
            return MarketSession.CLOSED
        events = [parse(event).time() for event in [self.pre_open,self.reg_open,self.reg_close,self.post_close]]
        if compare.time() < events[0]:
            return MarketSession.CLOSED
        else:
            session = MarketSession.NA
            if compare.time() >= events[0]:
                session = MarketSession.PRE
            if compare.time() >= events[1]:
                session = MarketSession.REG
            if compare.time() >= events[2]:
                session = MarketSession.POST
            if compare.time() >= events[3]:
                session = MarketSession.CLOSED
        return session

    def is_open(self) -> bool:
        return self.session() != MarketSession.CLOSED

    def has_update(self) -> bool:
        datetime_now = datetime.now(self.tz())
        self_ts = parse(self.timestamp)
        # Re-generate events for a new day.
        if datetime_now.day > self_ts.day:
            return True
        # No updates on holidays or when generated after post_close.
        if self.is_holiday or self_ts.time() >= parse(self.post_close).time():
            return False
        # Compare current time to generated event times.
        for event in [self.pre_open,self.reg_open,self.reg_close]:
            if datetime_now.time() > parse(event).time():
                return True
        # Current time is before pre_open.
        return False

    @classmethod
    def tz(cls):
        return pytz.timezone('US/Eastern') # Exchanges data is in eastern time.
    
    @classmethod
    def apply_fix(cls, value, fix: datetime) -> tuple[str, datetime]:
        api.validation_fail()
        value = fix.strftime('%c')
        return value, fix
    
    @field_validator("last_close")
    def valid_close(cls, value):
        date_gen = parse(value) # Generated close is in eastern time and tzinfo naive.
        date_now = parse(datetime.now(cls.tz()).strftime('%c')) # Need now in same format as generated.
        # Soft-pass: when actual session is closed after post-market
        if date_now.day == date_gen.day+1 and date_now.weekday() <= 4:
            date_fix = date_gen.replace(day=date_now.day)
            if date_fix.timestamp() < date_now.timestamp():
                value, date_gen = cls.apply_fix(value, date_fix) # soft-pass: use today's close
        # Soft-pass: when actual session is open post-market
        if date_now.day == date_gen.day and date_now.timestamp() < date_gen.timestamp():
            if date_now.weekday() > 0:
                date_fix = date_gen.replace(day=date_now.day-1)
            else:
                date_fix = date_gen.replace(day=date_now.day-3)
            if date_now.timestamp() > date_fix.timestamp():
                value, date_gen = cls.apply_fix(value, date_fix) # soft-pass: use previous close
        if date_now.weekday() == 0 or date_now.weekday() == 1 and date_gen.weekday() <= 4: # 0=monday, 4=friday
            return value # pass: generated thurs/friday on a monday/tues
        elif date_now.weekday() > 0 and date_now.weekday() <= 4 and date_gen.weekday() <= date_now.weekday()-1:
            return value # pass: generated yesterday/prior on a tues-fri
        elif date_now.weekday() > 4 and date_gen.weekday() <= 4:
            return value # pass: generated thurs/friday on a weekend
        elif date_now.day == date_gen.day and date_now.timestamp() > date_gen.timestamp():
            return value # pass: generated today after closed
        elif date_now.timestamp() < date_gen.timestamp():
            raise ValueError("last close cannot be a future value")
        else:
            raise ValueError("generated invalid last close")
        api.validation_fail()

class VectorStoreResult(BaseModel):
    docs: str
    dist: Optional[float] # requires query
    meta: Optional[dict]  # requires get or query
    store_id: str

class Aggregate(RestResultPoly):
    symbol: str
    open: float
    high: float
    low: float
    close: float
    volume: int
    otc: Optional[bool] = None
    preMarket: Optional[float] = None
    afterHours: Optional[float] = None

class DailyCandle(Aggregate):
    from_date: str

class AggregateWindow(BaseModel):
    o: float
    h: float
    l: float
    c: float
    v: int # traded volume
    n: Optional[int] = None # transaction count
    vw: Optional[float] = None # volume weighted average price
    otc: Optional[bool] = None
    t: int

    @field_validator("t")
    def valid_t(cls, value):
        if not value > 0:
            raise ValueError("invalid timestamp")
        if len(str(value)) == 13:
            return int(value/1000)
        return value

class CustomCandle(RestResultPoly): 
    ticker: str
    adjusted: bool
    queryCount: int
    resultsCount: int
    results: list[AggregateWindow]

    def model_post_init(self, *args, **kwargs) -> None:
        self.count = len(self.results)

    def get(self) -> list[AggregateWindow]:
        return self.results
    
class MarketStatus(BaseModel):
    exchange: str
    holiday: Optional[str] = None
    isOpen: bool
    session: Optional[MarketSession] = None
    t: int
    timezone: str

    def model_post_init(self, *args, **kwargs) -> None:
        if self.session is None:
            self.session = MarketSession.CLOSED
        if self.holiday is None:
            self.holiday = MarketSession.NA.value

class MarketStatusResult(BaseModel):
    results: MarketStatus

    def get(self) -> MarketStatus:
        return self.results

class Symbol(BaseModel):
    description: str
    displaySymbol: str
    symbol: str
    type: SymbolType

class SymbolResult(BaseModel):
    count: int
    result: list[Symbol]

    def model_post_init(self, *args, **kwargs) -> None:
        self.count = len(self.result)

    def get(self) -> list[Symbol]:
        return self.result

class Quote(BaseModel):
    c: float
    d: float
    dp: float
    h: float
    l: float
    o: float
    pc: float
    t: int

    @field_validator("t")
    def valid_t(cls, value):
        if not value > 0:
            raise ValueError("invalid timestamp")
        return value

class PeersResult(BaseModel):
    results: list[str]
    count: Optional[int] = None

    def model_post_init(self, *args, **kwargs) -> None:
        self.count = len(self.results)

    def get(self) -> list[str]:
        return self.results

class BasicFinancials(BaseModel):
    metric: dict
    metricType: str
    series: dict
    symbol: str

class Insight(BaseModel):
    sentiment: Sentiment|MarketCondition
    sentiment_reasoning: str
    ticker: str

class Publisher(BaseModel):
    favicon_url: Optional[str]
    homepage_url: str
    logo_url: str
    name: str

class NewsSummary(BaseModel):
    title: str
    summary: Optional[str]
    insights: Optional[list[Insight]]
    published_utc: str

class NewsTypePoly(BaseModel):
    amp_url: Optional[str] = None
    article_url: str
    title: str
    author: str
    description: Optional[str] = None
    id: str
    image_url: Optional[str] = None
    insights: Optional[list[Insight]] = None
    keywords: Optional[list[str]] = None
    published_utc: str
    publisher: Publisher
    tickers: list[str]

    def summary(self):
        return NewsSummary(title=self.title,
                           summary=self.description,
                           insights=self.insights,
                           published_utc=self.published_utc)

class NewsResultPoly(RestResultPoly):
    results: list[NewsTypePoly]

    def model_post_init(self, *args, **kwargs) -> None:
        self.count = len(self.results)

    def get(self) -> list[NewsTypePoly]:
        return self.results

class NewsTypeFinn(BaseModel):
    category: str
    datetime: int
    headline: str
    id: int
    image: str
    related: str # symbol
    source: str
    summary: str
    url: str

    def summary(self):
        return NewsSummary(title=self.headline,
                           summary=self.summary,
                           insights=None,
                           published_utc=self.datetime)

class NewsResultFinn(BaseModel):
    results: list[NewsTypeFinn]
    count: Optional[int] = None

    def model_post_init(self, *args, **kwargs) -> None:
        self.count = len(self.results)

    def get(self) -> list[NewsTypeFinn]:
        return self.results

class NewsTypeGenerated(BaseModel):
    title: str
    summary: str
    insights: list[Insight]
    keywords: list[str]
    source: Publisher
    published_utc: str
    tickers: list[str]
    url: str

    def summary(self):
        return NewsSummary(title=self.title,
                           summary=self.summary,
                           insights=self.insights,
                           published_utc=self.published_utc)

class TickerOverview(BaseModel):
    ticker: str
    name: str
    market: AssetClass
    locale: Locale
    primary_exchange: Optional[str] = None
    active: bool
    currency_name: str
    cik: Optional[str] = None
    composite_figi: Optional[str] = None
    share_class_figi: Optional[str] = None
    market_cap: Optional[int|float] = None
    phone_number: Optional[str] = None
    address: Optional[dict] = None
    description: Optional[str] = None
    sic_code: Optional[str] = None
    sic_description: Optional[str] = None
    ticker_root: Optional[str] = None
    homepage_url: Optional[str] = None
    total_employees: Optional[int] = None
    list_date: Optional[str] = None
    branding: Optional[dict] = None
    share_class_shares_outstanding: Optional[int] = None
    weighted_shares_outstanding: Optional[int] = None
    round_lot: Optional[int] = None

class OverviewResult(RestResultPoly):
    results: TickerOverview

    def get(self) -> TickerOverview:
        return self.results

class RecommendationTrend(BaseModel):
    buy: int
    hold: int
    period: str
    sell: int
    strongBuy: int
    strongSell: int
    symbol: str

class TrendsResult(BaseModel):
    results: list[RecommendationTrend]
    count: Optional[int] = None

    def model_post_init(self, *args, **kwargs) -> None:
        self.count = len(self.results)

    def get(self) -> list[RecommendationTrend]:
        return self.results
```

### Contents Memory


```python
# A contents-memory object.
class Memory:
    def __init__(self):
        self.system = f"""Give a concise, and detailed summary. Use information that you learn from the API responses.
        Use your tools and function calls according to the rules. Convert any all-upper case identifiers
        to proper case in your response. Convert any abbreviated or shortened identifiers to their full forms.
        Convert timestamps according to the rules before including them. Think step by step.
        """
        self.revery = {}
        self.contents = []
        self.prompt = None
        self.summary = None
        self.response = None
    
    def set_prompt(self, prompt):
        self.prompt = f"""
        The current date and time is: {datetime.now(GeneratedEvent.tz()).strftime('%c')}
        
        {prompt}
        """
        self.contents = [types.Content(role="user", parts=[types.Part(text=self.prompt)])]

    def set_reason(self, step):
        # Append the model's reasoning part.
        self.contents.append(types.Content(role="model", parts=[types.Part(thought=True,text=step)]))

    def append_code(self, prompt, code_response_parts):
        subroutine_content = [types.Content(role="user", parts=[types.Part(text=prompt)]),
                              types.Content(role="model", parts=code_response_parts)]
        # Append the model's generated code and execution result.
        self.revery[datetime.now(GeneratedEvent.tz()).strftime('%c')] = { 
            "contents": subroutine_content
        }

    def update_contents(self, function_call, api_response_part):
        # Append the model's function call part.
        self.contents.append(types.Content(role="model", parts=[types.Part(function_call=function_call)])) 
        # Append the api response part.
        self.contents.append(types.Content(role="user", parts=[api_response_part]))

    def set_summary(self, summary):
        self.summary = summary
        self.contents.append(types.Content(role="model", parts=[types.Part(text=summary)]))
        self.revery[datetime.now(GeneratedEvent.tz()).strftime('%c')] = {
            "prompt": self.prompt, 
            "summary": self.summary, 
            "contents": self.contents
        }
        self.contents = []

memory = Memory()
```

### Retrieval-Augmented Generation


```python
# Define tool: retrieval-augmented generation.
# - using Chroma and text-embedding-004 for storage and retrieval
# - using gemini-2.0-flash for augmented generation
class RetrievalAugmentedGenerator:
    chroma_client = chromadb.PersistentClient(path="vector_db")
    config_temp = types.GenerateContentConfig(temperature=0.0)
    exchange_codes: Optional[dict] = None
    exchange_lists: dict = {}
    events: dict = {}
    holidays: dict = {}

    def __init__(self, genai_client, collection_name):
        self.client = genai_client
        self.embed_fn = GeminiEmbedFunction(genai_client)
        self.db = self.chroma_client.get_or_create_collection(
            name=collection_name, 
            embedding_function=self.embed_fn,  # type: ignore
            metadata={"hnsw:space": "cosine"})
        logging.getLogger("chromadb").setLevel(logging.ERROR) # suppress warning on existing id
        self.set_holidays("US", ["09-01-2025","10-13-2025","11-11-2025","11-27-2025","12-25-2025"])
        #self.generated_events("US")

    def set_holidays(self, exchange_code: str, holidays: list):
        self.holidays[exchange_code] = [datetime.strptime(h, "%m-%d-%Y").date() for h in holidays]

    def get_exchange_codes(self, with_query: Optional[str] = None):
        gen = None
        if with_query and with_query not in self.exchange_lists.keys():
            gen = tqdm(total=1, desc="Generate exchange codes with_query")
            data = self.get_exchanges_csv(
                f"""What is the {with_query} exchange code? Return only the exchange codes 
                as a list in string form. Just the list string. 
                Omit all other information or details. Do not chat or use sentences.""").candidates[0].content
            self.exchange_lists[with_query] = ast.literal_eval(data.parts[-1].text)
        elif with_query is None and self.exchange_codes is None:
            gen = tqdm(total=1, desc="Generate exchange codes")
            data = self.get_exchanges_csv(
                """Give me a dictionary in string form. It must contain key:value pairs 
                mapping exchange code to name. Just the dictionary string. 
                Omit all other information or details. Do not chat or use sentences.""").candidates[0].content
            self.exchange_codes = ast.literal_eval(data.parts[-1].text.strip("\\`"))
        if gen:
            gen.update(1)
        return self.exchange_lists[with_query] if with_query else self.exchange_codes

    def get_event_date(self, event_t: str, exchange_code: str, event: MarketEvent):
        current_dt_str = datetime.now(GeneratedEvent.tz()).strftime('%c')
        current_dt = datetime.strptime(current_dt_str, "%a %b %d %H:%M:%S %Y")
        current_t_str = datetime.now(GeneratedEvent.tz()).strftime('%H:%M:%S')
        current_t = datetime.strptime(current_t_str, "%H:%M:%S").time()
        event_time = parse(event_t).time()
        gen_datetime = None
        if event is MarketEvent.LAST_CLOSE:
            last_close_day = current_dt.date() - timedelta(days=0 if current_t > event_time else 1)
            # Loop backwards to find the last valid trading day (not a weekend or holiday).
            while last_close_day.weekday() >= 5 or last_close_day in self.holidays[exchange_code]: # 5 = Sat, 6 = Sun
                last_close_day -= timedelta(days=1)
            # Combine the date and time.
            gen_datetime = datetime.combine(last_close_day, event_time)
        else:
            next_event_day = current_dt.date() + timedelta(days=0 if current_t < event_time else 1)
            # Loop forward to find the next valid trading day (not a weekend or holiday).
            while next_event_day.weekday() >= 5 or next_event_day in self.holidays[exchange_code]: # 5 = Sat, 6 = Sun
                next_event_day += timedelta(days=1)
            # Combine date and time.
            gen_datetime = datetime.combine(next_event_day, event_time)
        # Format the result as requested.
        return gen_datetime.strftime('%a %b %d %X %Y')

    def generate_event(self, exchange_code: str, event: MarketEvent):
        if event is MarketEvent.LAST_CLOSE or event is MarketEvent.POST_CLOSE:
            prompt = f"""What is the closing time including post_market hours."""
        elif event is MarketEvent.PRE_OPEN or event is MarketEvent.REG_OPEN:
            is_pre = "including" if event is MarketEvent.PRE_OPEN else "excluding"
            prompt = f"""What is the opening time {is_pre} pre_market hours."""
        elif event is MarketEvent.REG_CLOSE:
            prompt = f"""What is the closing time excluding post_market hours."""
        prompt = f"""Answer based on your knowledge of exchange operating hours.
            Do not answer in full sentences. Omit all chat and provide the answer only.
            The fields pre_market and post_market both represent extended operating hours.

            The current date and time: {datetime.now(GeneratedEvent.tz()).strftime('%c')}
            
            Consider the {exchange_code} exchange's operating hours.
            {prompt}
            
            Answer with the time in this format: '%H:%M:%S'.
            Omit all other chat and details. Do not use sentences."""
        progress = tqdm(total=1, desc=f"Generate {exchange_code}->{event}")
        response = self.get_exchanges_csv(prompt).candidates[0].content
        try:
            if Api.Const.Stop() in f"{response.parts[-1].text}":
                self.generate_event_failed(progress, exchange_code, event)
            else:
                response = self.get_event_date(response.parts[-1].text, exchange_code, event)
                progress.update(1)
                return response
        except Exception as e:
            self.generate_event_failed(progress, exchange_code, event)

    def generate_event_failed(self, progress: tqdm, exchange_code: str, event: MarketEvent):
        progress.close()
        api.generation_fail()
        time.sleep(api.dt_between)
        return self.generate_event(exchange_code, event)

    def generated_events(self, exchange_code: str) -> GeneratedEvent:
        # Check for an existing GeneratedEvent object having updates.
        if exchange_code in self.events.keys() and self.events[exchange_code].has_update():
            event_obj = self.events[exchange_code]
            event_state = [(event_obj.pre_open, MarketEvent.PRE_OPEN),
                           (event_obj.reg_open, MarketEvent.REG_OPEN),
                           (event_obj.reg_close, MarketEvent.REG_CLOSE),
                           (event_obj.post_close, MarketEvent.POST_CLOSE)]
            # Need now in same format as generated.
            datetime_now = parse(datetime.now(event_obj.tz()).strftime('%c'))
            gen_ts = parse(event_obj.timestamp)
            # Re-generate events when day changes.
            if datetime_now.day > gen_ts.day:
                del self.events[exchange_code]
                return self.generated_events(exchange_code)
            # Update changed events on trading days.
            for e in event_state:
                if datetime_now > parse(e[0]):
                    event_dt = self.generate_event(exchange_code, e[1])
                    match e[1]:
                        case MarketEvent.PRE_OPEN:
                            event_obj.pre_open = event_dt
                        case MarketEvent.REG_OPEN:
                            event_obj.reg_open = event_dt
                        case MarketEvent.REG_CLOSE:
                            event_obj.reg_close = event_dt
                        case MarketEvent.POST_CLOSE:
                            event_obj.post_close = event_dt
            event_obj.timestamp = datetime.now(event_obj.tz()).strftime('%c')
            self.events[exchange_code] = event_obj
        # Generate events for an exchange code not in cache.
        elif exchange_code not in self.events.keys():
            self.events[exchange_code] = GeneratedEvent(
                last_close=self.generate_event(exchange_code, MarketEvent.LAST_CLOSE),
                pre_open=self.generate_event(exchange_code, MarketEvent.PRE_OPEN),
                reg_open=self.generate_event(exchange_code, MarketEvent.REG_OPEN),
                reg_close=self.generate_event(exchange_code, MarketEvent.REG_CLOSE),
                post_close=self.generate_event(exchange_code, MarketEvent.POST_CLOSE),
                is_holiday=datetime.now().date() in self.holidays[exchange_code])
        return self.events[exchange_code]

    def set_holiday_event(self, exchange_code: str):
        self.generated_events(exchange_code).is_holiday = True

    def last_market_close(self, exchange_code: str):
        return self.generated_events(exchange_code).last_close

    def add_documents_list(self, docs: list):
        self.embed_fn.document_mode = True # Switch to document mode.
        ids = list(map(str, range(self.db.count(), self.db.count()+len(docs))))
        metas=[{"source": doc.metadata["source"]} for doc in docs]
        content=[doc.page_content for doc in docs]
        tqdm(self.db.add(ids=ids, documents=content, metadatas=metas), desc="Generate document embedding")

    def add_api_document(self, query: str, api_response: str, topic: str, source: str = "add_api_document"):
        self.embed_fn.document_mode = True # Switch to document mode.
        splitter = RecursiveJsonSplitter(max_chunk_size=Api.Const.ChunkMax())
        docs = splitter.create_documents(texts=[api_response], convert_lists=True)
        ids = list(map(str, range(self.db.count(), self.db.count()+len(docs))))
        content = [json.dumps(doc.page_content) for doc in docs]
        metas = [{"source": source, "topic": topic}]*len(docs)
        tqdm(self.db.add(ids=ids, documents=content, metadatas=metas), desc="Generate api embedding")

    def add_peers_document(self, query: str, names: list, topic: str, source: str, group: str):
        self.embed_fn.document_mode = True # Switch to document mode.
        peers = {"symbol": topic, "peers": names}
        tqdm(self.db.add(ids=str(self.db.count()),
                         documents=[json.dumps(peers)],
                         metadatas=[{"source": source, "topic": topic, "group": group}]),
             desc="Generate peers embedding")

    def get_peers_document(self, query: str, topic: str, group: str):
        return self.get_documents_list(query, where={"$and": [{"group": group}, {"topic": topic}]})

    def add_rest_chunks(self, chunks: list, topic: str, source: str, ids: Optional[list[str]] = None,
                        meta_opt: Optional[list[dict]] = None, is_update: bool = True):
        self.embed_fn.document_mode = True # Switch to document mode
        if ids is None:
            ids = list(map(str, range(self.db.count(), self.db.count()+len(chunks))))
        if isinstance(chunks[0], BaseModel):
            docs = [model.model_dump_json() for model in chunks]
        else:
            docs = [json.dumps(obj) for obj in chunks]
        meta_base = {"source": source, "topic": topic}
        if meta_opt is not None:
            for m in meta_opt:
                m.update(meta_base)
        metas = [meta_base]*len(chunks) if meta_opt is None else meta_opt
        if is_update:
            tqdm(self.db.upsert(ids=ids, documents=docs, metadatas=metas), desc="Upsert chunks embedding")
        else:
            tqdm(self.db.add(ids=ids, documents=docs, metadatas=metas), desc="Add chunks embedding")

    def get_market_status(self, exchange_code: str) -> tuple[list[VectorStoreResult], bool]: # result, has rest update
        self.embed_fn.document_mode = False # Switch to query mode.
        stored = self.stored_result(self.db.get(where={
            "$and": [{"exchange": exchange_code}, {"topic": "market_status"}]}))
        if len(stored) == 0:
            return stored, True
        # Check for a daily market status update.
        status = json.loads(stored[0].docs)
        gen_day = parse(self.generated_events(exchange_code).timestamp).day
        store_day = parse(stored[0].meta['timestamp']).day
        if status["holiday"] != MarketSession.NA.value and gen_day == store_day:
            return stored, False
        elif gen_day > store_day:
            return stored, True
        # Update with generated events to avoid rest api requests.
        status["session"] = self.generated_events(exchange_code).session().value
        status["isOpen"] = self.generated_events(exchange_code).is_open()
        stored[0].docs = json.dumps(status)
        return stored, False

    def get_basic_financials(self, query: str, topic: str, source: str = "get_financials_1"):
        return self.get_documents_list(
            query, max_sources=200, where={"$and": [{"source": source}, {"topic": topic}]})

    def add_quote_document(self, query: str, quote: str, topic: str, timestamp: int, source: str):
        self.embed_fn.document_mode = True # Switch to document mode.
        tqdm(self.db.add(ids=str(self.db.count()), 
                             documents=[quote], 
                             metadatas=[{"source": source, "topic": topic, "timestamp": timestamp}]), 
             desc="Generate quote embedding")

    def get_api_documents(self, query: str, topic: str, source: str = "add_api_document", 
                          meta_opt: Optional[list[dict]] = None):
        where = [{"source": source}, {"topic": topic}]
        if meta_opt is None:
            return self.get_documents_list(query, where={"$and": where})
        else:
            for meta in meta_opt:
                for k,v in meta.items():
                    where.append({k: v})
            return self.get_documents_list(query, where={"$and": where})

    def query_api_documents(self, query: str, topic: str, source: str = "add_api_document"):
        return self.generate_answer(query, where={"$and": [{"source": source}, {"topic": topic}]})

    def add_grounded_document(self, query: str, topic: str, result):
        self.embed_fn.document_mode = True # Switch to document mode.
        chunks = result.candidates[0].grounding_metadata.grounding_chunks
        supports = result.candidates[0].grounding_metadata.grounding_supports
        if supports is not None: # Only add grounded documents which have supports
            grounded_text = [f"{s.segment.text}" for s in supports]
            source = [f"{c.web.title}" for c in chunks]
            score = [f"{s.confidence_scores}" for s in supports]
            tqdm(self.db.add(ids=str(self.db.count()),
                             documents=json.dumps(grounded_text),
                             metadatas=[{"source": ", ".join(source),
                                         "confidence_score": ", ".join(score),
                                         "topic": topic,
                                         "question": query}]),
                 desc="Generate grounding embedding")

    def get_grounding_documents(self, query: str, topic: str):
        self.embed_fn.document_mode = False # Switch to query mode.
        return self.stored_result(self.db.get(where={"$and": [{"question": query}, {"topic": topic}]}))
            
    def add_wiki_documents(self, title: str, wiki_chunks: list):
        self.embed_fn.document_mode = True # Switch to document mode.
        result = self.get_wiki_documents(title)
        if len(result) == 0:
            ids = list(map(str, range(self.db.count(), self.db.count()+len(wiki_chunks))))
            metas=[{"title": title, "source": "add_wiki_documents"}]*len(wiki_chunks)
            tqdm(self.db.add(ids=ids, documents=wiki_chunks, metadatas=metas), desc="Generate wiki embeddings")

    @retry.Retry(
        predicate=is_retriable,
        initial=2.0,
        maximum=64.0,
        multiplier=2.0,
        timeout=600,
    )
    def generate_with_wiki_passages(self, query: str, title: str, passages: list[str]):
        return self.generate_answer(query, where={"title": title}, passages=passages)
    
    def get_wiki_documents(self, title: Optional[str] = None):
        self.embed_fn.document_mode = False # Switch to query mode.
        if title is None:
            return self.stored_result(self.db.get(where={"source": "add_wiki_document"}))
        else:
            return self.stored_result(self.db.get(where={"title": title}))

    @retry.Retry(
        predicate=is_retriable,
        initial=2.0,
        maximum=64.0,
        multiplier=2.0,
        timeout=600,
    )
    def get_documents_list(self, query: str, max_sources: int = 5000, where: Optional[dict] = None):
        self.embed_fn.document_mode = False # Switch to query mode.
        return self.stored_result(
            self.db.query(query_texts=[query], 
                          n_results=max_sources, 
                          where=where), 
            is_query = True)

    @retry.Retry(
        predicate=is_retriable,
        initial=2.0,
        maximum=64.0,
        multiplier=2.0,
        timeout=600,
    )
    def get_exchanges_csv(self, query: str):
        return self.generate_answer(query, max_sources=100, where={"source": "exchanges.csv"})

    @retry.Retry(
        predicate=is_retriable,
        initial=2.0,
        maximum=64.0,
        multiplier=2.0,
        timeout=600,
    )
    def generate_answer(self, query: str, max_sources: int = 10, 
                        where: Optional[dict] = None, passages: Optional[list[str]] = None):
        stored = self.get_documents_list(query, max_sources, where)
        query_oneline = query.replace("\n", " ")
        prompt = f"""You're an expert writer. You understand how to interpret html and markdown. You will accept the
        question below and answer based only on the passages. Never mention the passages in your answers. Be sure to 
        respond in concise sentences. Include all relevant background information when possible. If a passage is not 
        relevant to the answer you must ignore it. If no passage answers the question respond with: I don't know.

        QUESTION: {query_oneline}
        
        """
        # Add the retrieved documents to the prompt.
        stored_docs = [passage.docs for passage in stored]
        for passage in stored_docs if passages is None else stored_docs + passages:
            passage_oneline = passage.replace("\n", " ")
            prompt += f"PASSAGE: {passage_oneline}\n"
        # Generate the response.
        response = api.retriable(
            self.client.models.generate_content,
            model=api(Api.Model.GEN),
            config=self.config_temp,
            contents=prompt)
        # Check for generated code and store in memory.
        content = response.candidates[0].content
        if len(content.parts) > 1 and content.parts[0].executable_code:
            memory.append_code(prompt, content.parts)
        return response

    def stored_result(self, result, is_query: bool = False) -> list[VectorStoreResult]:
        try:
            results = []
            if len(result["documents"]) == 0:
                return results
            if isinstance(result["documents"][0], list):
                for i in range(len(result["documents"][0])):
                    obj = VectorStoreResult(docs=result["documents"][0][i],
                                            dist=result["distances"][0][i] if is_query else None,
                                            meta=result["metadatas"][0][i],
                                            store_id=result["ids"][0][i])
                    results.append(obj)
            else:
                results.append(
                    VectorStoreResult(docs=result["documents"][0],
                                      dist=result["distances"][0] if is_query else None,
                                      meta=result["metadatas"][0],
                                      store_id=result["ids"][0]))
            return results
        except Exception as e:
            raise e
```

### Wiki Grounding


```python
# Define tool: wiki-grounding generation.
# - using gemini-2.0-flash for response generation
# - using a RAG-implementation to store groundings
# - create new groundings by similarity to topic
# - retrieve existing groundings by similarity to topic
class WikiGroundingGenerator:   
    def __init__(self, genai_client, rag_impl):
        self.client = genai_client
        self.rag = rag_impl
        with warnings.catch_warnings():
            warnings.simplefilter("ignore") # suppress beta-warning
            self.splitter = HTMLSemanticPreservingSplitter(
                headers_to_split_on=[("h2", "Main Topic"), ("h3", "Sub Topic")],
                separators=["\n\n", "\n", ". ", "! ", "? "],
                max_chunk_size=Api.Const.ChunkMax(),
                chunk_overlap=50,
                preserve_links=True,
                preserve_images=True,
                preserve_videos=True,
                preserve_audio=True,
                elements_to_preserve=["table", "ul", "ol", "code"],
                denylist_tags=["script", "style", "head"],
                custom_handlers={"code": self.code_handler},
            )

    def generate_answer(self, query: str, topic: str):
        stored = self.rag.get_wiki_documents(topic)
        if len(stored) > 0:
            return self.rag.generate_with_wiki_passages(query, topic, [chunk.docs for chunk in stored]).text
        else:
            pages = wikipedia.search(topic + " company")
            if len(pages) > 0:
                p_topic_match = 0.80
                for i in range(len(pages)):
                    if tqdm(api.similarity([topic + " company", pages[i]]) > p_topic_match, 
                            desc= "Score wiki search by similarity to topic"):
                        page_html = Api.get(f"https://en.wikipedia.org/wiki/{pages[i]}")
                        chunks = [chunk.page_content for chunk in self.splitter.split_text(page_html)]
                        self.rag.add_wiki_documents(topic, chunks)
                        return self.rag.generate_with_wiki_passages(query, topic, chunks).text
            return Api.Const.Stop()

    def code_handler(self, element: Tag) -> str:
        data_lang = element.get("data-lang")
        code_format = f"<code:{data_lang}>{element.get_text()}</code>"
        return code_format
```

### Search Grounding


```python
# Define tool: search-grounding generation.
# - using gemini-2.0-flash with GoogleSearch tool for response generation
# - using a RAG-implementation to store groundings
# - create new groundings by exact match to topic
# - retrieve existing groundings by similarity to topic
class SearchGroundingGenerator:
    config_ground = types.GenerateContentConfig(
        tools=[types.Tool(google_search=types.GoogleSearch())],
        temperature=0.0
    )
    
    def __init__(self, genai_client, rag_impl):
        self.client = genai_client
        self.rag = rag_impl

    def generate_answer(self, query: str, topic: str):
        stored = self.rag.get_grounding_documents(query, topic)
        if len(stored) > 0:
            for i in range(len(stored)):
                meta_q = stored[i].meta["question"]
                p_ground_match = 0.95 # This can be really high ~ 95-97%
                if tqdm(api.similarity([query, meta_q]) > p_ground_match,
                        desc="Score similarity to stored grounding"):
                    return ast.literal_eval(stored[i].docs)
        return self.get_grounding(query, topic)

    @retry.Retry(
        predicate=is_retriable,
        initial=2.0,
        maximum=64.0,
        multiplier=2.0,
        timeout=600,
    )
    def get_grounding(self, query: str, topic: str):
        contents = [types.Content(role="user", parts=[types.Part(text=query)])]
        contents += f"""
        You're a search assistant that provides answers to questions about {topic}.
        Do not discuss alternative topics of interest. Do not discuss similar topics.
        You will provide answers that discuss only {topic}. 
        You may discuss the owner or parent of {topic} when no other answer is possible.
        Otherwise respond with: I don't know."""
        response = api.retriable(self.client.models.generate_content, 
                                 model=api(Api.Model.GEN), 
                                 config=self.config_ground, 
                                 contents=contents)
        if response.candidates[0].grounding_metadata.grounding_supports is not None:
            if self.is_consistent(query, topic, response.text):
                self.rag.add_grounded_document(query, topic, response)
                return response.text 
        return Api.Const.Stop() # Empty grounding supports or not consistent in response

    def is_consistent(self, query: str, topic: str, model_response: str) -> bool:
        topic = topic.replace("'", "")
        id_strs = topic.split()
        if len(id_strs) == 1:
            matches = re.findall(rf"{id_strs[0]}[\s,.]+\S+", query)
            if len(matches) > 0:
                topic = matches[0]
        compound_match = re.findall(rf"{id_strs[0]}[\s,.]+\S+", model_response)
        model_response = model_response.replace("'", "")
        if len(compound_match) == 0 and topic in model_response:
            return True # not a compound topic id and exact topic match
        for match in compound_match:
            if topic not in match:
                return False
        return True # all prefix matches contained topic
```

### Rest Grounding


```python
# Rest api-helpers to manage request-per-minute limits.
# - define an entry for each endpoint limit
# - init rest tool with limits to create blocking queues
# - apply a limit to requests with rest_tool.try_url
class ApiLimit(Enum):
    FINN = "finnhub.io",50
    POLY = "polygon.io",4 # (id_url,rpm)

class BlockingUrlQueue:
    on_cooldown = False
    cooldown = None
    cooldown_start = None
    
    def __init__(self, rest_fn: Callable, per_minute: int):
        self.per_minute_max = per_minute
        self.quota = per_minute
        self.rest_fn = rest_fn

    def push(self, rest_url: str):
        if not self.on_cooldown:
            self.cooldown = Timer(60, self.reset_quota)
            self.cooldown.start()
            self.cooldown_start = time.time()
            self.on_cooldown = True
        if self.quota > 0:
            self.quota -= 1
            time.sleep(0.034) # ~30 requests per second
            return self.rest_fn(rest_url)
        else:
            print(f"limited {self.per_minute_max}/min, waiting {self.limit_expiry()}s")
            time.sleep(max(self.limit_expiry(),0.5))
            return self.push(rest_url)

    def reset_quota(self):
        self.quota = self.per_minute_max
        self.on_cooldown = False
        self.cooldown_start = None

    def limit_expiry(self):
        if self.cooldown_start:
            return max(60-(time.time()-self.cooldown_start),0)
        return 0
```


```python
# Define tool: rest-grounding generation.
# - using gemini-2.0-flash for response generation
# - using a RAG-implementation to store groundings
# - reduce long-context by chunked pre-processing
class RestGroundingGenerator:    
    limits = None

    def __init__(self, rag_impl, with_limits: bool):
        self.rag = rag_impl
        if with_limits:
            self.limits = {}
            for rest_api in ApiLimit:
                self.limits[rest_api.value[0]] = BlockingUrlQueue(Api.get, rest_api.value[1])

    def get_limit(self, rest_api: ApiLimit) -> Optional[BlockingUrlQueue]:
        return self.limits[rest_api.value[0]] if self.limits else None

    def basemodel(self, data: str, schema: BaseModel, from_lambda: bool = False) -> Optional[BaseModel]:
        try:
            if from_lambda:
                return schema(results=json.loads(data))
            return schema.model_validate_json(data)
        except Exception as e:
            raise e

    def dailycandle(self, data: str) -> Optional[DailyCandle]:
        try:
            candle = json.loads(data)
            if "from" not in candle:
                raise ValueError("not a dailycandle / missing value for date")
            agg = self.basemodel(data, Aggregate)
            return DailyCandle(from_date=candle["from"], 
                               status=agg.status.value, 
                               symbol=agg.symbol, 
                               open=agg.open, 
                               high=agg.high, 
                               low=agg.low, 
                               close=agg.close, 
                               volume=agg.volume, 
                               otc=agg.otc, 
                               preMarket=agg.preMarket, 
                               afterHours=agg.afterHours)
        except Exception as e:
            raise e

    @retry.Retry(timeout=600)
    def try_url(self, url: str, schema: BaseModel, as_lambda: bool, with_limit: Optional[BlockingUrlQueue],
                success_fn: Callable, *args, **kwargs):
        try:
            if self.limits is None:
                data = Api.get(url)
            elif with_limit:
                data = with_limit.push(url)
            if schema is DailyCandle:
                model = self.dailycandle(data)
            else:
                model = self.basemodel(data, schema, as_lambda)
        except Exception as e:
            try:
                print(f"try_url exception: {e}")
                if issubclass(schema, RestResultPoly):
                    return success_fn(*args, **kwargs, result=self.basemodel(data, RestResultPoly))
            except Exception as not_a_result:
                print(not_a_result)
            return StopGeneration()
        else:
            return success_fn(*args, **kwargs, model=model)

    def get_symbol_matches(self, with_content, by_name: bool, model: SymbolResult):
        matches = []
        max_failed_match = model.count if not by_name else 3
        p_desc_match = 0.92
        p_symb_match = 0.95
        if model.count > 0:
            for obj in tqdm(model.get(), desc="Score similarity to query"):
                if max_failed_match > 0:
                    desc = [with_content["q"].upper(), obj.description.split("-", -1)[0]]
                    symb = [with_content["q"].upper(), obj.symbol]
                    if by_name and api.similarity(desc) > p_desc_match: 
                        matches.append(obj.symbol)
                    elif not by_name and api.similarity(symb) > p_symb_match:
                        matches.append(obj.description)
                        max_failed_match = 0
                    else:
                        max_failed_match -= 1
        if len(matches) > 0:
            self.rag.add_api_document(with_content["query"], matches, with_content["q"], "get_symbol_1")
            return matches
        return Api.Const.Stop()

    def get_quote(self, with_content, model: Quote):
        quote = model.model_dump_json()
        self.rag.add_quote_document(with_content["query"], quote, with_content["symbol"], model.t, "get_quote_1")
        return quote

    def parse_financials(self, with_content, model: BasicFinancials):
        metric = list(model.metric.items())
        chunks = []
        # Chunk the metric data.
        for i in range(0, len(metric), Api.Const.MetricBatch()):
            batch = metric[i:i + Api.Const.MetricBatch()]
            chunks.append({"question": with_content["query"], "answer": batch})
        # Chunk the series data.
        for key in model.series.keys():
            series = list(model.series[key].items())
            for s in series:
                if api.token_count(s) <= Api.Const.ChunkMax():
                    chunks.append({"question": with_content["query"], "answer": s})
                else:
                    k = s[0]
                    v = s[1]
                    for i in range(0, len(v), Api.Const.SeriesBatch()):
                        batch = v[i:i + Api.Const.SeriesBatch()]
                        chunks.append({"question": with_content["query"], "answer": {k: batch}})
        self.rag.add_rest_chunks(chunks, topic=with_content["symbol"], source="get_financials_1")
        return chunks

    def parse_news(self, with_content, model: NewsResultFinn):
        if model.count > 0:
            metas = []
            for digest in model.get():
                pub_date = datetime.fromtimestamp(digest.datetime, tz=GeneratedEvent.tz()).strftime("%Y-%m-%d")
                metas.append({"publisher": digest.source,
                              "published_est": parse(pub_date).timestamp(),
                              "news_id": digest.id,
                              "related": digest.related})
            self.rag.add_rest_chunks(model.get(), topic=with_content["symbol"], source="get_news_1",
                                     ids=[f"{digest.id}+news" for digest in model.get()],
                                     meta_opt=metas, is_update=False)
            return [digest.summary().model_dump_json() for digest in model.get()]
        return Api.Const.Stop()

    def parse_news(self, with_content, model: Optional[NewsResultPoly] = None,
                   result: Optional[RestResultPoly] = None) -> tuple[list, str]: # list of summary, next list url
        if model and model.status in [RestStatus.OK, RestStatus.DELAY]:
            metas = []
            for news in model.get():
                pub_date = parse(news.published_utc).strftime("%Y-%m-%d")
                metas.append({"publisher": news.publisher.name,
                              "published_utc": parse(pub_date).timestamp(),
                              "news_id": news.id,
                              "related": json.dumps(news.tickers),
                              "keywords": json.dumps(news.keywords)})
            self.rag.add_rest_chunks(model.get(), topic=with_content["ticker"], source="get_news_2",
                                     ids=[news.id for news in model.get()],
                                     meta_opt=metas, is_update=False)
            return [news.summary().model_dump_json() for news in model.get()], model.next_url
        elif result:
            return result.model_dump_json()

    def parse_daily_candle(self, with_content, model: Optional[DailyCandle] = None,
                           result: Optional[RestResultPoly] = None):
        if model and model.status in [RestStatus.OK, RestStatus.DELAY]:
            self.rag.add_rest_chunks(
                chunks=[model],
                topic=with_content["stocksTicker"],
                source="daily_candle_2",
                meta_opt=[{"from_date": model.from_date, "adjusted": with_content["adjusted"]}])
            return model
        elif result:
            return result

    def parse_custom_candle(self, with_content, model: Optional[CustomCandle] = None,
                            result: Optional[RestResultPoly] = None):
        if model and model.status in [RestStatus.OK, RestStatus.DELAY]:
            metas = [{
                "timespan": with_content["timespan"],
                "adjusted": with_content["adjusted"],
                "from": with_content["from"],
                "to": with_content["to"]}]*model.count
            candles = [candle.model_dump_json() for candle in model.get()]
            self.rag.add_rest_chunks(
                chunks=candles,
                topic=with_content["stocksTicker"],
                source="custom_candle_2",
                meta_opt=metas)
            return candles
        elif result:
            return result.model_dump_json()

    def parse_overview(self, with_content, model: OverviewResult):
        overview = [model.get().model_dump_json()]
        self.rag.add_rest_chunks(chunks=overview, topic=with_content["ticker"], source="ticker_overview_2")
        return overview

    def parse_trends(self, with_content, model: TrendsResult):
        if model.count > 0:
            metas = [{"period": trend.period} for trend in model.get()]
            trends = [trend.model_dump_json() for trend in model.get()]
            self.rag.add_rest_chunks(trends, topic=with_content["symbol"], source="trends_1", meta_opt=metas)
            return trends
        return Api.Const.Stop()

    def augment_market_status(self, with_id: Optional[str], model: MarketStatusResult):
        if model.get().holiday != MarketSession.NA.value:
            self.rag.set_holiday_event(model.get().exchange)
        events = self.rag.generated_events(model.get().exchange)
        model.get().session = events.session()
        model.get().isOpen = events.is_open()
        meta = {"exchange": model.get().exchange,
                "last_close": events.last_close,
                "pre_open": events.pre_open,
                "reg_open": events.reg_open,
                "reg_close": events.reg_close,
                "post_close": events.post_close,
                "timestamp": events.timestamp }
        self.rag.add_rest_chunks([model.get()],
                                 topic="market_status",
                                 source="get_market_status_1",
                                 ids=[with_id] if with_id else None,
                                 meta_opt=[meta])
        return model.get().model_dump_json()

    def get_symbol(self, content, by_name: bool = True):
        return self.try_url(
            f"https://finnhub.io/api/v1/search?q={content['q']}&exchange={content['exchange']}&token={FINNHUB_API_KEY}",
            schema=SymbolResult,
            as_lambda=False,
            with_limit=self.get_limit(ApiLimit.FINN),
            success_fn=self.get_symbol_matches,
            with_content=content,
            by_name=by_name)

    def get_current_price(self, content):
        return self.try_url(
            f"https://finnhub.io/api/v1/quote?symbol={content['symbol']}&token={FINNHUB_API_KEY}",
            schema=Quote,
            as_lambda=False,
            with_limit=self.get_limit(ApiLimit.FINN),
            success_fn=self.get_quote,
            with_content=content)

    def get_market_status(self, content, store_id: Optional[str] = None):
        return self.try_url(
            f"https://finnhub.io/api/v1/stock/market-status?exchange={content['exchange']}&token={FINNHUB_API_KEY}",
            schema=MarketStatusResult,
            as_lambda=True,
            with_limit=self.get_limit(ApiLimit.FINN),
            success_fn=self.augment_market_status,
            with_id=store_id)

    def get_peers(self, content):
        return self.try_url(
            f"https://finnhub.io/api/v1/stock/peers?symbol={content['symbol']}&grouping={content['grouping']}&token={FINNHUB_API_KEY}",
            schema=PeersResult,
            as_lambda=True,
            with_limit=self.get_limit(ApiLimit.FINN),
            success_fn=lambda model: model)

    def get_basic_financials(self, content):
        return self.try_url(
            f"https://finnhub.io/api/v1/stock/metric?symbol={content['symbol']}&metric={content['metric']}&token={FINNHUB_API_KEY}",
            schema=BasicFinancials,
            as_lambda=False,
            with_limit=self.get_limit(ApiLimit.FINN),
            success_fn=self.parse_financials,
            with_content=content)

    def get_news_simple(self, content):
        return self.try_url(
            f"https://finnhub.io/api/v1/company-news?symbol={content['symbol']}&from={content['from']}&to={content['to']}&token={FINNHUB_API_KEY}",
            schema=NewsResultFinn,
            as_lambda=True,
            with_limit=self.get_limit(ApiLimit.FINN),
            success_fn=self.parse_news,
            with_content=content)

    def get_news_tagged(self, content):
        next_url = f"https://api.polygon.io/v2/reference/news?ticker={content['ticker']}&published_utc.gte={content['published_utc.gte']}&published_utc.lte={content['published_utc.lte']}&order={content['order']}&limit={content['limit']}&sort={content['sort']}&apiKey={POLYGON_API_KEY}"
        news = []
        while True:
            news_list, next_url = self.try_url(
                next_url,
                schema=NewsResultPoly,
                as_lambda=False,
                with_limit=self.get_limit(ApiLimit.POLY),
                success_fn=self.parse_news,
                with_content=content)
            news += news_list
            if next_url is None:
                break
            next_url += f"&apiKey={POLYGON_API_KEY}"
        return news

    def get_daily_candle(self, content):
        return self.try_url(
            f"https://api.polygon.io/v1/open-close/{content['stocksTicker']}/{content['date']}?adjusted={content['adjusted']}&apiKey={POLYGON_API_KEY}",
            schema=DailyCandle,
            as_lambda=False,
            with_limit=self.get_limit(ApiLimit.POLY),
            success_fn=self.parse_daily_candle,
            with_content=content)

    def get_custom_candle(self, content):
        return self.try_url(
            f"https://api.polygon.io/v2/aggs/ticker/{content['stocksTicker']}/range/{content['multiplier']}/{content['timespan']}/{content['from']}/{content['to']}?adjusted={content['adjusted']}&sort={content['sort']}&limit={content['limit']}&apiKey={POLYGON_API_KEY}",
            schema=CustomCandle,
            as_lambda=False,
            with_limit=self.get_limit(ApiLimit.POLY),
            success_fn=self.parse_custom_candle,
            with_content=content)

    def get_overview(self, content):
        return self.try_url(
            f"https://api.polygon.io/v3/reference/tickers/{content['ticker']}?apiKey={POLYGON_API_KEY}",
            schema=OverviewResult,
            as_lambda=False,
            with_limit=self.get_limit(ApiLimit.POLY),
            success_fn=self.parse_overview,
            with_content=content)

    def get_trends_simple(self, content):
        return self.try_url(
            f"https://finnhub.io/api/v1/stock/recommendation?symbol={content['symbol']}&token={FINNHUB_API_KEY}",
            schema=TrendsResult,
            as_lambda=True,
            with_limit=self.get_limit(ApiLimit.FINN),
            success_fn=self.parse_trends,
            with_content=content)
```

### Callable Functions


```python
# Callable functions in openapi schema.
decl_get_symbol_1 = types.FunctionDeclaration(
    name="get_symbol_1",
    description="""Search for the stock ticker symbol of a given company, security, isin or cusip. Each ticker
                   entry provides a description, symbol, and asset type. If this doesn't help you should try 
                   calling get_wiki_tool_response next.""",
    parameters={
        "type": "object",
        "properties": {
            "q": {
                "type": "string",
                "description": """A ticker symbol to search for."""
            },
            "exchange": {
                "type": "string",
                "description": """The exchange code used to filter results. When not specified the default exchange 
                                  code you should use is 'US' for the US exchanges. A dictionary mapping all supported 
                                  exchange codes to their names be retrieved by calling get_exchange_codes_1. 
                                  Search for an exchange code to use by calling get_exchange_code_1, specifying the
                                  exchange code to search for."""
            },
            "query": {
                "type": "string",
                "description": "The question you're attempting to answer."
            }
        },
        "required": ["q", "exchange", "query"]
    }
)

decl_get_symbols_1 = types.FunctionDeclaration(
    name="get_symbols_1",
    description="""List all supported symbols and tickers. The results are filtered by exchange code.""",
    parameters={
        "type": "object",
        "properties": {
            "exchange": {
                "type": "string",
                "description": """The exchange code used to filter the results."""
            },
            "query": {
                "type": "string",
                "description": "The question you're attempting to answer."
            }
        },
        "required": ["exchange", "query"]
    }
)

decl_get_name_1 = types.FunctionDeclaration(
    name="get_name_1",
    description="""Search for the name associated with a stock ticker or symbol's company, security, isin or cusip. 
    Each ticker entry provides a description, matching symbol, and asset type.""",
    parameters={
        "type": "object",
        "properties": {
            "q": {
                "type": "string",
                "description": """The symbol or ticker to search for."""
            },
            "exchange": {
                "type": "string",
                "description": """The exchange code used to filter results. When not specified the default exchange 
                                  code you should use is 'US' for the US exchanges. A dictionary mapping all supported 
                                  exchange codes to their names be retrieved by calling get_exchange_codes_1. 
                                  Search for an exchange code to use by calling get_exchange_code_1, specifying the
                                  exchange code to search for."""
            },
            "query": {
                "type": "string",
                "description": "The question you're attempting to answer."
            },
            "company": {
                "type": "string",
                "description": "The company you're searching for."
            }
        },
        "required": ["q", "exchange", "query", "company"]
    }
)

decl_get_symbol_quote_1 = types.FunctionDeclaration(
    name="get_symbol_quote_1",
    description="""Search for the current price or quote of a stock ticker or symbol. The response is
                   provided in json format. Each response contains the following key-value pairs:
                   
                   c: Current price,
                   d: Change,
                  dp: Percent change,
                   h: High price of the day,
                   l: Low price of the day,
                   o: Open price of the day,
                  pc: Previous close price,
                   t: Epoch timestamp of price in seconds.

                   Parse the response and respond according to this information.""",
    parameters={
        "type": "object",
        "properties": {
            "symbol": {
                "type": "string",
                "description": "The stock ticker symbol for a company, security, isin, or cusip." 
            },
            "query": {
                "type": "string",
                "description": "The question you're attempting to answer."
            },
            "exchange": {
                "type": "string",
                "description": "The exchange code used to filter quotes. This must always be 'US'."
            }
        },
        "required": ["symbol", "query", "exchange"]
    }
)

decl_get_local_datetime = types.FunctionDeclaration(
    name="get_local_datetime",
    description="""Converts an array of timestamps from epoch time to the local timezone format. The result is an array
                   of date and time in locale appropriate format. Suitable for use in a locale appropriate response.
                   Treat this function as a vector function. Always prefer to batch timestamps for conversion. Use this
                   function to format date and time in your responses.""",
    parameters={
        "type": "object",
        "properties": {
            "t": {
                "type": "array",
                "description": """An array of timestamps in seconds since epoch to be converted. The order of
                                  timestamps matches the order of conversion.""",
                "items": {
                    "type": "integer"
                }
            }
        },
        "required": ["t"]
    }
)

decl_get_market_status_1 = types.FunctionDeclaration(
    name="get_market_status_1",
    description="""Get the current market status of global exchanges. Includes whether exchanges are open or closed.  
                   Also includes holiday details if applicable. The response is provided in json format. Each response 
                   contains the following key-value pairs:

                   exchange: Exchange code,
                   timezone: Timezone of the exchange,
                    holiday: Holiday event name, or null if it's not a holiday,
                     isOpen: Whether the market is open at the moment,
                          t: Epoch timestamp of status in seconds (Eastern Time),
                    session: The market session can be 1 of the following values: 
                    
                    pre-market,regular,post-market when open, or null if closed.
                    
                    Parse the response and respond according to this information.""",
    parameters={
        "type": "object",
        "properties": {
            "exchange": {
                "type": "string",
                "description": """The exchange code used to filter results. When not specified the default exchange 
                                  code you should use is 'US' for the US exchanges. A dictionary mapping all supported 
                                  exchange codes to their names be retrieved by calling get_exchange_codes_1. 
                                  Search for an exchange code to use by calling get_exchange_code_1, specifying the
                                  exchange code to search for."""
            }
        },
        "required": ["exchange"]
    }
)

decl_get_market_session_1 = types.FunctionDeclaration(
    name="get_market_session_1",
    description="Get the current market session of global exchanges.",
    parameters={
        "type": "object",
        "properties": {
            "exchange": {
                "type": "string",
                "description": """The exchange code used to filter results. When not specified the default exchange 
                                  code you should use is 'US' for the US exchanges. A dictionary mapping all supported 
                                  exchange codes to their names be retrieved by calling get_exchange_codes_1. 
                                  Search for an exchange code to use by calling get_exchange_code_1, specifying the
                                  exchange code to search for."""
            }
        },
        "required": ["exchange"]
    }
)

decl_get_company_peers_1 = types.FunctionDeclaration(
    name="get_company_peers_1",
    description="""Search for a company's peers. Returns a list of peers operating in the same country and in the same
                   sector, industry, or subIndustry. Each response contains the following key-value pairs: 
                   
                   symbol: The company's stock ticker symbol, 
                   peers: A list containing the peers.
                   
                   Each peers entry contains the following key-value pairs:
                   
                   symbol: The peer company's stock ticker symbol, 
                   name: The peer company's name.
                   
                   Parse the response and respond according to this information.""",
    parameters={
        "type": "object",
        "properties": {
            "symbol": {
                "type": "string",
                "description": "The stock ticker symbol of a company to obtain peers."
            },
            "grouping": {
                "type": "string",
                "description": """This parameter may be one of the following values: sector, industry, subIndustry.
                                  Always use subIndustry unless told otherwise."""
            },
            "exchange": {
                "type": "string",
                "description": """The exchange code used to filter results. When not specified the default exchange 
                                  code you should use is 'US' for the US exchanges. A dictionary mapping all supported 
                                  exchange codes to their names be retrieved by calling get_exchange_codes_1. 
                                  Search for an exchange code to use by calling get_exchange_code_1, specifying the
                                  exchange code to search for."""
            },
            "query": {
                "type": "string",
                "description": "The question you're attempting to answer."
            }
        },
        "required": ["symbol", "grouping", "exchange", "query"]
    }
)

decl_get_exchange_codes_1 = types.FunctionDeclaration(
    name="get_exchange_codes_1",
    description="""Get a dictionary mapping all supported exchange codes to their names."""
)

decl_get_exchange_code_1 = types.FunctionDeclaration(
    name="get_exchange_code_1",
    description="""Search for the exchange code to use when filtering by exchange. The result will be one or
                   more exchange codes provided as a comma-separated string value.""",
    parameters={
        "type": "object",
        "properties": {
            "q": {
                "type": "string",
                "description": "Specifies which exchange code to search for."
            }
        },
        "required": ["q"]
    }
)

decl_get_financials_1 = types.FunctionDeclaration(
    name="get_financials_1",
    description="""Get company basic financials such as margin, P/E ratio, 52-week high/low, etc. Parse the response for 
                   key-value pairs in json format and interpret their meaning as stock market financial indicators.""",
    parameters={
        "type": "object",
        "properties": {
            "symbol": {
                "type": "string",
                "description": "Stock ticker symbol for a company."
            },
            "metric": {
                "type": "string",
                "description": "It must always be declared as the value 'all'"
            },
            "query": {
                "type": "string",
                "description": "The question you're attempting to answer."
            }
        },
        "required": ["symbol", "metric", "query"]
    }
)

decl_get_daily_candlestick_2 = types.FunctionDeclaration(
    name="get_daily_candlestick_2",
    description="""Get a historical daily stock ticker candlestick / aggregate bar (OHLC). 
                   Includes historical daily open, high, low, and close prices. Also includes historical daily trade
                   volume and pre-market/after-hours trade prices. It provides the last trading days' data after 
                   11:59PM Eastern Time.""",
    parameters={
        "type": "object",
        "properties": {
            "stocksTicker": {
                "type": "string",
                "description": "The stock ticker symbol of a company to search for.",
            },
            "date": {
                "type": "string",
                "format": "date-time",
                "description": """The date of the requested candlestick in format YYYY-MM-DD."""
            },
            "adjusted": {
                "type": "string",
                "description": """May be true or false. Indicates if the results should be adjusted for splits.
                                  Use true unless told otherwise."""
            },
            "exchange": {
                "type": "string",
                "description": """The exchange code used to filter results. When not specified the default exchange 
                                  code you should use is 'US' for the US exchanges. A dictionary mapping all supported 
                                  exchange codes to their names be retrieved by calling get_exchange_codes_1. 
                                  Search for an exchange code to use by calling get_exchange_code_1, specifying the
                                  exchange code to search for."""
            },
            "query": {
                "type": "string",
                "description": "The question you're attempting to answer."
            }
        },
        "required": ["stocksTicker", "date", "adjusted", "exchange", "query"]
    },
)

decl_get_company_news_1 = types.FunctionDeclaration(
    name="get_company_news_1",
    description="Retrieve the most recent news articles related to a specified ticker.",
    parameters={
        "type": "object",
        "properties": {
            "symbol": {
                "type": "string",
                "description": "Stock ticker symbol for a company.",
            },
            "from": {
                "type": "string",
                "format": "date-time",
                "description": """A date in format YYYY-MM-DD. It must be older than the parameter 'to'."""
            },
            "to": {
                "type": "string",
                "format": "date-time",
                "description": """A date in format YYYY-MM-DD. It must be more recent than the parameter 'from'. The
                                  default value is today's date."""
            },
            "query": {
                "type": "string",
                "description": "The question you're attempting to answer."
            }
        },
        "required": ["symbol", "from", "to", "query"]
    },
)

decl_get_custom_candlestick_2 = types.FunctionDeclaration(
    name="get_custom_candlestick_2",
    description="""Get a historical stock ticker candlestick / aggregate bar (OHLC) over a custom date range and 
                   time interval in Eastern Time. Includes historical open, high, low, and close prices. Also 
                   includes historical daily trade volume and pre-market/after-hours trade prices. It includes 
                   the last trading days' data after 11:59PM Eastern Time.""",
    parameters={
        "type": "object",
        "properties": {
            "stocksTicker": {
                "type": "string",
                "description": "The stock ticker symbol of a company to search for.",
            },
            "multiplier": {
                "type": "integer",
                "description": "This must be included and equal to 1 unless told otherwise."
            },
            "timespan": {
                "type": "string",
                "description": """The size of the candlestick's time window. This is allowed to be one of the following:
                                  second, minute, hour, day, week, month, quarter, or year. The default value is day."""
            },
            "from": {
                "type": "string",
                "format": "date-time",
                "description": """A date in format YYYY-MM-DD must be older than the parameter 'to'."""
            },
            "to": {
                "type": "string",
                "format": "date-time",
                "description": """A date in format YYYY-MM-DD must be more recent than the parameter 'from'. The 
                                  default is one weekday before get_last_market_close.
                                  Replace more recent dates with the default."""
            },
            "adjusted": {
                "type": "string",
                "description": """May be true or false. Indicates if the results should be adjusted for splits.
                                  Use true unless told otherwise."""
            },
            "sort": {
                "type": "string",
                "description": """This must be included. May be one of asc or desc. asc will sort by timestmap in 
                                  ascending order. desc will sort by timestamp in descending order."""
            },
            "limit": {
                "type": "integer",
                "description": """Set the number of base aggregates used to create this candlestick. This must be 5000 
                                  unless told to limit base aggregates to something else."""
            },
            "query": {
                "type": "string",
                "description": "The question you're attempting to answer."
            }
        },
        "required": ["stocksTicker", "multiplier", "timespan", "from", "to", "adjusted", "sort", "limit", "query"]
    },
)

decl_get_last_market_close = types.FunctionDeclaration(
    name="get_last_market_close",
    description="""Get the last market close of the specified exchange in Eastern Time. The response has already
                   been converted by get_local_datetime so this step should be skipped.""",
    parameters={
        "type": "object",
        "properties": {
            "exchange": {
                "type": "string",
                "description": """The exchange code used to filter results. When not specified the default exchange 
                                  code you should use is 'US' for the US exchanges. A dictionary mapping all supported 
                                  exchange codes to their names be retrieved by calling get_exchange_codes_1. 
                                  Search for an exchange code to use by calling get_exchange_code_1, specifying the
                                  exchange code to search for."""
            }
        },
        "required": ["exchange"]
    }
)

decl_get_ticker_overview_2 = types.FunctionDeclaration(
    name="get_ticker_overview_2",
    description="""Retrieve comprehensive details for a single ticker symbol. It's a deep look into a company’s 
    fundamental attributes, including its primary exchange, standardized identifiers (CIK, composite FIGI, 
    share class FIGI), market capitalization, industry classification, and key dates. Also includes branding assets in
    the form of icons and logos.
    """,
    parameters={
        "type": "object",
        "properties": {
            "ticker": {
                "type": "string",
                "description": "Stock ticker symbol of a company."
            },
            "query": {
                "type": "string",
                "description": "The question you're attempting to answer."
            }
        },
        "required": ["ticker", "query"]
    }
)

decl_get_recommendation_trends_1 = types.FunctionDeclaration(
    name="get_recommendation_trends_1",
    description="""Get the latest analyst recommendation trends for a company.
                The data includes the latest recommendations as well as historical
                recommendation data for each month. The data is classified according
                to these categories: strongBuy, buy, hold, sell, and strongSell.
                The date of a recommendation indicated by the value of 'period'.""",
    parameters={
        "type": "object",
        "properties": {
            "symbol": {
                "type": "string",
                "description": "Stock ticker symbol for a company."
            },
            "query": {
                "type": "string",
                "description": "The question you're attempting to answer."
            }
        },
        "required": ["symbol", "query"]
    }
)

decl_get_news_with_sentiment_2 = types.FunctionDeclaration(
    name="get_news_with_sentiment_2",
    description="""Retrieve the most recent news articles related to a specified ticker. Each article includes 
                   comprehensive coverage. Including a summary, publisher information, article metadata, 
                   and sentiment analysis.""",
    parameters={
        "type": "object",
        "properties": {
            "ticker": {
                "type": "string",
                "description": "Stock ticker symbol for a company."
            },
            "published_utc.gte": {
                "type": "string",
                "format": "date-time",
                "description": """A date in format YYYY-MM-DD must be older than the parameter 'published_utc.lte'. 
                                  The default value is one-month ago from today's date."""
            },
            "published_utc.lte": {
                "type": "string",
                "format": "date-time",
                "description": """A date in format YYYY-MM-DD must be more recent than the parameter 'published_utc.gte'.
                                  The default is one weekday prior to get_last_market_close (excluding weekends).
                                  Replace more recent dates with the default."""
            },
            "order": {
                "type": "string",
                "description": """Must be desc for descending order, or asc for ascending order.
                                  When order is not specified the default is descending order.
                                  Ordering will be based on the parameter 'sort'."""
            },
            "limit": {
                "type": "integer",
                "description": """This must be included and equal to 1000 unless told otherwise."""
            },
            "sort": {
                "type": "string",
                "description": """The sort field used for ordering. This value must
                                  always be published_utc."""
            },
            "query": {
                "type": "string",
                "description": "The question you're attempting to answer."
            }
        },
        "required": ["limit", "ticker", "published_utc.gte", "published_utc.lte", "order", "sort", "query"]
    }
)

decl_get_rag_tool_response = types.FunctionDeclaration(
    name="get_rag_tool_response",
    description="""A database containing useful financial information. Always check here for answers first.""",
    parameters={
        "type": "object",
        "properties": {
            "question": {
                "type": "string",
                "description": "A question needing an answer. Asked as a simple string."
            }
        }
    }
)

decl_get_wiki_tool_response = types.FunctionDeclaration(
    name="get_wiki_tool_response",
    description="""Answers questions that still have unknown answers. Retrieve a wiki page related to a company, 
                   product, or service. Each web page includes detailed company information, financial indicators, 
                   tickers, symbols, history, and products and services.""",
    parameters={
        "type": "object",
        "properties": {
            "id": {
                "type": "string",
                "description": "The question's company or product. Just the name and no other details."
            },
            "q": {
                "type": "string",
                "description": "The complete, unaltered, query string."
            }
        },
        "required": ["id", "q"]
    }
)

decl_get_search_tool_response = types.FunctionDeclaration(
    name="get_search_tool_response",
    description="Answers questions that still have unknown answers. Use it after checking all your other tools.",
    parameters={
        "type": "object",
        "properties": {
            "q": {
                "type": "string",
                "description": "The question needing an answer. Asked as a simple string."
            },
            "id": {
                "type": "string",
                "description": "The question's company or product. In one word. Just the name and no other details."
            }
        },
        "required": ["q", "id"]
    }
)
```


```python
# Import the finance api secret keys.

POLYGON_API_KEY = UserSecretsClient().get_secret("POLYGON_API_KEY")
FINNHUB_API_KEY = UserSecretsClient().get_secret("FINNHUB_API_KEY")
```


```python
# Instantiate tools and load the exchange data from source csv.
# - Identifies exchanges by a 1-2 letter code which can be used to filter response data.
# - Also maps the exchange code to exchange details.
try:
    df = pandas.read_csv("/kaggle/input/exchanges/exchanges_src.csv")
except FileNotFoundError as e:
    df = pandas.read_csv("exchanges_src.csv") # local run
df = df.drop(["close_date"], axis=1).fillna("")
df.to_csv("exchanges.csv", index=False)
exchanges = CSVLoader(file_path="exchanges.csv", encoding="utf-8", csv_args={"delimiter": ","}).load()

# Prepare a RAG tool for use and add the exchange data.
tool_rag = RetrievalAugmentedGenerator(api.args.CLIENT, "finance")
tool_rag.add_documents_list(exchanges)

# Prepare a the grounding tools for use.
tool_wiki = WikiGroundingGenerator(api.args.CLIENT, tool_rag)
tool_ground = SearchGroundingGenerator(api.args.CLIENT, tool_rag)
tool_rest = RestGroundingGenerator(tool_rag, with_limits=True)
```

### Function Calling Expert


```python
# Implement the callable functions and function handler.

def ask_rag_tool(content):
    return tool_rag.generate_answer(content["question"]).text

def ask_wiki_tool(content):
    return tool_wiki.generate_answer(content["q"], content["id"])

def ask_search_tool(content):
    return tool_ground.generate_answer(content["q"], content["id"])

def get_exchange_codes_1(content):
    return tool_rag.get_exchange_codes()

def get_exchange_code_1(content):
    return tool_rag.get_exchange_codes(with_query=content)
    
def last_market_close(content):
    return tool_rag.last_market_close(content["exchange"])
    
def get_symbol_1(content, by_name: bool = True):
    stored = tool_rag.get_api_documents(content["query"], content["q"], "get_symbol_1")
    if len(stored) == 0:
        return tool_rest.get_symbol(content, by_name)
    return json.loads(stored[0].docs)

def get_symbols_1(content):
    return None # todo

def get_name_1(content):
    return get_symbol_1(content, by_name = False)

def get_quote_1(content):
    stored = tool_rag.get_api_documents(content["query"], content["symbol"], "get_quote_1")
    if tool_rag.generated_events(content["exchange"]).is_open():
        return get_current_price_1(content)
    elif len(stored) > 0:
        last_close = parse(tool_rag.last_market_close(content["exchange"])).timestamp()
        for quote in stored:
            if quote.meta["timestamp"] >= last_close:
                return [quote.docs for quote in stored]
    return get_current_price_1(content)

def get_current_price_1(content):
    return tool_rest.get_current_price(content)

def get_market_status_1(content):
    stored, has_update = tool_rag.get_market_status(content['exchange'])
    if has_update:
        with_id = stored[0].store_id if len(stored) > 0 else None
        return tool_rest.get_market_status(content, with_id)
    return stored[0].docs

def get_session_1(content):
    return json.loads(get_market_status_1(content))["session"]

def get_peers_1(content):
    stored = tool_rag.get_peers_document(content["query"], content["symbol"], content['grouping'])
    if len(stored) == 0:
        peers = tool_rest.get_peers(content)
        if peers.count > 0:
            names = []
            for peer in peers.get():
                if peer == content["symbol"]:
                    continue # skip including the query symbol in peers
                name = get_name_1(dict(q=peer, exchange=content["exchange"], query=content["query"]))
                if name != Api.Const.Stop():
                    data = {"symbol": peer, "name": name}
                    names.append(data)
            tool_rag.add_peers_document(content["query"], names, content["symbol"], "get_peers_1", content['grouping'])
            return names
        return Api.Const.Stop()
    return json.loads(stored[0].docs)["peers"]

def local_datetime(content):
    local_t = []
    for timestamp in content["t"]:
        local_t.append(local_date_from_epoch(timestamp))
    return local_t

def local_date_from_epoch(timestamp):
    if len(str(timestamp)) == 13:
        return datetime.fromtimestamp(timestamp/1000, tz=GeneratedEvent.tz()).strftime('%c')
    else:
        return datetime.fromtimestamp(timestamp, tz=GeneratedEvent.tz()).strftime('%c')

def get_financials_1(content):
    stored = tool_rag.get_basic_financials(content["query"], content["symbol"], "get_financials_1")
    if len(stored) == 0:
        return tool_rest.get_basic_financials(content)
    return [chunk.docs for chunk in stored]

def get_news_1(content):
    stored = tool_rag.get_api_documents(content["query"], content["symbol"], "get_news_1")
    if len(stored) == 0:
        return tool_rest.get_news_simple(content)
    return [NewsTypeFinn.model_validate_json(news.docs).summary().model_dump_json() for news in stored]

def get_daily_candle_2(content):
    stored = tool_rag.get_api_documents(
        query=content["query"], topic=content["stocksTicker"], source="daily_candle_2", 
        meta_opt=[{"from_date": content["date"], "adjusted": content["adjusted"]}])
    if len(stored) == 0:
        candle = tool_rest.get_daily_candle(content)
        # Attempt to recover from choosing a holiday.
        candle_date = parse(content["date"])
        if candle.status is RestStatus.NONE and candle_date.weekday() == 0 or candle_date.weekday() == 4:
            if candle_date.weekday() == 0: # index 0 is monday, index 4 is friday
                content["date"] = candle_date.replace(day=candle_date.day-3).strftime("%Y-%m-%d")
            else:
                content["date"] = candle_date.replace(day=candle_date.day-1).strftime("%Y-%m-%d")
            return get_daily_candle_2(content)
        return candle.model_dump_json()
    return [json.loads(candle.docs) for candle in stored]

def get_custom_candle_2(content):
    stored = tool_rag.get_api_documents(
        query=content["query"], topic=content["stocksTicker"], source="custom_candle_2", 
        meta_opt=[{
            "timespan": content["timespan"],
            "adjusted": content["adjusted"],
            "from": content["from"],
            "to": content["to"]}])
    if len(stored) == 0:
        return tool_rest.get_custom_candle(content)
    return [json.loads(candle.docs) for candle in stored]

def get_overview_2(content):
    stored = tool_rag.get_api_documents(content["query"], content["ticker"], "ticker_overview_2")
    if len(stored) == 0:
        return tool_rest.get_overview(content)
    return json.loads(stored[0].docs)

def get_trends_1(content):
    stored = tool_rag.get_api_documents(content["query"], content["symbol"], "trends_1")
    if len(stored) == 0:
        return tool_rest.get_trends_simple(content)
    return [json.loads(trend.docs) for trend in stored]

def get_news_2(content):
    timestamp_from = parse(content["published_utc.gte"]).timestamp()
    timestamp_to = parse(content["published_utc.lte"]).timestamp()
    news_from = tool_rag.get_api_documents(
        content["query"], content["ticker"], "get_news_2", [{"published_utc": timestamp_from}])
    news_to = tool_rag.get_api_documents(
        content["query"], content["ticker"], "get_news_2", [{"published_utc": timestamp_to}])
    if len(news_from) > 0 and len(news_to) > 0:
        stored = tool_rag.get_api_documents(
            content["query"], content["ticker"], "get_news_2",
            [{"published_utc": {"$gte": timestamp_from}},
             {"published_utc": {"$lte": timestamp_to}}])
        return [NewsTypePoly.model_validate_json(news.docs).summary().model_dump_json() for news in stored]
    return tool_rest.get_news_tagged(content)
        
finance_tool = types.Tool(
    function_declarations=[
        decl_get_symbol_1,
        decl_get_symbols_1,
        decl_get_name_1,
        decl_get_symbol_quote_1,
        decl_get_market_status_1,
        decl_get_market_session_1,
        decl_get_company_peers_1,
        decl_get_local_datetime,
        decl_get_last_market_close,
        decl_get_exchange_codes_1,
        decl_get_exchange_code_1,
        decl_get_financials_1,
        decl_get_daily_candlestick_2,
        decl_get_custom_candlestick_2,
        decl_get_ticker_overview_2,
        decl_get_recommendation_trends_1,
        decl_get_news_with_sentiment_2,
        decl_get_rag_tool_response,
        decl_get_wiki_tool_response,
        decl_get_search_tool_response
    ]
)

function_handler = {
    "get_symbol_1": get_symbol_1,
    "get_symbols_1": get_symbols_1,
    "get_name_1": get_name_1,
    "get_symbol_quote_1": get_quote_1,
    "get_market_status_1": get_market_status_1,
    "get_market_session_1": get_session_1,
    "get_company_peers_1": get_peers_1,
    "get_local_datetime": local_datetime,
    "get_last_market_close": last_market_close,
    "get_exchange_codes_1": get_exchange_codes_1,
    "get_exchange_code_1": get_exchange_code_1,
    "get_financials_1": get_financials_1,
    "get_daily_candlestick_2": get_daily_candle_2,
    "get_custom_candlestick_2": get_custom_candle_2,
    "get_ticker_overview_2": get_overview_2,
    "get_recommendation_trends_1": get_trends_1,
    "get_news_with_sentiment_2": get_news_2,
    "get_rag_tool_response": ask_rag_tool,
    "get_wiki_tool_response": ask_wiki_tool,
    "get_search_tool_response": ask_search_tool
}
```


```python
# Implement the function calling expert.
# Define the system prompt.
instruction = f"""You are a helpful and informative bot that answers finance and stock market questions. 
Only answer the question asked and do not change topic. While the answer is still
unknown you must follow these rules for predicting function call order:

RULE#1: Always consult your other functions before get_search_tool_response.
RULE#2: Always consult get_wiki_tool_response before get_search_tool_response.
RULE#3: Always consult get_search_tool_response last.
RULE#4: Always convert timestamps with get_local_datetime and use the converted date/time in your response.
RULE#5: Always incorporate as much useful information from tools and functions in your response."""

def get_response():
    # Enable system prompt, function calling and minimum-randomness.
    config_fncall = types.GenerateContentConfig(
        system_instruction=instruction,
        tools=[finance_tool],
        temperature=0.0
    )
    memory.response = api.retriable(
        api.args.CLIENT.models.generate_content,
        model=api(Api.Model.GEN),
        config=config_fncall,
        contents=memory.contents)

def retry_last_send():
    api.generation_fail()
    time.sleep(api.dt_between)
    get_response()

@retry.Retry(
    predicate=is_retriable,
    initial=2.0,
    maximum=64.0,
    multiplier=2.0,
    timeout=600,
)
def send_message(prompt):
    #display(Markdown("#### Prompt"))
    #print(prompt, "\n")
    memory.set_prompt(prompt)
    # Handle cases with multiple chained function calls.
    function_calling_in_process = True
    # Send the initial user prompt and function declarations.
    get_response()
    while function_calling_in_process:
        try:
            response_parts = memory.response.candidates[0].content.parts
            # A summary response never includes function calls.
            if not any(part.function_call for part in response_parts):
                memory.set_summary("\n".join(e.text for e in response_parts))
                function_calling_in_process = False
                break # The function calling chain is complete.
            else:
                # A part can be a function call or reasoning-step.
                for part in response_parts:
                    if function_call := part.function_call:
                        # Extract the function call.
                        fn_name = function_call.name
                        #display(Markdown("#### Predicted function name"))
                        #print(fn_name, "\n")
                        # Extract the function call arguments.
                        fn_args = {key: value for key, value in function_call.args.items()}
                        #display(Markdown("#### Predicted function arguments"))
                        #print(fn_args, "\n")
                        # Call the predicted function.
                        print("send_message: get function response")
                        api_response = function_handler[fn_name](fn_args)[:20000] # Stay within the input token limit
                        #display(Markdown("#### API response"))
                        #print(api_response[:500], "...", "\n")
                        # Create an API response part.
                        api_response_part = types.Part.from_function_response(
                            name=fn_name,
                            response={"content": api_response},
                        )
                        memory.update_contents(function_call, api_response_part)
                    else:
                        #display(Markdown("#### Natural language reasoning step"))
                        #print(part.text)
                        memory.set_reason(part.text)
                print("send_message: updating state")
                get_response() # Send the updated prompt.
                print("send_message: got a response")
        except Exception as e:
            if isinstance(response_parts, list):
                print("send_message: generated wrong function arguments")
            retry_last_send()
            
    # Show the final natural language summary.
    display(Markdown("#### Natural language response"))
    display(Markdown(memory.summary))
```

## RAG Baseline Check


```python
response = tool_rag.get_exchanges_csv(
    """Give me a dictionary in string form. It must contain key:value pairs mapping 
    exchange code to name. Just the dictionary string in pretty form.""")
print(response.candidates[0].content.parts[-1].text)

response = tool_rag.get_exchanges_csv(
    """What is the Germany exchange code? Return only the exchange codes as a simple 
    comma separated value that I can copy.""")
print(response.candidates[0].content.parts[-1].text, "\n")

response = tool_rag.get_exchanges_csv("What are the Germany exchanges and thier corresponding exchange codes?")
print(response.text, "\n")

response = tool_rag.generate_answer("What are Google's stock ticker symbols?")
print(response.text, "\n")

response = tool_rag.generate_answer("What is Facebook's stock ticker symbol?")
print(response.text, "\n")

response = tool_rag.get_exchanges_csv("What are the US exchange operating hours?")
print(response.text, "\n")

response = tool_rag.get_exchanges_csv(
    f"""Answer based on your knowledge of exchange operating hours.
    Do not answer in full sentences. Omit all chat and provide the answer only.
    The fields pre_market and post_market both represent extended operating hours.

    The current date and time: {datetime.now(GeneratedEvent.tz()).strftime('%c')}

    Weekdays are: Mon, Tue, Wed, Thu, Fri.
    On weekdays all exchanges open after pre-market and regular hours.
    On weekdays all exchanges close after regular and post-market hours.
    
    Weekends are: Sat, Sun.
    Always exclude weekends from exchange operating hours.
    A list of holidays in date format mm-dd-yyyy: {tool_rag.holidays["US"]}
    Always exclude holidays from exchange operating hours.
    When the answer is a holiday use the prior weekday for close.
    When the answer is a holiday use the next weekday for open.
    
    Consider the US exchange's operating hours.
    Provide the most recent weekday's close including post_market hours.
    
    Answer with a date that uses this format: '%a %b %d %X %Y'.""")
print(response.candidates[0].content.parts[-1].text)
```

```
{
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
```
DE, F, TG, SX, BE, DU, HA, HM, MU, SC, SG 

The Germany exchanges and their corresponding exchange codes are: XETRA (DE), DEUTSCHE BOERSE AG (F), Hanover Stock Exchange (HA), DEUTSCHE BOERSE TradeGate (TG), BOERSE BERLIN (BE), BOERSE DUESSELDORF (DU), HANSEATISCHE WERTPAPIERBOERSE HAMBURG (HM), BOERSE MUENCHEN (MU), DEUTSCHE BOERSE Stoxx (SX), BOERSE_FRANKFURT_ZERTIFIKATE (SC), and BOERSE STUTTGART (SG). 

I don't know. 

I don't know. 

US exchanges, including NYSE and Nasdaq, operate from 09:30 to 16:00 in the America/New_York timezone. 

Fri Nov 28 20:00:00 2025

## SC1 Baseline Check


```python
# Wait 59s for rate-limits to reset on FREE-tier.
if api.args.API_LIMIT is Api.Limit.FREE.value:
    print("Gemini API limit is FREE. Waiting 59s...")
    time.sleep(59)
```

Gemini API limit is FREE. Waiting 59s...
Api.refill_rpm 10

```python
send_message("What is the current session for US exchanges?")
```

The US market is currently **open** for the **regular** session.

The current market status was last updated on **Mon Dec 1 11:35:58 2025** (Eastern Time). There are no holidays affecting the market today.

```python
send_message("What is the US market status?")
```

The US market is currently **open** for the **regular** session.

The current market status was last updated on **Mon Dec 1 11:35:58 2025** (Eastern Time). There are no holidays affecting the market today.

```python
send_message("When was the last US market close?")
```

The last US market close was on Friday, November 28, 2025, at 8:00:00 PM.

```python
send_message("What is Apple's stock ticker?")
```

Apple's stock ticker symbol is AAPL.

```python
send_message("What is the current price of Amazon stock? Display the result as a json string in markdown.")
```

```json
{
"c": 234.125,
"d": 0.905,
"dp": 0.388,
"h": 235.797,
"l": 231.88,
"o": 231.88,
"pc": 233.22,
"t": 1764606938
}
```

```python
send_message("""Show me Apple's basic financials and help me understand key performance metrics. 
How has the stock performed?""")
```

Here's an overview of Apple's financials and stock performance based on the data from 2025:

**Financial Highlights:**

*   **Revenue Growth:** Apple has demonstrated strong revenue growth with a TTM YoY growth of 6.43%.
*   **Profitability:** The company maintains a high level of profitability, with a TTM Net Profit Margin of 26.92%.
*   **Gross Margin:** Apple's gross margin is also strong, with a TTM of 46.91%.
*   **Earnings Per Share (EPS):** Apple's EPS has grown significantly, with a TTM EPS Excl. Extra Items of 7.4593, reflecting a growth of 22.89% YoY.
*   **P/E Ratio:** The trailing twelve months (TTM) Price-to-Earnings (P/E) ratio is 36.7859. The forward P/E ratio is 33.6884.
*   **Dividends:** Apple pays a dividend, with a current dividend yield of 0.3743%. The dividend per share TTM is $1.0318.
*   **Return on Equity (ROE):** Apple's ROE is very high, with a TTM value of 164.05%.
*   **52-Week Performance:** The 52 week high is 280.38, reached on 2025-11-25, and the 52 week low is 169.2101, reached on 2025-04-08.
*   **Stock Performance:**
    *   The stock has a 5-Day Price Return Daily of 2.711%.
    *   The Month-to-Date Price Return Daily is 3.1364%.
    *   The Year-to-Date Price Return Daily is 11.3529%.
    *   The 52-Week Price Return Daily is 18.6293%.
    *   The 13-Week Price Return Daily is 19.9045%.
    *   The 26-Week Price Return Daily is 39.2788%.

**Key Performance Metrics:**

*   **Beta:** The beta is 1.0957, indicating that the stock is slightly more volatile than the market.
*   **PEG Ratio:** The PEG ratio is 1.6255, which is above 1, suggesting that the stock may be overvalued relative to its earnings growth.

**Financial Health:**

*   **Current Ratio:** The current ratio is 0.8933, which is below 1, suggesting that the company may have some liquidity issues.
*   **Debt-to-Equity Ratio:** The Long Term Debt to Equity Annual is 1.0623, indicating a moderate level of debt relative to equity.

**Valuation:**

*   **Price-to-Book Ratio (P/B):** The P/B ratio is 55.8825, which is very high, suggesting that the stock may be overvalued.
*   **Price-to-Sales Ratio (P/S):** The P/S ratio is 9.9009.

**Additional Indicators:**

*   **Price Relative to S&P 500:**
    *   Price Relative to S&P 500 13 Week: 14.5926
*   **Price Relative to S&P 500 26 Week:** 23.6753
*   **Price Relative to S&P 500 52 Week:** 4.8542

```python
send_message("I need Apple's daily candlestick from 2025-05-05")
```

Here is Apple's daily candlestick data for 2025-05-05:

*   **Symbol:** AAPL
*   **Open:** 203.1
*   **High:** 204.1
*   **Low:** 198.21
*   **Close:** 198.89
*   **Volume:** 69018452
*   **Pre-market:** 205.0
*   **After-hours:** 198.6

```python
send_message("Tell me who are Apple's peers?")
```

Apple's peers are: DELL TECHNOLOGIES -C (DELL), WESTERN DIGITAL CORP (WDC), SANDISK CORP (SNDK), HEWLETT PACKARD ENTERPRISE (HPE), PURE STORAGE INC - CLASS A (PSTG), HP INC (HPQ), NETAPP INC (NTAP), SUPER MICRO COMPUTER INC (SMCI), IONQ INC (IONQ), QUANTUM COMPUTING INC (QUBT), COMPOSECURE INC-A (CMPO).

```python
send_message("Tell me who are Amazon's peers?")
```

Amazon's peers include Coupang Inc (CPNG), eBay Inc (EBAY), Dillard's Inc-CL A (DDS), Ollie's Bargain Outlet Holdings (OLLI), Macy's Inc (M), Etsy Inc (ETSY), Kohl's Corp (KSS), Pattern Group Inc-CL A (PTRN), Savers Value Village Inc (SVV), and Groupon Inc (GRPN).

```python
send_message("""Locate Apple's stock ticker, then download recommendation trends of all Apple's peers by sub-industry, 
and then finally compare them.""")
```

Apple's stock ticker is **AAPL**.

Here is a comparison of the latest analyst recommendation trends for Apple and its peers in the sub-industry, based on data as of **Sun Dec 1 00:00:00 2024**:

| Company (Ticker) | Strong Buy | Buy | Hold | Sell | Strong Sell | Total Recommendations |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Apple (AAPL)** | 15 | 23 | 16 | 2 | 0 | 56 |
| **DELL TECHNOLOGIES -C (DELL)** | 8 | 16 | 7 | 1 | 0 | 32 |
| **WESTERN DIGITAL CORP (WDC)** | 6 | 19 | 6 | 0 | 0 | 31 |
| **SANDISK CORP (SNDK)** | 7 | 11 | 6 | 0 | 0 | 24 |
| **HEWLETT PACKARD ENTERPRISE (HPE)** | 6 | 7 | 13 | 0 | 0 | 26 |
| **PURE STORAGE INC - CLASS A (PSTG)** | 7 | 13 | 6 | 1 | 0 | 27 |
| **HP INC (HPQ)** | 1 | 1 | 16 | 6 | 1 | 25 |
| **NETAPP INC (NTAP)** | 3 | 10 | 14 | 0 | 0 | 27 |
| **SUPER MICRO COMPUTER INC (SMCI)** | 4 | 10 | 9 | 3 | 0 | 26 |
| **IONQ INC (IONQ)** | 2 | 10 | 4 | 0 | 0 | 16 |
| **QUANTUM COMPUTING INC (QUBT)** | 2 | 5 | 2 | 0 | 0 | 9 |
| **COMPOSECURE INC-A (CMPO)** | 2 | 8 | 2 | 0 | 0 | 12 |

### Key Observations:

*   **Apple (AAPL)** has the highest number of total recommendations (56) and a strong overall positive sentiment, with 38 "Buy" or "Strong Buy" ratings compared to 18 "Hold" or "Sell" ratings.
*   **WESTERN DIGITAL CORP (WDC)** has the highest proportion of "Buy" ratings among its peers, with 19 "Buy" and 6 "Strong Buy" ratings, and no "Sell" or "Strong Sell" ratings.
*   **HP INC (HPQ)** stands out with the most cautious outlook, having the highest number of "Hold" (16) and "Sell" (6) ratings, and the lowest number of "Strong Buy" ratings (1) among the group.
*   **NETAPP INC (NTAP)** and **HEWLETT PACKARD ENTERPRISE (HPE)** have a higher concentration of "Hold" ratings, suggesting analysts are taking a more neutral stance on these companies.
*   Smaller companies like **IONQ INC (IONQ)**, **QUANTUM COMPUTING INC (QUBT)**, and **COMPOSECURE INC-A (CMPO)** have fewer total recommendations, but generally maintain a positive to neutral outlook.

```python
send_message("""Tell me Amazon's current share price and provide candlestick data for the past month. 
Sort the data in descending order by date. Format the prices consistently as currency. 
Round prices to two decimal places. 
Present the data with multiple columns for display in markdown. 
Discuss and provide details about any patterns you notice in the price data. 
Correlate recent patterns with news over the same date range.""")
```

Amazon's (AMZN) current share price is $234.17, with a change of $0.95 and a percentage change of 0.4073%. The high price of the day was $235.797, the low price was $231.88, and the open price was $231.88. The previous close price was $233.22. This information is as of Mon Dec 1 11:37:16 2025.

Here is the candlestick data for Amazon (AMZN) for the past month, sorted in descending order by date:

| Date | Open | High | Low | Close | Volume |
|---|---|---|---|---|---|
| Fri Nov 28 00:00:00 2025 | $231.24 | $233.29 | $230.22 | $233.22 | 20,250,425 |
| Wed Nov 26 00:00:00 2025 | $230.74 | $231.75 | $228.77 | $229.16 | 38,497,719 |
| Tue Nov 25 00:00:00 2025 | $226.38 | $230.52 | $223.80 | $229.67 | 39,379,339 |
| Mon Nov 24 00:00:00 2025 | $222.56 | $227.33 | $222.27 | $226.28 | 54,318,223 |
| Fri Nov 21 00:00:00 2025 | $216.34 | $222.21 | $215.18 | $220.69 | 68,490,453 |
| Thu Nov 20 00:00:00 2025 | $227.05 | $227.41 | $216.74 | $217.14 | 50,308,862 |
| Wed Nov 19 00:00:00 2025 | $223.74 | $223.74 | $218.52 | $222.69 | 58,335,353 |
| Tue Nov 18 00:00:00 2025 | $228.10 | $230.20 | $222.42 | $222.55 | 60,608,442 |
| Mon Nov 17 00:00:00 2025 | $233.25 | $234.60 | $229.19 | $232.87 | 59,918,908 |
| Fri Nov 14 00:00:00 2025 | $235.06 | $238.73 | $232.89 | $234.69 | 38,956,619 |
| Thu Nov 13 00:00:00 2025 | $243.05 | $243.75 | $236.50 | $237.58 | 41,401,638 |
| Wed Nov 12 00:00:00 2025 | $250.24 | $250.37 | $243.75 | $244.20 | 31,190,063 |
| Tue Nov 11 00:00:00 2025 | $248.41 | $249.75 | $247.23 | $249.10 | 23,563,960 |
| Mon Nov 10 00:00:00 2025 | $248.34 | $251.75 | $245.59 | $248.40 | 36,476,474 |
| Fri Nov 7 00:00:00 2025 | $242.90 | $244.90 | $238.49 | $244.41 | 46,374,294 |
| Thu Nov 6 00:00:00 2025 | $249.15 | $250.38 | $242.17 | $243.04 | 46,004,201 |
| Wed Nov 5 00:00:00 2025 | $249.03 | $251.00 | $246.16 | $250.20 | 40,610,602 |
| Tue Nov 4 00:00:00 2025 | $250.38 | $257.01 | $248.66 | $249.32 | 51,546,311 |
| Mon Nov 3 00:00:00 2025 | $255.36 | $258.60 | $252.90 | $254.00 | 95,997,714 |

**Price Data Patterns and Correlation with News:**

Looking at the candlestick data for Amazon (AMZN) over the past month, several patterns emerge:

*   **Early November Surge and Mid-Month Dip:** The stock started November strong, reaching a high of $258.60 on Mon Nov 3 2025. This initial surge aligns with news from early November, where Amazon announced a significant $38 billion cloud computing services deal with OpenAI, which was seen as a major positive for its AWS segment and AI growth. Several articles from Nov 3rd and 4th highlight this deal and its positive impact on Amazon's stock.

    However, the price then experienced a noticeable dip, falling to a low of $215.18 on Fri Nov 21 2025. This decline coincides with news around Nov 13th-19th, where concerns about AI investment returns, potential market bubbles, and aggressive capital expenditures by tech giants were widely discussed. Articles from Nov 13th and 14th mention a tech stock selloff and Amazon's stock shedding market value. Additionally, news on Nov 19th highlighted Amazon selling shares of quantum computing and AI stocks (IonQ and AMD), potentially taking profits amid valuation concerns.

*   **Late November Recovery:** Towards the end of November, the stock showed signs of recovery, closing at $233.22 on Fri Nov 28 2025. This recovery aligns with a renewed positive sentiment around Amazon's AI initiatives and its strong position in e-commerce and cloud computing. News from Nov 25th-30th consistently highlights Amazon's strong AWS cloud computing business, its AI growth engine, and its potential to reach a $3 trillion market cap. Several articles also mention Amazon's legal victory in New York and its strong performance during Black Friday.

*   **Volume Fluctuations:** The trading volume was notably high at the beginning of November (95,997,714 on Nov 3rd) during the initial price surge, indicating strong investor interest. Volume remained relatively high during the mid-month dip, suggesting active trading during the period of uncertainty. Towards the end of the month, as the stock recovered, the volume was still substantial, but not as high as the initial surge.

In summary, Amazon's stock performance in November 2025 appears to be heavily influenced by news and sentiment surrounding its AI investments and cloud computing business. Initial excitement over a major OpenAI deal drove the stock up, while broader market concerns about AI valuations and Amazon's capital expenditures led to a mid-month correction. The stock then recovered as positive news about its AI growth engine, e-commerce strength, and legal victories re-emerged.

```python
send_message("What is Apple's ticker overview")
```

Apple Inc. (AAPL) is a technology company based in Cupertino, CA. Their address is ONE APPLE PARK WAY, CUPERTINO, CA, 95014, and their phone number is (408) 996-1010. Apple was listed on December 12, 1980. They have 166,000 employees and a market cap of $4,120,386,034,050.00. Their primary exchange is XNAS. Apple's description states: "Apple is among the largest companies in the world, with a broad portfolio of hardware and software products targeted at consumers and businesses. Apple's iPhone makes up a majority of the firm sales, and Apple's other products like Mac, iPad, and Watch are designed around the iPhone as the focal point of an expansive software ecosystem. Apple has progressively worked to add new applications, like streaming video, subscription bundles, and augmented reality. The firm designs its own software and semiconductors while working with subcontractors like Foxconn and TSMC to build its products and chips. Slightly less than half of Apple's sales come directly through its flagship stores, with a majority of sales coming indirectly through partnerships and distribution."

```python
send_message("What is Google's stock ticker symbol?")
```

Google is listed on the NASDAQ stock exchange under the ticker symbols **GOOGL** (Class A shares) and **GOOG** (Class C shares). These symbols now represent Alphabet Inc., Google's holding company.

Google is also listed on the Frankfurt Stock Exchange under the ticker symbol **GGQ1**.

```python
send_message("What is MGM Studio's stock symbol?")
```

I am unable to find the stock symbol for MGM Studios.

```python
send_message("What is MGM Studio's owner company stock symbol?")
```

MGM Studios is owned by Amazon, and Amazon's stock symbol is AMZN.

```python
send_message("What is Facebook's stock ticker symbol?")
```

Facebook's stock ticker symbol is META.

```python
send_message("""Compare Amazon's bullish versus bearish predictions from Oct 01 2025 until today. 
Include a discussion of recommendation trends, and sentiment analysis of news from the same dates. 
Discuss any patterns or correlations you find.""")
```

From October 1, 2025, until today, December 1, 2025, Amazon (AMZN) has consistently received a strong bullish outlook from analysts, while news sentiment has been more mixed, reflecting both significant growth opportunities and some operational challenges.

**Recommendation Trends (October 1, 2025 - December 1, 2025):**
Analyst recommendations for Amazon have been overwhelmingly positive throughout this period:
*   **October 1, 2025:** 52 "buy" recommendations, 3 "hold," and 23 "strongBuy."
*   **November 1, 2025:** 54 "buy" recommendations, 2 "hold," and 22 "strongBuy."
*   **December 1, 2025:** 52 "buy" recommendations, 5 "hold," and 21 "strongBuy."

Notably, there were no "sell" or "strongSell" recommendations during these months, indicating a consistently bullish sentiment from financial analysts.

**Sentiment Analysis of News (October 1, 2025 - December 1, 2025):**

**Bullish/Positive Sentiment:**
*   **AWS Dominance and AI Leadership:** Numerous articles highlight the accelerating growth of Amazon Web Services (AWS), Amazon's cloud computing division, with reported 20% year-over-year revenue increases. Significant investments in AI infrastructure, custom AI chips (Trainium, Inferentia), and strategic partnerships with companies like OpenAI (including a $38 billion cloud infrastructure deal) and Anthropic are consistently cited as major drivers for future growth and profitability. Amazon's role as a key player in the AI revolution and its potential to reach a $3-4 trillion market capitalization are frequently emphasized.
*   **E-commerce Strength and Efficiency:** Amazon's strong market share in e-commerce, improvements in operational efficiency through robotics and AI-driven logistics, and expanding delivery networks contribute to positive sentiment.
*   **Diversified Business Model:** The company's diverse revenue streams, spanning e-commerce, cloud computing, advertising, and emerging technologies like satellite internet, are seen as providing resilience and multiple avenues for growth.
*   **Analyst Confidence:** Many news pieces report positive analyst ratings, increased price targets (e.g., Wedbush raising to $340), and a general belief that Amazon is an attractive long-term investment.

**Bearish/Negative Sentiment:**
*   **Job Cuts and Restructuring:** Several articles report significant corporate layoffs, including up to 30,000 jobs and 15% of the HR staff. While sometimes framed as strategic restructuring for the AI era and cost-cutting measures, these are also viewed as indicators of potential workforce instability and operational challenges.
*   **High Capital Expenditures:** Concerns are raised about Amazon's aggressive capital expenditures in AI infrastructure (e.g., $125 billion planned investment), with some analysts questioning the immediate return on investment and potential impact on free cash flow.
*   **Competition and Market Share:** While a leader, Amazon faces intense competition in cloud computing (from Microsoft Azure and Google Cloud) and digital advertising (from Google and Meta). Some articles note instances where Amazon's stock has underperformed the broader S&P 500 or other "Magnificent Seven" stocks.
*   **Operational Issues:** A major global AWS outage due to a software bug was reported in late October, leading to negative sentiment regarding service reliability.
*   **Partnership Shifts:** UPS is strategically reducing its shipping volumes with Amazon due to lower margins, indicating a shift in that business relationship.

**Patterns and Correlations:**

1.  **AI as a Central Theme:** AI is the most prominent theme, acting as both a significant bullish catalyst and a source of some bearish concerns. The market is excited about Amazon's AI potential, particularly through AWS, but also watchful of the massive investments required and their impact on profitability and workforce.
2.  **AWS Performance is Key:** The performance and strategic moves of AWS are consistently highlighted as critical to Amazon's overall financial health and investor sentiment. Positive news about AWS directly correlates with bullish sentiment for the company.
3.  **Analyst Optimism vs. News Nuance:** There's a clear divergence between the consistently strong bullish analyst recommendations and the more nuanced, sometimes cautionary, tone of news articles. Analysts appear to be focusing on the long-term strategic advantages and growth potential, while news reports cover both the positive developments and the immediate operational challenges.
4.  **Market Concentration:** Amazon is frequently discussed within the context of the "Magnificent Seven" tech stocks, which have largely driven market performance. This highlights Amazon's systemic importance but also raises broader market concerns about concentration risk and potential overvaluation in the tech sector.

In conclusion, Amazon's bullish predictions are strongly supported by its leadership in cloud computing, aggressive AI investments, and diversified business model. Bearish sentiments are primarily linked to large-scale layoffs and the financial implications of massive AI capital expenditures. The overarching pattern is that the market views Amazon's strategic positioning in AI and cloud as a powerful long-term growth engine, despite short-term operational adjustments and competitive pressures.

```python
send_message("""Compare Google's bullish versus bearish predictions from Oct 01 2025 until today. 
Include a discussion of recommendation trends, and sentiment analysis of news from the same dates. 
Discuss any patterns or correlations you find.""")
```

Based on the analysis of analyst recommendations and news sentiment for Alphabet Inc. (GOOGL/GOOG) from **October 1, 2025, until today, December 1, 2025**, the overall prediction for the company is overwhelmingly **bullish**.

The market's confidence is driven almost entirely by the company's successful execution of its Artificial Intelligence (AI) strategy, which has translated into strong financial performance and strategic investments.

---

### 1. Recommendation Trends (Bullish vs. Bearish)

Analyst sentiment for Alphabet Inc. (GOOGL) remained highly bullish throughout the period, with a notable increase in conviction.

| Period | Strong Buy | Buy | Hold | Sell | Strong Sell | Total Bullish (Strong Buy + Buy) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Dec 1, 2025** | 20 | 43 | 10 | 0 | 0 | **63 (86.3%)** |
| **Nov 1, 2025** | 21 | 41 | 12 | 0 | 0 | **62 (83.8%)** |
| **Oct 1, 2025** | 21 | 39 | 13 | 0 | 0 | **60 (82.2%)** |

*   **Bullish Prediction:** The number of analysts recommending a **"Buy"** or **"Strong Buy"** increased from 60 to 63, raising the overall bullish percentage from 82.2% to 86.3%.
*   **Bearish Prediction:** There were **zero "Sell" or "Strong Sell"** recommendations in any month, indicating a complete absence of bearish conviction among major analysts. The slight decrease in total recommendations from November to December is due to a few analysts shifting from a neutral "Hold" rating to a more positive "Buy" rating.

---

### 2. Sentiment Analysis of News (October 1, 2025 – November 28, 2025)

News sentiment during this period was overwhelmingly positive, focusing on AI-driven growth and financial strength.

#### Bullish Drivers (Positive Sentiment)

The primary bullish narrative centers on Alphabet's AI leadership and financial execution:

*   **AI Dominance and Innovation:** The launch and success of the **Gemini 3 AI model** and its integration across Google Search, YouTube, and Google Cloud were consistently highlighted. News articles praised Alphabet's vertically integrated AI stack, including its custom **Tensor Processing Units (TPUs)**, which are seen as a cost-effective challenge to Nvidia's GPU dominance.
*   **Record Financial Performance:** The company reported its **first $100 billion quarterly revenue**, driven by strong growth in Google Services (advertising) and **Google Cloud (34% YoY growth)**. Analysts frequently noted the company's strong cash flow and relatively attractive valuation (low P/E ratio) compared to other "Magnificent Seven" stocks.
*   **Strategic Investor Confidence:** A major bullish catalyst was the disclosure of a **$4-5 billion investment by Warren Buffett's Berkshire Hathaway** in Q3, signaling confidence from a prominent value investor in Alphabet's long-term growth and stability.
*   **Massive Infrastructure Investment:** Alphabet announced significant capital expenditure plans, including a **$40 billion investment in Texas** by 2027 for cloud and AI infrastructure, and a **$6.4 billion expansion in Germany**, reinforcing its commitment to the AI race.

#### Bearish and Neutral Factors

The few negative or cautionary themes were generally overshadowed by the positive AI narrative:

*   **Competitive Threats:** The launch of **OpenAI's ChatGPT Atlas browser** caused a minor, short-term stock drop (approx. 2%), raising concerns about a potential challenge to Google's search and Chrome dominance. However, this was quickly mitigated by news of Google's own AI integration into Chrome.
*   **Regulatory/Legal Issues:** The company was named in a **NYC lawsuit over child social media addiction** (alongside Meta and Snap), and faced ongoing, though less prominent, geopolitical concerns about moving production out of China.
*   **Market Bubble Caution:** Several articles warned of a potential **"AI bubble"** or market overvaluation, but often positioned Alphabet as the "least overvalued" or a "safer" long-term AI play due to its diversified, profitable core business.

---

### 3. Patterns and Correlations

A clear and strong correlation exists between the news sentiment and analyst recommendations:

1.  **AI Success Drives Bullish Consensus:** The consistent stream of positive news regarding Alphabet's AI execution (Gemini, TPUs, Cloud growth) directly correlated with the increase in "Buy" ratings and the complete absence of "Sell" ratings. The market views Alphabet's AI strategy as a successful, revenue-generating endeavor, unlike competitors whose AI spending is sometimes viewed with skepticism (e.g., Meta's stock drop after announcing high AI CapEx).
2.  **Value and Growth Alignment:** The news frequently highlighted Alphabet's dual appeal as both a **high-growth AI leader** and a **value stock** (low P/E ratio). This combination attracted both growth investors (driven by AI) and value investors (like Buffett), creating a powerful, sustained bullish momentum that shrugged off minor competitive and regulatory risks.
3.  **Resilience to Disruption:** The pattern shows that while new competitors (like ChatGPT Atlas) can cause temporary stock dips, the market quickly reverts to focusing on Alphabet's core strengths: its massive cash flow, dominant search market, and profitable cloud business, all of which are being successfully fortified by AI.

```python
send_message("""How is the outlook for Apple based on trends and news sentiment from July 01 2025 until today? 
Perform the same analysis on all peers by sub-industry. Then compare Apple result to it's peers.""")
```

Here's an outlook for Apple and its sub-industry peers based on recommendation trends and news sentiment from July 1, 2025, until today, December 1, 2025:

**Apple (AAPL) Outlook:**

*   **Recommendation Trends:** As of December 1, 2025, Apple has a generally positive outlook from analysts, with 15 "Strong Buy" and 23 "Buy" recommendations, compared to 16 "Hold" and 2 "Sell" recommendations.
*   **News Sentiment (July 1, 2025 - December 1, 2025):**
    *   **Positive:** News highlights Apple's strong iPhone sales, particularly the iPhone 17 series, and the continued growth of its high-margin services segment. Strategic investments in AI (including partnerships with Google for Siri and MP Materials for rare earth magnets) and manufacturing diversification to India are seen as positive moves to mitigate risks and drive future growth. FDA approval for hypertension alerts on Apple Watch also contributes to a positive health tech narrative. Warren Buffett's continued, albeit sometimes trimmed, investment in Apple is also noted positively.
    *   **Neutral:** Several articles discuss Apple's stock trading near 52-week highs, prompting questions about its valuation and the pace of its AI strategy compared to competitors. Warren Buffett's trimming of his stake is viewed as a strategic portfolio adjustment rather than a negative signal about the company itself.
    *   **Negative:** Recurring themes include Apple's perceived lag in AI innovation compared to other tech giants, slower revenue growth in some areas, and ongoing regulatory pressures (antitrust lawsuits in India and the EU, and class-action lawsuits regarding Siri's AI capabilities). Some analysts predict that competitors with stronger AI strategies might surpass Apple's market capitalization.

**Apple's Sub-Industry Peers Outlook:**

Apple's sub-industry peers include companies involved in computer hardware, storage, and quantum computing. Here's a summary of their outlooks:

*   **Dell Technologies (DELL):**
    *   **Recommendation Trends:** Very positive, with 8 "Strong Buy" and 16 "Buy" recommendations.
    *   **News Sentiment:** Highly positive, driven by strong demand for AI servers, record AI server shipments, optimistic fiscal 2026 guidance, and strategic partnerships with Nvidia and Broadcom. Dell is seen as an undervalued AI infrastructure play, though some analysts note potential margin pressures from rising memory costs.
*   **Western Digital (WDC):**
    *   **Recommendation Trends:** Very positive, with 6 "Strong Buy" and 19 "Buy" recommendations.
    *   **News Sentiment:** Highly positive, recognized as a top S&P 500 performer in 2025 with significant stock returns and dividend increases. Strong demand for data storage from AI companies and expansion of its System Integration and Test (SIT) Lab for AI are key drivers.
*   **Hewlett Packard Enterprise (HPE):**
    *   **Recommendation Trends:** More balanced, with 6 "Strong Buy" and 7 "Buy" recommendations, alongside 13 "Hold."
    *   **News Sentiment:** Positive, following the successful $14 billion acquisition of Juniper Networks, which is expected to double its networking business and provide AI networking solutions. Collaborations on 5G and sovereign AI supercomputers are also positive. However, strategic restructuring costs have impacted profit margins.
*   **Pure Storage Inc - Class A (PSTG):**
    *   **Recommendation Trends:** Positive, with 7 "Strong Buy" and 13 "Buy" recommendations.
    *   **News Sentiment:** Positive, outperforming Nvidia in 2025 with strong annual recurring revenue growth and key clients in the AI sector.
*   **HP Inc (HPQ):**
    *   **Recommendation Trends:** More negative/hold, with 1 "Strong Buy" and 1 "Buy" against 16 "Hold" and 6 "Sell."
    *   **News Sentiment:** Mixed. While there are positive developments in AI-powered gaming hardware and sustainable products, the company has faced workforce reductions and missed revenue forecasts.
*   **NetApp Inc (NTAP):**
    *   **Recommendation Trends:** More balanced, leaning towards "Hold," with 3 "Strong Buy" and 10 "Buy" recommendations, and 14 "Hold."
    *   **News Sentiment:** Positive, aligning with Broadcom's quantum-safe SAN switch portfolio and focusing on infrastructure modernization and data protection.
*   **Super Micro Computer Inc (SMCI):**
    *   **Recommendation Trends:** Mixed to positive, with 4 "Strong Buy" and 10 "Buy" recommendations, but also 9 "Hold" and 3 "Sell."
    *   **News Sentiment:** Mixed. Positive sentiment stems from launching Nvidia Blackwell Ultra solutions, strong AI order backlogs, and institutional interest. However, negative sentiment arises from missing revenue expectations, stock declines due to weak guidance, and past fraud allegations.
*   **IonQ Inc (IONQ):**
    *   **Recommendation Trends:** Positive, with 2 "Strong Buy" and 10 "Buy" recommendations.
    *   **News Sentiment:** Highly speculative. While showing strong revenue growth and strategic acquisitions in quantum computing, it faces high valuations, significant net losses, and is considered a risky investment. Amazon notably sold its entire stake.
*   **Quantum Computing Inc (QUBT):**
    *   **Recommendation Trends:** Positive, with 2 "Strong Buy" and 5 "Buy" recommendations.
    *   **News Sentiment:** Highly speculative. Despite strong Q3 earnings and a substantial capital raise, the company has minimal sales, high operating expenses, and an expensive valuation. It's considered a high-risk investment.
*   **CompoSecure Inc-A (CMPO):**
    *   **Recommendation Trends:** Positive, with 2 "Strong Buy" and 8 "Buy" recommendations.
    *   **News Sentiment:** Positive, with plans for a business combination and ongoing management fee generation.

**Comparison of Apple to its Peers:**

*   **AI Leadership:** Many of Apple's peers, particularly Dell, Western Digital, Pure Storage, and Super Micro Computer, are seen as directly benefiting from and leading in the AI infrastructure and data storage boom. Apple, while making AI investments and partnerships, is often perceived as lagging in groundbreaking AI innovation compared to these specialized AI-focused companies.
*   **Growth Drivers:** Apple's growth is primarily driven by its established iPhone ecosystem and expanding services. Its peers are seeing significant growth from the broader AI revolution, data center expansion, and specialized technological advancements in areas like quantum computing and rare earth materials.
*   **Valuation & Risk:** Apple's valuation is a point of discussion, with some analysts questioning if it's justified given its slower AI progress. While some peers like Dell and Pure Storage are seen as undervalued, the quantum computing pure-plays (IonQ, QUBT) carry extremely high valuations and significant speculative risk, making them much riskier investments than Apple.
*   **Analyst Sentiment:** While Apple generally has a positive analyst sentiment, some of its peers, particularly Western Digital and Dell, show even stronger "Buy" recommendations, reflecting their more direct and impactful involvement in the current AI-driven market surge.

**Overall Conclusion:**

Apple's outlook is stable and positive, supported by its strong brand, loyal customer base, and growing services revenue. It is actively working to integrate AI into its ecosystem and diversify its manufacturing. However, it is currently perceived as playing catch-up in the AI race compared to some of its peers who are directly building the foundational AI infrastructure.

Many of Apple's peers, especially those in AI hardware and data storage, are experiencing more explosive growth and stronger positive sentiment due to the immense demand for AI technologies. The quantum computing peers, while highly speculative, represent a high-risk, high-reward segment of the tech industry.

In essence, Apple is a robust and profitable company with a solid future, but its growth trajectory is currently more measured compared to the rapid expansion seen in some of its more specialized, AI-centric peers.

```python
send_message("""What does the recent news say about Apple and the impact of tariffs? From 2025-09-01 up to today. 
Also locate candlestick data for the same dates. 
Discuss in detail any correlations in patterns between the candlestick and news data. Ignore duplicate news entry.""")
```

From September 1, 2025, to December 1, 2025, Apple's stock (AAPL) experienced a general upward trend, with some periods of volatility. The news during this period highlighted several factors, including the impact of tariffs, which showed a correlation with the stock's movements.

**Impact of Tariffs:**

*   **Negative Correlation:** News directly related to President Trump's tariff threats and Apple's reported tariff-related cost increases often coincided with periods of stock price decline or stagnation. For instance, on **October 10, 2025**, news broke about "Trump Shocks Markets: VIX Spikes 25%, S&P 500 Eyes Worst Day Since April," explicitly stating that Apple experienced a significant stock price decline due to renewed tariff threats against China. Similarly, on **November 18, 2025**, "The Stock Market Flashes a Warning as Investors Get Bad News About President Trump's Tariffs" reported Apple facing $1.1 billion in tariff-related cost increases, which could have contributed to downward pressure. On **October 26, 2025**, an article titled "Is Apple Going to Be Hit Hard by President Trump's Tariffs?" highlighted potential significant challenges from US-China trade tensions and rare earth element export restrictions.
*   **Positive/Mitigating Correlation:** Conversely, news detailing Apple's strategies to mitigate tariff impacts was often met with positive or neutral sentiment, potentially cushioning negative market reactions. For example, on **October 28, 2025**, "Top 3 Stocks Powering Through Trump’s Tariff Policies" noted that Apple successfully avoided arduous tariffs through strategic U.S. investments, relocated iPhone production, and achieved exemptions. This positive news could have contributed to a stock recovery after earlier tariff-related dips. Furthermore, Apple's strategic investments in rare earth materials, such as the $500 million investment in MP Materials for recycling facility development (reported on **October 31, 2025**, and **September 4, 6, 12, 30, November 2, 15, 17, 19, 26, 29, 30, December 1**), were seen as proactive measures to address supply chain risks stemming from China's export controls, which likely instilled investor confidence. The news on **September 17, 2025**, about Apple investing in Vietnam for supply chain diversification also falls into this category.

**Other Significant News and Candlestick Correlations:**

*   **Early September (around $225-$245):** The stock showed an upward trend, coinciding with several positive news items. Notably, favorable Google antitrust rulings (reported on **September 3, 4, 5, 7, 8, 9, 11, 12**) preserved Apple's significant annual revenue from Google, providing a strong positive impetus. News about Apple's AI future and strategic investments also contributed to this positive sentiment.
*   **Mid-September to Early October (fluctuating in $245-$260):** This period saw mixed news. While some reports indicated an "underwhelming" iPhone 17 launch (**September 12, 14, 15**) and concerns about Apple's AI progress (**September 28, October 8**), positive news about strong iPhone 17 pre-order demand in China (**September 22**) and positive analyst upgrades (**October 2**) helped to balance the sentiment, leading to fluctuating but generally stable prices.
*   **Mid-October to Early November (fluctuating in $255-$275):** This period included the negative tariff news mentioned above, which likely caused some dips. However, positive news about strong iPhone 17 sales (**October 23, 24, 30**) and Apple being a top holding in various ETFs (**October 14, 19, 22, 25, 27, 28, 29, 30, 31, November 2, 3, 4, 5, 8, 10, 11, 12, 14, 17, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, December 1**) indicated continued investor confidence.
*   **Late November to December 1 (upward trend towards $277-$279):** The stock showed a strong upward movement. This aligns with continued positive news regarding strong iPhone sales (**November 25, 28**), strategic partnerships, and Apple being a significant holding in various investment funds. Despite some negative news like new antitrust lawsuits in India and a class-action lawsuit over AI training (**November 27, 14**), the overall positive sentiment from product demand and strategic positioning seemed to drive the stock higher.

**In conclusion:** Apple's stock performance during this period was a complex interplay of various factors. While tariff-related news introduced volatility and sometimes downward pressure, Apple's proactive strategies to mitigate these risks, coupled with strong iPhone sales, favorable legal outcomes (like the Google antitrust case), and ongoing AI investments, generally contributed to a positive overall trend in its stock price. The candlestick data reflects these shifts in market sentiment, with dips often correlating with negative news and rallies aligning with positive developments.
