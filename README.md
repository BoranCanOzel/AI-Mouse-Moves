
# AI Mouse Movement 🖱️

## Overview 📚

This project uses a trained LSTM model to move the mouse cursor on a screen. The movement is controlled by predicting the velocity required to reach a target position.

## Files 🗂️

- **model.py**: Contains the LSTM model definition and a simple neural network class.
- **myAiMove.py**: The main script that utilizes the LSTM model to move the mouse cursor.

## Dependencies 📦

- Python 3.6+
- PyTorch
- NumPy
- pywin32

## Usage 🚀

1. **Install dependencies**:
   ```bash
   pip install torch numpy pywin32
   ```

2. **Run the script**:
   ```bash
   python myAiMove.py <targetX> <targetY> <maxSteps>
   ```
   - `<targetX>`: X-coordinate of the target position.
   - `<targetY>`: Y-coordinate of the target position.
   - `<maxSteps>`: Maximum number of steps for the cursor to reach the target.

## Example 🎯

```bash
python myAiMove.py 500 300 50
```

