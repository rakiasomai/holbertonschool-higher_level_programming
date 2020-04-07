#!/bin/bash
# Script that displays the size of body response
curl -sI "$1" | grep Content-Length | cut -d " " -f2
