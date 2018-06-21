## Snips-Wikipeda

A skill for the [Snips voice platform](http://snips.ai) to get the information from Wikipedia.

#### Limitations

Snips ASR is not able to capture arbitrary slot values. When using Snips ASR all searchable items must be
pre-defined. This is almost impossible for systems like Wikipedia. This may work in theory with injection,
but that means loading many thousands of terms (searchable items) into the skill.

## Installation

```
sam install skills --git https://gitlab.smb-tec.com/snips.ai/skills/snips-wikipedia.git
```

## Usage

### CrystalMethod:searchWikipedia

* *"Sag mir, was man unter __Gewitter__ versteht."*
* *"Wer war __Thomas Mann__?"*
* *"Wann spricht man von __Extremismus__?"*
* *"Sage mir die Definition von __Intelligenz__."*