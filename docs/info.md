## How it works

This project implements a 1-bit full adder.

A full adder is a combinational circuit that adds three 1-bit inputs:
- A
- B
- Cin

It produces two outputs:
- Sum
- Cout

The logic is:
- Sum = A XOR B XOR Cin
- Cout = (A AND B) OR (Cin AND (A XOR B))

## How to test

Apply all 8 input combinations and verify the outputs using the truth table.

| A | B | Cin | Sum | Cout |
|---|---|-----|-----|------|
| 0 | 0 | 0   | 0   | 0    |
| 0 | 0 | 1   | 1   | 0    |
| 0 | 1 | 0   | 1   | 0    |
| 0 | 1 | 1   | 0   | 1    |
| 1 | 0 | 0   | 1   | 0    |
| 1 | 0 | 1   | 0   | 1    |
| 1 | 1 | 0   | 0   | 1    |
| 1 | 1 | 1   | 1   | 1    |

## External hardware

None

## Pinout

### Inputs
- ui[0] = A
- ui[1] = B
- ui[2] = Cin

### Outputs
- uo[0] = Sum
- uo[1] = Cout
