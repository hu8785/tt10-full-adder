import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles

@cocotb.test()
async def test_project(dut):
    dut._log.info("Start")
    clock = Clock(dut.clk, 10, units="us")
    cocotb.start_soon(clock.start())

    # Reset
    dut.ena.value = 1
    dut.ui_in.value = 0
    dut.uio_in.value = 0
    dut.rst_n.value = 0
    await ClockCycles(dut.clk, 10)
    dut.rst_n.value = 1

    # A=0, B=0, Cin=0 → Sum=0, Cout=0
    dut.ui_in.value = 0b00000000
    await ClockCycles(dut.clk, 25)
    assert dut.uo_out[0].value == 0
    assert dut.uo_out[1].value == 0

    # A=0, B=0, Cin=1 → Sum=1, Cout=0
    dut.ui_in.value = 0b00000100
    await ClockCycles(dut.clk, 25)
    assert dut.uo_out[0].value == 1
    assert dut.uo_out[1].value == 0

    # A=0, B=1, Cin=0 → Sum=1, Cout=0
    dut.ui_in.value = 0b00000010
    await ClockCycles(dut.clk, 25)
    assert dut.uo_out[0].value == 1
    assert dut.uo_out[1].value == 0

    # A=0, B=1, Cin=1 → Sum=0, Cout=1
    dut.ui_in.value = 0b00000110
    await ClockCycles(dut.clk, 25)
    assert dut.uo_out[0].value == 0
    assert dut.uo_out[1].value == 1

    # A=1, B=0, Cin=0 → Sum=1, Cout=0
    dut.ui_in.value = 0b00000001
    await ClockCycles(dut.clk, 25)
    assert dut.uo_out[0].value == 1
    assert dut.uo_out[1].value == 0

    # A=1, B=0, Cin=1 → Sum=0, Cout=1
    dut.ui_in.value = 0b00000101
    await ClockCycles(dut.clk, 25)
    assert dut.uo_out[0].value == 0
    assert dut.uo_out[1].value == 1

    # A=1, B=1, Cin=0 → Sum=0, Cout=1
    dut.ui_in.value = 0b00000011
    await ClockCycles(dut.clk, 25)
    assert dut.uo_out[0].value == 0
    assert dut.uo_out[1].value == 1

    # A=1, B=1, Cin=1 → Sum=1, Cout=1
    dut.ui_in.value = 0b00000111
    await ClockCycles(dut.clk, 25)
    assert dut.uo_out[0].value == 1
    assert dut.uo_out[1].value == 1
