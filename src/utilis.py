import pandas as pd



def spliting(lines_as_lists):
    track_info = []
    trajectory_info = []

    for row in lines_as_lists:
        track_id = row[0]

        # add the first 4 values to track_info
        track_info.append(row[:4])

        remaining_values = row[4:]
        # reshape the list into a matrix and add track_id
        trajectory_matrix = [ [track_id] + remaining_values[i:i+6] for i in range(0, len(remaining_values), 6)]
        # add the matrix rows to trajectory_info
        trajectory_info = trajectory_info + trajectory_matrix
    return track_info, trajectory_info
    # df_track = pd.DataFrame(data= track_info,columns=track_cols)
    # df_trajectory = pd.DataFrame(data= trajectory_info,columns=trajectory_cols)
    # return df_track, df_trajectory
