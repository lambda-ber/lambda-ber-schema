---
marp: true
theme: default
class: lead
paginate: true
backgroundColor: #fff
---

# Lambda BER Schema

Organizing Structural Biology Data

---

## The Challenge

Structural biologists use many different techniques:

- **Cryo-EM** - Freezing and imaging proteins
- **X-ray Crystallography** - Analyzing protein crystals
- **SAXS/WAXS** - X-ray scattering experiments
- **SANS** - Neutron scattering experiments

Each technique generates different data formats and uses different tools.

---

## The Solution

**lambda-ber-schema** provides a common way to describe data from all these techniques.

Think of it as a shared vocabulary for structural biology experiments.

---

## What It Captures

From sample to final structure, we track:

- **Samples**: What you're studying (proteins, complexes, etc.)
- **Preparation**: How you prepared it
- **Instruments**: What equipment you used
- **Experiments**: How you collected data
- **Processing**: How you analyzed the data
- **Results**: Images and files produced

---

## Why This Matters

**Better organization** → Find your data easily

**Better collaboration** → Share data with colleagues

**Better reproducibility** → Others can understand and repeat your work

**Better integration** → Combine results from different techniques

---

## Example: A Cryo-EM Study

1. Start with a protein sample (TFIID complex)
2. Prepare it on a cryo-EM grid
3. Collect images on a Titan Krios microscope
4. Process the data to get a 3D structure
5. All steps are documented in a standard format

---

## What Makes It Unique

- **Multi-technique**: Works across all major structural biology methods
- **Complete workflow**: Captures the entire experimental pipeline
- **Standardized**: Uses consistent terms and formats
- **Flexible**: Adapts to different experimental designs

---

## Data Organization

```
Study
  ├── Sample information
  ├── How it was prepared
  ├── Instruments used
  ├── Experiments performed
  ├── Data processing workflows
  └── Output files and images
```

Everything in one place, consistently described.

---

## Real-World Example

Berkeley Lab studying TFIID protein complex:

- Sample: TFIID in buffer solution
- Technique: Cryo-electron microscopy
- Instrument: Titan Krios microscope
- Output: 3D reconstruction of the complex

All metadata captured in a structured, searchable format.

---

## Use Cases

**Data Repositories**: Submit data to archives

**Lab Notebooks**: Document your experiments

**Collaborative Projects**: Share data within teams

**Integrative Studies**: Combine multiple techniques

---

## Benefits for Researchers

- Spend less time organizing data
- Make your work more discoverable
- Enable better collaboration
- Facilitate data reuse
- Support reproducible science

---

## Project Resources

- **GitHub Repository**: Complete schema and examples
- **Documentation**: Guides and specifications
- **Examples**: Real-world datasets
- **Community**: Open for contributions

---

## Future Directions

- Support for more imaging techniques
- Integration with major data repositories
- Enhanced quality metrics
- Community-driven improvements

---

## Get Involved

We welcome:
- Feedback from the community
- Example datasets
- Feature requests
- Contributions

See our GitHub repository for more details.

---

## Questions?

**lambda-ber-schema**: Making structural biology data easier to manage and share

Thank you!
