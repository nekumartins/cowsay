import cowsay


chars = {
    'beavis': cowsay.beavis,
    'cheese': cowsay.cheese,
    'cow': cowsay.cow,
    'daemon': cowsay.daemon ,
    'dragon': cowsay.dragon,
    'fox': cowsay.fox,
    'ghostbusters': cowsay.ghostbusters,
    'kitty': cowsay.kitty,
    'meow': cowsay.meow,
    'miki': cowsay.miki,
    'milk': cowsay.milk,
    'pig': cowsay.pig,
    'stegosaurus': cowsay.stegosaurus, 
    'stimpy': cowsay.stimpy,
    'trex': cowsay.trex,
    'turkey': cowsay.turkey,
    'turtle': cowsay.turtle,
    'tux': cowsay.tux
    }
print("Hello, User")
ans = input("To see available lists of charactes input 'y', to skip hit any key: ")
if ans.lower() == 'y':
    for _ in chars:
        print (_)
        
message = input("What do you want to say: ")
character = input("What character do you want to use: ")





if character in chars:
    chars[character](message)
else:
    print(f"Sorry, '{character}' is not a valid character. Valid Characters are:")
    for _ in chars:
        print (_)



