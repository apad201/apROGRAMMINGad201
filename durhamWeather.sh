#!/bin/bash

# only works in X11, not in Terminal
  
 elinks -dump "google.com/search?hl=en&q=weather+${1:-durham}" | \
 grep "Images\s\+-\?\d\+"

# sed -n '/Weather for/,${/Weather/{s/^ *//;s/-.*//;};/iGoogle/d;s/|.*//;p;/Humidity/q;}'
