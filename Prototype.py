import streamlit as st

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="PathFinder | Career Guidance Platform", 
    page_icon="🎯", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# --- ADVANCED UI/UX CUSTOM CSS STYLING ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:wght@700;800&family=Figtree:wght@400;600;700&display=swap');
    :root {
        --ink: #14112B;
        --mist: #E8E3FF;
        --pink: #FF4F9A;
        --blue: #3D5AFE;
        --sun: #FFD23F;
        --mint: #5CF2C3;
        --paper: #FFFFFF;
    }
    /* ---------- BACKGROUND: topographic "path map" + colour blobs ---------- */
    .stApp {
        background-color: var(--mist);
        background-image:
            radial-gradient(circle at 8% 12%, rgba(255, 79, 154, 0.28) 0, transparent 30%),
            radial-gradient(circle at 92% 18%, rgba(92, 242, 195, 0.35) 0, transparent 28%),
            radial-gradient(circle at 80% 90%, rgba(61, 90, 254, 0.22) 0, transparent 32%),
            url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='360' height='360' viewBox='0 0 360 360' fill='none' stroke='%2314112B' stroke-opacity='0.09' stroke-width='1.5'%3E%3Ccircle cx='0' cy='0' r='50'/%3E%3Ccircle cx='0' cy='0' r='85'/%3E%3Ccircle cx='360' cy='360' r='50'/%3E%3Ccircle cx='360' cy='360' r='85'/%3E%3Cellipse cx='180' cy='180' rx='30' ry='18' transform='rotate(-20 180 180)'/%3E%3Cellipse cx='180' cy='180' rx='62' ry='38' transform='rotate(-20 180 180)'/%3E%3Cellipse cx='180' cy='180' rx='95' ry='60' transform='rotate(-20 180 180)'/%3E%3Cellipse cx='180' cy='180' rx='130' ry='84' transform='rotate(-20 180 180)'/%3E%3C/svg%3E");
        background-attachment: fixed;
        color: var(--ink);
    }
    .main {
        color: var(--ink);
    }
    [data-testid="stHeader"] {
        background: transparent;
    }
    /* ---------- TYPOGRAPHY ---------- */
    .stMarkdown, .stMarkdown p, .stMarkdown li, label, input, textarea, button, [data-baseweb="select"] {
        font-family: 'Figtree', sans-serif;
    }
    .stApp p, .stApp li, .stApp label, .stApp [data-testid="stWidgetLabel"] p {
        color: var(--ink);
    }
    .stApp [data-testid="stWidgetLabel"] p {
        font-weight: 700;
    }
    h1, h2, h3, h4, h5 {
        font-family: 'Bricolage Grotesque', sans-serif !important;
        color: var(--ink) !important;
        letter-spacing: -0.02em;
    }
    h1 {
        font-weight: 800 !important;
        font-size: 4rem !important;
        line-height: 1.05;
        text-shadow: 4px 4px 0 var(--pink);
    }
    h3 {
        font-weight: 800 !important;
    }
    h5 {
        font-weight: 700 !important;
        opacity: 0.8;
    }
    a, .stApp a {
        color: var(--blue) !important;
        font-weight: 700;
        text-decoration: underline wavy var(--pink);
        text-underline-offset: 4px;
    }
    hr {
        border: none !important;
        border-top: 3px dashed var(--ink) !important;
        opacity: 0.35;
    }
    /* ---------- BUTTONS (sticker style) ---------- */
    .stButton>button, .stFormSubmitButton>button {
        background: var(--pink);
        color: var(--ink);
        border-radius: 14px;
        padding: 0.7rem 1.8rem;
        font-weight: 700;
        border: 2.5px solid var(--ink);
        box-shadow: 4px 4px 0 var(--ink);
        transition: transform 0.15s ease, box-shadow 0.15s ease;
    }
    .stButton>button p, .stFormSubmitButton>button p {
        color: var(--ink);
        font-weight: 700;
        font-size: 1.05rem;
    }
    .stButton>button:hover, .stFormSubmitButton>button:hover {
        background: var(--sun);
        color: var(--ink);
        border: 2.5px solid var(--ink);
        box-shadow: 7px 7px 0 var(--ink);
        transform: translate(-3px, -3px);
    }
    .stButton>button:active, .stFormSubmitButton>button:active {
        box-shadow: 0 0 0 var(--ink);
        transform: translate(4px, 4px);
    }
    /* ---------- CARDS & BADGES ---------- */
    .card {
        background: var(--paper);
        padding: 1.8rem;
        border-radius: 22px;
        border: 3px solid var(--ink);
        box-shadow: 8px 8px 0 var(--ink);
        margin-bottom: 1.2rem;
    }
    .badge {
        background-color: var(--sun);
        color: var(--ink);
        padding: 0.3rem 0.8rem;
        border-radius: 20px;
        border: 2px solid var(--ink);
        font-size: 0.85rem;
        font-weight: 700;
    }
    /* ---------- ASSESSMENT FORM ---------- */
    [data-testid="stForm"] {
        background: var(--paper);
        border: 3px solid var(--ink);
        border-radius: 24px;
        box-shadow: 10px 10px 0 var(--blue);
        padding: 2rem;
    }
    [data-baseweb="select"] > div {
        background: #F6F3FF;
        border: 2.5px solid var(--ink);
        border-radius: 14px;
        color: var(--ink);
        transition: box-shadow 0.15s ease;
    }
    [data-baseweb="select"] > div:hover, [data-baseweb="select"] > div:focus-within {
        box-shadow: 4px 4px 0 var(--mint);
    }
    [data-baseweb="select"] * {
        color: var(--ink);
    }
    [data-baseweb="popover"] ul, [data-baseweb="popover"] li {
        background: var(--paper);
        color: var(--ink);
    }
    [data-baseweb="popover"] li:hover {
        background: var(--mist);
    }
    /* ---------- ALERTS (success / info / warning) ---------- */
    [data-testid="stAlert"] {
        border: 3px solid var(--ink);
        border-radius: 18px;
        box-shadow: 6px 6px 0 var(--ink);
        background: var(--mint);
    }
    [data-testid="stAlert"] * {
        color: var(--ink) !important;
    }
    [data-testid="stAlert"]:has([data-testid="stAlertContentWarning"]) {
        background: var(--sun);
    }
    [data-testid="stAlert"]:has([data-testid="stAlertContentInfo"]) {
        background: #FFFFFF;
        box-shadow: 6px 6px 0 var(--pink);
    }
    /* ---------- CHARTS ---------- */
    [data-testid="stArrowVegaLiteChart"], [data-testid="stVegaLiteChart"] {
        background: var(--paper);
        border: 3px solid var(--ink);
        border-radius: 20px;
        box-shadow: 6px 6px 0 var(--ink);
        padding: 1rem;
    }
    /* ---------- SIDEBAR / MENTOR CHAT ---------- */
    [data-testid="stSidebar"] {
        background: var(--sun);
        border-right: 3px solid var(--ink);
    }
    [data-testid="stSidebar"] > div {
        background-image: radial-gradient(rgba(20, 17, 43, 0.14) 1.5px, transparent 1.5px);
        background-size: 18px 18px;
    }
    [data-testid="stChatMessage"] {
        background: var(--paper);
        border: 2.5px solid var(--ink);
        border-radius: 18px;
        box-shadow: 4px 4px 0 var(--ink);
        margin-bottom: 0.6rem;
    }
    [data-testid="stChatInput"] {
        border: 3px solid var(--ink);
        border-radius: 16px;
        background: var(--paper);
        box-shadow: 4px 4px 0 var(--pink);
    }
    /* ---------- MOBILE + ACCESSIBILITY ---------- */
    @media (max-width: 640px) {
        h1 { font-size: 2.6rem !important; }
        [data-testid="stForm"] { padding: 1.1rem; box-shadow: 6px 6px 0 var(--blue); }
    }
    @media (prefers-reduced-motion: reduce) {
        .stButton>button, .stFormSubmitButton>button, [data-baseweb="select"] > div { transition: none; }
    }
    </style>
