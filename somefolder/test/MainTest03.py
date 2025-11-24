import somefolder.character.CharacterModule
somefolder.character.CharacterModule.namePrint()
somefolder.character.CharacterModule.sayHello('안녕하세요', 1)

from somefolder.character import CharacterModule
print()
CharacterModule.namePrint()
CharacterModule.sayHello('안녕하세요',2)

from somefolder.character.CharacterModule import *
print()
namePrint()
sayHello('안녕하세요', 1)

import somefolder.character.CharacterModule as info
print()
info.namePrint()
info.sayHello('안녕하세요', 3)

