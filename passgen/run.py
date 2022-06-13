from states import AppContext, MenuState
def fasade():
    mc = AppContext()
    mc.state = MenuState(mc)
    while True:
        user_input = input(f"{mc.state.prompt}")
        mc.state.perform(user_input)

fasade()
if __name__ == "__main__":
     #pgc= PassGenContext()
     #pgc.set_strategies= [
     #    TextChars(8),
     #    TextPhrase("krowi placek"),
     #    TextPokemon(3)
     #]
     #print(
     #pgc.get_password()
     #)
     fasade()