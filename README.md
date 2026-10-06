# Confidential Hopper

> Send private data from your laptop to a cloud GPU for AI analysis—without exposing the data to the cloud provider.

**Confidential Hopper** is an early-stage project exploring privacy-preserving AI workloads on untrusted cloud GPU infrastructure. The goal is to let users run computationally intensive analysis remotely while keeping their sensitive inputs protected from the infrastructure provider.

## Why this exists

Cloud GPUs make advanced AI workloads accessible, but sending sensitive files to a third-party provider creates privacy and compliance concerns. Confidential Hopper is intended to address that problem by separating:

- **The data owner** — the person or organization with private data.
- **The compute provider** — the party supplying GPU capacity.
- **The analysis workload** — the model or process that needs access to the data.

The project aims to ensure that the compute provider can execute the workload without being able to inspect the user's plaintext data.

## Conceptual workflow

```text
┌──────────────┐       protected workload       ┌──────────────────┐
│ Your laptop  │ ─────────────────────────────▶ │ Cloud GPU        │
│              │                                │                  │
│ Private data │ ◀────────── result ─────────── │ AI analysis       │
└──────────────┘                                └──────────────────┘
                                                        │
                                                        │ should not
                                                        ▼
                                                  Cloud provider
                                                  cannot read data
```

A complete implementation is expected to combine hardware-backed confidential computing, secure key exchange, authenticated workloads, and encrypted transport. The exact design is still being developed.

## Project status

This repository is currently at the beginning of development. Interfaces, protocols, and implementation details may change substantially.

## Goals

- Make private AI analysis practical on rented cloud GPUs.
- Minimize the trust required in the cloud infrastructure provider.
- Provide a simple workflow from a local machine to remote GPU compute.
- Make security assumptions and limitations explicit.
- Support reproducible, auditable workloads.

## Non-goals

- Claiming that encryption alone protects data while it is being processed.
- Treating an unverified remote workload as trustworthy.
- Hiding results from the person who owns the data.
- Providing production security guarantees before the design and implementation have been independently reviewed.

## Security model

The project is designed around the assumption that the cloud provider may be able to control or inspect parts of the hosting environment. A useful design must therefore consider:

- Protection of data **in transit**, **at rest**, and **during computation**.
- Verification that the expected software is running before releasing secrets.
- Key management and revocation.
- Malicious or compromised workloads.
- Side-channel and metadata leakage.
- Denial of service and incorrect results.
- What information may be revealed by outputs, timing, or resource usage.

These concerns are part of the design work, not solved claims of the current repository.

## Planned areas of work

- [ ] Define the threat model and security goals.
- [ ] Choose and document the confidential-computing platform.
- [ ] Design remote attestation and key-release flows.
- [ ] Build a minimal local client and cloud worker.
- [ ] Add workload packaging and reproducibility checks.
- [ ] Define result integrity and output-handling guarantees.
- [ ] Add security tests and documentation.
- [ ] Arrange an independent security review before production use.

## Getting started

Implementation and setup instructions will be added as the project develops.

For now, this repository is primarily a place to document the design and track implementation work. Do not upload sensitive data or rely on this project for confidentiality until a complete implementation, documented security model, and independent review are available.

## Contributing

Ideas, design critiques, threat-model feedback, and prototype implementations are welcome. When contributing, please:

1. Explain the security or usability problem being addressed.
2. State which trust assumptions the change relies on.
3. Document new attack surfaces or information leakage.
4. Include tests or a reproducible demonstration where practical.
5. Avoid presenting experimental behavior as a security guarantee.

## License

No license has been selected yet. Until a license is added to this repository, all rights are reserved.
