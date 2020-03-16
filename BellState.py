import cirq

(q1,q2) = cirq.GridQubit.rect(1 ,2)
c = cirq.Circuit(cirq.H(q1) , cirq.CNOT(q1,q2))
ZZ = cirq.Z( q1 ) * cirq .Z ( q2 )
bell = cirq.Simulator().simulate (c).final_state
expectation = ZZ.expectation_from_wavefunction (bell,dict(zip ([ q1 , q2 ] ,[0 ,1]) ))