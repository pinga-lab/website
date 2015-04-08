# Código para o site pinga-lab.org

[![Build Status](https://img.shields.io/travis/pinga-lab/website/master.svg?style=flat-square)](https://travis-ci.org/pinga-lab/website)
[![Powered by Pelican](https://img.shields.io/badge/powered_by-pelican-blue.svg?style=flat-square)](http://getpelican.com/)
[![Powered by Bootstrap](https://img.shields.io/badge/powered_by-bootstrap-blue.svg?style=flat-square)](http://getbootstrap.com/)
[![Theme by Bootswatch](https://img.shields.io/badge/theme_by-bootswatch-blue.svg?style=flat-square)](http://bootswatch.com/)

Este repositório contem o código fonte para compilar o site.
O site é gerado pelo sistema [Pelican](http://docs.getpelican.com/).
Ele converte os arquivos escritos em formato
[Markdown](https://guides.github.com/features/mastering-markdown/)
(os `.md` na pasta `content`)
para HTML usando o nosso template.

## Contribuindo

### Preparação

Primeiro, faça um fork desse repositório para sua própria conta.
Depois, clone o repositório para seu computador:

    git clone https://github.com/SEU_NOME/website

Quando terminar de clonar, entre na pasta do repositório e inicie o
[submodule](http://git-scm.com/docs/git-submodule) com os plug-ins do Pelican:

    cd website
    cd pelican-plugins
    git submodule init
    git submodule update

Isso só precisa ser feito uma vez.

Agora você vai precisar instalar os requisitos para compilação:

* Pelican (3.5.0)
* markdown (2.4)
* pillow
* beautifulsoup4 (4.3.2)

Instale essas bibliotecas usando o `pip`:

    pip install pelican==3.5.0 markdown==2.4 pillow beautifulsoup4==4.3.2

Agora você está pronto para fazer as suas mudanças no site.
Primeiro, crie um branch para você trabalhar:

    git checkout -b NOVA_COISA_LEGAL

### Compilando o site

> **Para os que usam Windows:** Você vai precisar do programa "make". Para
> instalá-lo, vá até [msysgit.github.io](http://msysgit.github.io/). Não clique
> no primeiro botão de "download" no topo da página. Use o link no final que
> diz "download msysGit". Na hora de instalar, tenha certeza que de que a opção
> de instalar o Make está selecionada (se ela existir).

Entre no repositório e use o `Makefile` para compilar o HTML do site.
Rode:

    make

para compilar os arquivos fonte (os `.md` na pasta `content`) para HTML. O
resultado é colocado na pasta `output`.

Para ver o site que você acabou de compilar, rode:

    make serve

O comando `make serve` iniciará um servidor local na pasta `output`.
Abra um navegador e vá para [http://127.0.0.1:8005](http://127.0.0.1:8005)
para visualizar o site.
Use `Ctrl+C` para interromper o servidor.

### Alterando a sua página pessoal

Cada membro do grupo recebe uma página pessoal. O arquivo fonte dessa página
está na pasta `content/people`. Por exemplo, o arquivo que gera
[pinga-lab.org/people/oliveira-jr.html](http://www.pinga-lab.org/people/oliveira-jr.html)
é `content/people/oliveira-jr.md`. Os arquivos Markdown tem um cabeçalho que
define informações da pessoa e depois algum texto fornecido por cada um (ou
copiado do Currículo Lattes).

O cabeçalho do arquivo segue a seguinte forma:

    title: Vanderlei C. Oliveira Jr.
    date: 01-01-2009
    slug: oliveira-jr
    lattes: http://lattes.cnpq.br/4332841435949533
    picture: oliveira-jr.jpg
    email: vanderlei@on.br
    github: birocoles
    scholar: http://scholar.google.com.br/citations?user=TQbQ4TcAAAAJ
    researcherid: E-1871-2013
    researchgate: https://www.researchgate.net/researcher/2021325258_Vanderlei_C_Oliveira_Jr/
    orcid: 0000-0002-6338-4086
    institution: Observatório Nacional
    location: Rio de Janeiro, Brazil
    position: Researcher

Os campos que são obrigatórios são:

* `title` (nome da pessoa)
* `date` (data aproximada que entrou no grupo)
* `slug` (deve ser igual ao nome do arquivo `.md`)
* `position` (o "cargo" da pessoa)

Os demais são optativos e usados para preencher as informações no quadro "Info"
da página.

Para colocar uma foto no seu perfil (ou trocar a atual), coloque a imagem na
pasta `content/images/pic`. Coloque o nome do arquivo igual ao no do arquivo
`.md` da sua página (ex `oliveira-jr.jpg`).
Não há limite para a resolução mas a **imagem deve ser quadrada**.

Abaixo do cabeçalho, escreva o que quiser usando Markdown. Não use `#` para
seções (reservado para o nome da pessoa).
Comece suas seções com `##` (que é convertido em um `<h2>` em HTML).

### Incluindo um novo artigo

Os códigos fonte dos artigos estão na pasta `content/papers`.
Cada artigo recebe um `.md` com suas informações.
A lista de artigos e a lista de artigos recentes na primeira página são gerados
automaticamente.

Para incluir um artigo novo, crie um arquivo `.md` na pasta `content/papers`.
**O nome deve começar com `paper-` e deve conter somente letras minúsculas**.
**Não use pontos, espaços, acentos, etc**.

O cabeçalho é parecido com o da página pessoal. Por exemplo:

    title: Robust 3D gravity gradient inversion by planting anomalous densities
    author: Uieda, L. and V.C.F. Barbosa
    date: 01-07-2012
    slug: paper-planting-anomalous-densities-2012
    pdf: paper-planting-anomalous-densities-2012.pdf
    repository: pinga-lab/paper-planting-densities
    doi: 10.1190/geo2011-0388.1
    journal: Geophysics
    supplement: 10.6084/m9.figshare.91574
    citation: Uieda, L., and V. C. F. Barbosa (2012), Robust 3D gravity gradient inversion by planting anomalous densities, Geophysics, 77(4), G55-G66, doi:10.1190/geo2011-0388.1

Os campos necessários são:

* `title`
* `author`
* `date` (data de publicação do artigo)
* `slug` (deve ser igual ao nome do arquivo `.md`)
* `journal`
* `citation` (citação completa do artigo, de preferência usando o formato da AGU. **Deve ser colocada em 1 linha só**)

Campos que são altamente recomendados:

* `doi` (o DOI do artigo publicado)

Para incluir um PDF do artigo, coloque-o na pasta `content/pdf`. O PDF deve ter
o mesmo nome que o arquivo `.md`. Inclua o nome do arquivo no cabeçalho, ex
`pdf: paper-planting-anomalous-densities-2012.pdf`.

Para indicar que um artigo é de acesso livre (open access), inclua o campo
`tags: OA`.
**Não inclua um PDF para artigos de acesso livre (open access).**
O PDF já é gratuito na página da revista.

Se o artigo está em revisão (ainda não foi publicado), indique isso colocando o
campo `tags: review`. Esse argumento pode ser combinado com o de acesso livre,
ex `tags: review, OA`.

Para artigos com material suplementar no [figshare](http://figshare.com/)
ou [Zenodo](http://zenodo.org/), coloque o DOI no campo `supplement`.

Depois do cabeçalho, inclua o abstract do artigo e, se possível, o código
BibTex da citação.

### Faça um Pull Request

Depois de fazer suas mudanças, faça um commit:

    git add ARQUIVO_MUDADO1 ARQUIVO_MUDADO2
    git commit

Mande suas modificações locais para o GitHub:

    git push

Depois, entre em https://github.com/pinga-lab/website/pulls e clique em "New
pull request".
Escolha para "base" o branch *master* ("pinga-lab/master") e como "compare" o
seu branch no seu fork.

## Atualização automática usando TravisCI

Este site é compilado automaticamente quando um novo *commit* é empurrado para
o branch *master*.
Assim, quando seu Pull Request for aceito e incorporado o site será atualizado
automaticamente.

Veja os arquivos `.travis.yml` e `.update-website.sh`.
Inspirado nas mágicas por
[Sleepy Coders](http://sleepycoders.blogspot.com.au/2013/03/sharing-travis-ci-generated-files.html)
e
[Mathieu Leplatre](http://blog.mathieu-leplatre.info/publish-your-pelican-blog-on-github-pages-via-travis-ci.html).

## License

[![Creative Commons
License](https://i.creativecommons.org/l/by/4.0/88x31.png)](http://creativecommons.org/licenses/by/4.0/)
This work is licensed under a
[Creative Commons Attribution 4.0 International
License](http://creativecommons.org/licenses/by/4.0/).

