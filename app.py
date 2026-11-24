
import streamlit as st
from restaurant_chain import generate_rest_namd_and_item

st.set_page_config(
    page_title="The Culinary Atelier",
    page_icon="🍽️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@400;500;600;700&family=DM+Sans:wght@400;500;600&display=swap');

:root {
    --cream: #F8F3E9;
    --wine: #311C21;
    --gold: #B4945B;
    --muted: #72655E;
}

.stApp {
    background: var(--cream);
    color: var(--wine);
    font-family: 'DM Sans', sans-serif;
}

header[data-testid="stHeader"] {
    background: transparent;
}

.block-container {
    max-width: 950px;
    padding-top: 1.5rem;
    padding-bottom: 4rem;
}

.hero {
    background: #311C21;
    padding: 58px 28px;
    text-align: center;
    border-radius: 12px;
    border: 1px solid #806547;
    margin-bottom: 35px;
}

.eyebrow {
    color: #D5B477;
    font-size: 12px;
    letter-spacing: 4px;
    text-transform: uppercase;
}

.hero h1 {
    font-family: 'Cormorant Garamond', serif;
    font-size: clamp(44px, 7vw, 76px);
    font-weight: 500;
    line-height: 1.05;
    color: #FFF3E2;
    margin: 20px 0 12px;
}

.hero p {
    color: #D6C4B2;
    font-size: 13px;
    letter-spacing: 2px;
}

.section-title {
    font-family: 'Cormorant Garamond', serif;
    text-align: center;
    font-size: 38px;
    color: #311C21;
    margin-bottom: 5px;
}

.section-subtitle {
    color: #786B63;
    text-align: center;
    font-size: 14px;
    margin-bottom: 28px;
}

.stSelectbox label {
    font-weight: 600;
    color: #311C21 !important;
}

div[data-baseweb="select"] > div {
    background: #FFFCF6 !important;
    border: 1px solid #CDBB9D !important;
    border-radius: 8px !important;
}

div.stButton > button {
    background: #311C21;
    color: #FFF3E2;
    border: 1px solid #B4945B;
    border-radius: 7px;
    min-height: 50px;
    font-weight: 600;
    letter-spacing: 1px;
    width: 100%;
}

div.stButton > button:hover {
    background: #56343A;
    color: white;
    border-color: #D5B477;
}

.result-card {
    background: #FFFCF6;
    border: 1px solid #D8C7A8;
    padding: 42px 28px;
    text-align: center;
    border-radius: 10px;
    margin-top: 30px;
    box-shadow: 0 8px 32px rgba(49, 28, 33, 0.05);
}

.result-label {
    font-size: 11px;
    color: #9A7844;
    letter-spacing: 3px;
    text-transform: uppercase;
}

.restaurant-name {
    font-family: 'Cormorant Garamond', serif;
    font-size: clamp(35px, 5vw, 55px);
    color: #311C21;
    margin: 14px 0;
    overflow-wrap: anywhere;
}

.ornament {
    color: #B4945B;
    margin: 15px 0;
    letter-spacing: 12px;
}

.menu-heading {
    font-family: 'Cormorant Garamond', serif;
    font-size: 32px;
    color: #311C21;
    margin: 20px 0;
}

.menu-item {
    padding: 12px 16px;
    border-bottom: 1px solid #E9DFC9;
    font-size: 15px;
    color: #493C38;
}

/* Make the Streamlit page fill the screen */
[data-testid="stAppViewContainer"] {
    min-height: 100vh;
}

[data-testid="stMainBlockContainer"] {
    min-height: 100vh;
    display: flex;
    flex-direction: column;
}

/* Push the footer to the bottom */
.footer {
    margin-top: auto;
    padding: 20px;
    text-align: center;
    border-top: 1px solid #D8C7A8;
    color: #83766C;
    font-size: 12px;
    letter-spacing: 1px;
}

@media (max-width: 600px) {
    .hero { padding: 40px 16px; }
    .block-container { padding-left: 1rem; padding-right: 1rem; }
    .result-card { padding: 28px 16px; }
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
    <div class="eyebrow">✦ The Culinary Atelier ✦</div>
    <h1>A Taste of Elegance</h1>
    <p>WHERE EVERY NAME TELLS A STORY</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="section-title">
    Discover Your Restaurant's Identity
</div>
<div class="section-subtitle">
    Select your cuisine and let imagination set the table.
</div>
""", unsafe_allow_html=True)

left, center, right = st.columns([1, 2, 1])
cuisine_options = [
    "Indian",
    "Afghan",
    "American",
    "Arabic",
    "Argentinian",
    "Australian",
    "Bakery & Café",
    "Bangladeshi",
    "Barbecue",
    "Brazilian",
    "British",
    "Burmese",
    "Caribbean",
    "Chinese",
    "Continental",
    "Desserts & Sweets",
    "Egyptian",
    "Ethiopian",
    "Fast Food",
    "Filipino",
    "French",
    "Fusion",
    "German",
    "Greek",
    "Indonesian",
    "Italian",
    "Japanese",
    "Korean",
    "Lebanese",
    "Malaysian",
    "Mediterranean",
    "Mexican",
    "Middle Eastern",
    "Moroccan",
    "Nepalese",
    "Pakistani",
    "Persian",
    "Peruvian",
    "Russian",
    "Seafood",
    "Singaporean",
    "South African",
    "Spanish",
    "Sri Lankan",
    "Street Food",
    "Thai",
    "Tibetan",
    "Turkish",
    "Vegan",
    "Vegetarian",
    "Vietnamese"
]

with center:
    cuisine = st.selectbox(
        "SELECT YOUR CUISINE",
        sorted(cuisine_options, key=str.casefold),
        index=None,
        placeholder="Choose a cuisine..."
    )

    generate = st.button(
        "✦ UNVEIL YOUR RESTAURANT ✦",
        use_container_width=True,
        disabled=cuisine is None
    )

if generate:
    with st.spinner("Crafting your culinary identity..."):
        try:
            response = generate_rest_namd_and_item(cuisine)
            st.session_state["result"] = response
            st.session_state["cuisine"] = cuisine
        except Exception as e:
            st.error(f"Unable to generate restaurant: {e}")

if "result" in st.session_state:
    response = st.session_state["result"]

    import html

    restaurant_name = html.escape(
        str(response.get("rest_name", "Your Restaurant"))
    )

    raw_menu = str(response.get("menu_item", ""))
    menu_items = [
        item.strip()
        for item in raw_menu.split(",")
        if item.strip()
    ]

    menu_html = "".join(
        f'<div class="menu-item">✦ &nbsp; {html.escape(item)}</div>'
        for item in menu_items
    )

    st.markdown(f"""
    <div class="result-card">
        <div class="result-label">Your Restaurant</div>
        <div class="restaurant-name">{restaurant_name}</div>
        <div class="ornament">✦ ── ✦ ── ✦</div>
        <div class="menu-heading">The Signature Menu</div>
        {menu_html}
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
<div class="footer">
    Developed BY Nagendra Chouhan 
</div>
""", unsafe_allow_html=True)
