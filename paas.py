import streamlit as st
from PIL import Image

# Set the page title and layout to wide
st.set_page_config(page_title="Modern Streamlit Website", layout="wide")

# Load an image for the header
header_image = Image.open("header_image.jpg")  # Replace with your image

# Main header section
st.image(header_image, use_column_width=True)
st.title("Welcome to My Modern Streamlit Website")
st.write("This is a clean and interactive web app built with Streamlit.")
st.markdown("---")  # Divider

# About section
st.header("About Us")
st.write("""
We are a forward-thinking company focused on delivering value through innovative solutions.
Our goal is to create seamless and impactful experiences for our users. With expertise in 
technology and design, we strive to bring the best solutions to life.
""")

# Three columns with images and descriptions
col1, col2, col3 = st.columns(3)

with col1:
    image1 = Image.open("image1.jpg")  # Replace with your image
    st.image(image1, caption="Our Team", use_column_width=True)
    st.write("Meet the talented people behind our success.")

with col2:
    image2 = Image.open("image2.jpg")  # Replace with your image
    st.image(image2, caption="Our Services", use_column_width=True)
    st.write("We offer a wide range of cutting-edge services.")

with col3:
    image3 = Image.open("image3.jpg")  # Replace with your image
    st.image(image3, caption="Our Vision", use_column_width=True)
    st.write("We are committed to shaping the future with innovation.")

st.markdown("---")  # Divider

# Services Section
st.header("Our Services")
st.write("We specialize in a variety of services tailored to meet the needs of our clients.")

service_col1, service_col2 = st.columns(2)

with service_col1:
    st.subheader("Web Development")
    st.write("""
    Our web development services are built to create fast, reliable, and visually appealing websites.
    From frontend design to backend development, we've got you covered.
    """)
    st.subheader("Data Analysis")
    st.write("""
    Leverage the power of data to drive informed decisions. Our data analysis team provides
    insights that can help you scale your business.
    """)

with service_col2:
    st.subheader("Mobile Apps")
    st.write("""
    Our team develops stunning and functional mobile applications for both Android and iOS platforms.
    We focus on creating intuitive user experiences.
    """)
    st.subheader("Consulting")
    st.write("""
    Need expert advice? Our consulting services provide you with the insights and strategies to
    tackle complex challenges and grow your business.
    """)

st.markdown("---")  # Divider

# Testimonials section
st.header("Testimonials")
st.write("Here’s what our clients have to say:")

testimonial_col1, testimonial_col2 = st.columns(2)

with testimonial_col1:
    st.write("""
    **"Their web development services were exceptional. Our traffic increased by 30%!"**
    - Sarah, CEO at Tech Innovators
    """)
    st.write("""
    **"Their consulting team helped us optimize our business strategy, resulting in a 15% growth."**
    - John, Founder of DataScape
    """)

with testimonial_col2:
    st.write("""
    **"We loved their attention to detail and the overall experience with our mobile app development."**
    - Emily, Product Manager at AppSolutions
    """)
    st.write("""
    **"The data insights they provided were game-changing for our company."**
    - Alex, Head of Marketing at FinCorp
    """)

st.markdown("---")  # Divider

# Contact section
st.header("Get in Touch")
contact_form = """
<form action="https://formsubmit.co/YOUR_EMAIL" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="Your email" required>
     <textarea name="message" placeholder="Your message here" required></textarea>
     <button type="submit">Send</button>
</form>
"""

st.markdown(contact_form, unsafe_allow_html=True)

# Apply basic CSS styling
st.markdown("""
    <style>
    form {
        display: flex;
        flex-direction: column;
        gap: 15px;
    }
    input, textarea {
        width: 100%;
        padding: 10px;
        border-radius: 5px;
        border: 1px solid #ccc;
        font-size: 16px;
    }
    button {
        padding: 10px;
        background-color: #04AA6D;
        color: white;
        border: none;
        border-radius: 5px;
        font-size: 16px;
        cursor: pointer;
    }
    button:hover {
        background-color: #45a049;
    }
    </style>
    """, unsafe_allow_html=True)

# Footer section
st.write("© 2024 Modern Streamlit Website. All rights reserved.")
