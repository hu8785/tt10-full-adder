<!--
How it works
-->

## How it works

A **1-bit Full Adder** adds three single-bit inputs — A, B, and Cin (carry-in) — and produces two outputs:

- **Sum** = A XOR B XOR Cin
- **Cout** = (A AND B) OR (Cin AND (A XOR B))

The design uses combinational logic only (no clock required). The XOR operation produces the Sum bit, and the carry-out (Cout) is high whenever at least two of the three inputs are logic 1.

**Pinout:**

| Pin       | Signal | Direction |
|-----------|--------|-----------|
| ui_in[0]  | A      | Input     |
| ui_in[1]  | B      | Input     |
| ui_in[2]  | Cin    | Input     |
| uo_out[0] | Sum    | Output    |
| uo_out[1] | Cout   | Output    |

**Truth Table:**

| A | B | Cin | Sum | Cout |
|---|---|-----|-----|------|
| 0 | 0 |  0  |  0  |  0   |
| 0 | 0 |  1  |  1  |  0   |
| 0 | 1 |  0  |  1  |  0   |
| 0 | 1 |  1  |  0  |  1   |
| 1 | 0 |  0  |  1  |  0   |
| 1 | 0 |  1  |  0  |  1   |
| 1 | 1 |  0  |  0  |  1   |
| 1 | 1 |  1  |  1  |  1   |

## How to test

Apply all 8 input combinations using:
- `ui_in[0]` = A
- `ui_in[1]` = B
- `ui_in[2]` = Cin

Check the outputs:
- `uo_out[0]` = Sum
- `uo_out[1]` = Cout

Verify each output against the truth table above.

Test sequence used in cocotb testbench:

```
A=0, B=0, Cin=0 → Sum=0, Cout=0
A=0, B=0, Cin=1 → Sum=1, Cout=0
A=0, B=1, Cin=0 → Sum=1, Cout=0
A=0, B=1, Cin=1 → Sum=0, Cout=1
A=1, B=0, Cin=0 → Sum=1, Cout=0
A=1, B=0, Cin=1 → Sum=0, Cout=1
A=1, B=1, Cin=0 → Sum=0, Cout=1
A=1, B=1, Cin=1 → Sum=1, Cout=1
```

## External hardware

None
!---

This file is used to generate your project datasheet. Please fill in the information below and delete any unused
sections.

You can also include images in this folder and reference them in the markdown. Each image must be less than
512 kb in size, and the combined size of all images must be less than 1 MB.
-->

