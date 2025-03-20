import streamlit as st
import time
from datetime import datetime, timedelta

def countdown_timer(target_time):
    while True:
        now = datetime.now()
        time_left = target_time - now
        if time_left.total_seconds() <= 0:
            st.subheader("🎉 Time's Up! INTEZAR KI GHARIYAN KHATAM 🎉")
            break
        
        days, remainder = divmod(time_left.total_seconds(), 86400)
        hours, remainder = divmod(remainder, 3600)
        minutes, seconds = divmod(remainder, 60)
        
        st.markdown(
            f"""
            <div class='timer-box'>
                <span style='color: green;'>{int(days)}d</span> 
                <span style='color: red;'>{int(hours)}h</span> 
                <span style='color: green;'>{int(minutes)}m</span> 
                <span style='color: red;'>{int(seconds)}s</span>
            </div>
            """,
            unsafe_allow_html=True,
        )
        time.sleep(1)
        st.rerun()

# Set the target date and time
target_datetime = datetime(2025, 3, 21, 2, 0, 0)

# Streamlit UI setup
st.set_page_config(page_title="JASHAN E AMAD", page_icon="🎉", layout="wide")

# Apply background animations at a slower speed
time.sleep(2)
st.balloons()
time.sleep(2)
st.snow()
time.sleep(2)

st.markdown(
    """
    <style>
        .centered-text {
            text-align: center;
            font-size: 50px;
            font-weight: bold;
            background: linear-gradient(45deg, #ff4b4b, #ffcc00);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            position: absolute;
            margin-top: 2%; /* Adjusted to move slightly up */
            left: 50%;
            transform: translate(-50%, -50%);
        }
        .subtext {
            text-align: center;
            font-size: 35px;
            font-weight: bold;
            background: linear-gradient(45deg, #00ffcc, #ff6600);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            position: absolute;
            margin-top: 12%; /* Moved slightly below first text */
            left: 50%;
            transform: translate(-50%, -50%);
        }
        .timer-box {
            text-align: center;
            font-size: 40px;
            font-weight: bold;
            border: 3px solid #ff4b4b;
            padding: 20px;
            display: inline-block;
            border-radius: 10px;
            background-color: white;
            position: absolute;
            margin-top: 25%; /* Adjusted to move to green box position */
            left: 50%;
            transform: translate(-50%, -50%);
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Display main content
st.markdown("<div class='centered-text'>🎊 JASHAN E AMAD E AFIFA & ITS CHINGERPOT 🎊</div>", unsafe_allow_html=True)
st.markdown("<div class='subtext'>🎈 Get Ready! Bus Thodi Der Aur! Hosla Rakho 🎈</div>", unsafe_allow_html=True)

# Run countdown timer
countdown_timer(target_datetime)