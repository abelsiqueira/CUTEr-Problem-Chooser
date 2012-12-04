#!/bin/bash
# Copyright Raniere Gaia Costa da Silva - 2012
# Licensed under GNU GPL v.3
wget http://www.cuter.rl.ac.uk/Problems/mastsif.shtml -O mastsif.shtml
sed -nr 's/<tr> <td> <b> ([^\]+) <\/b> <\/td>/\1/p' mastsif.shtml > CUTEr_problems
sed -nr 's/<td> ([^\]+) <\/td> <\/tr>/\1/p' mastsif.shtml > CUTEr_classification
rm -f mastsif.shtml
