from qiskit import QuantumCircuit
from qiskit_ibm_runtime import QiskitRuntimeService

with open('token_api_key.txt', 'r') as file:
    token = file.read().strip()

service = QiskitRuntimeService(channel="ibm_quantum",
                               token = token)
