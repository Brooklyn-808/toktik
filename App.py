import streamlit as st
import pandas as pd

# Mock user data
user_data = {
    "daily_usage": 120,  # in minutes
    "content_type_distribution": {"Educational": 30, "Entertainment": 70, "Creative": 20},
    "usage_goal": 90,  # in minutes
}

# Function to display mindful usage tracking
def mindful_usage_tracking(user_data):
    st.header("Mindful Usage Tracking")
    st.write("**Daily Usage:**")
    st.write(f"Total: {user_data['daily_usage']} minutes")

    st.write("**Content Type Distribution:**")
    content_types = list(user_data["content_type_distribution"].keys())
    content_values = list(user_data["content_type_distribution"].values())

    df = pd.DataFrame({
        'Content Type': content_types,
        'Minutes': content_values
    })

    st.bar_chart(df.set_index('Content Type'))

    st.write("**Set Your Usage Goal:**")
    new_goal = st.slider("Daily Usage Goal (minutes)", 30, 180, user_data["usage_goal"])
    if new_goal != user_data["usage_goal"]:
        user_data["usage_goal"] = new_goal
        st.success(f"Usage goal updated to {new_goal} minutes")

    st.write("**Reflection:**")
    reflection = st.text_area("How do you feel about your screen time today?")
    if st.button("Submit Reflection"):
        st.success("Reflection submitted! Thank you for sharing.")
        # Here you would typically save the reflection to a database or file

# Function to display positive content curation
def positive_content_curation():
    st.header("Positive Content Curation")
    st.write("**Well-Being Feed:**")
    st.image("https://via.placeholder.com/150", caption="Positive quotes")
    st.image("https://via.placeholder.com/150", caption="Mental health tips")
    st.image("https://via.placeholder.com/150", caption="Uplifting stories")

# Function to display educational integration
def educational_integration():
    st.header("Educational Integration")
    st.write("**Learning Modules:**")
    try:
        st.video("https://www.youtube.com/embed/dQw4w9WgXcQ", caption="Digital Literacy")
        st.video("https://www.youtube.com/embed/dQw4w9WgXcQ", caption="Mental Health Awareness")
        st.video("https://www.youtube.com/embed/dQw4w9WgXcQ", caption="Ethical Online Behavior")
    except Exception as e:
        st.error(f"Failed to load video: {e}")

# Function to display community building features
def community_building():
    st.header("Community Building")
    st.write("**Join Support Groups:**")
    support_groups = ["Study Buddies", "Mental Health Support", "Creative Minds"]
    selected_group = st.selectbox("Choose a support group to join", support_groups)
    st.write(f"You joined: {selected_group}")

# Function to display parental controls
def parental_controls():
    st.header("Parental Controls")
    st.write("**Activity Reports for Parents:**")
    st.write("Provide summaries and filters for parents to monitor and manage their child's app usage.")

# Main app function
def main():
    st.title("TikTok Well-Being Companion App")

    mindful_usage_tracking(user_data)
    positive_content_curation()
    educational_integration()
    community_building()
    parental_controls()

    st.write("---")
    st.write("Designed with Relational and Virtue Ethics in mind to promote healthier social media habits.")

if __name__ == "__main__":
    main()
