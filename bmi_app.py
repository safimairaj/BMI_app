import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Set page configuration
st.set_page_config(
    page_title="BMI Calculator & Health Guide",
    page_icon="💪",
    layout="wide"
)

def calculate_bmi(weight, height):
    """Calculate BMI given weight in kg and height in cm"""
    height_m = height / 100  # Convert cm to meters
    bmi = weight / (height_m ** 2)
    return round(bmi, 1)

def get_bmi_category(bmi):
    """Get BMI category based on WHO standards"""
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def get_positive_message(category, bmi):
    """Get positive, encouraging message based on BMI category"""
    messages = {
        "Underweight": f"Your BMI is {bmi}. Every body is unique and beautiful! If you'd like to gain some healthy weight, we have some great tips for you. Remember, small consistent steps lead to amazing results! 🌟",
        "Normal weight": f"Fantastic! Your BMI is {bmi}, which falls in the healthy range. You're doing great at maintaining your health. Keep up the wonderful work! 🎉",
        "Overweight": f"Your BMI is {bmi}. You're on a journey to better health, and that's something to be proud of! With some positive changes, you can reach your goals. Every small step counts! 💪",
        "Obese": f"Your BMI is {bmi}. Thank you for taking this important step towards better health! You have the power to make positive changes. Let's explore some encouraging strategies together! 🌈"
    }
    return messages[category]

def get_healthy_weight_range(height):
    """Calculate healthy weight range for given height"""
    height_m = height / 100
    min_weight = round(18.5 * (height_m ** 2), 1)
    max_weight = round(24.9 * (height_m ** 2), 1)
    return min_weight, max_weight

def get_recommendations(category, current_weight, target_min, target_max):
    """Get personalized recommendations based on BMI category"""
    
    recommendations = {
        "Underweight": {
            "goal": f"Aim to gradually gain weight to reach {target_min}-{target_max} kg",
            "tips": [
                "🥜 **Nutrient-dense calories**: Add healthy fats like nuts, avocados, and olive oil to your meals",
                "🍽️ **Frequent meals**: Eat 5-6 smaller meals throughout the day instead of 3 large ones",
                "💪 **Strength training**: Build muscle mass with resistance exercises 2-3 times per week",
                "🥛 **Protein power**: Include protein-rich foods like eggs, fish, dairy, and legumes",
                "🍌 **Healthy snacks**: Try smoothies, nuts, dried fruits, and whole grain crackers",
                "💧 **Stay hydrated**: Drink plenty of water, but avoid filling up on liquids before meals"
            ]
        },
        "Normal weight": {
            "goal": "Maintain your current healthy weight range",
            "tips": [
                "🏃 **Stay active**: Continue regular physical activity - aim for 150 minutes of moderate exercise weekly",
                "🥗 **Balanced diet**: Keep eating a variety of fruits, vegetables, whole grains, and lean proteins",
                "⚖️ **Regular monitoring**: Check your weight monthly to maintain your healthy range",
                "😴 **Quality sleep**: Maintain 7-9 hours of good sleep for optimal health",
                "🧘 **Stress management**: Practice stress-reduction techniques like meditation or yoga",
                "🎯 **Consistency**: Keep up your healthy habits - you're doing amazingly well!"
            ]
        },
        "Overweight": {
            "goal": f"Gradually work towards {target_min}-{target_max} kg through sustainable lifestyle changes",
            "tips": [
                "🚶 **Start moving**: Begin with 30 minutes of walking daily - it's free and effective!",
                "🍎 **Portion awareness**: Use smaller plates and listen to your hunger cues",
                "🥦 **Veggie power**: Fill half your plate with colorful vegetables at each meal",
                "💧 **Hydrate smart**: Drink water before meals and replace sugary drinks with water",
                "📱 **Track progress**: Keep a food diary or use an app to monitor your eating patterns",
                "🎯 **Small goals**: Aim to lose 1-2 pounds per week through sustainable changes"
            ]
        },
        "Obese": {
            "goal": f"Work towards {target_min}-{target_max} kg with support from healthcare professionals",
            "tips": [
                "👩‍⚕️ **Professional support**: Consider consulting with a doctor, nutritionist, or dietitian",
                "🐢 **Slow and steady**: Focus on gradual, sustainable changes rather than quick fixes",
                "🏊 **Low-impact exercise**: Try swimming, walking, or cycling to protect your joints",
                "🍽️ **Meal planning**: Prepare healthy meals in advance to avoid impulsive food choices",
                "👥 **Support network**: Join a support group or find an accountability partner",
                "🎉 **Celebrate wins**: Acknowledge every positive change, no matter how small!"
            ]
        }
    }
    
    return recommendations[category]

# Main app
st.title("💪 BMI Calculator & Your Personal Health Guide")
st.write("Welcome to your friendly BMI calculator! Let's discover where you stand and create a positive path forward. 🌟")

# Create two columns for input
col1, col2 = st.columns(2)

