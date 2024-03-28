#!/bin/bash
#This bash script sends a DELETE request to the URL passed
curl -sf -L "$1" -X DELETE
