#!/bin/bash
# cURL only methods
curl -s --head "$1" | grep OPTIONS | cut --complement -d " " -f1