with col1:
    st.subheader("📏 Your Measurements")
    
    # Unit selection
    unit_system = st.radio("Choose your preferred units:", ["Metric (kg/cm)", "Imperial (lbs/ft-in)"])
    
    if unit_system == "Metric (kg/cm)":
        weight = st.number_input("Weight (kg):", min_value=20.0, max_value=300.0, value=70.0, step=0.1)
        height = st.number_input("Height (cm):", min_value=100.0, max_value=250.0, value=170.0, step=0.1)
    else:
        weight_lbs = st.number_input("Weight (lbs):", min_value=44.0, max_value=660.0, value=154.0, step=0.1)
        feet = st.number_input("Height (feet):", min_value=3, max_value=8, value=5, step=1)
        inches = st.number_input("Height (inches):", min_value=0, max_value=11, value=7, step=1)
        
        # Convert to metric
        weight = weight_lbs * 0.453592  # Convert lbs to kg
        height = (feet * 12 + inches) * 2.54  # Convert ft-in to cm

with col2:
    st.subheader("🎯 Your Results")
    
    if weight and height:
        bmi = calculate_bmi(weight, height)
        category = get_bmi_category(bmi)
        
        # Display BMI with color coding
        if category == "Normal weight":
            st.success(f"**Your BMI: {bmi}**")
        elif category == "Underweight" or category == "Overweight":
            st.warning(f"**Your BMI: {bmi}**")
        else:
            st.info(f"**Your BMI: {bmi}**")
        
        st.write(f"**Category:** {category}")
        
        # Positive message
        st.info(get_positive_message(category, bmi))

# BMI Visualization
if weight and height:
    st.subheader("📊 BMI Visualization")
    
    # Create BMI scale visualization
    fig, ax = plt.subplots(figsize=(12, 3))
    
    # BMI ranges
    ranges = [0, 18.5, 25, 30, 40]
    colors = ['lightblue', 'lightgreen', 'orange', 'lightcoral']
    labels = ['Underweight\n(<18.5)', 'Normal\n(18.5-24.9)', 'Overweight\n(25-29.9)', 'Obese\n(≥30)']
    
    for i in range(len(ranges)-1):
        ax.barh(0, ranges[i+1]-ranges[i], left=ranges[i], color=colors[i], alpha=0.7, height=0.5)
        ax.text((ranges[i]+ranges[i+1])/2, 0, labels[i], ha='center', va='center', fontweight='bold')
    
    # Mark user's BMI
    ax.plot(bmi, 0, 'ro', markersize=15, markeredgecolor='darkred', markeredgewidth=2)
    ax.text(bmi, 0.3, f'Your BMI\n{bmi}', ha='center', va='center', fontweight='bold', 
            bbox=dict(boxstyle="round,pad=0.3", facecolor="yellow", alpha=0.7))
    
    ax.set_xlim(15, 35)
    ax.set_ylim(-0.5, 0.8)
    ax.set_xlabel('BMI Value', fontsize=12, fontweight='bold')
    ax.set_title('BMI Scale - Where You Stand', fontsize=14, fontweight='bold')
    ax.set_yticks([])
    ax.grid(True, alpha=0.3)
    
    st.pyplot(fig)
    
    # Healthy weight range
    min_weight, max_weight = get_healthy_weight_range(height)
    st.subheader("🎯 Your Healthy Weight Range")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Current Weight", f"{weight:.1f} kg")
    with col2:
        st.metric("Healthy Range", f"{min_weight}-{max_weight} kg")
    with col3:
        if category == "Normal weight":
            st.metric("Status", "Perfect! ✅", delta="Maintain")
        elif category == "Underweight":
            needed = min_weight - weight
            st.metric("To Gain", f"{needed:.1f} kg", delta=f"+{needed:.1f}")
        else:
            needed = weight - max_weight
            st.metric("To Lose", f"{needed:.1f} kg", delta=f"-{needed:.1f}")

# Recommendations section
if weight and height:
    st.subheader("🌟 Your Personalized Action Plan")
    
    recommendations = get_recommendations(category, weight, min_weight, max_weight)
    
    st.write(f"**Goal:** {recommendations['goal']}")
    st.write("**Here's your personalized roadmap to success:**")
    
    for tip in recommendations['tips']:
        st.write(f"• {tip}")

# Additional health tips
st.subheader("💡 Universal Health Tips for Everyone")
st.write("Regardless of your BMI, these habits will boost your overall well-being:")

tips_col1, tips_col2 = st.columns(2)

with tips_col1:
    st.write("""
    **🥗 Nutrition Fundamentals:**
    - Eat the rainbow - colorful fruits and vegetables
    - Choose whole grains over refined ones
    - Include lean proteins in every meal
    - Limit processed foods and added sugars
    - Practice mindful eating
    """)

with tips_col2:
    st.write("""
    **🏃 Lifestyle Essentials:**
    - Move your body daily - find activities you enjoy
    - Prioritize 7-9 hours of quality sleep
    - Manage stress through relaxation techniques
    - Stay hydrated throughout the day
    - Build a supportive community
    """)

# Disclaimer
st.markdown("---")
st.write("⚠️ **Important Note:** This BMI calculator is for educational purposes only. BMI doesn't account for muscle mass, bone density, or overall body composition. Always consult with healthcare professionals for personalized medical advice and before making significant changes to your diet or exercise routine.")

st.markdown("*Remember: Your worth isn't defined by a number. You're taking positive steps towards better health, and that's what truly matters! 💙*")
