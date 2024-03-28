#!/bin/bash
#This bash script display only body of a 200 status code response
curl -sf -L "$1" -X GET
