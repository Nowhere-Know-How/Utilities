#!/bin/bash
REPO_NAME=$1

## Check for game listed in `_config.yml`
LOWER_NAME=`echo "$REPO_NAME" | tr '[:upper:]' '[:lower:]'`
IN_MENU=`yq e '.menu.[] | .title == "'$REPO_NAME'"' _config.yml`

if echo $IN_MENU | grep -cq "true"
then
    echo "Game already listed."
else
    yq e '.menu += {"title": "'$REPO_NAME'", "url": "/'$LOWER_NAME'/"}' -i _config.yml
fi

## Check if markdown exists in `_featured_categories`


## Check if folder for game exists in `_posts`