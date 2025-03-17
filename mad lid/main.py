import streamlit as st
import random

# 🎉 Streamlit Page Configuration
st.set_page_config(page_title="Funniest Mad Libs Adventure Story",  page_icon="🎭", layout="centered")

# 🐾 Animal-Emoji Dictionary
animal_emojis = {
    "monkey": "🐒", "cat": "🐱", "dog": "🐶", "duck": "🦆",
    "panda": "🐼", "rabbit": "🐰", "tiger": "🐯", "lion": "🦁",
    "elephant": "🐘", "cow": "🐮", "chicken": "🐔", "fish": "🐠",
    "horse": "🐴", "penguin": "🐧", "unicorn": "🦄", "dinosaur": "🦖",
    "parrot": "🦜","butterfly": "🦋", "spider": "🕷", "snake": "🐍", "turtle": "🐢","fairy":"🧚🏼"
}

# Sidebar for Inputs
st.title("🎉 Welcome to the Mad Libs Adventure Story!✍️")

st.sidebar.header("Enter Your Story Details 📝")

name = st.sidebar.text_input("Enter Your Name",placeholder="Enter your name here")
animal = st.sidebar.text_input("Enter Your Favorite Animal",placeholder="e.g., Dog, Cat, Tiger").lower()
places = st.sidebar.selectbox("Select Your Favorite Place", ["Winter Land", "Halloween Land", "Choco Land", "Adventure Land", "Forest Land"])
celebrity = st.sidebar.text_input("Enter Your Favorite Celebrity",placeholder="Enter Your Favorite Celebrity")
funny_reaction = st.sidebar.text_input("Enter Your Funny Reaction", placeholder="e.g., LOL, OMG, Haha!")
adjective = st.sidebar.text_input("Enter Your Favorite Adjective",placeholder="e.g., Crazy, Fun, Amazing")


silly_phrases = "Banana is  my bestiii"
verb = "Dancing"
action = "crazy"
background_images = {
    "Winter Land": "https://img.freepik.com/free-vector/winter-cartoon-fairytale-landscape-with-royal-castle-forest-covered-with-snow-vector-landscape-medieval-fortress-with-gate-towers-surrounded-with-snowy-trees-ancient-fortress-snowdrifts_107791-24182.jpg",
    "Halloween Land": "https://img.freepik.com/free-vector/halloween-background-flat-design_52683-43845.jpg",
    "Choco Land": "https://t3.ftcdn.net/jpg/05/56/55/72/240_F_556557209_YiP6LXZ3AlLMbhVVK1PUquE3LaOvpgVo.jpg",
    "Adventure Land": "https://cdn.suwalls.com/wallpapers/fantasy/adventure-land-19950-1920x1080.jpg",
    "Forest Land": "https://img.freepik.com/free-vector/book-with-fairies-flying-garden_1308-36771.jpg"
}

background_image = background_images.get(places)

