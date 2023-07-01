import pickle

data = {
    "Man U": ['Sancho', 'Rashford', 'Antony'],
    "Tottenham": ['kulusevski', 'Kane', 'Son'],
    "New Castle": ["Gordon", "Wilson", "Almiron"]
}
# serialization
with open('london_players.pickle', 'wb') as f:
    pickle.dump(data, f)

#deserialization
with open('london_players.pickle', 'rb') as f:
    record = pickle.load(f)

print(record)