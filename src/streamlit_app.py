import streamlit as st
import datetime as dt

with st.sidebar:
    n_holes = int(st.number_input("No. of hole played", min_value=1))
    format_hole = lambda x: f"Hole {x}"
    hole = st.selectbox("Select hole to edit:", range(1, n_holes+1), format_func=format_hole)

possible_end_lies = ["Fairway", "Green", "In The Hole", "Bermuda", "Recovery", "Kitchen"]
possible_start_lies = ["Fairway", "Recovery", "Kitchen"]
def add_shots_to_container(container, hole_no):
    n_shots = int(
        container.number_input("No. of shots played: ", min_value=1, key=hole_no)
    )
    shots_dict = {"hole_id": hole_no}
    end_distances, end_lies, units = [], [], []
    for i in range(n_shots):

        if i == 0:
            start_lie = container.selectbox("Start Lie", possible_start_lies, key=f"start {hole_no}")
            start_distance = container.number_input(
                "Shot start distance (yds) ", min_value=0, key=f"start dist {hole_no}"
            )
            shots_dict["hole_yards"] = start_distance
            shots_dict["tee_lie"] = start_lie

            shot_end_lie = container.selectbox("End Lie", possible_end_lies, key=f"end lie h:{hole_no} s:{i}")
            unit = "ft" if shot_end_lie in ["Green", "Bermuda"] else "yds"
            end_distance = container.number_input(f"Shot end distance ({unit}) ", key=f"end dist h:{hole_no} s:{i}")
        else:
            shot_end_lie = container.selectbox("End Lie", possible_end_lies, key=f"end lie h:{hole_no} s:{i}")
            unit = "ft" if shot_end_lie in ["Green", "Bermuda"] else "yds"
            end_distance = container.number_input(f"Shot end distance ({unit}) ", key=f"end dist h:{hole_no} s:{i}")

    end_distances.append(end_distance)
    end_lies.append(shot_end_lie)
    units.append(unit)
    shot_details = {
        "shot_end_lie": end_lies,
        "shot_end_distance": end_distances,
        "distance_units": units,
        "update_time":dt.datetime.now()
    }
    shots_dict["shot_details"] = shot_details
    return shots_dict


if "shots_data" not in st.session_state:
    st.session_state.shots_data = {}

cont = st.container()
cont.write(f"Hole No. {hole}")
shots_dict = add_shots_to_container(cont, hole)
st.session_state.shots_data["hole_id"] = hole
st.session_state.shots_data["hole_details"] = shots_dict