#  🎨 Improved Styling
st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS4CAnPLNDTVd2Ibthjfh8xBsmY6o4XYajBcAGbqEqQSWHsZIKkbcQkys2gEGtgX2MXxf0&usqp=CAU');
        background-size: cover;
        background-repeat: no-repeat;
        background-position: center;

    }}
    [data-testid="stSidebar"] {{
        background-image: url('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS4CAnPLNDTVd2Ibthjfh8xBsmY6o4XYajBcAGbqEqQSWHsZIKkbcQkys2gEGtgX2MXxf0&usqp=CAU');
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        padding: 20px;
        border-radius: 10px;
        color: black;
        width: 300px;
    }}
    [data-testid="stSidebar"] label {{
        color: black !important;
        font-weight: bold !important;
        font-size: 24px !important;
    }}
    [data-testid="stSidebar"] input[type="text"] {{
        border: 2px solid black !important;
        border-radius: 5px !important;
        padding: 5px !important;
        background: transparent !important;
        font-size: 16px !important;
        border-color: black !important;
      }}
    [data-testid="stSidebar"] button {{
    border-color: black !important;
    color: black !important;
    font-weight: bold;
    background-color: white;
    border-radius: 5px;
    }}
    [data-testid="stSidebar"] button:hover {{
    background-color: #f0f0f0;
}}
    .story-box {{
       background: url({background_image});
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        padding: 30px;
        margin: 20px auto;
        border-radius: 10px;
        
    }}
    .info-box{{
        background: url('https://img.freepik.com/premium-vector/book-with-book-titled-moon-bottom_906149-78279.jpg');
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        padding: 30px;
        margin: 20px auto;
        border-radius: 10px;
        
    }}
    .text-box {{
        background-color: rgba(255, 255, 255, 0.4);
        padding: 30px;
        margin: 20px auto;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        font-size: 18px;
    }}
    .title {{
        color: #333;
        text-align: center;
        font-size: 32px;
        margin-bottom: 20px;
    }}
    .story-text {{
        font-size: 20px;
        color: black;
        line-height: 1.5;
    }}
    .highlight {{
        color:dark;  /* Bright and noticeable color */
        font-weight: bold;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# Generate Story
if st.sidebar.button("Generate Story 🎉"):
    animal_emoji = animal_emojis.get(animal, "🐾")
    random_objects = ["a flying banana 🍌", "an alien spaceship 🛸", "a talking pillow 🛏️", "a magical wand ✨", "a dancing parrot 🦜"]
    random_food = ["a giant pizza 🍕", "a floating ice cream 🍦", "a spicy burrito 🌯", "a singing donut 🍩"]
    random_sound = ["BOOM 💥", "SPLASH 💦", "MEOW 🐱", "WOOHOO 🎉"]
    random_object = random.choice(random_objects)
    random_food_item = random.choice(random_food)
    random_noise = random.choice(random_sound)

    if name.endswith("s"):
        possessive_name = name + "'"
    else:
        possessive_name = name + "'s"

    story = f"""
    <div class="story-box">
    <div class="text-box">
        <h2 class="title">Your Crazy Mad Libs Story! 🎭</h2>
        <p class="story-text">
        One day, <span class="highlight">{name}</span> and <span class="highlight">{possessive_name}</span> <span class="highlight">{animal}</span> {animal_emoji} decided to go on an adventure.<br>
        They traveled to <span class="highlight">{places}</span> 🌍, where they saw <span class="highlight">{celebrity}</span> 🎭.<br>
        {name} walked up and said, '<span class="highlight">{silly_phrases}</span>' 😂, and suddenly the <span class="highlight">{celebrity}</span> started <span class="highlight">{verb}</span> 💃!<br>
        Just then, {random_object} fell from the sky, making a loud <span class="highlight">{random_noise}</span>! Everyone <span class="highlight">{funny_reaction}</span> 🤣!<br>
        To make things even crazier, {random_food_item} appeared out of nowhere, and <span class="highlight">{possessive_name}</span> <span class="highlight">{animal}</span> {animal_emoji} started eating it! 🍽️😂<br>
        In the end, <span class="highlight">{possessive_name}</span> <span class="highlight">{animal}</span> {animal_emoji} laughed and said, 'Today was really <span class="highlight">{adjective}</span>!' <br>
        Then, <span class="highlight">{name}</span> and <span class="highlight">{possessive_name}</span> <span class="highlight">{animal}</span> {animal_emoji} <span class="highlight">{action}</span> 🚀 all the way to the moon 🌙 and safely returned home 🏡 to have even more fun! 🎉😂
        </p>
     </div>
    </div>
    """

    st.markdown(story, unsafe_allow_html=True)
else:
   
    info = f"""
    <div class="info-box">
     <div class="text-box">
      <h2 class="title">🌟 How to Play the Funniest Mad Libs Adventure Story 🌟</h2>
        <p class="story-text">
        🤔 To create your personalized funny story, follow these steps:<br>
        1. Enter your name and favorite animal in the sidebar. 📝<br>
        2. Choose a place, a celebrity to spice it up. 🌍🎭😂<br>
        3. Add your favorite action, adjective. 💃🤣🚀<br>
        4. Click on the "Generate Story 🎉" button to see your hilarious adventure!<br>
        5. Enjoy your story and share the laughs with friends! 🎉😂<br>
        </p>
    </div>
    </div>
    """
    st.markdown(info, unsafe_allow_html=True)
st.markdown("---")
st.markdown("<div style='text-align: center;'>Made by❤️ Rimsha Sultan</div>", unsafe_allow_html=True)
