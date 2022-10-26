# Add Characters to Words

### Use Case

The goal of this was to solve a very niche use case I had were I wanted to practice typing special characters but at best I only could find random ascii characters. I wanted to still retain some semblance of words while injecting the characters I wanted to learn into and around normal words which lead to this project.

Aside from the uneventful name this script will take a random word from wordlist.txt randomly pick either 2 or 3 passes, each pass consisting of randomly picking a length to split the word and adding a random character from a array of characters, finally adding each of these words to a final string that will be printed out and optionally, automatically copied to your clipboard.

### Setup

There are two default arrays one with numbers and another with special characters change the array variable to which ever array u want to use or to your own array. Change ammount_of_words to how many words you want to generate.

### Array Example

Add the characters you want in a array like the example below.

```
["!", "@", "#"]
```

### Optional Setup

Optionally install pyperclip to automatically copy output to your clipboard. The script will work with or without pyperclip, install pyperclip with pip if u want the added functionality.

```
pip install pyperclip
```

### Example Output

Using special_array

```
b}\e@sid v|ote me=dicines b%el_ cat(]alog re{spectiv< {:fo> .]ma :incid{ent \p'lu oxy:ge/ di=sc con%sult:a#n <chri$>stiani (universa) reve'r+s kis>-si; ^n%ic a)n) d!igest t>e!" [=;e s."ak ns"- a"/ssemb$ sim+il]{ar accur,at- "-_i s@]uperio $a|; c"*entur bubble< sh_^_ th?e ref!er'rin }ba-lanc hu,nt f.o| q(t$ m}yr$t$ mode^r/ato \>!ze a'r.m abst%rac| &publi\sh&e m]it'chel %b_r win$_te en^abl;e
```
