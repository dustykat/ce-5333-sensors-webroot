#!/bin/bash
# shell script to read sync_time_file.txt
# run on a remote either by chron 
read string < sync_time_file.txt
date -s "$string"
