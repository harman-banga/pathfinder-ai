import streamlit as st

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="PathFinder AI", 
    page_icon="🎯", 
    layout="wide", 
    initial_sidebar_state="expanded"
)

# --- PROFESSIONAL UI/UX CSS STYLING ---
st.markdown("""
    <style>
    .main {
        background-color: #0E1117;
        color: #FFFFFF;
    }
    .stButton>button {
        background: linear-gradient(90deg, #6C63FF 0%, #4834DF 100%);
        color: white;
        border-radius: 8px;
        padding: 0.6rem 1.5rem;
        font-weight: bold;
        border: none;
        box-shadow: 0 4px 12px rgba(108, 99, 255, 0.3);
    }
    .stButton>button:hover {
        background: linear-gradient(90deg, #5b52e3 0%, #3d2bc7 100%);
        color: #ffffff;
    }
    .card {
        background-color: #1A1C24;
        padding: 1.5rem;
        border-radius: 12px;
        border: 1px solid #2D303E;
        margin-bottom: 1rem;
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
        {"role": "assistant", "content": "Hello! I'm your PathFinder AI mentor. Ask me anything about career paths, skills, or what specific engineers and professionals do!"}
    ]

# --- SIDEBAR: ALWAYS-ON AI CHATBOT & API SETTINGS ---
with st.sidebar:
    st.image("https://img.icons8.com/fluency/96/artificial-intelligence.png", width=60)
    st.title("PathFinder AI")
    st.markdown("---")
    
    st.subheader("🤖 AI Career Mentor Chat")
    st.write("Ask any question about careers (e.g., *'What does an AI/ML engineer do?'*)")
    
    # Optional API Key for live AI responses
    api_key_input = st.text_input("Gemini API Key (Optional):", type="password", help="Leave blank to use built-in smart responses for your demo.")
    
    # Chat History Container
    chat_container = st.container(height=300)
    with chat_container:
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])

    if prompt := st.chat_input("Ask a career question..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        # Generate response (supports real Gemini API if key is provided, with a foolproof fallback)
        response = ""
        if api_key_input:
            try:
                import google.generativeai as genai
                genai.configure(api_key=api_key_input)
                model = genai.GenerativeModel('gemini-1.5-flash')
                chat_res = model.generate_content(f"You are a helpful career counselor for high school students. Answer this question concisely: {prompt}")
                response = chat_res.text
            except Exception as e:
                response = f"API Error: {e}. Using fallback mode: AI/ML Engineers build intelligent software systems that learn from data using Python, math, and machine learning models!"
        else:
            # Smart Fallbacks for Hackathon Demo
            p_lower = prompt.lower()
            if "ai" in p_lower or "ml" in p_lower or "engineer" in p_lower:
                response = "**AI/ML Engineers** design and build intelligent systems that allow computers to learn from data. They use Python, mathematics, and machine learning algorithms to solve complex automation problems!"
            elif "design" in p_lower or "ui/ux" in p_lower:
                response = "**UI/UX Designers** focus on creating intuitive, visually stunning, and user-friendly digital interfaces for apps and websites using tools like Figma."
            elif "data" in p_lower:
                response = "**Data Analysts** examine large sets of numbers and information to help organizations make smart, evidence-based decisions using SQL, Excel, and Python."
            else:
                response = f"That's a fantastic question regarding '{prompt}'! For high-school students exploring this field, we recommend starting with foundational free courses on edX or SWAYAM Plus, building small hands-on projects, and talking to a mentor."

        st.session_state.messages.append({"role": "assistant", "content": response})
        st.rerun()

# --- MAIN CONTENT AREA ---
st.title("🎯 PathFinder AI: Career Discovery Platform")
st.markdown("##### Empowering high-school students to discover vocational and technical career tracks through guided interest assessment.")
st.markdown("---")

# --- 10-QUESTION ASSESSMENT FORM ---
if not st.session_state.submitted:
    st.subheader("📝 Step 1: 10-Question Interest Assessment")
    st.write("Answer the questions below honestly. Our internal recommendation engine will map your strengths instantly upon submission.")

    with st.form("assessment_form"):
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

        submitted_btn = st.form_submit_button("🚀 Submit & Generate My Career Roadmap")

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

# --- RESULTS DASHBOARD (Automatically displayed after submission) ---
else:
    scores = st.session_state.scores
    best_category = max(scores, key=scores.get)

    st.success("🎉 Assessment Analyzed Successfully! Here is your customized career guidance report.")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("### 📊 Your Interest Vector Breakdown")
        st.bar_chart(scores)
    
    with col2:
        st.markdown(f"### 🎯 Primary Match: {best_category} Track")
        if best_category == "Technical":
            st.info("**Recommended Career Path:** AI & Software Development Track\n\n*Why it matches:* You show a strong inclination toward writing code, building digital systems, and automating processes.")
        elif best_category == "Analytical":
            st.info("**Recommended Career Path:** Data Science & Analytics Track\n\n*Why it matches:* You excel at logical evaluation, pattern recognition, and working with data metrics.")
        elif best_category == "Creative":
            st.info("**Recommended Career Path:** Digital Media & UI/UX Design Track\n\n*Why it matches:* Your responses demonstrate a high affinity for visual aesthetics, media, and creative user experiences.")
        elif best_category == "Practical":
            st.info("**Recommended Career Path:** Mechatronics & Vocational Tech Track\n\n*Why it matches:* You prefer hands-on mechanics, hardware setup, and building physical operational tools.")
        else:
            st.info("**Recommended Career Path:** Educational Counseling & HR Track\n\n*Why it matches:* You display natural empathy, communication strength, and leadership potential.")

    st.markdown("---")
    st.markdown("### 📚 Dynamic Free Learning Roadmap & Modules")
    st.write(f"Based on your highest score in **{best_category}**, our engine has dynamically curated these free university-backed modules:")

    # Dynamic Module Selector based on User Score
    if best_category == "Technical":
        st.markdown("- **edX Free Audit:** [Harvard's CS50 Introduction to Computer Science](https://www.edx.org/course/introduction-computer-science-harvardx-cs50x)")
        st.markdown("- **SWAYAM Plus Portal:** [Programming in Python by NPTEL / IIT Madras](https://swayam.gov.in)")
        st.markdown("- **Actionable Step:** Build 3 mini-Python scripts this week and upload your code to GitHub.")
    elif best_category == "Analytical":
        st.markdown("- **edX Free Audit:** [Introduction to Data Analytics by IBM](https://www.edx.org)")
        st.markdown("- **SWAYAM Plus Portal:** [Data Analysis and Decision Making courses](https://swayam.gov.in)")
        st.markdown("- **Actionable Step:** Learn basic Excel formulas and SQL queries through free online tutorials.")
    elif best_category == "Creative":
        st.markdown("- **edX Free Audit:** [Design Thinking and Creativity from top universities](https://www.edx.org)")
        st.markdown("- **SWAYAM Plus Portal:** [UI/UX and Multimedia Design Modules](https://swayam.gov.in)")
        st.markdown("- **Actionable Step:** Create a wireframe of a mobile app using the free version of Figma.")
    elif best_category == "Practical":
        st.markdown("- **edX Free Audit:** [Introduction to Engineering and Robotics](https://www.edx.org)")
        st.markdown("- **SWAYAM Plus Portal:** [Technical Trade & Vocational Modules via AICTE](https://swayam.gov.in)")
        st.markdown("- **Actionable Step:** Explore basic electronics assembly or Arduino starter projects.")
    else:
        st.markdown("- **edX Free Audit:** [Introduction to Psychology and Human Behavior](https://www.edx.org)")
        st.markdown("- **SWAYAM Plus Portal:** [Educational Psychology & Guidance Frameworks](https://swayam.gov.in)")
        st.markdown("- **Actionable Step:** Participate in school debates, peer mentoring, or community leadership activities.")

    st.markdown("---")
    if st.button("🔄 Retake Assessment"):
        st.session_state.submitted = False
        st.rerun()

