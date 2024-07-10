import streamlit as st
import matplotlib.pyplot as plt
def main():
    st.title("GPA Estimate Calculator AIML 3-2")
    st.text("Enter the expected GPAs for each course:")
    st.text("Made without love - charan")

    cc = st.number_input("Expected GPA in Cloud Computing", min_value=0.0, max_value=10.0, step=0.1)
    se = st.number_input("Expected GPA in Software Engineering", min_value=0.0, max_value=10.0, step=0.1)
    bda = st.number_input("Expected GPA in BIG DATA ANALYTICS", min_value=0.0, max_value=10.0, step=0.1)
    ml = st.number_input("Expected GPA in MACHINE LEARNING", min_value=0.0, max_value=10.0, step=0.1)
    bdal = st.number_input("Expected GPA in BDA Lab", min_value=0.0, max_value=10.0, step=0.1)
    mll = st.number_input("Expected GPA in ML Lab", min_value=0.0, max_value=10.0, step=0.1)
    mini = st.number_input("Expected GPA in Mini Project", min_value=0.0, max_value=10.0, step=0.1)

    if st.button("Calculate GPA"):
        gpa = (mini * 2) + (bdal * 1.5) + (mll * 1.5) + (cc * 3) + (se * 3) + (bda * 3) + (ml * 3) + (6 * 3)
        result = gpa / 20
        st.success(f"Your GPA is: {result:.2f}")
        categories = ['Mini Project', 'BDA Lab', 'ML Lab', 'CC', 'SE', 'BDA', 'ML', 'Extra Credit']
        gpas = [mini, bdal, mll, cc, se, bda, ml, 6]
        
        fig, ax = plt.subplots(figsize=(10, 6))
        bars = ax.bar(categories, gpas, color='skyblue')
        ax.set_ylabel('Expected GPA')
        ax.set_title('Expected GPAs per Course')
        
        for bar in bars:
            height = bar.get_height()
            ax.annotate(f'{height}',
                        xy=(bar.get_x() + bar.get_width() / 2, height),
                        xytext=(0, 3),
                        textcoords="offset points",
                        ha='center', va='bottom')

        st.pyplot(fig)

if __name__ == "__main__":
    main()
