import cirq
import sympy

theta = sympy.Symbol('theta')
c = cirq.Circuit(cirq.Rx(theta).on(q1))
resolver = cirq.ParamResolver({ theta :1})
results = cirq.Simulator().simulate(c,resolver)