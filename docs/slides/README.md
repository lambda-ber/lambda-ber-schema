# Presentation Slides

This directory contains presentation slides in Markdown format demonstrating lambda-ber-schema capabilities and use cases.

## Available Presentations

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

### Using Marp (Recommended)

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
