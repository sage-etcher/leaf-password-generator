# password-generator
Just a quick simple password generator, for personal use

# Using the password-generator
```
python genpass.py [arguements]
```

| Arguement | Description |
|:--------- |:----------- |
| `length=[int]` | password length. |
| `count=[int]` | number of passwords to generate. |
| `upper=[bool]` | use upper case letters? true or false |
| `lower=[bool]` | use lower case letters? true or false |
| `numeric=[bool]` | use numbers? true or false |
| `special=[bool]` | use special character? true or false |

# Example
If I wanted to generate 5 passwords, each password 20 characters long, containing just numbers and lowercase letters, I'd run 
```
python genpass.py count=5 length=20 numeric=true lower=true
```