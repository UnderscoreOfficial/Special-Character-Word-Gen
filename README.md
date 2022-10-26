# Add Characters to Words

### Use Case

The goal of this was to solve a very niche use case I had were I wanted to practice typing special characters but, at best I only could find random ascii characters. I wanted to still retain some semblance of words while injecting the characters I wanted to learn in and next to those words leading to this project.

Aside from the uneventful name this script will take a random word from wordlist.txt randomly pick either 2 or 3 passes, each pass consisting of randomly picking a length to split the word and adding a random character from a array of characters, finally adding each of these words to a final string that will be printed out and optionally automatically copied to your clipboard.

### Setup

There are two default arrays one with numbers and another with special characters change the array variable to which ever array u want to use or to your own array. Change ammount_of_words to how many words you want to generate.

### Array Example

Just add each character you want to add in a array like below.

```
["!", "@", "#"]
```

### Optional Setup

Optionally install pyperclip to automatically copy output to your clipboard. The script will work with or without pyperclip, install pyperclip with pip if u want the added functionality.

```
pip install pyperclip
```
