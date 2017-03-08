#!/bin/bash
# Based on
# http://sleepycoders.blogspot.com.au/2013/03/sharing-travis-ci-generated-files.html
# and https://github.com/richfitz/wood

REPO=pinga-lab/pinga-lab.github.io
REPO_URL=https://${GH_TOKEN}@github.com/${REPO}.git
BRANCH=master
CLONE_ARGS="--quiet --branch=$BRANCH --single-branch"

echo -e "Preparing to push the generated HTML to $REPO"
if [ "$TRAVIS_PULL_REQUEST" == "false" ] && [ "$TRAVIS_BRANCH" == "master" ]; then
    echo -e "Save the HTML files"
    cp -R _build $HOME/keep
    # Go to home and setup git
    cd $HOME
    echo -e "Configure git"
    git config --global user.email "leouieda@gmail.com"
    git config --global user.name "Leonardo Uieda"
    git config --global github.user "leouieda"
    echo -e "Clone $REPO"
    # Clone the project, using the secret token.
    # Uses /dev/null to avoid leaking decrypted key
    git clone $CLONE_ARGS $REPO_URL deploy > /dev/null
    cd deploy
    # Move the old branch out of the way and create a new one:
    git branch -m ${BRANCH}-old
    git checkout --orphan $BRANCH
    # Delete all the files and replace with our good set
    git rm -rf .
    cp -Rf $HOME/keep/. $HOME/deploy
    # add, commit and push files
    git add -f .
    git commit -m "Pushed by TravisCI build $TRAVIS_BUILD_NUMBER"
    echo -e "Push to $REPO"
    git push -fq origin $BRANCH > /dev/null
    echo -e "Uploaded generated files"
else
    echo -e "This is a pull request, no deploy"
fi
echo -e "Done"
