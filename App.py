import streamlit as st
from datetime import datetime, timedelta

st.title("TikTok Well-Being Companion App")

# Mock user data
user_data = {
    "daily_usage": 120,  # in minutes
    "content_type_distribution": {"Educational": 30, "Entertainment": 70, "Creative": 20},
    "usage_goal": 90,  # in minutes
}

# Mindful Usage Tracking
st.header("Mindful Usage Tracking")
st.write("**Daily Usage:**")
st.write(f"Total: {user_data['daily_usage']} minutes")

usage_types = user_data["content_type_distribution"]
st.write("**Content Type Distribution:**")
for content_type, minutes in usage_types.items():
    st.write(f"{content_type}: {minutes} minutes")

st.write("**Set Your Usage Goal:**")
new_goal = st.slider("Daily Usage Goal (minutes)", 30, 180, user_data["usage_goal"])
if new_goal != user_data["usage_goal"]:
    user_data["usage_goal"] = new_goal
    st.success(f"Usage goal updated to {new_goal} minutes")

# Reflection Prompts
st.write("**Reflection:**")
reflection = st.text_area("How do you feel about your screen time today?")

# Positive Content Curation
st.header("Positive Content Curation")
st.write("**Well-Being Feed:**")
st.write("- Positive quotes")
st.write("- Mental health tips")
st.write("- Uplifting stories")

# Educational Integration
st.header("Educational Integration")
st.write("**Learning Modules:**")
st.write("- Digital Literacy")
st.write("- Mental Health Awareness")
st.write("- Ethical Online Behavior")

# Community Building
st.header("Community Building")
st.write("**Join Support Groups:**")
support_groups = ["Study Buddies", "Mental Health Support", "Creative Minds"]
selected_group = st.selectbox("Choose a support group to join", support_groups)
st.write(f"You joined: {selected_group}")

# Parental Controls
st.header("Parental Controls")
st.write("**Activity Reports for Parents:**")
st.write("Provide summaries and filters for parents to monitor and manage their child's app usage.")

st.write("---")
st.write("Designed with Relational and Virtue Ethics in mind to promote healthier social media habits.")

if st.button("Submit Reflection"):
    st.success("Reflection submitted! Thank you for sharing.")
