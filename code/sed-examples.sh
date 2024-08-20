#!/bin/bash
cat << EOF
---
REPLACE SED -> Stream Editor:
EOF
set -x
sed "s/SED/Stream Editor/g" sample.txt
set +x

cat << EOF
---
DELETE lines with "example"
EOF
set -x
sed "/example/d" sample.txt
set +x

cat << EOF
---
INSERT a line before "Let's"
EOF
set -x
sed "/^Let's/i\\
tHIS IS AN INSERTED LINE." sample.txt
set +x


# THESE ARE NOT WORKING (GPT3.5's hallucination)! :(
#sed '/powerful/a\\
#This is an appended line.' sample.txt
#sed "3c\
#  This is the new third line." sample.txt

