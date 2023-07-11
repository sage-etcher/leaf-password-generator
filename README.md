# password-generator
Just a quick simple password generator, for personal use

## Using the password-generator
```
python genpass.py [show [w|c]|arguements]
```

### Arguements 
| Arguement        | Default Value | Description | 
|:---------------- |:------------- |:----------- |
| `show w` | *N/A* | prints warranty information, cannot be used with other arguements |
| `show c` | *N/A* | prints terms and condition for the license, cannot be used with other arguements |
| `length=[int]` | 16 | password length. |
| `count=[int]` | 1 | number of passwords to generate. |
| `upper=[bool]` | false | use upper case letters? true or false |
| `lower=[bool]` | false | use lower case letters? true or false |
| `numeric=[bool]` | false | use numbers? true or false |
| `special=[bool]` | false | use special character? true or false |
| `bare=[bool]` | false | when true, don't print licensing information |


### Usage Example
If I wanted to generate 5 passwords, each password 20 characters long, containing just numbers and lowercase letters, I'd run 
```
python genpass.py count=5 length=20 numeric=true lower=true
```

and the program would return something allong the lines of 
```
cjd6nbeeau51osyrj2i2
nee4ftfiskivyox468on
4nq5nn5hgsxwrwo1e71o
q0ti1d68ybqzg8224at8
l5h3qqw78e81t9krb8of
```