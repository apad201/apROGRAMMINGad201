#! /bin/bash
   
    elinks -dump "google.com/search?hl=en&q=weather+${1:-durham}" | sed -n '/Weather for/,${/Weather/{s/^ *//;s/-.*//;};/iGoogle/d;s/|.*//;p;/Humidity/q;}'







