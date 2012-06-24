# Qingwen

Translate the output from the
[Qingwen](http://karanmisra.com/qingwen/Qingwen.html)
dictionary to a tab delimited format that can be read by
[ProVoc](http://www.arizona-software.ch/provoc/).

## Managing word lists in Qingwen

1. Create a word list, by pressing the '+' icon from the Word Lists
tab.

2. As you find words you want to remember, add them to a list in
Qingwen. This can be done from the '+' icon on the word definition
page.

3. From the Word Lists tab, press the icon in the top left. Then
select the list you want to export, and choose Export from the
options.

4. Save the resulting email on your computer somewhere, as a UTF-8
text file (eg. words.txt).

5. Convert the file to tab delimited:

      python qingwen.py words.txt output.txt

6. In ProVoc, open the vocabulary file (or create a new one with
Chinese and English as the language pairs), then select
File->Import... and choose the output.txt file.

7. You can optionally export from ProVoc to iVocabulary on the iPhone.


# Generate output

    python qingwen.py data/example.txt output.txt

# Running tests

    PYTHONPATH=. py.test -f test/test.py


