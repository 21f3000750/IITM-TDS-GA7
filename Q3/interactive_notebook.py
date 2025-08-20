import marimo as mo

# Email: 21f3000750@ds.study.iitm.ac.in

# Cell 1: This cell initializes the interactive components.
# The 'slider' widget provides the input value 'x'. Other cells
# will reactively update when its value changes.
slider = mo.ui.slider(start=1, stop=25, step=1, value=5, label="Select a value for x:")

# This cell simply displays the slider widget in the notebook output.
slider

# Cell 2: This cell's execution depends on the value from the 'slider' in Cell 1.
# It calculates the square of the slider's current value and stores it.
# This demonstrates a direct dependency on a widget's state.
x_squared = slider.value**2

# Cell 3: This cell's output depends on both 'slider' and 'x_squared'.
# It uses an f-string inside mo.md to create a dynamic markdown display
# that updates automatically whenever the slider is moved.
mo.md(
    f"""
    ## 📊 Interactive Analysis

    This notebook demonstrates the relationship between an input variable and its calculated outputs.

    ### Current Values:
    - **Selected value (x):** {slider.value}
    - **Squared value (x²):** {x_squared}

    *Change the slider's position to see how the output text updates in real-time.*
    """
)
