# SCENE Kit

**Scientific Communication through Explanation, Narration and Evidence.**

[English](README.md) | **Português (Brasil)**

Instruções reutilizáveis para produzir vídeos acadêmicos com explicação do método, demonstrações, resultados rastreáveis e narração. O agente usa HyperFrames para a composição, FFmpeg para operações de mídia e, quando desejado, VoiceStudio para a voz.

Este é um kit de documentação e uma skill. Não contém artigos, gravações, exemplos de pesquisas reais ou um renderizador próprio.

## Qual arquivo faz o quê?

| Arquivo | Função |
|---|---|
| [README.md](README.md) / [README.pt-BR.md](README.pt-BR.md) | Instalação, dependências e início de um projeto. |
| [AGENTS.md](AGENTS.md) | Instruções permanentes para agentes que trabalham neste repositório. |
| [SKILL.md](.agents/skills/scene/SKILL.md) | Fluxo portátil, ativado por `$scene`. |
| [Guia de produção](.agents/skills/scene/references/production.md) | Direção visual, evidências, cortes, voz e verificação. |
| [Modelo de briefing](.agents/skills/scene/assets/BRIEF.template.md) | Informações específicas de cada vídeo. |

O nome convencional da skill é **`SKILL.md`, no singular**, dentro de sua própria pasta. `AGENTS.md` e uma skill se complementam: um orienta o repositório; a outra permite levar o processo para outros projetos. Consulte a documentação oficial de [AGENTS.md](https://developers.openai.com/codex/guides/agents-md/) e [skills](https://developers.openai.com/codex/skills/).

## O que instalar

| Componente | Necessidade | Obtenção e verificação |
|---|---|---|
| Agente de IA para programação | Ler o artigo, seguir a skill e executar ferramentas locais. | Use um agente já configurado com acesso a arquivos e terminal, como o [Codex](https://developers.openai.com/codex/). Os caminhos de descoberta deste kit seguem o Codex; outros clientes podem exigir outra pasta de skills ou a leitura explícita de `SKILL.md`. |
| Git | Versionar este kit. | [Git](https://git-scm.com/downloads); `git --version`. |
| Node.js 22 ou superior e npm | Executar HyperFrames. O perfil inicial deste kit usa Node 22. | [Node.js](https://nodejs.org/en/download); `node --version` e `npm --version`. |
| HyperFrames | Criar, visualizar e renderizar as composições. | Plugin do agente **ou** CLI standalone; veja abaixo. |
| FFmpeg e FFprobe | Cortar, recortar, inspecionar, montar e exportar mídia. | [FFmpeg](https://ffmpeg.org/download.html); `ffmpeg -version` e `ffprobe -version`. |
| Chrome/Chromium compatível com o HyperFrames | Visualização, snapshots e renderização de HTML. | Comece com `hyperframes doctor` usando a instalação escolhida e siga suas instruções de preparo do runtime. Se precisar de um navegador de sistema, use [Chrome](https://www.google.com/chrome/) ou o pacote Chromium da distribuição. Confirme a inicialização com `check`; ter um navegador aberto não basta. |
| Poppler (`pdftotext`) | Extrair texto quando o artigo chegar em PDF. | Pacote `poppler-utils` no Ubuntu/Debian; `pdftotext -v`. PDFs digitalizados podem precisar de OCR. |
| VoiceStudio | Opcional; recomendado para narração local por agente. | [Aplicativo Electron](https://github.com/debpalash/VoiceStudio/releases) e modelos escolhidos no aplicativo. Veja a seção de voz. |
| Plugin de percepção de vídeo | Opcional; facilita revisar gravações. | Instale `claude-video-vision` pelo catálogo compatível com seu agente e confira as ferramentas disponíveis. FFmpeg também permite extrair quadros. |
| Python 3 | Opcional; somente se o projeto exigir processamento adicional. | [Python](https://www.python.org/downloads/). Este kit não exige pacotes Python. |

HyperFrames documenta [Node.js 22+ e FFmpeg como requisitos](https://github.com/heygen-com/hyperframes/blob/main/packages/cli/README.md). O perfil standalone abaixo fixa **HyperFrames 0.8.177**, para evitar variações silenciosas. Isso não significa que seja a versão mais recente. Atualizações devem ser verificadas antes de alterar o perfil.

No Ubuntu/Debian, os utilitários de sistema podem ser instalados com:

```bash
sudo apt update
sudo apt install git ffmpeg poppler-utils
```

Instale Node pelo distribuidor oficial ou por um gerenciador de versões. Se já usa `nvm`, execute na raiz deste kit:

```bash
nvm install
nvm use
node --version
npm --version
```

O arquivo `.nvmrc` seleciona a linha 22. Executar `nvm install` pressupõe que o próprio `nvm` já esteja instalado; essa etapa está nas [instruções oficiais de instalação](https://github.com/nvm-sh/nvm#installing-and-updating).

### HyperFrames: escolha uma instalação

**Plugin do agente:** instale HyperFrames pelo gerenciador de plugins compatível com o agente e carregue a skill de entrada `hyperframes`. Use o launcher e a versão definidos pelo plugin instalado. Não execute comandos standalone para atualizar suas skills nem copie diretórios de cache de outra máquina.

**Standalone:** os comandos a seguir usam a versão explícita e podem baixar esse pacote do npm. Execute-os na raiz deste kit:

```bash
mkdir -p work
npx --yes hyperframes@0.8.177 init work/my-video --non-interactive
mkdir -p work/my-video/input/recordings
cp .agents/skills/scene/assets/BRIEF.template.md work/my-video/BRIEF.md
```

O scaffold pode consultar ou instalar skills externas; confira o que a versão escolhida oferece. Não instale um segundo conjunto quando já usa o plugin. Dentro de `work/my-video`, use o fluxo da instalação escolhida. No modo standalone:

```bash
cd work/my-video
npx --yes hyperframes@0.8.177 doctor
npx --yes hyperframes@0.8.177 preview --background
npx --yes hyperframes@0.8.177 preview --status
npx --yes hyperframes@0.8.177 check --json
```

Depois de revisar a prévia, renderize e inspecione o arquivo. Consulte `render --help` para as opções de saída da versão instalada:

```bash
mkdir -p renders
npx --yes hyperframes@0.8.177 render -o renders/review-v01.mp4
ffprobe -v error -show_streams -show_format -of json renders/review-v01.mp4
```

Mantenha a prévia disponível durante a revisão; encerre com `preview --stop` quando terminar. Prefira a [documentação e a ajuda da versão instalada](https://github.com/heygen-com/hyperframes/blob/main/docs/packages/cli.mdx) a flags lembradas de outra versão.

### Voz: VoiceStudio

1. Instale e abra o aplicativo Electron. Para uso normal de narração, não é necessário compilar seu código-fonte.
2. Escolha o motor de fala e instale o modelo necessário no aplicativo. Transcrição pode exigir outro modelo. GPU, memória e espaço dependem dessa escolha; não existe uma exigência única de hardware para todas as vozes.
3. Em **Integrations**, exporte a configuração MCP para seu agente. O endereço padrão é `http://127.0.0.1:3900/mcp/`; respeite a porta e a autenticação da instalação.
4. Verifique `check_health`, liste vozes e personalidades e gere uma amostra curta antes da narração completa. Use a skill `voicestudio` para produção de áudio; `voicestudio-maintainer` trata manutenção do aplicativo.
5. Guarde um perfil de voz estável e seus parâmetros no projeto local. Use voz sintética original ou uma referência autorizada.

Se a skill de áudio ainda não estiver disponível, o VoiceStudio documenta este comando de instalação para agentes compatíveis. Escolha `voicestudio` para produção e confira as opções de destino do instalador; não substitua um plugin que já funciona:

```bash
npx skills add debpalash/VoiceStudio
```

Consulte o [guia do aplicativo](https://github.com/debpalash/VoiceStudio#readme) e a [documentação MCP](https://github.com/debpalash/VoiceStudio/blob/main/docs/mcp.md). A API e as ferramentas evoluem: descubra o contrato da versão em execução. Um nome de modelo em catálogo não comprova que seus arquivos estejam instalados.

Não presuma que `instruct` aceite uma descrição livre: alguns motores aceitam apenas atributos enumerados. Liste as opções disponíveis. Prefira arquivos ou recursos MCP para transferir áudio, evitando despejar base64 na conversa. Entradas por caminho dependem da pasta permitida pelo servidor; não altere essa configuração para contornar uma recusa.

## Criar o próximo vídeo

Clone ou baixe este kit e abra sua raiz no agente. Os comandos standalone acima pressupõem esse diretório inicial.

1. Abra este repositório no agente; ele encontrará `AGENTS.md` e a skill local. Se acabou de instalar a skill, abra uma nova sessão para conferir sua descoberta.
2. Crie um projeto em `work/`, copie o briefing e preencha público, objetivo, materiais, idioma, duração e versão anônima ou pública.
3. Coloque os materiais reais apenas no projeto de trabalho. Registre a origem das métricas e os trechos utilizáveis das gravações.
4. Use o prompt abaixo. O agente deve ajustar roteiro, duração e montagem aos materiais recebidos, seguindo o guia de produção.
5. Revise imagens, números e voz no MP4 final. Identifique claramente o arquivo aprovado.

```text
Use $scene para produzir o vídeo descrito em work/my-video/BRIEF.md.
Leia o artigo e inspecione as gravações fornecidas antes de montar o roteiro.
Explique o método com SVGs e apresente as demonstrações e métricas indicadas.
Ajuste a narração às durações reais, usando o perfil visual do briefing.
Entregue o projeto editável, o MP4 e o registro das verificações realizadas.
```

Perfil visual inicial, ajustável: 1920×1080 a 30 fps; fundo preto; tipografia clara; animações SVG que explicam o método; demonstrações com tempo suficiente; métricas legíveis; narração em inglês com ritmo medido. Voz masculina é uma preferência inicial, não uma exigência para todos os artigos.

Não há duração fixa de um minuto. O tempo necessário para explicar e observar os experimentos orienta o roteiro.

## Exemplos de uso

Estes são prompts genéricos para um projeto em `work/my-video/`. Substitua os nomes de arquivos e os locais das fontes pelos materiais fornecidos. Eles descrevem um fluxo de trabalho, não um estudo existente, e não contêm valores medidos de pesquisas. Mantenha entradas e saídas específicas do projeto dentro de `work/`, excluída do Git.

### 1. Criar um vídeo acadêmico completo

```text
Use $scene. Leia work/my-video/input/paper.pdf e inspecione as gravações em
work/my-video/input/recordings/. Use o briefing como fonte das decisões do projeto.
Crie um vídeo acadêmico em inglês com fundo preto e tipografia clara.
Explique o método com SVGs e depois apresente as demonstrações e resultados pedidos.
Reserve tempo para observar os experimentos, sem impor o limite de um minuto.
Prepare o storyboard, gere uma amostra de voz masculina com ritmo medido e siga
o fluxo do HyperFrames instalado até a revisão e a exportação. Mantenha o trabalho local.
```

### 2. Seguir uma referência visual

```text
Inspecione work/my-video/input/reference-video.mp4 antes de propor a direção visual.
Use como referência seu ritmo, hierarquia tipográfica e cartelas acadêmicas discretas.
O conteúdo científico deve vir do artigo e das gravações fornecidos.
Siga o modo de divulgação do briefing para decidir quais identificações podem aparecer.
```

### 3. Melhorar as ilustrações do método

```text
Valide cada animação do método contra as equações e a arquitetura do artigo.
Mostre cada mecanismo se ativando por uma mudança clara de estado no SVG.
Confira limites dos blocos, setas, marcadores, rótulos e significado das equações.
Preserve os vídeos e as cenas de métricas que já foram aceitos.
```

### 4. Escolher uma gravação melhor e integrar os resultados

```text
Use apenas work/my-video/input/recordings/experiment-b.mp4 no experimento real.
Retire a câmera anterior e não repita o mesmo voo ou ensaio duas vezes.
Apresente essa gravação pela primeira vez ao lado do painel de resultados agregados.
Corte a preparação e o encerramento, inclusive decolagem ou pouso se forem irrelevantes.
Se um tracejado ajudar, identifique-o como anotação 2D, e não como posição de referência medida.
```

### 5. Adicionar uma visualização qualitativa da simulação

```text
Use work/my-video/input/recordings/simulation-overview.mp4 somente como visualização.
Mantenha a ida até o checkpoint e retire o trecho de retorno.
Recorte as janelas do simulador e do visualizador para remover bordas e áreas do desktop.
Mantenha as duas vistas sincronizadas a partir dos mesmos quadros. Não adicione métricas.
```

### 6. Adicionar simulação com métricas antes dos resultados reais

```text
Adicione work/my-video/input/recordings/simulation-benchmark.mp4 antes dos resultados reais.
Coloque a gravação ao lado de um painel de métricas. Extraia apenas os valores do
método proposto na tabela de benchmark indicada no briefing, sem comparações com outros métodos.
Preserve unidades, número de execuções, agregação, incerteza e localização das fontes.
Inclua narração em inglês explicando o que observar e como interpretar os valores.
Desloque as cenas seguintes, legendas, narração e encerramento pela duração adicionada.
```

### 7. Melhorar a narração sem acelerar

```text
Revise o arquivo exato work/my-video/renders/review-v03.mp4 e meça suas pausas.
Use a voz masculina selecionada com articulação mais clara e ritmo mais pausado.
Acrescente informações úteis do artigo além do que já está escrito na tela.
Mantenha pausas curtas de observação e preencha vazios involuntários, especialmente nas demos.
Meça os novos takes e regenere ou reescreva os que ultrapassarem seu tempo, sem acelerá-los.
Confira os números por transcrição e a naturalidade por escuta; informe verificações indisponíveis.
```

### 8. Preparar uma versão anônima para revisão

```text
Prepare uma versão anônima para revisão por pares.
Remova nomes, afiliações, marcas institucionais, links identificadores e créditos
das cenas ativas, cartelas, legendas, voz, detalhes visíveis do desktop e metadados.
Mantenha o título e a explicação científica. Preserve o método e os vídeos já aceitos.
Inspecione o MP4 final e identifique o arquivo de submissão separadamente dos anteriores.
```

Nas revisões seguintes, indique o arquivo exato e a cena, descreva a mudança pedida e diga quais partes aceitas devem ser preservadas. Isso dá ao agente um alvo concreto de revisão, em vez de uma instrução ambígua para editar o último vídeo.

### Levar a skill para outro repositório

Copie a pasta completa `.agents/skills/scene/` para `.agents/skills/` no outro projeto, preservando `references/`, `assets/` e `agents/`. Para disponibilizá-la ao usuário em outros repositórios, o Codex também admite skills em `~/.agents/skills/`. Confira os caminhos na documentação oficial da versão usada.

Não é necessário instalar novamente HyperFrames ou VoiceStudio se já estiverem funcionando. Esta skill define a direção editorial; as skills desses produtos definem seus contratos técnicos.

## O que deve ficar no projeto de trabalho

Além dos arquivos gerados pelo HyperFrames, mantenha:

- `BRIEF.md`: decisões específicas do vídeo, incluindo identificação ou anonimato.
- `STORYBOARD.md`: cenas, duração, função de cada demonstração e posição das métricas.
- `CLAIMS.md`: afirmações e valores, com tabela, figura, página ou fonte correspondente.
- `assets/`: cópias locais dos derivados, com recortes e origem registrados.
- `voiceover/`: roteiro, perfil e parâmetros de voz, takes e alinhamento medido.
- `validation.md`: o que foi verificado, o que falhou e eventuais limitações.
- O arquivo MP4 aprovado, com nome inequívoco.

## Problemas que merecem atenção

| Sintoma | Como proceder |
|---|---|
| Node incompatível | Confirme o executável no terminal do agente, ative a versão correta e repita a verificação. |
| Chrome não inicia ou porta local recusada | Registre o erro real e corrija runtime/permissões disponíveis. Não declare que `check` passou quando o navegador foi ignorado. |
| Renderizador indisponível | FFmpeg pode cortar, montar ou trocar áudio de cenas já renderizadas. Ele não renderiza animações HTML/GSAP. Descreva precisamente qualquer montagem alternativa. |
| CLI HTTP falha, mas MCP responde | Use o transporte MCP conectado. Não conclua que o aplicativo está indisponível apenas por uma chamada HTTP recusada. |
| Vídeo tem longos espaços sem fala | Meça os intervalos; acrescente explicações sustentadas pelo artigo ou redistribua as falas, preservando pausas úteis de observação. |
| Voz rápida, artificial ou variável | Revise uma amostra, use o mesmo perfil e reescreva/regere os trechos. Um multiplicador de velocidade não garante a mesma cadência em vozes diferentes. |
| Transcrição parece correta | Isso verifica conteúdo reconhecido; não comprova naturalidade, pronúncia ou sincronização visual. Escute o áudio final. |

## Manter este kit compartilhável

`work/` está excluída do Git para os projetos de produção. Também são ignorados formatos comuns de artigos, imagens, áudios e vídeos, caches e configurações locais. Essas exclusões ajudam a evitar inclusões acidentais; não substituem revisar os arquivos antes de enviar um repositório.

Versione apenas instruções e modelos genéricos. Antes de publicar, confira `git status`, os arquivos preparados para commit e o histórico. Este kit não configura remotos nem publica conteúdo automaticamente.

As referências externas pertencem aos respectivos projetos; suas licenças e requisitos de distribuição são independentes deste kit.
