#imports

def fasade():
    mc = MainContext()
    mc.state = MenuState(mc)
    while True:
        user_input = input(f"{mc.state.prompt}")
        mc.state.perform(user_input)
    
if __name__ == "__main__":
     fasade()