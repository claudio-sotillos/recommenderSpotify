import pickle 

recommended_track_ids = set()
with open('recommended_ids#.pkl', 'wb') as f:
    pickle.dump(recommended_track_ids, f)