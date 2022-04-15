import streamlit as st

possible_end_lies = ["Fairway", "Green", "Bermuda", "Recovery", "Kitchen"]
possible_start_lies = ["Fairway", "Recovery", "Kitchen"]

def add_shots_to_container(container, hole_no):
    n_shots = container.number_input("No. of shots played: ", min_value=1)
    shots_dict = {"hole_id":hole_no}
    end_distances, end_lies, units= [], [], []
    for i in range(n_shots):

        if i == 0:
            start_lie = container.selectbox("Start Lie", possible_start_lies)
            start_distance = container.number_input(
                "Shot start distance (yds) ", min_value=0
            )
            shots_dict["hole_yards"] = start_distance
            shots_dict["tee_lie"] = start_lie
            
            shot_end_lie = container.selectbox("End Lie", possible_end_lies)
            unit = "ft" if shot_end_lie in ["Green", "Bermuda"] else "yds"
            end_distance = container.number_input(f"Shot end distance ({unit}) ")
        else:
            shot_end_lie = container.selectbox("End Lie", possible_end_lies)
            unit = "ft" if shot_end_lie in ["Green", "Bermuda"] else "yds"
            end_distance = container.number_input(f"Shot end distance ({unit}) ")
    
    end_distances.append(end_distance)
    end_lies.append(shot_end_lie)
    units.append(unit)
    shot_details = {"shot_end_lie":end_lies, "shot_end_distance":end_distances, "distance_units":units}
    shots_dict["shot_details"] = shot_details
    return shots_dict



no_holes_played = int(st.number_input("How many holes are you playing?", min_value=1))

round_shots = {}

for hole_no in range(1, no_holes_played+1):
    cont = st.container()
    cont.write(f"Hole No. {hole_no}")
    shots_dict = add_shots_to_container(cont, hole_no)
    round_shots["hole_id"] = hole_no
    round_shots["hole_details"] = shots_dict


with open("shots.json", "w") as file:
     btn = st.download_button(
             label="Download shots",
             data=file,
             file_name="shots.json",
           )

