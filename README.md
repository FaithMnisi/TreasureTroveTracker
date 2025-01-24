# TreasureTroveTracker 💰  

## Overview  
**TreasureTroveTracker** is a versatile financial calculator that allows users to easily calculate investment growth or bond repayments. Designed with simplicity and user-friendliness in mind, this tool provides clear calculations and robust error handling for a seamless user experience.  

## Features  
1. **Menu Options**:  
   - **Investment**: Choose between simple and compound interest to calculate the future value of an investment.  
   - **Bond**: Calculate the monthly repayment amount for a bond (loan).  
   - **Exit**: Close the program at any time.  

2. **Investment Calculations**:  
   - **Simple Interest**: Calculates returns based on a fixed interest rate over the chosen time period.  
   - **Compound Interest**: Calculates returns where interest is reinvested annually.  
   - User Inputs:  
     - Principal amount  
     - Interest rate (as a percentage, e.g., 7)  
     - Investment duration (in years)  

3. **Bond Calculations**:  
   - Calculates monthly repayment amounts for a bond (loan).  
   - User Inputs:  
     - Present value of the house  
     - Interest rate (as a percentage, e.g., 7)  
     - Repayment period (in months)  

4. **Error Handling**:  
   - Displays error messages for invalid menu choices (e.g., selecting an unavailable option).  
   - Prompts users to enter valid inputs for investment type (simple or compound).  
   - Exits the program automatically after three invalid attempts to choose an investment type.  

5. **Menu Navigation**:  
   - Users can return to the main menu after completing a calculation or exit the program directly.  

## Usage  
1. Launch the program and choose an option: **investment**, **bond**, or **exit**.  
2. If choosing **investment**, select the interest type (**simple** or **compound**) and enter the required details to see the total value of your investment.  
3. If choosing **bond**, input the required details to calculate the monthly repayment amount.  
4. Return to the menu or exit the program after each calculation.  

## Example Outputs  
- **Investment (Compound Interest)**:  
  ```
  The total investment amount after 5 years will be R14025.52  
  ```  

- **Bond (Monthly Repayment)**:  
  ```
  The monthly repayment amount for your bond will be R1936.43  
  ```  

## Error Handling  
- Invalid menu selections display:  
  `"Error: Please choose 'investment', 'bond', or 'exit'."`  
- Invalid interest type inputs display:  
  `"Error: Please choose 'simple' or 'compound'."`  
- Program exits after three incorrect investment type entries:  
  `"Too many invalid attempts. Exiting program."`  

## Benefits  
- Provides quick and easy calculations for investments and bonds.  
- Ensures smooth user interaction with clear instructions and error messages.  
- Handles invalid inputs gracefully, avoiding crashes or confusing results.  
