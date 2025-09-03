import streamlit as st

# Page setup
st.set_page_config(page_title="To-Do List App", page_icon="📝", layout="centered")

# Track which page we are on
if "page" not in st.session_state:
    st.session_state.page = "home"

# ---------------- HOME PAGE ----------------
if st.session_state.page == "home":
    st.title("📝 Welcome to To-Do List Tracker")
    st.write("Stay organized and track your daily tasks 🚀")

    if st.button("➡️ Let's Go"):
        st.session_state.page = "todo"
        

# ---------------- TO-DO LIST PAGE ----------------
elif st.session_state.page == "todo":
    st.title("📝 To-Do List Tracker")

    # Back button to homepage
    if st.button("🏠 Back to Home"):
        st.session_state.page = "home"
        

    # Initialize task list
    if "tasks" not in st.session_state:
        st.session_state.tasks = []

    # Input box for new task
    with st.form("task_form", clear_on_submit=True):
        new_task = st.text_input("Add a new task:")
        submitted = st.form_submit_button("➕ Add Task")
        if submitted and new_task.strip():
            st.session_state.tasks.append({"task": new_task, "done": False})

    st.markdown("---")

    # Show tasks
    if not st.session_state.tasks:
        st.info("No tasks yet. Add one above 🚀")
    else:
        for i, t in enumerate(st.session_state.tasks):
            cols = st.columns([0.1, 0.7, 0.2])

            # Checkbox for completion
            with cols[0]:
                st.session_state.tasks[i]["done"] = st.checkbox(
                    "", value=t["done"], key=f"done_{i}"
                )

            # Task text
            with cols[1]:
                if t["done"]:
                    st.markdown(f"✅ ~~{t['task']}~~")
                else:
                    st.markdown(f"🔲 {t['task']}")

            # Delete button
            with cols[2]:
                if st.button("🗑️", key=f"del_{i}"):
                    st.session_state.tasks.pop(i)
                    