""", unsafe_allow_html=True)

# --- INITIALIZE SESSION STATE ---
if "scores" not in st.session_state:
    st.session_state.scores = {"Technical": 0, "Analytical": 0, "Creative": 0, "Practical": 0, "Social": 0}
if "submitted" not in st.session_state:
    st.session_state.submitted = False
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "👋 Hello! I'm your PathFinder Mentor. Ask me about any career path, how this assessment works, or for guidance on your future!"}
    ]

# --- SIDEBAR: ALWAYS-ON ADVANCED CHATBOT ---
with st.sidebar:
    st.markdown("### 🎯 PathFinder Mentor")
    st.write("Your 24/7 intelligent career companion.")
    st.markdown("---")
    
    # Chat container with fixed height
    chat_container = st.container(height=380)
    with chat_container:
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

    if prompt := st.chat_input("Ask about careers or assessment..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        p_lower = prompt.lower()
        response = ""
        
        # Robust conversational handling
        if any(g in p_lower for g in ["hi", "hello", "hey", "greetings", "how are you"]):
            response = "Hello! I'm doing great and ready to help you discover your ideal career path. Feel free to ask me about specific tech, analytical, or vocational careers, or how our assessment works!"
        elif "assessment" in p_lower or "how does" in p_lower or "help" in p_lower:
            response = (
                "**How PathFinder Assessment Works:**\n\n"
                "Our psychometric evaluation maps your personal inclinations across 5 core professional vectors: **Technical, Analytical, Creative, Practical, and Social**.\n\n"
                "By analyzing your spontaneous preferences in free time, school subjects, and problem-solving styles, PathFinder eliminates guesswork and connects you directly with high-growth technical tracks and free university modules on platforms like edX and SWAYAM Plus."
            )
        elif "ai" in p_lower or "ml" in p_lower or "engineer" in p_lower or "software" in p_lower:
            response = (
                "### 💻 AI & Software Engineering Track\n\n"
                "**What they do:** AI and Software Engineers build the digital architecture that powers modern apps, websites, and intelligent automation systems. They write robust code (primarily in Python, C++, or JavaScript), train machine learning models on large datasets, and solve complex logical challenges.\n\n"
                "**Core Skills Required:** Problem-solving, algorithm design, version control (Git), and data structures.\n\n"
                "**Career Outlook:** High demand globally with exceptional growth across all industries, offering remote work flexibility and startup or enterprise opportunities."
            )
        elif "data" in p_lower or "analyst" in p_lower:
            response = (
                "### 📊 Data Science & Analytics Track\n\n"
                "**What they do:** Data Analysts and Scientists examine complex, messy datasets to extract actionable business insights. They clean data, build visual dashboards in Tableau or PowerBI, and use statistical models to guide executive decision-making.\n\n"
                "**Core Skills Required:** Python/R, SQL, Excel, statistical analysis, and data storytelling.\n\n"
                "**Career Outlook:** Essential in finance, healthcare, e-commerce, and tech firms looking to make data-driven decisions."
            )
        elif "design" in p_lower or "ui/ux" in p_lower:
            response = (
                "### 🎨 Digital Media & UI/UX Design Track\n\n"
                "**What they do:** UI/UX Designers bridge the gap between human psychology and digital technology. They research user behavior, design intuitive wireframes and interactive prototypes in Figma, and ensure applications are visually stunning and accessible.\n\n"
                "**Core Skills Required:** User empathy, wireframing, color theory, typography, and prototyping tools.\n\n"
                "**Career Outlook:** Highly sought after by product-based companies and digital agencies worldwide."
            )
        else:
            response = (
                f"That is a wonderful question about **'{prompt}'**!\n\n"
                "In today's rapidly evolving job market, exploring such fields early in high school gives you a massive advantage. Professionals in this domain typically combine continuous online learning (via free university audits on edX or government platforms like SWAYAM Plus) with practical, hands-on mini-projects. \n\n"
                "I recommend completing our 10-question assessment on the main screen to see how closely your natural strengths align with this pathway!"
            )

        st.session_state.messages.append({"role": "assistant", "content": response})
        st.rerun()

# --- MAIN DASHBOARD HEADER ---
st.markdown("# 🎯 PathFinder")
st.markdown("##### Intelligent Career Counselling & Skill Roadmap Platform for High-School Students")
st.markdown("---")

# --- 10-QUESTION ASSESSMENT FORM ---
if not st.session_state.submitted:
    st.markdown("### 📝 Step 1: 10-Question Psychometric Interest Assessment")
    st.write("Answer the questions below honestly based on your genuine preferences. Our recommendation engine will instantly synthesize your personalized career profile upon submission.")

    with st.form("assessment_form"):
        col1, col2 = st.columns(2)
        
        with col1:
            q1 = st.selectbox("1. What do you enjoy doing most in your free time?", 
                              ["Select", "Building or fixing gadgets (Technical)", "Solving puzzles or coding (Analytical)", "Designing graphics or writing stories (Creative)", "Doing hands-on mechanical work (Practical)", "Helping friends and organizing events (Social)"])
            
            q2 = st.selectbox("2. Which school subject do you look forward to the most?", 
                              ["Select", "Computer Science / Physics", "Mathematics / Economics", "Art / Literature", "Workshop / Biology labs", "Social Studies / Public Speaking"])

            q3 = st.selectbox("3. How do you prefer solving a challenging problem?", 
                              ["Select", "By writing code or setting up hardware", "By analyzing data and calculating metrics", "By brainstorming out-of-the-box visual concepts", "By using physical tools to build a prototype", "By talking it through and collaborating with a team"])

            q4 = st.selectbox("4. What kind of online videos do you watch for fun?", 
                              ["Select", "Tech reviews, robotics, and coding tutorials", "Science experiments, stock market, or puzzles", "Animation, filmmaking, and UI design tutorials", "DIY woodworking, car repair, and crafting", "Psychology, interviews, and community leadership talks"])

            q5 = st.selectbox("5. If you were given a group project, what role would you pick?", 
                              ["Select", "Building the technical backend or app tool", "Handling the research, logic, and data analysis", "Designing the presentation slides and aesthetics", "Assembling the physical model or setup", "Leading the team and presenting to the audience"])

        with col2:
            q6 = st.selectbox("6. Which workplace environment sounds most exciting to you?", 
                              ["Select", "A high-tech software development lab", "A data-driven financial or research firm", "A creative design studio or media agency", "A manufacturing workshop or automated plant", "A community center, school, or corporate HR department"])

            q7 = st.selectbox("7. What is your preferred way to learn a new concept?", 
                              ["Select", "Experimenting directly with code or machines", "Reading statistical reports and logical proofs", "Visualizing through mood boards and sketches", "Learning by doing physical assembly", "Discussing ideas in interactive group sessions"])

            q8 = st.selectbox("8. Which extracurricular activity do you lean towards?", 
                              ["Select", "Robotics club or coding hackathons", "Math olympiad or chess club", "Art club, drama, or graphic design workshop", "Crafts, mechanical tinkering, or sports gear maintenance", "Student council, debate club, or volunteering"])

            q9 = st.selectbox("9. How would your teachers describe your strongest skill?", 
                              ["Select", "Logical troubleshooting and tech-savviness", "Sharp numerical accuracy and problem-solving", "Exceptional creativity and visual presentation", "Excellent manual dexterity and execution speed", "Strong empathy, communication, and leadership"])

            q10 = st.selectbox("10. What is your ideal future job title?", 
                               ["Select", "AI Engineer / Software Developer", "Data Analyst / Research Scientist", "UI/UX Designer / Digital Creator", "Mechatronics / Field Operations Specialist", "Career Counselor / HR & Training Manager"])

        st.markdown("<br>", unsafe_allow_html=True)
        submitted_btn = st.form_submit_button("🚀 Generate My Personalized Career Roadmap")

        if submitted_btn:
            if "Select" in [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10]:
                st.warning("⚠️ Please answer all 10 questions before submitting!")
            else:
                temp_scores = {"Technical": 0, "Analytical": 0, "Creative": 0, "Practical": 0, "Social": 0}
                questions = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10]
                
                for q in questions:
                    if "Technical" in q or "Computer" in q or "Python" in q or "AI" in q: temp_scores["Technical"] += 2
                    if "Analytical" in q or "Math" in q or "Data" in q: temp_scores["Analytical"] += 2
                    if "Creative" in q or "Art" in q or "Design" in q: temp_scores["Creative"] += 2
                    if "Practical" in q or "Workshop" in q or "mechanical" in q: temp_scores["Practical"] += 2
                    if "Social" in q or "Social Studies" in q or "Counselor" in q: temp_scores["Social"] += 2

                st.session_state.scores = temp_scores
                st.session_state.submitted = True
                st.rerun()

# --- DYNAMIC RESULTS & ROADMAP DASHBOARD ---
else:
    scores = st.session_state.scores
    best_category = max(scores, key=scores.get)

    st.success("🎉 Assessment successfully evaluated! Here is your custom-synthesized career guidance profile.")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("### 📊 Your Core Vector Breakdown")
        st.bar_chart(scores)
    
    with col2:
        st.markdown(f"### 🎯 Primary Alignment: {best_category} Track")
        if best_category == "Technical":
            st.info("**Path Profile:** AI & Software Development Track\n\n*Why it matches:* Your responses demonstrate a high affinity for building digital logic, automation, and structured software systems.")
        elif best_category == "Analytical":
            st.info("**Path Profile:** Data Science & Analytics Track\n\n*Why it matches:* You excel at logical evaluation, pattern recognition, and working with quantitative metrics.")
        elif best_category == "Creative":
            st.info("**Path Profile:** Digital Media & UI/UX Design Track\n\n*Why it matches:* Your profile highlights a strong inclination toward visual aesthetics, user experience, and creative media.")
        elif best_category == "Practical":
            st.info("**Path Profile:** Mechatronics & Vocational Tech Track\n\n*Why it matches:* You prefer hands-on mechanics, hardware assembly, and building tangible real-world solutions.")
        else:
            st.info("**Path Profile:** Educational Counseling & Leadership Track\n\n*Why it matches:* You display natural empathy, communication strength, and organizational leadership potential.")

    st.markdown("---")
    st.markdown("### 🗺️ Step-by-Step Strategic Roadmap for Your Career")
    st.write(f"Based on your dominance in the **{best_category}** vector, follow this structured action plan to transition from high school to professional success:")

    # Dynamic Phase Roadmap based on Career Track
    if best_category == "Technical":
        st.markdown("""
        * **Phase 1 (Short-Term - Months 1-3):** Master fundamentals of Python programming and logic building. 
          * *Free Resource:* [Harvard's CS50 Introduction to Computer Science (edX)](https://www.edx.org/course/introduction-computer-science-harvardx-cs50x)
        * **Phase 2 (Medium-Term - Months 4-6):** Build 3 foundational mini-projects (calculator, web scraper, simple automation script) and publish code on GitHub.
          * *Free Resource:* [Programming in Python by NPTEL / IIT Madras (SWAYAM Plus)](https://swayam.gov.in)
        * **Phase 3 (Long-Term - Year 1+):** Participate in high school coding hackathons, build a portfolio website, and apply for technical internships or vocational diplomas.
        """)
    elif best_category == "Analytical":
        st.markdown("""
        * **Phase 1 (Short-Term - Months 1-3):** Build fluency in advanced Excel, statistics, and introductory SQL queries.
          * *Free Resource:* [Introduction to Data Analytics by IBM (edX)](https://www.edx.org)
        * **Phase 2 (Medium-Term - Months 4-6):** Clean a public dataset from Kaggle and build visual dashboards using free tools.
          * *Free Resource:* [Data Analysis and Decision Making Modules (SWAYAM Plus)](https://swayam.gov.in)
        * **Phase 3 (Long-Term - Year 1+):** Complete a data science capstone project and participate in school data challenges.
        """)
    elif best_category == "Creative":
        st.markdown("""
        * **Phase 1 (Short-Term - Months 1-3):** Learn the principles of Design Thinking and user interface layouts.
          * *Free Resource:* [Design Thinking and Creativity Courses (edX)](https://www.edx.org)
        * **Phase 2 (Medium-Term - Months 4-6):** Practice wireframing mobile app screens using the free tier of Figma.
          * *Free Resource:* [UI/UX & Multimedia Modules (SWAYAM Plus)](https://swayam.gov.in)
        * **Phase 3 (Long-Term - Year 1+):** Assemble a digital portfolio of your design projects and collaborate with student developers.
        """)
    elif best_category == "Practical":
        st.markdown("""
        * **Phase 1 (Short-Term - Months 1-3):** Study basic electronics, circuitry, and mechanical assembly fundamentals.
          * *Free Resource:* [Introduction to Engineering and Robotics (edX)](https://www.edx.org)
        * **Phase 2 (Medium-Term - Months 4-6):** Build physical microcontroller starter projects (e.g., Arduino or Raspberry Pi).
          * *Free Resource:* [Technical Trade & Vocational Modules via AICTE (SWAYAM Plus)](https://swayam.gov.in)
        * **Phase 3 (Long-Term - Year 1+):** Enroll in specialized vocational technology certifications or hardware fabrication workshops.
        """)
    else:
        st.markdown("""
        * **Phase 1 (Short-Term - Months 1-3):** Develop active listening, public speaking, and foundational psychology knowledge.
          * *Free Resource:* [Introduction to Psychology and Human Behavior (edX)](https://www.edx.org)
        * **Phase 2 (Medium-Term - Months 4-6):** Take on leadership roles in school clubs, student councils, or community mentoring programs.
          * *Free Resource:* [Educational Psychology & Guidance Frameworks (SWAYAM Plus)](https://swayam.gov.in)
        * **Phase 3 (Long-Term - Year 1+):** Pursue formal training in educational counseling, human resources, or social work.
        """)

    st.markdown("---")
    col_btn1, col_btn2 = st.columns([1, 4])
    with col_btn1:
        if st.button("🔄 Retake Assessment"):
            st.session_state.submitted = False
            st.rerun()

