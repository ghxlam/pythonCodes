import state
myState= state.State('New Jersey')
myState.add_university('NJIT')
myState.add_university('Princeton')
print(myState.is_home_of('MIT'))
