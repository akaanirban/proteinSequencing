# Manisit's protein sequencing stuff

Edit the `sequenceFile.conf` by adding sequences in newlines in the following order:

`sequence_name=actual_sequence` , for example a sample content in `sequenceFile.conf` might look like the following:

`sequence1=MTEYKLVVVGAGGVGKSALTIQLIQNHFVDEYDPTIEDSYRKQVVIDGETCLLDILDTAGQEEYSAMRDQYMRTGEGFLCVFAINNTKSFEDIHHYREQIKRVKDSEDVPMVLVGNKCDLPSRTVDTKQAQELARSYGIPFIETSAKTRQGVDDAFYTLVREIRKHKEKMSKDGKKKKKKSRTRCTVM
sequence2=MTEYKLVVVGAGGVGKSALTIQLIQNHFVDEYDPTIEDSYRKQVVIDGETCLLDILDTAGQEEYSAMRDQYMRTGEGFLCVFAINNTKSFEDIHHYREQIKRVKDSEDVPMVLVGNKCDLPSRTVDTKQAQDLARSYGIPFIETSAKTRQRVEDAFYTLVREIRQYRLKKISKEEKTPGCVKIKKCIIM`

Then go in the `possible_combinations.py` and look at line 40 : 
```python
validAlphabet = 'GALMFWKQESPVICYHRNDT'
```
to check if the valid alphabets character us correct. Change if necessary.

Run the file in windows as:
```
python possible_combinations
```
or in Ubuntu:
```
python3 possible_combinations
```

This will generate one text file and one CSV file for two sequences each. Names are self explanatory. The files will be inside `Outputs` directory.

## Change-log:
1. All combination strings now produced would be unique.
2. Outputs are now in `Outputs/` folder.

### N.B. the latest protein added is 
Sequence3 --> Protein name: p53 CCDS48826.1 NCBI
MTAMEESQSDISLELPLSQETFSGLWKLLPPEDILPSPHCMDDLLLPQDVEEFFEGPSEALRVSGAPAAQDPVTETPGPVAPAPATPWPLSSFVPSQKTYQGNYGFHLGFLQSGTAKSVMCTYSPPLNKLFCQLAKTCPVQLWVSATPPAGSRVRAMAIYKKSQHMTEVVRRCPHHERCSDGDGLAPPQHLIRVEGNLYPEYLEDRQTFRHSVVVPYEPPEAGSEYTTIHYKYMCNSSCMGGMNRRPILTIITLEDSSGNLLGRDSFEVRVCACPGRDRRTEEENFRKKEVLCPELPPGSAKRALPTCTSASPPQKKKPLDGEYFTLKIRGRKRFEMFRELNEALELKDAHATEESGDSRAHSSLQPRAFQALIKEESPNC -- 381 characters