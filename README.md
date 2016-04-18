# Souce code for pinga-lab.org

[![Build Status](https://img.shields.io/travis/pinga-lab/website/master.svg?style=flat-square)](https://travis-ci.org/pinga-lab/website)
[![Powered by Urubu](https://img.shields.io/badge/powered_by-urubu-blue.svg?style=flat-square)](http://urubu.jandecaluwe.com/)

## Dependencies

You'll need to install Urubu and all it's dependencies to build the site. See
file `requirements.txt` for the complete dependency list. The build works on
Python 2.7 or Python 3.5.

You can create a conda environment with all required dependencies by running
`conda env create` in the root of the repository. To activate the environment
and run the build use `source activate pinga-site`.

## Compiling the site

Use the `Makefile`:

    make
    make serve

The command `make serve` will start a simple server at the `_build` dir
where the built HTML files are.
Point your browser to [http://127.0.0.1:8000](http://127.0.0.1:8000)
to view the site.
Use `Ctrl+C` to kill the server.

## The theme

The website theme is made using [bootstrap](http://getbootstrap.com/)
and tweaked from the Cosmo [Bootswatch](http://bootswatch.com/) theme.
Icons are provided by [FontAwesome](http://fontawesome.io/) and
[Academicons](http://jpswalsh.github.io/academicons/).
The Jinja2 templates and CSS are located in the `_layouts` and `css` folders.

## Adding a publication

The paper entries are `.md` files in the `papers` folder.
The site theme takes a lot of extra metadata in the post to make the "Info"
section of each entry.

To add a new entry, create the `.md` file in the corresponding folder.
Please, follow the naming conventions used for the other files.

### Metadata for entries

Required:

    title: Geophysical tutorial: Euler deconvolution of potential-field data
    author: Uieda, L., V. C. Oliveira Jr, and V. C. F. Barbosa
    date: yyyy-mm-dd
    journal: The Leading Edge
    doi: 10.1190/tle33040448.1
    citation: Uieda, L., V. C. Oliveira Jr, and V. C. F. Barbosa (2014), Geophysical tutorial: Euler deconvolution of potential-field data, The Leading Edge, 33(4), 448-450, doi:10.1190/tle33040448.1
    layout: publication

Note that `citation` has to be in a single line.

Optional:

    repository: pinga-lab/paper-tle-euler-tutorial
    supplement: 10.6084/m9.figshare.923450
    pdf: paper-tle.pdf
    oa: true
    inreview: true

* An entry with `oa: true` will be marked as open-acess.
* `inreview: true` will mark the entry as under peer-review (unpublished).
* `pdf` should be the name of PDF file in the `pdf` folder

## Adding a new member

Group member pages are the `.md` files in the `people` folder.
To add a new member, create the `.md` file in the corresponding folder with the
**last name** of the person (in lowercase).

### Metadata for entries

Required:

    title: Fulano de Tal
    date: yyyy-mm-dd
    position: PhD Student
    institution: Observatório Nacional
    location: Rio de Janeiro, Brasil
    layout: person

* Use the date that you started on the group.
* `position` should be one of: `PhD Student`, `MSc Student`, `Undergraduate
  Student`

Optional:

    lattes: http://lattes.cnpq.br/8939551682050504
    website: http://www.leouieda.com
    picture: uieda.jpg
    github: leouieda
    email: bla@on.br
    scholar: http://scholar.google.com.br/citations?user=qfmPrUEAAAAJ
    researcherid: G-3258-2012
    researchgate: https://www.researchgate.net/profile/Leonardo_Uieda
    orcid: 0000-0001-6123-9515

* `picture` should be the name of a square image in folder `images/pic`.


## Automatic deploy with TravisCI

The site is automatically built and deployed to
[leouieda/leouieda.github.com](https://github.com/leouieda/leouieda.github.com)
every time a commit is pushed to the *master* branch.
See files `.travis.yml` and `ci-tools/deply-gh-pages.sh`.

Inspired by
[Sleepy Coders](http://sleepycoders.blogspot.com.au/2013/03/sharing-travis-ci-generated-files.html)
and
[Mathieu Leplatre](http://blog.mathieu-leplatre.info/publish-your-pelican-blog-on-github-pages-via-travis-ci.html).

[![TravisCI status](http://img.shields.io/travis/leouieda/website.svg?style=flat)](https://travis-ci.org/leouieda/website)

## License

[![Creative Commons
License](https://i.creativecommons.org/l/by/4.0/88x31.png)](http://creativecommons.org/licenses/by/4.0/)
This work is licensed under a
[Creative Commons Attribution 4.0 International
License](http://creativecommons.org/licenses/by/4.0/).
