from pawpal_system import Owner, Pet, Task, Scheduler
import streamlit as st

st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")

st.title("🐾 PawPal+")

st.markdown(
    """
Welcome to the PawPal+ starter app.

This file is intentionally thin. It gives you a working Streamlit app so you can start quickly,
but **it does not implement the project logic**. Your job is to design the system and build it.

Use this app as your interactive demo once your backend classes/functions exist.
"""
)

with st.expander("Scenario", expanded=True):
    st.markdown(
        """
**PawPal+** is a pet care planning assistant. It helps a pet owner plan care tasks
for their pet(s) based on constraints like time, priority, and preferences.

You will design and implement the scheduling logic and connect it to this Streamlit UI.
"""
    )

with st.expander("What you need to build", expanded=True):
    st.markdown(
        """
At minimum, your system should:
- Represent pet care tasks (what needs to happen, how long it takes, priority)
- Represent the pet and the owner (basic info and preferences)
- Build a plan/schedule for a day that chooses and orders tasks based on constraints
- Explain the plan (why each task was chosen and when it happens)
"""
    )

st.divider()

if "owner" not in st.session_state:
    st.session_state.owner = Owner(name="Jordan")

if "scheduler" not in st.session_state:
    st.session_state.scheduler = Scheduler()

'''
st.subheader("Quick Demo Inputs (UI only)")
owner_name = st.text_input("Owner name", value="Jordan")
pet_name = st.text_input("Pet name", value="Mochi")
species = st.selectbox("Species", ["dog", "cat", "other"])
'''

st.subheader("Add a New Pet")

with st.form("add_pet_form"):
    pet_name_input = st.text_input("Pet Name")
    species_input = st.selectbox("Species", ["dog", "cat", "other"])
    submitted = st.form_submit_button("Add Pet")

    if submitted and pet_name_input:
        new_pet = Pet(name=pet_name_input, species=species_input)
        st.session_state.owner.add_pet(new_pet)
        st.success(f"{pet_name_input} added!")

st.subheader("Add a Task")

if st.session_state.owner.pets:
    selected_pet = st.selectbox(
        "Select Pet", [pet.name for pet in st.session_state.owner.pets]
    )
    pet_obj = next(pet for pet in st.session_state.owner.pets if pet.name == selected_pet)

    task_title = st.text_input("Task Title", value="Morning walk")
    duration = st.number_input("Duration (minutes)", min_value=1, max_value=240, value=20)
    priority = st.selectbox("Priority", ["low", "medium", "high"], index=2)

    if st.button("Add Task"):
        new_task = Task(title=task_title, duration=duration, priority=priority)
        pet_obj.add_task(new_task)
        st.success(f"Task '{task_title}' added to {pet_obj.name}!")
        
        st.subheader(f"Tasks for {pet_obj.name}")
        if pet_obj.tasks:
            st.table([
                {"Title": t.title, "Duration (mins)": t.duration, "Priority": t.priority} 
                for t in pet_obj.tasks
        ])
else:
    st.info("No pets yet. Add a pet first.")

st.subheader("Build Schedule")

if st.button("Generate Schedule"):
    scheduler = st.session_state.scheduler
    tasks, conflicts = scheduler.generate_schedule(st.session_state.owner)

    st.subheader("Today's Schedule")
    for t in tasks:
        st.write(f"- {t.title} ({t.priority}, {t.duration} mins)")

    if conflicts:
        st.subheader("Conflicts")
        for c in conflicts:
            st.warning(c)

'''

st.markdown("### Tasks")
st.caption("Add a few tasks. In your final version, these should feed into your scheduler.")

if "tasks" not in st.session_state:
    st.session_state.tasks = []

col1, col2, col3 = st.columns(3)
with col1:
    task_title = st.text_input("Task title", value="Morning walk")
with col2:
    duration = st.number_input("Duration (minutes)", min_value=1, max_value=240, value=20)
with col3:
    priority = st.selectbox("Priority", ["low", "medium", "high"], index=2)


if st.button("Add task"):
    st.session_state.tasks.append(
        {"title": task_title, "duration_minutes": int(duration), "priority": priority}
    )
    

if st.session_state.tasks:
    st.write("Current tasks:")
    st.table(st.session_state.tasks)
else:
    st.info("No tasks yet. Add one above.")

st.divider()

st.subheader("Build Schedule")
st.caption("This button should call your scheduling logic once you implement it.")

if st.button("Generate schedule"):
    st.warning(
        "Not implemented yet. Next step: create your scheduling logic (classes/functions) and call it here."
    )
    st.markdown(
        """
Suggested approach:
1. Design your UML (draft).
2. Create class stubs (no logic).
3. Implement scheduling behavior.
4. Connect your scheduler here and display results.
"""
    )
'''