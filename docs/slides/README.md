# Presentation Slides

This directory contains presentation slides and standalone HTML decks demonstrating lambda-ber-schema capabilities and use cases.

## Available Presentations

### lambda-ro-crate-vision.html

**Title**: LAMBDA RO-Crates: A Federation Contract for Structural Biology Data

**Description**: Vision deck outlining how LAMBDA can use RO-Crate as a cross-facility semantic contract while preserving facility storage autonomy. It frames `lambda-ber-schema` as a structured relational/domain projection, recommends a small technique-neutral LAMBDA Core profile, and proposes macromolecular crystallography (MX) as the first technique extension.

**Primary Artifact**: [`lambda-ro-crate-vision.html`](lambda-ro-crate-vision.html) is a hand-authored standalone HTML deck with inline SVG figures. Publish this file through MkDocs; any PDF/PPTX exports should be regenerated from the HTML deck if needed.

**Topics Covered**:
- RO-Crate background and bioimaging precedent
- RO-Crate as the canonical graph contract
- LAMBDA Core, Federation Crate, and Canonical Projection layers
- Relationship between RO-Crate and `lambda-ber-schema`
- Concrete RO-Crate JSON-LD examples for MX data and workflow provenance
- Schema-slot overlays showing how JSON-LD fields project to LinkML classes and slots
- Sample metadata crates and sample-only metadata handoff
- Profile strategy: core profile plus technique extensions where needed
- MX profile as an initial pilot
- Facility-to-BRIDGE/lakehouse ingest and retrieval use case
- Workflow provenance, file integrity, validation, and projection targets

**Target Audience**: LAMBDA collaborators, facility data architects, beamline scientists, metadata modelers, and pipeline developers

**Duration**: ~40-50 minutes with discussion

### 9B7F-example.md

**Title**: S-SAD Structure of Lysozyme: NSLS2-BER-LAMBDA Integration (PDB 9B7F)

**Description**: Comprehensive presentation demonstrating the complete crystallographic workflow for hen egg white lysozyme structure determination using sulfur-SAD phasing. Shows how lambda-ber-schema captures all metadata from crystallization through structure deposition.

**Topics Covered**:
- S-SAD phasing methodology
- Lossless compression of diffraction data
- Complete NSLS-II FMX beamline workflow
- NSLS2-BER-LAMBDA metadata integration
- lambda-ber-schema validation and benefits
- FAIR data principles in structural biology

**Target Audience**: Structural biologists, beamline scientists, database curators, computational scientists

**Duration**: ~45 minutes with Q&A

## Viewing the Slides

### Standalone HTML

The RO-Crate vision deck is designed directly in HTML:
```bash
open lambda-ro-crate-vision.html
```

Use arrow keys, Page Up/Page Down, Home/End, or scrolling to navigate.

### Using Marp

Install [Marp CLI](https://github.com/marp-team/marp-cli):
```bash
npm install -g @marp-team/marp-cli
```

**View as HTML**:
```bash
marp 9B7F-example.md -o 9B7F-example.html
open 9B7F-example.html
```

**Generate PDF**:
```bash
marp 9B7F-example.md --pdf -o 9B7F-example.pdf
```

**Present with live reload**:
```bash
marp -w -s 9B7F-example.md
```

### Using Pandoc + reveal.js

```bash
pandoc 9B7F-example.md -t revealjs -s -o 9B7F-example-reveal.html
```

### Using remark.js

Create an HTML file:
```html
<!DOCTYPE html>
<html>
<head>
  <link rel="stylesheet" href="https://remarkjs.com/downloads/remark-latest.min.js">
</head>
<body>
  <textarea id="source">
    <!-- Paste slide content here -->
  </textarea>
  <script src="https://remarkjs.com/downloads/remark-latest.min.js">
  </script>
  <script>
    var slideshow = remark.create();
  </script>
</body>
</html>
```

### As Plain Markdown

The slides are written in standard Markdown and can be viewed in any Markdown viewer. Slides are separated by `---`.

## Customizing Slides

### Marp Themes

Add to the front matter:
```yaml
---
marp: true
theme: default  # or gaia, uncover
size: 16:9
paginate: true
---
```

### Custom CSS

Add a `<style>` block at the beginning:
```css
<style>
section {
  background-color: #f0f0f0;
}
h1 {
  color: #2c3e50;
}
</style>
```

## Creating New Presentations

When adding new presentation slides:

1. **Use descriptive filenames**: `topic-description.md`
2. **Include YAML front matter** with title, author, date
3. **Add to this README** with description and topics
4. **Keep slides concise**: ~20-30 slides, 1-2 minutes per slide
5. **Include examples**: Code snippets, data samples
6. **End with resources**: Links, references, contacts

## Contributing

To contribute new presentations:

1. Create markdown file in `docs/slides/`
2. Follow the structure of existing presentations
3. Test with multiple viewers (Marp, reveal.js)
4. Update this README
5. Submit pull request

## Resources

- **Marp**: https://marp.app/
- **reveal.js**: https://revealjs.com/
- **remark.js**: https://remarkjs.com/
- **Pandoc**: https://pandoc.org/

## License

Slides are distributed under the same license as the lambda-ber-schema project.
