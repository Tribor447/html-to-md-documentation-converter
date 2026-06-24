# QuMat

## Navigation

- [QuMat Documentation](#index)
- [Getting Started](#qumat-getting-started)
  - [Getting Started](#qumat-getting-started)
- [Qumat (Circuits)](#qumat)
  - [Basic Gates](#qumat-basic-gates)
  - [Parameterized Circuits](#qumat-parameterized-circuits)
  - [Api](#qumat-api)
  - [Core Concepts - Qumat](#qumat-concepts)
  - [Examples - Qumat](#qumat-examples)
- [QDP (Data Encoding)](#qdp)
  - [Getting Started with QDP](#qdp-getting-started)
  - [Core Concepts - QDP](#qdp-concepts)
  - [API Reference - QDP](#qdp-api)
  - [Examples - QDP](#qdp-examples)
  - [Internals](#qdp-readers)
    - [Readers](#qdp-readers)
    - [Observability](#qdp-observability)
    - [Testing](#qdp-testing)
- [Advanced Topics](#advanced-pqc)
  - [Pqc](#advanced-pqc)
  - [Gap Analysis](#advanced-gap-analysis)
- [Quantum Computing Primer](#learning-quantum-computing-primer)
  - [Introduction to Quantum Computing](#learning-quantum-computing-primer-introduction)
  - [Quantum Bits (Qubits)](#learning-quantum-computing-primer-qubits)
  - [Quantum Gates](#learning-quantum-computing-primer-quantum-gates)
  - [Quantum Circuits](#learning-quantum-computing-primer-quantum-circuits)
  - [Quantum Entanglement](#learning-quantum-computing-primer-quantum-entanglement)
  - [Quantum Algorithms](#learning-quantum-computing-primer-quantum-algorithms)
  - [Quantum Error Correction](#learning-quantum-computing-primer-quantum-error-correction)
  - [Applications of Quantum Computing](#learning-quantum-computing-primer-applications)
  - [Advanced Topics](#learning-quantum-computing-primer-advanced-topics)
- [Research Papers](#learning-papers)
  - [Summary of 'An Efficient Quantum Factoring Algorithm'](#learning-papers-an-efficient-quantum-factoring-algorithm)
  - [Summary of 'Quantum Kernel Estimation With Neutral Atoms For Supervised Classification: A Gate-Based Approach'](#learning-papers-quantum-kernel-estimation-with-neutral-atoms-for-supervised-classification)
  - [Summary of 'Quantum machine learning beyond kernel methods'](#learning-papers-quantum-machine-learning-beyond-kernel-methods)
  - [Summary of 'Unleashing the Potential of LLMs for Quantum Computing: A Study in Quantum Architecture Design'](#learning-papers-unleashing-the-potential-of-llms-for-quantum-computing)
- [Community](#community)
  - [Who Are We?](#community-who-we-are)
  - [Mailing Lists, IRC and Archives](#community-mailing-lists)
  - [Code of Conduct](#community-code-of-conduct)
- [Contributing](#about-how-to-contribute)
  - [How To Contribute](#about-how-to-contribute)

## Content

<a id="index"></a>

<!-- source_url: https://mahout.apache.org/docs/ -->

<!-- page_index: 1 -->

# QuMat

Version: latest

![QuMat Logo](assets/images/mascot-with-text-adde2e49824f2c7fd0a05eff83e9f3cc_8fce0f64aba911d6.png)

QuMat is a high level Python library for interfacing with multiple
quantum computing backends. It is designed to be easy to use and to abstract
the particularities of each backend, so that you may 'write once, run
anywhere.'

- [Getting Started with QuMat](#qumat-getting-started) - Introduction and setup guide

- [Basic Gates](#qumat-basic-gates) - Introduction to fundamental quantum gates (NOT, Hadamard, CNOT, Toffoli, SWAP, Pauli gates, CSWAP, U gate)
- [Parameterized Quantum Circuits and Rotation Gates](#qumat-parameterized-circuits) - Rotation gates (Rx, Ry, Rz) and creating/optimizing parameterized circuits

- [API Documentation](#qumat-api) - Complete reference for all QuMat class methods

- [Parameterized Quantum Circuits: Developer's Guide](#advanced-pqc) - In-depth guide to PQCs
- [Qumat Gap Analysis for PQC](#advanced-gap-analysis) - Analysis of PQC capabilities

- [Qumat (Circuits)](#qumat) - Quantum circuit abstraction layer
- [QDP (Quantum Data Plane)](#qdp) - GPU-accelerated data encoding

---

<a id="qumat-getting-started"></a>

<!-- source_url: https://mahout.apache.org/docs/qumat/getting-started/ -->

<!-- page_index: 2 -->

# Getting Started with Qumat

Version: latest

Install Qumat from PyPI:

```bash
pip install qumat 
```

Install with QDP (Quantum Data Plane) support:

```bash
pip install qumat[qdp] 
```

For development or the latest changes, use [uv](https://docs.astral.sh/uv/):

```bash
git clone https://github.com/apache/mahout.git 
cd mahout 
pip install uv 
uv sync                     # Core Qumat 
uv sync --extra qdp         # With QDP (requires NVIDIA GPU + CUDA) 
```

> [!NOTE]
> **Why uv?**
> The project uses `uv` to handle dependency overrides required for Python 3.10+ compatibility with some backend dependencies.

```python
from qumat import QumatCircuit 
 
circuit = QumatCircuit(2) 
circuit.h(0) 
circuit.cx(0, 1) 
result = circuit.run() 
print(result) 
```

Prior to installation, ensure Python 3.10-3.12 is installed. Dependencies such as Qiskit, Cirq, and Amazon Braket SDK are managed automatically.

Official source releases are available at [apache.org/dist/mahout](http://www.apache.org/dist/mahout).

To verify the integrity of a downloaded release:

```bash
gpg --import KEYS 
gpg --verify mahout-qumat-0.5.zip.asc mahout-qumat-0.5.zip 
```

Refer to repository examples:

- `examples/Simple_Example.ipynb`
- `examples/Optimization_Example.ipynb`

- [Basic Gates](#qumat-basic-gates)
- [API Reference](#qumat-api)
- [QDP Getting Started](#qdp-getting-started)

---

<a id="qumat"></a>

<!-- source_url: https://mahout.apache.org/docs/qumat/ -->

<!-- page_index: 3 -->

# Qumat

Version: latest

Qumat is a high-level Python library for quantum computing that provides:

- **Quantum Circuit Abstraction** - Build quantum circuits with standard gates (Hadamard, CNOT, Pauli, etc.) and run them on Qiskit, Cirq, or Amazon Braket with a single unified API. Write once, execute anywhere.
- **QDP (Quantum Data Plane)** - Encode classical data into quantum states using GPU-accelerated kernels. Zero-copy tensor transfer via DLPack lets you move data between PyTorch, NumPy, and TensorFlow without overhead.

- [Getting Started](#qumat-getting-started)
- [Basic Gates](#qumat-basic-gates)
- [Parameterized Circuits](#qumat-parameterized-circuits)
- [API Reference](#qumat-api)
- [Core Concepts](#qumat-concepts)
- [Examples](#qumat-examples)

- [QDP (Quantum Data Plane)](#qdp)
- [Quantum Computing Primer](#learning-quantum-computing-primer)
- [Research Papers](#learning-papers)

---

<a id="qumat-basic-gates"></a>

<!-- source_url: https://mahout.apache.org/docs/qumat/basic-gates/ -->

<!-- page_index: 4 -->

# Quantum Gate Explanations

Version: latest

The NOT gate, also called the **Pauli X Gate**, is a fundamental quantum gate used to flip the state of a qubit. It is often referred to as a bit-flip gate. When applied to a qubit in the

<math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>∣</mi><mn>0</mn><mo>⟩</mo></mrow><annotation>|0\rangle</annotation></semantics></math>

∣0⟩ state, it changes it to the

<math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>∣</mi><mn>1</mn><mo>⟩</mo></mrow><annotation>|1\rangle</annotation></semantics></math>

∣1⟩ state, and vice versa. Mathematically, if

<math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>∣</mi><mi>ψ</mi><mo>⟩</mo></mrow><annotation>|\psi\rangle</annotation></semantics></math>

∣ψ⟩ represents the qubit's state, applying the X-gate results in:

<math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>X</mi><mi>∣</mi><mi>ψ</mi><mo>⟩</mo><mo>=</mo><mi>∣</mi><mi>¬</mi><mi>ψ</mi><mo>⟩</mo></mrow><annotation>X|\psi\rangle = |\neg\psi\rangle</annotation></semantics></math>

X∣ψ⟩=∣¬ψ⟩

The Hadamard gate, denoted as the H-gate, is used to create superposition states. When applied to a qubit in the

<math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>∣</mi><mn>0</mn><mo>⟩</mo></mrow><annotation>|0\rangle</annotation></semantics></math>

∣0⟩ state, it transforms it into an equal superposition of

<math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>∣</mi><mn>0</mn><mo>⟩</mo></mrow><annotation>|0\rangle</annotation></semantics></math>

∣0⟩ and

<math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>∣</mi><mn>1</mn><mo>⟩</mo></mrow><annotation>|1\rangle</annotation></semantics></math>

∣1⟩ states. Mathematically:

<math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>H</mi><mi>∣</mi><mn>0</mn><mo>⟩</mo><mo>=</mo><mfrac><mrow><mi>∣</mi><mn>0</mn><mo>⟩</mo><mo>+</mo><mi>∣</mi><mn>1</mn><mo>⟩</mo></mrow><msqrt><mn>2</mn></msqrt></mfrac></mrow><annotation>H|0\rangle = \frac{|0\rangle + |1\rangle}{\sqrt{2}}</annotation></semantics></math>

H∣0⟩=2

<svg height="1.08em" preserveaspectratio="xMinYMin slice" viewbox="0 0 400000 1080" width="400em" xmlns="http://www.w3.org/2000/svg"><path></path></svg>

∣0⟩+∣1⟩

This gate is crucial in quantum algorithms like Grover's and quantum teleportation.

The CNOT gate, or controlled-X gate, is an entangling gate that acts on two qubits: a control qubit and a target qubit. If the control qubit is in the

<math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>∣</mi><mn>1</mn><mo>⟩</mo></mrow><annotation>|1\rangle</annotation></semantics></math>

∣1⟩ state, it applies the X-gate to the target qubit; otherwise, it does nothing. It creates entanglement between the two qubits and is essential in building quantum circuits for various applications.

The Toffoli gate is a three-qubit gate that acts as a controlled-controlled-X gate. It applies the X-gate to the target qubit only if both control qubits are in the

<math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>∣</mi><mn>1</mn><mo>⟩</mo></mrow><annotation>|1\rangle</annotation></semantics></math>

∣1⟩ state. It is used in quantum computing for implementing reversible classical logic operations.

The SWAP gate exchanges the states of two qubits. When applied, it swaps the state of the first qubit with the state of the second qubit. This gate is fundamental in quantum algorithms and quantum error correction codes.

The Pauli Y gate introduces complex phase shifts along with a bit-flip operation. It can be thought of as a combination of bit-flip and phase-flip gates. Mathematically:

<math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>Y</mi><mi>∣</mi><mn>0</mn><mo>⟩</mo><mo>=</mo><mi>i</mi><mi>∣</mi><mn>1</mn><mo>⟩</mo></mrow><annotation>Y|0\rangle = i|1\rangle</annotation></semantics></math>

Y∣0⟩=i∣1⟩

<math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>Y</mi><mi>∣</mi><mn>1</mn><mo>⟩</mo><mo>=</mo><mo>−</mo><mi>i</mi><mi>∣</mi><mn>0</mn><mo>⟩</mo></mrow><annotation>Y|1\rangle = -i|0\rangle</annotation></semantics></math>

Y∣1⟩=−i∣0⟩

It's essential in quantum error correction and quantum algorithms.

The Pauli Z gate introduces a phase flip without changing the qubit's state. It leaves

<math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>∣</mi><mn>0</mn><mo>⟩</mo></mrow><annotation>|0\rangle</annotation></semantics></math>

∣0⟩ unchanged and transforms

<math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>∣</mi><mn>1</mn><mo>⟩</mo></mrow><annotation>|1\rangle</annotation></semantics></math>

∣1⟩ to

<math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mo>−</mo><mi>∣</mi><mn>1</mn><mo>⟩</mo></mrow><annotation>-|1\rangle</annotation></semantics></math>

−∣1⟩. Mathematically:

<math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>Z</mi><mi>∣</mi><mn>0</mn><mo>⟩</mo><mo>=</mo><mi>∣</mi><mn>0</mn><mo>⟩</mo></mrow><annotation>Z|0\rangle = |0\rangle</annotation></semantics></math>

Z∣0⟩=∣0⟩

<math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>Z</mi><mi>∣</mi><mn>1</mn><mo>⟩</mo><mo>=</mo><mo>−</mo><mi>∣</mi><mn>1</mn><mo>⟩</mo></mrow><annotation>Z|1\rangle = -|1\rangle</annotation></semantics></math>

Z∣1⟩=−∣1⟩

It's used for measuring the phase of a qubit.

The T-Gate applies a **π/4 phase shift** to the qubit. It is essential for quantum computing because it, along with the Hadamard and CNOT gates, allows for **universal quantum computation**. Mathematically:

<math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>T</mi><mi>∣</mi><mn>0</mn><mo>⟩</mo><mo>=</mo><mi>∣</mi><mn>0</mn><mo>⟩</mo></mrow><annotation>T|0\rangle = |0\rangle</annotation></semantics></math>

T∣0⟩=∣0⟩

<math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>T</mi><mi>∣</mi><mn>1</mn><mo>⟩</mo><mo>=</mo><msup><mi>e</mi><mrow><mi>i</mi><mi>π</mi><mi>/</mi><mn>4</mn></mrow></msup><mi>∣</mi><mn>1</mn><mo>⟩</mo></mrow><annotation>T|1\rangle = e^{i\pi/4} |1\rangle</annotation></semantics></math>

T∣1⟩=eiπ/4∣1⟩

The CSWAP gate, also known as the **Fredkin gate**, is a three-qubit gate that conditionally swaps the states of two target qubits based on the state of a control qubit. If the control qubit is in the

<math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>∣</mi><mn>1</mn><mo>⟩</mo></mrow><annotation>|1\rangle</annotation></semantics></math>

∣1⟩ state, it swaps the states of the two target qubits; otherwise, it leaves them unchanged.

The CSWAP gate acts on three qubits: a control qubit

<math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>∣</mi><mi>c</mi><mo>⟩</mo></mrow><annotation>|c\rangle</annotation></semantics></math>

∣c⟩ and two target qubits

<math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>∣</mi><msub><mi>t</mi><mn>1</mn></msub><mo>⟩</mo></mrow><annotation>|t_1\rangle</annotation></semantics></math>

∣t1⟩ and

<math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>∣</mi><msub><mi>t</mi><mn>2</mn></msub><mo>⟩</mo></mrow><annotation>|t_2\rangle</annotation></semantics></math>

∣t2⟩. The operation is:

<math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mtext>CSWAP</mtext><mi>∣</mi><mi>c</mi><mo>⟩</mo><mi>∣</mi><msub><mi>t</mi><mn>1</mn></msub><mo>⟩</mo><mi>∣</mi><msub><mi>t</mi><mn>2</mn></msub><mo>⟩</mo><mo>=</mo><mrow><mo>{</mo><mtable><mtr><mtd><mstyle><mrow><mi>∣</mi><mi>c</mi><mo>⟩</mo><mi>∣</mi><msub><mi>t</mi><mn>1</mn></msub><mo>⟩</mo><mi>∣</mi><msub><mi>t</mi><mn>2</mn></msub><mo>⟩</mo></mrow></mstyle></mtd><mtd><mstyle><mrow><mtext>if </mtext><mi>c</mi><mo>=</mo><mn>0</mn></mrow></mstyle></mtd></mtr><mtr><mtd><mstyle><mrow><mi>∣</mi><mi>c</mi><mo>⟩</mo><mi>∣</mi><msub><mi>t</mi><mn>2</mn></msub><mo>⟩</mo><mi>∣</mi><msub><mi>t</mi><mn>1</mn></msub><mo>⟩</mo></mrow></mstyle></mtd><mtd><mstyle><mrow><mtext>if </mtext><mi>c</mi><mo>=</mo><mn>1</mn></mrow></mstyle></mtd></mtr></mtable></mrow></mrow><annotation>\text{CSWAP}|c\rangle|t_1\rangle|t_2\rangle = \begin{cases} |c\rangle|t_1\rangle|t_2\rangle &amp; \text{if } c = 0 \\ |c\rangle|t_2\rangle|t_1\rangle &amp; \text{if } c = 1 \end{cases}</annotation></semantics></math>

CSWAP∣c⟩∣t1⟩∣t2⟩={∣c⟩∣t1⟩∣t2⟩∣c⟩∣t2⟩∣t1⟩if c=0if c=1

In matrix form (for the 8-dimensional space of three qubits), the CSWAP gate is:

<math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mtext>CSWAP</mtext><mo>=</mo><mrow><mo>(</mo><mtable><mtr><mtd><mstyle><mn>1</mn></mstyle></mtd><mtd><mstyle><mn>0</mn></mstyle></mtd><mtd><mstyle><mn>0</mn></mstyle></mtd><mtd><mstyle><mn>0</mn></mstyle></mtd><mtd><mstyle><mn>0</mn></mstyle></mtd><mtd><mstyle><mn>0</mn></mstyle></mtd><mtd><mstyle><mn>0</mn></mstyle></mtd><mtd><mstyle><mn>0</mn></mstyle></mtd></mtr><mtr><mtd><mstyle><mn>0</mn></mstyle></mtd><mtd><mstyle><mn>1</mn></mstyle></mtd><mtd><mstyle><mn>0</mn></mstyle></mtd><mtd><mstyle><mn>0</mn></mstyle></mtd><mtd><mstyle><mn>0</mn></mstyle></mtd><mtd><mstyle><mn>0</mn></mstyle></mtd><mtd><mstyle><mn>0</mn></mstyle></mtd><mtd><mstyle><mn>0</mn></mstyle></mtd></mtr><mtr><mtd><mstyle><mn>0</mn></mstyle></mtd><mtd><mstyle><mn>0</mn></mstyle></mtd><mtd><mstyle><mn>1</mn></mstyle></mtd><mtd><mstyle><mn>0</mn></mstyle></mtd><mtd><mstyle><mn>0</mn></mstyle></mtd><mtd><mstyle><mn>0</mn></mstyle></mtd><mtd><mstyle><mn>0</mn></mstyle></mtd><mtd><mstyle><mn>0</mn></mstyle></mtd></mtr><mtr><mtd><mstyle><mn>0</mn></mstyle></mtd><mtd><mstyle><mn>0</mn></mstyle></mtd><mtd><mstyle><mn>0</mn></mstyle></mtd><mtd><mstyle><mn>1</mn></mstyle></mtd><mtd><mstyle><mn>0</mn></mstyle></mtd><mtd><mstyle><mn>0</mn></mstyle></mtd><mtd><mstyle><mn>0</mn></mstyle></mtd><mtd><mstyle><mn>0</mn></mstyle></mtd></mtr><mtr><mtd><mstyle><mn>0</mn></mstyle></mtd><mtd><mstyle><mn>0</mn></mstyle></mtd><mtd><mstyle><mn>0</mn></mstyle></mtd><mtd><mstyle><mn>0</mn></mstyle></mtd><mtd><mstyle><mn>1</mn></mstyle></mtd><mtd><mstyle><mn>0</mn></mstyle></mtd><mtd><mstyle><mn>0</mn></mstyle></mtd><mtd><mstyle><mn>0</mn></mstyle></mtd></mtr><mtr><mtd><mstyle><mn>0</mn></mstyle></mtd><mtd><mstyle><mn>0</mn></mstyle></mtd><mtd><mstyle><mn>0</mn></mstyle></mtd><mtd><mstyle><mn>0</mn></mstyle></mtd><mtd><mstyle><mn>0</mn></mstyle></mtd><mtd><mstyle><mn>0</mn></mstyle></mtd><mtd><mstyle><mn>1</mn></mstyle></mtd><mtd><mstyle><mn>0</mn></mstyle></mtd></mtr><mtr><mtd><mstyle><mn>0</mn></mstyle></mtd><mtd><mstyle><mn>0</mn></mstyle></mtd><mtd><mstyle><mn>0</mn></mstyle></mtd><mtd><mstyle><mn>0</mn></mstyle></mtd><mtd><mstyle><mn>0</mn></mstyle></mtd><mtd><mstyle><mn>1</mn></mstyle></mtd><mtd><mstyle><mn>0</mn></mstyle></mtd><mtd><mstyle><mn>0</mn></mstyle></mtd></mtr><mtr><mtd><mstyle><mn>0</mn></mstyle></mtd><mtd><mstyle><mn>0</mn></mstyle></mtd><mtd><mstyle><mn>0</mn></mstyle></mtd><mtd><mstyle><mn>0</mn></mstyle></mtd><mtd><mstyle><mn>0</mn></mstyle></mtd><mtd><mstyle><mn>0</mn></mstyle></mtd><mtd><mstyle><mn>0</mn></mstyle></mtd><mtd><mstyle><mn>1</mn></mstyle></mtd></mtr></mtable><mo>)</mo></mrow></mrow><annotation>\text{CSWAP} = \begin{pmatrix} 1 &amp; 0 &amp; 0 &amp; 0 &amp; 0 &amp; 0 &amp; 0 &amp; 0 \\ 0 &amp; 1 &amp; 0 &amp; 0 &amp; 0 &amp; 0 &amp; 0 &amp; 0 \\ 0 &amp; 0 &amp; 1 &amp; 0 &amp; 0 &amp; 0 &amp; 0 &amp; 0 \\ 0 &amp; 0 &amp; 0 &amp; 1 &amp; 0 &amp; 0 &amp; 0 &amp; 0 \\ 0 &amp; 0 &amp; 0 &amp; 0 &amp; 1 &amp; 0 &amp; 0 &amp; 0 \\ 0 &amp; 0 &amp; 0 &amp; 0 &amp; 0 &amp; 0 &amp; 1 &amp; 0 \\ 0 &amp; 0 &amp; 0 &amp; 0 &amp; 0 &amp; 1 &amp; 0 &amp; 0 \\ 0 &amp; 0 &amp; 0 &amp; 0 &amp; 0 &amp; 0 &amp; 0 &amp; 1 \end{pmatrix}</annotation></semantics></math>

CSWAP=

<svg height="9.600em" viewbox="0 0 875 9600" width="0.875em" xmlns="http://www.w3.org/2000/svg"><path></path></svg>

1000000001000000001000000001000000001000000000100000010000000001

<svg height="9.600em" viewbox="0 0 875 9600" width="0.875em" xmlns="http://www.w3.org/2000/svg"><path></path></svg>

The CSWAP gate is fundamental in quantum algorithms such as the swap test, quantum error correction, and quantum state comparison. The CSWAP gate is reversible and preserves the number of

<math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>∣</mi><mn>1</mn><mo>⟩</mo></mrow><annotation>|1\rangle</annotation></semantics></math>

∣1⟩ states in the system (conserves the Hamming weight).

The U gate is a **universal single-qubit gate** parameterized by three angles (

<math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>θ</mi></mrow><annotation>\theta</annotation></semantics></math>

θ,

<math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>ϕ</mi></mrow><annotation>\phi</annotation></semantics></math>

ϕ,

<math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>λ</mi></mrow><annotation>\lambda</annotation></semantics></math>

λ) that can represent any single-qubit unitary operation. It provides a complete parameterization of single-qubit rotations and is essential for implementing arbitrary quantum operations.

The U gate matrix representation is:

<math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>U</mi><mo>(</mo><mi>θ</mi><mo>,</mo><mi>ϕ</mi><mo>,</mo><mi>λ</mi><mo>)</mo><mo>=</mo><mrow><mo>(</mo><mtable><mtr><mtd><mstyle><mrow><mi>cos</mi><mo>⁡</mo><mo>(</mo><mi>θ</mi><mi>/</mi><mn>2</mn><mo>)</mo></mrow></mstyle></mtd><mtd><mstyle><mrow><mo>−</mo><msup><mi>e</mi><mrow><mi>i</mi><mi>λ</mi></mrow></msup><mi>sin</mi><mo>⁡</mo><mo>(</mo><mi>θ</mi><mi>/</mi><mn>2</mn><mo>)</mo></mrow></mstyle></mtd></mtr><mtr><mtd><mstyle><mrow><msup><mi>e</mi><mrow><mi>i</mi><mi>ϕ</mi></mrow></msup><mi>sin</mi><mo>⁡</mo><mo>(</mo><mi>θ</mi><mi>/</mi><mn>2</mn><mo>)</mo></mrow></mstyle></mtd><mtd><mstyle><mrow><msup><mi>e</mi><mrow><mi>i</mi><mo>(</mo><mi>ϕ</mi><mo>+</mo><mi>λ</mi><mo>)</mo></mrow></msup><mi>cos</mi><mo>⁡</mo><mo>(</mo><mi>θ</mi><mi>/</mi><mn>2</mn><mo>)</mo></mrow></mstyle></mtd></mtr></mtable><mo>)</mo></mrow></mrow><annotation>U(\theta, \phi, \lambda) = \begin{pmatrix} \cos(\theta/2) &amp; -e^{i\lambda}\sin(\theta/2) \\ e^{i\phi}\sin(\theta/2) &amp; e^{i(\phi+\lambda)}\cos(\theta/2) \end{pmatrix}</annotation></semantics></math>

U(θ,ϕ,λ)=(cos(θ/2)eiϕsin(θ/2)−eiλsin(θ/2)ei(ϕ+λ)cos(θ/2))

The U gate can be decomposed into rotations around the Z, Y, and Z axes:

<math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>U</mi><mo>(</mo><mi>θ</mi><mo>,</mo><mi>ϕ</mi><mo>,</mo><mi>λ</mi><mo>)</mo><mo>=</mo><msub><mi>R</mi><mi>z</mi></msub><mo>(</mo><mi>ϕ</mi><mo>)</mo><mo>⋅</mo><msub><mi>R</mi><mi>y</mi></msub><mo>(</mo><mi>θ</mi><mo>)</mo><mo>⋅</mo><msub><mi>R</mi><mi>z</mi></msub><mo>(</mo><mi>λ</mi><mo>)</mo></mrow><annotation>U(\theta, \phi, \lambda) = R_z(\phi) \cdot R_y(\theta) \cdot R_z(\lambda)</annotation></semantics></math>

U(θ,ϕ,λ)=Rz(ϕ)⋅Ry(θ)⋅Rz(λ)

This decomposition shows that the U gate applies:

1. A rotation by λ around the Z-axis
2. A rotation by θ around the Y-axis
3. A rotation by φ around the Z-axis

- **Identity**: U(0, 0, 0) = I
- **Pauli X**: U(π, 0, π) = X
- **Pauli Y**: U(π, π/2, π/2) = Y
- **Pauli Z**: U(0, 0, π) = Z
- **Hadamard**: U(π/2, 0, π) = H

This gate is particularly useful in parameterized quantum circuits and variational quantum algorithms where you need to optimize over all possible single-qubit operations.

<a id="qumat-basic-gates--updates"></a>

# **Updates**

- **Acknowledged support for Cirq & Braket** (New Addition)
- **Removed Pauli X Gate** (Merged into NOT Gate)
- **Added T-Gate** (New Addition)
- **Added CSWAP Gate** (New Addition)
- **Added U Gate** (New Addition)
- **Fixed typos**

These quantum gates are fundamental building blocks in quantum computing, enabling the manipulation and transformation of qubit states to perform various quantum algorithms and computations.

---

<a id="qumat-parameterized-circuits"></a>

<!-- source_url: https://mahout.apache.org/docs/qumat/parameterized-circuits/ -->

<!-- page_index: 5 -->

# Parameterized Quantum Circuits and Rotation Gates

Version: latest

Parameterized quantum circuits (PQCs) contain gates with tunable parameters that can be optimized. Instead of using fixed angles, you use symbolic parameters that can be adjusted to find optimal values.

**Why use parameters?** Fixed angles give you one specific operation. Parameters let you:

- **Optimize**: Find the best angles for your task
- **Train**: Adjust parameters based on results (like machine learning)
- **Explore**: Try different values without rewriting the circuit

Rotation gates (Rx, Ry, Rz) are the primary parameterized gates. Use string names (e.g., `"theta"`) instead of numbers to create parameters, then bind values before execution.

Rotation gates rotate a qubit around the X, Y, or Z axis of the Bloch sphere. Each axis controls different aspects:

- **X-axis (Rx)**: Bit-flip rotations
- **Y-axis (Ry)**: Creates superpositions (like Hadamard)
- **Z-axis (Rz)**: Phase rotations (doesn't change probabilities)

Rotates a qubit around the X-axis by angle

<math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>θ</mi></mrow><annotation>\theta</annotation></semantics></math>

θ.

<math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><msub><mi>R</mi><mi>x</mi></msub><mo>(</mo><mi>θ</mi><mo>)</mo><mo>=</mo><mrow><mo>(</mo><mtable><mtr><mtd><mstyle><mrow><mi>cos</mi><mo>⁡</mo><mo>(</mo><mi>θ</mi><mi>/</mi><mn>2</mn><mo>)</mo></mrow></mstyle></mtd><mtd><mstyle><mrow><mo>−</mo><mi>i</mi><mi>sin</mi><mo>⁡</mo><mo>(</mo><mi>θ</mi><mi>/</mi><mn>2</mn><mo>)</mo></mrow></mstyle></mtd></mtr><mtr><mtd><mstyle><mrow><mo>−</mo><mi>i</mi><mi>sin</mi><mo>⁡</mo><mo>(</mo><mi>θ</mi><mi>/</mi><mn>2</mn><mo>)</mo></mrow></mstyle></mtd><mtd><mstyle><mrow><mi>cos</mi><mo>⁡</mo><mo>(</mo><mi>θ</mi><mi>/</mi><mn>2</mn><mo>)</mo></mrow></mstyle></mtd></mtr></mtable><mo>)</mo></mrow></mrow><annotation>R_x(\theta) = \begin{pmatrix} \cos(\theta/2) &amp; -i\sin(\theta/2) \\ -i\sin(\theta/2) &amp; \cos(\theta/2) \end{pmatrix}</annotation></semantics></math>

Rx(θ)=(cos(θ/2)−isin(θ/2)−isin(θ/2)cos(θ/2))

<math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><msub><mi>R</mi><mi>x</mi></msub><mo>(</mo><mi>π</mi><mi>/</mi><mn>2</mn><mo>)</mo><mi>∣</mi><mn>0</mn><mo>⟩</mo><mo>=</mo><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac><mo>(</mo><mi>∣</mi><mn>0</mn><mo>⟩</mo><mo>−</mo><mi>i</mi><mi>∣</mi><mn>1</mn><mo>⟩</mo><mo>)</mo></mrow><annotation>R_x(\pi/2)|0\rangle = \frac{1}{\sqrt{2}}(|0\rangle - i|1\rangle)</annotation></semantics></math>

Rx(π/2)∣0⟩=2

<svg height="1.08em" preserveaspectratio="xMinYMin slice" viewbox="0 0 400000 1080" width="400em" xmlns="http://www.w3.org/2000/svg"><path></path></svg>

1(∣0⟩−i∣1⟩)

```python
from qumat import QuMat 
import numpy as np 
 
backend_config = { 
    'backend_name': 'qiskit', 
    'backend_options': {'simulator_type': 'qasm_simulator', 'shots': 1000} 
} 
qumat = QuMat(backend_config) 
qumat.create_empty_circuit(num_qubits=1) 
qumat.apply_rx_gate(0, angle=np.pi / 2) 
results = qumat.execute_circuit() 
```

Rotates a qubit around the Y-axis by angle

<math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>θ</mi></mrow><annotation>\theta</annotation></semantics></math>

θ.

<math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><msub><mi>R</mi><mi>y</mi></msub><mo>(</mo><mi>θ</mi><mo>)</mo><mo>=</mo><mrow><mo>(</mo><mtable><mtr><mtd><mstyle><mrow><mi>cos</mi><mo>⁡</mo><mo>(</mo><mi>θ</mi><mi>/</mi><mn>2</mn><mo>)</mo></mrow></mstyle></mtd><mtd><mstyle><mrow><mo>−</mo><mi>sin</mi><mo>⁡</mo><mo>(</mo><mi>θ</mi><mi>/</mi><mn>2</mn><mo>)</mo></mrow></mstyle></mtd></mtr><mtr><mtd><mstyle><mrow><mi>sin</mi><mo>⁡</mo><mo>(</mo><mi>θ</mi><mi>/</mi><mn>2</mn><mo>)</mo></mrow></mstyle></mtd><mtd><mstyle><mrow><mi>cos</mi><mo>⁡</mo><mo>(</mo><mi>θ</mi><mi>/</mi><mn>2</mn><mo>)</mo></mrow></mstyle></mtd></mtr></mtable><mo>)</mo></mrow></mrow><annotation>R_y(\theta) = \begin{pmatrix} \cos(\theta/2) &amp; -\sin(\theta/2) \\ \sin(\theta/2) &amp; \cos(\theta/2) \end{pmatrix}</annotation></semantics></math>

Ry(θ)=(cos(θ/2)sin(θ/2)−sin(θ/2)cos(θ/2))

<math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><msub><mi>R</mi><mi>y</mi></msub><mo>(</mo><mi>π</mi><mi>/</mi><mn>2</mn><mo>)</mo><mi>∣</mi><mn>0</mn><mo>⟩</mo><mo>=</mo><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac><mo>(</mo><mi>∣</mi><mn>0</mn><mo>⟩</mo><mo>+</mo><mi>∣</mi><mn>1</mn><mo>⟩</mo><mo>)</mo></mrow><annotation>R_y(\pi/2)|0\rangle = \frac{1}{\sqrt{2}}(|0\rangle + |1\rangle)</annotation></semantics></math>

Ry(π/2)∣0⟩=2

<svg height="1.08em" preserveaspectratio="xMinYMin slice" viewbox="0 0 400000 1080" width="400em" xmlns="http://www.w3.org/2000/svg"><path></path></svg>

1(∣0⟩+∣1⟩)

```python
qumat.create_empty_circuit(num_qubits=1) 
qumat.apply_ry_gate(0, angle=np.pi / 2)  # Creates (|0⟩ + |1⟩)/√2 
results = qumat.execute_circuit() 
```

Rotates a qubit around the Z-axis by angle

<math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>θ</mi></mrow><annotation>\theta</annotation></semantics></math>

θ. Changes phase without affecting probability amplitudes.

<math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><msub><mi>R</mi><mi>z</mi></msub><mo>(</mo><mi>θ</mi><mo>)</mo><mo>=</mo><mrow><mo>(</mo><mtable><mtr><mtd><mstyle><msup><mi>e</mi><mrow><mo>−</mo><mi>i</mi><mi>θ</mi><mi>/</mi><mn>2</mn></mrow></msup></mstyle></mtd><mtd><mstyle><mn>0</mn></mstyle></mtd></mtr><mtr><mtd><mstyle><mn>0</mn></mstyle></mtd><mtd><mstyle><msup><mi>e</mi><mrow><mi>i</mi><mi>θ</mi><mi>/</mi><mn>2</mn></mrow></msup></mstyle></mtd></mtr></mtable><mo>)</mo></mrow></mrow><annotation>R_z(\theta) = \begin{pmatrix} e^{-i\theta/2} &amp; 0 \\ 0 &amp; e^{i\theta/2} \end{pmatrix}</annotation></semantics></math>

Rz(θ)=(e−iθ/200eiθ/2)

<math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><msub><mi>R</mi><mi>z</mi></msub><mo>(</mo><mi>π</mi><mi>/</mi><mn>2</mn><mo>)</mo><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac><mo>(</mo><mi>∣</mi><mn>0</mn><mo>⟩</mo><mo>+</mo><mi>∣</mi><mn>1</mn><mo>⟩</mo><mo>)</mo><mo>=</mo><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac><mo>(</mo><mi>∣</mi><mn>0</mn><mo>⟩</mo><mo>+</mo><mi>i</mi><mi>∣</mi><mn>1</mn><mo>⟩</mo><mo>)</mo></mrow><annotation>R_z(\pi/2)\frac{1}{\sqrt{2}}(|0\rangle + |1\rangle) = \frac{1}{\sqrt{2}}(|0\rangle + i|1\rangle)</annotation></semantics></math>

Rz(π/2)2

<svg height="1.08em" preserveaspectratio="xMinYMin slice" viewbox="0 0 400000 1080" width="400em" xmlns="http://www.w3.org/2000/svg"><path></path></svg>

1(∣0⟩+∣1⟩)=2

<svg height="1.08em" preserveaspectratio="xMinYMin slice" viewbox="0 0 400000 1080" width="400em" xmlns="http://www.w3.org/2000/svg"><path></path></svg>

1(∣0⟩+i∣1⟩)

Probabilities remain: P(|0⟩) = P(|1⟩) = 1/2

```python
qumat.create_empty_circuit(num_qubits=1) 
qumat.apply_hadamard_gate(0) 
qumat.apply_rz_gate(0, angle=np.pi / 2) 
results = qumat.execute_circuit() 
```

**Notes**: Angles are in **radians** (π = 180°, π/2 = 90°, π/4 = 45°). Supported across all backends (Qiskit, Cirq, Braket).

**Fixed value** (angle is set once):

```python
qumat.apply_ry_gate(0, angle=0.5)  # Fixed angle 
```

**Parameterized** (angle can be changed):

```python
qumat.apply_ry_gate(0, angle="theta")  # Parameter - can be optimized 
```

Use string names instead of numbers to create parameters:

```python
from qumat import QuMat 
import numpy as np 
 
backend_config = { 
    'backend_name': 'qiskit', 
    'backend_options': {'simulator_type': 'qasm_simulator', 'shots': 1000} 
} 
qumat = QuMat(backend_config) 
 
# Step 1: Create circuit with parameterized gates 
qumat.create_empty_circuit(num_qubits=2) 
qumat.apply_ry_gate(0, angle="theta")  # String = parameter 
qumat.apply_rz_gate(0, angle="phi") 
qumat.apply_rx_gate(1, angle="alpha") 
 
# Step 2: Parameters are automatically registered 
print(list(qumat.parameters.keys()))  # ['theta', 'phi', 'alpha'] 
 
# Step 3: Bind parameters before execution 
qumat.bind_parameters({ 
    "theta": np.pi / 4, 
    "phi": np.pi / 2, 
    "alpha": np.pi / 3 
}) 
 
# Step 4: Execute with bound parameters 
results = qumat.execute_circuit() 
 
# Alternative: Bind during execution (skips step 3) 
results = qumat.execute_circuit(parameter_values={ 
    "theta": np.pi / 4, 
    "phi": np.pi / 2, 
    "alpha": np.pi / 3 
}) 
```

Assigns numerical values to symbolic parameters. Must be called before `execute_circuit()` if parameters are used.

**Raises**: `ValueError` if parameter name not found.

```python
# Create circuit with parameters 
qumat.create_empty_circuit(num_qubits=1) 
qumat.apply_ry_gate(0, angle="theta") 
qumat.apply_rz_gate(0, angle="phi") 
 
# Bind values to parameters 
qumat.bind_parameters({"theta": 0.5, "phi": 1.0}) 
 
# Now you can execute 
results = qumat.execute_circuit() 
```

The power of parameterized circuits: optimize parameters to minimize a cost function. The workflow is:

1. Create circuit with parameters
2. Try different parameter values
3. Execute and compute cost
4. Find values that minimize cost

Example:

```python
from qumat import QuMat 
import numpy as np 
 
backend_config = { 
    'backend_name': 'qiskit', 
    'backend_options': {'simulator_type': 'qasm_simulator', 'shots': 1000} 
} 
qumat = QuMat(backend_config) 
 
# Create parameterized circuit once 
qumat.create_empty_circuit(num_qubits=2) 
qumat.apply_ry_gate(0, angle="theta") 
qumat.apply_cnot_gate(0, 1) 
qumat.apply_rz_gate(1, angle="phi") 
 
# Simple optimization loop 
best_cost = float('inf') 
best_params = None 
 
for iteration in range(10): 
    # Try different parameter values 
    theta = np.random.uniform(0, 2 * np.pi) 
    phi = np.random.uniform(0, 2 * np.pi) 
 
    # Bind and execute 
    qumat.bind_parameters({"theta": theta, "phi": phi}) 
    results = qumat.execute_circuit() 
 
    # Compute cost (example: minimize probability of |00⟩) 
    total_shots = sum(results.values()) 
    prob_00 = results.get("00", 0) / total_shots 
    cost = prob_00 
 
    # Track best result 
    if cost < best_cost: 
        best_cost = cost 
        best_params = {"theta": theta, "phi": phi} 
 
print(f"Best parameters: {best_params}, cost: {best_cost}") 
 
# With SciPy optimizer 
from scipy.optimize import minimize 
 
def cost_function(params): 
    theta, phi = params 
    qumat.bind_parameters({"theta": theta, "phi": phi}) 
    results = qumat.execute_circuit() 
    total_shots = sum(results.values()) 
    prob_00 = results.get("00", 0) / total_shots 
    return prob_00 
 
result = minimize(cost_function, [0.5, 0.5], method='COBYLA') 
print(f"Optimized: {result.x}, cost: {result.fun}") 
```

- **Parameter creation**: Use string names (e.g., `"theta"`) in rotation gates to create parameters
- **Auto-registration**: Parameters are automatically registered when first used
- **Binding required**: All parameters must be bound (assigned values) before execution
- **Value types**: Parameter values must be numerical (float or int)
- **Backend support**: Works with all backends (Qiskit, Cirq, Braket)
- **Reuse**: Create circuit once, bind different parameter values for optimization loops

---

<a id="qumat-api"></a>

<!-- source_url: https://mahout.apache.org/docs/qumat/api/ -->

<!-- page_index: 6 -->

# QuMat Class Methods

Version: latest

- **Purpose**: Initializes the QuMat instance with a specific backend.
- **Parameters**:
  - `backend_config` (dict): Configuration for the backend including its name and options.
- **Usage**: Used to set up the quantum computing backend based on user configuration.

- **Purpose**: Creates an empty quantum circuit with a specified number of qubits.
- **Parameters**:
  - `num_qubits` (int): Number of qubits in the quantum circuit.
- **Usage**: Used at the start of quantum computations to prepare a new quantum circuit.

- **Purpose**: Applies a NOT gate (quantum equivalent of a classical NOT) to a specified qubit.
- **Parameters**:
  - `qubit_index` (int): Index of the qubit to which the gate is applied.
- **Usage**: Used to flip the state of a qubit from 0 to 1 or from 1 to 0.

- **Purpose**: Applies a Hadamard gate to a specified qubit.
- **Parameters**:
  - `qubit_index` (int): Index of the qubit.
- **Usage**: Used to create a superposition state, allowing the qubit to be both 0 and 1 simultaneously.

- **Purpose**: Applies a Controlled-NOT (CNOT) gate between two qubits.
- **Parameters**:
  - `control_qubit_index` (int): Index of the control qubit.
  - `target_qubit_index` (int): Index of the target qubit.
- **Usage**: Fundamental for entangling qubits, which is essential for quantum algorithms.

- **Purpose**: Applies a Toffoli gate (CCX gate) to three qubits.
- **Parameters**:
  - `control_qubit_index1` (int): Index of the first control qubit.
  - `control_qubit_index2` (int): Index of the second control qubit.
  - `target_qubit_index` (int): Index of the target qubit.
- **Usage**: Acts as a quantum AND gate, used in algorithms requiring conditional logic.

- **Purpose**: Swaps the states of two qubits.
- **Parameters**:
  - `qubit_index1` (int): Index of the first qubit.
  - `qubit_index2` (int): Index of the second qubit.
- **Usage**: Useful in quantum algorithms for rearranging qubit states.

- **Purpose**: Applies a controlled-SWAP (Fredkin) gate that swaps two targets when the control is |1⟩.
- **Parameters**:
  - `control_qubit_index` (int): Index of the control qubit.
  - `target_qubit_index1` (int): Index of the first target qubit.
  - `target_qubit_index2` (int): Index of the second target qubit.
- **Usage**: Used in overlap estimation routines such as the swap test.

- **Purpose**: Applies a Pauli-X gate to a specified qubit.
- **Parameters**:
  - `qubit_index` (int): Index of the qubit.
- **Usage**: Equivalent to a NOT gate, flips the qubit state.

- **Purpose**: Applies a Pauli-Y gate to a specified qubit.
- **Parameters**:
  - `qubit_index` (int): Index of the qubit.
- **Usage**: Impacts the phase and amplitude of a qubit's state.

- **Purpose**: Applies a Pauli-Z gate to a specified qubit.
- **Parameters**:
  - `qubit_index` (int): Index of the qubit.
- **Usage**: Alters the phase of a qubit without changing its amplitude.

- **Purpose**: Applies the T (π/8) phase gate to a specified qubit.
- **Parameters**:
  - `qubit_index` (int): Index of the qubit.
- **Usage**: Adds a π/4 phase to |1⟩. Together with the Hadamard (H) and CNOT gates, it enables universal single-qubit control.

- **Purpose**: Executes the quantum circuit and retrieves the results.
- **Usage**: Used to run the entire set of quantum operations and measure the outcomes.

- **Purpose**: Returns the final state vector of the circuit from the configured backend.
- **Usage**: Retrieves the full quantum state for simulation and analysis workflows.

- **Purpose**: Visualizes the quantum circuit.
- **Returns**: A string representation of the circuit visualization (format depends on backend).
- **Usage**: Returns a visualization string that can be printed or used programmatically. Example: `print(qc.draw_circuit())` or `viz = qc.draw_circuit()`.

> [!NOTE]
> - : Uses underlying libraries' methods for drawing circuits (Qiskit's `draw()`, Cirq's `str()`, or Braket's `str()`).

- **Purpose**: Applies a rotation around the X-axis to a specified qubit with an optional parameter for optimization.
- **Parameters**:
  - `qubit_index` (int): Index of the qubit.
  - `angle` (str or float): Angle in radians for the rotation. Can be a static value or a parameter name for optimization.
- **Usage**: Used to rotate a qubit around the X-axis, often in parameterized quantum circuits for variational algorithms.

- **Purpose**: Applies a rotation around the Y-axis to a specified qubit with an optional parameter for optimization.
- **Parameters**:
  - `qubit_index` (int): Index of the qubit.
  - `angle` (str or float): Angle in radians for the rotation. Can be a static value or a parameter name for optimization.
- **Usage**: Used to rotate a qubit around the Y-axis in parameterized circuits, aiding in the creation of complex quantum states.

- **Purpose**: Applies a rotation around the Z-axis to a specified qubit with an optional parameter for optimization.
- **Parameters**:
  - `qubit_index` (int): Index of the qubit.
  - `angle` (str or float): Angle in radians for the rotation. Can be a static value or a parameter name for optimization.
- **Usage**: Utilized in parameterized quantum circuits to modify the phase of a qubit state during optimization.

- **Purpose**: Applies the universal single-qubit U(θ, φ, λ) gate.
- **Parameters**:
  - `qubit_index` (int): Index of the qubit.
  - `theta` (float): Rotation angle θ.
  - `phi` (float): Rotation angle φ.
  - `lambd` (float): Rotation angle λ.
- **Usage**: Provides full single-qubit unitary control via Z–Y–Z Euler decomposition.

- **Purpose**: Executes the quantum circuit with the ability to bind specific parameter values if provided.
- **Parameters**:
  - `parameter_values` (dict, optional): A dictionary where keys are parameter names and values are the numerical values to bind.
- **Usage**: Enables the execution of parameterized circuits by binding parameter values, facilitating optimization processes.

- **Purpose**: Binds numerical values to the parameters of the quantum circuit, allowing for dynamic updates during optimization.
- **Parameters**:
  - `parameter_values` (dict): A dictionary with parameter names as keys and numerical values to bind.
- **Usage**: Essential for optimization loops where parameters are adjusted based on cost function evaluations.

- **Purpose**: Internal function to manage parameter registration.
- **Parameters**:
  - `param_name` (str): The name of the parameter to handle.
- **Usage**: Automatically invoked when applying parameterized gates to keep track of parameters efficiently.

- **Purpose**: Builds the swap-test subcircuit (H–CSWAP–H) to compare two quantum states.
- **Parameters**:
  - `ancilla_qubit` (int): Index of the ancilla control qubit.
  - `qubit1` (int): Index of the first state qubit.
  - `qubit2` (int): Index of the second state qubit.
- **Usage**: Used in overlap/fidelity estimation between two states.

- **Purpose**: Executes the swap test and returns |⟨ψ|φ⟩|² using backend-specific measurement parsing.
- **Parameters**:
  - `qubit1` (int): Index of the first state qubit.
  - `qubit2` (int): Index of the second state qubit.
  - `ancilla_qubit` (int, default to 0): Index of the ancilla qubit.
- **Usage**: Convenience wrapper for fidelity/overlap measurement across backends.

---

<a id="qumat-concepts"></a>

<!-- source_url: https://mahout.apache.org/docs/qumat/concepts/ -->

<!-- page_index: 7 -->

# Core Concepts

Version: latest

---

<a id="qumat-examples"></a>

<!-- source_url: https://mahout.apache.org/docs/qumat/examples/ -->

<!-- page_index: 8 -->

# Examples

Version: latest

---

<a id="qdp"></a>

<!-- source_url: https://mahout.apache.org/docs/qdp/ -->

<!-- page_index: 9 -->

# QDP

Version: latest

QDP (Quantum Data Plane) is a high-performance GPU-accelerated library for encoding classical data into quantum states.

- [Getting Started](#qdp-getting-started)
- [Core Concepts](#qdp-concepts)
- [API Reference](#qdp-api)
- [Examples](#qdp-examples)

---

<a id="qdp-getting-started"></a>

<!-- source_url: https://mahout.apache.org/docs/qdp/getting-started/ -->

<!-- page_index: 10 -->

# Getting Started with QDP

Version: latest

QDP (Quantum Data Plane) is a GPU-accelerated library for encoding classical data into quantum states.

- Linux with NVIDIA GPU
- CUDA toolkit installed (`nvcc --version` to verify)
- Python 3.10+

```bash
pip install qumat[qdp] 
```

For development (from source):

```bash
git clone https://github.com/apache/mahout.git 
cd mahout/qdp/qdp-python 
uv venv -p python3.10 && source .venv/bin/activate 
uv sync --group dev && uv run maturin develop 
```

```python
import torch 
from qumat.qdp import QdpEngine 
 
engine = QdpEngine(0)  # GPU device 0 
data = [0.5, 0.5, 0.5, 0.5] 
qtensor = engine.encode(data, num_qubits=2, encoding_method="amplitude") 
 
# Convert to PyTorch (zero-copy) 
tensor = torch.from_dlpack(qtensor)  # Note: can only be consumed once 
```

| Method | Constraint | Example |
| --- | --- | --- |
| `amplitude` | data length ≤ 2^num\_qubits | `encode([0.5, 0.5, 0.5, 0.5], num_qubits=2, encoding_method="amplitude")` |
| `angle` | data length = num\_qubits | `encode([0.1, 0.2, 0.3, 0.4], num_qubits=4, encoding_method="angle")` |
| `basis` | data length = num\_qubits | `encode([1, 0, 1, 1], num_qubits=4, encoding_method="basis")` |

```python
engine.encode("data.parquet", num_qubits=10, encoding_method="amplitude")  # also: .arrow, .npy, .pt, .pb 
```

Remote object storage URLs are supported when QDP is built with `remote-io`:

```python
engine.encode("s3://my-bucket/path/data.parquet", num_qubits=10, encoding_method="amplitude") 
engine.encode("gs://my-bucket/path/data.parquet", num_qubits=10, encoding_method="amplitude") 
```

Notes:

- Remote URL query/fragment is not supported (`?versionId=...`, `#...`).
- Streaming still requires `.parquet`.

- Use `precision="float64"` for higher precision: `QdpEngine(0, precision="float64")`
- NumPy inputs must be `float64` dtype
- Streaming only works with Parquet files

| Problem | Solution |
| --- | --- |
| Import fails | Activate venv: `source .venv/bin/activate` |
| CUDA errors | Run `cargo clean` in `qdp/` and rebuild |
| Out of memory | Reduce `num_qubits` or use `precision="float32"` |

- [Concepts](#qdp-concepts) - Learn about quantum encoding concepts
- [API Reference](#qdp-api) - Detailed API documentation
- [Examples](#qdp-examples) - More usage examples

- Mailing List: [dev@mahout.apache.org](mailto:dev@mahout.apache.org)
- [GitHub Issues](https://github.com/apache/mahout/issues)

---

<a id="qdp-concepts"></a>

<!-- source_url: https://mahout.apache.org/docs/qdp/concepts/ -->

<!-- page_index: 11 -->

# Core Concepts

Version: latest

This page explains the core concepts behind QDP (Quantum Data Plane): the architecture, the supported encoding methods, GPU memory management, DLPack zero-copy integration, and key performance characteristics.

---

At a high level, QDP is organized as layered components:

- **Python API (Qumat)**: `qumat.qdp` exposes a friendly Python entry point (`QdpEngine`).
- **Python native extension (PyO3)**: `qdp/qdp-python` builds the `_qdp` module, bridging Python ↔ Rust and implementing Python-side DLPack (`__dlpack__`).
- **Rust core**: `qdp/qdp-core` contains the engine (`QdpEngine`), encoder implementations, IO readers, GPU pipelines, and DLPack export.
- **CUDA kernels**: `qdp/qdp-kernels` provides the CUDA kernels invoked by the Rust encoders.

Data flow (conceptual):

```text
Python (qumat.qdp)  →  _qdp (PyO3)  →  qdp-core (Rust)  →  qdp-kernels (CUDA) 
        │                        │              │                 │ 
        └──── torch.from_dlpack(qtensor) ◄──────┴── DLPack DLManagedTensor (GPU ptr) 
```

---

QDP encodes classical data into a **state vector**

<math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>∣</mi><mi>ψ</mi><mo>⟩</mo></mrow><annotation>\vert\psi\rangle</annotation></semantics></math>

∣ψ⟩ for

<math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>n</mi></mrow><annotation>n</annotation></semantics></math>

n qubits.

- **State length**:

<math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><msup><mn>2</mn><mi>n</mi></msup></mrow><annotation>2^{n}</annotation></semantics></math>

  2n
- **Type**: complex numbers (on GPU)
- **Shape exposed via DLPack**:
  - Single sample: `[1, 2^n]` (always 2D)
  - Batch: `[batch_size, 2^n]`

QDP supports two output precisions:

- **complex64** (2×float32) when output precision is `float32`
- **complex128** (2×float64) when output precision is `float64`

---

QDP uses a strategy pattern for encoding methods:

- `encoding_method` is a string, e.g. `"amplitude"`, `"basis"`, `"angle"`
- QDP maps it to a concrete encoder at runtime

All encoders perform input validation (at minimum):

-
<math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mn>1</mn><mo>≤</mo><mi>n</mi><mo>≤</mo><mn>30</mn></mrow><annotation>1 \le n \le 30</annotation></semantics></math>

  1≤n≤30
- input is not empty
- for amplitude: `len(data) <= 2^n`; for angle: `len(data) = n` (one per qubit); for basis: index in range

Note:

<math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>n</mi><mo>=</mo><mn>30</mn></mrow><annotation>n=30</annotation></semantics></math>

n=30 is already very large—just the output state for a single sample is on the order of

<math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><msup><mn>2</mn><mn>30</mn></msup></mrow><annotation>2^{30}</annotation></semantics></math>

230 complex numbers.

---

**Goal**: represent a real-valued feature vector

<math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>x</mi></mrow><annotation>x</annotation></semantics></math>

x as quantum amplitudes:

<math display="block" xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>∣</mi><mi>ψ</mi><mo>⟩</mo><mo>=</mo><munderover><mo>∑</mo><mrow><mi>i</mi><mo>=</mo><mn>0</mn></mrow><mrow><msup><mn>2</mn><mi>n</mi></msup><mo>−</mo><mn>1</mn></mrow></munderover><mfrac><msub><mi>x</mi><mi>i</mi></msub><mrow><mi>∥</mi><mi>x</mi><msub><mi>∥</mi><mn>2</mn></msub></mrow></mfrac><mtext> </mtext><mi>∣</mi><mi>i</mi><mo>⟩</mo></mrow><annotation>\vert\psi\rangle = \sum_{i=0}^{2^{n}-1} \frac{x_i}{\|x\|_2}\,\vert i\rangle</annotation></semantics></math>

∣ψ⟩=i=0∑2n−1∥x∥2xi∣i⟩

Key properties in QDP:

- **Normalization**: QDP computes

<math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>∥</mi><mi>x</mi><msub><mi>∥</mi><mn>2</mn></msub></mrow><annotation>\|x\|_2</annotation></semantics></math>

  ∥x∥2 and rejects zero-norm inputs.
- **Padding**: if `len(x) < 2^n`, the remaining amplitudes are treated as zeros.
- **GPU execution**: the normalization and write into the GPU state vector is performed by CUDA kernels.
- **Batch support**: amplitude encoding supports a batch path to reduce kernel launch / allocation overhead (recommended when encoding many samples).

When to use it:

- You have dense real-valued vectors and want a direct amplitude representation.

Trade-offs:

- Output size grows exponentially with `num_qubits` (

<math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><msup><mn>2</mn><mi>n</mi></msup></mrow><annotation>2^n</annotation></semantics></math>

  2n), so it can become memory-heavy quickly.

**Goal**: map an integer index

<math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>i</mi></mrow><annotation>i</annotation></semantics></math>

i into a computational basis state

<math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>∣</mi><mi>i</mi><mo>⟩</mo></mrow><annotation>\vert i\rangle</annotation></semantics></math>

∣i⟩.

For

<math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>n</mi></mrow><annotation>n</annotation></semantics></math>

n qubits with

<math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mn>0</mn><mo>≤</mo><mi>i</mi><mo>&lt;</mo><msup><mn>2</mn><mi>n</mi></msup></mrow><annotation>0 \le i &lt; 2^n</annotation></semantics></math>

0≤i<2n:

-
<math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>ψ</mi><mo>[</mo><mi>i</mi><mo>]</mo><mo>=</mo><mn>1</mn></mrow><annotation>\psi[i] = 1</annotation></semantics></math>

  ψ[i]=1
-
<math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>ψ</mi><mo>[</mo><mi>j</mi><mo>]</mo><mo>=</mo><mn>0</mn></mrow><annotation>\psi[j] = 0</annotation></semantics></math>

  ψ[j]=0 for all

<math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>j</mi><mo>≠</mo><mi>i</mi></mrow><annotation>j \ne i</annotation></semantics></math>

  j=i

Key properties in QDP:

- **Input shape**:
  - single sample expects exactly one value: `[index]`
  - batch expects one index per sample (effectively `sample_size = 1`)
- **Range checking**: indices must be valid for the chosen `num_qubits`
- **GPU execution**: kernel sets the one-hot amplitude at the requested index

When to use it:

- Your data naturally represents discrete states (categories, token IDs, hashed features, etc.).

**Goal**: map one real angle per qubit to a product state. For angles

<math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><msub><mi>x</mi><mn>0</mn></msub><mo>,</mo><mo>…</mo><mo>,</mo><msub><mi>x</mi><mrow><mi>n</mi><mo>−</mo><mn>1</mn></mrow></msub></mrow><annotation>x_0, \ldots, x_{n-1}</annotation></semantics></math>

x0,…,xn−1 (one per qubit):

<math display="block" xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>∣</mi><mi>ψ</mi><mo>(</mo><mi>x</mi><mo>)</mo><mo>⟩</mo><mo>=</mo><munderover><mo>⨂</mo><mrow><mi>k</mi><mo>=</mo><mn>0</mn></mrow><mrow><mi>n</mi><mo>−</mo><mn>1</mn></mrow></munderover><mo>(</mo><mi>cos</mi><mo>⁡</mo><mo>(</mo><msub><mi>x</mi><mi>k</mi></msub><mo>)</mo><mtext> </mtext><mi>∣</mi><mn>0</mn><mo>⟩</mo><mo>+</mo><mi>sin</mi><mo>⁡</mo><mo>(</mo><msub><mi>x</mi><mi>k</mi></msub><mo>)</mo><mtext> </mtext><mi>∣</mi><mn>1</mn><mo>⟩</mo><mo>)</mo></mrow><annotation>\vert\psi(x)\rangle = \bigotimes_{k=0}^{n-1} \bigl( \cos(x_k)\,\vert 0\rangle + \sin(x_k)\,\vert 1\rangle \bigr)</annotation></semantics></math>

∣ψ(x)⟩=k=0⨂n−1(cos(xk)∣0⟩+sin(xk)∣1⟩)

So each basis state

<math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>∣</mi><mi>i</mi><mo>⟩</mo></mrow><annotation>\vert i\rangle</annotation></semantics></math>

∣i⟩ gets a real amplitude

<math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><msub><mo>∏</mo><mi>k</mi></msub><mo>(</mo><mo>(</mo><msub><mi>i</mi><mi>k</mi></msub><mo>=</mo><mn>0</mn><mo>⇒</mo><mi>cos</mi><mo>⁡</mo><mo>(</mo><msub><mi>x</mi><mi>k</mi></msub><mo>)</mo><mo>)</mo><mo>,</mo><mtext> </mtext><mo>(</mo><msub><mi>i</mi><mi>k</mi></msub><mo>=</mo><mn>1</mn><mo>⇒</mo><mi>sin</mi><mo>⁡</mo><mo>(</mo><msub><mi>x</mi><mi>k</mi></msub><mo>)</mo><mo>)</mo><mo>)</mo></mrow><annotation>\prod_{k} \bigl( (i_k=0 \Rightarrow \cos(x_k)),\ (i_k=1 \Rightarrow \sin(x_k)) \bigr)</annotation></semantics></math>

∏k((ik=0⇒cos(xk)), (ik=1⇒sin(xk))) (no phase; state is real-valued in the computational basis).

Key properties in QDP:

- **Input shape**: exactly **one angle per qubit** — `sample_size` must equal `num_qubits`. Single sample: length-`n` vector; batch: shape `[batch_size, n]`.
- **Validation**: all angles must be finite (no NaN/Inf). Input is not normalized.
- **GPU execution**: CUDA kernels compute the product-state amplitudes directly (no circuit simulation).
- **Batch support**: angle encoding supports a batch path for many samples; streaming Parquet with `"angle"` is also supported.

When to use it:

- You have per-qubit or per-feature rotation angles (e.g. from classical preprocessing or embedding) and want a product state on GPU.

Trade-offs:

- Only

<math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>n</mi></mrow><annotation>n</annotation></semantics></math>

  n real numbers per sample, so input is compact. Output is still

<math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><msup><mn>2</mn><mi>n</mi></msup></mrow><annotation>2^n</annotation></semantics></math>

  2n complex amplitudes. Does not by itself create entanglement (product state).

---

QDP is designed to keep the encoded states on the GPU and to avoid unnecessary allocations/copies where possible.

For each encoded sample, QDP allocates a state vector of size

<math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><msup><mn>2</mn><mi>n</mi></msup></mrow><annotation>2^n</annotation></semantics></math>

2n. Memory usage grows exponentially:

- complex128 uses 16 bytes per element
- rough output size (single sample) is:
  -
<math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><msup><mn>2</mn><mi>n</mi></msup><mo>×</mo><mn>16</mn></mrow><annotation>2^n \times 16</annotation></semantics></math>

    2n×16 bytes for complex128
  -
<math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><msup><mn>2</mn><mi>n</mi></msup><mo>×</mo><mn>8</mn></mrow><annotation>2^n \times 8</annotation></semantics></math>

    2n×8 bytes for complex64

QDP performs **pre-flight checks** before large allocations to fail fast with an OOM-aware message (e.g., suggesting smaller `num_qubits` or batch size).

For high-throughput IO → GPU workflows (especially streaming from Parquet), QDP uses:

- **Pinned host buffers** (page-locked memory) to speed up host↔device transfers.
- **Double buffering** (ping-pong) so one buffer can be filled while another is being processed.
- **Device staging buffers** (for streaming) so that copies and compute can overlap.

Streaming Parquet encoding is implemented as a **producer/consumer pipeline**:

- a background IO thread reads chunks into pinned host buffers
- the GPU side processes each chunk while IO continues

In the current implementation, streaming Parquet supports:

- `"amplitude"`
- `"angle"`
- `"basis"`

For large workloads, QDP uses multiple CUDA streams and CUDA events to overlap:

- **H2D copies** (copy stream)
- **kernel execution** (compute stream)

This reduces time spent waiting on PCIe transfers and can improve throughput substantially for large batches.

---

QDP exposes results using the **DLPack protocol**, which allows frameworks like PyTorch to consume GPU memory **without copying**.

Conceptually:

1. Rust allocates GPU memory for the state vector.
2. Rust wraps it into a DLPack `DLManagedTensor`.
3. Python returns an object that implements `__dlpack__`.
4. PyTorch calls `torch.from_dlpack(qtensor)` and takes ownership via DLPack's deleter.

Important details:

- The returned DLPack capsule is **single-consume** (can only be used once). This prevents double-free bugs.
- Memory lifetime is managed safely via reference counting on the Rust side, and freed by the DLPack deleter when the consumer releases it.

---

- GPU kernels replace circuit-based state preparation for the supported encodings.
- Batch APIs reduce allocation and kernel launch overhead.
- Streaming pipelines overlap IO and GPU compute.

- **Prefer batch encoding** when encoding many samples (lower overhead, better GPU utilization).
- **Keep `num_qubits` realistic**. Output size is

<math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><msup><mn>2</mn><mi>n</mi></msup></mrow><annotation>2^n</annotation></semantics></math>

  2n and becomes the dominant cost quickly.
- **Pick the right encoding**:
  - amplitude: dense real-valued vectors
  - angle: one real angle per qubit (product state)
  - basis: discrete indices / categorical states

If you need to understand where time is spent (copy vs compute), QDP supports NVTX-based profiling. See [Observability](#qdp-observability).

---

<a id="qdp-api"></a>

<!-- source_url: https://mahout.apache.org/docs/qdp/api/ -->

<!-- page_index: 12 -->

# API Reference

Version: latest

Mahout QDP (Quantum Data Plane) provides GPU-accelerated quantum state encoding.
It writes classical data directly into GPU memory and returns a DLPack-compatible
handle for zero-copy integration with downstream frameworks.

Prefer importing from `qumat.qdp`; the native extension is `_qdp`.

```python
import qumat.qdp as qdp 
# or: from _qdp import QdpEngine, QuantumTensor 
```

Create a GPU encoder instance.

**Parameters**

- `device_id` (int): CUDA device ID, default `0`.
- `precision` (str): `"float32"` or `"float64"`.

**Raises**

- `RuntimeError`: Initialization failure or unsupported precision.

Encode classical input into a quantum state and return a DLPack tensor on GPU.

**Parameters**

- `data`: Supported inputs
  - `list[float]`
  - `numpy.ndarray` (1D/2D, dtype=float64, C-contiguous)
  - `torch.Tensor` (CPU, float64, contiguous)
  - `str` / `pathlib.Path` file path
    - `.parquet`, `.arrow` / `.feather`, `.npy`, `.pt` / `.pth`, `.pb`
    - remote URL (`s3://bucket/key`, `gs://bucket/key`) when built with `remote-io`
- `num_qubits` (int): Number of qubits, range 1–30.
- `encoding_method` (str): `"amplitude" | "angle" | "basis" | "iqp" | "iqp-z"` (lowercase).

**Returns**

- `QuantumTensor` with 2D shape:
  - single sample: `[1, 2^num_qubits]`
  - batch: `[batch_size, 2^num_qubits]`

**Notes**

- Output dtype is `complex64` (`precision="float32"`) or `complex128` (`precision="float64"`).
- Parquet streaming currently supports `"amplitude"` and `"basis"`.
- PyTorch file inputs (`.pt`, `.pth`) require building with the `pytorch` feature.
- Remote URL query/fragment is not supported (`?versionId=...`, `#...`).

**Raises**

- `RuntimeError`: Invalid inputs, shapes, dtypes, or unsupported formats.

Encode directly from a TensorFlow TensorProto file (`.pb`).

DLPack wrapper for GPU-resident quantum states.

Return a DLPack PyCapsule. This can be consumed only once.

Return `(device_type, device_id)`; CUDA devices report `(2, gpu_id)`.

**Ownership & Lifetime**

- If not consumed, memory is freed when the object is dropped.
- If consumed, ownership transfers to the consumer (e.g., PyTorch).

- Input length `<= 2^num_qubits`; remaining entries are zero-padded.
- L2 normalization is applied.
- Zero vectors / NaN / Inf raise errors.

- Each sample must provide exactly `num_qubits` angles.
- NaN / Inf raise errors.

- Each sample provides one integer index in `[0, 2^num_qubits)`.

- Expects `n + n*(n-1)/2` parameters for `n = num_qubits` (Z + ZZ terms).
- All parameters must be finite (no NaN/Inf).

- Expects `n` parameters for `n = num_qubits` (Z terms only).
- All parameters must be finite (no NaN/Inf).

- **Parquet**: `.parquet`
- **Arrow IPC**: `.arrow`, `.feather`
- **NumPy**: `.npy`
- **PyTorch**: `.pt`, `.pth` (requires `pytorch` feature)
- **TensorFlow**: `.pb` (TensorProto)

- `num_qubits` out of range.
- Input length exceeds `2^num_qubits`.
- Non-`float64` NumPy/Torch inputs.
- Torch tensors not on CPU or not contiguous.
- DLPack capsule consumed more than once.

- Linux with an NVIDIA GPU (CUDA).
- CUDA driver/toolkit installed.
- Python 3.10–3.12 (`requires-python >=3.10,<3.13`).
- `qumat` installed (the QDP native extension ships as `qumat-qdp`).
- Optional: `torch` for DLPack integration, `numpy` for NumPy inputs.

No deprecations are planned for the initial PoC.

---

<a id="qdp-examples"></a>

<!-- source_url: https://mahout.apache.org/docs/qdp/examples/ -->

<!-- page_index: 13 -->

# Examples

Version: latest

> [!NOTE]
> **Coming Soon**
> This documentation is under development. Check back soon!

---

<a id="qdp-readers"></a>

<!-- source_url: https://mahout.apache.org/docs/qdp/readers/ -->

<!-- page_index: 14 -->

# QDP Input Format Architecture

Version: latest

This document describes the refactored input handling system in QDP that makes it easy to support multiple data formats.

QDP now uses a trait-based architecture for reading quantum data from various sources. This design allows adding new input formats (NumPy, PyTorch, HDF5, etc.) without modifying core library code.

Basic interface for batch reading:

```rust
pub trait DataReader { 
    fn read_batch(&mut self) -> Result<(Vec<f64>, usize, usize)>; 
    fn get_sample_size(&self) -> Option<usize> { None } 
    fn get_num_samples(&self) -> Option<usize> { None } 
} 
```

Extended interface for large files that don't fit in memory:

```rust
pub trait StreamingDataReader: DataReader { 
    fn read_chunk(&mut self, buffer: &mut [f64]) -> Result<usize>; 
    fn total_rows(&self) -> usize; 
} 
```

| Format | Reader | Streaming | Status |
| --- | --- | --- | --- |
| Parquet | `ParquetReader` | ✅ `ParquetStreamingReader` | ✅ Complete |
| Arrow IPC | `ArrowIPCReader` | ❌ | ✅ Complete |
| NumPy | `NumpyReader` | ❌ | ✅ Complete |
| PyTorch | `TorchReader` | ❌ | ✅ (feature: `pytorch`) |

Adding a new format requires only:

- Implementing the `DataReader` trait
- Registering in `readers/mod.rs`
- Optional: Add convenience functions

No changes to core QDP code needed!

- Traits use static dispatch where possible
- No runtime polymorphism overhead in hot paths
- Same zero-copy and streaming capabilities as before
- No memory allocation overhead

All existing APIs continue to work:

```rust
// Old API still works 
let (data, samples, size) = read_parquet_batch("data.parquet")?; 
let (data, samples, size) = read_arrow_ipc_batch("data.arrow")?; 
 
// ParquetBlockReader is now an alias to ParquetStreamingReader 
let mut reader = ParquetBlockReader::new("data.parquet", None)?; 
reader.read_chunk(&mut buffer)?; 
```

Readers can be used generically:

```rust
fn process_data<R: DataReader>(mut reader: R) -> Result<()> { 
    let (data, samples, size) = reader.read_batch()?; 
    // Process data... 
} 
 
// Works with any reader! 
process_data(ParquetReader::new("data.parquet", None)?)?; 
process_data(ArrowIPCReader::new("data.arrow")?)?; 
```

```rust
use qdp_core::reader::DataReader; 
use qdp_core::readers::ArrowIPCReader; 
 
let mut reader = ArrowIPCReader::new("quantum_states.arrow")?; 
let (data, num_samples, sample_size) = reader.read_batch()?; 
 
println!("Read {} samples of {} qubits", 
         num_samples, (sample_size as f64).log2() as usize); 
```

```rust
use qdp_core::reader::StreamingDataReader; 
use qdp_core::readers::ParquetStreamingReader; 
 
let mut reader = ParquetStreamingReader::new("large_dataset.parquet", None)?; 
let mut buffer = vec![0.0; 1024 * 1024]; // 1M element buffer 
 
loop { 
    let written = reader.read_chunk(&mut buffer)?; 
    if written == 0 { break; } 
 
    // Process chunk 
    process_chunk(&buffer[..written])?; 
} 
```

```rust
fn read_quantum_data(path: &str) -> Result<(Vec<f64>, usize, usize)> { 
    use qdp_core::reader::DataReader; 
 
    if path.ends_with(".parquet") { 
        ParquetReader::new(path, None)?.read_batch() 
    } else if path.ends_with(".arrow") { 
        ArrowIPCReader::new(path)?.read_batch() 
    } else if path.ends_with(".npy") { 
        NumpyReader::new(path)?.read_batch() 
    } else if path.ends_with(".pt") || path.ends_with(".pth") { 
        TorchReader::new(path)?.read_batch() 
    } else { 
        Err(MahoutError::InvalidInput("Unsupported format".into())) 
    } 
} 
```

See ADDING\_INPUT\_FORMATS.md (TODO) for detailed instructions.

Quick overview:

1. Create `readers/myformat.rs`
2. Implement `DataReader` trait
3. Add to `readers/mod.rs`
4. Add tests
5. (Optional) Add convenience functions

```text
qdp-core/src/ 
├── reader.rs              # Trait definitions 
├── readers/ 
│   ├── mod.rs            # Reader registry 
│   ├── parquet.rs        # Parquet implementation 
│   ├── arrow_ipc.rs      # Arrow IPC implementation 
│   ├── numpy.rs          # NumPy implementation 
│   └── torch.rs          # PyTorch (feature-gated) 
├── io.rs                 # Legacy API & helper functions 
└── lib.rs                # Main library 
 
examples/ 
└── flexible_readers.rs   # Demo of architecture 
 
docs/ 
├── readers/ 
│   └── README.md         # This file 
└── ADDING_INPUT_FORMATS.md  # Extension guide 
```

- **Parquet Streaming**: Constant memory usage for any file size
- **Zero-copy**: Direct buffer access where possible
- **Pre-allocation**: Reserves capacity when total size is known

- **Static dispatch**: No virtual function overhead
- **Batch operations**: Minimizes function call overhead
- **Efficient formats**: Columnar storage (Parquet/Arrow) for fast reading

The architecture maintains the same performance as before:

- Parquet streaming: ~2GB/s throughput
- Arrow IPC: ~4GB/s throughput (zero-copy)
- Memory usage: O(buffer\_size), not O(file\_size)

No changes required! All existing code continues to work.

If you were directly using internal reader structures:

**Before:**

```rust
let reader = ParquetBlockReader::new(path, None)?; 
```

**After:**

```rust
// Still works (it's a type alias) 
let reader = ParquetBlockReader::new(path, None)?; 
 
// Or use the new name 
let reader = ParquetStreamingReader::new(path, None)?; 
```

Planned format support:

- **NumPy streaming**: Chunked reads for large `.npy` files
- **PyTorch streaming**: Streaming support for large tensors
- **HDF5** (`.h5`): Scientific data storage
- **JSON**: Human-readable format for small datasets
- **CSV**: Simple tabular data

- See examples: `cargo run --example flexible_readers`
- Read extension guide: ADDING\_INPUT\_FORMATS.md (TODO)
- Check tests: `qdp-core/tests/*_io.rs`

---

<a id="qdp-observability"></a>

<!-- source_url: https://mahout.apache.org/docs/qdp/observability/ -->

<!-- page_index: 15 -->

# NVTX Profiling Guide

Version: latest

NVTX (NVIDIA Tools Extension) provides performance markers visible in Nsight Systems. This project uses zero-cost macros that compile to no-ops when the `observability` feature is disabled.

Default builds exclude NVTX for zero overhead. Enable profiling with:

```bash
cd mahout/qdp 
cargo build -p qdp-core --example nvtx_profile --features observability --release 
```

```bash
./target/release/examples/nvtx_profile 
```

**Expected output:**

```text
=== NVTX Profiling Example === 
 
✓ Engine initialized 
✓ Created test data: 1024 elements 
 
Starting encoding (NVTX markers will appear in Nsight Systems)... 
Expected NVTX markers: 
  - Mahout::Encode 
  - CPU::L2Norm 
  - GPU::Alloc 
  - GPU::H2DCopy 
  - GPU::KernelLaunch 
  - GPU::Synchronize 
  - DLPack::Wrap 
 
✓ Encoding succeeded 
✓ DLPack pointer: 0x558114be6250 
✓ Memory freed 
 
=== Test Complete === 
```

```bash
nsys profile --trace=cuda,nvtx -o report ./target/release/examples/nvtx_profile 
```

This generates `report.nsys-rep` and `report.sqlite`.

Open the report in Nsight Systems GUI:

```bash
nsys-ui report.nsys-rep 
```

In the GUI timeline view, you will see:

- Colored blocks for each NVTX marker
- CPU timeline showing `CPU::L2Norm`
- GPU timeline showing `GPU::Alloc`, `GPU::H2DCopy`, `GPU::Kernel`
- Overall workflow covered by `Mahout::Encode`

View summary statistics:

```bash
nsys stats report.nsys-rep 
```

**Example NVTX Range Summary output:**

```text
Time (%)  Total Time (ns)  Instances    Avg (ns)      Med (ns)     Min (ns)    Max (ns)   StdDev (ns)   Style        Range 
--------  ---------------  ---------  ------------  ------------  ----------  ----------  -----------  --------  -------------- 
   50.0       11,207,505          1  11,207,505.0  11,207,505.0  11,207,505  11,207,505          0.0  StartEnd  Mahout::Encode 
   48.0       10,759,758          1  10,759,758.0  10,759,758.0  10,759,758  10,759,758          0.0  StartEnd  GPU::Alloc 
    1.8          413,753          1     413,753.0     413,753.0     413,753     413,753          0.0  StartEnd  CPU::L2Norm 
    0.1           15,873          1      15,873.0      15,873.0      15,873      15,873          0.0  StartEnd  GPU::H2DCopy 
    0.0              317          1         317.0         317.0         317         317          0.0  StartEnd  GPU::KernelLaunch 
```

The output shows:

- Time percentage for each operation
- Total time in nanoseconds
- Number of instances
- Average, median, min, max execution times

**CUDA API Summary** shows detailed CUDA call statistics:

Time (%) Total Time (ns) Num Calls Avg (ns) Med (ns) Min (ns) Max (ns) StdDev (ns) Name

---

```text
 99.2       11,760,277          2  5,880,138.5  5,880,138.5     2,913  11,757,364  8,311,652.0  cuMemAllocAsync 
  0.4           45,979          2     22,989.5     22,989.5     7,938      38,041     21,286.0  cuMemcpyHtoDAsync_v2 
  0.1           14,722          1     14,722.0     14,722.0    14,722      14,722          0.0  cuEventCreate 
  0.1           13,100          3      4,366.7      3,512.0       861       8,727      4,002.0  cuStreamSynchronize 
  0.1            9,468         11        860.7        250.0       114       4,671      1,453.3  cuCtxSetCurrent 
  0.1            6,479          1      6,479.0      6,479.0     6,479       6,479          0.0  cuEventDestroy_v2 
  0.0            4,599          2      2,299.5      2,299.5     1,773       2,826        744.6  cuMemFreeAsync 
```

- Memory allocation (`cuMemAllocAsync`)
- Memory copies (`cuMemcpyHtoDAsync_v2`)
- Stream synchronization (`cuStreamSynchronize`)

The following markers are tracked:

- `Mahout::Encode` - Complete encoding workflow
- `CPU::L2Norm` - L2 normalization on CPU
- `GPU::Alloc` - GPU memory allocation
- `GPU::H2DCopy` - Host-to-device memory copy
- `GPU::KernelLaunch` - CPU-side kernel launch
- `GPU::Synchronize` - CPU waiting for GPU completion
- `DLPack::Wrap` - Conversion to DLPack pointer

The project provides zero-cost macros in `qdp-core/src/profiling.rs`:

```rust
// Profile a scope (automatically pops on exit) 
crate::profile_scope!("MyOperation"); 
 
// Mark a point in time 
crate::profile_mark!("Checkpoint"); 
```

When `observability` feature is disabled, these macros compile to no-ops with zero runtime cost.

Source code: `qdp-core/examples/nvtx_profile.rs`

**NVTX markers not appearing:**

- Ensure `--features observability` is used during build
- Verify CUDA device is available
- Check that encoding actually executes

**nsys warnings:**
Warnings about CPU sampling are normal and can be ignored. They do not affect NVTX marker recording.

---

<a id="qdp-testing"></a>

<!-- source_url: https://mahout.apache.org/docs/qdp/testing/ -->

<!-- page_index: 16 -->

# QDP Core Test Suite

Version: latest

Unit tests for QDP core library covering input validation, API workflows, and memory safety.

- Invalid encoder strategy rejection
- Qubit size validation (mismatch, zero, max limit 30)
- Empty and zero-norm data rejection
- Error type formatting
- Non-Linux platform graceful failure

- Engine initialization
- Amplitude encoding with DLPack pointer management

- Memory leak detection (100 encode/free cycles)
- Concurrent state vector management
- DLPack tensor metadata validation

- Simulates a QML training loop that streams batches of 64 vectors
- Producer/consumer model with configurable prefetch to avoid GPU starvation
- Reports vectors-per-second to verify QDP keeps the GPU busy
- Run: `cargo run -p qdp-core --example dataloader_throughput --release`
- Environment overrides: `BATCHES=<usize>` (default 200), `PREFETCH=<usize>` (default 16)

- `create_test_data(size)`: Generates normalized test data

```bash
# Run all tests cargo test --package qdp-core
 
# Run specific test file cargo test --package qdp-core --test validation cargo test --package qdp-core --test api_workflow cargo test --package qdp-core --test memory_safety
```

- Linux OS (tests skip on other platforms)
- CUDA-capable GPU (tests skip if unavailable)
- Rust toolchain with CUDA support

---

<a id="advanced-pqc"></a>

<!-- source_url: https://mahout.apache.org/docs/advanced/pqc/ -->

<!-- page_index: 17 -->

# Parameterized Quantum Circuits: Developer's Guide

Version: latest

Welcome to the guide designed for developers interested in implementing parameterized quantum circuits (PQCs) from scratch. This document provides detailed information about the theory, design, and applications of PQCs without reliance on existing quantum computing frameworks like Qiskit or Cirq.

---

1. **Introduction to Parameterized Quantum Circuits**
2. **Variational Quantum Algorithms**
3. **Designing Parameterized Quantum Circuits**
4. **Training Parameterized Quantum Circuits**
5. **Quantum Machine Learning with PQCs**
6. **Optimization Challenges and Solutions**
7. **Noise and Error Mitigation in PQCs**
8. **Expressibility and Entanglement in PQCs**
9. **Hardware Considerations and Implementations**
10. **Advanced Applications of PQCs**
11. **Scalability and Resource Estimations**
12. **Current Research and Open Problems**

---

Quantum gates are the building blocks of quantum circuits, functioning similarly to classical logic gates but operating on qubits, the fundamental units of quantum information. Unlike classical bits, which can be either 0 or 1, qubits can exist in superpositions of states, represented as linear combinations of |0⟩ and |1⟩.

**Universal Gate Sets:** To perform arbitrary quantum computations, it's essential to understand universal gate sets. A set of quantum gates is considered universal if any unitary operation (any quantum computation) can be approximated to arbitrary accuracy using these gates. Common universal gate sets include the set of Hadamard (H), CNOT, and

<math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>T</mi></mrow><annotation>T</annotation></semantics></math>

T gates. The H gate creates superpositions, CNOT is an entangling operation, and the

<math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>T</mi></mrow><annotation>T</annotation></semantics></math>

T gate provides a necessary phase shift.

Parameterized gates are quantum gates that include parameters that can be adjusted, often continuously. These gates are integral to parameterized quantum circuits, as their parameters can be optimized during algorithms. Common parameterized gates include rotation gates such as

<math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><msub><mi>R</mi><mi>x</mi></msub><mo>(</mo><mi>θ</mi><mo>)</mo></mrow><annotation>R_x(\theta)</annotation></semantics></math>

Rx(θ),

<math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><msub><mi>R</mi><mi>y</mi></msub><mo>(</mo><mi>θ</mi><mo>)</mo></mrow><annotation>R_y(\theta)</annotation></semantics></math>

Ry(θ), and

<math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><msub><mi>R</mi><mi>z</mi></msub><mo>(</mo><mi>θ</mi><mo>)</mo></mrow><annotation>R_z(\theta)</annotation></semantics></math>

Rz(θ), each corresponding to a rotation around the respective axes in the Bloch sphere representation of a qubit.

**Rotation Gates:** For instance, a rotation gate around the x-axis,

<math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><msub><mi>R</mi><mi>x</mi></msub><mo>(</mo><mi>θ</mi><mo>)</mo></mrow><annotation>R_x(\theta)</annotation></semantics></math>

Rx(θ), can be represented by the unitary operation:

<math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><msub><mi>R</mi><mi>x</mi></msub><mo>(</mo><mi>θ</mi><mo>)</mo><mo>=</mo><mi>exp</mi><mo>⁡</mo><mrow><mo>(</mo><mo>−</mo><mi>i</mi><mfrac><mi>θ</mi><mn>2</mn></mfrac><msub><mi>σ</mi><mi>x</mi></msub><mo>)</mo></mrow></mrow><annotation>R_x(\theta) = \exp\left(-i \frac{\theta}{2} \sigma_x\right)</annotation></semantics></math>

Rx(θ)=exp(−i2θσx)
where

<math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><msub><mi>σ</mi><mi>x</mi></msub></mrow><annotation>\sigma_x</annotation></semantics></math>

σx is the Pauli X matrix. The parameter

<math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>θ</mi></mrow><annotation>\theta</annotation></semantics></math>

θ can be adjusted during the circuit's operation, which is key in variational and learning-based quantum algorithms.

The motivation for using parameterized quantum circuits (PQCs) rests in their adaptability and efficiency in capturing complex quantum phenomena. PQCs are a powerful tool for near-term quantum computing, particularly in approaches like hybrid quantum-classical algorithms where classical optimizers adjust quantum circuit parameters to minimize error or energy functions.

**Near-Term Applications:** PQCs are pivotal in the realm of Noisy Intermediate-Scale Quantum (NISQ) technology, where current quantum hardware limitations require algorithms that do not require fault-tolerant quantum error correction. They are used extensively in variational quantum algorithms, where quantum resources are utilized to process information, and classical algorithms handle the parameter optimization.

By understanding these foundational concepts, developers can implement software architectures that accurately simulate and manipulate parameterized quantum circuits, forming a basis for advanced quantum computational applications.

Variational Quantum Algorithms (VQAs) leverage the principles of both quantum mechanics and classical optimization to solve complex problems efficiently. They are central to near-term applications of quantum computing because of their ability to work within the constraints of noisy intermediate-scale quantum (NISQ) devices.

The variational principle is a foundational concept in quantum mechanics, especially useful for approximating the ground state energy of a quantum system. The basic idea is that the lowest energy an electron in a molecule can have is governed by this principle. By constructing a parameterized quantum circuit to prepare various quantum states that serve as trial solutions, VQAs explore the energy landscape to find the state that minimizes a given cost function, typically expected energy.

- **Variational Quantum Eigensolver (VQE):** A VQA designed to find the eigenvalues of a Hamiltonian, which is crucial in quantum chemistry for determining molecule energy levels. VQE encodes the Hamiltonian of a molecule into a PQC. The circuit parameters are tuned using a classical optimizer to minimize the expectation value of the Hamiltonian, thereby approximating the molecule's ground state energy.
- **Quantum Approximate Optimization Algorithm (QAOA):** This algorithm is used for solving combinatorial optimization problems. QAOA represents problem constraints as Hamiltonians and finds the bit string that minimizes these constraints. The algorithm uses a PQC to approximate the solution state, systematically optimizing its parameters to improve the solution quality.

In the context of VQAs, PQCs act as an approximation model which can be adjusted through parameter tuning. Unlike traditional quantum algorithms that require a precise sequence of quantum operations, PQCs provide a flexible framework where parameters can be continuously varied. This adaptability makes them well-suited for iterative optimization processes essential in VQAs.

PQCs leverage parameterized gates capable of representing a wide class of quantum states. Through classical-quantum interplay, where quantum circuits process the data while classical systems optimize the parameters based on the feedback, the PQCs are tuned to solve specific problems or approximate desired states. This makes PQCs integral to enabling VQAs to achieve high fidelity results while remaining viable on NISQ devices.

Overall, VQAs represent one of the most promising approaches to practical quantum advantage. They serve as a bridge from current hardware capabilities to solving meaningful problems, with PQCs being the core mechanism allowing flexibility, adaptability, and execution within noisy constraints.

A variational quantum circuit or ansatz is a crucial part of designing parameterized quantum circuits. The design of these circuits can be oriented towards hardware efficiency, problem inspiration, or heuristic patterns:

- **Hardware-Efficient Ansätze:** These are designed to work well on existing quantum devices, minimizing the circuit depth and using gates that are easily implementable on specific quantum hardware. For example, these ansätze might use a set of parameterized single-qubit rotation gates and CNOTs pre-optimized for the target hardware's fidelity and connectivity. The main advantage is reduced error rates due to shorter circuits and fewer gate operations.
- **Problem-Inspired Ansätze:** Tailored to exploit the structure of the specific problem at hand, these ansätze draw on insights from the problem's domain, such as quantum chemistry or optimization. For instance, in VQE, one might use ansätze inspired by known efficient classical approximations or simplified physical models of the molecular system.
- **Heuristic Ansätze:** These are not derived from specific physical insights but instead rely on general properties like expressibility and trainability. These might include layered structures where each layer applies the same set of gates. This flexibility can help in exploring a wider state space to find potentially optimal quantum solutions.

Entanglement is a fundamental resource in quantum computing, and how it is introduced in a circuit impacts its efficacy:

- An appropriate entanglement scheme ensures that the ansatz can explore complex, entangled states of the system, which are essential for solving many quantum problems efficiently. Common schemes involve multi-qubit gate layers like CNOT gates or controlled-Z gates applied in a specific pattern to ensure all qubits are appropriately correlated.
- Balancing the 'amount' and 'distribution' of entanglement is non-trivial and often problem-specific. Too little entanglement might make the circuit unable to represent the required state complexity, whereas excessive entanglement could lead to optimization challenges, such as barren plateaus.

When designing parameterized quantum circuits, a critical challenge is balancing circuit depth and expressibility:

- **Circuit Depth:** A deeper circuit can potentially represent more complex states but also incurs higher noise and decoherence in real quantum hardware. The depth must stay within the coherence time limits of the quantum device to prevent excessive error accumulation.
- **Expressibility:** This refers to the circuit's ability to cover a vast swath of the Hilbert space. More expressibility generally means the circuit can represent a broader range of quantum states, thereby solving a more extensive set of problems or finding better approximations.

The trade-offs must be carefully considered when designing circuits, especially in hardware where decoherence and gate error rates limit the practical depth of any quantum circuit.

These design principles are foundational for creating efficient, effective parameterized quantum circuits that meet the demands of specific applications, striking a fine balance between theoretical expressibility and practical implementability.

**Key Concepts:**

The training of parameterized quantum circuits (PQCs) involves optimizing the parameters of the quantum gates to minimize a specific cost function, typically corresponding to the expectation value of an observable. The two main classes of optimization methods are:

- **Gradient-Based Methods:**
  These methods use derivatives of the cost function with respect to the circuit parameters to navigate the optimization landscape. The **parameter shift rule** is particularly important, as it provides a way to estimate gradients analytically on quantum hardware. The rule leverages the circuit's periodic nature to compute the gradient by evaluating the cost at a small number of shifted parameter values. Common gradient-based techniques include:

  - **Gradient Descent**: Iteratively updates parameters in the direction of the negative gradient.
  - **Adam**: An adaptive learning rate optimization algorithm that combines momentum and scaling techniques.
- **Gradient-Free Methods:**
  These approaches do not require explicit gradient computation and are useful when gradients are costly or infeasible to obtain. Methods like **Nelder-Mead** and **COBYLA** evaluate the cost function at different parameter settings to guide optimization. These methods are often more resilient to noise, making them suitable for noisy quantum devices.

**Barren plateaus** refer to regions in the parameter space where the gradient is extremely small, leading to slow convergence of the optimization algorithms. Several factors contribute to barren plateaus:

- **Circuit Depth**: As circuit depth increases, gradients tend to vanish. Balancing depth with expressibility is crucial.
- **Random Initialization**: Arbitrary parameter initialization can lead to initial points in barren plateaus. Careful initialization strategies are necessary to circumvent this issue.

Mitigation strategies include using circuit architectures tailored to specific problems or employing progressive, layer-wise training to narrow down the parameter space iteratively.

The **parameter shift rule** is an essential tool for obtaining exact gradients of parameters in a PQC. It is specifically designed taking into account the unitary nature of quantum gates. For a parameterized gate

<math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>U</mi><mo>(</mo><mi>θ</mi><mo>)</mo></mrow><annotation>U(\theta)</annotation></semantics></math>

U(θ), the gradient of the expectation value

<math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mo>⟨</mo><mi>ψ</mi><mi>∣</mi><msup><mi>U</mi><mo>†</mo></msup><mo>(</mo><mi>θ</mi><mo>)</mo><mi>O</mi><mi>U</mi><mo>(</mo><mi>θ</mi><mo>)</mo><mi>∣</mi><mi>ψ</mi><mo>⟩</mo></mrow><annotation>\langle \psi | U^{\dagger}(\theta) O U(\theta) | \psi \rangle</annotation></semantics></math>

⟨ψ∣U†(θ)OU(θ)∣ψ⟩ with respect to

<math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>θ</mi></mrow><annotation>\theta</annotation></semantics></math>

θ can be calculated by evaluating the expectation with shifted parameters:

<math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mfrac><mi>d</mi><mrow><mi>d</mi><mi>θ</mi></mrow></mfrac><mo>⟨</mo><mi>ψ</mi><mi>∣</mi><msup><mi>U</mi><mo>†</mo></msup><mo>(</mo><mi>θ</mi><mo>)</mo><mi>O</mi><mi>U</mi><mo>(</mo><mi>θ</mi><mo>)</mo><mi>∣</mi><mi>ψ</mi><mo>⟩</mo><mo>=</mo><mfrac><mn>1</mn><mn>2</mn></mfrac><mrow><mo>(</mo><mo>⟨</mo><mi>ψ</mi><mi>∣</mi><msup><mi>U</mi><mo>†</mo></msup><mo>(</mo><mi>θ</mi><mo>+</mo><mfrac><mi>π</mi><mn>2</mn></mfrac><mo>)</mo><mi>O</mi><mi>U</mi><mo>(</mo><mi>θ</mi><mo>+</mo><mfrac><mi>π</mi><mn>2</mn></mfrac><mo>)</mo><mi>∣</mi><mi>ψ</mi><mo>⟩</mo><mo>−</mo><mo>⟨</mo><mi>ψ</mi><mi>∣</mi><msup><mi>U</mi><mo>†</mo></msup><mo>(</mo><mi>θ</mi><mo>−</mo><mfrac><mi>π</mi><mn>2</mn></mfrac><mo>)</mo><mi>O</mi><mi>U</mi><mo>(</mo><mi>θ</mi><mo>−</mo><mfrac><mi>π</mi><mn>2</mn></mfrac><mo>)</mo><mi>∣</mi><mi>ψ</mi><mo>⟩</mo><mo>)</mo></mrow></mrow><annotation>\frac{d}{d\theta} \langle \psi | U^\dagger(\theta) O U(\theta) |\psi\rangle = \frac{1}{2}\left(\langle \psi | U^\dagger(\theta + \frac{\pi}{2}) O U(\theta + \frac{\pi}{2}) |\psi\rangle - \langle \psi | U^\dagger(\theta - \frac{\pi}{2}) O U(\theta - \frac{\pi}{2}) |\psi\rangle\right)</annotation></semantics></math>

dθd⟨ψ∣U†(θ)OU(θ)∣ψ⟩=21(⟨ψ∣U†(θ+2π)OU(θ+2π)∣ψ⟩−⟨ψ∣U†(θ−2π)OU(θ−2π)∣ψ⟩)

This approach is hardware-efficient since it requires only a few additional circuit evaluations per parameter.

---

These key concepts provide foundational insights into the training procedures for PQCs, emphasizing the careful selection of optimization strategies, understanding the challenges with barren plateaus, and leveraging theoretical methods like the parameter shift rule to achieve effective parameter updates.

**Quantum Classifiers**

Quantum classifiers are used in machine learning to categorize or predict outcomes based on quantum-encoded data. Leveraging PQCs, these classifiers can offer novel approaches to traditional classification tasks by exploiting quantum superposition and entanglement. Unlike classical classifiers, quantum classifiers can potentially offer an exponential increase in feature space, which is particularly advantageous for complex datasets. A typical quantum classifier involves feeding classical data into a quantum circuit, where it is processed by a parameterized circuit before being measured. The outcomes of these measurements are used to make predictions or classifications, often through a post-processing classical algorithm that determines the final output based on quantum results.

**Data Encoding Strategies**

To make use of quantum classifiers, efficient data encoding is crucial:

- **Amplitude Encoding** utilizes the amplitudes of quantum states to encode classical data. This method can encode

<math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><msup><mn>2</mn><mi>n</mi></msup></mrow><annotation>2^n</annotation></semantics></math>

  2n dimensional data into n qubits, offering exponential data compression. However, the challenge lies in preparing the exact quantum state, which can be resource-intensive and sensitive to noise.
- **Angle Encoding** involves mapping classical data points directly to the rotation angles of quantum gates. This simple yet effective method can encode data by transforming features into angles that control the operations of parameterized gates (e.g., RX, RY, RZ). Its advantage lies in the straightforward implementation and flexibility, but it may not fully exploit the exponential scaling potential.

Quantum Machine Learning models often use these encoding strategies to input data into quantum circuits, which, in combination with different PQC designs, perform a wide range of quantum-enhanced computations. The effectiveness of the encoding strategy is context-dependent and often dictates the potential advantage over classical systems.

**Quantum Neural Networks (QNNs)**

Quantum Neural Networks represent a new paradigm inspired by classical neural networks, combining quantum computing principles with deep learning architectures. At their core, QNNs harness parameterized quantum circuits as quantum layers interspersed with classical processing layers. The ability of quantum circuits to span highly complex state spaces offers an avenue for significant representation power.

A QNN typically includes a classical dataset, which is encoded into quantum states and processed through several layers involving parameterized gates. Each layer adjusts parameters during training, akin to updating weights in classical neural networks. QNNs can potentially leverage both classical computing's strengths through hybrid symbiosis and quantum advantages like entanglement and superposition, potentially solving problems intractable by classical counterparts.

**Key Considerations in Implementing Quantum ML Models:**

1. **Scalability:** Current quantum hardware has limitations on qubit count and coherence time. Ensuring circuits are designed with hardware constraints in mind is essential. Scaling QNNs is a non-trivial task and requires careful balancing between depth (and corresponding expressibility) and noise mitigation.
2. **Noisy Intermediate-Scale Quantum (NISQ) Presence:** Tailoring QNN architectures to operate effectively on NISQ devices, which are susceptible to environmental noise, involves employing error mitigation and robust training techniques.
3. **Hybrid Frameworks:** Often QNNs are employed in hybrid frameworks where quantum computation handles certain tasks (e.g., feature space transformations), while the bulk of data manipulation occurs classically. Understanding where quantum processing provides advantages is pivotal for designing effective hybrid solutions.

This section provides a gateway into quantum-enhanced machine learning applications, highlighting critical considerations and emerging approaches in the field through parameterized quantum circuits. The distinct nature of quantum mechanics offers exciting possibilities for future developments in machine learning paradigms.

Barren plateaus present significant challenges in optimizing parameterized quantum circuits (PQCs). These are regions in the parameter space where the gradients of the cost function vanish, making it difficult to locate the optimal parameter settings using gradient descent methods. The presence of barren plateaus often increases with the size and complexity of the quantum circuit, posing a significant hurdle for scalability.

1. **Layerwise Training:** This approach involves training the quantum circuit in layers or segments rather than as a whole. By optimizing each segment individually, one can manage the complexity of the optimization process, thereby reducing the likelihood of encountering barren plateaus.
2. **Random Initialization:** During initialization, parameters can be set randomly in a way that avoids symmetries in the parameter landscape that can lead to flat regions. Using prior knowledge to smartly choose these initial parameters can break symmetries that contribute to barren plateaus.
3. **Adaptive Learning Rates:** Dynamically adjusting the learning rates during training can help navigate around or out of barren plateaus. Low gradients can be handled by slower learning rates that allow for more precise searching of the parameter space.
4. **Heuristic Approaches:** Utilize heuristic or problem-specific information to bias the initialization of parameters or the design of the circuit ansatz to regions of the parameter space with favorable optimization landscapes.

Noise in quantum circuits can exacerbate the challenges posed by barren plateaus, as it can obscure the signal required for successful optimization. Noise originates from hardware imperfections and environmental factors that compromise the accuracy of quantum operations.

1. **Noise-Resilient Cost Functions:** Designing cost functions that are less sensitive to noise can help maintain optimization progress even in the presence of significant hardware noise.
2. **Error Mitigation Strategies:** Techniques like error extrapolation or error correction can be employed to reduce the impact of noise on the optimization process. These methods aim to "simulate" a noise-free environment or directly correct errors introduced by noise.
3. **Robust Circuit Design:** Developing circuits that inherently minimize the effective noise through error-resistant configurations or operational strategies keeps optimization signals strong.
4. **Use of Quantum Simulators for Training:** Simulators can provide an environment to pre-train circuits, allowing them to reach a certain level of optimization before being deployed to real hardware where noise is a factor.

These optimization challenges are fundamental to the development and deployment of effective PQCs, especially in the currently noise-prone quantum computers. By understanding and addressing these issues, developers can significantly enhance the performance and scalability of PQCs in real-world applications.

**Key Concepts:**

- **Hardware Noise**

  Hardware noise is an inherent challenge in quantum computing that affects the reliability and accuracy of quantum computations. Types of noise include decoherence, gate errors, readout errors, and crosstalk, each of which can degrade the performance of Parameterized Quantum Circuits (PQCs). Understanding these noise sources is critical for developing techniques to mitigate their effects. Decoherence refers to the loss of quantum coherence in qubits due to interaction with their environment. Gate errors occur due to imperfections in implementing quantum gates. Readout errors happen during the measurement process, resulting in incorrect qubit states being recorded. Crosstalk involves unintended interactions between qubits or quantum gates, complicating the execution of precise quantum operations. Identifying these errors and modeling their impact help in developing robust mitigation strategies.
- **Error Mitigation Techniques**

  Error mitigation is crucial for enhancing the accuracy of PQCs without the overhead of full quantum error correction, which is not feasible on current noisy intermediate-scale quantum (NISQ) devices. Popular techniques include:

  1. **Zero-Noise Extrapolation:** This approach involves executing the quantum circuit at different noise levels and extrapolating the results to an estimated zero-noise scenario. This can be achieved by intentionally increasing the noise through techniques like gate repetition and using polynomial or linear extrapolation methods to predict results as if no noise were present.
  2. **Probabilistic Error Cancellation:** This method involves creating an error model to characterize the types of noise affecting the circuit. A quantum operation is devised to effectively invert this noise in a probabilistic manner, canceling out errors in expected outcomes. Calculating the inverse operations requires an accurate noise model and efficient computation of the noise-free probability utilizing classical post-processing techniques.

These error mitigation strategies are vital for making PQCs feasible on current quantum hardware, allowing developers to improve the fidelity of quantum operations and obtain reliable results even in the presence of significant noise. Employing these techniques enables practical applications of PQCs, such as variational quantum algorithms and quantum machine learning, on NISQ devices.

**Key Concepts:**

- **Circuit Expressibility:**

  Expressibility in parameterized quantum circuits (PQCs) refers to the ability of a circuit to represent a wide range of quantum states. This is crucial for ensuring that the quantum circuit can span enough of the state space to solve a given problem effectively. When designing a PQC, one must consider whether the chosen ansatz can adequately represent the required state with the available quantum resources. The expressibility can sometimes be quantified using metrics such as the concentration of measure, which evaluates how uniformly the circuit covers the state space over different parameter configurations.

  A highly expressible circuit might not always be desirable, as it could also introduce complexities like barren plateaus—regions in the parameter space where the gradient becomes very small, making optimization difficult. Therefore, developers need to balance expressibility with trainability. This may involve choosing or designing ansätze that are inherently structured to target particular types of problems, leveraging prior knowledge about the problem domain to select more efficient pathways through parameter space.
- **Entanglement Measures:**

  Entanglement is a fundamental resource in quantum computing, enabling the powerful computational capabilities of quantum systems. In the context of PQCs, the degree of entanglement produced by a circuit is often aligned with its potential computational power. Entangled states are necessary for many quantum algorithms that offer a speedup over classical ones.

  To evaluate entanglement within a PQC, one can use various measures, such as the entanglement entropy, which quantifies the degree of entanglement between different parts of a quantum system. A developer must ensure that the circuit design incorporates sufficient entangling operations to leverage this quantum resource effectively. However, similar to expressibility, there's a trade-off involved. Excessive entanglement may lead to increased susceptibility to noise and other decoherence effects in real quantum hardware, especially in noisy intermediate-scale quantum (NISQ) devices, where noise levels are non-negligible.

  In designing a PQC, considering the connectivity of qubits on the target hardware is crucial, as hardware limitations may restrict which qubits can be directly entangled with one another. This necessitates efficient mapping strategies that translate the ideal circuit design into one that respects these constraints while still achieving desired levels of entanglement.

**Gate Fidelities and Connectivity**

The fidelity of quantum gates is a crucial factor in quantum computing. Fidelity measures how accurately a quantum gate performs the operation it is intended to implement. High-fidelity gates are essential to ensure that the quantum computations are reliable and less prone to errors. In practice, gate errors can arise from various sources like cross-talk, decoherence, or imperfect calibration. Developers must design parameterized quantum circuits (PQCs) with these constraints in mind.

Connectivity in quantum hardware pertains to the ability of qubits to interact with one another directly. Not all qubits in a quantum device can be entangled with each other due to specific connectivity graphs set by architecture. This limitation affects the design of PQCs as it determines which qubits can easily share entangled states or swapped gate operations. Efficiently mapping a logical circuit with qubits that optimally fit the connectivity map involves the use of SWAP gates at strategic locations to mitigate the issue, which can otherwise lead to increased circuit depth and further introduce errors.

**Pulse-Level Control**

Pulse-level control refers to the fine-tuning of the microwave or laser pulses that drive quantum gates in a physical quantum system. When qubits are manipulated with pulses that create a desired change in their states, the precision of these operations is paramount. Developers designing PQCs from scratch may delve into pulse calibration and shaping techniques to optimize quantum gate operations. Understanding how pulse distortions affect gate fidelity, and learning how to correct them, allows developers to improve PQC implementations' performance, both in terms of speed and accuracy.

Pulse-level control also opens opportunities for new optimization strategies such as designing custom gates that may offer better performance for certain PQC tasks. By customizing pulse sequences, developers can circumvent some of the inefficiencies present in standard gate operations, thus achieving higher fidelity and reduced execution time. Mastery over pulse control can lead to enhancements in how variational algorithms perform under real-world conditions, where hardware noise and decoherence significantly affect outcomes.

In this section, we delve into some of the cutting-edge applications of parameterized quantum circuits (PQCs) across various fields of research and industry. By exploring these advanced applications, developers can gain insight into the potential of PQCs to solve real-world problems and drive innovation in computing.

Parameterized quantum circuits play a vital role in the domain of quantum generative models. These models, such as Quantum Generative Adversarial Networks (QGANs) and Born Machines, leverage quantum superposition and entanglement to generate complex probabilistic distributions that classical models struggle to replicate.

- **Quantum GANs (QGANs):** Based on the classical GAN architecture, QGANs comprise a generator and a discriminator implemented via PQCs. The generator circuit produces quantum states intended to mimic the true data distribution, while the discriminator evaluates the authenticity of the quantum samples. This adversarial setup allows QGANs to potentially surpass classical generative models in efficiency and performance, particularly for data types where quantum data encoding offers a natural advantage.
- **Born Machines:** Inspired by the probabilistic interpretation of quantum mechanics, Born machines utilize PQCs to define probability distributions through the Born rule. By appropriately setting parameters, these circuits can model complex distributions and have applications in areas such as unsupervised learning and probabilistic inference.

One of the significant applications of PQCs is in quantum chemistry and material science, where these circuits address the computational challenges of simulating molecular and atomic interactions.

- **Molecule Simulation:** PQCs are used in algorithms like the Variational Quantum Eigensolver (VQE) to approximate the electronic structure (ground state energy) of molecules. By designing problem-inspired ansätze, PQCs efficiently capture molecular properties, potentially leading to breakthroughs in understanding chemical reactions, discovering new materials, and optimizing catalysts.
- **Quantum Phase Estimation:** While traditionally considered a resource-intensive task, PQCs employed in variational forms provide a hybrid approach to quantum phase estimation. This influences study areas such as superconductivity and correlated electron systems by offering insights into their energy landscapes and phase structures.

The financial industry is another field ripe for innovation through PQCs, where they offer novel methods for risk assessment, asset pricing, and portfolio optimization.

- **Risk Analysis:** PQCs can model complex financial systems more naturally than classical algorithms by exploiting superposition and entanglement to analyze multiple risk scenarios concurrently. This capability could lead to more accurate predictions and better risk management strategies.
- **Portfolio Optimization:** Using quantum optimization algorithms, such as QAOA with PQCs, investors can potentially solve portfolio optimization problems more efficiently than classical methods, taking into account a multitude of constraints and objectives that characterize financial decisions.

By understanding these advanced applications, developers can conceptualize and implement parameterized quantum circuits in groundbreaking ways, pushing the boundaries of current technological capabilities. As quantum hardware continues to evolve, the scope and impact of PQCs in diverse scientific and commercial sectors are poised to expand dramatically.

---

<a id="advanced-gap-analysis"></a>

<!-- source_url: https://mahout.apache.org/docs/advanced/gap-analysis/ -->

<!-- page_index: 18 -->

# Analysis of the QuMat Codebase for Implementing Parameterized Quantum Circuits

Version: latest

This analysis examines the provided `qumat` codebase to identify the necessary modifications and additions required to implement Parameterized Quantum Circuits (PQCs). The analysis is divided into two parts:

1. **Minimally Viable Product (MVP):** Outlines the essential features and changes needed to support basic PQC functionality.
2. **Feature-Complete Implementation:** Details the additional features and improvements needed to create a robust and comprehensive PQC framework.

---

The `qumat` codebase is designed to provide a unified interface for quantum circuit simulation across multiple backends, including Qiskit, Cirq, and Amazon Braket. The core components include:

- **Backend Modules:** Separate modules for each supported backend (`qiskit_backend.py`, `cirq_backend.py`, `amazon_braket_backend.py`) containing functions to manipulate quantum circuits using the respective libraries.
- **QuMat Class (`qumat.py`):** A class that abstracts backend-specific operations and provides methods to create circuits and apply standard quantum gates.

Currently, the codebase allows users to:

- Create quantum circuits.
- Apply a fixed set of quantum gates (NOT, Hadamard, CNOT, Toffoli, SWAP, Pauli X/Y/Z).
- Execute circuits and obtain measurement results.
- Draw circuits (limited support, backend-dependent).

---

To support basic PQC functionality, the following features and modifications are necessary:

**Shortcoming:**

- The current implementation only includes fixed gates without parameters (e.g., NOT, Hadamard, CNOT).

**Required Changes:**

- **Implement Parameterized Gate Methods:**

  - Add functions to apply parameterized rotation gates such as `R_X(θ)`, `R_Y(θ)`, `R_Z(θ)`, and general single-qubit rotation `U(θ, φ, λ)`.
  - Ensure these methods accept continuous parameters (e.g., rotation angles).
- **Example Function Signature:**


```python
def apply_rotation_x_gate(circuit, qubit_index, theta): 
    # Implementation for rotation around X-axis by angle theta 
```

**Shortcoming:**

- No mechanism to store and update gate parameters within the circuit.

**Required Changes:**

- **Parameter Management:**
  Use variables or symbols to represent parameters that can be updated during optimization.
  Ensure that the parameters are accessible and modifiable after circuit creation.

**Shortcoming:**

- Execution functions do not account for circuits with variable parameters.

**Required Changes:**

- Bind Parameter Values at Execution:
- Modify the execution functions to accept parameter values and bind them to the circuit before execution.
- Ensure backends support parameter binding (may require additional handling for different libraries).

**Shortcoming:**

- No functionality for optimizing parameters (e.g., gradient descent).

**Required Changes:**

- Simple Parameter Update Mechanism:
- Implement a basic optimization loop outside the qumat library, where parameter values are updated based on cost function evaluations.
- Provide support for running circuits with updated parameters.

To create a comprehensive PQC framework, the following features and enhancements are needed:

**Shortcoming:**

- No support for computing gradients of the cost function with respect to circuit parameters.

**Required Additions:**

- **Parameter Shift Rule Implementation:**

  - Implement the parameter shift rule to compute exact gradients for parameterized gates.
  - Provide functions to calculate gradients efficiently.
- **Integration with Automatic Differentiation Libraries:**

  - (Optional) Integrate with libraries that support automatic differentiation to handle complex circuits.

**Enhancements:**

- **Symbolic Parameters:**

  - Implement a system to handle symbolic parameters, enabling complex parameter relationships and shared parameters across gates.
- **Parameter Dictionaries:**

  - Use dictionaries or parameter objects to manage parameter values and updates systematically.

**Shortcoming:**

- No predefined circuit structures (ansätze) commonly used in PQCs.

**Required Additions:**

- **Circuit Templates:**
  - Implement functions to generate commonly used PQC ansätze, such as hardware-efficient ansatz or layered variational circuits.
  - Allow customization of ansatz depth and structure.

**Shortcoming:**

- Lack of built-in optimization routines for training PQCs.

**Required Additions:**

- **Optimization Module:**
  - Include various classical optimization algorithms (gradient-based and gradient-free) tailored for quantum circuits.
  - Provide interfaces for selecting and configuring optimization strategies.

**Enhancements:**

- **Expectation Values:**
  - Implement functions to compute expectation values of observables, which are crucial for many VQAs.
  - Support measurement of arbitrary operators through decomposition into measurable components.

**Shortcoming:**

- No support for simulating noise or implementing error mitigation techniques.

**Required Additions:**

- **Noise Models:**

  - Incorporate noise modeling capabilities to simulate realistic hardware conditions.
  - Allow users to define noise parameters and types (e.g., depolarizing noise, readout errors).
- **Error Mitigation Techniques:**

  - Implement methods like zero-noise extrapolation or probabilistic error cancellation.

**Enhancements:**

- **Improved Circuit Drawing:**
  - Develop a unified circuit drawing utility that provides clear and informative visualizations across backends.

**Enhancements:**

- **Backend Abstraction Improvements:**
  - Refine the backend interface to support additional libraries or custom simulators.
  - Ensure consistent behavior and capabilities across different backends.

**Shortcoming:**

- Limited testing and validation mechanisms.

**Required Additions:**

- **Unit Tests and Integration Tests:**
  - Develop thorough tests for all functionalities, including parameterized gates, optimization routines, and backends.
  - Validate correctness and performance.

**Enhancements:**

- **Detailed Documentation:**
  - Create comprehensive documentation covering all aspects of the library.
  - Include tutorials and examples demonstrating how to implement various PQCs and algorithms.

**Enhancements:**

- **Real Hardware Integration:**
  - Provide support for executing circuits on actual quantum hardware (where available).
  - Handle job submission, monitoring, and result retrieval for hardware devices.

**Enhancements:**

- **Plugin System:**

  - Design the codebase to be extensible, allowing users to add custom gates, ansätze, or optimization algorithms.
- **Community Contributions:**

  - Set up guidelines and infrastructure to encourage community involvement.

---

---

<a id="learning-quantum-computing-primer"></a>

<!-- source_url: https://mahout.apache.org/docs/learning/quantum-computing-primer/ -->

<!-- page_index: 19 -->

# Quantum Computing Primer

Version: latest

- **1.1 What is Quantum Computing?**
- **1.2 Why Quantum Computing?**

- **2.1 Installing `qumat` (TODO)**
- **2.2 Overview of `qumat` (TODO)**

- **3.1 Classical Bits vs. Qubits**
- **3.2 Representing Qubits**
- **3.3 Creating Qubits with `qumat`**

- **4.1 Single-Qubit Gates**
- **4.2 Multi-Qubit Gates**
- **4.3 Applying Gates with `qumat`**

- **5.1 Building Quantum Circuits**
- **5.2 Visualizing Circuits**

- **6.1 Understanding Entanglement**
- **6.2 Entanglement with `qumat`**

- **7.1 Deutsch-Jozsa Algorithm**
- **7.2 Grover's Algorithm**

- **8.1 Introduction to Quantum Error Correction**
- **8.2 Implementing Error Correction with `qumat`**

- **9.1 Quantum Cryptography**
- **9.2 Quantum Simulation**
- **9.3 Quantum Machine Learning**

- **10.1 Quantum Fourier Transform**
- **10.2 Quantum Phase Estimation**
- **10.3 Quantum Annealing**

---

<a id="learning-quantum-computing-primer-introduction"></a>

<!-- source_url: https://mahout.apache.org/docs/learning/quantum-computing-primer/introduction/ -->

<!-- page_index: 20 -->

# 1. Introduction to Quantum Computing

Version: latest

Quantum computing is a revolutionary approach to computation that leverages the principles of quantum mechanics to process information in ways that classical computers cannot. Unlike classical computers, which use bits as the smallest unit of information (representing either a 0 or a 1), quantum computers use **qubits** (quantum bits). Qubits can exist in a **superposition** of states, meaning they can be both 0 and 1 simultaneously. This property allows quantum computers to perform many calculations at once, potentially solving certain problems much faster than classical computers.

- **Qubits**: The fundamental unit of quantum information, which can be in a superposition of states.
- **Superposition**: A quantum phenomenon where a qubit can be in multiple states at once.
- **Entanglement**: A unique quantum property where qubits become interconnected, such that the state of one qubit is directly related to the state of another, even if they are separated by large distances.
- **Quantum Gates**: Operations that manipulate qubits, analogous to classical logic gates but with the ability to exploit quantum phenomena.

Quantum computing has the potential to revolutionize fields such as cryptography, optimization, and material science. For example, quantum algorithms like **Shor's algorithm** can factorize large numbers exponentially faster than classical algorithms, posing a threat to current cryptographic systems. Similarly, **Grover's algorithm** can search unsorted databases quadratically faster than classical methods.

---

Quantum computing is not just a theoretical concept; it has practical implications that could transform industries. Here are some reasons why quantum computing is gaining attention:

- Quantum computers can solve certain problems exponentially faster than classical computers. For example, simulating quantum systems (e.g., molecules for drug discovery) is infeasible for classical computers but manageable for quantum computers.

- Quantum algorithms like Shor's algorithm can break widely used cryptographic schemes, such as RSA, by efficiently factorizing large numbers. This has spurred interest in **quantum-resistant cryptography**.

- Quantum computers can explore multiple solutions simultaneously, making them ideal for optimization problems in logistics, finance, and machine learning.

- Quantum computers can simulate quantum systems, enabling breakthroughs in chemistry, material science, and physics.

- Quantum machine learning algorithms promise to accelerate training and improve model performance for specific tasks.

---

| Feature | Classical Computing | Quantum Computing |
| --- | --- | --- |
| **Basic Unit** | Bit (0 or 1) | Qubit (superposition of 0 and 1) |
| **State Representation** | Deterministic | Probabilistic |
| **Operations** | Logic gates (AND, OR, NOT, etc.) | Quantum gates (X, Y, Z, H, etc.) |
| **Parallelism** | Limited by CPU cores | Exponential parallelism via superposition |
| **Error Correction** | Well-established | Still an active area of research |

---

To begin your journey into quantum computing, you'll use the `qumat` library, which provides a simple and unified interface for working with quantum circuits across different backends (e.g., Amazon Braket, Cirq, Qiskit). Here's a quick example to get you started:

```python
from qumat import QuMat 
 
# Initialize a quantum circuit with 1 qubit 
backend_config = {'backend_name': 'qiskit', 'backend_options': {'simulator_type': 'qasm_simulator', 'shots': 1000}} 
qc = QuMat(backend_config) 
qc.create_empty_circuit(1) 
 
# Apply a Hadamard gate to create a superposition 
qc.apply_hadamard_gate(0) 
 
# Execute the circuit and measure the result 
result = qc.execute_circuit() 
print(result) 
```

In this example, we:

- Created a quantum circuit with 1 qubit.
- Applied a Hadamard gate to put the qubit into a superposition state.
- Measured the qubit to observe the probabilistic outcome.

This is just the beginning! In the next sections, you'll dive deeper into quantum gates, circuits, and algorithms using qumat.

---

- Quantum computing leverages quantum mechanics to process information in fundamentally new ways.
- Qubits, superposition, and entanglement are the building blocks of quantum computing.
- Quantum computing has the potential to solve problems that are intractable for classical computers.
- The `qumat` library provides a simple way to explore quantum computing concepts and algorithms.

In the next section, we'll set up your environment and explore the basics of quantum circuits using `qumat`.

---

<a id="learning-quantum-computing-primer-qubits"></a>

<!-- source_url: https://mahout.apache.org/docs/learning/quantum-computing-primer/qubits/ -->

<!-- page_index: 21 -->

# 3. Quantum Bits (Qubits)

Version: latest

In classical computing, the fundamental unit of information is the **bit**, which can exist in one of two states: `0` or `1`. Quantum computing, however, introduces the concept of a **qubit**, which can exist in a **superposition** of both states simultaneously. This means a qubit can be in a state that is a combination of `0` and `1`, represented as:

<math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>∣</mi><mi>ψ</mi><mo>⟩</mo><mo>=</mo><mi>α</mi><mi>∣</mi><mn>0</mn><mo>⟩</mo><mo>+</mo><mi>β</mi><mi>∣</mi><mn>1</mn><mo>⟩</mo></mrow><annotation>\vert\psi\rangle = \alpha\vert 0\rangle + \beta\vert 1\rangle</annotation></semantics></math>

∣ψ⟩=α∣0⟩+β∣1⟩

where

<math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>α</mi></mrow><annotation>\alpha</annotation></semantics></math>

α and

<math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>β</mi></mrow><annotation>\beta</annotation></semantics></math>

β are complex numbers representing the probability
amplitudes of the qubit being in the

<math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>∣</mi><mn>0</mn><mo>⟩</mo></mrow><annotation>\vert 0\rangle</annotation></semantics></math>

∣0⟩ and

<math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>∣</mi><mn>1</mn><mo>⟩</mo></mrow><annotation>\vert 1\rangle</annotation></semantics></math>

∣1⟩ states, respectively. The probabilities of measuring the qubit in either state are given
by

<math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>∣</mi><mi>α</mi><msup><mi>∣</mi><mn>2</mn></msup></mrow><annotation>\vert\alpha\vert^2</annotation></semantics></math>

∣α∣2 and

<math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>∣</mi><mi>β</mi><msup><mi>∣</mi><mn>2</mn></msup></mrow><annotation>\vert\beta\vert^2</annotation></semantics></math>

∣β∣2, and they must satisfy the normalization condition:

<math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>∣</mi><mi>α</mi><msup><mi>∣</mi><mn>2</mn></msup><mo>+</mo><mi>∣</mi><mi>β</mi><msup><mi>∣</mi><mn>2</mn></msup><mo>=</mo><mn>1</mn></mrow><annotation>\vert\alpha\vert^2 + \vert\beta\vert^2 = 1</annotation></semantics></math>

∣α∣2+∣β∣2=1

Qubits can be visualized using the **Bloch sphere**, a geometric representation
of the quantum state of a single qubit. The Bloch sphere is a unit sphere where
the north and south poles represent the

<math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>∣</mi><mn>0</mn><mo>⟩</mo></mrow><annotation>\vert 0\rangle</annotation></semantics></math>

∣0⟩ and

<math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>∣</mi><mn>1</mn><mo>⟩</mo></mrow><annotation>\vert 1\rangle</annotation></semantics></math>

∣1⟩ states, respectively. Any point on the surface of the sphere represents a valid quantum
state of the qubit.

The state of a qubit can also be described using a **state vector** in a
two-dimensional complex vector space. For example, the state

<math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>∣</mi><mn>0</mn><mo>⟩</mo></mrow><annotation>\vert 0\rangle</annotation></semantics></math>

∣0⟩ is
represented as:

<math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>∣</mi><mn>0</mn><mo>⟩</mo><mo>=</mo><mrow><mo>(</mo><mtable><mtr><mtd><mstyle><mn>1</mn></mstyle></mtd></mtr><mtr><mtd><mstyle><mn>0</mn></mstyle></mtd></mtr></mtable><mo>)</mo></mrow></mrow><annotation>\vert 0\rangle = \begin{pmatrix} 1 \\ 0 \end{pmatrix}</annotation></semantics></math>

∣0⟩=(10)

and the state

<math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>∣</mi><mn>1</mn><mo>⟩</mo></mrow><annotation>\vert 1\rangle</annotation></semantics></math>

∣1⟩ is represented as:

<math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>∣</mi><mn>1</mn><mo>⟩</mo><mo>=</mo><mrow><mo>(</mo><mtable><mtr><mtd><mstyle><mn>0</mn></mstyle></mtd></mtr><mtr><mtd><mstyle><mn>1</mn></mstyle></mtd></mtr></mtable><mo>)</mo></mrow></mrow><annotation>\vert 1\rangle = \begin{pmatrix} 0 \\ 1 \end{pmatrix}</annotation></semantics></math>

∣1⟩=(01)

In `qumat`, qubits are created by initializing a quantum circuit with a specified number of qubits. The `create_empty_circuit` function is used to create a circuit with a given number of qubits. Here's an example of creating a quantum circuit with a single qubit:

```python
from qumat import QuMat 
 
# Initialize the quantum circuit with a single qubit 
backend_config = { 
    'backend_name': 'qiskit',  # Choose the backend (e.g., 'qiskit', 'cirq', 'amazon_braket') 
    'backend_options': { 
        'simulator_type': 'qasm_simulator',  # Type of simulator 
        'shots': 1000  # Number of shots (measurements) 
    } 
} 
 
qc = QuMat(backend_config) 
qc.create_empty_circuit(1)  # Create a circuit with 1 qubit 
```

In this example, we initialize a quantum circuit with one qubit using the qiskit backend. The create\_empty\_circuit function sets up the circuit, and we can now apply quantum gates to manipulate the qubit.

The Hadamard gate (

<math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>H</mi></mrow><annotation>H</annotation></semantics></math>

H) is a fundamental quantum gate that puts a qubit into a
superposition state. Applying the Hadamard gate to a qubit initially in the

<math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>∣</mi><mn>0</mn><mo>⟩</mo></mrow><annotation>\vert 0\rangle</annotation></semantics></math>

∣0⟩ state results in the state:

<math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>H</mi><mi>∣</mi><mn>0</mn><mo>⟩</mo><mo>=</mo><mfrac><mn>1</mn><msqrt><mn>2</mn></msqrt></mfrac><mo>(</mo><mi>∣</mi><mn>0</mn><mo>⟩</mo><mo>+</mo><mi>∣</mi><mn>1</mn><mo>⟩</mo><mo>)</mo></mrow><annotation>H\vert 0\rangle = \frac{1}{\sqrt{2}}(\vert 0\rangle + \vert 1\rangle)</annotation></semantics></math>

H∣0⟩=2

<svg height="1.08em" preserveaspectratio="xMinYMin slice" viewbox="0 0 400000 1080" width="400em" xmlns="http://www.w3.org/2000/svg"><path></path></svg>

1(∣0⟩+∣1⟩)

Here's how you can apply a Hadamard gate to a qubit using qumat:

```python
# Apply the Hadamard gate to the first qubit (index 0) 
qc.apply_hadamard_gate(0) 
 
# Execute the circuit and get the measurement results 
result = qc.execute_circuit() 
print(result) 
```

In this example, the Hadamard gate is applied to the qubit at index 0, and the
circuit is executed to obtain the measurement results. The output will show the
probabilities of measuring the qubit in the

<math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>∣</mi><mn>0</mn><mo>⟩</mo></mrow><annotation>\vert 0\rangle</annotation></semantics></math>

∣0⟩ and

<math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>∣</mi><mn>1</mn><mo>⟩</mo></mrow><annotation>\vert 1\rangle</annotation></semantics></math>

∣1⟩ states.

You can also visualize the quantum circuit using the draw method:

```python
# Draw the circuit 
qc.draw() 
```

This returns a textual representation of the circuit, which you can print with `print(qc.draw())` or use programmatically. The visualization shows the sequence of gates applied to the qubits.

---

This section introduced the concept of qubits, their representation, and how to create and manipulate them using the qumat library. In the next section, we will explore quantum gates in more detail and learn how to apply them to perform quantum operations.

---

<a id="learning-quantum-computing-primer-quantum-gates"></a>

<!-- source_url: https://mahout.apache.org/docs/learning/quantum-computing-primer/quantum-gates/ -->

<!-- page_index: 22 -->

# 4. Quantum Gates

Version: latest

Quantum gates are the building blocks of quantum circuits, analogous to classical logic gates in classical computing. They manipulate qubits, enabling the creation of complex quantum algorithms. In this section, we will explore the different types of quantum gates and how to apply them using the `qumat` library.

Single-qubit gates operate on a single qubit, changing its state. Some of the most common single-qubit gates include:

- **Pauli-X Gate**: Similar to the classical NOT gate, it flips the state of a qubit.
- **Pauli-Y Gate**: Introduces a phase flip and a bit flip.
- **Pauli-Z Gate**: Introduces a phase flip without changing the bit value.
- **Hadamard Gate**: Creates superposition by transforming the basis states.
- **Rotation Gates (Rx, Ry, Rz)**: Rotate the qubit state around the X, Y, or Z axis of the Bloch sphere.

```python
from qumat import QuMat 
 
# Initialize the quantum circuit with 1 qubit 
backend_config = {'backend_name': 'qiskit', 'backend_options': {'simulator_type': 'qasm_simulator', 'shots': 1000}} 
qc = QuMat(backend_config) 
qc.create_empty_circuit(1) 
 
# Apply the Hadamard gate to the first qubit 
qc.apply_hadamard_gate(0) 
 
# Execute the circuit and print the results 
result = qc.execute_circuit() 
print(result) 
```

Multi-qubit gates operate on two or more qubits, enabling entanglement and more
complex quantum operations. Some of the most common multi-qubit gates include:

- **CNOT Gate (Controlled-NOT)**: Flips the target qubit if the control qubit is
  in the state

<math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>∣</mi><mn>1</mn><mo>⟩</mo></mrow><annotation>\vert 1\rangle</annotation></semantics></math>

  ∣1⟩.
- **Toffoli Gate (CCNOT)**: A controlled-controlled-NOT gate that flips the
  target qubit if both control qubits are in the state

<math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>∣</mi><mn>1</mn><mo>⟩</mo></mrow><annotation>\vert 1\rangle</annotation></semantics></math>

  ∣1⟩.
- **SWAP Gate**: Exchanges the states of two qubits.

```python
# Initialize the quantum circuit with 2 qubits 
qc.create_empty_circuit(2) 
 
# Apply the Hadamard gate to the first qubit 
qc.apply_hadamard_gate(0) 
 
# Apply the CNOT gate with qubit 0 as control and qubit 1 as target 
qc.apply_cnot_gate(0, 1) 
 
# Execute the circuit and print the results 
result = qc.execute_circuit() 
print(result) 
```

The `qumat` library provides a simple and consistent interface for applying quantum gates. Below are some examples of how to apply different gates using `qumat`.

```python
# Initialize the quantum circuit with 1 qubit 
qc.create_empty_circuit(1) 
 
# Apply an Rx gate with a rotation angle of π/2 
qc.apply_rx_gate(0, 3.14159 / 2) 
 
# Apply an Ry gate with a rotation angle of π/4 
qc.apply_ry_gate(0, 3.14159 / 4) 
 
# Apply an Rz gate with a rotation angle of π 
qc.apply_rz_gate(0, 3.14159) 
 
# Execute the circuit and print the results 
result = qc.execute_circuit() 
print(result) 
```

```python
# Initialize the quantum circuit with 3 qubits 
qc.create_empty_circuit(3) 
 
# Apply the Hadamard gate to the first two qubits 
qc.apply_hadamard_gate(0) 
qc.apply_hadamard_gate(1) 
 
# Apply the Toffoli gate with qubits 0 and 1 as controls and qubit 2 as target 
qc.apply_toffoli_gate(0, 1, 2) 
 
# Execute the circuit and print the results 
result = qc.execute_circuit() 
print(result) 
```

```python
# Initialize the quantum circuit with 2 qubits 
qc.create_empty_circuit(2) 
 
# Apply the Hadamard gate to the first qubit 
qc.apply_hadamard_gate(0) 
 
# Apply the SWAP gate to exchange the states of qubits 0 and 1 
qc.apply_swap_gate(0, 1) 
 
# Execute the circuit and print the results 
result = qc.execute_circuit() 
print(result) 
```

Visualizing quantum circuits can help in understanding the flow of quantum operations. The `qumat` library provides a simple way to draw circuits.

```python
# Initialize the quantum circuit with 2 qubits 
qc.create_empty_circuit(2) 
 
# Apply a Hadamard gate to the first qubit 
qc.apply_hadamard_gate(0) 
 
# Apply a CNOT gate with qubit 0 as control and qubit 1 as target 
qc.apply_cnot_gate(0, 1) 
 
# Draw the circuit 
qc.draw() 
```

This section introduced the fundamental quantum gates and demonstrated how to apply them using the `qumat` library. In the next section, we will explore how to build more complex quantum circuits by combining these gates.

---

<a id="learning-quantum-computing-primer-quantum-circuits"></a>

<!-- source_url: https://mahout.apache.org/docs/learning/quantum-computing-primer/quantum-circuits/ -->

<!-- page_index: 23 -->

# 5. Quantum Circuits

Version: latest

Quantum circuits are the backbone of quantum computing. They are composed of quantum gates that manipulate qubits to perform computations. In this section, we will explore how to build and visualize quantum circuits using the `qumat` library.

A quantum circuit is a sequence of quantum gates applied to qubits. The `qumat` library provides a simple and intuitive way to create and manipulate quantum circuits. Let's start by creating a basic quantum circuit.

To create a quantum circuit with two qubits, we first initialize the circuit and then apply gates to the qubits.

```python
from qumat import QuMat 
 
# Initialize the quantum circuit with 2 qubits 
backend_config = {'backend_name': 'qiskit', 'backend_options': {'simulator_type': 'qasm_simulator', 'shots': 1000}} 
qc = QuMat(backend_config) 
qc.create_empty_circuit(2) 
 
# Apply a Hadamard gate to the first qubit 
qc.apply_hadamard_gate(0) 
 
# Apply a CNOT gate with the first qubit as control and the second qubit as target 
qc.apply_cnot_gate(0, 1) 
 
# Execute the circuit and get the results 
result = qc.execute_circuit() 
print(result) 
```

In this example, we create a quantum circuit with two qubits. We apply a Hadamard gate to the first qubit, which puts it into a superposition state. Then, we apply a CNOT gate, which entangles the two qubits. Finally, we execute the circuit and print the measurement results.

A Bell state is a specific type of entangled quantum state. Let's create a Bell state using `qumat`.

```python
from qumat import QuMat 
 
# Initialize the quantum circuit with 2 qubits 
backend_config = {'backend_name': 'qiskit', 'backend_options': {'simulator_type': 'qasm_simulator', 'shots': 1000}} 
qc = QuMat(backend_config) 
qc.create_empty_circuit(2) 
 
# Apply a Hadamard gate to the first qubit 
qc.apply_hadamard_gate(0) 
 
# Apply a CNOT gate with the first qubit as control and the second qubit as target 
qc.apply_cnot_gate(0, 1) 
 
# Execute the circuit and get the results 
result = qc.execute_circuit() 
print(result) 
```

This code creates a Bell state by applying a Hadamard gate to the first qubit and then a CNOT gate with the first qubit as the control and the second qubit as the target. The result is an entangled state where the measurement outcomes of the two qubits are correlated.

Visualizing quantum circuits is an essential part of understanding and debugging quantum algorithms. The `qumat` library provides a simple way to draw quantum circuits.

To visualize a quantum circuit, you can use the `draw` method provided by `qumat`.

```python
from qumat import QuMat 
 
# Initialize the quantum circuit with 2 qubits 
backend_config = {'backend_name': 'qiskit', 'backend_options': {'simulator_type': 'qasm_simulator', 'shots': 1000}} 
qc = QuMat(backend_config) 
qc.create_empty_circuit(2) 
 
# Apply a Hadamard gate to the first qubit 
qc.apply_hadamard_gate(0) 
 
# Apply a CNOT gate with the first qubit as control and the second qubit as target 
qc.apply_cnot_gate(0, 1) 
 
# Draw the circuit 
qc.draw() 
```

This code returns a textual representation of the quantum circuit, which you can print with `print(qc.draw())` or use programmatically. The visualization shows the sequence of gates applied to the qubits and helps in understanding the structure of the circuit and the flow of quantum information.

Quantum circuits can be made more complex by combining multiple gates. Let's create a more complex circuit that involves multiple gates.

```python
from qumat import QuMat 
 
# Initialize the quantum circuit with 3 qubits 
backend_config = {'backend_name': 'qiskit', 'backend_options': {'simulator_type': 'qasm_simulator', 'shots': 1000}} 
qc = QuMat(backend_config) 
qc.create_empty_circuit(3) 
 
# Apply a Hadamard gate to the first qubit 
qc.apply_hadamard_gate(0) 
 
# Apply a CNOT gate with the first qubit as control and the second qubit as target 
qc.apply_cnot_gate(0, 1) 
 
# Apply a Toffoli gate with the first and second qubits as controls and the third qubit as target 
qc.apply_toffoli_gate(0, 1, 2) 
 
# Execute the circuit and get the results 
result = qc.execute_circuit() 
print(result) 
```

In this example, we create a quantum circuit with three qubits. We apply a Hadamard gate to the first qubit, a CNOT gate with the first qubit as control and the second qubit as target, and a Toffoli gate with the first and second qubits as controls and the third qubit as target. This creates a more complex entangled state.

In this section, we explored how to build and visualize quantum circuits using the `qumat` library. We started with simple circuits and gradually built more complex ones by combining multiple gates. Visualizing these circuits helps in understanding the flow of quantum information and debugging quantum algorithms.

Next, we will dive deeper into quantum entanglement and its applications in quantum computing.

---

<a id="learning-quantum-computing-primer-quantum-entanglement"></a>

<!-- source_url: https://mahout.apache.org/docs/learning/quantum-computing-primer/quantum-entanglement/ -->

<!-- page_index: 24 -->

# 6. Quantum Entanglement

Version: latest

Quantum entanglement is one of the most fascinating and counterintuitive phenomena in quantum mechanics. When two or more qubits become entangled, the state of one qubit becomes directly related to the state of the other, no matter how far apart they are. This means that measuring one qubit instantly determines the state of the other, even if they are light-years apart.

- **Entangled States**: A quantum state of two or more qubits that cannot be described independently of each other.
- **Bell States**: Specific examples of maximally entangled quantum states of two qubits.
- **Non-Locality**: The idea that entangled particles can influence each other instantaneously, regardless of distance.

In this section, we will explore how to create and measure entangled states using the `qumat` library. We will start by creating a simple entangled state known as a Bell state, which is a maximally entangled quantum state of two qubits.

A Bell state can be created by applying a Hadamard gate to the first qubit, followed by a CNOT gate with the first qubit as the control and the second qubit as the target. This results in a state where the two qubits are perfectly correlated.

```python
from qumat import QuMat 
 
# Initialize the quantum circuit with 2 qubits 
backend_config = {'backend_name': 'qiskit', 'backend_options': {'simulator_type': 'qasm_simulator', 'shots': 1000}} 
qc = QuMat(backend_config) 
qc.create_empty_circuit(2) 
 
# Apply a Hadamard gate to the first qubit 
qc.apply_hadamard_gate(0) 
 
# Apply a CNOT gate with the first qubit as control and the second as target 
qc.apply_cnot_gate(0, 1) 
 
# Execute the circuit and measure the results 
result = qc.execute_circuit() 
print(result) 
```

The output will show the measurement results of the two qubits. Since the qubits are entangled, you should observe that the states of the two qubits are perfectly correlated. For example, if the first qubit is measured as `0`, the second qubit will also be `0`, and if the first qubit is `1`, the second qubit will also be `1`.

You can also visualize the circuit to better understand the sequence of operations:

```python
qc.draw() 
```

- **Hadamard Gate**: Creates a superposition of the first qubit.
- **CNOT Gate**: Entangles the two qubits, creating a Bell state.

Once the qubits are entangled, measuring one qubit will instantly determine the state of the other. This is a key feature of quantum entanglement and is used in various quantum algorithms and protocols.

```python
# Execute the circuit and measure the results 
result = qc.execute_circuit() 
print(result) 
```

The output will show the measurement counts for the two qubits. Since the qubits are entangled, the results will show a strong correlation between the states of the two qubits.

Quantum entanglement is a fundamental resource in quantum computing and is used in various applications, including:

- **Quantum Teleportation**: Transmitting quantum information from one location to another.
- **Quantum Cryptography**: Securely sharing encryption keys using entangled qubits.
- **Quantum Error Correction**: Protecting quantum information from errors using entangled states.

Quantum teleportation is a protocol that allows the transfer of quantum information from one qubit to another, even if they are far apart. This is achieved using entanglement and classical communication.

```python
# Example implementation of quantum teleportation 
qc.create_empty_circuit(3) 
 
# Create an entangled pair between qubit 1 and qubit 2 
qc.apply_hadamard_gate(1) 
qc.apply_cnot_gate(1, 2) 
 
# Prepare the qubit to be teleported (qubit 0) 
qc.apply_hadamard_gate(0) 
 
# Perform the teleportation protocol 
qc.apply_cnot_gate(0, 1) 
qc.apply_hadamard_gate(0) 
qc.apply_cnot_gate(1, 2) 
qc.apply_toffoli_gate(0, 1, 2) 
 
# Measure the qubits 
result = qc.execute_circuit() 
print(result) 
```

The output will show the measurement results, demonstrating that the state of qubit 0 has been successfully teleported to qubit 2.

Quantum entanglement is a powerful and essential concept in quantum computing. By understanding how to create and manipulate entangled states using `qumat`, you can begin to explore more advanced quantum algorithms and applications. In the next section, we will delve into quantum algorithms, starting with the Deutsch-Jozsa algorithm.

---

<a id="learning-quantum-computing-primer-quantum-algorithms"></a>

<!-- source_url: https://mahout.apache.org/docs/learning/quantum-computing-primer/quantum-algorithms/ -->

<!-- page_index: 25 -->

# 7. Quantum Algorithms

Version: latest

Quantum algorithms leverage the unique properties of quantum mechanics, such as superposition and entanglement, to solve problems more efficiently than classical algorithms. In this section, we will explore two fundamental quantum algorithms: the **Deutsch-Jozsa Algorithm** and **Grover's Algorithm**. We will also provide implementations using the `qumat` library.

---

The Deutsch-Jozsa algorithm is one of the earliest quantum algorithms that
demonstrates the potential of quantum computing. It solves a specific problem
exponentially faster than any classical algorithm.

Given a function

<math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>f</mi><mo>:</mo><mo>{</mo><mn>0</mn><mo>,</mo><mn>1</mn><msup><mo>}</mo><mi>n</mi></msup><mo>→</mo><mo>{</mo><mn>0</mn><mo>,</mo><mn>1</mn><mo>}</mo></mrow><annotation>f: \{0,1\}^n \rightarrow \{0,1\}</annotation></semantics></math>

f:{0,1}n→{0,1}, determine whether the
function is **constant** (returns the same value for all inputs) or **balanced**
(returns 0 for half of the inputs and 1 for the other half).

The Deutsch-Jozsa algorithm uses quantum parallelism to evaluate the function
over all possible inputs simultaneously. It requires only **one query** to the
function, whereas a classical algorithm would need

<math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><msup><mn>2</mn><mrow><mi>n</mi><mo>−</mo><mn>1</mn></mrow></msup><mo>+</mo><mn>1</mn></mrow><annotation>2^{n-1} + 1</annotation></semantics></math>

2n−1+1 queries in
the worst case.

Here’s how you can implement the Deutsch-Jozsa algorithm using `qumat`:

```python
from qumat import QuMat 
 
# Initialize the quantum circuit with 2 qubits 
backend_config = {'backend_name': 'qiskit', 'backend_options': {'simulator_type': 'qasm_simulator', 'shots': 1000}} 
qc = QuMat(backend_config) 
qc.create_empty_circuit(2) 
 
# Apply Hadamard gates to both qubits 
qc.apply_hadamard_gate(0) 
qc.apply_hadamard_gate(1) 
 
# Apply the oracle (example: constant function) 
# For a constant function, the oracle does nothing 
# For a balanced function, the oracle would flip the second qubit based on the first qubit 
qc.apply_cnot_gate(0, 1) 
 
# Apply Hadamard gate to the first qubit 
qc.apply_hadamard_gate(0) 
 
# Measure the first qubit 
result = qc.execute_circuit() 
print(result) 
```

- If the function is **constant**, the first qubit will always measure as `0`.
- If the function is **balanced**, the first qubit will measure as `1` with high probability.

---

Grover's algorithm is a quantum search algorithm that can search an unsorted
database of

<math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>N</mi></mrow><annotation>N</annotation></semantics></math>

N items in

<math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>O</mi><mo>(</mo><msqrt><mi>N</mi></msqrt><mo>)</mo></mrow><annotation>O(\sqrt{N})</annotation></semantics></math>

O(N

<svg height="1.08em" preserveaspectratio="xMinYMin slice" viewbox="0 0 400000 1080" width="400em" xmlns="http://www.w3.org/2000/svg"><path></path></svg>

) time, compared to

<math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>O</mi><mo>(</mo><mi>N</mi><mo>)</mo></mrow><annotation>O(N)</annotation></semantics></math>

O(N) for
classical algorithms.

Given an unsorted database of

<math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>N</mi></mrow><annotation>N</annotation></semantics></math>

N items, find a specific item (marked by an oracle) with as few queries as possible.

Grover's algorithm uses amplitude amplification to increase the probability of measuring the marked item. It consists of two main steps:

1. **Oracle**: Marks the desired item.
2. **Diffusion Operator**: Amplifies the probability of the marked item.

Here’s a simplified implementation of Grover's algorithm using `qumat`:

```python
from qumat import QuMat 
 
# Initialize the quantum circuit with 3 qubits 
backend_config = {'backend_name': 'qiskit', 'backend_options': {'simulator_type': 'qasm_simulator', 'shots': 1000}} 
qc = QuMat(backend_config) 
qc.create_empty_circuit(3) 
 
# Apply Hadamard gates to all qubits 
qc.apply_hadamard_gate(0) 
qc.apply_hadamard_gate(1) 
qc.apply_hadamard_gate(2) 
 
# Apply the oracle (example: marks the state |110>) 
qc.apply_pauli_x_gate(0) 
qc.apply_pauli_x_gate(1) 
qc.apply_toffoli_gate(0, 1, 2) 
qc.apply_pauli_x_gate(0) 
qc.apply_pauli_x_gate(1) 
 
# Apply the diffusion operator (Grover's diffusion) 
qc.apply_hadamard_gate(0) 
qc.apply_hadamard_gate(1) 
qc.apply_hadamard_gate(2) 
qc.apply_pauli_x_gate(0) 
qc.apply_pauli_x_gate(1) 
qc.apply_pauli_x_gate(2) 
qc.apply_toffoli_gate(0, 1, 2) 
qc.apply_pauli_x_gate(0) 
qc.apply_pauli_x_gate(1) 
qc.apply_pauli_x_gate(2) 
qc.apply_hadamard_gate(0) 
qc.apply_hadamard_gate(1) 
qc.apply_hadamard_gate(2) 
 
# Measure the qubits 
result = qc.execute_circuit() 
print(result) 
```

- The oracle marks the desired state (e.g.,

<math xmlns="http://www.w3.org/1998/Math/MathML"><semantics><mrow><mi>∣</mi><mn>110</mn><mo>⟩</mo></mrow><annotation>\vert 110\rangle</annotation></semantics></math>

  ∣110⟩).
- The diffusion operator amplifies the probability of measuring the marked state.
- After running the algorithm, the marked state will have a higher probability of being measured.

---

Quantum algorithms like Deutsch-Jozsa and Grover's are foundational to many advanced quantum computing applications, including:

- **Cryptography**: Breaking classical encryption schemes.
- **Optimization**: Solving complex optimization problems.
- **Machine Learning**: Speeding up training and inference in quantum machine learning models.

By mastering these algorithms with `qumat`, you can begin to explore the vast potential of quantum computing in real-world applications.

---

This section provides a hands-on introduction to quantum algorithms using `qumat`. Experiment with the provided code examples to deepen your understanding of quantum computing principles!

---

<a id="learning-quantum-computing-primer-quantum-error-correction"></a>

<!-- source_url: https://mahout.apache.org/docs/learning/quantum-computing-primer/quantum-error-correction/ -->

<!-- page_index: 26 -->

# 8. Quantum Error Correction

Version: latest

Quantum error correction is a crucial aspect of quantum computing, as quantum systems are inherently prone to errors due to decoherence and noise. This section introduces the basics of quantum error correction and demonstrates how to implement simple error correction circuits using the `qumat` library.

Quantum bits (qubits) are highly susceptible to errors caused by environmental noise, imperfect gate operations, and other quantum phenomena. Unlike classical bits, which can be easily corrected using redundancy, qubits require more sophisticated error correction techniques to maintain their quantum states.

- **Qubit Errors**: Errors in quantum computing can be classified into bit-flip errors (X gate), phase-flip errors (Z gate), and combinations thereof.
- **Error Correction Codes**: Quantum error correction codes, such as the Shor code and the Steane code, are designed to detect and correct these errors by encoding a single logical qubit into multiple physical qubits.

The following example demonstrates a simple bit-flip error correction circuit using `qumat`. The circuit encodes one logical qubit into three physical qubits and corrects a single bit-flip error.

```python
from qumat import QuMat 
 
# Initialize the quantum circuit with 3 qubits 
backend_config = {'backend_name': 'qiskit', 'backend_options': {'simulator_type': 'qasm_simulator', 'shots': 1000}} 
qc = QuMat(backend_config) 
qc.create_empty_circuit(3) 
 
# Encode the logical qubit into 3 physical qubits 
qc.apply_hadamard_gate(0) 
qc.apply_cnot_gate(0, 1) 
qc.apply_cnot_gate(0, 2) 
 
# Simulate a bit-flip error on qubit 1 
qc.apply_pauli_x_gate(1) 
 
# Error correction steps 
qc.apply_cnot_gate(0, 1) 
qc.apply_cnot_gate(0, 2) 
qc.apply_toffoli_gate(1, 2, 0) 
 
# Execute the circuit and print the results 
result = qc.execute_circuit() 
print(result) 
```

1. **Encoding**: The logical qubit (qubit 0) is encoded into three physical qubits using a Hadamard gate and two CNOT gates.
2. **Error Simulation**: A bit-flip error is simulated by applying an X gate to qubit 1.
3. **Error Correction**: The error is detected and corrected using additional CNOT gates and a Toffoli gate.

You can visualize the error correction circuit using the `draw` method:

```python
qc.draw() 
```

This will display the circuit diagram, showing the encoding, error simulation, and correction steps.

The Shor code is a more advanced error correction code that can correct both bit-flip and phase-flip errors. It encodes one logical qubit into nine physical qubits.

The Steane code is another error correction code that can correct arbitrary single-qubit errors. It encodes one logical qubit into seven physical qubits.

While the above example demonstrates a simple bit-flip error correction, `qumat` can also be used to implement more advanced codes like the Shor code and Steane code. These implementations require more qubits and gates but follow similar principles of encoding, error detection, and correction.

Quantum error correction is essential for building reliable quantum computers. By using `qumat`, you can implement and experiment with various error correction techniques, from simple bit-flip correction to more advanced codes like the Shor and Steane codes. As quantum hardware continues to improve, these techniques will play a critical role in realizing the full potential of quantum computing.

---

This section provides a foundational understanding of quantum error correction and demonstrates how to implement basic error correction circuits using `qumat`. For further exploration, consider experimenting with more complex error correction codes and their applications in quantum computing.

---

<a id="learning-quantum-computing-primer-applications"></a>

<!-- source_url: https://mahout.apache.org/docs/learning/quantum-computing-primer/applications/ -->

<!-- page_index: 27 -->

# 9. Applications of Quantum Computing

Version: latest

Quantum computing holds the potential to revolutionize various fields by solving problems that are currently intractable for classical computers. In this section, we will explore some of the key applications of quantum computing and demonstrate how to implement them using the `qumat` library.

Quantum cryptography leverages the principles of quantum mechanics to create secure communication channels. One of the most well-known applications is Quantum Key Distribution (QKD), which allows two parties to generate a shared, secret key that is secure against eavesdropping.

Below is a simplified example of how to implement a basic QKD protocol using `qumat`. This example demonstrates the generation of a shared key between two parties, Alice and Bob.

```python
from qumat import QuMat 
 
# Initialize the quantum circuit 
backend_config = {'backend_name': 'qiskit', 'backend_options': {'simulator_type': 'qasm_simulator', 'shots': 1000}} 
qc = QuMat(backend_config) 
qc.create_empty_circuit(2) 
 
# Alice prepares her qubits 
qc.apply_hadamard_gate(0) 
qc.apply_cnot_gate(0, 1) 
 
# Alice sends the second qubit to Bob 
# Bob measures the qubit in the same basis as Alice 
qc.apply_hadamard_gate(1) 
 
# Execute the circuit and get the results 
result = qc.execute_circuit() 
print("Shared key:", result) 
```

Quantum simulation involves using a quantum computer to simulate quantum systems, which is particularly useful in fields like chemistry, material science, and physics. Quantum computers can efficiently simulate the behavior of molecules and materials at the quantum level.

In this example, we simulate a simple quantum system, such as a hydrogen molecule, using `qumat`. The goal is to find the ground state energy of the molecule.

```python
from qumat import QuMat 
 
# Initialize the quantum circuit 
backend_config = {'backend_name': 'qiskit', 'backend_options': {'simulator_type': 'statevector_simulator', 'shots': 1}} 
qc = QuMat(backend_config) 
qc.create_empty_circuit(2) 
 
# Apply gates to simulate the hydrogen molecule 
qc.apply_hadamard_gate(0) 
qc.apply_cnot_gate(0, 1) 
qc.apply_rz_gate(1, 0.5)  # Example of a parameterized gate 
 
# Execute the circuit and get the final state vector 
state_vector = qc.get_final_state_vector() 
print("Final state vector:", state_vector) 
```

Quantum machine learning (QML) is an emerging field that combines quantum computing with classical machine learning techniques. Quantum computers can potentially speed up certain machine learning algorithms, such as classification and clustering.

In this example, we implement a basic quantum classifier using `qumat`. The classifier is trained to distinguish between two classes based on a simple dataset.

```python
from qumat import QuMat 
 
# Initialize the quantum circuit 
backend_config = {'backend_name': 'qiskit', 'backend_options': {'simulator_type': 'qasm_simulator', 'shots': 1000}} 
qc = QuMat(backend_config) 
qc.create_empty_circuit(2) 
 
# Apply gates to create a quantum classifier 
qc.apply_hadamard_gate(0) 
qc.apply_cnot_gate(0, 1) 
qc.apply_ry_gate(1, 0.3)  # Example of a parameterized gate 
 
# Execute the circuit and get the results 
result = qc.execute_circuit() 
print("Classification result:", result) 
```

Quantum optimization involves using quantum algorithms to solve optimization problems more efficiently than classical methods. One of the most well-known quantum optimization algorithms is the Quantum Approximate Optimization Algorithm (QAOA).

In this example, we use `qumat` to implement a simple QAOA circuit to solve a basic optimization problem.

```python
from qumat import QuMat 
 
# Initialize the quantum circuit 
backend_config = {'backend_name': 'qiskit', 'backend_options': {'simulator_type': 'qasm_simulator', 'shots': 1000}} 
qc = QuMat(backend_config) 
qc.create_empty_circuit(2) 
 
# Apply gates to implement QAOA 
qc.apply_hadamard_gate(0) 
qc.apply_hadamard_gate(1) 
qc.apply_rx_gate(0, 0.5)  # Example of a parameterized gate 
qc.apply_ry_gate(1, 0.5)  # Example of a parameterized gate 
 
# Execute the circuit and get the results 
result = qc.execute_circuit() 
print("Optimization result:", result) 
```

Quantum chemistry involves the application of quantum mechanics to chemical systems. Quantum computers can simulate molecular structures and reactions more accurately than classical computers, which is crucial for drug discovery and material design.

In this example, we use `qumat` to simulate a simple chemical reaction, such as the formation of a hydrogen molecule from two hydrogen atoms.

```python
from qumat import QuMat 
 
# Initialize the quantum circuit 
backend_config = {'backend_name': 'qiskit', 'backend_options': {'simulator_type': 'statevector_simulator', 'shots': 1}} 
qc = QuMat(backend_config) 
qc.create_empty_circuit(2) 
 
# Apply gates to simulate the chemical reaction 
qc.apply_hadamard_gate(0) 
qc.apply_cnot_gate(0, 1) 
qc.apply_rz_gate(1, 0.5)  # Example of a parameterized gate 
 
# Execute the circuit and get the final state vector 
state_vector = qc.get_final_state_vector() 
print("Final state vector:", state_vector) 
```

Quantum finance involves the application of quantum computing to financial problems, such as portfolio optimization, risk analysis, and option pricing. Quantum algorithms can potentially provide faster and more accurate solutions to these problems.

In this example, we use `qumat` to implement a simple quantum algorithm for portfolio optimization.

```python
from qumat import QuMat 
 
# Initialize the quantum circuit 
backend_config = {'backend_name': 'qiskit', 'backend_options': {'simulator_type': 'qasm_simulator', 'shots': 1000}} 
qc = QuMat(backend_config) 
qc.create_empty_circuit(2) 
 
# Apply gates to implement portfolio optimization 
qc.apply_hadamard_gate(0) 
qc.apply_cnot_gate(0, 1) 
qc.apply_ry_gate(1, 0.5)  # Example of a parameterized gate 
 
# Execute the circuit and get the results 
result = qc.execute_circuit() 
print("Portfolio optimization result:", result) 
```

Quantum artificial intelligence (QAI) combines quantum computing with artificial intelligence to create more powerful AI models. Quantum computers can potentially speed up training and inference processes in AI.

In this example, we use `qumat` to implement a simple quantum neural network (QNN) for a basic classification task.

```python
from qumat import QuMat 
 
# Initialize the quantum circuit 
backend_config = {'backend_name': 'qiskit', 'backend_options': {'simulator_type': 'qasm_simulator', 'shots': 1000}} 
qc = QuMat(backend_config) 
qc.create_empty_circuit(2) 
 
# Apply gates to implement a quantum neural network 
qc.apply_hadamard_gate(0) 
qc.apply_cnot_gate(0, 1) 
qc.apply_ry_gate(1, 0.5)  # Example of a parameterized gate 
 
# Execute the circuit and get the results 
result = qc.execute_circuit() 
print("QNN classification result:", result) 
```

Quantum sensing involves using quantum systems to measure physical quantities with high precision. Quantum sensors can potentially outperform classical sensors in terms of sensitivity and accuracy.

In this example, we use `qumat` to implement a simple quantum sensor for measuring a physical quantity, such as magnetic field strength.

```python
from qumat import QuMat 
 
# Initialize the quantum circuit 
backend_config = {'backend_name': 'qiskit', 'backend_options': {'simulator_type': 'statevector_simulator', 'shots': 1}} 
qc = QuMat(backend_config) 
qc.create_empty_circuit(2) 
 
# Apply gates to implement a quantum sensor 
qc.apply_hadamard_gate(0) 
qc.apply_cnot_gate(0, 1) 
qc.apply_rz_gate(1, 0.5)  # Example of a parameterized gate 
 
# Execute the circuit and get the final state vector 
state_vector = qc.get_final_state_vector() 
print("Quantum sensor measurement:", state_vector) 
```

Quantum communication involves the transmission of information using quantum states. Quantum communication protocols, such as quantum teleportation, can provide secure and efficient communication channels.

In this example, we use `qumat` to implement a quantum teleportation protocol, which allows the transfer of quantum information from one qubit to another.

```python
from qumat import QuMat 
 
# Initialize the quantum circuit 
backend_config = {'backend_name': 'qiskit', 'backend_options': {'simulator_type': 'statevector_simulator', 'shots': 1}} 
qc = QuMat(backend_config) 
qc.create_empty_circuit(3) 
 
# Apply gates to implement quantum teleportation 
qc.apply_hadamard_gate(0) 
qc.apply_cnot_gate(0, 1) 
qc.apply_cnot_gate(1, 2) 
 
# Execute the circuit and get the final state vector 
state_vector = qc.get_final_state_vector() 
print("Quantum teleportation result:", state_vector) 
```

Quantum error correction is essential for building reliable quantum computers. Quantum error correction codes can detect and correct errors that occur during quantum computation.

In this example, we use `qumat` to implement a simple quantum error correction code, such as the bit-flip code.

```python
from qumat import QuMat 
 
# Initialize the quantum circuit 
backend_config = {'backend_name': 'qiskit', 'backend_options': {'simulator_type': 'qasm_simulator', 'shots': 1000}} 
qc = QuMat(backend_config) 
qc.create_empty_circuit(3) 
 
# Apply gates to implement the bit-flip code 
qc.apply_hadamard_gate(0) 
qc.apply_cnot_gate(0, 1) 
qc.apply_cnot_gate(0, 2) 
 
# Simulate an error (e.g., bit flip on qubit 1) 
qc.apply_pauli_x_gate(1) 
 
# Error correction steps 
qc.apply_cnot_gate(0, 1) 
qc.apply_cnot_gate(0, 2) 
qc.apply_toffoli_gate(1, 2, 0) 
 
# Execute the circuit and get the results 
result = qc.execute_circuit() 
print("Error correction result:", result) 
```

Quantum games are games that incorporate quantum mechanics into their rules or strategies. These games can be used to explore quantum phenomena in a fun and interactive way.

In this example, we use `qumat` to implement a simple quantum game, such as the quantum version of the classic game "Rock-Paper-Scissors."

```python
from qumat import QuMat 
 
# Initialize the quantum circuit 
backend_config = {'backend_name': 'qiskit', 'backend_options': {'simulator_type': 'qasm_simulator', 'shots': 1000}} 
qc = QuMat(backend_config) 
qc.create_empty_circuit(2) 
 
# Apply gates to implement the quantum game 
qc.apply_hadamard_gate(0) 
qc.apply_cnot_gate(0, 1) 
 
# Execute the circuit and get the results 
result = qc.execute_circuit() 
print("Quantum game result:", result) 
```

Quantum random number generation (QRNG) uses the inherent randomness of quantum mechanics to generate truly random numbers. These numbers are useful in cryptography, simulations, and other applications.

In this example, we use `qumat` to implement a simple quantum random number generator.

```python
from qumat import QuMat 
 
# Initialize the quantum circuit 
backend_config = {'backend_name': 'qiskit', 'backend_options': {'simulator_type': 'qasm_simulator', 'shots': 1000}} 
qc = QuMat(backend_config) 
qc.create_empty_circuit(1) 
 
# Apply a Hadamard gate to generate a random bit 
qc.apply_hadamard_gate(0) 
 
# Execute the circuit and get the results 
result = qc.execute_circuit() 
print("Random number:", result) 
```

Quantum image processing involves using quantum algorithms to process and analyze images. Quantum computers can potentially provide faster and more efficient image processing techniques.

In this example, we use `qumat` to implement a simple quantum image processing algorithm, such as edge detection.

```python
from qumat import QuMat 
 
# Initialize the quantum circuit 
backend_config = {'backend_name': 'qiskit', 'backend_options': {'simulator_type': 'qasm_simulator', 'shots': 1000}} 
qc = QuMat(backend_config) 
qc.create_empty_circuit(2) 
 
# Apply gates to implement edge detection 
qc.apply_hadamard_gate(0) 
qc.apply_cnot_gate(0, 1) 
 
# Execute the circuit and get the results 
result = qc.execute_circuit() 
print("Edge detection result:", result) 
```

Quantum natural language processing (QNLP) involves using quantum algorithms to process and analyze natural language data. Quantum computers can potentially provide faster and more efficient NLP techniques.

In this example, we use `qumat` to implement a simple quantum NLP algorithm, such as text classification.

```python
from qumat import QuMat 
 
# Initialize the quantum circuit 
backend_config = {'backend_name': 'qiskit', 'backend_options': {'simulator_type': 'qasm_simulator', 'shots': 1000}} 
qc = QuMat(backend_config) 
qc.create_empty_circuit(2) 
 
# Apply gates to implement text classification 
qc.apply_hadamard_gate(0) 
qc.apply_cnot_gate(0, 1) 
 
# Execute the circuit and get the results 
result = qc.execute_circuit() 
print("Text classification result:", result) 
```

Quantum robotics involves using quantum computing to enhance the capabilities of robots. Quantum algorithms can potentially improve robot perception, decision-making, and control.

In this example, we use `qumat` to implement a simple quantum robotics algorithm, such as path planning.

```python
from qumat import QuMat 
 
# Initialize the quantum circuit 
backend_config = {'backend_name': 'qiskit', 'backend_options': {'simulator_type': 'qasm_simulator', 'shots': 1000}} 
qc = QuMat(backend_config) 
qc.create_empty_circuit(2) 
 
# Apply gates to implement path planning 
qc.apply_hadamard_gate(0) 
qc.apply_cnot_gate(0, 1) 
 
# Execute the circuit and get the results 
result = qc.execute_circuit() 
print("Path planning result:", result) 
```

The quantum internet is a proposed network that uses quantum communication protocols to enable secure and efficient communication between quantum devices.

In this example, we use `qumat` to implement a simple quantum internet protocol, such as quantum key distribution.

```python
from qumat import QuMat 
 
# Initialize the quantum circuit 
backend_config = {'backend_name': 'qiskit', 'backend_options': {'simulator_type': 'qasm_simulator', 'shots': 1000}} 
qc = QuMat(backend_config) 
qc.create_empty_circuit(2) 
 
# Apply gates to implement quantum key distribution 
qc.apply_hadamard_gate(0) 
qc.apply_cnot_gate(0, 1) 
 
# Execute the circuit and get the results 
result = qc.execute_circuit() 
print("Quantum key distribution result:", result) 
```

Quantum biology explores the role of quantum mechanics in biological processes. Quantum computers can potentially simulate biological systems more accurately than classical computers.

In this example, we use `qumat` to simulate a simple biological process, such as photosynthesis.

```python
from qumat import QuMat 
 
# Initialize the quantum circuit 
backend_config = {'backend_name': 'qiskit', 'backend_options': {'simulator_type': 'statevector_simulator', 'shots': 1}} 
qc = QuMat(backend_config) 
qc.create_empty_circuit(2) 
 
# Apply gates to simulate photosynthesis 
qc.apply_hadamard_gate(0) 
qc.apply_cnot_gate(0, 1) 
 
# Execute the circuit and get the final state vector 
state_vector = qc.get_final_state_vector() 
print("Photosynthesis simulation result:", state_vector) 
```

Quantum materials science involves using quantum computing to study and design new materials with unique properties. Quantum computers can potentially simulate material properties more accurately than classical computers.

In this example, we use `qumat` to simulate a simple material, such as graphene.

```python
from qumat import QuMat 
 
# Initialize the quantum circuit 
backend_config = {'backend_name': 'qiskit', 'backend_options': {'simulator_type': 'statevector_simulator', 'shots': 1}} 
qc = QuMat(backend_config) 
qc.create_empty_circuit(2) 
 
# Apply gates to simulate graphene 
qc.apply_hadamard_gate(0 
```

---

<a id="learning-quantum-computing-primer-advanced-topics"></a>

<!-- source_url: https://mahout.apache.org/docs/learning/quantum-computing-primer/advanced-topics/ -->

<!-- page_index: 28 -->

# 10. Advanced Topics

Version: latest

In this section, we will explore some advanced topics in quantum computing, focusing on how to implement them using the `qumat` library. These topics include the Quantum Fourier Transform, Quantum Phase Estimation, and Quantum Annealing. Each topic will be explained with a brief overview, followed by a practical example using `qumat`.

The Quantum Fourier Transform (QFT) is a quantum analogue of the classical Fourier Transform. It is a key component in many quantum algorithms, including Shor's algorithm for integer factorization. The QFT transforms a quantum state into its frequency domain representation.

Below is an example of how to implement the QFT using `qumat`. This example assumes a 3-qubit system.

```python
from qumat import QuMat 
 
# Initialize the quantum circuit 
backend_config = {'backend_name': 'qiskit', 'backend_options': {'simulator_type': 'qasm_simulator', 'shots': 1000}} 
qc = QuMat(backend_config) 
qc.create_empty_circuit(3) 
 
# Apply the Quantum Fourier Transform 
def apply_qft(qc, n_qubits): 
    for qubit in range(n_qubits): 
        qc.apply_hadamard_gate(qubit) 
        for next_qubit in range(qubit + 1, n_qubits): 
            angle = 2 * 3.14159 / (2 ** (next_qubit - qubit + 1)) 
            qc.apply_cu_gate(next_qubit, qubit, angle) 
 
apply_qft(qc, 3) 
 
# Execute the circuit and print the results 
result = qc.execute_circuit() 
print(result) 
```

Quantum Phase Estimation (QPE) is a quantum algorithm used to estimate the phase (or eigenvalue) of an eigenvector of a unitary operator. It is a crucial subroutine in many quantum algorithms, including Shor's algorithm and quantum simulations.

Below is an example of how to implement QPE using `qumat`. This example assumes a 3-qubit system and a simple unitary operator.

```python
from qumat import QuMat 
 
# Initialize the quantum circuit 
backend_config = {'backend_name': 'qiskit', 'backend_options': {'simulator_type': 'qasm_simulator', 'shots': 1000}} 
qc = QuMat(backend_config) 
qc.create_empty_circuit(3) 
 
# Apply the Quantum Phase Estimation 
def apply_qpe(qc, n_qubits): 
    for qubit in range(n_qubits): 
        qc.apply_hadamard_gate(qubit) 
        # Apply controlled unitary operations (simplified example) 
        qc.apply_cu_gate(1, 0, 3.14159 / 2) 
        qc.apply_cu_gate(2, 1, 3.14159 / 4) 
# Inverse QFT 
apply_qft(qc, n_qubits) 
 
apply_qpe(qc, 3) 
 
# Execute the circuit and print the results 
result = qc.execute_circuit() 
print(result) 
```

Quantum Annealing is a quantum computing technique used to solve optimization problems. It leverages quantum tunneling to find the global minimum of a given objective function. Quantum Annealing is particularly useful for problems like the Traveling Salesman Problem and other combinatorial optimization challenges.

Below is an example of how to implement a simple quantum annealing process using `qumat`. This example assumes a 2-qubit system and a simple objective function.

```python
from qumat import QuMat 
 
# Initialize the quantum circuit 
backend_config = {'backend_name': 'qiskit', 'backend_options': {'simulator_type': 'qasm_simulator', 'shots': 1000}} 
qc = QuMat(backend_config) 
qc.create_empty_circuit(2) 
 
# Apply the Quantum Annealing process 
def apply_quantum_annealing(qc, n_qubits): 
    for qubit in range(n_qubits): 
        qc.apply_hadamard_gate(qubit) 
        # Apply a simple Hamiltonian (simplified example) 
        qc.apply_rx_gate(0, 3.14159 / 2) 
        qc.apply_ry_gate(1, 3.14159 / 2) 
    # Measure the qubits 
    qc.execute_circuit() 
 
apply_quantum_annealing(qc, 2) 
 
# Execute the circuit and print the results 
result = qc.execute_circuit() 
print(result) 
```

In this section, we explored advanced topics in quantum computing, including the Quantum Fourier Transform, Quantum Phase Estimation, and Quantum Annealing. Each topic was accompanied by a practical example using the `qumat` library. These advanced techniques are essential for understanding and implementing more complex quantum algorithms and applications.

For further reading, consider exploring the official documentation of `qumat` and other quantum computing resources to deepen your understanding of these topics.

---

<a id="learning-papers"></a>

<!-- source_url: https://mahout.apache.org/docs/learning/papers/ -->

<!-- page_index: 29 -->

# Research Papers

Version: latest

Research papers and publications related to Qumat and quantum computing.

- [An Efficient Quantum Factoring Algorithm](#learning-papers-an-efficient-quantum-factoring-algorithm)
- [Quantum Kernel Estimation With Neutral Atoms For Supervised Classification](#learning-papers-quantum-kernel-estimation-with-neutral-atoms-for-supervised-classification)
- [Quantum Machine Learning Beyond Kernel Methods](#learning-papers-quantum-machine-learning-beyond-kernel-methods)
- [Unleashing the Potential of LLMs for Quantum Computing](#learning-papers-unleashing-the-potential-of-llms-for-quantum-computing)

---

<a id="learning-papers-an-efficient-quantum-factoring-algorithm"></a>

<!-- source_url: https://mahout.apache.org/docs/learning/papers/An-Efficient-Quantum-Factoring-Algorithm/ -->

<!-- page_index: 30 -->

# Summary of 'An Efficient Quantum Factoring Algorithm'

Version: latest

Author: Oded Regev

[Original Paper](https://arxiv.org/abs/2308.06572)

The paper presents an efficient quantum factoring algorithm that can be used to
factorize n-bit integers. The algorithm involves running a quantum circuit with
˜O(n3/2) gates for √n + 4 times, and then using a polynomial-time classical
post-processing step. The correctness of the algorithm is based on a
number-theoretic assumption similar to those used in subexponential classical
factorization algorithms. The author demonstrates that quantum circuits of size
˜O(n3/2) are sufficient for factoring integers, which is an improvement over
previous algorithms that required larger circuit sizes. The number of qubits in
the quantum circuit is O(n3/2), which is higher than the qubit requirement in
optimized implementations of Shor's algorithm. However, the depth of the quantum
circuit is smaller than Shor's algorithm, making it more feasible for
implementation. The paper also discusses the potential implications of the
algorithm in practice. It is highlighted that the analysis is asymptotic and the
algorithm may not be efficient for small values of n. The algorithm may benefit
from optimizations in fast integer multiplication and the use of smaller qubit
counts, similar to optimizations used in Shor's algorithm. However, it is
currently unclear if these optimizations can be applied to the proposed
algorithm. The author concludes by stating that the algorithm provides an
improvement over Shor's algorithm in terms of circuit size. However, it remains
to be seen if the algorithm can be practically implemented and if it can provide
an improvement over Shor's algorithm for small values of n. The analysis in the
paper is based on asymptotics, and it is unclear if hidden constants in the
algorithm would make it inefficient for small values of n. In summary, the paper
presents an efficient quantum factoring algorithm that uses a quantum circuit
with ˜O(n3/2) gates and a classical post-processing step. The algorithm provides
an improvement over previous algorithms in terms of circuit size, but its
practicality and potential improvements for small values of n remain to be seen.

---

<a id="learning-papers-quantum-kernel-estimation-with-neutral-atoms-for-supervised-classification"></a>

<!-- source_url: https://mahout.apache.org/docs/learning/papers/Quantum-Kernel-Estimation-With-Neutral-Atoms-For-Supervised-Classification/ -->

<!-- page_index: 31 -->

# Summary of 'Quantum Kernel Estimation With Neutral Atoms For Supervised Classification: A Gate-Based Approach'

Version: latest

Author: Marco Russo, Edoardo Giusto, Bartolomeo Montrucchio

[Original Paper](https://arxiv.org/abs/2307.15840)

In this paper, the authors propose a gate-based approach to quantum kernel
estimation (QKE) for supervised classification using neutral atom quantum
computers. QKE is a technique that leverages the power of quantum computing to
estimate a kernel function that is difficult to compute classically. The
estimated kernel is then used by a classical computer to train a support vector
machine (SVM) for classification tasks. The authors focus on neutral atom
quantum computers because they allow for more freedom in arranging the atoms, which is essential for implementing the necessary gates for QKE. They present a
general method for deriving 1-qubit and 2-qubit gates from laser pulses, which
are then used to construct a parameterized sequence for feature mapping on 3
qubits. They show that this approach can be extended to N qubits, taking
advantage of the more flexible arrangement of atoms in neutral atom devices. The
experimental setup involves simulating the Pasqal Chadoq2 device, which allows
for planar arrangement of atoms. The authors generate a dataset of 40 training
samples and 20 test samples with 3 features and a separation gap of 0.1. They
use the Qiskit library to implement the feature mapping circuit and generate the
sequences of pulses for QKE. The training and testing of the SVM are performed
on a classical computer using the estimated kernel matrices. The results show
that the proposed approach achieves a high accuracy of 75% on the test set, despite the small size of the dataset and the low separation. The authors
compare the performance to a classical SVM with a radial basis function kernel
and find that the quantum approach outperforms the classical approach. The
authors discuss the advantages of using neutral atom quantum computers for QKE.
The arbitrary arrangement of atoms allows for more direct connections between
qubits, reducing the depth of the circuit and reducing the impact of
decoherence. They also highlight the exponential computational advantage of
quantum feature kernels over classical kernel computation methods for
high-dimensional feature spaces. Overall, the paper presents a gate-based
approach to QKE using neutral atom quantum computers. The experimental results
demonstrate the potential of this approach for supervised classification tasks
and highlight the advantages of neutral atom devices for implementing QKE
circuits. The paper provides a foundation for future research in the field of
quantum machine learning and quantum computing.

---

<a id="learning-papers-quantum-machine-learning-beyond-kernel-methods"></a>

<!-- source_url: https://mahout.apache.org/docs/learning/papers/Quantum-machine-learning-beyond-kernel-methods/ -->

<!-- page_index: 32 -->

# Summary of 'Quantum machine learning beyond kernel methods'

Version: latest

Author: Soﬁene Jerbi, Lukas J. Fiderer, Hendrik Poulsen Nautrup, Jonas M. Kübler, Hans J. Briegel, Vedran Dunjko

Journal: Nature Communications

[Original Paper](https://www.nature.com/articles/s41467-023-36159-y)

This article presents a study on quantum machine learning models and their
comparison to classical models. The authors propose a framework that captures
all standard models based on parametrized quantum circuits, focusing on linear
quantum models. They analyze the resource requirements and learning performance
guarantees of these models, particularly comparing explicit and implicit models.
They show that implicit models can achieve a lower training loss but may suffer
from poor generalization performance. They also show that data re-uploading
models, a type of explicit model, can be more general than both explicit and
implicit models. The authors further investigate the advantages of explicit
models by testing their performance on a learning task involving
quantum-generated data. They find that explicit models can outperform both
implicit models and classical models on this task, highlighting the potential
learning advantage of explicit quantum models. The study provides insights into
the capabilities and limitations of different quantum machine learning models, and it contributes to understanding the possible advantages of quantum models in
practical applications.

---

<a id="learning-papers-unleashing-the-potential-of-llms-for-quantum-computing"></a>

<!-- source_url: https://mahout.apache.org/docs/learning/papers/Unleashing-the-Potential-of-LLMs-for-Quantum-Computing/ -->

<!-- page_index: 33 -->

# Summary of 'Unleashing the Potential of LLMs for Quantum Computing: A Study in Quantum Architecture Design'

Version: latest

Author: Zhiding Liang, Jinglei Cheng, Rui Yang, Hang Ren, Zhixin Song, Di Wu, Xuehai Qian, Tongyang Li, Yiyu Shi

[Original Paper](https://arxiv.org/abs/2307.08191)

This paper discusses the potential of large language models (LLMs), specifically
generative pretrained transformers (GPTs), in the field of quantum computing.
The authors propose a Quantum GPT-Guided Architecture Search (QGAS) model that
utilizes GPT-4 to recommend high-quality ansatz architectures for variational
quantum algorithms (VQAs). The ansatz architecture is a crucial component of
quantum computing and determines the efficiency and accuracy of quantum
algorithms. The authors conduct experiments using a series of application
benchmarks, including portfolio optimization, the MaxCut problem, the Traveling
Salesman Problem (TSP), and the estimation of molecule ground state energy for
Lithium Hydride (LiH) and Water (H2O). They compare the performance of the
ansatz architectures generated by QGAS with existing ansatzes and
state-of-the-art ansatz architecture search methods. The results show that QGAS
outperforms other ansatz architectures in some benchmark applications, demonstrating the potential of LLMs in quantum architecture design. The authors
highlight the importance of human feedback in guiding the performance of GPT-4.
Human experts provide specific guidance and feedback to improve the search
strategies and evaluate the generated ansatz architectures. The iterative
feedback loop between human experts and GPT-4 leads to better performance and
optimization of the quantum circuits. The paper also discusses the limitations
of GPT in the field of quantum computing. GPT is not a general artificial
intelligence and cannot think dynamically about quantum physics or make accurate
predictions about scientific phenomena in quantum experiments. It also relies on
large-scale data models, which may contain biased or misleading information
about quantum computing. The authors suggest future directions for the
integration of LLMs, such as GPT, in quantum computing. They propose that GPT
can be used to design and optimize fault-tolerant quantum algorithms and assist
in the calibration of quantum hardware. They also envision GPT playing a role in
the simulation of quantum computers and providing agile validation of
algorithmic innovations. In conclusion, this paper highlights the potential of
LLMs, specifically GPT, in the field of quantum computing. The QGAS model
demonstrates the effectiveness of using GPT-4 to generate high-performance
ansatz architectures for quantum algorithms. The integration of human feedback
and the power of GPT-4 provides a promising avenue for advancing quantum
architecture design and optimization. However, the limitations of GPT and the
challenges of applying LLMs to quantum computing should be considered. The
authors suggest further research and development to leverage the capabilities of
GPT and address the limitations to fully harness the potential of LLMs in
quantum computing.

---

<a id="community"></a>

<!-- source_url: https://mahout.apache.org/docs/community/ -->

<!-- page_index: 34 -->

# Community Overview

Version: latest

The Apache Mahout community consists of developers, users, data scientists, researchers, and open-source contributors who collaborate to build scalable machine-learning libraries on the Apache platform.
Mahout follows the principles of the Apache Software Foundation — openness, transparency, community-driven development, and meritocracy.

This page explains the official communication channels, how to participate, and how to contribute to the project.

There are numerous ways to engage with the Mahout community, no matter your background or skill level. Some options include:

Apache Mahout holds a community meeting every two weeks. To get involved, subscribe to the Google Calendar to view and join the meeting.

[Subscribe](https://calendar.google.com/calendar/u/0/r?cid=ZGM4MWY4MTYxYjcyYTRkNGM4ZTVkYjU4MjI5MzYzZWUxMzkxZDllNWU5ZWI1NzUyNzliZTdmN2NhOGQ2ODUzMUBncm91cC5jYWxlbmRhci5nb29nbGUuY29t)

---

There are several ways to engage with the Mahout community:

All official communication for Mahout happens on Apache-managed public mailing lists:

- **User List (questions, installation help, usage discussions):**
  <https://lists.apache.org/list.html?user@mahout.apache.org>
- **Development List (design discussions, patches, roadmap, votes):**
  <https://lists.apache.org/list.html?dev@mahout.apache.org>

To subscribe, send an empty email to:

- `user-subscribe@mahout.apache.org`
- `dev-subscribe@mahout.apache.org`

---

Mahout uses **GitHub Issues and Pull Requests** for development.

- **Source Code:** <https://github.com/apache/mahout>
- **Open Issues:** <https://github.com/apache/mahout/issues>
- **Pull Requests:** <https://github.com/apache/mahout/pulls>

If you find a bug or want to propose a feature:

1. Open a GitHub issue
2. Discuss the design on the **dev mailing list**
3. Submit a Pull Request

---

Contribute to documentation or help update website pages (like this one):

- [https://mahout.apache.org](https://mahout.apache.org/)
- Website source folder: `/website/`

Documentation improvements are always welcome — fixing broken links, updating examples, adding explanations, etc.

---

Apache Mahout follows the ASF standard contribution process:

- Communicate on the mailing list before large changes
- Submit well-tested Pull Requests
- Follow project coding style and review guidelines
- Participate in community discussions and votes
- Respect others — Mahout operates under the ASF Code of Conduct

ASF Code of Conduct:
<https://www.apache.org/foundation/policies/conduct>

---

Mahout is governed by the **Apache Mahout PMC** (Project Management Committee).
The PMC is responsible for project direction, releases, and community oversight.

Contributors who consistently help the project through code, documentation, or community involvement may be invited to become:

- **Committers** — have write access to the repository
- **PMC Members** — participate in project decision-making

Mahout community decisions are made publicly on the **[dev@mahout.apache.org](mailto:dev@mahout.apache.org)** mailing list following ASF voting rules.

---

Thank you for being part of the Apache Mahout community!
Contributions of all kinds — code, documentation, discussion, or feedback — help keep the project healthy and evolving.

---

<a id="community-who-we-are"></a>

<!-- source_url: https://mahout.apache.org/docs/community/who-we-are/ -->

<!-- page_index: 35 -->

# Who we are

Version: latest

Apache Mahout is maintained by a team of volunteer developers.

(Please keep the list below in alphabetical order by first name.)

| Name | Mail | PMC | Comment |
| --- | --- | --- | --- |
| Anand Avati | avati@... | No | @anandavati |
| Andrew Musselman | akm@... | Yes | @akm |
| Andrew Palumbo | apalumbo@... | Yes |  |
| Dan Filimon | dfilimon@... | No |  |
| Dmitriy Lyubimov | dlyubimov@... | No | (Emeritus PMC) |
| Drew Farris | drew@... | No | (Emeritus PMC) |
| Dustin VanStee | vanstee@... | No |  |
| Ellen Friedman | ellenf@... | No | @Ellen\_Friedman |
| Frank Scholten | frankscholten@... | No |  |
| Gokhan Capan | gcapan@... | No |  |
| Grant Ingersoll | gsingers@... | No | (Emeritus PMC) @gsingers |
| Guan-Ming (Wesley) Chiu | guanmingchiu@... | Yes | @guan404ming |
| Holden Karau | holden@... | No |  |
| Isabel Drost-Fromm | isabel@... | Yes |  |
| Jacob Alexander Mannix | jmannix@... | Yes |  |
| Jeff Eastman | jeastman@... | No | (Emeritus PMC) |
| Jie-Kai (Jay) Chang | jiekaichang@... | Yes | @400Ping |
| Krishna Dave | krishnadave829@... | No | @krishnadave |
| Nikolay Sakharnykh | nsakharnykh@... | No |  |
| Paritosh Ranjan | pranjan@... | Yes | @paritoshranjan |
| Pat Ferrel | pat@... | Yes | (Emeritus PMC) @occam |
| Robin Anil | robinanil@... | Yes |  |
| Ryan Huang | hcr@... | No | @ryankert01 |
| Sean Owen | srowen@... | No | (Emeritus PMC) |
| Sebastian Schelter | ssc@... | Yes |  |
| Shannon Quinn | squinn@... | Yes | PMC Chair @[magsol@quinnwitz.house](mailto:magsol@quinnwitz.house) |
| Stevo Slavić | sslavic@... | Yes | @sslavic |
| Suneel Marthi | smarthi@... | No | (Emeritus PMC) @suneelmarthi |
| Ted Dunning | tdunning@... | Yes |  |
| Tom Pierce | tcp@... | No |  |
| Trevor Grant | rawkintrevo@... | Yes | @rawkintrevo |

- Niranjan Balasubramanian (nbalasub@...)
- Otis Gospodnetic (otis@...)
- David Hall (dlwh@...)
- Erik Hatcher (ehatcher@...)
- Ozgur Yilmazel (oyilmazel@...)
- Dawid Weiss (dweiss@...)
- Karl Wettin (kalle@...)
- Abdel Hakim Deneche (adeneche@...)
- Benson Margulies (bimargulies@...)

Note that the email addresses above end with @apache.org.

Apache Mahout contributors and their contributions to individual issues can be found at Apache [JIRA](http://issues.apache.org/jira/browse/MAHOUT).

---

<a id="community-mailing-lists"></a>

<!-- source_url: https://mahout.apache.org/docs/community/mailing-lists/ -->

<!-- page_index: 36 -->

# Mailing Lists, IRC and Archives

Version: latest

Communication at Mahout happens primarily online via mailing lists. We have
a user as well as a dev list for discussion. In addition, there is a commit
list so we are able to monitor what happens in the GitHub repository.

Follow the links below, or send mail manually, with empty subject and body.
The pattern for subscribing and unsubscribing to mailing lists at the ASF is
`<list-name>-<action>@<project>.apache.org`.

This list is for users of Mahout to ask questions, share knowledge, and
discuss issues. Do send mail to this list with usage and configuration
questions and problems. Also, please send questions to this list to verify
your problem before filing issues on GitHub.

- [Subscribe](mailto:user-subscribe@mahout.apache.org)
- [Unsubscribe](mailto:user-unsubscribe@mahout.apache.org)

This is the list where participating developers of the Mahout project meet
and discuss issues concerning Mahout internals, code changes/additions, etc. Do not send mail to this list with usage questions or configuration
questions and problems.

**Discussion list:**

- [Subscribe](mailto:dev-subscribe@mahout.apache.org)
- [Unsubscribe](mailto:dev-unsubscribe@mahout.apache.org)

**Commit notifications:**

- [Subscribe](mailto:commits-subscribe@mahout.apache.org)
- [Unsubscribe](mailto:commits-unsubscribe@mahout.apache.org)

Most discussions now happen on the mailing lists and via GitHub issues and
discussions. It is a logged channel. Please keep in mind that it is for
discussion purposes only and that (pseudo)decisions should be brought back
to the dev@ mailing list or GitHub issues and discussions, and other people
who are not on Slack should be given time to respond before any work is
committed.

Mahout's IRC channel is **#mahout**. Note that real-time project discussions
primarily take place on Slack now (see the Slack section above).

- <https://mail-archives.apache.org/mod_mbox/mahout-dev/>
- <https://mail-archives.apache.org/mod_mbox/mahout-user/>

Please note the inclusion of a link to an archive does not imply an
endorsement of that company by any of the committers of Mahout, the Lucene
PMC, or the Apache Software Foundation. Each archive owner is solely
responsible for the contents and availability of their archive.

---

<a id="community-code-of-conduct"></a>

<!-- source_url: https://mahout.apache.org/docs/community/code-of-conduct/ -->

<!-- page_index: 37 -->

# Apache Mahout Community Code of Conduct

Version: latest

The Apache Mahout community is committed to providing a welcoming, inclusive, and supportive environment for everyone, regardless of their background, identity, or level of expertise. This Code of Conduct outlines our expectations for community members' behavior and serves as a guide for maintaining a positive, respectful, and collaborative community.

We pledge to create a safe and positive environment for all community members, including users, contributors, committers, and maintainers. We encourage open collaboration, constructive feedback, and the free exchange of ideas, while fostering an atmosphere of respect, kindness, and mutual support.

Examples of behavior that contributes to a positive community environment include:

- Demonstrating empathy and kindness toward others
- Being respectful of differing opinions, perspectives, and experiences
- Giving and gracefully accepting constructive feedback
- Accepting responsibility for our actions and apologizing when needed
- Focusing on what is best for the community and the project

Examples of unacceptable behavior include:

- Harassment, intimidation, or discrimination of any kind
- Offensive comments related to gender, gender identity, sexual orientation, race, ethnicity, religion, disability, or physical appearance
- Inappropriate use of sexualized language or imagery
- Personal attacks, insults, or derogatory remarks
- Trolling, sustained disruption of discussions, or deliberate intimidation
- Public or private harassment
- Other conduct that is inappropriate or unprofessional in a community setting

Maintainers and community leaders are responsible for clarifying and enforcing the standards of acceptable behavior and may take appropriate and fair corrective action in response to any instances of unacceptable behavior.

If a community member engages in unacceptable behavior, maintainers and community leaders may take any action they deem appropriate, up to and including temporary bans or permanent expulsion from the community without warning.

If you are subject to or witness any violations of this Code of Conduct, please contact the project maintainers or raise the issue on the community mailing list. All complaints will be reviewed and investigated promptly and fairly.

This Code of Conduct applies within all community spaces, including online forums, mailing lists, chat rooms, issue trackers, and any other public spaces where community members interact. It also applies to private communication when the parties involved are members of the Apache Mahout community.

This Code of Conduct is adapted from the [Contributor Covenant](https://www.contributor-covenant.org/), version 2.0, available at <https://www.contributor-covenant.org/version/2/0/code_of_conduct.html>.

---

<a id="about-how-to-contribute"></a>

<!-- source_url: https://mahout.apache.org/docs/about/how-to-contribute/ -->

<!-- page_index: 38 -->

# How to contribute

Version: latest

*Contributing to an Apache project* is about more than just writing code --
it's about doing what you can to make the project better. There are lots
of ways to contribute!

Discussions at Apache happen on the mailing list. To get involved, you should join the [Mahout mailing lists](#community-mailing-lists). In particular:

- The **user list** (to help others)
- The **development list** (to join discussions of changes) -- This is the best place
  to understand where the project is headed.
- The **commit list** (to see changes as they are made)

Please keep discussions about Mahout on list so that everyone benefits.
Emailing individual committers with questions about specific Mahout issues
is discouraged. See <https://www.apache.org/theapacheway/>
. Apache has a number of [email tips for contributors](http://www.apache.org/dev/contrib-email-tips) as well.

What do you like to work on? There are a ton of things in Mahout that we
would love to have contributions for: documentation, performance improvements, better tests, etc.
The best place to start is by looking into our [issue tracker](https://github.com/apache/mahout/issues) and
seeing what bugs have been reported and seeing if any look like you could
take them on. Small, well written, well tested patches are a great way to
get your feet wet. It could be something as simple as fixing a typo. The
more important piece is you are showing you understand the necessary steps
for making changes to the code. Mahout is a pretty big beast at this
point, so changes, especially from non-committers, need to be evolutionary
not revolutionary since it is often very difficult to evaluate the merits
of a very large patch. Think small, at least to start!

Beyond GitHub Issues, hang out on the dev@ mailing list. That's where we discuss
what we are working on in the internals and where you can get a sense of
where people are working.

Also, documentation is a great way to familiarize yourself with the code
and is always a welcome addition to the codebase and this website. Feel free
to contribute texts and tutorials! Committers will make sure they are added
to this website.

If you are interested in working towards being a committer, general guidelines are available in the [Apache Community documentation](https://community.apache.org/contributors/).

This section identifies the ''optimal'' steps community member can take to
submit a changes or additions to the Mahout code base. This can be new
features, bug fixes optimizations of existing features, or tests of
existing code to prove it works as advertised (and to make it more robust
against possible future changes).

Please note that these are the "optimal" steps, and community members that
don't have the time or resources to do everything outlined on this below
should not be discouraged from submitting their ideas "as is" per "Yonik
Seeley's (Solr committer) Law of Patches":

*A half-baked patch in GitHub Issues, with no documentation, no tests and no backwards compatibility is better than no patch at all.*

Just because you may not have the time to write unit tests, or cleanup
backwards compatibility issues, or add documentation, doesn't mean other
people don't. Putting your patch out there allows other people to try it
and possibly improve it.

First of all, you need to get the Mahout source code from [GitHub](https://github.com/apache/mahout). Most development is done on the "main" branch. The first step to making a contribution is to fork Mahout's main branch to your GitHub repository.

Before you start, you should send a message to the [Mahout developer mailing list](#community-mailing-lists)
(note: you have to subscribe before you can post), or file a ticket in our [issue tracker](https://github.com/apache/mahout/issues).
Describe your proposed changes and check that they fit in with what others are doing and have planned for the project. Be patient, it may take folks a while to understand your requirements.

1. Create a GitHub Issue in the [issue tracker](https://github.com/apache/mahout/issues) (if one does not already exist)
2. Pull the code from your GitHub repository
3. Ensure that you are working with the latest code from the [apache/mahout](https://github.com/apache/mahout) main branch.
4. Modify the source code and add some (very) nice features.
   - Be sure to adhere to the following points:
     - All public classes and methods should have informative Javadoc
       comments.
     - Code should be formatted according to standard
       [Java coding conventions](http://www.oracle.com/technetwork/java/codeconventions-150003.pdf),
       with two exceptions:
       - indent two spaces per level, not four.
       - lines can be 120 characters, not 80.
     - Contributions should pass existing unit tests.
     - New unit tests should be provided to demonstrate bugs and fixes.
5. Commit the changes to your local repository.
6. Push the code back up to your GitHub repository.
7. Create a [Pull Request](https://help.github.com/articles/creating-a-pull-request) to the apache/mahout repository on GitHub.
   - Reference the related GitHub Issue in your pull request (for example, by including `Closes #xxxx` in the pull request description).
8. Committers and other members of the Mahout community can then comment on the Pull Request. Be sure to watch for comments, respond and make any necessary changes.

Please be patient. Committers are busy people too. If no one responds to your Pull Request after a few days, please make friendly reminders on the mailing list. Please
incorporate other's suggestions into into your changes if you think they're reasonable. Finally, remember that even changes that are not committed are useful to the community.

Please make sure that all unit tests succeed before creating your Pull Request.

Run *mvn clean test*, if you see *BUILD SUCCESSFUL* after the tests have finished, all is ok, but if you see *BUILD FAILED*, please carefully read the errors messages and check your code.

Please do not:

- reformat code unrelated to the bug being fixed: formatting changes should
  be done in separate issues.
- comment out code that is now obsolete: just remove it.
- insert comments around each change, marking the change: folks can use
  subversion to figure out what's changed and by whom.
- make things public which are not required by end users.

Please do:

- try to adhere to the coding style of files you edit;
- comment code whose function or rationale is not obvious;
- update documentation (e.g., ''package.html'' files, the website, etc.)

If there's a GitHub issue that already has a Pull Request with changes that you think are really good, and works well for you -- please add a comment saying so. If there's room
for improvement (more tests, better javadocs, etc...) then make the changes on your GitHub branch and add a comment about them. If a lot of people review a Pull Request and give it a
thumbs up, that's a good sign for committers when deciding if it's worth spending time to review it -- and if other people have already put in
effort to improve the docs/tests for an issue, that helps even more.

For more information see the [PR policy and review guidelines](https://github.com/apache/mahout/blob/main/docs/community/pr-policy-and-review-guidelines.md).

---
